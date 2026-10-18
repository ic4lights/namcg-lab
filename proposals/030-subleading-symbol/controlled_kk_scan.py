"""030 script 13: controlled KK model, dependence of the decomposition residual on the width of the NON-kernel part of the window (P4 -> f P4, f -> 0 = wide window)."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from tail_coeffs import *
from controlled_kk import QEH_kk
eta = np.diag(eta_a)
rng = np.random.default_rng(2)
for trial in range(3):
    kH = rng.normal(size=4); yH = rng.normal(size=4); yH = yH - kH * (kH @ yH) / (kH @ kH); YV = rng.normal(size=2)
    P4 = rng.normal(size=(4, 4)); P4 = P4 @ P4.T + 0.5 * np.eye(4)
    Pk = rng.normal(size=(2, 2)); Pk = Pk @ Pk.T + 0.5 * np.eye(2)
    for f in [1.0, 0.1, 0.01, 0.001]:
        P = np.zeros((6, 6)); P[:4, :4] = f * P4; P[4:, 4:] = Pk
        W = np.zeros((4, 6)); W[:, :4] = np.eye(4)
        dat = dict(W=W, Y=np.concatenate([yH, YV]), P=P, kappa=kH)
        Q0, Q1, Q2 = [to_np(Q) for Q in forms(dat)]
        Im1 = Q1.imag
        kl = eta @ kH; k2 = kH @ eta @ kH
        Gm = k2 * eta - np.outer(kl, kl)
        QE = QEH_kk(yH, kH)
        Bm = np.array([QE.flatten(), Gm.flatten()]).T
        c, *_ = np.linalg.lstsq(Bm, Im1.flatten(), rcond=None)
        r = np.linalg.norm(Bm @ c - Im1.flatten()) / np.linalg.norm(Im1)
        print("trial %d  P4 scale %.3f: residual of Im Q1 = lam1 QEH + lam2 Gm: %.3e ; lam1=%.5e ; lam2=%.4e" % (trial, f, r, c[0], c[1]))
