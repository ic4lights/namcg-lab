# patch_r2.py -- regenerate proposal-r2.md byte-exactly from the recorded
# proposal-r1.md bytes (sha1 2ffe61497fefa51597f2381555f28983355ee3e4, 30536 B)
# plus the round-2 replacement blocks in r2_blocks.txt (FINDING 1 payload
# display repair, option (a); FINDING 2 tube-bound wording; r2 reproduction
# pack, decisions, gatekeeper notes). OLD spans are addressed by (start,end)
# line ranges guarded by ASCII substrings from proposal-r1.md itself, so no
# OLD text is retyped. Block encoding: '@(' = backslash-open-math, '@)' closes
# (every other '@' is illegal); on read '@' is replaced by chr(92). Re-run
# reproduces proposal-r2.md byte-for-byte (asserted).
# Run:  python -I -B patch_r2.py     (from the proposal folder)
import os, re, hashlib

BS = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
CRLF = bytes([13, 10])
R1SHA = "2ffe61497fefa51597f2381555f28983355ee3e4"
raw = open(os.path.join(HERE, "proposal-r1.md"), "rb").read()
assert hashlib.sha1(raw).hexdigest() == R1SHA and len(raw) == 30536, "proposal-r1.md off its pin"
lines = raw.split(CRLF)
assert CRLF.join(lines) == raw, "CRLF round-trip failed"

# ---- load replacement blocks ----
bx = open(os.path.join(HERE, "r2_blocks.txt"), "rb").read()
blocks = {}
for m in re.finditer(rb"<<<BLOCK (\d+)>>>(.*?)<<<END \1>>>", bx, re.S):
    n = int(m.group(1))
    body = m.group(2)
    assert body.startswith(b"\n") and body.endswith(b"\n"), "block %d bounds" % n
    body = body[1:-1]
    assert all(c == 10 or 32 <= c < 127 for c in body), "block %d non-printable byte" % n
    p = body.find(b"@")
    while p != -1:
        assert body[p:p+2] in (b"@(", b"@)"), "block %d illegal @ at %d" % (n, p)
        p = body.find(b"@", p+1)
    blocks[n] = body.replace(b"@", BS.encode("ascii")).split(b"\n")
assert sorted(blocks) == list(range(1, 19)), sorted(blocks)

# ---- replacements: (start_line, end_line, guard, block#) ----
REPS = [
    (1, 1, "round 1", 1),
    (23, 25, "volume-averaged soft-event bound", 2),
    (139, 141, "the upper bound gives", 3),
    (191, 191, "averaged consumption", 4),
    (199, 201, "Markov on the one-point law", 5),
    (272, 274, "averaged soft-event bound", 6),
    (293, 293, "4597 B, sha1", 7),
    (300, 301, "(839349 B)", 8),
    (331, 331, "31 checks: S1-S7 symbolic", 9),
    (341, 342, "PASS 31 FAIL 0", 10),
    (343, 343, "byte-identical on", 11),
    (344, 345, "Invariant output", 12),
    (346, 346, "out-of-repo copy (untracked", 13),
    (361, 361, "839349", 14),
    (368, 371, "Reproduction pack", 15),
    (390, 391, "rigorous monotonicity + averaged bound", 16),
    (404, 404, "post-116 author rule", 17),
    (477, 477, "N6/N7 are probes", 18),
]
starts = [r[0] for r in REPS]
assert starts == sorted(starts), "REPS must be in ascending order"
for a, b, guard, n in REPS:
    seg = CRLF.join(lines[a-1:b])
    assert guard.encode("ascii") in seg, "guard %r not in lines %d-%d" % (guard, a, b)
for a, b, guard, n in sorted(REPS, key=lambda r: -r[0]):
    lines[a-1:b] = blocks[n]
out = CRLF.join(lines)

# ---- global invariants of proposal-r2 ----
assert out.count(b"round 2") >= 1 and lines[0].endswith(b"round 2")
for tok in [b"51010545179a3d3609826aefa0f6c1fa84182ae4", b"ce91063fddcaa5599429519f4bc2c478e0d919e8"]:
    assert out.count(tok) >= 2, tok
assert out.count(b"PASS 35 FAIL 0") == 2
assert b"(839349 B)" not in out and b"7e0546a425c16b55e30f2513a228efd836c120b8` (839349" not in out
# r1 artifacts may still be referenced with the OLD sha1 (r1 blocks kept):
assert out.count(b"7e0546a425c16b55e30f2513a228efd836c120b8") == 1  # one r1 cert record kept
assert sum(1 for c in out if not (10 == c or 13 == c or 32 <= c < 127)) == 2, "proposal-r2 stray byte (expect exactly the 2 non-ASCII bytes inherited from r1)"
assert sum(1 for c in out if c < 32 and c not in (10, 13)) == 0, "proposal-r2 control byte"
loneCR = out.count(b"\r") - out.count(CRLF)
assert loneCR == 2, "expected the 2 pre-existing lone CRs of r1, got %d" % loneCR

path = os.path.join(HERE, "proposal-r2.md")
if os.path.exists(path):
    assert open(path, "rb").read() == out, "REGENERATION MISMATCH: patch_r2.py did not reproduce proposal-r2.md"
    print("REPRODUCED byte-exactly")
else:
    with open(path, "wb") as f:
        f.write(out)
    print("proposal-r2.md written")
print("sha1 %s size %d loneCR %d" % (hashlib.sha1(out).hexdigest(), len(out), loneCR))
print("PATCH OK")
