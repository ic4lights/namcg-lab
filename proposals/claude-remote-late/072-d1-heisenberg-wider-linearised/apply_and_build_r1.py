"""
Apply the 072 r1 change to a COPY of the manuscript outside the repository and
(with --build) build it there.  Never writes into the repository.

  python -I -B apply_and_build_r1.py            # simulate, print hashes, labels
  python -I -B apply_and_build_r1.py --build    # also build in a temporary copy

Edit 1: the block appH_insert_r1.tex (CRLF) plus one blank CRLF line is inserted immediately before the
unique line '\\section{Problem E: signature}', i.e. directly after the closing paragraph of 'First-order
equivariant class on left-invariant backgrounds with curvature and torsion: exact solutions and the
linearised equations' (integrated 071).
Edit 2 (stale passage in that closing paragraph): the unique string
  'Family (ii), its extension with \\(\\chi\\neq0\\) and the survey solutions with ..., for which no scaling
   symmetry is shown, are not linearised here, and'
becomes
  'Family (ii) and its extension with \\(\\chi\\neq0\\) are linearised in the following paragraph; the survey
   solutions with ..., for which no scaling symmetry is shown, are not linearised here, and'.
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
PRE = "b98a3a34d2ac71800ceae7369db90d373d8bcdc139fe7fb81e7bad3e552df1c0"
POST = "ae6c95cdb240188807e403fc23ed5240a7cf8fdfef853ba3be6830974f844fa3"
ANCHOR = b"\\section{Problem E: signature}"
PREV_START = (b"These statements are for Equation~\\eqref{eq:Smatrix} with \\(C_{\\mu\\nu\\lambda}=0\\) and no "
              b"matter term, tree level, the Lorentzian contraction, left-invariant backgrounds with constant connection")
S_OLD = (b"Family (ii), its extension with \\(\\chi\\neq0\\) and the survey solutions with "
         b"\\(\\mathsf R_{abcd}\\mathsf R^{abcd}\\neq0\\), for which no scaling symmetry is shown, are not linearised here, and")
S_NEW = (b"Family (ii) and its extension with \\(\\chi\\neq0\\) are linearised in the following paragraph; the survey solutions with "
         b"\\(\\mathsf R_{abcd}\\mathsf R^{abcd}\\neq0\\), for which no scaling symmetry is shown, are not linearised here, and")


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
assert prev.startswith(PREV_START), "insert would not follow the 071 closing paragraph"
print("anchor unique: True; offset", off, "line", src[:off].count(b"\n") + 1)
print("paragraph before the insert ends:", prev[-62:].decode())
assert src.count(S_OLD) == 1, "stale-passage anchor not unique"
soff = src.index(S_OLD)
assert off - 4 - len(prev) <= soff < off, "stale passage not in the 071 closing paragraph"
print("stale-passage anchor unique: True; line", src[:soff].count(b"\n") + 1)
new = src[:off] + blk + b"\r\n" + src[off:]
new = new.replace(S_OLD, S_NEW)
assert new.count(S_NEW) == 1 and new.count(S_OLD) == 0
print("block bytes", len(blk), "sha256", sha(blk))
print("appH post sha256", sha(new), "bytes", len(new), "bare LF", new.count(b"\n") - new.count(b"\r\n"))
assert len(new) == len(src) + len(blk) + 2 + len(S_NEW) - len(S_OLD) and new.count(ANCHOR) == 1
if POST != "__POST__":
    assert sha(new) == POST, "post hash mismatch"
bl = blk.split(b"\r\n")
print("status sentences in block:", blk.count(b"remain open"), "; in last paragraph:", b"remain open" in bl[-2])
assert blk.count(b"remain open") == 1 and b"remain open" in bl[-2]
print("block ends:", bl[-2][-62:].decode())
noff = new.index(ANCHOR)
print("line after the insert:", new[noff:noff + len(ANCHOR)].decode(), "; preceded by blank line:", new[noff - 4:noff] == b"\r\n\r\n")

txt = blk.decode("utf-8")
alltex = "".join(p.read_text(encoding="utf-8", errors="replace") for p in (root / "chapters").glob("*.tex"))
for lab in sorted(set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", txt))):
    print("label", lab, "defined", alltex.count("\\label{%s}" % lab))
for lab in re.findall(r"\\label\{([^}]+)\}", txt):
    print("new label", lab, "already defined", alltex.count("\\label{%s}" % lab))
print("citations in block:", re.findall(r"\\cite\{([^}]+)\}", txt))

if "--build" in sys.argv:
    tmp = Path(tempfile.mkdtemp(prefix="namcg072r1_"))
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
