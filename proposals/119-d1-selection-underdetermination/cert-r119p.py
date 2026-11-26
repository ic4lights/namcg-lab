# cert-r119p.py -- two-pass pdflatex compile certificate for the chain-119 payload splice.
# Builds a FRESH out-of-repo temp tree from tracked working-tree bytes (plus the working
# .bbl), splices the payload, HARD-asserts pins BEFORE compiling, compiles twice, scans logs.
# Prints CERT PASS only if every assert holds. Temp tree is deleted afterwards.
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PAY = os.path.join(HERE, "insert-overdetermination-r1.tex")
ANCHOR = "\\section{Problem E: signature}"
BASE_SIZE = 843649
BASE_SHA1_12 = "2ed53c7778c1"
PAY_SHA1_12 = "c085c19cba68"
PAY_SIZE = 5191
POST = 848842
POST_SHA1 = "9e0b198af2c3c7f11454980ec6df2e875fbb80ef"


def sha1b(b):
    return hashlib.sha1(b).hexdigest()


# ---- payload artifact read from disk (the object under certification) ----
pay = open(PAY, "rb").read()
assert len(pay) == PAY_SIZE and sha1b(pay)[:12] == PAY_SHA1_12, "payload artifact pin mismatch"

# ---- fresh out-of-repo temp tree ----
tmp = tempfile.mkdtemp(prefix="cert119_")
try:
    files = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, capture_output=True, check=True).stdout
    paths = [f.decode("utf-8") for f in files.split(b"\0") if f]
    keep = [p for p in paths if p not in ("namcg-book7.pdf",) and not p.startswith("reports/")]
    assert len(keep) == len(paths) - 1 - sum(p.startswith("reports/") for p in paths)
    n = 0
    for p in keep:
        src = os.path.join(REPO, p.replace("/", os.sep))
        dst = os.path.join(tmp, p.replace("/", os.sep))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
        n += 1
    bbl = os.path.join(REPO, "namcg-book7.bbl")
    if os.path.exists(bbl):
        shutil.copyfile(bbl, os.path.join(tmp, "namcg-book7.bbl"))
        n += 1
    assert os.path.exists(os.path.join(tmp, "namcg-book7.bbl")), "bbl missing in tree"
    assert not os.path.exists(os.path.join(tmp, "namcg-book7.pdf"))
    print("tree files copied: %d (root PDF excluded, reports/ excluded, .bbl included)" % n)

    # ---- HARD asserts BEFORE compile, on the tree copy (independent byte reconstruction) ----
    ap = os.path.join(tmp, "chapters", "appH-microscopic-proofs.tex")
    raw = open(ap, "rb").read()
    assert len(raw) == BASE_SIZE, "baseline size mismatch in tree: %d" % len(raw)
    assert sha1b(raw)[:12] == BASE_SHA1_12, "baseline sha1 pin mismatch in tree"
    text = raw.decode("utf-8")
    assert text.count(ANCHOR) == 1, "anchor count != 1 in tree"
    spliced = (text.replace(ANCHOR, pay.decode("ascii") + "\r\n" + ANCHOR, 1)).encode("utf-8")
    assert len(spliced) == POST == BASE_SIZE + len(pay) + 2, "POST mismatch"
    assert sha1b(spliced) == POST_SHA1, "POST full-sha1 mismatch"
    print("PRE-COMPILE PINS OK: baseline %s/%d, anchor 1, payload %s/%d, POST %d %s"
          % (BASE_SHA1_12, BASE_SIZE, PAY_SHA1_12, PAY_SIZE, POST, POST_SHA1))
    open(ap, "wb").write(spliced)
    assert sha1b(open(ap, "rb").read()) == POST_SHA1, "post-write readback mismatch"

    # ---- two pdflatex passes ----
    logs = []
    for i in (1, 2):
        r = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
            cwd=tmp, capture_output=True, timeout=1800)
        log = r.stdout + r.stderr
        logs.append(log)
        errs = [l for l in log.splitlines() if l.startswith(b"!")]
        print("PASS %d: rc=%d, '!' error lines: %d" % (i, r.returncode, len(errs)))
        for l in errs[:5]:
            print("   ERR:", l.decode("ascii", "replace"))
        assert r.returncode == 0, "pdflatex pass %d nonzero rc" % i
        assert not errs, "error lines in pass %d" % i
    p2 = logs[1]
    undef = [l for l in p2.splitlines() if b"undefined" in l.lower()]
    mult = [l for l in p2.splitlines() if b"ultiply defined" in l.lower()]
    print("PASS 2 log: 'undefined' lines: %d, 'multiply defined' lines: %d" % (len(undef), len(mult)))
    for l in (undef + mult)[:10]:
        print("   LOG:", l.decode("ascii", "replace"))
    assert not undef and not mult, "undefined/multiply-defined references in pass 2"
    pdfp = os.path.join(tmp, "namcg-book7.pdf")
    assert os.path.exists(pdfp) and os.path.getsize(pdfp) > 100000, "output PDF missing/too small"
    print("output PDF bytes: %d" % os.path.getsize(pdfp))
    print("CERT PASS")
finally:
    shutil.rmtree(tmp, ignore_errors=True)
    print("temp tree removed")
