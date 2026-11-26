# simulate_apply_108_r1.py -- PRE/PIN/POST splice simulation for proposal 108 r1.
# READ-ONLY on chapters/ ; writes only scratch/sim/ under the repo root.
# Rebuilds the PIN from CURRENT live bytes at run time (no hard-coded offsets).
# Run:  python -I simulate_apply_108_r1.py
import io, os, hashlib, sys

repo = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
apph = os.path.join(repo, "chapters", "appH-microscopic-proofs.tex")
ins = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insert-r1.tex")
simdir = os.path.join(repo, "scratch", "sim")
os.makedirs(simdir, exist_ok=True)

data = io.open(apph, "rb").read()
payload = io.open(ins, "rb").read()

def triple(b):
    return (len(b), hashlib.sha256(b).hexdigest()[:16], b.count(b"\r\n"))

pre = triple(data)
print("PRE live appH: size=%d sha256/16=%s CRLF=%d" % pre)
print("PRE insert payload: size=%d sha256/16=%s CRLF=%d" % triple(payload))

HEAD = b"does not close Problem~A.\r\n\r\n"
TAIL = b"\\paragraph{Missing step.}"
PIN = HEAD + TAIL
short = b"does not close Problem~A."
c_pin = data.count(PIN)
c_short = data.count(short)
off = data.find(PIN)
print("PIN count=%d (short-string count=%d, offset=%d)" % (c_pin, c_short, off))
assert c_pin == 1, "PIN must be unique in live bytes"

new = data.replace(PIN, HEAD + payload + b"\r\n" + TAIL, 1)
post = triple(new)
print("POST preview: size=%d sha256/16=%s CRLF=%d" % post)
print("delta size=%d delta CRLF=%d (expect +%d / +2: payload plus one blank-line CRLF)" % (post[0]-pre[0], post[2]-pre[2], len(payload)+2))

outp = os.path.join(simdir, "appH_after_108_r1_preview.tex")
io.open(outp, "wb").write(new)
print("preview written: %s" % outp)

# undo check: remove the inserted block from the preview and compare to original
back = new.replace(HEAD + payload + b"\r\n" + TAIL, PIN, 1)
print("undo check (restores PRE bytes): %s" % (back == data))
print("POST PIN count=%d (expect 1: the unique PIN migrates to follow the new paragraph)" % new.count(PIN))
print("live appH unchanged after run: %s" % (io.open(apph, "rb").read() == data))
raise SystemExit(0)
