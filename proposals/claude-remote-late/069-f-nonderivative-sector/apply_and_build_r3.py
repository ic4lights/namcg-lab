"""
Apply the 069 r3 changes to a COPY of the manuscript outside the repository and (with --build)
build that copy.  Never writes into the repository.

  python -I apply_and_build_r3.py            # simulate: hashes, anchors, labels, citations, checks
  python -I apply_and_build_r3.py --build    # also build in a temporary copy (pdflatex, bibtex, 2x pdflatex)

Edits (all in chapters/appH-microscopic-proofs.tex, paragraph 'Conjugate-coordinate class times a fuzzy
factor: response of the scale of K to the frame, ...', sec:status-F):
  E1-E4, E6, E8, E9  in-place qualifiers of the false or unscoped sentences (E5 of r2 withdrawn) (exact old -> new byte strings below;
         each old string occurs exactly once in the pre-image and lies inside that paragraph);
  E7     the block appH_insert_r3.tex (LF in the proposal folder, converted to CRLF), inserted
         immediately before the unique line '\\section{Problem G: HBEV}', i.e. after the scope
         sentence of that paragraph and its blank line.
"""
import hashlib, re, shutil, subprocess, sys, tempfile
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parents[1]
appH = root / "chapters" / "appH-microscopic-proofs.tex"
PRE = "6a72a3268302d46b9b5d3ede69f8b15e838a0a3c14bfddc2e1b4e8ab58b39a7c"
POST = "a7f1492a30c89b52e9ecadcd2550aaab89261796c35266b19bfed0d5b354e842"
ANCHOR = b"\\section{Problem G: HBEV}"
PARA = b"\\paragraph{Conjugate-coordinate class times a fuzzy factor: response of the scale of \\(K\\) to the frame"
NEWKEYS = ("IsoKimuraTanakaWakatsuki2001",)

EDITS = [
    ("E1 cubic/mass beta_K forms (pre L2966)",
     rb"with \(\partial Y/\partial\ln\chi\) neglected in these three forms.",
     rb"with \(\partial Y/\partial\ln\chi\) neglected in these three forms; in the second and third, \(U_4\), \(U_2\) and \(Y\) are those of the operators without the Hessian of the tree cubic or mass term, so these are not the one-loop forms of the action with that term (paragraph on the Hessian of a tree stabiliser on \(K\) below)."),
    ("E2 beta_K = 1 attained in the cubic case (pre L2966)",
     rb"then \(\beta_K=1\) is attained in the cubic case",
     rb"then, in these forms, \(\beta_K=1\) is attained in the cubic case"),
    ("E3 example on S^2_N (pre L2980)",
     rb"With a tree cubic term \(\beta_K=1\) is attained at a local minimum with \(\hat U>0\):",
     rb"With a tree cubic term, and the operators without its Hessian (paragraph on the Hessian of a tree stabiliser on \(K\) below), \(\beta_K=1\) is attained at a local minimum with \(\hat U>0\):"),
    ("E8 V and T scale as chi^2 (pre L3000)",
     rb"\(V\) and \(T\) both scale as \(\chi^2\), so the response of \(\chi\) does not move the condition \(V=T\).",
     rb"For the operators without a tree stabiliser on \(K\), \(V\) and \(T\) both scale as \(\chi^2\), so the response of \(\chi\) does not move the condition \(V=T\)."),
    ("E4 V=T without a tuned K (pre L3000)",
     rb"so \(V=T\) is approached at large \(N\) for this \(K\) and does not need a tuned \(K\);",
     rb"so, for the operators without a tree stabiliser on \(K\), \(V=T\) is approached at large \(N\) for this \(K\) and does not need a tuned \(K\); with the Hessian of a tree cubic term it is not (paragraph on the Hessian of a tree stabiliser on \(K\) below);"),
    ("E9 start of the beta_K = 1 sentence (pre L3002)",
     rb"The value \(\beta_K=1\) needs a tree term of negative slope at the minimum and,",
     rb"In the forms with a tree stabiliser above, which omit its Hessian, the value \(\beta_K=1\) needs a tree term of negative slope at the minimum and,"),
    ("E6 scope sentence (pre L3004)",
     rb"with \(V=T\) where the index part alone enters \(U_2\) and with \(W_R\propto\hat V-\hat T\) neglected;",
     rb"with \(V=T\) where the index part alone enters \(U_2\) and with \(W_R\propto\hat V-\hat T\) neglected; \(U_4\), \(U_2\) and \(Y\) of the operators without the Hessian of a tree stabiliser on \(K\), so that the forms with a tree cubic or mass term are one-loop forms only as its coefficient tends to zero;"),
]
# E5 of r2 is withdrawn: its old string stays unchanged; the scope is carried by E9 at the start of the same sentence.
E5_KEPT = rb"for \(\hat U<0\), where \(q_b^2<0\), it is available at negligible \(Y\)."
E9_SENTENCE = (rb"In the forms with a tree stabiliser above, which omit its Hessian, the value \(\beta_K=1\) needs a tree term of negative slope at the minimum and, for \(\hat U\ge0\), \(Y>4|U_4|+2|U_2|\), which at large \(N\) on \(S^2_N\) is \(\chi^2<(\sqrt{39}-3)\vartheta/4\); "
               + E5_KEPT)


