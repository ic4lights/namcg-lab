# smoke_compile_092.py - POS compile of insert-r1.tex standalone + NEG byte-surgery control
# (first \bigl -> \biglz must fail undefined-control-sequence). Scratch in-folder, deleted.
# Run: python -I proposals/092-g-profile-coordinate-transport/smoke_compile_092.py
import os, subprocess, shutil, sys
D = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(D, "scratch_latex_092")
ins = open(os.path.join(D, "insert-r1.tex"), "rb").read().replace(b"\r\n", b"\n")
def wrap(body):
    return b"\\documentclass{article}\\usepackage{amsmath,amssymb}\\begin{document}\n" + body + b"\n\\end{document}\n"
if os.path.isdir(S):
    shutil.rmtree(S)
os.makedirs(S)
def compile_tex(name, body):
    open(os.path.join(S, name + ".tex"), "wb").write(wrap(body))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                       cwd=S, capture_output=True)
    logp = os.path.join(S, name + ".log")
    log = open(logp, "rb").read() if os.path.exists(logp) else b""
    return r.returncode, log
rc, log = compile_tex("pos", ins)
pos_ok = rc == 0
print("POS rc:", rc, "expect 0 ->", "OK" if pos_ok else "FAIL")
if not pos_ok:
    print(log[-1200:].decode(errors="replace"))
i = ins.index(b"\\bigl")
neg = ins[:i] + b"\\biglz" + ins[i + 5:]
rc2, log2 = compile_tex("neg", neg)
neg_ok = rc2 != 0 and b"undefined control sequence" in log2.lower()
print("NEG rc:", rc2, "expect nonzero with undefined control sequence ->", "OK" if neg_ok else "FAIL")
shutil.rmtree(S)
print("SMOKE 092:", "PASS" if pos_ok and neg_ok else "FAIL")
sys.exit(0 if pos_ok and neg_ok else 1)
