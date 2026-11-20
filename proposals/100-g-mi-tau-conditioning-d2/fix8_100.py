# fix8_100.py -- sole byte authority for mc100s.py v6. Root cause of the last eh_ref error:
# gz = wt*tl**(al-1)*exp(-tl)/lgamma(al) divides by LOG-gamma ln Gamma(4) = 1.7918 instead of
# Gamma(4) = 6, inflating every gz by 6/ln(6) = 3.3487 (exactly the observed 3.34866 ratio in
# the standalone check: int t^3 e^-t on (0,60) = 6.000000 to 1e-14, gz sum = 3.34866).
# Fix: divide by gamma(al).
import hashlib, pathlib
base = pathlib.Path(__file__).resolve().parent
src = (base / "mc100s.py").read_bytes()
nl = b"\r\n" if b"\r\n" in src else b"\n"
lines = src.split(nl)
def find(pref):
    idx = [i for i, l in enumerate(lines) if l.startswith(pref)]
    assert len(idx) == 1, "prefix %r found %d times" % (pref, len(idx))
    return idx[0]
i = find(b"from math import lgamma")
lines[i] = b"from math import gamma"
j = find(b"        gz = wt*tl**(al-1)")
lines[j] = b"        gz = wt*tl**(al-1)*np.exp(-tl)/gamma(al)"
out = nl.join(lines)
(base / "mc100s.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF", len(lines)))