def sha(b):
    return hashlib.sha256(b).hexdigest()


src = appH.read_bytes()
print("appH pre  sha256", sha(src), "bytes", len(src))
print("pre-hash matches expected:", sha(src) == PRE)
assert sha(src) == PRE, "appH changed since the proposal was written: re-anchor"
assert src.count(b"\n") == src.count(b"\r\n") and not src.startswith(b"\xef\xbb\xbf")

p0 = src.index(PARA); p1 = src.index(ANCHOR)
assert src.count(PARA) == 1 and src.count(ANCHOR) == 1 and p0 < p1
print("target paragraph: line", src[:p0].count(b"\n") + 1, "to line", src[:p1].count(b"\n"))

new = src
for name, old, rep in EDITS:
    assert b"\n" not in old and b"\n" not in rep
    n = new.count(old); off = new.find(old)
    line = new[:off].count(b"\n") + 1
    inside = new.index(PARA) < off < new.index(ANCHOR)
    print(f"{name}: occurs {n}x, line {line}, inside target paragraph {inside}")
    assert n == 1 and inside and new.count(rep) == 0
    new = new[:off] + rep + new[off + len(old):]

assert new.count(E5_KEPT) == 1 and new.count(E9_SENTENCE) == 1
assert new.count(b"(next paragraph)") == src.count(b"(next paragraph)")
print("E5 old string kept once; final E9 sentence present once; no new (next paragraph)")
print("final sentence:", E9_SENTENCE.decode())
blk = (here / "appH_insert_r3.tex").read_bytes()
assert b"\r" not in blk and not blk.startswith(b"\xef\xbb\xbf") and all(b < 128 for b in blk)
assert blk.endswith(b".\n\n")
blk_crlf = blk.replace(b"\n", b"\r\n")
off = new.index(ANCHOR)
assert new[off - 4:off] == b"\r\n\r\n"
prev = new[:off - 4].rsplit(b"\r\n", 1)[1]
assert prev.startswith(b"These statements are for the hypotheses of the preceding paragraph, the product background without mixed flux")
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
assert "\\label{" not in txt
bib = (root / "bib" / "namcg.bib").read_text(encoding="utf-8", errors="replace")
add = (here / "new_bib_entry.bib").read_text(encoding="utf-8")
for k in sorted(set(sum((x.split(",") for x in re.findall(r"\\cite\{([^}]+)\}", txt)), []))):
    print("cite", k, "in bib", bib.count("{%s," % k), "in additions", add.count("{%s," % k))
    assert bib.count("{%s," % k) + add.count("{%s," % k) == 1
print("status sentences in insert:", txt.count("PROGRAMME-CONDITIONAL"), "; at the end:", txt.rstrip().endswith("remain open and PROGRAMME-CONDITIONAL."))
assert txt.count("PROGRAMME-CONDITIONAL") == 1 and txt.rstrip().endswith("remain open and PROGRAMME-CONDITIONAL.")
reps = b"".join(r for _, _, r in EDITS).decode()
for t, nm in ((txt, "insert"), (reps, "in-place edits")):
    assert not re.search(r"Status:|CRITICAL PATH|DERIVED|CLOSED|OPEN\b", t), nm
    assert not re.search(r"proposal|gatekeeper|researcher|adversary|review|\bround\b", t), nm
    assert t.count("{") == t.count("}") and t.count("\\(") == t.count("\\)") and t.count("\\[") == t.count("\\]"), nm
    print(nm + ": no label words, no process language, balanced delimiters")
assert not re.search(r"(?<![_a-zA-Z\\])c[=/\\)]|(?<![\\a-zA-Z])\\kappa(?!_)|L'", txt.replace("c_3", "").replace(r"the weight \(\kappa\)", "")), "old symbols left"
print("no bare c, bare kappa or L' left in insert")
print("paragraph blocks in insert:", txt.count("\n\n"))

if "--build" in sys.argv:
    tmp = Path(tempfile.mkdtemp(prefix="namcg069r3_"))
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
