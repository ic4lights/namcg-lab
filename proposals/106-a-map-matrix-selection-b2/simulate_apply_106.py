# simulate_apply_106.py -- PIN-based byte-surgery SIMULATION of inserting insert-r1.tex
# into chapters/appH-microscopic-proofs.tex. Anchor: the end of the integrated
# order-Theta^2 dichotomy paragraph (which ends "does not close Problem~A.") followed by
# a blank line and "\paragraph{Missing step.}" (count 1 on the live tree). The PIN is
# built PROGRAMMATICALLY from the LIVE appH bytes (no hardcoded positions). The simulated
# output is written to scratch/sim/ ONLY. chapters/ is never written.
import hashlib
import os
import sys

A = r"chapters\appH-microscopic-proofs.tex"
INS = r"proposals\106-a-map-matrix-selection-b2\insert-r2.tex"
OUT = r"scratch\sim\appH_after_106.tex"
app = open(A, "rb").read()
ins = open(INS, "rb").read()
print("appH BEFORE: size %d sha256/16 %s CRLF %d" %
      (len(app), hashlib.sha256(app).hexdigest()[:16], app.count(b"\r\n")))
sent = b"does not close Problem~A."
tail = b"\paragraph{Missing step.}"
PIN = sent + b"\r\n\r\n" + tail
occ = [i for i in range(len(app)) if app.startswith(PIN, i)]
print("PIN occurrences:", len(occ))
assert len(occ) == 1, "PIN not unique"
p = occ[0]
print("PIN: size %d, context before: %r" % (len(PIN), app[p - 40:p]))
assert ins.endswith(b"\r\n") and ins.count(b"\r\n") == 1
new = (app[:p] + sent + b"\r\n\r\n" + ins + b"\r\n" + tail + app[p + len(PIN):])
assert new.count(b"\r\n") == app.count(b"\r\n") + 2
assert len(new) == len(app) + len(ins) + 2
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "wb").write(new)
print("simulated output (scratch only): %s" % OUT)
print("appH AFTER(simulated): size %d sha256/16 %s CRLF %d" %
      (len(new), hashlib.sha256(new).hexdigest()[:16], new.count(b"\r\n")))
print("live appH untouched: sha256/16 %s" % hashlib.sha256(
      open(A, "rb").read()).hexdigest()[:16])
sys.exit(0)
