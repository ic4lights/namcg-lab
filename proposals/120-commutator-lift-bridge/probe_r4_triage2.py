import sys
import os

_orig = sys.argv[1] if len(sys.argv) > 1 else "heavy2"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_av = sys.argv
sys.argv = [sys.argv[0], "inert"]
import sympy as sp
from probe_r4_triage import QUAD, QUAR, w3, w4, nulltest, SHdia, cmat, polyvec
sys.argv = _av
mode = _orig

if mode == "p1":
    a1, a2, a3, a4 = sp.symbols("a1 a2 a3 a4", real=True)
    al = a1 + sp.I * a2
    be = a3 + sp.I * a4
    U2g = sp.Matrix([[al, be], [-sp.conjugate(be), sp.conjugate(al)]])
    norm = a1 ** 2 + a2 ** 2 + a3 ** 2 + a4 ** 2
    Pg = cmat(2, "g")
    dnum = sp.expand((U2g * Pg).adjoint() * (U2g * Pg) - norm * (Pg.adjoint() * Pg))
    print("P1' numerator identity (U2g Pg)^dag(U2g Pg) == norm Pg^dag Pg:",
          all(x == 0 for x in dnum), flush=True)
    sys.exit(0)


def nulltestL(family, SH):
    rows = [polyvec(sp.expand(q.xreplace(SH) - q)) for q in family]
    mons = sorted(set().union(*[set(r.monoms()) for r in rows]))
    Mx = sp.Matrix(len(rows), len(mons), lambda i, j: rows[i].coeff_monomial(mons[j]))
    return Mx.shape, Mx.T.nullspace()


shp, nsL = nulltestL(QUAD, SHdia)
print("QUAD shape", shp, "left null dim:", len(nsL), flush=True)
for v in nsL:
    print([str(x) for x in v.T.tolist()[0]], flush=True)
shp2, nsL2 = nulltestL(QUAR, SHdia)
print("QUAR shape", shp2, "left null dim:", len(nsL2), flush=True)
for v in nsL2:
    print([str(x) for x in v.T.tolist()[0]], flush=True)
print("ALL PROBE2 DONE", flush=True)
