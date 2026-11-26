# fix3_100.py -- sole byte authority for mc100s.py v2. numpy leggauss returns (nodes, weights)
# (pinned empirically: n=200 weights sum to 2.0, nodes antisymmetric); mc100s.gl returns
# lo+(hi-lo)*(t+1)/2 FIRST = nodes. The v1 unpacks wu,um / wx,xm / wt,tl / wxq,xq held nodes
# where weights were needed (and vice versa), which is why v1 reference values were garbage
# while the direct simulation rows (which do not use gl) matched the pipeline. Fix all four.
import hashlib, pathlib
base = pathlib.Path(__file__).resolve().parent
src = (base / "mc100s.py").read_bytes()
nl = b"\r\n" if b"\r\n" in src else b"\n"
lines = src.split(nl)
def find(pref):
    idx = [i for i, l in enumerate(lines) if l.startswith(pref)]
    assert len(idx) == 1, "prefix %r found %d times" % (pref, len(idx))
    return idx[0]
i = find(b"    wu, um = gl(400")
lines[i] = b"    um, wu = gl(400, 0, 0.5)   # gl returns (nodes, weights)"
j = find(b"    wx, xm = gl(nX")
lines[j] = b"    xm, wx = gl(nX, 0, 1); tl, wt = gl(nT, 0, 60)"
k = find(b"        wxq, xq = gl(200")
lines[k] = b"        xq, wxq = gl(200, 0, 1)"
out = nl.join(lines)
(base / "mc100s.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF", len(lines)))
