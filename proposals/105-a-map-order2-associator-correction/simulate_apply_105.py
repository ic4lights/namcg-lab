# simulate_apply_105.py -- PIN-based byte-surgery simulation of inserting insert-r2.tex
# (r2 line; r1 superseded). r2 expected POST per review-r1.md: 807971/53c1c478ae1a79ff/3872.
# into chapters/appH-microscopic-proofs.tex. The PIN and the insertion point are built
# PROGRAMMATICALLY from the LIVE appH bytes (never hardcoded positions). The simulated
# output is written to scratch/sim/ ONLY. chapters/ is never written.
import hashlib
import os
import sys

A = r"chapters\appH-microscopic-proofs.tex"
INS = r"proposals\105-a-map-order2-associator-correction\insert-r2.tex"
OUT = r"scratch\sim\appH_after_105.tex"
app = open(A, "rb").read()
ins = open(INS, "rb").read()
print("appH BEFORE: size %d sha256/16 %s CRLF %d" %
      (len(app), hashlib.sha256(app).hexdigest()[:16], app.count(b"\r\n")))
tail = b"\\paragraph{Missing step.}"
sent = b"they do not derive Assumption~\\ref{ass:dictionary}."
occ = [i for i in range(len(app)) if app.startswith(sent, i)]
print("sentence occurrences:", len(occ))
assert len(occ) == 1, "anchor sentence not unique"
i = occ[0]
PIN = app[i:app.find(tail, i) + len(tail)]
print("PIN: size %d, whole-line context: preceded by %r" %
      (len(PIN), app[i - 30:i]))
n_pin = app.count(PIN)
print("PIN count:", n_pin)
assert n_pin == 1, "PIN not unique"
assert ins.endswith(b"\r\n") and ins.count(b"\r\n") == 1
p = app.find(PIN)
new = (app[:p] + sent + b"\r\n\r\n" + ins + b"\r\n" +
       PIN[len(sent) + 4:] + app[p + len(PIN):])
assert new.count(b"\r\n") == app.count(b"\r\n") + 2
assert len(new) == len(app) + len(ins) + 2
assert len(new) == 807971 and hashlib.sha256(new).hexdigest()[:16] == "53c1c478ae1a79ff", \
    "POST differs from review-r1.md r2 contract (807971/53c1c478ae1a79ff)"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "wb").write(new)
print("simulated output (scratch only): %s" % OUT)
print("appH AFTER(simulated): size %d sha256/16 %s CRLF %d" %
      (len(new), hashlib.sha256(new).hexdigest()[:16], new.count(b"\r\n")))
print("live appH untouched: sha256/16 %s" % hashlib.sha256(
      open(A, "rb").read()).hexdigest()[:16])
sys.exit(0)
