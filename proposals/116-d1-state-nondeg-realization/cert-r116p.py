# cert-r116p.py -- compile certificate for insert-d1-state-nondeg.tex
# Copy of the working tree (minus .git, scratch/, proposals/, reports/, build
# junk; untracked namcg-book7.bbl INCLUDED) into a temp dir OUTSIDE the
# repository; the insert (one CRLF-terminated line) is spliced into the copy
# of chapters/appH-microscopic-proofs.tex immediately before the unique line
# "\section{Problem E: signature}" (live appH L1713; the pre-existing blank
# L1712 keeps the paragraph break before the insert). One pdflatex pass is
# run; rc==0, no "! " error lines and "Output written" are asserted.
# Run:  python -I cert-r116p.py     (from the proposal folder)
import os, shutil, subprocess, sys, tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
INS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insert-d1-state-nondeg.tex")
SKIP_DIRS = {".git", "scratch", "proposals", "reports"}
SKIP_EXT = {".aux", ".log", ".out", ".toc", ".lof", ".lot", ".fls",
            ".fdb_latexmk", ".synctex.gz"}
ANCHOR = b"\section{Problem E: signature}"

tmp = tempfile.mkdtemp(prefix="cert116_")
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
data = open(apph, "rb").read()
assert data.count(ANCHOR) == 1, "anchor not unique: %d" % data.count(ANCHOR)
ins = open(INS, "rb").read()
assert ins.endswith(b"\r\n") and ins.count(b"\n") == 1, "insert must be one CRLF line"
out = data.replace(ANCHOR, ins + ANCHOR, 1)
open(apph, "wb").write(out)
CMDC = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"]
p1 = subprocess.run(CMDC, cwd=tmp, capture_output=True, text=True)   # pass 1: builds .aux
p2 = subprocess.run(CMDC, cwd=tmp, capture_output=True, text=True)   # pass 2: resolves refs
log = open(os.path.join(tmp, "namcg-book7.log"), "r", errors="replace").read()
errs = [l for l in log.splitlines() if l.startswith("! ")]
undef = [l for l in log.splitlines() if "undefined" in l and "There were" not in l]
ok = p1.returncode == 0 and p2.returncode == 0 and not errs and "Output written" in log
print("rc1=%d rc2=%d errlines=%d outw=%s undefrefs_pass2=%d" %
      (p1.returncode, p2.returncode, len(errs), "Output written" in log, len(undef)))
for l in errs[:5]:
    print("ERR:", l)
for l in undef[:10]:
    print("UNDEF:", l)
mine = [l for l in undef if any(k in l for k in ("eq:V'", "eq:vacuum-manifold", "eq:Phi-eom", "eq:vev-is-frame", "ass:nondeg", "ass:frame-lock", "sec:ch3-relate"))]
print("undefrefs-touching-package-labels=%d" % len(mine))
for l in mine[:10]:
    print("PKG-UNDEF:", l)
assert len(undef) == 0, "undefined references remain after pass 2: %d" % len(undef)
assert len(mine) == 0, "package labels unresolved after pass 2: %d" % len(mine)
shutil.rmtree(tmp, ignore_errors=True)
print("CERT PASS" if ok else "CERT FAIL")
raise SystemExit(0 if ok else 1)
