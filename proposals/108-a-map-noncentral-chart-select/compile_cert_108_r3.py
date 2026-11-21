# compile_cert_108_r3.py -- compile certificate for the r3 payload: build ONLY in scratch/compile108/.
# NEVER writes into chapters/ or .git/. Splices insert-r3.tex at the PIN into the COPIED appH,
# then runs one pdflatex pass (nonstopmode, halt-on-error) and certifies exit 0 + no "! " lines.
import io, os, shutil, hashlib, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(os.path.join(here, "..", ".."))
dst = os.path.join(repo, "scratch", "compile108")
if os.path.isdir(dst):
    shutil.rmtree(dst)
os.makedirs(dst)
def junk(f):
    return f.lower().endswith((".aux", ".log", ".out", ".flc", ".lof", ".toc", ".pdf", ".synctex.gz"))
for root, dirs, files in os.walk(repo):
    rel = os.path.relpath(root, repo)
    parts = rel.split(os.sep)
    top = parts[0]
    if top in (".git", "scratch", "__pycache__", ".claude", "proposals", "reports", "archive",
               "gpu", "sm", "sparc", "agents", "code", "scripts", "namcg-book7_KC", "namcg-book7_KC1", "namcg-book7_KC2", ".venv"):
        dirs[:] = []
        continue
    dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
    tdir = os.path.join(dst, rel)
    os.makedirs(tdir, exist_ok=True)
    for f in files:
        if top == "." and not (f.endswith((".tex", ".bbl", ".sty", ".cls", ".cfg", ".def", ".bst"))):
            continue
        if top in ("chapters", "frontmatter", "bib", "figs") or (top == "." and not junk(f)):
            if junk(f):
                continue
            shutil.copy2(os.path.join(root, f), os.path.join(tdir, f))
apph = os.path.join(dst, "chapters", "appH-microscopic-proofs.tex")
live = io.open(os.path.join(repo, "chapters", "appH-microscopic-proofs.tex"), "rb").read()
data = io.open(apph, "rb").read()
def triple(b):
    return (len(b), hashlib.sha256(b).hexdigest()[:16], b.count(b"\r\n"))
assert triple(data) == triple(live) == (812227, "698f38979140770d", 3876), "copy/live triple mismatch"
payload = io.open(os.path.join(here, "insert-r3.tex"), "rb").read()
HEAD = b"does not close Problem~A.\r\n\r\n"
TAIL = b"\paragraph{Missing step.}"
PIN = HEAD + TAIL
assert data.count(PIN) == 1, "PIN not unique"
new = data.replace(PIN, HEAD + payload + b"\r\n" + TAIL, 1)
io.open(apph, "wb").write(new)
print("spliced copy: %d/%s/%d" % triple(new))
print("live appH sha after copy+splice: %s (must equal PRE)" % hashlib.sha256(io.open(os.path.join(repo, "chapters", "appH-microscopic-proofs.tex"), "rb").read()).hexdigest()[:16])
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
                   cwd=dst, capture_output=True, timeout=480)
log = io.open(os.path.join(dst, "namcg-book7.log"), "rb").read().decode("utf-8", "replace")
errs = [l for l in log.splitlines() if l.startswith("! ")]
pages = [l for l in log.splitlines() if "Output written" in l]
print("pdflatex exit=%d" % r.returncode)
print("error lines starting with '!': %d" % len(errs))
for l in errs[:5]: print("ERR:", l[:120])
for l in pages: print("OUT:", l[:120])
ok = (r.returncode == 0 and len(errs) == 0 and len(pages) > 0)
print("COMPILE CERT: PASS=%s exit=%d errlines=%d output_written=%s" % (ok, r.returncode, len(errs), bool(pages)))
print("live appH unchanged: %s" % (io.open(os.path.join(repo, "chapters", "appH-microscopic-proofs.tex"), "rb").read() == live))
sys.exit(0 if ok else 1)
