# apply_trims120.py -- one-shot: applies trims.json replacements to gen_payload_120.py,
# each exactly once. Run: python -I -B apply_trims120.py  (then rerun gen_payload_120.py twice)
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
gp = os.path.join(HERE, "gen_payload_120.py")
tp = os.path.join(HERE, "trims.json")
op = os.path.join(HERE, "insert-commutator-lift-r1.tex")
b = io.open(gp, "rb").read()
pairs = json.load(io.open(tp, encoding="utf-8"))
for old, new in pairs:
    ob = old.encode("utf-8")
    nb = new.encode("utf-8")
    assert b.count(ob) == 1, "trim search not unique/found: %r" % old[:60]
    b = b.replace(ob, nb)
io.open(gp, "wb").write(b)
if os.path.exists(op):
    os.remove(op)
print("TRIMS APPLIED %d" % len(pairs))
