# adopt_r2_108.py -- byte-adoption of gatekeeper-staged insert-corrected-gk.tex -> insert-r2.tex.
# Reads the gatekeeper candidate, asserts its triple and control bytes, writes insert-r2.tex in the
# proposal folder in binary mode (no retyping), re-reads, re-hashes, prints CANDIDATE MATCH.
import io, os, hashlib
repo = r"C:\Users\redgi\Projects\namcg-lab@gpu"
cand = os.path.join(repo, "scratch", "gk108", "insert-corrected-gk.tex")
dest = os.path.join(repo, "proposals", "108-a-map-noncentral-chart-select", "insert-r2.tex")
c = io.open(cand, "rb").read()
assert len(c) == 3072, "candidate size %d" % len(c)
assert hashlib.sha256(c).hexdigest()[:16] == "180b005188c8268a", "candidate sha16"
assert c.count(b"\r\n") == 1, "candidate CRLF %d" % c.count(b"\r\n")
bad = [b for b in c if b < 0x20 and b not in (0x0D, 0x0A)]
assert not bad, "control bytes below 0x20 other than CR/LF: %r" % bad[:8]
io.open(dest, "wb").write(c)
d = io.open(dest, "rb").read()
print("candidate: size=%d sha16=%s crlf=%d" % (len(c), hashlib.sha256(c).hexdigest()[:16], c.count(b"\r\n")))
print("insert-r2: size=%d sha16=%s crlf=%d" % (len(d), hashlib.sha256(d).hexdigest()[:16], d.count(b"\r\n")))
print("CANDIDATE MATCH", d == c)
print("head48=", repr(d[:48]))
print("tail40=", repr(d[-40:]))
