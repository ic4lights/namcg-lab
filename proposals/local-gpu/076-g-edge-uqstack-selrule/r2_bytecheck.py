# r2_bytecheck.py - fenced copy in proposal-r2.md vs insert-r1.tex minus terminal CRLF.
# Re-run: python -I proposals/076-g-edge-uqstack-selrule/r2_bytecheck.py  (repo root)
# Expected invariant output: BYTECHECK EQUAL, equal size and sha on both sides.
import hashlib

doc = open("proposals/076-g-edge-uqstack-selrule/proposal-r2.md", "rb").read()
ins = open("proposals/076-g-edge-uqstack-selrule/insert-r1.tex", "rb").read()
assert ins.endswith(b"\r\n") and ins.count(b"\r") == 1
want = ins[:-2]

OPEN = b"```latex\r\n"
CLOSE = b"\r\n```"
i = doc.rfind(OPEN)
assert i != -1, "no ```latex fence found"
j = doc.find(CLOSE, i + len(OPEN))
assert j != -1, "no closing fence found"
assert doc.find(OPEN, i + 1) == -1, "more than one latex fence (ambiguous)"
fenced = doc[i + len(OPEN): j]

s1, s2 = hashlib.sha256(fenced).hexdigest(), hashlib.sha256(want).hexdigest()
print(f"fenced   size {len(fenced)} sha256 {s1}")
print(f"insert-2 size {len(want)} sha256 {s2}")
assert fenced == want, "BYTECHECK MISMATCH"
print("BYTECHECK EQUAL")
