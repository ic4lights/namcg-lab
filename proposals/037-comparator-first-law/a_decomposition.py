"""037-a: Is the Weyl-type content of tr Omega^2 on the 033 modes carried by the Levi-Civita-lifted part or by a non-metric part?
For each mode: <Omega,Omega>, <Omega,R>, <R,R> (R = Levi-Civita curvature as an so(4)-valued 2-form, R^mu_nu = R_{mu nu st}/g0), 
N := Omega - R, and the functional ell_H(X) = tr(H X_12)/g0 for H = J_12 (the replica / Killing-flow holonomy)."""
import sympy as sp
from modes_lib import *
for name, Thb in backgrounds():
    ms = modes(Thb, 10, 11)
    print('==', name, ' g0 =', ms[0]['g0'])
    rows = []
    for m in ms:
        g0 = m['g0']; Om = m['Om']; R = m['Rmat']
        N = {k: Om[k] - R[k] for k in Om}
        OO, OR, RR, NN, NR = ip(Om, Om, g0), ip(Om, R, g0), ip(R, R, g0), ip(N, N, g0), ip(N, R, g0)
        C2 = m['C2']
        J12 = gen(0, 1)
        lO, lR, lN = [(J12*X[(0, 1)]).trace()/g0 for X in (Om, R, N)]
        rows.append((sp.simplify(OO/C2), sp.simplify(OR/C2), sp.simplify(RR/C2), sp.simplify(NN/C2), sp.simplify(NR/C2), sp.simplify(lO + m['Rj']), sp.simplify(lR + m['Rj']), sp.simplify(lN)))
    print(' columns: <Om,Om>/C2, <Om,R>/C2, <R,R>/C2, <N,N>/C2, <N,R>/C2, ell(Om)+R_ijij, ell(R)+R_ijij, ell(N)')
    for r in rows: print('  ', r)
    print(' distinct values per column:', [sorted(set(c)) for c in zip(*rows)])
