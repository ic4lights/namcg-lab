# cert-r111p.py -- spliced-file pdflatex certificate for insert-g-srel.tex
# Run from repo root: python -I proposals/111-g-relative-entropy-density/cert-r111p.py
# Copy of tracked tree (minus scratch/reports/proposals) plus untracked namcg-book7.bbl
# (build artifact needed by \bibliography; without it every citation is undefined).
import os, subprocess, hashlib, shutil, re
ROOT = os.getcwd()
PAY = os.path.join("proposals", "111-g-relative-entropy-density", "insert-g-srel.tex")
TREE = os.path.join(ROOT, "scratch", "r111p", "tree")
LOG1 = os.path.join(ROOT, "scratch", "r111p", "pass1.log")
LOG2 = os.path.join(ROOT, "scratch", "r111p", "pass2.log")

def sha1(b): return hashlib.sha1(b).hexdigest()

def main():
    pay = open(PAY, "rb").read()
    assert pay and b"\r\n" in pay and pay.count(b"\n") == pay.count(b"\r\n"), "payload not pure CRLF"
    ps, ph = len(pay), sha1(pay)
    os.makedirs(TREE, exist_ok=True)
    files = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True).stdout.decode().split("\0")
    extra = ["namcg-book7.bbl"]
    n = 0
    for f in files + extra:
        if not f or f.startswith(("scratch/", "reports/", "proposals/")): continue
        src = os.path.join(ROOT, f)
        if not os.path.exists(src): continue
        dst = os.path.join(TREE, f.replace("/", os.sep))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst); n += 1
    ap = os.path.join(TREE, "chapters", "appH-microscopic-proofs.tex")
    d = open(ap, "rb").read()
    A1 = b"\\paragraph{Edge entropy of a matrix block"
    A2 = "Closing the matrix-derived criterion for Problem~G requires".encode()
    assert d.count(A1) == 1 and d.count(A2) == 1 and d.find(A2) < d.find(A1), "anchor uniqueness/order"
    i = d.find(A1)
    d2 = d[:i] + pay + b"\r\n\r\n" + d[i:]
    assert d2.count(pay) == 1, "payload not exactly once post-splice"
    open(ap, "wb").write(d2)
    print("payload sha1", ph, "bytes", ps, "| files copied", n, "| appH sha1", sha1(d2))
    for logp in (LOG1, LOG2):
        with open(logp, "wb") as lg:
            r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"],
                               cwd=TREE, stdout=lg, stderr=subprocess.STDOUT, timeout=580)
        print("pass rc", r.returncode, "log", os.path.basename(logp))
    t = open(LOG2, "rb").read().decode("utf-8", "replace")
    errs = len([l for l in t.splitlines() if l.startswith("! ")])
    ucit = len(re.findall(r"Citation `.*' on page .* undefined", t))
    uref = len(re.findall(r"Reference `.*' on page .* undefined", t))
    multi = len(re.findall(r"multiply[- ]defined", t, re.I))
    m = re.search(r"(\d+) pages", t)
    pages = m.group(1) if m else "?"
    verdict = "PASS" if (errs == 0 and ucit == 0 and uref == 0 and multi == 0) else "FAIL"
    print("SUMMARY PAGES", pages, "ERRORS", errs, "UNDEF_CITS", ucit, "UNDEF_REFS", uref,
          "MULTIPLY", multi, verdict, "payload sha1", ph)

if __name__ == "__main__":
    main()
