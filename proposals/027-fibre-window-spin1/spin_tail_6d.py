"""027 script 14: large-s tail of the 6D spin term.  integrand  g_6(x) d1_sp(x)/x  ->  C/x  with  C = -8 i * (sum over ker S of -K31 in the S eigenbasis) / sqrt(prod |lambda'_k|)  (W = I/4, lambda' = eig(W^-1 S) nonzero),
purely imaginary; the real part of the proper-time integral is therefore defined only up to the choice of the contour angle (Re shifts by theta*Im C)."""
import numpy as np
from cone_window_geometry import *
rng = np.random.default_rng(11)
for t_ in range(6):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); y = M0[:5, 5]
    try: r = analyse(M0)
    except Exception: continue
    F = r['F']; T = r['T']; S = r['S']; K31 = T.T @ F['C31'] @ T
    ell2 = -(y @ np.diag([-1., 1, 1, 1, 1]) @ y); a = abs(y[4])/np.sqrt(ell2)
    sw, V = np.linalg.eigh(S); ker = np.abs(sw) < 1e-8
    dk = np.diag(V.T @ (-K31) @ V); lam = (sw[~ker])/0.25
    Cpred = -8j*np.sum(dk[ker])/np.sqrt(np.prod(np.abs(lam)))
    W = 0.25*np.eye(6)
    x = 1e5*np.exp(-1j*np.pi/4)
    g6 = np.prod([(1 + 1j*x*l)**-0.5 for l in lam]); d1 = 2*x**2*np.trace(np.linalg.solve(W + 1j*x*S, -K31))
    Cnum = g6*d1/x*x
    qc = (1 - a*a)/(2*(1 + 2*a*a))
    print("a=%.3f  C_pred=%s  C_num=%s  sum_ker(-K31)=%.5f vs 2*q_c=%.5f" % (a, np.round(Cpred, 5), np.round(Cnum, 5), np.sum(dk[ker]), 2*qc))
