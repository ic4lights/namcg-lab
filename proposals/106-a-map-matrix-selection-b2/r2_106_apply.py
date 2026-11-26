# r2_106_apply.py -- mechanically applies gatekeeper findings F1/F2 from
# proposals/106-a-map-matrix-selection-b2/review-r1.md to insert-r1.tex, producing
# insert-r2.tex. Replacement strings are extracted PROGRAMMATICALLY from the ```latex
# fence of the review; nothing of the gatekeeper's text is retyped here.
# Run from repo root: python -I scratch/r2_106_apply.py
import hashlib
import sys

REVIEW = r"proposals\106-a-map-matrix-selection-b2\review-r1.md"
INS1 = r"proposals\106-a-map-matrix-selection-b2\insert-r1.tex"
OUT = r"proposals\106-a-map-matrix-selection-b2\insert-r2.tex"
CAND = r"scratch\gk106\insert-r2-candidate.tex"
R1_SHA16 = "e10d4960e7777f54"

def sha16(b):
    return hashlib.sha256(b).hexdigest()[:16]

# --- parse the gatekeeper fence -------------------------------------------------
rev = open(REVIEW, "rb").read()
open_tok = b"```latex"
i = rev.index(open_tok)
j = rev.index(b"```", i + len(open_tok))
fence = rev[i + len(open_tok):j]
# review file is LF-only; strip only a possible trailing CR per line
lines = [ln[:-1] if ln.endswith(b"\r") else ln for ln in fence.split(b"\n")]

def count_marker(tag):
    return sum(1 for ln in lines if ln == tag)

for tag in (b"% F1: replace", b"% with", b"% F2: replace"):
    n = count_marker(tag)
    exp = 2 if tag == b"% with" else 1
    assert n == exp, "marker %r count %d != %d" % (tag, n, exp)

pairs = {}          # key -> [old, new]
cur = None
want = None
for ln in lines:
    if ln == b"% F1: replace":
        cur, want = "F1", "old"
    elif ln == b"% F2: replace":
        cur, want = "F2", "old"
    elif ln == b"% with":
        want = "new"
    elif ln.strip() and want:
        # text lines in the fence carry no leading indentation (verified)
        assert ln[:1] not in (b" ", b"\t"), "unexpected indent: %r" % ln[:20]
        pairs.setdefault(cur, {})[want] = ln
        want = None

assert set(pairs) == {"F1", "F2"} and all(
    set(v) == {"old", "new"} for v in pairs.values()), "fence parse incomplete"
old1, new1 = pairs["F1"]["old"], pairs["F1"]["new"]
old2, new2 = pairs["F2"]["old"], pairs["F2"]["new"]
print("fence parsed: old1/new1/old2/new2 = %d/%d/%d/%d B" %
      (len(old1), len(new1), len(old2), len(new2)))

# --- load insert-r1 and verify provenance ---------------------------------------
ins1 = open(INS1, "rb").read()
full = hashlib.sha256(ins1).hexdigest()
print("insert-r1: %d B sha256 %s" % (len(ins1), full))
assert full[:16] == R1_SHA16, "insert-r1 sha256/16 mismatch"
assert ins1.count(old1) == 1, "old1 not unique in insert-r1"
assert ins1.count(old2) == 1, "old2 not unique in insert-r1"

# --- apply (single occurrence each -> order does not matter) --------------------
new = ins1.replace(old1, new1).replace(old2, new2)
assert new.count(old1) == 0 and new.count(old2) == 0
assert new.count(new1) == 1 and new.count(new2) == 1
assert new.count(b"\n") == 1 and new.count(b"\r") == 1 and new.endswith(b"\r\n"), \
    "result must remain exactly one CRLF-terminated line"

with open(OUT, "wb") as f:
    f.write(new)
back = open(OUT, "rb").read()
assert back == new, "written file differs from computed bytes"

# --- compare with the gatekeeper byte-staged candidate --------------------------
cand = open(CAND, "rb").read()
print("insert-r2 : %d B sha256 %s" % (len(new), hashlib.sha256(new).hexdigest()))
print("candidate : %d B sha256 %s" % (len(cand), hashlib.sha256(cand).hexdigest()))
if new == cand:
    print("CANDIDATE MATCH: True")
else:
    k = min(len(new), len(cand))
    off = next((p for p in range(k) if new[p] != cand[p]), k)
    lo, hi = max(0, off - 40), min(max(len(new), len(cand)), off + 40)
    print("MISMATCH at offset %d (r2 %d B vs candidate %d B)" % (off, len(new), len(cand)))
    print("  r2  ctx:", repr(new[lo:hi]))
    print("  cnd ctx:", repr(cand[lo:hi]))
    sys.exit(1)
sys.exit(0)
