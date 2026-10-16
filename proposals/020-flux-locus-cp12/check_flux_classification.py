"""Package 020: flux eigenvalues (f1,f2) of the Euclidean-contracted symbol over the whole CP^{1,2} leaf (018 class H1-H5).

Claim tested (derived in proposal-r1.md, section A):
  Let y^a=M^{a5}, y^4=M^{45}, l=|y.y|^{1/2}, Q^{ab}=y4^2 eta^{ab}+y^a y^b (Gram matrix of the horizontal fields D^a in the
  ambient metric of R^{1,4}).  The vertical part F_ab(zeta)=zeta_k S^{ab}_k of [D^a,D^b] has the form
        F = Q^{1/2} omega Q^{1/2},   omega self-dual (or anti-self-dual) w.r.t. delta, fixed orientation on the leaf.
  Then (f1,f2)=(|p|+|r|,|p|-|r|) with p,r the delta-SD / delta-ASD parts of F.
  In the frame where Q=diag(a,b,m,m) (a,b the eigenvalues of Q on span(e0,yhat), m=y4^2, ab=l^2 m):
     f2/f1 = min/max of (sqrt(ab),m) for n along the axis, min/max of (sqrt(am),sqrt(bm)) for n orthogonal to it.
Checks: (1) SD property at random points, fixed sign; (2) numerics vs closed form; (3) global scan of f2/f1;
(4) the locus Sigma = {y_i=0,|y4|=l} (found by minimisation) with f1=f2 for every zeta and several fibre points;
(5) Lorentzian eta-contraction: E parallel B, |E|=l|y4||n|, |B|=y4^2|n|.
"""
import numpy as np
from scipy.optimize import minimize
from cp12_realisation import *

np.set_printoptions(precision=5, suppress=True, linewidth=170)
s = -1.0
pairs = [(A, B) for A in range(6) for B in range(A + 1, 6)]
eta4 = np.diag([-1., 1, 1, 1])


def vec(M0, C, D):
    return np.array([s * lie(C, D, A, B, M0) for (A, B) in pairs])


def structure(M0):
    D = np.array([vec(M0, a, 4) for a in range(4)])
    J = {(a, b): vec(M0, a, b) for a in range(4) for b in range(a + 1, 4)}
    Qr, _ = np.linalg.qr(D.T)
    Jp = {k: v - Qr @ (Qr.T @ v) for k, v in J.items()}
    u, sv, vh = np.linalg.svd(np.array(list(Jp.values())))
    Z = vh[:2]
    S = np.zeros((4, 4, 2))
    for (a, b), v in Jp.items():
        c = Z @ v
        S[a, b] = c
        S[b, a] = -c
    return S


def sqrtm_sym(Q):
    w, v = np.linalg.eigh(Q)
    return (v * np.sqrt(w)) @ v.T


def hodge_split(F):
    """delta-SD and ASD parts of an antisymmetric 4x4 matrix (eps_{0123}=+1)."""
    eps = np.zeros((4, 4, 4, 4))
    import itertools
    for p in itertools.permutations(range(4)):
        sgn = np.linalg.det(np.eye(4)[list(p)])
        eps[p] = sgn
    dual = 0.5 * np.einsum('abcd,cd->ab', eps, F)
    return 0.5 * (F + dual), 0.5 * (F - dual)


def amp(Fh):
    """amplitude |p| of an SD (or ASD) matrix: Fh = sum p_i eta^i -> |p| = sqrt(sum Fh_ab^2 /4)."""
    return np.sqrt(0.25 * np.sum(Fh ** 2))


def flux_ratio(F):
    Fp, Fm = hodge_split(F)
    p, r = amp(Fp), amp(Fm)
    f1, f2 = p + r, abs(p - r)
    ev = np.sort(np.abs(np.linalg.eigvals(F).imag))[::2]
    return f1, f2, ev, p, r


def Qmat(M0):
    y = M0[:4, 5]
    y4 = M0[4, 5]
    return y4 ** 2 * eta4 + np.outer(y, y), y, y4


