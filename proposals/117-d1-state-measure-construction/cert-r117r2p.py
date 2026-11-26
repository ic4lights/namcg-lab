# cert-r117r2p.py -- compile certificate for insert-d1-state-measure-r2.tex (proposal 117)
# Copy of the working tree (minus .git, scratch/, proposals/, reports/, build
# junk; untracked namcg-book7.bbl INCLUDED) into a temp dir OUTSIDE the
# repository. Two edits are applied to the copy of
# chapters/appH-microscopic-proofs.tex, in order:
#   (1) stale-passage amendment of the integrated 116 clause (unique count 1,
#       recounted live);
#   (2) the insert (leading CRLF separator + one paragraph line + CRLF) spliced
#       immediately before the unique line "\section{Problem E: signature}"
#       via the 115-form join  data.replace(ANCHOR, INS + CRLF + ANCHOR, 1).
# Two pdflatex passes are run (pass 1 builds .aux, pass 2 resolves refs);
# rc1==rc2==0, zero "! " error lines, "Output written", zero undefined
# references at pass 2, and zero undefined references touching package labels
# are HARD-ASSERTED before CERT PASS is printed.
# Run:  python -I -B cert-r117r2p.py     (from the proposal folder)
import os, shutil, subprocess, sys, tempfile, hashlib

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
HERE = os.path.dirname(os.path.abspath(__file__))
INS = os.path.join(HERE, "insert-d1-state-measure-r2.tex")
SKIP_DIRS = {".git", "scratch", "proposals", "reports"}
SKIP_EXT = {".aux", ".log", ".out", ".toc", ".lof", ".lot", ".fls",
            ".fdb_latexmk", ".synctex.gz"}
ANCHOR = b"\section{Problem E: signature}"
OLD = b"no state of the matrix theory and no integration measure is constructed"
NEW = (b"no state of the matrix theory is constructed (the Euclidean Gibbs "
       b"measure of the paragraph below is a Presentation-B probe measure, "
       b"not a matrix-theory state)")

tmp = tempfile.mkdtemp(prefix="cert117r2_")
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
assert hashlib.sha1(base).hexdigest() == "28f3a0d2401efc1c65b53a99a5968cdcb70fed7d" and len(base) == 834663, "live appH moved off the 117 baseline pin"
assert base.find(ANCHOR) == 281406, "anchor byte offset moved: %d" % base.find(ANCHOR)
assert base.count(ANCHOR) == 1, "anchor not unique: %d" % base.count(ANCHOR)
assert base.count(OLD) == 1, "amendment string not unique: %d" % base.count(OLD)
amended = base.replace(OLD, NEW, 1)
print("amended   sha1 %s size %d (delta %+d)" % (hashlib.sha1(amended).hexdigest(),
                                                 len(amended), len(amended) - len(base)))
assert hashlib.sha1(amended).hexdigest() == "a38d4e293806a09f7fc5072a273ae49f62100590" and len(amended) == 834750, "Edit A intermediate off pin" 
ins = open(INS, "rb").read()
assert hashlib.sha1(ins).hexdigest() == "51010545179a3d3609826aefa0f6c1fa84182ae4" and len(ins) == 4585, "r2 payload off pin"
BS = chr(92)
OLD_SENT = b"so the volume-averaged soft-event estimate " + (BS+"("+BS+"mathrm{Vol}^{-1}"+BS+"int"+BS+"omega_x").encode("ascii")
NEW_SENT = b"so the spacetime-integrated soft-event estimate " + (BS+"("+BS+"int"+BS+"omega_x").encode("ascii")
r1p = open(os.path.join(HERE, "insert-d1-state-measure.tex"), "rb").read()
assert hashlib.sha1(r1p).hexdigest() == "b514e44a19ee627f0aab4ac3d4f69bc052506154" and len(r1p) == 4597, "r1 payload moved off its pin"
assert r1p.count(OLD_SENT) == 1, "OLD (v) sentence not unique in r1"
assert r1p.replace(OLD_SENT, NEW_SENT, 1) == ins, "r2 is NOT the r1 bytes with exactly the (v)-sentence replacement"
assert ins.replace(NEW_SENT, OLD_SENT, 1) == r1p, "reverse substitution does not recover r1 bytes"
print("byte-reconstruction: r2 = r1 + single (v)-sentence replacement; reverse exact OK")
assert ins.startswith(b"\r\n") and ins.endswith(b"\r\n"), "insert must start and end with CRLF"
assert ins.count(b"\n") == 2 and ins.count(b"\r") == 2, "insert must be blank CRLF + one CRLF line"
assert all(b < 128 for b in ins) and b"\t" not in ins, "insert not ASCII/tab-free"
out = amended.replace(ANCHOR, ins + b"\r\n" + ANCHOR, 1)
print("POST      sha1 %s size %d (= baseline %+d amend, +%d payload, +2 join)"
      % (hashlib.sha1(out).hexdigest(), len(out), len(NEW) - len(OLD), len(ins)))
assert len(out) == 834750 + 4585 + 2, "POST size arithmetic wrong"
assert hashlib.sha1(out).hexdigest() == "ce91063fddcaa5599429519f4bc2c478e0d919e8", "POST sha1 off expected r2 splice"
assert len(out) == len(amended) + len(ins) + 2, "POST = amended + payload + 2 CRLF join" 
open(apph, "wb").write(out)
CMDC = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"]
p1 = subprocess.run(CMDC, cwd=tmp, capture_output=True, text=True)   # pass 1
p2 = subprocess.run(CMDC, cwd=tmp, capture_output=True, text=True)   # pass 2
log = open(os.path.join(tmp, "namcg-book7.log"), "r", errors="replace").read()
errs = [l for l in log.splitlines() if l.startswith("! ")]
undef = [l for l in log.splitlines() if "undefined" in l and "There were" not in l]
mine = [l for l in undef if any(k in l for k in ("eq:V'", "eq:Smicro", "eq:vacuum-manifold",
                                                 "eq:vev-is-frame", "ass:nondeg",
                                                 "ass:frame-lock", "sec:ch3-relate"))]
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
