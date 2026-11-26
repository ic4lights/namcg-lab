"""s7_inert_schur.py (proposal 047): exploratory relaxation of 'inert amplitudes set to zero'. Schur complement of the three
inert amplitudes in the induced forms alone (tree-level form neglected), fibre-trace reading, at three base/wave-vector cases.
Reports the generalised eigenvalues on the five traceless polarisations relative to EH(hbar), before and after elimination.
Prints to stdout only; writes nothing. Not used in the manuscript insert."""
import sys, os
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '046-fibre-regime-interpolation'))
from forms_lib import *
import numpy as np, scipy.linalg as sl
cases = [((5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)]), ((5, 3), [R(-1, 3), R(2, 5), R(1, 4), R(-3, 2)]), ((13, 5), [R(2, 3), R(-1, 2), R(1, 3), R(1, 7)])]
for (y0, y4), qq in cases:
    F = cp12_forms(y0, y4, qq); f = D_forms(F)
    A = lambda k: np.array(f[k].evalf(), dtype=float)
    IX2, SC2, EH = A('IX2'), A('SC2'), A('EH1')
    Gm = gram(F); E1, E2, trv = cov_span_forms(Gm)
    Ntl = np.array(sp.Matrix.hstack(*trv.nullspace()).evalf(), dtype=float)
    E5 = Ntl.T @ EH[:6, :6] @ Ntl
    ev = lambda Q: np.round(np.sort(sl.eigvals(Ntl.T @ Q @ Ntl, E5).real), 4).tolist()
    schur = lambda Q: Q[:6, :6] - Q[:6, 6:] @ np.linalg.solve(Q[6:, 6:], Q[6:, :6])
    print((y0, y4), [str(v) for v in qq])
    print("  EH on the inert block: max |entry| =", float(np.abs(EH[6:, :]).max()))
    print("  IX2 before", ev(IX2[:6, :6]), "after", ev(schur(IX2)))
    print("  SC2 before", ev(SC2[:6, :6]), "after", ev(schur(SC2)))
    for r in (1, 6, 12):
        print("  IX2 + %d SC2 after elimination" % r, ev(schur(IX2 + r * SC2)))
