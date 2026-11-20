# smoke_compile_091.py - POS compile of insert-r1.tex in a minimal amsmath/amssymb document
# plus a NEG byte-surgery control (first \lvert -> \lvertz must fail with undefined control
# sequence). Scratch build dir is in-folder and deleted afterwards. Read-only elsewhere.
# Run: python -I proposals/091-g-core-induced-pair-correlation/smoke_compile_091.py
import os, subprocess, shutil, sys
D = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(D, "scratch_latex_091")
ins = open(os.path.join(D, "insert-r1.tex"), "rb").read().replace(b"\r\n", b"\n")
def wrap(body):
    head = (b"\\documentclass{article}\\usepackage{amsmath,amssymb}\\begin{document}\n")
    return head + body + b"\n\\end{document}\n"
if os.path.isdir(S):
    shutil.rmtree(S)
os.makedirs(S)
def compile_tex(name, body):
    open(os.path.join(S, name + ".tex"), "wb").write(wrap(body))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                       cwd=S, capture_output=True)
    log = open(os.path.join(S, name + ".log"), "rb").read() if os.path.exists(os.path.join(S, name + ".log")) else b""
    return r.returncode, log
rc, log = compile_tex("pos", ins)
pos_ok = rc == 0
print("POS rc:", rc, "expect 0 ->", "OK" if pos_ok else "FAIL")
i = ins.index(b"\\lvert")
neg = ins[:i] + b"\\lvertz" + ins[i + 6:]
rc2, log2 = compile_tex("neg", neg)
neg_ok = rc2 != 0 and b"undefined control sequence" in log2.lower()
print("NEG rc:", rc2, "expect nonzero with undefined control sequence ->", "OK" if neg_ok else "FAIL")
shutil.rmtree(S)
print("SMOKE 091:", "PASS" if pos_ok and neg_ok else "FAIL")
sys.exit(0 if pos_ok and neg_ok else 1)
