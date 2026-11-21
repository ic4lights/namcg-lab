# fix_s3_v3.py -- byte-surgery driver (proposal 107): produce clean v3 of the central
# script from v2 by removing the single dead placeholder line. Writes ONLY inside the
# proposal 107 folder. Verifies parse and byte-diff is exactly one line.
import ast
import hashlib
import os
import sys

d = "proposals/107-a-map-chart-condensate-selection"
src = os.path.join(d, "s3_symbol_selection_v2.py")
dst = os.path.join(d, "s3_symbol_selection_v3.py")

b = open(src, "rb").read()
print("v2: %d bytes sha256/16 %s" % (len(b), hashlib.sha256(b).hexdigest()[:16]))
lines = b.split(b"\n")
hits = [i for i, ln in enumerate(lines) if b"placeholder replaced below" in ln]
assert len(hits) == 1, "expected exactly 1 placeholder line, got %d" % len(hits)
print("removing line %d: %r" % (hits[0], lines[hits[0]][:70]))
out = b"\n".join(lines[:hits[0]] + lines[hits[0] + 1:])
ast.parse(out.decode("utf-8"))
assert b"placeholder" not in out
open(dst, "wb").write(out)
print("v3: %d bytes sha256/16 %s ; AST parse: OK" % (len(out), hashlib.sha256(out).hexdigest()[:16]))
sys.exit(0)
