"""032 script 5: validation of engine.py.
(A) F = 0, pure gauge field: T2/Theta -> (i s)^2 (-1/12) <F_ab F^ab>  with F_ab = n-field strength: a_b = eps n_b sin(phi), F_ab = eps cos(phi)(kappa_a n_b - kappa_b n_a),
    <cos^2> = 1/2, in the term of order kappa^2: T2/Theta = (s^2/12) * (1/2) F_ab F^ab / eps^2 (Lorentzian t = i s, e^{-t Delta}); other orders in kappa are polynomial corrections.
(B) F != 0, pure gauge, m = 0:  gauge invariance n_a -> n_a + lambda kappa_a (exact: Omega_a shifted by a pure-gauge x-dependent phase because the metric is untouched).
(C) F != 0, kappa -> 0, pure gauge: T2/Theta -> (1/4) d^2/dt^2 Theta(F + t Q)/Theta(F),  Q_ab = kappa_a n_b - kappa_b n_a  (constant-field limit).
(D) F != 0, kappa -> 0, pure vielbein m = -alpha y^T: constant vielbein limit, T2/Theta -> (1/2)(1/2) d^2/d eps^2 [ |det(1+eps m)|^{-1} Theta(F') ]/Theta(F),  F' = M F M^T, M = 1 + eps m.
(E) F = 0, vielbein: the O(s) coefficient of T2/Theta_0 at order kappa^2 m^2 is proportional to the proposal-030 tensor A(alpha,y,kappa) (same constant for random draws)."""
import numpy as np, mpmath as mp, sys
from engine import *
rng = np.random.default_rng(7)
mp.mp.dps = 30

def theta_F(F, s):
    a, b = theta_ab(F)
    s = complex(s)
    return -1j * a * b / (16 * np.pi ** 2 * np.sinh(s * a) * np.sin(s * b))

def d2(f, h=2e-3):
    # Richardson-extrapolated central second difference at 0
    def cd(h):
        return (f(h) - 2 * f(0.0) + f(-h)) / h ** 2
    return (4 * cd(h / 2) - cd(h)) / 3

def rand_F(fe, fm):
    # random Lorentz frame (boost x rotation) applied to block F (lower indices): F' = L^{-T} F L^{-1} with L in SO(3,1)
    from scipy.linalg import expm
    gens = []
    for i in range(1, 4):
        B = np.zeros((4, 4)); B[0, i] = B[i, 0] = 1; gens.append(B)
    for (i, j) in [(1, 2), (1, 3), (2, 3)]:
        R = np.zeros((4, 4)); R[i, j] = 1; R[j, i] = -1; gens.append(R)
    X = sum(rng.normal() * 0.4 * g for g in gens)
    L = expm(X)
    F0 = np.zeros((4, 4)); F0[0, 1] = fe; F0[1, 0] = -fe; F0[2, 3] = fm; F0[3, 2] = -fm
    Li = np.linalg.inv(L)
    return Li.T @ F0 @ Li, L

def rand_perp(kappa):
    kup = eta @ kappa
    v = rng.normal(size=4)
    return v - kup * (v @ kappa) / (kup @ kappa)       # y with y.kappa = 0   (y upper index, y^b kappa_b = 0)

