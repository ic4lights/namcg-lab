"""022 script 8: symbol of the full so(4,2) Casimir C = 1/2 eta_A eta_B J^{AB} J^{AB} (the natural matrix-built 'Box of the whole structure')
pushed to the base y^C = M^{C5} (C=0..4), compared with g^{-1} = eta5 + y y /ell^2 (SO(4,1)-invariant, Euclidean) and with K4 = m^2 eta (4-matrix class).
Also the symbol of Box_{P4} = eta_ab D^a D^b and Box_{P5} = eta_AB D^A D^B on the base."""
import numpy as np
from symbol_tools import *
rng = np.random.default_rng(31)
e5 = np.diag([-1., 1, 1, 1, 1]); eta = np.diag([-1., 1, 1, 1])
errC = 0; errP5 = 0; ratC = []; ratP5 = []; sigC = {}
for t in range(30):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
    y = M0[:5, 5]; ell2 = -(y @ e5 @ y)
    ginv = e5 + np.outer(y, y) / ell2
    V = {p: vec(M0, *p) for p in pairs}
    K6 = np.zeros((5, 5))
    for (A, B) in pairs:
        w = eta6[A, A] * eta6[B, B]
        v = V[(A, B)]
        row = np.array([v[pidx[(C, 5)]] for C in range(5)])
        K6 += w * np.outer(row, row)
    # sum over unordered pairs = 1/2 sum over ordered
    # compare with proportional to ginv
    c = np.trace(K6 @ np.linalg.inv(ginv)) / 5.0 if False else (K6[1, 1] / ginv[1, 1])
    errC = max(errC, np.max(np.abs(K6 - c * ginv)) / abs(c))
    ratC.append(c / ell2)
    w6 = np.linalg.eigvalsh(K6 @ np.linalg.pinv(ginv) if False else K6)
    sigC[(int(np.sum(w6 < -1e-9)), int(np.sum(w6 > 1e-9)))] = sigC.get((int(np.sum(w6 < -1e-9)), int(np.sum(w6 > 1e-9))), 0) + 1
    # P5 box symbol on base
    K5 = np.zeros((5, 5))
    for A in range(5):
        v = V[(A, 5)]
        row = np.array([v[pidx[(C, 5)]] for C in range(5)])
        K5 += e5[A, A] * np.outer(row, row)
    c5 = K5[1, 1] / ginv[1, 1]
    errP5 = max(errP5, np.max(np.abs(K5 - c5 * ginv)) / abs(c5))
    ratP5.append(c5 / ell2)
print("Casimir C_{so(4,2)} base symbol  = c * g^{-1}: max rel. deviation", errC, "; c/ell^2 range", min(ratC), max(ratC), "; signature of K6:", sigC)
print("Box_{P5} base symbol = c5 * g^{-1}: max rel. deviation", errP5, "; c5/ell^2 range", min(ratP5), max(ratP5))
