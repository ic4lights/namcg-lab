# s3_monte_carlo.py (084) Monte Carlo check of the induced coupled law, D=6, s2=1.7.
# w_i ~ CN(0, s2*g_i) independent; u random complex gaussian normalized; a = Im(u^dag w),
# r = |w|^2 - |u^dag w|^2; spectrum -2a +/- 2*sqrt(a^2+r); trQ^m = e+^m + e-^m.
# Every comparison is est-vs-pred with a Monte-Carlo standard error (|z| < 5 PASS,
# and the coupled-vs-product tr4 gap must be significant |z| > 5).  Run from root:
#   python -I proposals/084-g-moments-coupledmixed/s3_monte_carlo.py
import numpy as np
rng = np.random.default_rng(20261118)
D, N, s2 = 6, 600000, 1.7
g = np.sort(rng.uniform(0.1, 0.9, D))
u = rng.standard_normal(D) + 1j*rng.standard_normal(D); u /= np.linalg.norm(u)
mu = float(np.sum(g*np.abs(u)**2)); W = float(g.sum())
Gam = float(np.sum(np.abs(u)**2*(g-mu)**2)); V = s2*mu/2
w = (rng.standard_normal((N, D)) + 1j*rng.standard_normal((N, D)))*np.sqrt(s2*g/2)
al = w @ np.conj(u)
a = al.imag; r = (w*np.conj(w)).real.sum(axis=1) - al.real**2 - a**2
sq = np.sqrt(a*a + r); e1 = -2*a + 2*sq; e2 = -2*a - 2*sq
tr1, tr3, tr4 = e1+e2, e1**3+e2**3, e1**4+e2**4
E = lambda v: float(np.mean(v))
def zrow(name, stat, pred):
    est = E(stat); se = np.std(stat)/np.sqrt(N); zz = abs(est-pred)/max(se, 1e-30)
    print("%-30s est % .6g pred % .6g  |z| %.2f" % (name, est, pred, zz))
    return zz
zs = [zrow("E[a r] = 0", a*r, 0.0),
      zrow("E[a^2] = s2 mu/2", a*a, V),
      zrow("E[r] = s2(W-mu)", r, s2*(W-mu)),
      zrow("E[a^4] = 3V^2", a**4, 3*V*V),
      zrow("E[a^2 r] - V E[r] = s4G/2", a*a*r - V*r, s2**2*Gam/2),
      zrow("<trQ2> = 8 s2 W", e1**2+e2**2, 8*s2*W),
      zrow("<trQ> odd = 0", tr1, 0.0),
      zrow("<trQ3> odd = 0", tr3, 0.0),
      zrow("<trQ4> = prod+128 s4 G", tr4, 32*(E(r*r)+8*V*E(r)+24*V*V)+128*s2**2*Gam)]
bad = sum(zz > 5 for zz in zs)
prod_pred = 32*(E(r*r)+8*V*E(r)+24*V*V)
gapstat = tr4 - 32*(r*r + 8*V*r + 8*a**4)
zg = abs(E(gapstat) - 128*s2**2*Gam)/(np.std(gapstat)/np.sqrt(N))
print("Gamma = %.6g ; measured tr4 gap = %.6g ; predicted 128 s^4 Gamma = %.6g ; gap |z| vs pred %.2f"
      % (Gam, E(gapstat), 128*s2**2*Gam, zg))
print("S3 OK" if bad == 0 and zg < 5 else "S3 FAIL")
