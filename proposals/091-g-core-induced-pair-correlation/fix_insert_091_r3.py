# fix_insert_091_r3.py - r3 surgery: insert-r2.tex -> insert-r3.tex per review-r2 finding 1(i)+(ii),
# corrected snippet verbatim. Two substring replacements, counts asserted. Never edits r1/r2 files.
# Run: python -I proposals/091-g-core-induced-pair-correlation/fix_insert_091_r3.py
import hashlib
D = "proposals/091-g-core-induced-pair-correlation/"
raw = open(D + "insert-r2.tex", "rb").read()
assert len(raw) == 3749 and hashlib.sha256(raw).hexdigest()[:8] == "ecc2b239"
old1 = b"In the rank-one edge-datum class of the Row length paragraph the slot vector is a gaussian column contraction with independent complex entries, and its normalised squared entries are exactly flat on the simplex at \(D=2\),"
new1 = b"In the rank-one edge-datum class of the Row length paragraph at constant variance on the contracted entries the slot vector is a gaussian column contraction with independent identically distributed complex entries, and its normalised squared entries are exactly flat on the simplex at \(D=2\),"
old2 = b"the rank-one slot class of the gaussian state model;"
new2 = b"the constant-profile rank-one slot subclass of the gaussian state model;"
assert raw.count(old1) == 1 and raw.count(old2) == 1
out = raw.replace(old1, new1).replace(old2, new2)
assert out.count(new1) == 1 and out.count(new2) == 1 and out.count(old1) == 0 and out.count(old2) == 0
out.decode("ascii")
ctl = [i for i, c in enumerate(out) if c < 0x20 and not (i >= len(out) - 2)]
assert ctl == [] and out[-2:] == b"\r\n" and out.count(b"\r\n") == 1 and out.count(b"\n") == 1
assert out.count(b"\(") == out.count(b"\)") == 35
assert out.count(b"\emph") == 1 and out.count(b"they close nothing in Problem~G.") == 1
assert out.count(b"Eigenvalue reduction of the edge Gram") == 1
assert b"identically distributed" in out
open(D + "insert-r3.tex", "wb").write(out)
print("insert-r3.tex size:", len(out), "delta vs r2:", len(out) - 3749)
print("sha256:", hashlib.sha256(out).hexdigest())
print("FIX R3 DONE")
