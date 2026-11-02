"""049 s10: apply G1-G9 of review-r2.md to the r2 insert.

The old and new strings are read as raw text from review-r2.md; none is typed here. The source is the r2 insert: the
archive appH_insert.r2.tex if present, otherwise appH_insert.tex, which is then archived. Each old string must occur
exactly once at its turn, and the result must have the byte count and sha256 stated in the review. On any mismatch
the script exits without writing. Re-running it on the finished folder reproduces the same bytes."""
import hashlib
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
SRC_SHA = "92f8033b70adb8140f1c70b69e81f101ae30597d10d662c4c70f72045a10e4e2"
SRC_LEN = 21698
OUT_SHA = "b19b4c9890f65a15f33ec0fb21bc5af957ad2e56617335ec3e7f3ff7d47e43e3"
OUT_LEN = 22769


def sha(b):
    return hashlib.sha256(b).hexdigest()


def refuse(msg):
    print("REFUSED, nothing written:", msg)
    sys.exit(1)


review = open(os.path.join(here, "review-r2.md"), "rb").read().decode("utf-8").replace("\r\n", "\n")
pairs = re.findall(r"^- \*\*G(\d)\.\*\* old: `([^`\n]*)`\n  new: `([^`\n]*)`$", review, flags=re.M)
if [p[0] for p in pairs] != [str(i) for i in range(1, 10)]:
    refuse("parsed items %s, expected G1..G9" % [p[0] for p in pairs])

arch = os.path.join(here, "appH_insert.r2.tex")
cur = os.path.join(here, "appH_insert.tex")
src_path = arch if os.path.exists(arch) else cur
src = open(src_path, "rb").read()
if len(src) != SRC_LEN or sha(src) != SRC_SHA:
    refuse("source %s is %d bytes, sha %s" % (os.path.basename(src_path), len(src), sha(src)))
print("source", os.path.basename(src_path), len(src), "bytes, sha256", sha(src))

s = src.decode("ascii")
for k, old, new in pairs:
    n_turn = s.count(old)
    n_src = src.decode("ascii").count(old)
    print("G%s: old occurs %d at its turn, %d in r2; old %d chars, new %d chars" % (k, n_turn, n_src, len(old), len(new)))
    if n_turn != 1:
        refuse("G%s old string occurs %d times" % (k, n_turn))
    s = s.replace(old, new)

out = s.encode("ascii")
print("result", len(out), "bytes, sha256", sha(out))
if len(out) != OUT_LEN or sha(out) != OUT_SHA:
    refuse("result differs from the review's %d bytes, sha %s" % (OUT_LEN, OUT_SHA))
print("matches the review's byte count and sha256")

if not os.path.exists(arch):
    with open(arch, "wb") as f:
        f.write(src)
    print("archived r2 bytes as appH_insert.r2.tex")
with open(cur, "wb") as f:
    f.write(out)
print("wrote appH_insert.tex; ASCII", all(b < 128 for b in out), "CR", out.count(b"\r"), "BOM", out[:3] == b"\xef\xbb\xbf")
