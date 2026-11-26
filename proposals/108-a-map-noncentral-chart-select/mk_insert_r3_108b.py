# mk_insert_r3_108b.py -- insert-r3.tex := insert-r2.tex + math delimiters ONLY (fixed island join).
# Text/math regions parsed by \( \) toggling. In TEXT regions, maximal whitespace-joined runs of
# mathy tokens (contain ^ _ $ or a backslash-command outside SAFE) are wrapped in \( ... \).
import io, os, hashlib, re
here = os.path.dirname(os.path.abspath(__file__))
r2 = io.open(os.path.join(here, "insert-r2.tex"), "rb").read()
assert (len(r2), hashlib.sha256(r2).hexdigest()[:16], r2.count(b"\r\n")) == (3072, "180b005188c8268a", 1)
assert not [b for b in r2 if b < 0x20 and b not in (0x0D, 0x0A)], "control bytes below 0x20"
txt = r2.decode("ascii")
parts = re.split(r"(\\(|\\))", txt)
mode, segs, i = 0, [], 0
while i < len(parts):
    p = parts[i]
    if p == r"\(":
        assert mode == 0; mode = 1; i += 1; continue
    if p == r"\)":
        assert mode == 1; mode = 0; i += 1; continue
    if p: segs.append((mode, p))
    i += 1
assert mode == 0, "unclosed math at EOF"
SAFE = (r"\paragraph",)
def mathy(tok):
    if tok.startswith("\\"):
        return not any(tok.startswith(s) for s in SAFE)
    return any(c in tok for c in "^_$")
out, wraps = [], []
for md, s in segs:
    if md == 1:
        out.append(s); continue
    toks = re.findall(r"\S+|\s+", s)
    res, buf, j = [], "", 0
    while j < len(toks):
        t = toks[j]
        if mathy(t):
            buf = buf + t if buf else t
        elif buf and t.isspace() and j + 1 < len(toks) and mathy(toks[j + 1]):
            buf += t
        elif buf:
            wraps.append(buf); res.append(r"\(" + buf + r"\)"); buf = ""; res.append(t)
        else:
            res.append(t)
        j += 1
    if buf:
        wraps.append(buf); res.append(r"\(" + buf + r"\)")
    out.append("".join(res))
r3txt = "".join(out)
r3 = r3txt.encode("ascii")
strip = lambda b: b.replace(b"\(", b"").replace(b"\)", b"")
assert strip(r3) == strip(r2), "NORMALIZATION TEST FAILED"
assert len(r3) == len(r2) + 2 * len(wraps)
assert r3.count(b"\(") == r2.count(b"\(") + len(wraps) and r3.count(b"\)") == r2.count(b"\)") + len(wraps)
assert r3.count(b"\r\n") == 1 and not [b for b in r3 if b < 0x20 and b not in (0x0D, 0x0A)]
io.open(os.path.join(here, "insert-r3.tex"), "wb").write(r3)
print("wraps added = %d" % len(wraps))
for w in wraps: print("WRAPPED:", repr(w))
print("NORMALIZATION TEST PASS (stripped r3 == stripped r2)")
print("r3: size=%d sha16=%s crlf=%d  (delta=%d)" % (len(r3), hashlib.sha256(r3).hexdigest()[:16], r3.count(b"\r\n"), len(r3) - len(r2)))
