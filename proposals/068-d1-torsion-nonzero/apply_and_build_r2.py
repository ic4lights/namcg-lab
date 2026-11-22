"""
Apply the 068 r2 changes to a COPY of the manuscript outside the repository and
(with --build) build it there.  Never writes into the repository.

  python -I apply_and_build_r2.py            # simulate, print hashes, labels, citations
  python -I apply_and_build_r2.py --build    # also build in a temporary copy

Edit 1 (review-r1 m5): the last sentence of appH line 1581 of the pre-image (paragraph
'First-order equivariant class: one loop about commuting matrices ...'),
  'Whether the remaining modes acquire a mass term of definite sign is not computed.'
(unique in the file), is replaced by the m5 text.
Edit 2 (review-r1 m1): the block appH_insert_r2.tex (CRLF) plus one blank CRLF line is
inserted immediately before the unique line '\\section{Problem E: signature}', i.e.
directly after the paragraph 'The locked frame as a gauge-invariant composite ...'.
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
POST = "6a72a3268302d46b9b5d3ede69f8b15e838a0a3c14bfddc2e1b4e8ab58b39a7c"
ANCHOR = b"\\section{Problem E: signature}"
M5_OLD = b"Whether the remaining modes acquire a mass term of definite sign is not computed."
M5_NEW = (b"Whether the remaining modes acquire a mass term of definite sign is not computed in this part; for "
          b"left-invariant backgrounds with vanishing connection their linearised equations are given in the "
          b"paragraph on left-invariant backgrounds with torsion later in this section.")
NEWKEYS = ("NielsenOlesen1978",)


def sha(b):
    return hashlib.sha256(b).hexdigest()


src = appH.read_bytes()
blk = (here / "appH_insert_r2.tex").read_bytes()
assert not blk.startswith(b"\xef\xbb\xbf"), "BOM"
assert blk.count(b"\n") == blk.count(b"\r\n") and blk.endswith(b"\r\n"), "block must be CRLF"
print("appH pre  sha256", sha(src), "bytes", len(src))
print("pre-hash matches expected:", sha(src) == PRE)
assert sha(src) == PRE, "appH changed since the proposal was written: re-anchor"

# edit 1 (m5)
assert src.count(M5_OLD) == 1, "m5 anchor not unique"
o5 = src.index(M5_OLD)
line5 = src[:o5].count(b"\n") + 1
print("m5 anchor unique: True; offset", o5, "line", line5)
assert line5 == 1581, "m5 anchor moved"
assert src[o5 + len(M5_OLD):o5 + len(M5_OLD) + 2] == b"\r\n", "m5 sentence is not the last of its line"
assert src.count(M5_NEW) == 0
mid = src[:o5] + M5_NEW + src[o5 + len(M5_OLD):]
assert len(mid) == len(src) - len(M5_OLD) + len(M5_NEW) and mid.count(b"\n") == src.count(b"\n")

# edit 2 (m1)
assert mid.count(ANCHOR) == 1, "anchor not unique"
off = mid.index(ANCHOR)
assert mid[off - 4:off] == b"\r\n\r\n", "anchor not preceded by a blank line"
prev = mid[:off - 4].rsplit(b"\r\n", 1)[1]
assert prev.startswith(b"Elitzur's theorem"), "insert would not follow the locked-frame composite paragraph"
print("anchor unique: True; offset", off, "line", mid[:off].count(b"\n") + 1)
print("paragraph before the insert ends:", prev[-62:].decode())
new = mid[:off] + blk + b"\r\n" + mid[off:]
print("block bytes", len(blk), "sha256", sha(blk))
print("appH post sha256", sha(new), "bytes", len(new), "bare LF", new.count(b"\n") - new.count(b"\r\n"))
assert len(new) == len(mid) + len(blk) + 2 and new.count(ANCHOR) == 1
if POST != "__POST__":
    assert sha(new) == POST, "post hash mismatch"

# closers
bl = blk.split(b"\r\n")
print("status sentences in block:", blk.count(b"remain open"),
      "; first block line with a status sentence:", next(i for i, x in enumerate(bl) if b"remain open" in x) + 1,
      "of", len(bl) - 1)
assert blk.count(b"remain open") == 1 and b"remain open" in bl[-2] and b"remain open" not in bl[1]
print("block ends:", bl[-2][-62:].decode())
print("line after the insert:", new[off + len(blk) + 2:off + len(blk) + 2 + len(ANCHOR)].decode())

txt = blk.decode("utf-8")
alltex = "".join(p.read_text(encoding="utf-8", errors="replace") for p in (root / "chapters").glob("*.tex"))
for lab in sorted(set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", txt))):
    print("label", lab, "defined", alltex.count("\\label{%s}" % lab))
for lab in re.findall(r"\\label\{([^}]+)\}", txt):
    print("new label", lab, "already defined", alltex.count("\\label{%s}" % lab))
bib = (root / "bib" / "namcg.bib").read_text(encoding="utf-8", errors="replace")
add = (here / "bib-additions-r2.bib").read_text(encoding="utf-8")
for k in sorted(set(sum((x.split(",") for x in re.findall(r"\\cite\{([^}]+)\}", txt)), []))):
    print("cite", k, "in bib", bib.count("{%s," % k), "in additions", add.count("{%s," % k))

if "--build" in sys.argv:
    tmp = Path(tempfile.mkdtemp(prefix="namcg068r2_"))
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
