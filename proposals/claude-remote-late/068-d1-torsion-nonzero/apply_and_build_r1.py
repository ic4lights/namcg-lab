"""
Apply the 068 r1 insertion to a COPY of the manuscript outside the repository and
(with --build) build it there.  Never writes into the repository.

  python -I apply_and_build_r1.py            # simulate, print hashes, labels, citations
  python -I apply_and_build_r1.py --build    # also build in a temporary copy

Anchor: the unique line
  \\paragraph{The locked frame as a gauge-invariant composite (conditional; not closure).}
of chapters/appH-microscopic-proofs.tex; the block (CRLF) plus one blank CRLF line is
inserted immediately before it, i.e. directly after the paragraph 'First-order equivariant
class on a compact toy: equivariant lifts and finite-N truncations'.
"""
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parents[1]
appH = root / "chapters" / "appH-microscopic-proofs.tex"
PRE = "8d1eb5dccd6c808feb0bfbc935b5d5d0444dbfd8a46ac9c56c56519d07cfd41e"
POST = "08bc659e6f37446c700d2ef9757aca76dfe96ae84688d40e0d5b756e4791b543"
ANCHOR = b"\\paragraph{The locked frame as a gauge-invariant composite (conditional; not closure).}"
NEWKEYS = ("NielsenOlesen1978",)


def sha(b):
    return hashlib.sha256(b).hexdigest()


src = appH.read_bytes()
blk = (here / "appH_insert_r1.tex").read_bytes()
assert not blk.startswith(b"\xef\xbb\xbf"), "BOM"
assert blk.count(b"\n") == blk.count(b"\r\n") and blk.endswith(b"\r\n"), "block must be CRLF"
print("appH pre  sha256", sha(src), "bytes", len(src))
print("pre-hash matches expected:", sha(src) == PRE)
assert sha(src) == PRE, "appH changed since the proposal was written: re-anchor"
assert src.count(ANCHOR) == 1, "anchor not unique"
off = src.index(ANCHOR)
assert src[off - 4:off] == b"\r\n\r\n", "anchor not preceded by a blank line"
new = src[:off] + blk + b"\r\n" + src[off:]
print("block bytes", len(blk), "sha256", sha(blk))
print("anchor offset", off, "line", src[:off].count(b"\n") + 1)
print("appH post sha256", sha(new), "bytes", len(new), "bare LF", new.count(b"\n") - new.count(b"\r\n"))
assert len(new) == len(src) + len(blk) + 2 and new.count(ANCHOR) == 1
if POST:
    assert sha(new) == POST, "post hash mismatch"

txt = blk.decode("utf-8")
alltex = "".join(p.read_text(encoding="utf-8", errors="replace") for p in (root / "chapters").glob("*.tex"))
for lab in sorted(set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", txt))):
    print("label", lab, "defined", alltex.count("\\label{%s}" % lab))
for lab in re.findall(r"\\label\{([^}]+)\}", txt):
    print("new label", lab, "already defined", alltex.count("\\label{%s}" % lab))
bib = (root / "bib" / "namcg.bib").read_text(encoding="utf-8", errors="replace")
add = (here / "bib-additions-r1.bib").read_text(encoding="utf-8")
for k in sorted(set(sum((x.split(",") for x in re.findall(r"\\cite\{([^}]+)\}", txt)), []))):
    print("cite", k, "in bib", bib.count("{%s," % k), "in additions", add.count("{%s," % k))

if "--build" in sys.argv:
    tmp = Path(tempfile.mkdtemp(prefix="namcg068_"))
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
            print(s[0], "rc", p.returncode, ("pages " + m.group(1)) if m else "")
            if p.returncode != 0 and s[0] == "pdflatex":
                print("\n".join(line for line in p.stdout.splitlines() if line.startswith("!"))[:2000])
                break
        log = (tmp / "namcg-book7.log").read_text(errors="replace")
        bad = [line for line in log.splitlines() if re.search(
            r"undefined references|Reference `.*' on page .* undefined|Citation `.*' on page .* undefined|multiply[- ]defined|There were undefined", line)]
        print("undefined/multiply-defined warnings:", len(bad))
        for line in bad[:20]:
            print("  ", line)
        blg = (tmp / "namcg-book7.blg").read_text(errors="replace") if (tmp / "namcg-book7.blg").exists() else ""
        print("bibtex warnings for new keys:", [line for line in blg.splitlines() if any(k in line for k in NEWKEYS)])
        print("BUILD", "CLEAN" if not bad else "PROBLEMS")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("temp copy removed:", not tmp.exists())
