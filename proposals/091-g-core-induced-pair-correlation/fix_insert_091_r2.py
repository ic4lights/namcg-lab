# fix_insert_091_r2.py - F1 byte surgery: insert-r1.tex -> insert-r2.tex. Deletes the 24-byte
# phrase "identically distributed " from the rank-one sentence only. Never touches r1 files.
# Run: python -I proposals/091-g-core-induced-pair-correlation/fix_insert_091_r2.py
import hashlib
D = "proposals/091-g-core-induced-pair-correlation/"
raw = open(D + "insert-r1.tex", "rb").read()
assert len(raw) == 3773, "frozen r1 size"
assert hashlib.sha256(raw).hexdigest()[:8] == "3e471d12", "frozen r1 sha8"
tgt = b"independent identically distributed complex entries"
assert raw.count(tgt) == 1, "target phrase count"
iid_keep = b"independent identically distributed complex gaussians"
assert raw.count(iid_keep) == 1, "A-block iid phrase must stay"
out = raw.replace(tgt, b"independent complex entries")
assert len(out) == 3749, "r2 size"
assert out.count(b"identically distributed") == 1, "exactly one remaining (the gaussians one)"
out.decode("ascii")
assert out.count(b"\(") == out.count(b"\)") == 35, "paren balance"
assert out.count(b"they close nothing in Problem~G.") == 1, "close idiom"
assert out.count(b"Eigenvalue reduction of the edge Gram") == 1, "header"
assert out.count(b"\r\n") == 1 and out.count(b"\n") == 1, "single CRLF line"
open(D + "insert-r2.tex", "wb").write(out)
print("insert-r2.tex size:", len(out), "sha256:", hashlib.sha256(out).hexdigest())
print("FIX DONE")
