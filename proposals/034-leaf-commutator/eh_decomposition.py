"""030 script 11: does the 1/s tail c1 of the 6D integrand contain the Einstein-Hilbert (Seeley-DeWitt a_1) form of the CANONICAL base metric, plus the Maxwell tensor?
Canonical base metric: gbar^{mu nu} = eta^{ab} W_a(y^mu) W_b(y^nu) (push-forward of the degenerate cometric by dy^mu, vertical directions drop out); under A:
  W_a -> W_a - eps S alpha_a Y,  so  G1 = -S (u v^T + v u^T),  u^mu = sum_a eta_a alpha_a W_a(y^mu),  v^mu = Y(y^mu) = {phi, y^mu}  (v.q = 0 by antisymmetry).
Prediction (non-degenerate case, validated in validate_seeley_4d.py):  c1 ~ i (4 pi)^-2 rho <sqrt g a_1>_{eps^2}[gbar],  <sqrt g a_1> = FP[h]/6 - (1/32)(q.q)_g (tr h)^2,  with rho a (window/kernel) constant.
Fit: Im Q1 = lam1 * Q_EH + lam2 * Gm  (Gm = Maxwell tensor), reporting the relative residual; also the fit with Gm alone and with Q_EH alone."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from tail_coeffs import *
from tail_structure import analyse
eta = np.diag(eta_a)

def FP_avg_g(h, q, gl):
    gu = np.linalg.inv(gl)
    qU = gu @ q
    hU = gu @ h @ gu
    trh = np.trace(gu @ h)
    qq = q @ gu @ q
    t1 = -qq * np.sum(h * hU)
    qh = qU @ h
    t2 = 2 * (qh @ gu @ qh)
    t3 = -2 * (qU @ h @ qU) * trh
    t4 = qq * trh ** 2
    return (t1 + t2 + t3 + t4) / 8.0, qq, trh

def QEH(dat, q):
    W, Y, E = dat['W'], dat['Y'], dat['E']
    b = np.array([E[:, pidx[(m, 5)]] for m in range(4)])           # (4,6) base covectors dy^mu
    Wy = b @ W.T                                                    # (mu, a) = W_a(y^mu)
    gbar0 = Wy @ eta @ Wy.T                                         # upper-index base metric
    gl = np.linalg.inv(gbar0)
    v = b @ Y
    Q = np.zeros((4, 4))
    def A1(alpha):
        u = Wy @ (eta_a * alpha)
        G1 = -(np.outer(u, v) + np.outer(v, u))
        h = -gl @ G1 @ gl
        fp, qq, trh = FP_avg_g(h, q, gl)
        return fp / 6 - qq * trh ** 2 / 32
    E_ = np.eye(4)
    d = [A1(E_[i]) for i in range(4)]
    for i in range(4):
        Q[i, i] = d[i]
        for j in range(i + 1, 4):
            Q[i, j] = Q[j, i] = (A1(E_[i] + E_[j]) - d[i] - d[j]) / 2
    return Q, gbar0, v

if __name__ == "__main__":
    rng = np.random.default_rng(31)
    for t in range(8):
        z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
        q = rng.normal(size=4)
        out = analyse(M0, q, verbose=False)
        dat = out['dat']
        Q1 = out['Q1']
        kap = dat['kappa']; kl = eta @ kap; k2 = kap @ eta @ kap
        Gm = k2 * eta - np.outer(kl, kl)
        QE, gbar0, v = QEH(dat, q)
        # base check: v.q = 0 and gbar0 ~ m^2 eta
        m = M0[4, 5]
        chk = np.abs(gbar0 - m ** 2 * np.diag([-1., 1, 1, 1])).max()
        def fit(basis):
            Bm = np.array([b.flatten() for b in basis]).T
            c, *_ = np.linalg.lstsq(Bm, Q1.flatten(), rcond=None)
            return c, np.linalg.norm(Bm @ c - Q1.flatten()) / np.linalg.norm(Q1)
        c2, r2 = fit([QE, Gm]); cE, rE = fit([QE]); cG, rG = fit([Gm])
        print("point %d: |gbar0 - m^2 eta| = %.1e, v.q = %.1e | residual: EH+Maxwell %.3e, EH only %.3e, Maxwell only %.3e | lam1 = %.4e, lam2 = %.4e" % (t, chk, v @ q, r2, rE, rG, c2[0], c2[1]))
