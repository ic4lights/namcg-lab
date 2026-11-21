"""
Apply the 059 local-r3 insertion to a COPY of the manuscript outside the
repository and (with --build) build it there.  Never writes into the repo.

  python -I apply_and_build_local_r2.py            # simulate, print hashes
  python -I apply_and_build_local_r2.py --build    # also build in a temp copy

Anchor: the unique line "\section{Problem E: signature}" of
chapters/appH-microscopic-proofs.tex; the block (CRLF) plus one blank CRLF
line is inserted immediately before it.
"""
import hashlib, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parents[2]
appH = root / "chapters" / "appH-microscopic-proofs.tex"
PRE = "4ea0ee0f50b0676ee161ff8ebd6620e3bd775ae74ffb1796b07d8a78f9e24b18"
POST = "8d1eb5dccd6c808feb0bfbc935b5d5d0444dbfd8a46ac9c56c56519d07cfd41e"
ANCHOR = b"\\section{Problem E: signature}"

def sha(b): return hashlib.sha256(b).hexdigest()

src = appH.read_bytes()
blk_lf = (here / "insertion-block-local-r3.tex").read_bytes()
assert b"\r" not in blk_lf and blk_lf.endswith(b"\n") and not blk_lf.startswith(b"\xef\xbb\xbf")
blk = blk_lf.replace(b"\n", b"\r\n")
print("appH pre  sha256", sha(src), "bytes", len(src), "CRLF", src.count(b"\r\n"),
      "bare LF", src.count(b"\n") - src.count(b"\r\n"))
print("pre-hash matches expected:", sha(src) == PRE)
assert src.count(ANCHOR) == 1, "anchor not unique"
off = src.index(ANCHOR)
assert src[off - 4:off] == b"\r\n\r\n", "anchor not preceded by a blank line"
new = src[:off] + blk + b"\r\n" + src[off:]
print("block LF bytes", len(blk_lf), "sha256", sha(blk_lf))
print("block CRLF bytes", len(blk), "sha256", sha(blk))
print("anchor offset", off)
print("appH post sha256", sha(new), "bytes", len(new), "CRLF", new.count(b"\r\n"),
      "bare LF", new.count(b"\n") - new.count(b"\r\n"))
assert len(new) == len(src) + len(blk) + 2 and new.count(ANCHOR) == 1
print("post-hash matches expected:", sha(new) == POST)
assert sha(new) == POST, "post hash mismatch"

# labels and citations used by the block
txt = blk_lf.decode("utf-8")
labels = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", txt))
alltex = "".join(p.read_text(encoding="utf-8", errors="replace") for p in (root / "chapters").glob("*.tex"))
for l in sorted(labels):
    print("label", l, "defined", alltex.count("\\label{%s}" % l))
bib = (root / "bib" / "namcg.bib").read_text(encoding="utf-8", errors="replace")
add = (here / "bib-additions-local-r2.bib").read_text(encoding="utf-8")
for k in sorted(set(re.findall(r"\\cite\{([^}]+)\}", txt))):
    for kk in k.split(","):
        print("cite", kk, "in bib", bib.count("{%s," % kk), "in additions", add.count("{%s," % kk))

if "--build" in sys.argv:
    tmp = Path(tempfile.mkdtemp(prefix="namcg059_"))
    assert root not in tmp.parents and tmp != root
    try:
        for d in ("chapters", "frontmatter", "bib", "figs"):
            if (root / d).exists():
                shutil.copytree(root / d, tmp / d)
        for f in root.iterdir():
            if f.is_file() and f.suffix.lower() in (".tex", ".sty", ".cls", ".png", ".jpg", ".pdf", ".bst"):
                shutil.copy2(f, tmp / f.name)
        (tmp / "chapters" / "appH-microscopic-proofs.tex").write_bytes(new)
        b = (tmp / "bib" / "namcg.bib").read_bytes()
        sep = b"\r\n" if b.endswith(b"\r\n") else b"\r\n\r\n"
        (tmp / "bib" / "namcg.bib").write_bytes(b + sep + add.replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8"))
        steps = [["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
                 ["bibtex", "namcg-book7"],
                 ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
                 ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"]]
        for s in steps:
            p = subprocess.run(s, cwd=tmp, capture_output=True, text=True, errors="replace", timeout=1200)
            m = re.search(r"Output written on .*?\((\d+) pages", p.stdout)
            print(" ".join(s[:1]), "rc", p.returncode, ("pages " + m.group(1)) if m else "")
            if p.returncode != 0 and s[0] == "pdflatex":
                print("\n".join(l for l in p.stdout.splitlines() if l.startswith("!"))[:2000])
                break
        log = (tmp / "namcg-book7.log").read_text(errors="replace")
        bad = [l for l in log.splitlines() if re.search(
            r"undefined references|Reference `.*' on page .* undefined|Citation `.*' on page .* undefined|multiply[- ]defined|There were undefined", l)]
        print("undefined/multiply-defined warnings:", len(bad))
        for l in bad[:20]:
            print("  ", l)
        blg = (tmp / "namcg-book7.blg").read_text(errors="replace") if (tmp / "namcg-book7.blg").exists() else ""
        print("bibtex warnings for new keys:",
              [l for l in blg.splitlines() if any(k in l for k in ("HattoriSekoTsuchiya2026", "Elitzur1975", "FradkinShenker1979"))])
        print("BUILD", "CLEAN" if not bad else "PROBLEMS")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("temp copy removed:", not tmp.exists())
