"""070 round 2: apply check and out-of-repository build. Read-only on the repository.

Re-run (from any directory):
    python -I proposals/070-b-content-class/apply_build_r2.py [BUILD_BASE_DIR]

Without BUILD_BASE_DIR only the apply checks run. With it, the script copies the build inputs to a new
subdirectory of BUILD_BASE_DIR (which must lie outside the repository), writes the applied appH there, and
runs two pdflatex passes. Nothing is deleted; the copy is left for inspection.
"""
import glob
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys
import time

here = pathlib.Path(__file__).resolve().parent
root = here.parents[1]
appH_path = root / "chapters" / "appH-microscopic-proofs.tex"

PRE = "5106f9938be746607dd0b5fe6ecbf89a2918d795ffad7ee79d9ed7bf972d7681"
POST = "7e9f6760aa8d353fd2c4beac1f13d67fd516644de0d06813c2aac7a510b28072"

ANCHOR = (b"These identifications record what the published mechanisms do and do not supply for Problem~B; "
          b"no result is imported into the matrix theory. Problems~B and~D remain open and PROGRAMME-CONDITIONAL."
          b"\r\n\r\n\\section{Problem C: conformal mode and Cassini}")
CUT_AT = b"\\section{Problem C: conformal mode and Cassini}"

# companion edit: the paragraph on nearest published statements is no longer the last of the section
OLD2 = b"in the paragraph on the nearest published statements at the end of this section)"
NEW2 = b"in the paragraph on the nearest published statements later in this section)"

ok = True


def check(label, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + label)
    ok &= bool(cond)


app = appH_path.read_bytes()
pre = hashlib.sha256(app).hexdigest()
print("pre appH:", len(app), pre)
check("pre hash matches", pre == PRE)
check("anchor occurs once", app.count(ANCHOR) == 1)
check("companion phrase occurs once", app.count(OLD2) == 1)

ins = (here / "appH_insert_r3.tex").read_bytes()
check("insert is CRLF only", b"\n" not in ins.replace(b"\r\n", b"") and b"\r\n" in ins)
check("insert has no BOM", not ins.startswith(b"\xef\xbb\xbf"))
check("insert ends with one blank line", ins.endswith(b".\r\n\r\n") and not ins.endswith(b"\r\n\r\n\r\n"))

cut = app.index(ANCHOR) + ANCHOR.index(CUT_AT)
new = app[:cut] + ins + app[cut:]
new = new.replace(OLD2, NEW2, 1)
check("result CRLF only", b"\n" not in new.replace(b"\r\n", b""))
check("insert lies in sec:status-B", new.index(b"\\label{sec:status-B}") < new.index(ins) < new.index(b"\\label{sec:status-C}"))
check("companion edit precedes insert, inside sec:status-B",
      new.index(b"\\label{sec:status-B}") < new.index(NEW2) < new.index(ins))

txt = ins.decode("utf-8")
others = "".join(pathlib.Path(p).read_text(encoding="utf-8", errors="replace")
                 for p in glob.glob(str(root / "chapters" / "*.tex")))
for lab in sorted(set(re.findall(r"\\(?:eq)?ref\{([^}]*)\}", txt))):
    c = others.count("\\label{%s}" % lab)
    check("ref %s has exactly one label (%d)" % (lab, c), c == 1)
check("insert adds no label", not re.findall(r"\\label\{", txt))
bib = (root / "bib" / "namcg.bib").read_text(encoding="utf-8", errors="replace")
for key in sorted(set(k.strip() for g in re.findall(r"\\cite\{([^}]*)\}", txt) for k in g.split(","))):
    c = len(re.findall(r"@\w+\{%s," % re.escape(key), bib))
    check("cite %s has one bib entry (%d)" % (key, c), c == 1)
main = (root / "namcg-book7.tex").read_text(encoding="utf-8", errors="replace")
check("\\LUV defined in namcg-book7.tex", "\\LUV" in main)
bal = (txt.count("{") - txt.count("}"), txt.count("\\(") - txt.count("\\)"),
       txt.count("\\[") - txt.count("\\]"), txt.count("\\begin{") - txt.count("\\end{"))
check("brace/inline/display/env balance %s" % (bal,), bal == (0, 0, 0, 0))
bad = [w for w in ("proposal", "researcher", "gatekeeper", "adversary", "as proposed", "round", "frontier", "chain")
       if re.search(r"%s" % w, txt.lower())]
check("no process words %s" % bad, not bad)
check("no ledger-label line", "Status:" not in txt and "Priority:" not in txt and "Completion:" not in txt)
status = re.findall(r"Problems?~[^.]*?(?:remain|stays?) open[^.]*\.", txt)
check("exactly one status sentence %s" % status, len(status) == 1)
prev_status = b"Problems~B and~D remain open and PROGRAMME-CONDITIONAL."
check("status sentence differs from the adjacent preceding one", status and status[0].encode() != prev_status)
labels = re.findall(r"\\label\{([^}]*)\}", "".join(
    pathlib.Path(p).read_text(encoding="utf-8", errors="replace") for p in glob.glob(str(root / "chapters" / "*.tex"))
    if not p.endswith("appH-microscopic-proofs.tex")) + new.decode("utf-8"))
dups = sorted({l for l in labels if labels.count(l) > 1})
check("no duplicate labels after apply %s" % dups, not dups)

post = hashlib.sha256(new).hexdigest()
print("post appH:", len(new), post)
if POST != "EXPECTED_POST":
    check("post hash matches expected", post == POST)

if len(sys.argv) > 1:
    base = pathlib.Path(sys.argv[1]).resolve()
    check("build base lies outside the repository", root not in base.parents and base != root)
    if ok:
        dest = base / ("070-r2-build-%d" % int(time.time()))
        dest.mkdir(parents=True)
        for name in ("namcg-book7.tex", "namcg-book7.bbl"):
            shutil.copy2(root / name, dest / name)
        for p in root.glob("*.png"):
            shutil.copy2(p, dest / p.name)
        for p in root.glob("*.jpg"):
            shutil.copy2(p, dest / p.name)
        for d in ("chapters", "frontmatter", "figs", "bib"):
            if (root / d).exists():
                shutil.copytree(root / d, dest / d)
        (dest / "chapters" / "appH-microscopic-proofs.tex").write_bytes(new)
        print("build copy:", dest)
        pages = None
        for i in (1, 2):
            p = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
                               cwd=dest, capture_output=True, text=True, errors="replace", timeout=1200)
            m = re.search(r"Output written on .*?\((\d+) pages", p.stdout)
            check("pdflatex pass %d" % i, p.returncode == 0 and m)
            if not m:
                print("\n".join(l for l in p.stdout.splitlines() if l.startswith("!"))[:2000])
                break
            pages = m.group(1)
        log = (dest / "namcg-book7.log").read_text(errors="replace")
        badl = [l for l in log.splitlines() if re.search(
            r"undefined references|Reference `.*' on page .* undefined|Citation `.*' on page .* undefined|"
            r"multiply[- ]defined|There were undefined", l)]
        check("no undefined/multiply-defined references or citations (%d)" % len(badl), not badl)
        for l in badl[:10]:
            print("   ", l)
        print("pages:", pages)
        aux_in_repo = (root / "namcg-book7.pdf").stat().st_mtime
        print("repository PDF mtime unchanged by this script (not written):", aux_in_repo)

print("APPLY/BUILD R2 PASS" if ok else "APPLY/BUILD R2 FAIL")
sys.exit(0 if ok else 1)
