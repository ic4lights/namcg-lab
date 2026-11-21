# mk_hygiene_r2_108.py -- retarget hygiene_108_r1.py to insert-r2.tex by byte substitution only.
# Replaces the two filename tokens; the 21 checks stay code-identical. Writes hygiene_108_r2.py.
import io, os, hashlib
here = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(here, "hygiene_108_r1.py"), "rb").read()
out = src.replace(b"hygiene_108_r1", b"hygiene_108_r2").replace(b"insert-r1.tex", b"insert-r2.tex")
assert b"insert-r1" not in out and b"hygiene_108_r1" not in out
assert out.count(b"insert-r2.tex") == src.count(b"insert-r1.tex")
dest = os.path.join(here, "hygiene_108_r2.py")
io.open(dest, "wb").write(out)
d = io.open(dest, "rb").read()
print("hygiene_108_r2.py: size=%d sha16=%s crlf=%d" % (len(d), hashlib.sha256(d).hexdigest()[:16], d.count(b"\r\n")))
