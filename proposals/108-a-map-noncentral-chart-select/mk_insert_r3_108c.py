# mk_insert_r3_108c.py -- insert-r3.tex := insert-r2.tex + math delimiters ONLY.
# No regex and no backslash string literals (built from 0x5C) to avoid transfer mangling.
# Char-level mode toggle on backslash-paren delimiters; text islands = maximal whitespace-joined
# runs of mathy tokens (start with backslash, or contain ^ _ $), excluding SAFE text commands.
import io, os, hashlib
BS = chr(0x5C)
OPEN, CLOSE = BS + "(", BS + ")"
SAFE = (BS + "paragraph",)
here = os.path.dirname(os.path.abspath(__file__))
r2 = io.open(os.path.join(here, "insert-r2.tex"), "rb").read()
assert (len(r2), hashlib.sha256(r2).hexdigest()[:16], r2.count(b"\r\n")) == (3072, "180b005188c8268a", 1)
assert not [b for b in r2 if b < 0x20 and b not in (0x0D, 0x0A)]
txt = r2.decode("ascii")
assert txt.count(OPEN) == txt.count(CLOSE) == 25
segs, mode, start, i = [], 0, 0, 0
while i < len(txt):
    if txt[i] == BS and i + 1 < len(txt) and txt[i + 1] in "()":
        segs.append((mode, txt[start:i]))
        mode ^= 1; start = i + 2; i += 2; continue
    i += 1
assert mode == 0 and start <= len(txt)
segs.append((mode, txt[start:]))
def tokens(s):
    out, cur, ws = [], "", False
    for c in s:
        w = c.isspace()
        if cur and (w != ws):
            out.append(cur); cur = ""
        cur += c; ws = w
    if cur: out.append(cur)
    return out
def mathy(t):
    if t[0] == BS:
        return not any(t.startswith(s) for s in SAFE)
    return any(c in t for c in "^_$")
out, wraps = [], []
for md, s in segs:
    if md == 1:
        out.append(s); continue
    toks, buf, j = tokens(s), "", 0
    while j < len(toks):
        t = toks[j]
        if not t.isspace() and mathy(t):
            buf = buf + t if buf else t
        elif buf and t.isspace() and j + 1 < len(toks) and not toks[j + 1].isspace() and mathy(toks[j + 1]):
            buf += t
        elif buf:
            wraps.append(buf); out.append(OPEN + buf + CLOSE); buf = ""; out.append(t)
        else:
            out.append(t)
        j += 1
    if buf:
        wraps.append(buf); out.append(OPEN + buf + CLOSE)
r3 = "".join(out).encode("ascii")
bb, bo, bc = b"\x5c", b"\x5c(", b"\x5c)"
assert r3.replace(bo, b"").replace(bc, b"") == r2.replace(bo, b"").replace(bc, b""), "NORMALIZATION TEST FAILED"
assert len(r3) == len(r2) + 2 * len(wraps)
assert r3.count(bo.encode("ascii")) == 25 + len(wraps) and r3.count(bc.encode("ascii")) == 25 + len(wraps)
assert r3.count(b"\r\n") == 1 and not [b for b in r3 if b < 0x20 and b not in (0x0D, 0x0A)]
io.open(os.path.join(here, "insert-r3.tex"), "wb").write(r3)
print("wraps added =", len(wraps))
for w in wraps: print("WRAPPED:", repr(w))
print("NORMALIZATION TEST PASS")
print("r3: size=%d sha16=%s crlf=%d delta=%d" % (len(r3), hashlib.sha256(r3).hexdigest()[:16], r3.count(b"\r\n"), len(r3) - len(r2)))
