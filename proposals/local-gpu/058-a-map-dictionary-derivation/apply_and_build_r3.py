"""Apply the r3 insertion to a COPY of the manuscript outside the repository and build it.

Usage:  python -I apply_and_build_r3.py <repo-root> <empty-build-dir-outside-repo> [--keep]

Never writes into <repo-root>. Steps: copy namcg-book7.tex, namcg-book7.bbl, chapters/*.tex,
frontmatter/*.tex, figs/, bib/, *.png into the build dir; check the pre-image sha256 of
chapters/appH-microscopic-proofs.tex; check the anchor occurs exactly once; insert
insert-r3.tex (CRLF) before the Problem A "Missing step" paragraph; print the post-image
sha256; run pdflatex twice; scan the log for undefined / multiply-defined references and
LaTeX errors; check CRLF purity of the patched file; delete the build dir unless --keep.
"""
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

PRE = "fc0884aa8c24e414020520f979a356b07374e2d58e8cdedf55910344a16510c6"
ANCHOR = (b"control only the difference from an unproven candidate, not from the\r\n"
          b"diamond modular\r\nHamiltonian.\r\n\r\n")
AFTER = b"\\paragraph{Missing step.}\r\nAn error-controlled identification of the algebraic inclusion generated"

here = Path(__file__).resolve().parent
repo = Path(sys.argv[1]).resolve()
build = Path(sys.argv[2]).resolve()
keep = "--keep" in sys.argv
assert repo not in build.parents and build != repo, "build dir must be outside the repository"
assert not build.exists() or not any(build.iterdir()), "build dir must be empty"
build.mkdir(parents=True, exist_ok=True)

for name in ("namcg-book7.tex", "namcg-book7.bbl"):
    shutil.copy2(repo / name, build / name)
for sub, pat in (("chapters", "*.tex"), ("frontmatter", "*.tex"), ("figs", "*"), ("bib", "*")):
    (build / sub).mkdir(exist_ok=True)
    for f in (repo / sub).glob(pat):
        if f.is_file():
            shutil.copy2(f, build / sub / f.name)
for f in repo.glob("*.png"):
    shutil.copy2(f, build / f.name)

target = build / "chapters" / "appH-microscopic-proofs.tex"
data = target.read_bytes()
pre = hashlib.sha256(data).hexdigest()
print("pre-image sha256 :", pre, "MATCH" if pre == PRE else "MISMATCH")
assert pre == PRE
assert data.count(ANCHOR + AFTER) == 1, "anchor not unique"
ins = (here / "insert-r3.tex").read_bytes()
assert ins.count(b"\r\n") == ins.count(b"\n"), "insert not pure CRLF"
assert ins.endswith(b"\r\n\r\n")
new = data.replace(ANCHOR + AFTER, ANCHOR + ins + AFTER, 1)
target.write_bytes(new)
post = hashlib.sha256(new).hexdigest()
print("post-image sha256:", post)
print("patched file CRLF-pure:", new.count(b"\r\n") == new.count(b"\n"))
print("insert line count:", ins.count(b"\r\n"))

pages = None
for i in (1, 2):
    p = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
                       cwd=build, capture_output=True, text=True, errors="replace", timeout=900)
    m = re.search(r"Output written on .*?\((\d+) pages", p.stdout)
    print("pdflatex pass %d: rc=%d pages=%s" % (i, p.returncode, m.group(1) if m else "?"))
    pages = m.group(1) if m else None
log = (build / "namcg-book7.log").read_text(errors="replace")
undef = re.findall(r"(?:Reference|Citation) `[^']+' on page \d+ undefined", log)
multi = re.findall(r"Label `[^']+' multiply defined", log)
errs = re.findall(r"^! .*", log, flags=re.M)
print("undefined refs/cites:", len(undef), undef[:5])
print("multiply-defined labels:", len(multi), multi[:5])
print("LaTeX errors:", len(errs), errs[:5])
aux = (build / "chapters" / "appH-microscopic-proofs.aux").read_text(errors="replace")
print("BUILD", "PASS" if pages and not undef and not multi and not errs else "FAIL", "pages=%s" % pages)
if not keep:
    shutil.rmtree(build)
    print("build dir removed")
