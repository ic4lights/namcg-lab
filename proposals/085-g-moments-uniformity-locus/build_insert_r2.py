import hashlib

# Build insert-r2.tex from insert-r1.tex bytes with exactly two byte-surgery
# edits required by review-r1: F1 (fixed-total-weight qualifier) and F4
# ("row length" -> "slot count"). Every other byte is preserved, so the diff
# r1 -> r2 is exactly the two corrected clauses.
SRC = "proposals/085-g-moments-uniformity-locus/insert-r1.tex"
DST = "proposals/085-g-moments-uniformity-locus/insert-r2.tex"

b = open(SRC, "rb").read()
h = hashlib.sha256(b).hexdigest()
assert len(b) == 3371 and h[:8] == "994032c1", (len(b), h[:8])

edits = [
    (b"their effective dimension stays strictly below the row length at every cutoff",
     b"their effective dimension stays strictly below the slot count at every cutoff"),
    (b"their frame-averaged coupling vanishes as the slot count grows",
     b"their frame-averaged coupling at fixed total weight \\(W\\) vanishes as the slot count grows"),
]
for old, new in edits:
    assert b.count(old) == 1, (b.count(old), old[:48])
    b = b.replace(old, new)

assert b.count(b"\r\n") == 1 and b.endswith(b"\r\n")
assert b"\r" not in b[:-2] and b"\n" not in b[:-2]
open(DST, "wb").write(b)
print("wrote %s size %d sha256 %s" % (DST, len(b), hashlib.sha256(b).hexdigest()))
