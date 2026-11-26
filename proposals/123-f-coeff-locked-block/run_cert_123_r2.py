# -*- coding: ascii -*-
# Item 123 r2 compile certificate. Same protocol as run_cert_123.py (r1,
# bytes f54de3d0e12e, left untouched) with r2 constants and -r2 artifact
# names: fresh %TEMP% copy of the minimal build tree, substitute the r2
# SPLICED appH (hash-asserted), pdflatex + bibtex + pdflatex x2, log scan,
# summary written with python file IO. Exit 0 iff certificate holds.
import os, shutil, subprocess, hashlib, re

REPO = r"C:\Users\redgi\Projects\namcg-lab@gpu"
CERT = os.path.join(os.environ["TEMP"], "cert123r2build")
FOLD = os.path.join(REPO, "proposals", "123-f-coeff-locked-block")
SPLICED = os.path.join(os.environ["TEMP"], "cert123r2", "appH-spliced-r2.tex")
POST_SHA1 = "ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1"
POST_SIZE = 869275

def sha(p):
    return hashlib.sha1(open(p, "rb").read()).hexdigest()

log = []
def note(s):
    log.append(s)
    print(s)

if os.path.exists(CERT):
    shutil.rmtree(CERT)
os.makedirs(CERT)
shutil.copy2(os.path.join(REPO, "namcg-book7.tex"), CERT)
shutil.copy2(os.path.join(REPO, "namcg-book7.bbl"), CERT)
for d in ("chapters", "frontmatter", "bib", "figs"):
    shutil.copytree(os.path.join(REPO, d), os.path.join(CERT, d))
sp = open(SPLICED, "rb").read()
if hashlib.sha1(sp).hexdigest() != POST_SHA1 or len(sp) != POST_SIZE:
    note("CERT FAIL: spliced file hash/size mismatch %s %d" % (sha(SPLICED)[:12], len(sp)))
    open(os.path.join(FOLD, "cert-summary-123-r2.txt"), "w").write("\n".join(log))
    raise SystemExit(1)
open(os.path.join(CERT, "chapters", "appH-microscopic-proofs.tex"), "wb").write(sp)
tgt = os.path.join(CERT, "chapters", "appH-microscopic-proofs.tex")
note("SUBSTITUTED appH sha1 %s size %d (expect POST %s %d)"
     % (sha(tgt)[:12], len(sp), POST_SHA1[:12], POST_SIZE))

import time
def run(cmd):
    p = subprocess.run(cmd, cwd=CERT, shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.returncode

r = []
r.append(("pdflatex1", run('pdflatex -interaction=nonstopmode namcg-book7.tex > pl1.log 2>&1')))
r.append(("bibtex", run('bibtex namcg-book7 > bib.log 2>&1')))
r.append(("pdflatex2", run('pdflatex -interaction=nonstopmode namcg-book7.tex > pl2.log 2>&1')))
r.append(("pdflatex3", run('pdflatex -interaction=nonstopmode namcg-book7.tex > pl3.log 2>&1')))
for name, rc in r:
    note("%s rc=%d" % (name, rc))

def scan(fname):
    t = open(os.path.join(CERT, fname), "r", errors="replace").read()
    bang = len(re.findall(r"(?m)^!", t))
    undef = len(re.findall(r"undefined (?:references|citations)|Reference .* undefined|Citation .* undefined", t))
    mult = len(re.findall(r"multiply.defined|Multiplication|multiply defined", t))
    q = len(re.findall(r"(?m)^! ", t))
    return bang, undef, mult, q

tot = [0, 0, 0]
for lg in ("pl1.log", "pl2.log", "pl3.log"):
    b, u, m, q = scan(lg)
    note("%s: bang-lines=%d undefined=%d multiply=%d '^!'=%d" % (lg, b, u, m, q))
    tot[0] += b; tot[1] += u; tot[2] += m
b3, u3, m3, _ = scan("pl3.log")
time.sleep(10)
r2 = []
for lg in ("pl1.log", "pl2.log", "pl3.log"):
    b, u, m, q = scan(lg)
    r2.append((lg, b, u, m))
    note("ENDSTATE %s: bang=%d undefined=%d multiply=%d" % (lg, b, u, m))
note("STABLE = %s" % ([(x[1], x[2], x[3]) for x in r2] ==
                      [(b, u, m) for lg in ("pl1.log", "pl2.log", "pl3.log")
                       for (b, u, m, q) in [scan(lg)]]))
pdf = os.path.join(CERT, "namcg-book7.pdf")
have_pdf = os.path.exists(pdf)
rcs = all(rc == 0 for _, rc in r)
verdict = rcs and b3 == 0 and u3 == 0 and m3 == 0 and tot[0] == 0 and have_pdf
note("PDF present: %s size %d" % (have_pdf, os.path.getsize(pdf) if have_pdf else -1))
note("CERT VERDICT: %s" % ("PASS" if verdict else "FAIL"))
tail3 = open(os.path.join(CERT, "pl3.log"), "r", errors="replace").read()[-3000:]
open(os.path.join(FOLD, "cert-pl3-tail-123-r2.txt"), "w").write(tail3)
shutil.copy2(os.path.join(CERT, "pl3.log"), os.path.join(FOLD, "cert-pl3-full-123-r2.log"))
shutil.copy2(os.path.join(CERT, "bib.log"), os.path.join(FOLD, "cert-bib-123-r2.log"))
open(os.path.join(FOLD, "cert-summary-123-r2.txt"), "w").write("\n".join(log) + "\n")
raise SystemExit(0 if verdict else 1)
