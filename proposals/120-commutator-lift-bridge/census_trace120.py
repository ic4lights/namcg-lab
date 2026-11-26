# census_trace120.py -- trace-macro census on live bytes (appH + book-wide chapters/)
# and payload census for the integrated 119 paragraph (delta attribution).
import glob
import io
import os
import re

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

def txt(p):
    return io.open(p, "r", encoding="utf-8", newline="").read()

def census(t):
    n1 = len(re.findall(r"\\operatorname\{Tr\}", t))
    n2 = len(re.findall(r"\\mathrm\{Tr\}", t))
    n3 = len(re.findall(r"\\Tr(?![A-Za-z])", t))
    return n1, n2, n3

ap = os.path.join(REPO, "chapters", "appH-microscopic-proofs.tex")
t = txt(ap)
print("appH: operatornameTr=%d mathrmTr=%d standaloneTr=%d" % census(t))

tot1 = tot2 = tot3 = 0
for f in sorted(glob.glob(os.path.join(REPO, "chapters", "*.tex"))):
    a, b, c = census(txt(f))
    tot1 += a
    tot2 += b
    tot3 += c
print("chapters book-wide: operatornameTr=%d mathrmTr=%d standaloneTr=%d" % (tot1, tot2, tot3))

pay = os.path.join(REPO, "proposals", "119-d1-selection-underdetermination",
                   "insert-overdetermination-r1.tex")
p = txt(pay)
print("integrated-119 payload: operatornameTr=%d mathrmTr=%d standaloneTr=%d" % census(p))

# pre-integration appH reconstruction: live minus the 119 payload block
anchor = "\\section{Problem E: signature}"
assert t.count(anchor) == 1
pre = t.replace(p + "\r\n" + anchor, anchor, 1)
assert len(pre) == len(t) - len(p) - 2, "119 block not cleanly removable: %d %d %d" % (
    len(pre), len(t), len(p))
print("appH minus 119 payload (pre-integration reconstruction): operatornameTr=%d mathrmTr=%d standaloneTr=%d"
      % census(pre))
