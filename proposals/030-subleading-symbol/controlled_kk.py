"""030 script 12: controlled Kaluza-Klein test of the decomposition of the 1/s tail.
n = 6 momentum space, w0_a = e_a (a=1..4), kernel directions e_5, e_6; Y = (y_H, Y_V) with kappa = (kappa_H, 0) and y_H.kappa_H = 0 (Hamiltonian-like, divergence free);
window P = blockdiag(P_4, P_k) (decoupled) or with an off-diagonal block of relative strength t.  Base metric from y_H (canonical: W_a(y^mu) = delta, gbar0 = eta).
Reports the relative residual of  Im Q1 = lam1 Q_EH[y_H] + lam2 Gm  vs the coupling t, and the Maxwell tensor test for Q0."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from tail_coeffs import *
from eh_decomposition import FP_avg_g
eta = np.diag(eta_a)

def QEH_kk(yH, kH):
    gl = eta.copy()
    Q = np.zeros((4, 4))
    def A1(alpha):
        u = eta_a * alpha
        G1 = -(np.outer(u, yH) + np.outer(yH, u))
        h = -gl @ G1 @ gl
        fp, qq, trh = FP_avg_g(h, kH, gl)
        return fp / 6 - qq * trh ** 2 / 32
    E_ = np.eye(4)
    d = [A1(E_[i]) for i in range(4)]
    for i in range(4):
        Q[i, i] = d[i]
        for j in range(i + 1, 4):
            Q[i, j] = Q[j, i] = (A1(E_[i] + E_[j]) - d[i] - d[j]) / 2
    return Q

rng = np.random.default_rng(2)
for trial in range(2):
    kH = rng.normal(size=4); yH = rng.normal(size=4); yH = yH - kH * (kH @ yH) / (kH @ kH); YV = rng.normal(size=2)
    P4 = rng.normal(size=(4, 4)); P4 = P4 @ P4.T + 0.5 * np.eye(4)
    Pk = rng.normal(size=(2, 2)); Pk = Pk @ Pk.T + 0.5 * np.eye(2)
    Off = rng.normal(size=(4, 2))
    for t in [0.0, 0.05, 0.2, 0.5]:
        P = np.zeros((6, 6)); P[:4, :4] = P4; P[4:, 4:] = Pk; P[:4, 4:] = t * Off; P[4:, :4] = t * Off.T
        if np.min(np.linalg.eigvalsh(P)) <= 0:
            print("  t=%.2f: P not positive, skipped" % t); continue
        W = np.zeros((4, 6)); W[:, :4] = np.eye(4)
        Y = np.concatenate([yH, YV]); kappa = np.concatenate([kH, [0, 0]])
        dat = dict(W=W, Y=Y, P=P, kappa=kH)
        Q0, Q1, Q2 = [to_np(Q) for Q in forms(dat)]
        Im1 = Q1.imag
        kl = eta @ kH; k2 = kH @ eta @ kH
        Gm = k2 * eta - np.outer(kl, kl)
        QE = QEH_kk(yH, kH)
        Bm = np.array([QE.flatten(), Gm.flatten()]).T
        c, *_ = np.linalg.lstsq(Bm, Im1.flatten(), rcond=None)
        r = np.linalg.norm(Bm @ c - Im1.flatten()) / np.linalg.norm(Im1)
        lam0 = np.sum(Q0.real * Gm) / np.sum(Gm * Gm); res0 = np.linalg.norm(Q0.real - lam0 * Gm) / np.linalg.norm(Q0.real)
        print("trial %d t=%.2f: Q0 ~ Gm residual %.1e | Im Q1 = lam1 QEH + lam2 Gm: residual %.2e (lam1=%.4e, lam2=%.4e)" % (trial, t, res0, r, c[0], c[1]))