if __name__ == "__main__":
    print("(A) F=0 gauge Maxwell coefficient")
    for s in [0.5, 1.3 * np.exp(-0.4j)]:
        kappa = rng.normal(size=4); n = rng.normal(size=4); m = np.zeros((4, 4))
        lam = [1e-2, 2e-2, 3e-2, 4e-2]
        vals = [second_order(np.zeros((4, 4)), l * kappa, m, n, s) for l in lam]
        c2 = np.polyfit([l ** 2 for l in lam], vals, 3)[-2]       # coefficient of l^2
        Fq = np.outer(kappa, n) - np.outer(n, kappa)
        FF = np.einsum('ab,ac,bd,cd->', Fq, eta, eta, Fq) if False else np.einsum('ab,cd,ac,bd->', Fq, Fq, eta, eta)
        pred = s ** 2 / 12 * 0.5 * FF
        print("   s=%s : coefficient of kappa^2 = %s ; prediction (s^2/24) F_ab F^ab = %s ; ratio %.10f" % (np.round(s, 3), np.round(c2, 8), np.round(pred, 8), (c2 / pred).real))
    print("(B) gauge invariance at F != 0 (m = 0)")
    for (fe, fm) in [(0.7, 1.3), (0.2, 0.5)]:
        F, L = rand_F(fe, fm)
        s = 0.8 * np.exp(-0.5j)
        kappa = rng.normal(size=4) * 0.7; n = rng.normal(size=4)
        t0 = second_order(F, kappa, np.zeros((4, 4)), n, s)
        t1 = second_order(F, kappa, np.zeros((4, 4)), n + 0.9 * kappa, s)
        print("   (fe,fm)=(%.1f,%.1f): T2/Theta = %s ; shifted n_a -> n_a + 0.9 kappa_a: %s ; |diff| = %.2e" % (fe, fm, np.round(t0, 10), np.round(t1, 10), abs(t0 - t1)))
    print("(C) kappa -> 0 constant-field limit, pure gauge")
    for (fe, fm) in [(0.7, 1.3), (0.6, 0.3)]:
        F, L = rand_F(fe, fm)
        s = 0.9 * np.exp(-0.5j)
        kappa0 = rng.normal(size=4); n = rng.normal(size=4)
        Q = np.outer(kappa0, n) - np.outer(n, kappa0)
        d2v = d2(lambda t: theta_F(F + t * Q, s)) / theta_F(F, s)
        for lam in [1e-2, 5e-3]:
            val = second_order(F, lam * kappa0, np.zeros((4, 4)), n, s)
            print("   (fe,fm)=(%.1f,%.1f) lam=%.0e : T2/Theta / lam^2 = %s ; (1/4) D^2Theta[Q,Q]/Theta = %s" % (fe, fm, lam, np.round(val / lam ** 2, 8), np.round(d2v / 4, 8)))
    print("(D) kappa -> 0 constant-vielbein limit")
    for (fe, fm) in [(0.7, 1.3), (0.6, 0.3)]:
        F, L = rand_F(fe, fm)
        s = 0.9 * np.exp(-0.5j)
        kappa = rng.normal(size=4); alpha = rng.normal(size=4); y = rand_perp(kappa)
        m = -np.outer(alpha, y)
        def Tm(e):
            Mx = np.eye(4) + e * m
            Fp = Mx @ F @ Mx.T
            return theta_F(Fp, s) / abs(np.linalg.det(Mx))
        d2v = d2(Tm) / theta_F(F, s)
        for lam in [1e-3, 3e-4]:
            # kappa small with y.kappa = 0 preserved (y fixed, kappa scaled)
            val = second_order(F, lam * kappa, m, np.zeros(4), s)
            print("   (fe,fm)=(%.1f,%.1f) lam=%.0e : T2/Theta = %s ; (1/4) d^2/de^2 [det^-1 Theta(F')]/Theta = %s" % (fe, fm, lam, np.round(val, 8), np.round(d2v / 4, 8)))
    print("(E) F=0 vielbein: s-linear coefficient vs tensor A")
    ratios = []
    for t in range(5):
        kappa = rng.normal(size=4); alpha = rng.normal(size=4); y = rand_perp(kappa)
        m = -np.outer(alpha, y)
        # exact polynomial in lam=scale of (kappa) at fixed m: take kappa^2 coefficient; and the s-expansion: T2/Theta_0 = c0 + c1 s + ...
        def coeff_k2(s):
            lam = [1e-2, 2e-2, 3e-2, 4e-2]
            vals = [second_order(np.zeros((4, 4)), l * kappa, m, np.zeros(4), s) for l in lam]
            return np.polyfit([l ** 2 for l in lam], vals, 3)[-2]
        ss = [0.2, 0.4, 0.6, 0.8, 1.0]
        cs = np.array([coeff_k2(s) for s in ss])
        pc = np.polyfit(ss, cs, 4)[::-1]            # c0, c1, c2, ...
        # tensor A with alpha upper index (alpha^a), y upper (y^b), kappa lower: a_mu = alpha_lower, v = y_up, q = kappa_lower
        al_lo = eta @ alpha; q = kappa; v = y
        qa = q @ alpha; q2 = q @ eta @ q; a2 = al_lo @ alpha; v2 = v @ eta @ v; av = al_lo @ v
        A = (1 / 24) * (v2 * (qa ** 2 - q2 * a2) - 2 * q2 * av ** 2)
        ratios.append(pc[1] / A)
        print("   draw %d: T2/Theta0 |_{kappa^2} = %s + %s s + %s s^2 + ... ; c1/A = %s" % (t, np.round(pc[0], 8), np.round(pc[1], 8), np.round(pc[2], 8), np.round(pc[1] / A, 8)))
    print("   c1/A spread:", np.round(np.array(ratios), 8))
