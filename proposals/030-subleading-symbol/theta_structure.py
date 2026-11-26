"""030 script 15: the base 2-form theta^{mu nu} = {y^mu, y^nu} on CP^{1,2}, and the tensor T^{rho sigma} = theta^{rho mu} eta_{mu nu} theta^{sigma nu} that sets v^2 = q_rho q_sigma T^{rho sigma}, v = theta q (the vector entering the base-metric fluctuation).
Checks: theta^{mu nu} = -s M^{mu nu} (s = -1 in the code's bracket convention); T is fitted to  c0 eta^{rho sigma} + c1 y^rho y^sigma + c2 t^rho t^sigma + c3 (y t + t y),  y^mu = M^{mu 5}, t^mu = M^{mu 4}  (the orbit relations of the minimal so(4,2) coadjoint orbit).
Reports residual of the fit and whether c1,c2,c3 are nonzero (Lorentz-violating by the time-like vector fields)."""
import sys, numpy as np
sys.dont_write_bytecode = True
from geom28 import *
eta = np.diag([-1., 1, 1, 1])
rng = np.random.default_rng(7)
for t in range(6):
    z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
    Pi, W, Yb, c, E = fields(M0)
    b = np.array([E[:, pidx[(m, 5)]] for m in range(4)])
    theta = np.array([[b[n] @ Yb[m] for n in range(4)] for m in range(4)])           # theta[m,n] = Y_m(y^n) = {y^m, y^n}
    Mmn = M0[:4, :4]
    ratio = theta / np.where(np.abs(Mmn) > 1e-9, Mmn, np.nan)
    Tm = theta @ eta @ theta.T
    y = M0[:4, 5]; tv = M0[:4, 4]
    basis = [np.linalg.inv(eta), np.outer(y, y), np.outer(tv, tv), np.outer(y, tv) + np.outer(tv, y)]
    Bm = np.array([x.flatten() for x in basis]).T
    coef, *_ = np.linalg.lstsq(Bm, Tm.flatten(), rcond=None)
    res = np.linalg.norm(Bm @ coef - Tm.flatten()) / np.linalg.norm(Tm)
    print("point %d: theta/M^{mu nu} ratio (nanmedian) = %.6f | T fit residual %.2e | coefficients c0..c3 = %s | y.y=%.3f t.t=%.3f y.t=%.3f" % (t, np.nanmedian(ratio), res, np.round(coef, 5), y @ eta @ y, tv @ eta @ tv, y @ eta @ tv))
