# check_labels120.py -- grep-confirms every label the chain-120 payload will reference is
# defined exactly once book-wide (all *.tex in chapters/ plus root namcg-book7.tex), and
# that the \LUV macro used by the payload is defined. Run: python -I -B check_labels120.py
import io
import os

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
LABELS = ["eq:Smatrix", "eq:Smicro", "eq:Dmu-Phi", "eq:dictionary", "ass:dictionary",
          "eq:LUV-def", "eq:vacuum-manifold", "eq:V", "def:matrix-coords-ext",
          "sec:ch3-relate", "ass:emergent-op"]
paths = [os.path.join(REPO, "namcg-book7.tex")]
for root, dirs, fs in os.walk(os.path.join(REPO, "chapters")):
    for f in sorted(fs):
        if f.endswith(".tex"):
            paths.append(os.path.join(root, f))
cnt = {l: 0 for l in LABELS}
luvl = 0
for p in paths:
    t = io.open(p, encoding="utf-8", errors="replace").read()
    for l in LABELS:
        cnt[l] += t.count("\\label{" + l + "}")
    luvl += t.count("\\newcommand{\\LUV}")
bad = 0
for l in LABELS:
    ok = cnt[l] == 1
    bad += 0 if ok else 1
    print(("PASS " if ok else "FAIL ") + "label " + l + " defined " + str(cnt[l]) + "x")
ok = luvl >= 1
bad += 0 if ok else 1
print(("PASS " if ok else "FAIL ") + "\\LUV macro defs " + str(luvl))
print("LABELS " + ("OK 120" if bad == 0 else "PROBLEMS " + str(bad)))
