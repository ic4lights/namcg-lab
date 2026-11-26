"""030 script 9: structure of the tail coefficients as quadratic forms in alpha.
 (i) Q0 (s^0 tail) against the Maxwell tensor  Gm = (kappa.kappa) eta - kappa_a kappa_b  (kappa_a lowered with eta), fit Q0 = lam0 * Gm.
 (ii) Q1 (1/s tail, purely imaginary): gauge test  |Q1 kappa| / (|Q1| |kappa|)  (a gauge-invariant quadratic form has Q1 kappa = 0),
      covariant fit  Q1 ~ A (kappa.kappa) eta + B kappa_a kappa_b  with relative residual,
 (iii) eigenvalue signs of Q1 restricted to the quotient by kappa and of Q1 on the whole space (definiteness).
Random orbit points of CP^{1,2} (Lorentzian leaf), random covectors q, Gaussian window of Delta_{3/4}."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from tail_coeffs import *
eta = np.diag(eta_a)

def analyse(M0, q, verbose=True):
    dat = frozen_data(M0, q)
    kap = dat['kappa']; kl = eta @ kap; k2 = kap @ eta @ kap
    Q0, Q1, Q2 = [to_np(Q) for Q in forms(dat)]
    Gm = k2 * eta - np.outer(kl, kl)
    lam0 = np.sum(Q0.real * Gm) / np.sum(Gm * Gm)
    res0 = np.linalg.norm(Q0.real - lam0 * Gm) / np.linalg.norm(Q0.real)
    Im1 = Q1.imag; Re1 = Q1.real
    gauge = np.linalg.norm(Im1 @ kap) / (np.linalg.norm(Im1) * np.linalg.norm(kap))
    # covariant fit
    Bs = np.array([ (k2 * eta).flatten(), np.outer(kl, kl).flatten() ]).T
    coef, *_ = np.linalg.lstsq(Bs, Im1.flatten(), rcond=None)
    resid = np.linalg.norm(Bs @ coef - Im1.flatten()) / np.linalg.norm(Im1)
    ev = np.linalg.eigvalsh(Im1)
    out = dict(lam0=lam0, res0=res0, gauge=gauge, A=coef[0], B=coef[1], resid=resid, ev=ev, re1=np.linalg.norm(Re1) / np.linalg.norm(Im1), k2=k2, dat=dat, Q1=Im1, Q0=Q0.real)
    if verbose:
        print("   Q0 = lam0*Gm: lam0=%.5e residual %.2e | Q1: |Re|/|Im|=%.1e, gauge test |Q1 kappa|/(|Q1||kappa|)=%.3f, covariant-fit residual=%.3f (A=%.3e,B=%.3e), eigenvalues of Im Q1/|Q1|: %s" % (lam0, res0, out['re1'], gauge, resid, coef[0], coef[1], np.round(ev / np.linalg.norm(Im1), 3)))
    return out

if __name__ == "__main__":
    rng = np.random.default_rng(21)
    for t in range(6):
        z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
        q = rng.normal(size=4)
        print("point %d: y.y=%.3f m=%.3f" % (t, M0[:4, 5] @ np.diag([-1., 1, 1, 1]) @ M0[:4, 5], M0[4, 5]))
        analyse(M0, q)
