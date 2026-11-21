# fix_s3_v4.py -- byte-surgery driver (proposal 107): v3 -> v4.
# Three fixes, each asserted as an exact unique byte replacement:
#  (1) Taylor check: series order 6 -> 5 so removeO() leaves exactly the terms
#      through th^3 (v3 compared a th^3 target against a th^5-truncated series).
#  (2) Q1c Weyl(): cmath.exp(scalar) cannot multiply a nested list; make the
#      phase multiplication explicit.
#  (3) Header title/provenance line updated (v4 supersedes v2/v3/s3).
# Writes ONLY inside the proposal 107 folder; asserts ast.parse of the result.
import ast
import hashlib
import sys

d = "proposals/107-a-map-chart-condensate-selection/"
src = d + "s3_symbol_selection_v3.py"
dst = d + "s3_symbol_selection_v4.py"
b = open(src, "rb").read()
print("v3: %d bytes sha256/16 %s" % (len(b), hashlib.sha256(b).hexdigest()[:16]))

OLD1 = b"ser = sp.series(cph(*p0) - cph(p0[1], p0[0]), th, 0, 6).removeO()"
NEW1 = b"ser = sp.series(cph(*p0) - cph(p0[1], p0[0]), th, 0, 5).removeO()"
OLD2 = (b"def Weyl(m, n):\n"
        b"    return cmath.exp(-1j * ang * m * n / 2) * matmul(Um(m), Vn(n))")
NEW2 = (b"def Weyl(m, n):\n"
        b"    ph = cmath.exp(-1j * ang * m * n / 2)\n"
        b"    MM = matmul(Um(m), Vn(n))\n"
        b"    return [[ph * MM[i][j] for j in range(N)] for i in range(N)]")
OLD3 = (b"# s3_symbol_selection_v2.py -- proposal 107 r1, central computation (AUTHORITATIVE;\n"
        b"# supersedes s3_symbol_selection.py, which contains a dead pre-edit block and is kept\n"
        b"# only as provenance).")
NEW3 = (b"# s3_symbol_selection_v4.py -- proposal 107 r1, central computation (AUTHORITATIVE).\n"
        b"# Supersedes s3_symbol_selection_v3.py (crash at Q1c, wrong Taylor order), v2 (dead\n"
        b"# placeholder line) and s3 (dead pre-edit block); all retained as provenance.")
for old, new in ((OLD1, NEW1), (OLD2, NEW2), (OLD3, NEW3)):
    assert b.count(old) == 1, "pattern not unique/absent: %r" % old[:60]
    b = b.replace(old, new, 1)
ast.parse(b.decode("utf-8"))
open(dst, "wb").write(b)
print("v4: %d bytes sha256/16 %s ; AST parse: OK" % (len(b), hashlib.sha256(b).hexdigest()[:16]))
sys.exit(0)
