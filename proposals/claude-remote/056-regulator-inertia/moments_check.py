#!/usr/bin/env python3
"""Monte Carlo check at N = 2 of the second-moment formula used in proposal 056:
    R(h)_{ab} = <Tr X_a X_b>_h = c_E e^{i pi/4} (h^{-1})_{ab}   for h in C_0,
with c_E = <Tr X_0^2>_E the Euclidean value, and R(-h) = R(h) (the integrand is even in h), so that on -C_0
    <Tr A_mu A_nu> = Lambda R(h) Lambda^T = -c_E e^{i pi/4} eta_{mu nu}.
Units 1/(4 g_YM^2) = 1.  Same importance sampler as proposal 055 (mc_check.py): density
det(X^T X)^4 exp(-c sigma_2(X^T X)), Gram eigenvalues by Metropolis, Stiefel frames Haar.
Tr X_a X_b = (1/2)(X X^T)_{ab} at N = 2.  Errors: batch means over 20 batches (1 sigma).
This is a check of a holomorphy argument, not a proof.
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(5603)
n = 10
out = []
pr = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))


def sample_g(nchain=2000, nstep=3200, burn=800, thin=8, step=0.35):
    y = rng.normal(0, 0.3, (nchain, 3))
    def logp(y):
        g = np.exp(y)
        s2 = g[:, 0] * g[:, 1] + g[:, 0] * g[:, 2] + g[:, 1] * g[:, 2]
        dlt = np.abs((g[:, 0] - g[:, 1]) * (g[:, 0] - g[:, 2]) * (g[:, 1] - g[:, 2]))
        return 8 * y.sum(1) + np.log(dlt + 1e-300) - s2
    lp = logp(y)
    keep = []
    for it in range(nstep):
        yn = y + rng.normal(0, step, y.shape)
        lpn = logp(yn)
        a = np.log(rng.random(nchain)) < lpn - lp
        y[a] = yn[a]; lp[a] = lpn[a]
        if it >= burn and (it - burn) % thin == 0:
            keep.append(np.exp(y).copy())
    return np.concatenate(keep)


def imdet_ratio(h, a, b):
    haa = a @ h @ a; hbb = b @ h @ b; hab = a @ h @ b
    return np.imag(haa * hbb - hab ** 2) / ((a @ a) * (b @ b) - (a @ b) ** 2)


def c_lower(h, starts=30):
    best = np.inf
    f = lambda x: imdet_ratio(h, x[:n], x[n:])
    r = np.random.default_rng(1)
    for _ in range(starts):
        res = minimize(f, r.standard_normal(2 * n), method='BFGS')
        best = min(best, res.fun)
    return best


def R_estimate(h, g, U, c):
    s = c ** -0.25
    nb = 20
    num_b, den_b = [], []
    for gb, Ub in zip(np.array_split(g, nb), np.array_split(U, nb)):
        sq = np.sqrt(gb) * s
        X = Ub * sq[:, None, :]                                   # (N, n, 3)
        Hm = np.einsum('nma,mk,nkb->nab', X, h, X)
        G = sq ** 2
        detG = G.prod(1)
        s2G = G[:, 0] * G[:, 1] + G[:, 0] * G[:, 2] + G[:, 1] * G[:, 2]
        detH = np.linalg.det(Hm)
        trH = np.einsum('naa->n', Hm); trH2 = np.einsum('nab,nba->n', Hm, Hm)
        s2H = (trH ** 2 - trH2) / 2
        w = np.exp(4 * np.log(detH / detG) + 1j * s2H + c * s2G)
        num_b.append(0.5 * np.einsum('n,nma,nka->mk', w, X, X))
        den_b.append(w.sum())
    num_b = np.array(num_b); den_b = np.array(den_b)
    ests = num_b / den_b[:, None, None]
    est = num_b.sum(0) / den_b.sum()
    err = (ests.real.std(0, ddof=1) + 1j * ests.imag.std(0, ddof=1)) / np.sqrt(nb)
    return est, err


g = sample_g()
N = len(g)
U = np.linalg.qr(rng.standard_normal((N, n, 3)))[0]
pr(f"samples {N}")
hE = np.exp(1j * np.pi / 4) * np.eye(n)
RE, eE = R_estimate(hE, g, U, 1.0)
cE = np.trace(RE).real / n
pr(f"Euclidean point: c_E = trace/10 = {cE:.5f}; off-diagonal max |R| = {np.max(np.abs(RE - np.diag(np.diag(RE)))):.1e}")

cases = []
for spread in (0.25, 0.4):
    b = np.pi / 4 + rng.uniform(-spread, spread, n)
    cases.append((f"diagonal, phases pi/4 +- {spread}", np.diag(np.exp(1j * b))))
O = np.linalg.qr(rng.standard_normal((n, n)))[0]
cases.append(("O^T D O (last D, O real orthogonal)", O.T @ cases[-1][1] @ O))
for name, h in cases:
    c = 0.95 * c_lower(h)
    R, e = R_estimate(h, g, U, c)
    pred = cE * np.exp(1j * np.pi / 4) * np.linalg.inv(h)
    dev = np.abs(R - pred) / (np.abs(e) + 1e-12)
    rel = np.linalg.norm(R - pred) / np.linalg.norm(pred)
    # discrimination: the prediction with the opposite sign, and with h^{-1} replaced by its diagonal-averaged phase
    rel_flip = np.linalg.norm(R + pred) / np.linalg.norm(pred)
    pr(f"{name}: c_h = {c/0.95:.3f}; |R - c_E e^(i pi/4) h^-1| / |pred| = {rel:.4f};"
       f" median/max entrywise deviation in sigma: {np.median(dev):.2f}/{np.max(dev):.2f};"
       f" opposite sign would give {rel_flip:.3f}")
    pr(f"   R_00 = {R[0,0]:.4f} +- {e[0,0]:.4f}  predicted {pred[0,0]:.4f}")
open(__file__.replace('.py', '.txt'), 'w').write('\n'.join(out) + '\n')