def closed_form_ratios(M0):
    Q, y, y4 = Qmat(M0)
    ell2 = -(y @ eta4 @ y + y4 ** 2)
    ell = np.sqrt(ell2)
    T = y @ y  # delta-norm: y0^2+r^2
    disc = T ** 2 - 4 * ell2 * y4 ** 2
    lp, lm = 0.5 * (T + np.sqrt(disc)), 0.5 * (T - np.sqrt(max(disc, 0)))
    m = y4 ** 2
    ax = min(np.sqrt(lp * lm), m) / max(np.sqrt(lp * lm), m)
    pe = np.sqrt(lm / lp)
    return ell, ax, pe, (lp, lm, m)


if __name__ == "__main__":
    rng = np.random.default_rng(11)
    # --- (1)+(2): SD property, orientation sign, closed forms
    signs = []
    maxerr_sd = 0
    maxerr_cf = 0
    ratios_all = []
    npts = 300
    for t in range(npts):
        z = rand_z_pos(rng, rng.uniform(0.5, 4))
        M0 = Mfun(z)
        S = structure(M0)
        Q, y, y4 = Qmat(M0)
        Qh = sqrtm_sym(Q)
        Qhi = np.linalg.inv(Qh)
        # omega_k = Q^{-1/2} S_k Q^{-1/2}
        for k in range(2):
            om = Qhi @ S[:, :, k] @ Qhi
            Op, Om = hodge_split(om)
            if amp(Op) > amp(Om):
                signs.append(+1)
                maxerr_sd = max(maxerr_sd, amp(Om) / amp(Op))
            else:
                signs.append(-1)
                maxerr_sd = max(maxerr_sd, amp(Op) / amp(Om))
        ell, ax, pe, ev = closed_form_ratios(M0)
        # f2/f1 over the zeta circle
        rr = []
        for ph in np.linspace(0, np.pi, 91):
            F = S[:, :, 0] * np.cos(ph) + S[:, :, 1] * np.sin(ph)
            f1, f2, _, p, r = flux_ratio(F)
            rr.append(f2 / f1)
        rr = np.array(rr)
        lo, hi = min(ax, pe), max(ax, pe)
        maxerr_cf = max(maxerr_cf, max(lo - rr.min(), rr.max() - hi, 0))
        ratios_all.append((rr.min(), rr.max(), lo, hi))
    print("(1) SD-orientation signs over %d points x 2 centre dirs: all equal = %s ; worst opposite-part fraction = %.2e"
          % (npts, len(set(signs)) == 1, maxerr_sd))
    print("(2) closed-form bracket [min(ax,pe),max(ax,pe)] contains numerical f2/f1 range: max violation = %.2e" % maxerr_cf)
    ra = np.array(ratios_all)
    print("    numerical global range of f2/f1 over %d points: [%.4f, %.4f]" % (npts, ra[:, 0].min(), ra[:, 1].max()))
    # --- (3) attainment of the bracket ends (fibre point chosen so that n is along/orthogonal to axis not controlled; check extremes touched)
    touched = np.mean([(abs(r[0] - r[2]) < 1e-6 or abs(r[0] - r[3]) < 1e-6) for r in ra])
    print("    fraction of points where the numerical min equals a bracket end:", round(touched, 3))

    # --- (4) the locus Sigma: y_i=0, |y4|=l
    def obj(p, n):
        zz = p[:4] + 1j * p[4:]
        q = np.real(zz.conj() @ H @ zz)
        if q < 1e-6:
            return 1e6
        zz = zz * np.sqrt(n / q)
        M = Mfun(zz)
        y = M[:4, 5]
        y4 = M[4, 5]
        ell = n / 2.0
        return np.sum(y[1:] ** 2) + (abs(y4) - ell) ** 2
    print("(4) locus Sigma (y_i=0,|y4|=l): minimisation and f1/f2 for all zeta:")
    for trial in range(6):
        n = rng.uniform(0.8, 3.0)
        best = None
        for t in range(10):
            r = minimize(obj, rng.normal(size=8), args=(n,), method='Nelder-Mead',
                         options={'xatol': 1e-13, 'fatol': 1e-26, 'maxiter': 60000})
            if best is None or r.fun < best.fun:
                best = r
        zz = best.x[:4] + 1j * best.x[4:]
        zz = zz * np.sqrt(n / np.real(zz.conj() @ H @ zz))
        M0 = Mfun(zz)
        S = structure(M0)
        rr = []
        for ph in np.linspace(0, np.pi, 91):
            F = S[:, :, 0] * np.cos(ph) + S[:, :, 1] * np.sin(ph)
            f1, f2, _, p, r = flux_ratio(F)
            rr.append(f2 / f1)
        print("   n=%.3f residual=%.2e y=%s  |y4|/l=%.6f  f2/f1 in [%.6f, %.6f]" %
              (n, best.fun, np.round(M0[:5, 5], 4), abs(M0[4, 5]) / (n / 2), min(rr), max(rr)))
    # slightly displaced from Sigma: linear (conical) growth of |f1-f2|/(f1+f2)
    print("    displacement from Sigma: relative tachyon depth |f1-f2|/(f1+f2) = |r|/|p| vs displacement")
    n = 2.0
    ell = n / 2
    def point_from_y(yv):
        """find z with prescribed y^A (A<=4) by minimisation"""
        def o(p):
            zz = p[:4] + 1j * p[4:]
            q = np.real(zz.conj() @ H @ zz)
            if q < 1e-6:
                return 1e6
            zz = zz * np.sqrt(n / q)
            M = Mfun(zz)
            return np.sum((M[:5, 5] - yv) ** 2)
        best = None
        for t in range(12):
            r = minimize(o, rng.normal(size=8), method='Nelder-Mead', options={'xatol': 1e-13, 'fatol': 1e-28, 'maxiter': 80000})
            if best is None or r.fun < best.fun:
                best = r
        zz = best.x[:4] + 1j * best.x[4:]
        zz = zz * np.sqrt(n / np.real(zz.conj() @ H @ zz))
        return Mfun(zz), best.fun
    for d in (0.2, 0.1, 0.05):
        y4 = ell * (1 + d)
        y0 = np.sqrt(ell ** 2 + y4 ** 2)
        M0, res = point_from_y(np.array([y0, 0, 0, 0, y4]))
        S = structure(M0)
        vals = []
        for ph in np.linspace(0, np.pi, 91):
            F = S[:, :, 0] * np.cos(ph) + S[:, :, 1] * np.sin(ph)
            f1, f2, _, p, r = flux_ratio(F)
            vals.append(r / p)
        print("   y4=l(1+%.2f): res=%.1e  |r|/|p| in [%.5f,%.5f]  (closed form l-direction: |l-y4|/(l+y4)=%.5f)" %
              (d, res, min(vals), max(vals), abs(ell - y4) / (ell + y4)))

    # --- (5) Lorentzian eta contraction: eigenvalues of F eta; E and B
    print("(5) Lorentzian eta-contraction at 4 random points: eigenvalues of F.eta for unit zeta, and l|y4|, y4^2 scaling")
    for t in range(4):
        z = rand_z_pos(rng, rng.uniform(0.5, 4))
        M0 = Mfun(z)
        S = structure(M0)
        Q, y, y4 = Qmat(M0)
        ell = np.sqrt(-(y @ eta4 @ y + y4 ** 2))
        F = S[:, :, 0]
        ev = np.sort_complex(np.linalg.eigvals(F @ eta4))
        # invariants I=B^2-E^2 =  -(1/2)tr(F eta F eta)/... compare ratio E/B=l/|y4|
        lam_re = np.max(np.abs(ev.real))
        lam_im = np.max(np.abs(ev.imag))
        print("   y4/l=%.3f  real/imag eigenvalue ratio = %.5f  expected l/|y4| = %.5f" % (abs(y4) / ell, lam_re / lam_im, ell / abs(y4)))
