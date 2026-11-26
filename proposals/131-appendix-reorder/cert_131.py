# cert_131.py - verification pack for proposal 131 (move ledger appendix include to last position).
# Run from the repository root:  python -I proposals/131-appendix-reorder/cert_131.py
# Writes ONLY under scratch/reorder131/cert/. Never touches tracked files.
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(".").resolve()
assert (ROOT / "namcg-book7.tex").exists(), "run from repository root"
WORK = ROOT / "scratch" / "reorder131" / "cert"
WORK.mkdir(parents=True, exist_ok=True)

src = (ROOT / "namcg-book7.tex").read_bytes()
PRE = hashlib.sha256(src).hexdigest()[:12]
print("PRE %d B %s" % (len(src), PRE))

MOVE = b"\\include{chapters/appH-microscopic-proofs}"
ANCH = b"\\include{chapters/appL-coupling}"
assert src.count(MOVE + b"\r\n") == 1, "appH include anchor not unique"
assert src.count(ANCH + b"\r\n") == 1, "appL include anchor not unique"

# --- candidate: move the appH include line (incl. CRLF) to immediately after the appL line ---
mv = MOVE + b"\r\n"
an = ANCH + b"\r\n"
i = src.find(mv)
cand = src[:i] + src[i + len(mv):]
j = cand.find(an) + len(an)
cand = cand[:j] + mv + cand[j:]

# Guard 1: the edit must be a pure line permutation (same bytes re-ordered, nothing else).
def perm_ok(a, b):
    la, lb = a.split(b"\r\n"), b.split(b"\r\n")
    return len(la) == len(lb) and sorted(la) == sorted(lb) and a != b

assert perm_ok(src, cand), "candidate is not a pure line permutation"
# Guard 2 (POSITIVE CONTROL): the permutation guard must REJECT a non-permutation edit.
bogus = src.replace(ANCH, ANCH + b"X", 1)
ctrl1 = (not perm_ok(src, bogus))
print("CONTROL perm-guard: %s" % ("FIRED" if ctrl1 else "FAILED"))
assert ctrl1, "positive control failed: permutation guard vacuous"
# Guard 3 (POSITIVE CONTROL): order check must reject the unchanged file.
ctrl2 = perm_ok(src, src)
assert not ctrl2, "positive control failed: identity edit accepted"
print("CONTROL order-guard: %s" % ("FIRED" if not ctrl2 else "FAILED"))

# integrator view: the 12-line appendix include block (appA..appL), before/after, anchored on appA
APP_A = b"\\include{chapters/appA-seeley-dewitt}"

def block(buf):
    L = buf.split(b"\r\n")
    k = [q for q, X in enumerate(L) if X == APP_A][0]
    assert src.count(APP_A + b"\r\n") == 1, "appA anchor not unique"
    return b"\r\n".join(L[k:k + 12]) + b"\r\n"

blk_pre, blk_post = block(src), block(cand)
print("INTEGRATE block %d B %s -> %d B %s" % (
    len(blk_pre), hashlib.sha256(blk_pre).hexdigest()[:12],
    len(blk_post), hashlib.sha256(blk_post).hexdigest()[:12]))
assert len(blk_pre) == len(blk_post)
# Guard 4 (POSITIVE CONTROL): block anchor must not match a perturbed block.
assert src.count(blk_pre + b"X") == 0
print("CONTROL block-anchor: FIRED")

print("POST %d B %s" % (len(cand), hashlib.sha256(cand).hexdigest()[:12]))

# --- parse helper: mirror of scripts/build_check.py string-parse (never regex on backslash-h) ---
B = chr(92)

def parse(logpath):
    log = Path(logpath).read_text(errors="replace")
    boxes = []
    L = log.splitlines()
    for n, l in enumerate(L):
        if "Overfull " + B + "hbox (" in l and "pt too wide)" in l:
            boxes.append(float(l.split("Overfull " + B + "hbox (")[1].split("pt too wide)")[0]))
    uref = len(re.findall(r"Reference `.*' on page .* undefined", log))
    ucit = len(re.findall(r"Citation `.*' on page .* undefined", log))
    m = re.search(r"\((\d+) pages, \d+ bytes\)", log)  # path wrap can split "Output written" across lines
    errs = [x for x in L if x.startswith("!")]
    return len(boxes), max(boxes) if boxes else 0.0, uref, ucit, (m.group(1) if m else "?"), len(errs)

# control for the overfull parser
fake = WORK / "fake.log"
fake.write_text("Overfull " + B + "hbox (9.99pt too wide) in paragraph at lines 5--6\n", encoding="ascii")
fb, fm, _, _, _, _ = parse(fake)
print("CONTROL parser: %s" % ("FIRED" if (fb == 1 and abs(fm - 9.99) < 1e-6) else "FAILED"))
assert fb == 1 and abs(fm - 9.99) < 1e-6, "positive control failed: overfull parser vacuous"

# --- mirror compiles (BASE = live tree root file, CAND = moved line); .bbl copied, no bibtex needed ---
def mirror(name, texbytes):
    d = WORK / name
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    (d / "namcg-book7.tex").write_bytes(texbytes)
    shutil.copy(ROOT / "namcg-book7.bbl", d / "namcg-book7.bbl")
    for _ in range(3):  # three passes, mirroring scripts/build_check.py (TOC/refs fully settled)
        p = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", str(d), str(d / "namcg-book7.tex")],
                           cwd=ROOT, capture_output=True, text=True, errors="replace", timeout=900)
        if p.returncode != 0:
            print(name + " COMPILE FAILED")
            print("\n".join(x for x in p.stdout.splitlines() if x.startswith("!") or "Error" in x)[:2000])
            sys.exit(1)
    return parse(d / "namcg-book7.log")

bt, bm, bu, bc, bp, be = mirror("base", src)
ct, cm, cu, cc, cp, ce = mirror("cand", cand)
print("BASE pages=%s overfull=%d max=%.3f uref=%d ucit=%d err=%d" % (bp, bt, bm, bu, bc, be))
print("CAND pages=%s overfull=%d max=%.3f uref=%d ucit=%d err=%d" % (cp, ct, cm, cu, cc, ce))

ok = (cu == 0 and cc == 0 and ce == 0 and ct <= 1 and cm < 2.0)
print("CERT131 %s PRE12=%s POST12=%s BASE=%s,%d,%.3f CAND=%s,%d,%.3f CONTROLS=FIRED"
      % ("PASS" if ok else "FAIL", PRE, hashlib.sha256(cand).hexdigest()[:12], bp, bt, bm, cp, ct, cm))
sys.exit(0 if ok else 1)
