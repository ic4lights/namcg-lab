"""030 script 16: Lorentz covariance of the Einstein-Hilbert-form coefficient after averaging over the fibre.
Total quadratic form = int dmu_Liouville  Pf(Pi) * N(point);  at a fixed base point and fixed base covector q the fibre points are g.M0 (g in the compact stabiliser SO(4) of y, Haar measure),
N = lam1(point) * Q_EH(point) in the wide-horizontal-window limit (eh_limit.py).  Reports, for q.q = +1 and the boost q = (sinh th, cosh th, 0, 0) at a base point with y^i = 0:
  (i) the fibre average Qbar_ab(th) = sum w Q_EH / N_f (w = Pf*lam1),
  (ii) its decomposition on the covariant gauge-invariant tensor  Gq = q.q eta - q q  (coefficient c_cov) and the remainder,
  (iii) the remainder's size and the dependence of c_cov on th (Lorentz violation through y^mu).
Also: <t t> over the fibre vs (|t|^2/3)(eta - y y / y.y)  (uniform sphere test)."""
import sys, numpy as np, scipy.linalg as sl
sys.dont_write_bytecode = True
from geom28 import *
from tail_coeffs import frozen_data
from eh_decomposition import QEH
from eh_limit import window_family
eta5 = np.diag([-1., 1, 1, 1, 1])
eta4 = np.diag([-1., 1, 1, 1])

def haar_so4(rng):
    A = rng.normal(size=(4, 4)); Q, R = np.linalg.qr(A); Q = Q * np.sign(np.diag(R))
    if np.linalg.det(Q) < 0: Q[:, 0] = -Q[:, 0]
    return Q

def fibre_points(M0, n, rng):
    y = M0[:5, 5].copy()
    Py = np.outer(y, y @ eta5) / (y @ eta5 @ y)
    # eta5-orthonormal basis of y-perp
    Bs = []
    cand = list(np.eye(5))
    for e in cand:
        e = e - Py @ e
        for b in Bs:
            e = e - (b @ eta5 @ e) * b
        nn = e @ eta5 @ e
        if nn > 1e-9:
            Bs.append(e / np.sqrt(nn))
        if len(Bs) == 4: break
    B = np.array(Bs).T                                          # (5,4)
    out = []
    for i in range(n):
        R = haar_so4(rng)
        g5 = Py + B @ R @ B.T @ eta5
        g6 = np.eye(6); g6[:5, :5] = g5
        out.append(g6 @ M0 @ g6.T)
    return out

if __name__ == "__main__":
    rng = np.random.default_rng(17)
    z = point_y_spatial_zero(0, n=1.0); M0 = Mfun(z)
    y = M0[:4, 5]
    print("base point: y^mu =", np.round(y, 4), " y.y =", round(float(y @ eta4 @ y), 4), " M^{45} =", round(float(M0[4, 5]), 4))
    Mf = fibre_points(M0, 300, rng)
    # sanity: y^mu invariant along the fibre
    print("max |y^mu(fibre) - y^mu| =", max(np.abs(M[:4, 5] - y).max() for M in Mf))
    tt = np.mean([np.outer(M[:4, 4], M[:4, 4]) for M in Mf], axis=0)
    tn = np.mean([M[:4, 4] @ eta4 @ M[:4, 4] for M in Mf])
    Pperp = np.linalg.inv(eta4) - np.outer(y, y) / (y @ eta4 @ y)
    print("<t t> vs (|t|^2/3) P_perp: relative deviation = %.3f (300 Haar points)" % (np.linalg.norm(tt - tn / 3 * Pperp) / np.linalg.norm(tt)))
    res = []
    for th in [0.0, 0.4, 0.8, 1.2]:
        q = np.array([np.sinh(th), np.cosh(th), 0, 0])
        qq = q @ eta4 @ q; ql = eta4 @ q
        Gq = qq * eta4 - np.outer(ql, ql)
        num = 0; den = 0
        for M in Mf:
            dat = frozen_data(M, q)
            QE, gbar0, v = QEH(dat, q)
            Pf_, lam1, Lam, V = window_family(dat, 0.0)
            Pi_ = poisson_bivector(M)[0]
            w = np.sqrt(abs(np.linalg.det(Pi_))) * lam1
            num = num + w * QE; den += w
        Qb = num / den
        ccov = np.sum(Qb * Gq) / np.sum(Gq * Gq)
        rem = np.linalg.norm(Qb - ccov * Gq) / np.linalg.norm(Qb)
        kk = eta4 @ q; gauge = np.linalg.norm(Qb @ kk) / (np.linalg.norm(Qb) * np.linalg.norm(kk))
        print("th=%.2f  q.q=%.3f q.y=%.4f | fibre-averaged Q_EH: c_cov = %.5e, remainder/|Q| = %.3e, gauge test = %.1e, eigenvalues(Qbar/|Qbar|) = %s" % (th, qq, q @ y, ccov, rem, gauge, np.round(np.linalg.eigvalsh(Qb) / np.linalg.norm(Qb), 3)))
        res.append((th, ccov))
    print("c_cov(th)/c_cov(0) =", [round(r[1] / res[0][1], 4) for r in res])
