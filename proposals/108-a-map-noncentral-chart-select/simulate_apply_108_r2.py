# simulate_apply_108_r2.py -- PRE/PIN/POST splice simulation for proposal 108 r2 (adopted insert-r2.tex).
# READ-ONLY on chapters/ ; writes only scratch/sim/appH_after_108_r2_preview.tex.
# Rebuilds the PIN from CURRENT live bytes at run time (no hard-coded offsets).
# Run from repo root:  python -I proposals/108-a-map-noncentral-chart-select/simulate_apply_108_r2.py
import io, os, hashlib
here = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(os.path.join(here, "..", ".."))
apph = os.path.join(repo, "chapters", "appH-microscopic-proofs.tex")
ins = os.path.join(here, "insert-r2.tex")
simdir = os.path.join(repo, "scratch", "sim")
os.makedirs(simdir, exist_ok=True)
def triple(b):
    return (len(b), hashlib.sha256(b).hexdigest()[:16], b.count(b"\r\n"))
data = io.open(apph, "rb").read()
payload = io.open(ins, "rb").read()
pre = triple(data)
print("PRE live appH: size=%d sha256/16=%s CRLF=%d" % pre)
assert pre == (812227, "698f38979140770d", 3876), "live appH triple unexpected"
print("PRE insert payload: size=%d sha256/16=%s CRLF=%d" % triple(payload))
assert triple(payload) == (3072, "180b005188c8268a", 1), "insert-r2.tex triple unexpected"
HEAD = b"does not close Problem~A.\r\n\r\n"
TAIL = b"\paragraph{Missing step.}"
PIN = HEAD + TAIL
c_pin = data.count(PIN)
off = data.find(PIN)
print("PIN count=%d (short-string count=%d, offset=%d)" % (c_pin, data.count(b"does not close Problem~A."), off))
assert c_pin == 1, "PIN must be unique in live bytes"
INSB = HEAD + payload + b"\r\n" + TAIL
new = data.replace(PIN, INSB, 1)
post = triple(new)
print("POST preview (computed): size=%d sha256/16=%s CRLF=%d" % post)
exp = (815301, "316c7b6f549ed660", 3878)
print("POST == gatekeeper-certified %s: %s" % (exp, post == exp))
if post != exp:
    print("!!!! LOUD FLAG: POST differs from gatekeeper certification ---- CHECK ----")
print("delta size=%d delta CRLF=%d (payload %d bytes + one blank-line CRLF pair)" % (post[0]-pre[0], post[2]-pre[2], len(payload)))
outp = os.path.join(simdir, "appH_after_108_r2_preview.tex")
io.open(outp, "wb").write(new)
print("preview written: %s" % outp)
back = new.replace(INSB, PIN, 1)
print("undo check (restores PRE bytes): %s" % (back == data))
print("POST PIN count=%d (expect 1)" % new.count(PIN))
print("live appH unchanged after run: %s" % (io.open(apph, "rb").read() == data))
