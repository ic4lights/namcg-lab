# make_payload_127.r2.py - mechanical r2 revision for proposal 127.
# Applies review-r1.md REQUIRED REVISIONS R1 (payload-P1) and R2 (payload-P2)
# byte-mechanically: no other edits. Never overwrites the frozen r1 files.
# Run: python -I make_payload_127.r2.py
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sha1_12(b):
    return hashlib.sha1(b).hexdigest()[:12]


def replace_once(data, old, new, tag):
    n = data.count(old)
    if n != 1:
        raise AssertionError(
            "%s: old string count == %d (expected exactly 1)" % (tag, n))
    return data.replace(old, new, 1)


R1_OLD = (r"to \(K^{\mu\nu}=\Theta^{\alpha\mu}g^{(0)}_{\alpha\beta}"
          r"\Theta^{\beta\nu}\) of Definition~\ref{def:matrix-coords-ext},"
          r" which is congruent to")
R1_NEW = (r"to the background-form \(K^{\mu\nu}="
          r"\Theta^{\alpha\mu}g^{(0)}_{\alpha\beta}\Theta^{\beta\nu}\) of the"
          r" kinetic tensor of Definition~\ref{def:matrix-coords-ext} (the"
          r" induced tensor \(g_{\alpha\beta}\) of the definition replaced by"
          r" \(g^{(0)}_{\alpha\beta}\)), which is congruent to")
R2_OLD = r"costs: complex self-dual \(\Theta\)"
R2_NEW = r"costs: complex (anti-)self-dual \(\Theta\)"

JOBS = [
    # (r1 name, r2 name, old, new, r1 sha1_12, r1 size, r2 sha1_12, r2 size)
    ("payload-P1.txt", "payload-P1-r2.txt", R1_OLD, R1_NEW,
     "8df7a7f42a97", 871, "6dd693e2cf0b", 1010),
    ("payload-P2.txt", "payload-P2-r2.txt", R2_OLD, R2_NEW,
     "e30a1cd68ed6", 3043, "73aca8c862ec", 3050),
]

# --- CONTROL (house rule: prove the uniqueness guard fires) ---------------
probe = b"this-string-must-never-occur-in-127-r1-bytes-XYZQ"
try:
    with open(os.path.join(HERE, "payload-P1.txt"), "rb") as f:
        replace_once(f.read(), probe, b"X", "control-probe")
    print("CONTROL FAIL: uniqueness assert did NOT fire on absent probe")
    sys.exit(2)
except AssertionError as e:
    print("CONTROL FIRED (expected): %s" % e)

# --- Build r2 bytes in memory; only write if every pin matches -------------
outputs = []
for src, dst, old, new, h1, s1, h2, s2 in JOBS:
    p = os.path.join(HERE, src)
    with open(p, "rb") as f:
        data = f.read()
    if sha1_12(data) != h1 or len(data) != s1:
        raise SystemExit("R1-BASE MISMATCH %s: %s/%d expected %s/%d"
                         % (src, sha1_12(data), len(data), h1, s1))
    newdata = replace_once(data, old.encode("ascii"), new.encode("ascii"),
                           src)
    got_h, got_s = sha1_12(newdata), len(newdata)
    if got_h != h2 or got_s != s2:
        raise SystemExit("PIN MISMATCH %s -> %s: got %s/%d expected %s/%d"
                         % (src, dst, got_h, got_s, h2, s2))
    # hygiene: ASCII, no CR, ends LF, bare-LF convention
    if any(b > 127 for b in newdata):
        raise SystemExit("HYGIENE: non-ASCII byte in %s" % dst)
    if b"\r" in newdata:
        raise SystemExit("HYGIENE: CR byte in %s" % dst)
    if not newdata.endswith(b"\n"):
        raise SystemExit("HYGIENE: missing trailing LF in %s" % dst)
    nlines = newdata.count(b"\n")
    outputs.append((dst, newdata, nlines))

for dst, newdata, nlines in outputs:
    with open(os.path.join(HERE, dst), "wb") as f:
        f.write(newdata)

for dst, newdata, nlines in outputs:
    print("WROTE %s sha1_12=%s size=%d lines=%d ascii=yes cr=no trailingLF=yes"
          % (dst, sha1_12(newdata), len(newdata), nlines))
print("ALL PINS MATCH")
