# r2_insert_patch.py - asserted byte replacement for finding 1 (review-r1.md).
# Re-run: python -I proposals/076-g-edge-uqstack-selrule/r2_insert_patch.py  (from repo root)
# Expected invariant output: PATCH OK, then old/new size and sha256 of insert-r1.tex.
import hashlib, sys

P = "proposals/076-g-edge-uqstack-selrule/insert-r1.tex"

OLD = (b"Under the hypotheses of the selection rule transplanted in the first of the four "
       b"preceding paragraphs, the U(q) repetition of that rule selects a stacked diagram only "
       b"when the nonzero spectrum of the classical edge charge has multiplicity q, and within "
       b"the supplied class of Gaussian states this is a property of the state, not of the "
       b"background alone:")

NEW = (b"Under the hypotheses of the selection rule transplanted in the first of the four "
       b"preceding paragraphs, and with its U(q) repetition supplied as a further conditional "
       b"reading, in which multiplicity \\(q\\) of the nonzero spectrum of the classical edge "
       b"charge is read as \\(q\\) equal rows, that reading fixes a stacked diagram only when "
       b"that spectral condition holds, and within the supplied class of Gaussian states the "
       b"multiplicity is a property of the state, not of the background alone:")

data = open(P, "rb").read()
old_size = len(data)
old_sha = hashlib.sha256(data).hexdigest()

n = data.count(OLD)
assert n == 1, f"OLD span count {n} != 1; aborting, file unchanged"
# Terminal CRLF preservation check: exactly one CR, at end, followed by LF.
assert data.count(b"\r") == 1 and data.endswith(b"\r\n") and b"\n" not in data[:-2], "CRLF contract broken pre-patch"
# ASCII only
assert all(b < 128 for b in data), "non-ASCII byte present pre-patch"

new = data.replace(OLD, NEW, 1)
assert new.count(NEW) == 1 and new.count(OLD) == 0
assert new.count(b"\r") == 1 and new.endswith(b"\r\n") and b"\n" not in new[:-2], "CRLF contract broken post-patch"
assert all(b < 128 for b in new), "non-ASCII byte present post-patch"
# Colon-onward contract: the byte immediately after NEW must be the original ": for q coincident copies"
tailpos = new.find(NEW) + len(NEW)
assert new[tailpos:tailpos + len(b" for q coincident copies")] == b" for q coincident copies", "colon-onward contract broken"

open(P, "wb").write(new)
print("PATCH OK")
print(f"old size {old_size} sha256 {old_sha}")
print(f"new size {len(new)} sha256 {hashlib.sha256(new).hexdigest()}")
