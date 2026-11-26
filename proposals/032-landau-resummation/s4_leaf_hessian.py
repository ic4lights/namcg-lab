"""032 script 4: leaf geometry of the resummed leading-symbol mass term.
(1) On the kernel plane of sigma(Box) (the centre variable k of the nilpotent model) the flux F_ab(k) has f_e/f_m = 1/sinh(tau) = l/|y^4| independent of the direction of k
    (028 closed form re-checked at random orbit points).
(2) The leading nilpotent coefficient depends on A only through F: g(F) := finite part of i int ds Theta  (s2_mass_term, g = pi[b S(b/a) + i a S(a/b)]), a homogeneous function of degree 1.
    Under A^a = eps alpha^a cos(q.y) the centre-valued field strength changes by Q_ab = zeta_Y(k) (kappa_a alpha_b - kappa_b alpha_a), zeta_Y = k(Y).
    Second variation (Maxwell-type): q(alpha) = < D^2 g(F(k)) [Q,Q] >_k, average over the direction of k with the Gaussian window of Delta_{3/4} restricted to the kernel plane,
    weight  p(phi)^{-3/2}  (radial integral of a degree-1 homogeneous integrand).  Reported: eigenvalues (signs) of q on alpha mod kappa, and the residual of the best fit to the
    covariant Maxwell structure G = (kappa.kappa) eta - kappa kappa  (isotropic leaf-independent form of the unresummed c0)."""
import numpy as np, mpmath as mp
from z4_large_s import *
rng = np.random.default_rng(21)
etan = eta4

def Sfun(r):
    n = np.arange(1, 400)
    return np.sum((-1.0) ** n / np.sinh(n * np.pi * r))

def g_ab(a, b):
    return np.pi * (b * Sfun(b / a) + 1j * a * Sfun(a / b))

def ab_of(F):
    ev = np.linalg.eigvals(F @ etan)
    return np.max(np.abs(ev.real)), np.max(np.abs(ev.imag))

def g_of_F(F):
    a, b = ab_of(F)
    return g_ab(a, b)

def d2g(F, Q, h=2e-3):
    f = lambda t: g_of_F(F + t * Q)
    cd = lambda hh: (f(hh) - 2 * f(0.0) + f(-hh)) / hh ** 2
    return (4 * cd(h / 2) - cd(h)) / 3

if __name__ == "__main__":
    print("point | a_=|y4|/l | f_e/f_m on kernel plane (min..max over directions) | 1/a_")
    data = []
    for t in range(4):
        z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
        Fv, Ev, Bv, W, c = flux_vectors(M0)
        Pi, W, Yb, c, E = fields(M0)
        wf = window_forms(M0); P = wf['P']
        S = sum(eta4[a, a] * np.outer(W[a], W[a]) for a in range(4))
        w_, v_ = np.linalg.eigh(S); N = v_[:, np.abs(w_) < 1e-9 * np.abs(w_).max()]
        y = M0[:5, 5]; a_ = abs(M0[4, 5]) / np.sqrt(-(y @ np.diag([-1., 1, 1, 1, 1]) @ y))
        rat = []
        for ph in np.linspace(0, 2 * np.pi, 24, endpoint=False):
            xi = N @ np.array([np.cos(ph), np.sin(ph)])
            F = np.einsum('abk,k->ab', Fv, xi); fe, fm = fe_fm(F)
            rat.append(fe / fm)
        print("  %d | %.4f | %.5f .. %.5f | %.5f" % (t, a_, min(rat), max(rat), 1 / a_))
        data.append((M0, Fv, N, P, Yb, a_))
    print("\nResummed Maxwell-type quadratic form q(alpha) (leaf-averaged), Re and Im parts")
    for (M0, Fv, N, P, Yb, a_) in data:
        q = rng.normal(size=4)
        Yq = sum(q[m] * Yb[m] for m in range(4))
        Pi, W, Yb2, c, E = fields(M0)
        dphi = sum(q[m] * E[:, pidx[(m, 5)]] for m in range(4))
        kappa = np.array([dphi @ W[a] for a in range(4)])
        phis = np.linspace(0, 2 * np.pi, 16, endpoint=False)
        Hq = np.zeros((4, 4), complex); wsum = 0
        for ph in phis:
            kd = np.array([np.cos(ph), np.sin(ph)]); xi = N @ kd
            F = np.einsum('abk,k->ab', Fv, xi)
            zeta = Yq @ xi
            p = kd @ (N.T @ P @ N) @ kd
            wgt = p ** -1.5
            Mq = np.zeros((4, 4), complex)
            Eb = np.eye(4)
            def val(al):
                Qm = zeta * (np.outer(kappa, al) - np.outer(al, kappa))
                return d2g(F, Qm)
            d = [val(Eb[i]) for i in range(4)]
            for i in range(4):
                Mq[i, i] = d[i]
                for j in range(i + 1, 4):
                    Mq[i, j] = Mq[j, i] = (val(Eb[i] + Eb[j]) - d[i] - d[j]) / 2
            Hq += wgt * Mq; wsum += wgt
        Hq /= wsum
        Gm = (kappa @ etan @ kappa) * etan - np.outer(etan @ kappa, etan @ kappa)
        # covariant structure in the same index placement: alpha lower index -> quadratic form G^{ab} = (kappa.kappa) eta^{ab} - kappa^a kappa^b
        for name, part in (("Re", Hq.real), ("Im", Hq.imag)):
            lam = np.sum(part * Gm) / np.sum(Gm * Gm)
            res = np.linalg.norm(part - lam * Gm) / np.linalg.norm(part)
            # quotient by kappa^up? kernel of q is alpha ~ kappa (lower index alpha = kappa): check
            gauge = np.linalg.norm(part @ kappa) / (np.linalg.norm(part) * np.linalg.norm(kappa))
            # signs on the 3-dim quotient: restrict to a complement of kappa
            Qb = np.linalg.svd(kappa[None, :])[2][1:]
            ev = np.linalg.eigvalsh(Qb @ part @ Qb.T)
            print("   a_=%.3f %s: gauge test |q kappa|/(|q||kappa|) = %.1e ; eigenvalues on quotient %s ; best fit to lambda*G residual %.3f (rel.)" % (a_, name, gauge, np.round(ev / np.abs(ev).max(), 3), res))
