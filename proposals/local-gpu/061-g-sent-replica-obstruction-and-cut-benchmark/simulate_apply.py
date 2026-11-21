"""Proposal 061: byte-exact apply simulation for the single splice into
chapters/appH-microscopic-proofs.tex. Does NOT write anything outside this
folder; it only predicts the post-state of the spliced file.

APPLY RULE (single-pass ascending splice, exactly one insertion):
  anchor A1 = b'scope-limited model.'  (offset 540076, unique, count 1);
  bytes [540096:540100] must equal b'\r\n\r\n';
  at offset 540100 the full line
    b'\section{Problem H: modular origin of the interpolating function}'
  must begin and that full header line must occur exactly once;
  insertion offset X = 540100;
  insert = bytes of insert-r1.tex, verified to contain no carriage return,
  LF->CRLF converted, right-stripped of CR/LF and re-terminated with
  b'\r\n\r\n';
  result = appH[:X] + insert + appH[X:].
Run: python -I simulate_apply.py
"""
import hashlib

path = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex"
b = open(path, 'rb').read()
assert len(b) == 560743, f"appH size {len(b)} != 560743"
assert hashlib.sha256(b).hexdigest() == \
    "fe02de8970b7dee8b0df8cad9a84ca557b1ecf41bc9d2b4984135a50b8faab8d"

A1 = b'scope-limited model.'
assert b.count(A1) == 1 and b.find(A1) == 540076
hdr = b'\section{Problem H: modular origin of the interpolating function}'
assert b.count(hdr) == 1 and b.find(hdr) == 540100
assert b[540096:540100] == b'\r\n\r\n'
X = 540100

ins = open('insert-r1.tex', 'rb').read()
assert b'\r' not in ins, "insert file must be pure LF"
ins = ins.rstrip(b'\n').replace(b'\n', b'\r\n') + b'\r\n\r\n'

out = b[:X] + ins + b[X:]
print("insert bytes:", len(ins), "sha256:", hashlib.sha256(ins).hexdigest())
print("predicted post-state:")
print("  size:", len(out))
print("  CRLF:", out.count(b'\r\n'))
print("  bare LF:", out.count(b'\n') - out.count(b'\r\n'))
print("  sha256:", hashlib.sha256(out).hexdigest())
# local context check
seg = out[540076:540076+len(A1)+len(ins)+40]
print("context head:", seg[:80])
print("context tail:", seg[-80:])
