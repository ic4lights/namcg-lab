"""
Apply the 076 r2 changes to a COPY of the manuscript outside the repository and (with --build) build
that copy.  Never writes into the repository.

  python -I apply_and_build_r2.py            # hashes, anchors, labels, checks; prints the post hash
  python -I apply_and_build_r2.py --build    # also build in a temporary copy (pdflatex, bibtex, 2x pdflatex)

Edits (chapters/appH-microscopic-proofs.tex, sec:status-F):
  E1  paragraph on the tadpole of the static scalar channel ('Profile and stationarity'): the parenthesis on
      the tree terms in the list of terms that could supply the Yukawa condition;
  E2  paragraph on the tree non-derivative terms ('The singlet sector at q=0'): pointer after the sentence on
      the kinetic matrix of the singlets;
  E3  the block appH_insert_r2.tex (LF in the proposal folder, converted to CRLF), inserted immediately
      before the unique line '\section{Problem G: HBEV}'.
"""
import hashlib, re, shutil, subprocess, sys, tempfile
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parents[1]
appH = root / "chapters" / "appH-microscopic-proofs.tex"
PRE = "8aed4519472ef5ec9b1c8a4668e39b02b0882b5e7edb2cf9a9e0b5ba513ae229"
POST = "2b8f46a62f3b4480152f93801170029b589a08618ec1cf5504b8aea04eb85a4d"
ANCHOR = b"\\section{Problem G: HBEV}"

EDITS = [
    ("E1 Yukawa-condition list (tadpole paragraph)",
     rb"(on two other realisations of this channel the tree terms supply no positive constant; paragraph on the tree non-derivative terms below)",
     rb"(on two other realisations of this channel the tree terms supply no positive constant, and on the singlet sector, for a positive-definite kinetic matrix of the singlets, they supply one only together with a static pole of the tachyonic sign in the neutral singlet; paragraphs on the tree non-derivative terms and on the kinetic matrix of the static scalar singlets below)"),
    ("E2 singlet-sector pointer (tree non-derivative paragraph)",
     rb"and the induced and loop parts of that matrix are not computed.",
     rb"and the induced and loop parts of that matrix are not computed (for its tree part, the recorded coupling and the combination they select see the paragraph on the kinetic matrix of the static scalar singlets below)."),
]
PARAS = {
    "E1": b"\paragraph{Conjugate-coordinate class times a fuzzy factor: the tadpole of the static scalar channel",
    "E2": b"\paragraph{Conjugate-coordinate class times a fuzzy factor: the tree non-derivative terms of the static scalar channel",
}


def sha(b):
    return hashlib.sha256(b).hexdigest()


src = appH.read_bytes()
print("appH pre  sha256", sha(src), "bytes", len(src))
print("pre-hash matches expected:", sha(src) == PRE)
assert sha(src) == PRE, "appH changed since the proposal was written: re-anchor"
assert src.count(b"\n") == src.count(b"\r\n") and not src.startswith(b"\xef\xbb\xbf")
assert src.count(ANCHOR) == 1

new = src
for name, old, rep in EDITS:
    assert b"\n" not in old and b"\n" not in rep
    n = new.count(old); off = new.find(old)
    para = PARAS[name.split()[0]]
    p0 = new.index(para)
    nxt = min(x for x in [m.start() for m in re.finditer(rb"\\paragraph\{|\\section\{", new)] if x > p0)
    inside = p0 < off < nxt
    ln = new[:off].count(b"\n") + 1
    print(f"{name}: occurs {n}x, line {ln}, inside intended paragraph {inside}")
    assert n == 1 and inside and new.count(rep) == 0
    new = new[:off] + rep + new[off + len(old):]

blk = (here / "appH_insert_r2.tex").read_bytes()
assert b"\r" not in blk and not blk.startswith(b"\xef\xbb\xbf") and all(b < 128 for b in blk)
assert blk.endswith(b".\n\n")
blk_crlf = blk.replace(b"\n", b"\r\n")
off = new.index(ANCHOR)
assert new[off - 4:off] == b"\r\n\r\n"
prev = new[:off - 4].rsplit(b"\r\n", 1)[1]
assert prev.startswith(b"These statements are for the Poisson limit on \(M\), tree level, the conjugate-coordinate class")
assert prev.endswith(b"Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.")
new = new[:off] + blk_crlf + new[off:]
print("insert: LF bytes", len(blk), "sha256(LF)", sha(blk), "; inserted at line", new[:off].count(b"\n") + 1)
print("line after the insert:", new[off + len(blk_crlf):off + len(blk_crlf) + len(ANCHOR)].decode())
print("appH post sha256", sha(new), "bytes", len(new), "lines", new.count(b"\n"), "bare LF", new.count(b"\n") - new.count(b"\r\n"))
assert new.count(b"\n") == new.count(b"\r\n") and new.count(ANCHOR) == 1
if POST != "__POST__":
    assert sha(new) == POST, "post hash mismatch"
    print("post-hash matches expected: True")

txt = blk.decode()
alltex = "".join(p.read_text(encoding="utf-8", errors="replace") for p in (root / "chapters").glob("*.tex"))
for lab in sorted(set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", txt))):
    print("label", lab, "defined", alltex.count("\\label{%s}" % lab))
    assert alltex.count("\\label{%s}" % lab) == 1
assert "\\label{" not in txt and "\\cite{" not in txt
print("status sentences in insert:", txt.count("PROGRAMME-CONDITIONAL"), "; at the end:", txt.rstrip().endswith("remain open and PROGRAMME-CONDITIONAL."))
assert txt.count("PROGRAMME-CONDITIONAL") == 1 and txt.rstrip().endswith("remain open and PROGRAMME-CONDITIONAL.")
reps = b"".join(r for _, _, r in EDITS).decode()
for t, nm in ((txt, "insert"), (reps, "in-place edits")):
    assert not re.search(r"Status:|CRITICAL PATH|DERIVED|CLOSED|OPEN\b", t), nm
    assert not re.search(r"proposal|gatekeeper|researcher|adversary|review|\bround\b", t), nm
    assert t.count("{") == t.count("}") and t.count("\\(") == t.count("\\)") and t.count("\\[") == t.count("\\]"), nm
    print(nm + ": no label words, no process language, balanced delimiters")
print("paragraph blocks in insert:", txt.count("\n\n"))

if "--build" in sys.argv:
    tmp = Path(tempfile.mkdtemp(prefix="namcg076r2_"))
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
