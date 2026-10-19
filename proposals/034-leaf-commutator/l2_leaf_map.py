"""034 script 2: map of the leaf data into the engine variables and consistency checks.
 (1) F_ab(zeta) = -S_ab^k zeta_k antisymmetric, eigenvalue structure (a, b) with a/b = l/|y^4| on the kernel plane (028/032 closed form).
 (2) Engine variables (alpha_a, kappa_a, y^c) reproduce 030's quadratic form Q_EH (the Fierz-Pauli+dilaton form A) up to one overall constant, for random alpha.
 (3) F_ac y^c versus kappa_a (alignment): the leaf flux does not annihilate y; compare with the Jacobi statement [W_a,Y] horizontal.
"""
import numpy as np, sys
sys.dont_write_bytecode = True
from leafdata import *
from canon import canonical
from tail_coeffs import frozen_data
from eh_decomposition import QEH
rng = np.random.default_rng(12)
def A_engine(alpha, kappa, y):
    al_up = etan @ alpha
    return (1 / 24) * ((y @ etan @ y) * ((kappa @ al_up) ** 2 - (kappa @ etan @ kappa) * (alpha @ al_up)) - 2 * (kappa @ etan @ kappa) * (alpha @ y) ** 2)
for t in range(5):
    M0 = rand_point(rng); q = rng.normal(size=4)
    d = leaf_data(M0, q)
    S, y, yk, kappa = d['S'], d['y'], d['yk'], d['kappa']
    ell = np.sqrt(-(M0[:5, 5] @ np.diag([-1., 1, 1, 1, 1]) @ M0[:5, 5])); y4 = abs(M0[4, 5])
    out = []
    for th in (0.3, 1.9, 4.0):
        zeta = np.array([np.cos(th), np.sin(th)])
        F = -np.einsum('abk,k->ab', S, zeta)
        a, b, C, Bm, Fc = canonical(F)
        Fy = F @ y                                        # F_ac y^c
        al = (Fy @ kappa) / (kappa @ kappa)
        out.append((a / b, np.linalg.norm(Fy - al * kappa) / max(np.linalg.norm(Fy), 1e-30), np.linalg.norm(Fy) / (np.linalg.norm(y) * np.linalg.norm(F))))
    # (2): Q_EH of 030 vs A formula in engine variables
    dat = frozen_data(M0, q)
    QE, gbar0, v = QEH(dat, q)
    ratios = []
    for _ in range(4):
        alpha = rng.normal(size=4)
        ratios.append((alpha @ QE @ alpha) / A_engine(alpha, kappa, y))
    print("pt %d: l/|y4| = %.4f ; a/b at 3 centre directions = %s ; F y not parallel to kappa (resid, |Fy|/|y||F|) = %s ; Q_EH / A_engine = %s ; y.kappa = %.1e" % (
        t, ell / y4, np.round([o[0] for o in out], 4), [(round(o[1], 3), round(o[2], 3)) for o in out], np.round(ratios, 6), abs(y @ kappa)))
