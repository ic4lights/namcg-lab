"""
Apply the 071 r1 change to a COPY of the manuscript outside the repository and
(with --build) build it there.  Never writes into the repository.

  python -I apply_and_build_r1.py            # simulate, print hashes, labels
  python -I apply_and_build_r1.py --build    # also build in a temporary copy

Edit: the block appH_insert_r1.tex (CRLF) plus one blank CRLF line is inserted
immediately before the unique line '\\section{Problem E: signature}', i.e. directly
after the paragraph 'First-order equivariant class on left-invariant backgrounds with
torsion: the linearised frame and connection equations' (integrated 068).
No bibliography change.
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
PRE = "d8d8b678fa0ceabe03f3f9c2f56cc60dbe140aa845658beddb0c206ba26c9180"
POST = "a73760f2181d68d04e99915aac756907a2ef753f746e4920d388c37bfc0e13c0"
ANCHOR = b"\\section{Problem E: signature}"
PREV_START = (b"These statements are for Equation~\\eqref{eq:Smatrix} with \\(C_{\\mu\\nu\\lambda}=0\\) and no "
              b"matter term, tree level, linear order in the fluctuation, left-invariant backgrounds with "
              b"vanishing connection")


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
prev = src[:off - 4].rsplit(b"\r\n", 1)[1]
assert prev.startswith(PREV_START), "insert would not follow the 068 paragraph"
print("anchor unique: True; offset", off, "line", src[:off].count(b"\n") + 1)
print("paragraph before the insert ends:", prev[-62:].decode())
new = src[:off] + blk + b"\r\n" + src[off:]
print("block bytes", len(blk), "sha256", sha(blk))
print("appH post sha256", sha(new), "bytes", len(new), "bare LF", new.count(b"\n") - new.count(b"\r\n"))
assert len(new) == len(src) + len(blk) + 2 and new.count(ANCHOR) == 1
if POST != "__POST__":
    assert sha(new) == POST, "post hash mismatch"
bl = blk.split(b"\r\n")
print("status sentences in block:", blk.count(b"remain open"), "; in last paragraph:", b"remain open" in bl[-2])
assert blk.count(b"remain open") == 1 and b"remain open" in bl[-2]
print("block ends:", bl[-2][-62:].decode())
print("line after the insert:", new[off + len(blk) + 2:off + len(blk) + 2 + len(ANCHOR)].decode())

txt = blk.decode("utf-8")
alltex = "".join(p.read_text(encoding="utf-8", errors="replace") for p in (root / "chapters").glob("*.tex"))
for lab in sorted(set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", txt))):
    print("label", lab, "defined", alltex.count("\\label{%s}" % lab))
for lab in re.findall(r"\\label\{([^}]+)\}", txt):
    print("new label", lab, "already defined", alltex.count("\\label{%s}" % lab))
print("citations in block:", re.findall(r"\\cite\{([^}]+)\}", txt))

if "--build" in sys.argv:
    tmp = Path(tempfile.mkdtemp(prefix="namcg071r1_"))
    assert root not in tmp.parents and tmp != root
    try:
        for d in ("chapters", "frontmatter", "bib", "figs"):
            if (root / d).exists():
                shutil.copytree(root / d, tmp / d)
        for f in root.iterdir():
            if f.is_file() and f.suffix.lower() in (".tex", ".sty", ".cls", ".png", ".jpg", ".pdf", ".bst"):
                shutil.copy2(f, tmp / f.name)
        (tmp / "chapters" / "appH-microscopic-proofs.tex").write_bytes(new)
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
        print("BUILD", "CLEAN" if not bad else "PROBLEMS")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("temp copy removed:", not tmp.exists())
