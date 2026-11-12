#!/usr/bin/env python3
"""Search (proposal 056) for linear contours with h in -C_0 that are admissible for a general positive definite
regulator matrix P, in dimensions n = 3, 4 and 10.

Frame: a real basis that makes P the identity and eta = E = diag(-mu_0, mu_1, ..., mu_{n-1}) (every positive
definite P reduces to this; the mu are the moduli of the eigenvalues of P^{-1} eta).  A real congruence
preserves both Re M > 0 and the class of h, so h = -diag(e^{i beta}) with beta in K_0 (pair sums in (0, pi))
without loss of generality, and every Lambda with Lambda^T E Lambda = h is S Lambda_0 with S^T E S = E.
S = expm(E^{-1} A), A complex antisymmetric.  Objective: maximise lambda_min(Re Lambda^T Lambda)/|M| with a
beta parametrised inside K_0 (beta_0 in (-pi/2, pi), the other beta in the interval that keeps every pair sum in
(0, pi); this covers the part of K_0 with at most one beta outside (0, pi/2)).  A positive maximum would be an admissible -C_0 contour for that P.
Isotropic rows (all spatial mu equal) are controls: there the maximum is <= 0 by the inertia lemma.
"""
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import expm

rng = np.random.default_rng(56004)
out = []
pr = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))


def run(n, mus, restarts):
    E = np.diag(np.concatenate([[-mus[0]], mus[1:]]))
    sqE = np.sqrt(E.diagonal().astype(complex))
    def build(x):
        A = (x[:n * n] + 1j * x[n * n:2 * n * n]).reshape(n, n); A = (A - A.T) / 2
        S = expm(np.linalg.solve(E, A))
        d = np.exp(1j * betas(x[2 * n * n:]))
        return S @ np.diag(np.sqrt(-d) / sqE), d
    def betas(y):
        sg = 1 / (1 + np.exp(-y))
        b0 = -np.pi / 2 + 1.5 * np.pi * sg[0]
        lo = max(0.0, -b0) + 1e-3; hi = min(np.pi / 2, np.pi - b0) - 1e-3
        return np.concatenate([[b0], lo + (hi - lo) * sg[1:]])
    def pen(beta):
        s = beta[:, None] + beta[None, :]; off = ~np.eye(n, dtype=bool)
        return np.sum(np.maximum(0, -s[off]) + np.maximum(0, s[off] - np.pi))
    def f(x):
        L, d = build(x); M = L.T @ L
        if not np.all(np.isfinite(M)):
            return 10.0
        return -np.linalg.eigvalsh(M.real)[0] / np.linalg.norm(M)
    best, bestres = -np.inf, None
    for r in range(restarts):
        x0 = np.concatenate([rng.standard_normal(2 * n * n) * rng.uniform(0.2, 2),
                             rng.standard_normal(n)])
        res = minimize(f, x0, method='L-BFGS-B', options={'maxiter': 4000})
        L, d = build(res.x); M = L.T @ L
        if np.all(np.isfinite(M)) and pen(betas(res.x[2 * n * n:])) == 0:
            v = np.linalg.eigvalsh(M.real)[0] / np.linalg.norm(M)
            if v > best:
                best, bestres = v, res.x
    if bestres is None:
        return np.nan, np.nan
    # independent re-check of the best point: h = Lambda^T E Lambda equals -diag(d)
    L, d = build(bestres)
    err = np.max(np.abs(L.T @ E @ L + np.diag(d)))
    return best, err


with np.errstate(all='ignore'):
    for n, restarts in ((3, 30), (4, 30), (10, 4)):
        pats = [("isotropic", np.ones(n)),
                ("one large spatial weight", np.array([1.0] * (n - 1) + [10.0])),
                ("geometric 10^j", 10.0 ** np.arange(n)),
                ("geometric 100^j", 100.0 ** np.arange(n)),
                ("time weight 5, spatial 30^(j-1)", np.array([5.0] + list(30.0 ** np.arange(n - 1))))]
        for lab, mus in pats:
            b, err = run(n, mus, restarts)
            if np.isnan(b):
                pr(f"n={n:2d} {lab:34s}: no finite admissible optimum among the restarts (overflow)")
                continue
            pr(f"n={n:2d} {lab:34s}: sup found of lambda_min(Re M)/|M| = {b:+.3e}  (h = -diag(d) to {err:.1e})")
open(__file__.replace('.py', '.txt'), 'w').write('\n'.join(out) + '\n')
