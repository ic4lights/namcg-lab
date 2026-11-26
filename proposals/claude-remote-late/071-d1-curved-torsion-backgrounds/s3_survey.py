"""S3. Numerical survey of left-invariant solutions of the first-order class (constant W).
(i) flat frame (C = 0): random least-squares starts, normalised |w| = 1, Lorentzian and Euclidean;
(ii) stored solutions on four-dimensional Lie algebras with dim [g,g] = 2 (found by the same
least-squares method with C free and the Jacobi identity imposed, seed 21; file
solvable_solutions_seed21.npy): re-verified here, with their invariants.
Numerical, not a classification.  Run: python -I s3_survey.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import least_squares
import bg, invariants as I

rng = np.random.default_rng(1)


def res(p, eta):
    B1, B2, T, R = bg.brackets(np.zeros((4, 4, 4)), bg.W_of(p), eta)
    return np.concatenate([B1.ravel(), B2.ravel(), [np.sum(p ** 2) - 1.0]])


for sig in ([-1, 1, 1, 1], [1, 1, 1, 1]):
    eta = bg.eta_of(sig); n = nR = 0; RRmax = 0.0; scal = []
    for t in range(60):
        p0 = rng.normal(size=24); p0 /= np.linalg.norm(p0)
        s = least_squares(res, p0, args=(eta,), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
        if np.abs(s.fun).max() < 1e-11:
            n += 1
            d = I.info(np.zeros((4, 4, 4)), bg.W_of(s.x), eta)
            if d['|R|max'] > 1e-6:
                nR += 1; RRmax = max(RRmax, abs(d['RR'])); scal.append(d['scalar'])
    print('(i) flat frame, eta =', sig, ': 60 starts, %d converged (residual < 1e-11), %d with R != 0;'
          ' max |R_abcd R^abcd| among them = %.1e; scalar curvature range %s'
          % (n, nR, RRmax, (np.round(min(scal), 3), np.round(max(scal), 3)) if scal else '-'))

PA = bg.PAIRS
def C_of(p):
    C = np.zeros((4, 4, 4))
    for k, (a, b) in enumerate(PA):
        C[a, b] = p[4 * k:4 * k + 4]; C[b, a] = -p[4 * k:4 * k + 4]
    return C
X = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'solvable_solutions_seed21.npy'))
eta = bg.eta_of([-1, 1, 1, 1])
for x in X:
    C = C_of(x[:24]); W = bg.W_of(x[24:]); d = I.info(C, W, eta)
    print('(ii) |B1| %.1e |B2| %.1e Jacobi %.1e | |T| %.3f |R| %.3f R_abcd R^abcd %.2e scalar %.3f | dim[g,g] %d, center %d, derived series %s'
          % (d['B1'], d['B2'], d['jacobi'], d['|T|max'], d['|R|max'], d['RR'], d['scalar'],
             d['lie']['dim_derived'], d['lie']['dim_center'], d['lie']['derived_series'][:2]))
