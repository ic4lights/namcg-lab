#!/usr/bin/env python3
"""Monte Carlo check at N = 2 of  V(h,q) = F_E(e^{i pi/4} q^T h^{-1} q)  (proposal 055).

Units 1/(4 g_YM^2) = 1.  For a 10x3 real X (rows mu, colour columns), G_h = X^T h X, G = X^T X.
  W(h,q) = int dX det(G_h)^4 exp(i sigma_2(G_h)) Tr exp(i q^T X . sigma/2),   V = W(h,q)/W(h,0),
  Tr exp(i v.sigma/2) = 2 cos( sqrt(v.v)/2 ),  v = q^T X.
Sampling density p(X) ~ det(G)^4 exp(-c sigma_2(G)), c <= c_h (so the importance weights are bounded):
  eigenvalues g of G with density ~ prod g^7 |Delta(g)| exp(-c sigma_2(g)) (Metropolis in log g),
  X = U diag(sqrt g) with U Haar on the Stiefel manifold V_3(R^10) (QR of a Gaussian matrix).
Each contour h = D diagonal with distinct phases near pi/4 (so that c_h = min Im(d_mu d_nu) is close to the
typical damping and the importance weights are well behaved) and a generic real q is compared with the single-axis diagonal contour h' = diag(1/z, e^{i b_s},...) with q' = e_0, which has the
same z = q^T h^{-1} q.  The theorem predicts equal V.  A Euclidean row (h = e^{i pi/4} I) is included.
Errors: batch means over 20 batches (1 sigma).
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(5502)
n = 10


def sample_g(nchain=2000, nstep=4000, burn=800, thin=8, step=0.35):
    y = rng.normal(0, 0.3, (nchain, 3))
    def logp(y):
        g = np.exp(y)
        s2 = g[:, 0] * g[:, 1] + g[:, 0] * g[:, 2] + g[:, 1] * g[:, 2]
        dlt = np.abs((g[:, 0] - g[:, 1]) * (g[:, 0] - g[:, 2]) * (g[:, 1] - g[:, 2]))
        return 8 * y.sum(1) + np.log(dlt + 1e-300) - s2
    lp = logp(y)
    keep = []
    acc = 0
    for it in range(nstep):
        yn = y + rng.normal(0, step, y.shape)
        lpn = logp(yn)
        a = np.log(rng.random(nchain)) < lpn - lp
        y[a] = yn[a]; lp[a] = lpn[a]; acc += a.mean()
        if it >= burn and (it - burn) % thin == 0:
            keep.append(np.exp(y).copy())
    return np.concatenate(keep), acc / nstep


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


def V_estimate(h, q, g, U, c):
    s = c ** -0.25
    sq = np.sqrt(g) * s                       # (N,3)
    Hm = np.einsum('nma,mk,nkb->nab', U, h, U) * sq[:, :, None] * sq[:, None, :]
    G = (sq ** 2)
    detG = G.prod(1)
    s2G = G[:, 0] * G[:, 1] + G[:, 0] * G[:, 2] + G[:, 1] * G[:, 2]
    detH = np.linalg.det(Hm)
    trH = np.einsum('naa->n', Hm)
    trH2 = np.einsum('nab,nba->n', Hm, Hm)
    s2H = (trH ** 2 - trH2) / 2
    logw = 4 * np.log(detH / detG) + 1j * s2H + c * s2G
    w = np.exp(logw)
    qU = np.einsum('m,nma->na', q, U) * sq
    vv = (qU ** 2).sum(1)
    O = 2 * np.cos(np.sqrt(vv) / 2)
    nb = 20
    wb = np.array_split(w, nb); ob = np.array_split(w * O, nb)
    ests = np.array([o.mean() / x.mean() for o, x in zip(ob, wb)])
    est = (w * O).mean() / w.mean()
    err = (np.std(ests.real, ddof=1) + 1j * np.std(ests.imag, ddof=1)) / np.sqrt(nb)
    return est, err, np.max(np.abs(w))


out = []
pr = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))

g, acc = sample_g()
N = len(g)
U = np.linalg.qr(rng.standard_normal((N, n, 3)))[0]
pr(f"samples {N}, Metropolis acceptance {acc:.3f}")

cases = []
# Euclidean row
cases.append(("Euclidean h=e^{i pi/4}I, |q|^2=2", np.exp(1j * np.pi / 4) * np.eye(n), np.sqrt(2.0) * np.eye(n)[3]))
for t, spread in enumerate([0.25, 0.3, 0.4, 0.5]):
    b = np.pi / 4 + rng.uniform(-spread, spread, n)
    D = np.diag(np.exp(1j * b))
    q = rng.standard_normal(n); q *= rng.uniform(1.0, 1.6) / np.linalg.norm(q)
    cases.append((f"diagonal, distinct phases (spread {spread}) #{t}", D, q))
# one non-diagonal h = O^T D O with O real orthogonal (exact change of variables; included as a consistency row)
O = np.linalg.qr(rng.standard_normal((n, n)))[0]
cases.append(("O^T D O, same D as last row, q -> O^T q", O.T @ D @ O, O.T @ q))

for name, h, q in cases:
    z = q @ np.linalg.solve(h, q)
    ch = c_lower(h)
    c = 0.95 * ch
    V, e, wmax = V_estimate(h, q, g, U, c)
    # single-axis comparison contour with the same z
    a0 = -np.angle(z)                     # phase of 1/z
    lo, hi = max(0.0, -a0), min(np.pi / 2, np.pi - a0)
    bs = 0.5 * (lo + hi)
    hp = np.diag([1 / z] + [np.exp(1j * bs)] * 9)
    chp = c_lower(hp)
    Vp, ep, wmaxp = V_estimate(hp, np.eye(n)[0], g, U, 0.95 * chp)
    pr(f"{name}: z = {z:.4f} (arg/pi {np.angle(z)/np.pi:+.3f}); c_h={ch:.3f}")
    pr(f"   V(h,q)            = {V:.4f} +- {e:.4f}   (max |w| {wmax:.2f})")
    pr(f"   V(axis, same z)   = {Vp:.4f} +- {ep:.4f}   (max |w| {wmaxp:.2f}, c_h'={chp:.3f})")
    pr(f"   difference / combined error = {abs(V - Vp) / abs(abs(e) + abs(ep)):.2f}")
    if name.startswith("diagonal"):
        # discrimination row: the same |q|^2 with the phases of h averaged (a wrong z)
        zw = np.sum(q ** 2) * np.exp(-1j * np.mean(np.angle(np.diag(h))))
        a0 = -np.angle(zw); lo, hi = max(0.0, -a0), min(np.pi / 2, np.pi - a0)
        hw = np.diag([1 / zw] + [np.exp(1j * 0.5 * (lo + hi))] * 9)
        Vw, ew, _ = V_estimate(hw, np.eye(n)[0], g, U, 0.95 * c_lower(hw))
        pr(f"   control: V(axis) at averaged-phase z' = {zw:.4f}: {Vw:.4f} +- {ew:.4f};"
           f" |V(h,q) - control| / error = {abs(V - Vw) / abs(abs(e) + abs(ew)):.1f}")
open(__file__.replace('.py', '.txt'), 'w').write('\n'.join(out) + '\n')
