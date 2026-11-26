"""030 script 14: the wide-horizontal-window limit on CP^{1,2}.
Coordinates on covector space adapted to the splitting T = H + V', H = span{W_a}, V' = vertical (fibre) tangent space = common kernel of the four covectors dy^mu (dy^mu(v) = 0):
   xi' = Lam xi,  Lam rows = (W_a [4], v_k [2]),  i.e. omega_a = xi(W_a), xi_k = xi(v_k).   P' = Lam^{-T} P Lam^{-1}.
Window family P_f = Lam^T blockdiag( f P'_hh , P'_kk ) Lam  (decoupled; f -> 0 is flat in the horizontal covector directions).
Prediction: as f -> 0,  Im Q1 -> lam1 * Q_EH(canonical base metric),  lam1 = |det Lam|^-1 (4 pi)^-3 det(P'_kk)^-1/2   (no free parameter),
Q_EH = quadratic form <sqrt g a_1>_{eps^2}[gbar] of the base cometric gbar^{mu nu} = eta^{ab} W_a(y^mu) W_b(y^nu) (FP/6 - (1/32) q.q (tr h)^2, validated in validate_seeley_4d.py).
The script also reports the gauge test |Q kappa|/(|Q||kappa|) for Q_EH and for Im Q1 at f=1 (the actual window) and f -> 0."""
import sys, numpy as np, mpmath as mp, scipy.linalg as sl
sys.dont_write_bytecode = True
from tail_coeffs import *
from eh_decomposition import QEH
eta = np.diag(eta_a)

def window_family(dat, f):
    W, E, P = dat['W'], dat['E'], dat['P']
    b = np.array([E[:, pidx[(m, 5)]] for m in range(4)])
    V = sl.null_space(b)                                   # (6,2) vertical vectors
    assert V.shape[1] == 2
    Lam = np.vstack([W, V.T])
    Li = np.linalg.inv(Lam)
    Pp = Li.T @ P @ Li
    Pf = np.zeros((6, 6)); Pf[:4, :4] = f * Pp[:4, :4]; Pf[4:, 4:] = Pp[4:, 4:]
    lam1 = abs(np.linalg.det(Lam)) ** -1 * (4 * np.pi) ** -3 * np.linalg.det(Pp[4:, 4:]) ** -0.5
    return Lam.T @ Pf @ Lam, lam1, Lam, V

if __name__ == "__main__":
    rng = np.random.default_rng(41)
    for t in range(4):
        z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
        q = rng.normal(size=4)
        dat = frozen_data(M0, q)
        QE, gbar0, v = QEH(dat, q)
        kap = dat['kappa']
        print("point %d: |Q_EH kappa|/(|Q_EH||kappa|) = %.2e ; dphi(V')=%.1e" % (t, np.linalg.norm(QE @ kap) / (np.linalg.norm(QE) * np.linalg.norm(kap)), 0.0))
        for f in [1.0, 0.1, 0.01, 0.001]:
            Pf, lam1, Lam, V = window_family(dat, f)
            d2 = dict(dat); d2['P'] = Pf
            Q0, Q1, Q2 = [to_np(Q) for Q in forms(d2)]
            Im1 = Q1.imag
            diff = np.linalg.norm(Im1 - lam1 * QE) / np.linalg.norm(lam1 * QE)
            gauge = np.linalg.norm(Im1 @ kap) / (np.linalg.norm(Im1) * np.linalg.norm(kap))
            print("   f=%-6g |Im Q1 - lam1 Q_EH|/|lam1 Q_EH| = %.3e   gauge test of Im Q1: %.3e   (lam1 = %.4e, dphi.V' = %.1e)" % (f, diff, gauge, lam1, np.abs(dat['dphi'] @ V).max()))
