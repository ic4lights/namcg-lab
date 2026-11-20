# fix9_100.py -- patches hygiene_100.py (predecessor artifact, kept as v1 lineage). Bug in
# the post.adjacency check (line 52): it counted b"Problem~G.\r\n"+ins[:12], but the contract
# layout (line 43, matching the orchestrator byte contract: post = PRE[:756799] + ins + CRLF +
# PRE[756799:], cut immediately after the pin's \r\n\r\n) places the header after TWO CRLFs,
# so the single-CRLF pattern can never occur and the check was unsatisfiable for any insert.
# (Line 51's dead `seam` variable carried the same off-by-one-CRLF pattern; never checked.)
# Fix: require b"Problem~G.\r\n\r\n"+ins[:12] count == 1, and drop the dead line.
import hashlib, pathlib
base = pathlib.Path(__file__).resolve().parent
src = (base / "hygiene_100.py").read_bytes()
nl = b"\r\n" if b"\r\n" in src else b"\n"
lines = src.split(nl)
def find(pref):
    idx = [i for i, l in enumerate(lines) if l.startswith(pref)]
    assert len(idx) == 1, "prefix %r found %d times" % (pref, len(idx))
    return idx[0]
i = find(b"seam = b")
assert lines[i+1].startswith(b'chk("post.adjacency"')
lines[i:i+2] = [b'chk("post.adjacency", post.count(b"Problem~G.\\r\\n\\r\\n" + ins[:12]) == 1)']
out = nl.join(lines)
(base / "hygiene_100.py").write_bytes(out)
print("bytes=%d sha256=%s eol=%s lines=%d"
      % (len(out), hashlib.sha256(out).hexdigest(), "CRLF" if nl == b"\r\n" else "LF", len(lines)))
