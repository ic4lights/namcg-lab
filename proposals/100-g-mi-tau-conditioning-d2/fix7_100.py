# fix7_100.py -- sole byte authority for mc100s.py v5. Final eh_ref bug: consts always uses
# gl(400,0,0.5) u-nodes (400 of them), but eh_ref looped `for k in range(nU)` with nU=240,
# so the reference E[h(rho)] integrated f_u only over the first 240 of 400 nodes (u < ~0.30),
# dropping the upper-u half of the distribution -- hence refs -0.7467 / -242 while every
# other test passed. Fix: loop over the actual number of u nodes returned by consts.
import hashlib, pathlib
base = pathlib.Path(__file__).resolve().parent
src = (base / "mc100s.py").read_bytes()
nl = b"\r\n" if b"\r\n" in src else b"\n"
lines = src.split(nl)
def find(pref):
    idx = [i for i, l in enumerate(lines) if l.startswith(pref)]
    assert len(idx) == 1, "prefix %r found %d times" % (pref, len(idx))
    return idx[0]
i = find(b"    for k in range(nU):")
lines[i] = b"    for k in range(um.shape[0]):"
out = nl.join(lines)
(base / "mc100s.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF", len(lines)))
