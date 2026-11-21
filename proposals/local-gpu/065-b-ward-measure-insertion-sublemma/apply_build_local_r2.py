"""065 local round 2: apply check (in memory) and optional out-of-repo build.

Without arguments: read-only. Asserts the live pre-states of appH and bib, checks that the
anchor (closing sentence of the paragraph on the matrix gauge realisation, blank line,
Problem C header) occurs exactly once, splices insert-local-r2.tex immediately before
\\section{Problem C: conformal mode and Cassini}, appends bib_additions.bib, and prints the
predicted post-states. Nothing in the repository is written.

With --build DIR (DIR must be outside the repository and must not exist): copies
namcg-book7.tex, chapters/, frontmatter/, bib/, figs/, code/ into DIR, writes the applied appH
and bib there, runs pdflatex, bibtex, pdflatex, pdflatex in DIR and scans the log. The copy is
left in place (no deletion).

Run:  python -I apply_build_local_r2.py [--build DIR]
"""
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
APPH = os.path.join(ROOT, "chapters", "appH-microscopic-proofs.tex")
BIB = os.path.join(ROOT, "bib", "namcg.bib")
INS = os.path.join(HERE, "insert-local-r2.tex")
BIBADD = os.path.join(HERE, "bib_additions.bib")
CR, LF = b"\x0d", b"\x0a"
NL = CR + LF

APPH_SHA = "4d6d58cf7947dae9570e917ced6db8b6e40287437162321c4517eb726a568fce"
BIB_SHA = "a7aec454de0f6591c157ecb4709179f212c876b6f0df5df67713df85bb0493ed"
INS_SHA = "c8a2422bed86cb74a983ced0e3f64db25d9c68b578fee24a0a9c8dec8f5c312e"
ANCHOR_SENT = (b"the Dirac sector or the measure of the matrix integral, and derive no local Lorentz "
               b"symmetry. Problems~B and~D remain open and PROGRAMME-CONDITIONAL.")
HEADER = b"\\section{Problem C: conformal mode and Cassini}"
CLOSE_065 = (b"These identifications record what the published mechanisms do and do not supply for "
             b"Problem~B; no result is imported into the matrix theory. Problems~B and~D remain open "
             b"and PROGRAMME-CONDITIONAL.")
NEW_KEYS = ["ChoudhuryLaurenzano2024", "TsuchiyaYamashiro2022", "KawamotoKuroki2021", "AlloucheDou2026",
            "Craps2026", "EynardOrantin2009", "JacobsonVisser2019", "Svesko2019", "JensenSorceSperanza2023",
            "ArataLiberatiNeri2026", "ArataIsmailLiberati2026"]


def stats(tag, b):
    crlf = b.count(NL)
    print("%s: bytes=%d CRLF=%d bareLF=%d sha256=%s" % (tag, len(b), crlf, b.count(LF) - crlf, hashlib.sha256(b).hexdigest()))


pre = io.open(APPH, "rb").read()
stats("appH pre", pre)
assert hashlib.sha256(pre).hexdigest() == APPH_SHA, "appH is not the certified live pre-state"
bib = io.open(BIB, "rb").read()
stats("bib  pre", bib)
assert hashlib.sha256(bib).hexdigest() == BIB_SHA, "bib is not the certified live pre-state"
ins = io.open(INS, "rb").read()
stats("insert", ins)
assert hashlib.sha256(ins).hexdigest() == INS_SHA and ins.count(LF) == ins.count(NL) and ins.endswith(NL)

anchor = ANCHOR_SENT + NL + NL + HEADER
print("anchor sentence occurrences:", pre.count(ANCHOR_SENT), "| anchor+header occurrences:", pre.count(anchor),
      "| header occurrences:", pre.count(HEADER))
assert pre.count(ANCHOR_SENT) == 1 and pre.count(anchor) == 1 and pre.count(HEADER) == 1
i = pre.index(HEADER)
post = pre[:i] + ins + NL + pre[i:]
stats("appH post", post)
assert post.count(LF) == post.count(NL)
assert post.replace(ins + NL, b"", 1) == pre, "splice changes something other than the insert"
s_B = post.index(b"\\section{Problem B: replica Ward identity}")
assert s_B < post.index(ins) < post.index(HEADER), "insert not inside sec:status-B"
assert post.count(CLOSE_065 + NL + NL + HEADER) == 1
print("post: 065 closing sentence + blank + Problem C header occurs once (re-anchor point for local 070)")
j = post.index(ANCHOR_SENT + NL + NL + b"\\paragraph{Schwinger--Dyson insertion")
assert post.rfind(b"\\paragraph{", 0, j) == post.index(b"\\paragraph{Matrix gauge realisation of the compensating rotation")
print("post: matrix gauge realisation paragraph is immediately followed by the 065 block ('preceding paragraph' resolves)")

