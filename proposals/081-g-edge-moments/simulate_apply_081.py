"""081 simulate_apply_081: READ-ONLY byte contract for inserting insert-r1.tex
into chapters/appH-microscopic-proofs.tex immediately before the unique
line-start anchor '\\emph{Vacuum term.}' (live line 3177), i.e. after the 080
paragraph. No write is performed.

Run: python -I proposals/081-g-edge-moments/simulate_apply_081.py
Expected: PRE lines match the pinned live values, POST computed, last lines
'SIMULATED OK' and 'no write performed'. Nonzero exit with 'LIVE PRE DRIFT'
if the live file differs from the pins.
"""
import hashlib
import sys

APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/081-g-edge-moments/insert-r1.tex"
PIN_SIZE = 725541
PIN_SHA = "f8797f82be8d590929388ea9eeb48b1988c4ce164445a2be362c51242df63ea1"
PIN_CRLF = 3826
ANCHOR = b"\\emph{Vacuum term.}"
TAIL = (b"per-factor depths only in the fixed-depth regime of the selection-rule "
       b"reading, and they close nothing in Problem~G.")
HEADER = b"\\emph{Charge-to-edge moment identification in the Gaussian rank-one class.}"


def sha(b):
    return hashlib.sha256(b).hexdigest()


pre = open(APP, "rb").read()
ins = open(INS, "rb").read()
drift = []
if len(pre) != PIN_SIZE:
    drift.append(f"size {len(pre)} != {PIN_SIZE}")
if sha(pre) != PIN_SHA:
    drift.append(f"sha {sha(pre)} != {PIN_SHA}")
if pre.count(b"\r\n") != PIN_CRLF:
    drift.append(f"CRLF {pre.count(bytes([13,10]))} != {PIN_CRLF}")
if drift:
    print("LIVE PRE DRIFT: " + "; ".join(drift))
    sys.exit(1)
bare = pre.count(b"\n") - pre.count(b"\r\n")
assert bare == 0, f"bareLF {bare} != 0"
assert pre.count(ANCHOR) == 2, f"anchor count {pre.count(ANCHOR)}"  # L3006 and L3177
assert pre.count(TAIL) == 1, f"080 tail count {pre.count(TAIL)}"
assert pre.count(HEADER) == 0, f"header collision {pre.count(HEADER)}"
assert ins.count(b"\n") - ins.count(b"\r\n") == 0 and ins.endswith(b"\r\n")

off = pre.index(TAIL) + len(TAIL) + 4  # past the CRLFCRLF
assert pre[off:off + len(ANCHOR)] == ANCHOR
line = pre[:off].count(b"\r\n") + 1
assert line == 3177, line
block = ins + b"\r\n"  # paragraph + blank CRLF separator before anchor line
post = pre[:off] + block + pre[off:]
print(f"PRE size {len(pre)} sha256 {sha(pre)} CRLF {pre.count(bytes([13,10]))} bareLF {bare}")
print(f"insert bytes {len(ins)} sha256 {sha(ins)}")
print(f"anchor offset {off} line {line}")
print(f"POST size {len(post)} sha256 {sha(post)} "
      f"CRLF {post.count(bytes([13,10]))} bareLF {post.count(bytes([10]))-post.count(bytes([13,10]))}")
tail = post[off:off+len(block)+40]
assert post.count(ANCHOR) == 2 and post.count(HEADER) == 1
assert pre == post[:off] + post[off+len(block):]
print(f"POST context check: inserted block precedes anchor line: "
      f"{post[off+len(block):off+len(block)+len(ANCHOR)] == ANCHOR}")
print("SIMULATED OK")
print("no write performed")
