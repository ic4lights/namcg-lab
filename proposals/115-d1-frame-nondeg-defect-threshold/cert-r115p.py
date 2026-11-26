# cert-r115p.py -- compile certificate for insert-d1-frame-threshold.tex
# Copy of the working tree (minus .git, scratch/, build junk; untracked
# namcg-book7.bbl INCLUDED) into a temp dir OUTSIDE the repository; the insert
# is spliced into the copy of chapters/appH-microscopic-proofs.tex immediately
# before the unique line "\section{Problem E: signature}"; one pdflatex pass is
# run; rc==0, no "! " error lines and "Output written" are asserted.
# Run:  python -I cert-r115p.py     (repo root resolved from cwd's parent)
import os, shutil, subprocess, sys, tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
INS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insert-d1-frame-threshold.tex")
SKIP_DIRS = {".git", "scratch", "proposals", "reports"}
SKIP_EXT = {".aux", ".log", ".out", ".toc", ".lof", ".lot", ".fls",
            ".fdb_latexmk", ".synctex.gz"}
ANCHOR = b"\section{Problem E: signature}"

tmp = tempfile.mkdtemp(prefix="cert115_", dir=os.path.join(os.environ.get("TEMP", "."), "..") if False else None)
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
out = data.replace(ANCHOR, ins + ANCHOR, 1)
open(apph, "wb").write(out)
p = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
                   cwd=tmp, capture_output=True, text=True)
log = open(os.path.join(tmp, "namcg-book7.log"), "r", errors="replace").read()
errs = [l for l in log.splitlines() if l.startswith("! ")]
ok = p.returncode == 0 and not errs and "Output written" in log
print("rc=%d errlines=%d outw=%s" % (p.returncode, len(errs), "Output written" in log))
for l in errs[:5]:
    print("ERR:", l)
shutil.rmtree(tmp, ignore_errors=True)
print("CERT PASS" if ok else "CERT FAIL")
raise SystemExit(0 if ok else 1)