txt = ins.decode("utf-8")
cites = sorted(set(k.strip() for grp in re.findall(r"\\cite\{([^}]*)\}", txt) for k in grp.split(",")))
refs = sorted(set(re.findall(r"\\(?:eq)?ref\{([^}]*)\}", txt)))
print("cite keys:", cites)
print("refs:", refs)
assert set(cites) == set(NEW_KEYS)
alltex = "".join(io.open(os.path.join(ROOT, "chapters", f), encoding="utf-8").read()
                 for f in os.listdir(os.path.join(ROOT, "chapters")) if f.endswith(".tex"))
for r in refs:
    nlab = alltex.count("\\label{%s}" % r)
    print("  label %-10s defined %d time(s) in chapters/" % (r, nlab))
    assert nlab == 1

add = io.open(BIBADD, "rb").read().replace(NL, LF).replace(LF, NL)
for k in NEW_KEYS:
    assert bib.count(("{%s," % k).encode()) == 0 and add.count(("{%s," % k).encode()) == 1, k
bpost = bib + NL + add
stats("bib  post", bpost)
print("bib entries post:", len(re.findall(rb"^@\w+\{", bpost, re.M)))
for w in ("proposal", "researcher", "gatekeeper", "as proposed", " round ", "this book proposes"):
    assert w not in txt.lower(), w
print("APPLY CHECK PASS")

if "--build" in sys.argv:
    out = os.path.abspath(sys.argv[sys.argv.index("--build") + 1])
    assert not out.startswith(ROOT), "build dir must be outside the repository"
    assert not os.path.exists(out), "build dir must not exist"
    os.makedirs(out)
    shutil.copy2(os.path.join(ROOT, "namcg-book7.tex"), out)
    for d in ("chapters", "frontmatter", "bib", "figs", "code"):
        if os.path.isdir(os.path.join(ROOT, d)):
            shutil.copytree(os.path.join(ROOT, d), os.path.join(out, d))
    io.open(os.path.join(out, "chapters", "appH-microscopic-proofs.tex"), "wb").write(post)
    io.open(os.path.join(out, "bib", "namcg.bib"), "wb").write(bpost)
    steps = [["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
             ["bibtex", "namcg-book7"],
             ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
             ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"]]
    for st in steps:
        p = subprocess.run(st, cwd=out, capture_output=True, text=True, errors="replace", timeout=1800)
        m = re.search(r"Output written on .*?\((\d+) pages", p.stdout)
        print("%-8s rc=%d %s" % (st[0], p.returncode, ("pages=" + m.group(1)) if m else ""))
        if st[0] == "pdflatex" and (p.returncode != 0 or not m):
            print("\n".join(l for l in p.stdout.splitlines() if l.startswith("!"))[:2000])
            sys.exit(1)
    log = io.open(os.path.join(out, "namcg-book7.log"), encoding="utf-8", errors="replace").read()
    bad = [l for l in log.splitlines() if re.search(r"undefined references|Reference `.*' on page .* undefined|Citation `.*' on page .* undefined|multiply[- ]defined|There were undefined", l)]
    print("undefined/multiply-defined warnings: %d" % len(bad))
    for l in bad[:10]:
        print("  " + l)
    blg = io.open(os.path.join(out, "namcg-book7.blg"), encoding="utf-8", errors="replace").read()
    print("bibtex warnings/errors:", len(re.findall(r"^(Warning|I couldn't|Repeated entry)", blg, re.M)))
    bbl = io.open(os.path.join(out, "namcg-book7.bbl"), encoding="utf-8", errors="replace").read()
    print("new keys in bbl:", sum(1 for k in NEW_KEYS if "{%s}" % k in bbl), "/", len(NEW_KEYS))
    print("BUILD PASS" if not bad else "BUILD WARNINGS")
