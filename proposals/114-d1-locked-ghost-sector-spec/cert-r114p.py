# -*- coding: ascii -*-
# R114 compile certificate: splice insert-d1-locked-ghosts.tex into a copy of
# appH at the pinned anchor and run ONE pdflatex pass outside the repository.
# Run: python -I -B cert-r114p.py     (expects: CERT OK)
import os, shutil, subprocess, sys, tempfile

REPO = r"C:\Users\redgi\Projects\namcg-lab@gpu"
FOLDER = os.path.join(REPO, "proposals", "114-d1-locked-ghost-sector-spec")
ANCHOR = "\\paragraph{Diffeomorphism symmetry of the displayed action (conditional; not closure).}"

tmp = tempfile.mkdtemp(prefix="r114cert_")
try:
    for item in ["namcg-book7.tex", "namcg-book7.bbl"]:
        shutil.copy2(os.path.join(REPO, item), tmp)
    for d in ["chapters", "figs", "bib"]:
        shutil.copytree(os.path.join(REPO, d), os.path.join(tmp, d))
    appH = os.path.join(tmp, "chapters", "appH-microscopic-proofs.tex")
    src = open(appH, "rb").read().decode("utf-8")
    assert src.count(ANCHOR) == 1, "anchor not unique in spliced copy"
    insert = open(os.path.join(FOLDER, "insert-d1-locked-ghosts.tex"), "rb").read()
    assert b"\r\n" in insert, "insert not CRLF"
    spliced = src.replace(ANCHOR, insert.decode("utf-8") + "\r\n" + ANCHOR)
    open(appH, "wb").write(spliced.encode("utf-8"))
    p = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
        cwd=tmp, capture_output=True, text=True)
    log = open(os.path.join(tmp, "namcg-book7.log"), "r", errors="replace").read()
    errs = [l for l in log.splitlines() if l.startswith("! ")]
    ok = (p.returncode == 0) and (not errs) and ("Output written" in log)
    print("spliced bytes:", len(spliced), "rc:", p.returncode,
          "exclam-lines:", len(errs), "Output written:", "Output written" in log)
    print("CERT OK" if ok else "CERT FAIL " + str(errs[:3]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
