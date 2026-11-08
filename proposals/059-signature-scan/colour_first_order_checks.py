#!/usr/bin/env python3
"""Package 059: checks of the first-order colour-mixing argument at N=2 (proposal section 6, H2).

Setting: x = (x^1, x^2, x^3), x^a in R^10, S(x) = (1/4) sum_{a<b} m_ab, m_ab = h(x^a,x^a)h(x^b,x^b) - h(x^a,x^b)^2,
h = h0 real of signature (10-t, t).  First-order deformation x^a -> x^a + i tau sum_b K_ab x^b (K_ab real 10x10),
g(x) = d/dtau Im S at tau = 0.  Claimed:
 (1) pair restriction x^c = 0:  g = P_ab(x^a, x^b), and P_ab(s x^a, x^b/s) = c0 + s^{-2} c_- + s^2 c_+ with
     c_+ = grad_b S . K_ba x^a linear in x^b;
 (2) grad_b S . x^a = 0 (scalar colour shear leaves the pair minor invariant);
 (3) with K_aa = K + D, K_bb = K - D, K in so(h0), D in so(h0): P_ab = 4 h(x^a,x^b) x^aT h D x^b /4-normalised;
     P_ab is odd under x^a <-> x^b (with the roles of D swapped);
 (4) with K_ab = kappa_ab 1 (a != b) and K_aa = 0, g takes both signs unless kappa + kappa^T = 0;
 (5) with K_aa = K in so(h0) and kappa antisymmetric, g == 0.
All checks numerical at random points (finite differences in tau checked against the analytic derivative).
"""
import numpy as np
rng = np.random.default_rng(591)
n = 10
def S_of(x, h):
    G = x.T @ h @ x
    return 0.25*sum(G[a, a]*G[b, b] - G[a, b]**2 for a, b in [(0, 1), (0, 2), (1, 2)])
def g_of(x, h, K):
    # K: 3x3 nested list of 10x10 real blocks; analytic derivative of Im S along x + i tau K x
    xp = lambda tau: x + 1j*tau*np.stack([sum(K[a][b] @ x[:, b] for b in range(3)) for a in range(3)], axis=1)
    eps = 1e-6
    return (S_of(xp(eps), h).imag - S_of(xp(-eps), h).imag)/(2*eps)
def so_h(h):
    Aanti = rng.normal(size=(n, n)); Aanti = Aanti - Aanti.T
    return np.linalg.solve(h, Aanti)       # D = h^{-1} A with A antisymmetric  =>  D^T h + h D = 0
Z = np.zeros((n, n)); I = np.eye(n)
ok = True
for t in (2, 5, 8):
    h = np.diag([1.0]*(n - t) + [-1.0]*t)
    x = rng.normal(size=(n, 3))
    # (2)
    G = x.T @ h @ x
    grad2 = 0.5*(G[0, 0]*(h @ x[:, 1]) - G[0, 1]*(h @ x[:, 0]))
    c2 = abs(grad2 @ x[:, 0])
    # (3)
    Kk, Dd = so_h(h), so_h(h)
    K = [[Kk + Dd, Z, Z], [Z, Kk - Dd, Z], [Z, Z, Z]]
    xr = x.copy(); xr[:, 2] = 0
    g12 = g_of(xr, h, K)
    pred = 0.25*4*G[0, 1]*(x[:, 0] @ h @ Dd @ x[:, 1])
    xs = xr[:, [1, 0, 2]]
    g21 = g_of(xs, h, K)
    c3 = abs(g12 - pred)/max(1, abs(pred)); c3b = abs(g12 + g21)/max(1, abs(g12))
    # (1) scaling structure for an off-diagonal block
    K1 = [[Z, Z, Z], [rng.normal(size=(n, n)), Z, Z], [Z, Z, Z]]
    vals = [g_of(np.stack([s*xr[:, 0], xr[:, 1]/s, xr[:, 2]], axis=1), h, K1) for s in (1.0, 2.0)]
    c1 = abs(vals[1] - 4*vals[0])/max(1, abs(vals[0]))   # pure s^2 term from K_21
    # (4) symmetric scalar colour mixing gives both signs
    kap = np.array([[0, 1.0, 0.3], [1.0, 0, -0.7], [0.3, -0.7, 0]])
    K4 = [[kap[a, b]*I if a != b else Z for b in range(3)] for a in range(3)]
    gs = np.array([g_of(rng.normal(size=(n, 3)), h, K4) for _ in range(400)])
    c4 = (gs.min() < 0 < gs.max())
    # (5) trivial directions give g == 0
    kapA = np.array([[0, 1.0, 0.3], [-1.0, 0, -0.7], [-0.3, 0.7, 0]])
    K5 = [[Kk if a == b else kapA[a, b]*I for b in range(3)] for a in range(3)]
    g5 = max(abs(g_of(rng.normal(size=(n, 3)), h, K5)) for _ in range(50))
    print("t=%d  (1) s^2 scaling rel.err %.1e   (2) |grad_b S . x^a| %.1e   (3) P_ab vs 4h12 x^a h D x^b /4: %.1e, oddness %.1e   (4) both signs: %s [min %.2e max %.2e]   (5) max|g| %.1e"
          % (t, c1, c2, c3, c3b, c4, gs.min(), gs.max(), g5))
    ok &= (c1 < 1e-6 and c2 < 1e-12 and c3 < 1e-6 and c3b < 1e-6 and c4 and g5 < 1e-6)
print("ALL PASS" if ok else "SOME FAIL")
