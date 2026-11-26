# cert-r118p.py -- compile certificate for insert-potential-selection-r1.tex (proposal 118)
# Modeled on cert-r117r2p.py (117 form). Copy of the working tree (minus .git,
# scratch/, proposals/, reports/, build junk; untracked namcg-book7.bbl
# INCLUDED) into a temp dir OUTSIDE the repository. ONE edit is applied to the
# copy of chapters/appH-microscopic-proofs.tex:
#   the insert (leading CRLF separator + one paragraph line + CRLF) spliced
#   immediately before the unique line "\section{Problem E: signature}"
#   via the canonical join  data.replace(ANCHOR, INS + CRLF + ANCHOR, 1).
# POST size and sha1 (independently pre-computed for the pinned baseline) are
# asserted BEFORE any compile. Two pdflatex passes are run (pass 1 builds .aux,
# pass 2 resolves refs); rc1==rc2==0, zero "! " error lines, "Output written",
# zero undefined references at pass 2, and zero undefined references touching
# the package labels are HARD-ASSERTED before CERT PASS is printed.
# Run:  python -I -B cert-r118p.py     (from the proposal folder)
import os, shutil, subprocess, sys, tempfile, hashlib

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
HERE = os.path.dirname(os.path.abspath(__file__))
INS = os.path.join(HERE, "insert-potential-selection-r1.tex")
SKIP_DIRS = {".git", "scratch", "proposals", "reports"}
SKIP_EXT = {".aux", ".log", ".out", ".toc", ".lof", ".lot", ".fls",
            ".fdb_latexmk", ".synctex.gz"}
ANCHOR = b"\section{Problem E: signature}"
MYREFS = ("eq:V'", "eq:Smatrix'", "eq:vacuum-manifold'", "ass:dictionary'",
          "sec:ch3-relate'", "eq:Phi-eom'")

tmp = tempfile.mkdtemp(prefix="cert118p_")
print("temp:", tmp)
for root, dirs, files in os.walk(REPO):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    rel = os.path.relpath(root, REPO)
    dst = os.path.join(tmp, rel)
    os.makedirs(dst, exist_ok=True)
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in SKIP_EXT:
            continue
        if ext == ".pdf" and rel == ".":
            continue  # skip the tracked root namcg-book7.pdf, keep figs/*.pdf
        shutil.copy2(os.path.join(root, f), os.path.join(dst, f))
bbl = os.path.join(tmp, "namcg-book7.bbl")
assert os.path.isfile(bbl), "namcg-book7.bbl missing in copy"
apph = os.path.join(tmp, "chapters", "appH-microscopic-proofs.tex")
base = open(apph, "rb").read()
print("baseline sha1 %s size %d" % (hashlib.sha1(base).hexdigest(), len(base)))
assert hashlib.sha1(base).hexdigest() == "ce91063fddcaa5599429519f4bc2c478e0d919e8" and len(base) == 839337, "live appH moved off the 118 baseline pin"
assert base.count(ANCHOR) == 1, "anchor not unique: %d" % base.count(ANCHOR)
assert base.find(ANCHOR) == 286080, "anchor byte offset moved: %d" % base.find(ANCHOR)
ins = open(INS, "rb").read()
assert hashlib.sha1(ins).hexdigest() == "bbe4e535dd31c76a82ea89ff1b20980eb979f9bf" and len(ins) == 4024, "payload off pin"
assert ins.startswith(b"\r\n") and ins.endswith(b"\r\n"), "insert must start and end with CRLF"
assert ins.count(b"\n") == 2 and ins.count(b"\r") == 2, "insert must be blank CRLF + one CRLF line"
assert all(b < 128 for b in ins) and b"\t" not in ins, "insert not ASCII/tab-free"
out = base.replace(ANCHOR, ins + b"\r\n" + ANCHOR, 1)
print("POST      sha1 %s size %d (= baseline %d + payload %d + 2 join)"
      % (hashlib.sha1(out).hexdigest(), len(out), len(base), len(ins)))
assert len(out) == 839337 + 4024 + 2, "POST size arithmetic wrong"
assert hashlib.sha1(out).hexdigest() == "c24902b31abafc126a7e59485f2b706d2f2b17d4", "POST sha1 off independently computed pin"
assert len(out) == len(base) + len(ins) + 2, "POST = base + payload + 2 CRLF join"
open(apph, "wb").write(out)
CMDC = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"]
p1 = subprocess.run(CMDC, cwd=tmp, capture_output=True, text=True)   # pass 1
p2 = subprocess.run(CMDC, cwd=tmp, capture_output=True, text=True)   # pass 2
log = open(os.path.join(tmp, "namcg-book7.log"), "r", errors="replace").read()
errs = [l for l in log.splitlines() if l.startswith("! ")]
undef = [l for l in log.splitlines() if "undefined" in l and "There were" not in l]
mine = [l for l in undef if any(k in l for k in MYREFS)]
ok = p1.returncode == 0 and p2.returncode == 0 and not errs and "Output written" in log
print("rc1=%d rc2=%d errlines=%d outw=%s undefrefs_pass2=%d" %
      (p1.returncode, p2.returncode, len(errs), "Output written" in log, len(undef)))
for l in errs[:5]:
    print("ERR:", l)
for l in undef[:10]:
    print("UNDEF:", l)
print("undefrefs-touching-package-labels=%d" % len(mine))
for l in mine[:10]:
    print("PKG-UNDEF:", l)
assert len(undef) == 0, "undefined references remain after pass 2: %d" % len(undef)
assert len(mine) == 0, "package labels unresolved after pass 2: %d" % len(mine)
assert ok, "compile failed"
shutil.rmtree(tmp, ignore_errors=True)
print("CERT PASS")
raise SystemExit(0)
