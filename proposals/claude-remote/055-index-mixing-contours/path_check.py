#!/usr/bin/env python3
"""Path construction for real spacelike momenta (proposal 055).

For real k with k.k = kappa^2 > 0 (eta = diag(-1,1,...,1)), build Lambda(tau), tau in [0,1]:
    Lambda(tau) = L S(tau) D_half(tau),
  L real in O(9,1) with L^T k = kappa e_1;
  phases beta(tau) = (pi - tau*3 pi u/4, -tau*pi u/8, tau*pi u/4 (x8));
  D_half = diag(e^{i(beta_0 - pi)/2}, e^{i beta_i/2});
  S(tau) complex Lorentz (S eta S^T = eta) whose row 1 is s = D_half^{-1} r, r real supported on (1,2) with
  r_1^2 e^{-i beta_1} + r_2^2 e^{-i beta_2} = 1; other rows by eta-Gram-Schmidt.
Checks on a tau grid:
  (a) h(tau) = Lambda^T eta Lambda = diag(e^{i beta(tau)}) (so Im sigma_2 >= 0 along the path, > 0 for tau>0);
  (b) Re(Lambda^T Lambda) positive definite (regulator real part > 0, so Stokes at fixed eps applies);
  (c) q = Lambda^T k real (observable unitary on the end contour), q^T h^{-1} q = k.k;
  (d) Lambda(0) real (end contour 0 is the Hermitian contour).
u is halved until (b) holds on the grid.
"""
import numpy as np

rng = np.random.default_rng(55)
n = 10
eta = np.diag([-1.0] + [1.0] * 9)


def random_lorentz(r, maxrap):
    # product of random boosts in (0,i) planes and random rotations
    L = np.eye(n)
    for _ in range(4):
        i = r.integers(1, n)
        y = r.uniform(-maxrap, maxrap)
        B = np.eye(n); B[0, 0] = B[i, i] = np.cosh(y); B[0, i] = B[i, 0] = np.sinh(y)
        Q, _ = np.linalg.qr(r.standard_normal((n - 1, n - 1)))
        Rm = np.eye(n); Rm[1:, 1:] = Q
        L = L @ B @ Rm
    assert np.allclose(L.T @ eta @ L, eta)
    return L


def build(tau, u):
    beta = np.array([np.pi - tau * 3 * np.pi * u / 4, -tau * np.pi * u / 8] + [tau * np.pi * u / 4] * 8)
    dh = np.exp(1j * beta / 2); dh[0] = np.exp(1j * (beta[0] - np.pi) / 2)
    a = tau * np.pi * u / 8
    r2sq = 1.0 / (4 * np.cos(a) ** 2 - 1)
    r1sq = 2 * np.cos(a) * r2sq
    r = np.zeros(n); r[1] = np.sqrt(r1sq); r[2] = np.sqrt(r2sq)
    s = r / dh
    rows = {1: s}
    order = [0] + list(range(2, n))
    for mu in order:
        v = np.zeros(n, complex); v[mu] = 1.0
        for nu, w in rows.items():
            v = v - (v @ eta @ w) / (w @ eta @ w) * w
        nv = v @ eta @ v
        v = v / np.sqrt(nv / eta[mu, mu])
        rows[mu] = v
    S = np.array([rows[mu] for mu in range(n)])
    return S @ np.diag(dh), beta, S


out = []
pr = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))
pr("per k: maxrap, kappa, u used, max|h-D|, min eig Re(Lam^T Lam) over tau, max|Im q|/|q|, |q^T h^-1 q - k.k|,"
   " min pair sum/pi at tau=1, max pair sum/pi at tau=1, |Im Lambda(0)|")
for trial in range(40):
    maxrap = [0.0, 0.5, 1.0, 2.0][trial % 4]
    L = random_lorentz(rng, maxrap)
    kappa = rng.uniform(0.3, 3.0)
    k = np.linalg.solve(L.T, kappa * np.eye(n)[1])  # L^T k = kappa e_1
    kk = k @ eta @ k
    assert abs(kk - kappa ** 2) < 1e-9 * max(1, kappa ** 2)
    u = 0.5
    while True:
        ok = True
        worst = np.inf
        for tau in np.linspace(0, 1, 401):
            Lp, beta, S = build(tau, u)
            Lam = L @ Lp
            mev = np.linalg.eigvalsh((Lam.T @ Lam).real)[0]
            worst = min(worst, mev)
            if mev <= 0:
                ok = False
                break
        if ok:
            break
        u /= 2
    errh, errq, errz = 0, 0, 0
    for tau in np.linspace(0, 1, 401):
        Lp, beta, S = build(tau, u)
        assert np.allclose(S @ eta @ S.T, eta, atol=1e-10)
        Lam = L @ Lp
        h = Lam.T @ eta @ Lam
        errh = max(errh, np.max(np.abs(h - np.diag(np.exp(1j * beta)))))
        q = Lam.T @ k
        errq = max(errq, np.max(np.abs(q.imag)) / np.linalg.norm(q))
        errz = max(errz, abs(q @ np.linalg.solve(h, q) - kk))
    Lp0, _, _ = build(0.0, u)
    im0 = np.max(np.abs((L @ Lp0).imag))
    _, beta1, _ = build(1.0, u)
    ps = [beta1[i] + beta1[j] for i in range(n) for j in range(i + 1, n)]
    pr(f"{maxrap:3.1f} {kappa:6.3f} {u:8.5f} {errh:.1e} {worst:.3e} {errq:.1e} {errz:.1e} "
       f"{min(ps)/np.pi:.5f} {max(ps)/np.pi:.5f} {im0:.1e}")
open(__file__.replace('.py', '.txt'), 'w').write('\n'.join(out) + '\n')
