# fix_s3_v5.py -- byte-surgery driver (proposal 107): v4 -> v5.
# One fix, asserted as an exact unique byte replacement:
#   inv = R.nullspace()  ->  inv = R.T.nullspace()
# R is 36x20 of rank 20; its RIGHT nullspace is 0-dimensional (v4: vacuous invis_ok,
# len(inv)=0 -> Q3pt FAIL). The invisible kernel directions are coefficient vectors c in
# R^36 with c^T R = 0, i.e. the LEFT nullspace = nullspace of R^T, dimension 36-20=16.
# Also updates the header provenance line. Writes only inside the proposal folder.
import ast
import hashlib
import sys

d = "proposals/107-a-map-chart-condensate-selection/"
src = d + "s3_symbol_selection_v4.py"
dst = d + "s3_symbol_selection_v5.py"
b = open(src, "rb").read()
print("v4: %d bytes sha256/16 %s" % (len(b), hashlib.sha256(b).hexdigest()[:16]))

OLD1 = b"    inv = R.nullspace()"
NEW1 = b"    inv = R.T.nullspace()   # LEFT nullspace (coefficients c in R^36, c^T R = 0)"
OLD2 = (b"# s3_symbol_selection_v4.py -- proposal 107 r1, central computation (AUTHORITATIVE).\n"
        b"# Supersedes s3_symbol_selection_v3.py (crash at Q1c, wrong Taylor order), v2 (dead\n"
        b"# placeholder line) and s3 (dead pre-edit block); all retained as provenance.")
NEW2 = (b"# s3_symbol_selection_v5.py -- proposal 107 r1, central computation (AUTHORITATIVE).\n"
        b"# v4 ran all claims PASS except Q3pt, whose right-nullspace bug this version fixes\n"
        b"# (invisible basis must be the LEFT nullspace of the pairing matrix). Supersedes\n"
        b"# v4/v3/v2/s3, all retained as provenance.")
for old, new in ((OLD1, NEW1), (OLD2, NEW2)):
    assert b.count(old) == 1, "pattern not unique/absent: %r" % old[:70]
    b = b.replace(old, new, 1)
assert b.count(b"R.nullspace()") == 0 or b.count(b"R.T.nullspace()") == 1
ast.parse(b.decode("utf-8"))
open(dst, "wb").write(b)
print("v5: %d bytes sha256/16 %s ; AST parse: OK" % (len(b), hashlib.sha256(b).hexdigest()[:16]))
sys.exit(0)
