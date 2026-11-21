# retarget_106.py -- point the insert-path constants of hygiene_106.py and
# simulate_apply_106.py from insert-r1.tex to insert-r2.tex.
# Edits ONLY the F / INS constant lines. Backslash-free byte patterns throughout.
import sys

H = r"proposals/106-a-map-matrix-selection-b2/hygiene_106.py"
S = r"proposals/106-a-map-matrix-selection-b2/simulate_apply_106.py"

def retarget(path, prefix):
    b = open(path, "rb").read()
    eol = b"\r\n" if b"\r\n" in b else b"\n"
    lines = b.split(eol)
    hits = [k for k, ln in enumerate(lines) if ln.startswith(prefix)]
    assert len(hits) == 1, "%s: prefix count %d" % (path, len(hits))
    k = hits[0]
    old = lines[k]
    assert b.count(b"insert-r1.tex" + b'"') >= 1
    assert old.count(b"insert-r1.tex") == 1 and old.endswith(b'"'), repr(old)
    new = old.replace(b"insert-r1.tex", b"insert-r2.tex")
    assert new != old
    lines[k] = new
    open(path, "wb").write(eol.join(lines))
    return new

nh = retarget(H, b"F = r")
ns = retarget(S, b"INS = r")
print("hygiene  F   =", nh.decode())
print("simulate INS =", ns.decode())
# re-read and prove the constants actually changed
for path, prefix in ((H, b"F = r"), (S, b"INS = r")):
    bb = open(path, "rb").read()
    ln = [l for l in bb.split(b"\n") if l.startswith(prefix)][0]
    assert b"insert-r2.tex" in ln and b"insert-r1.tex" not in ln.rstrip(b"\r"), path
    print("verified-in-file:", path.decode())
sys.exit(0)
