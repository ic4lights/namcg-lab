"""027 script 9: Lemma (Lorentzian Gaussian moment).  Let lam = (-c, a_1..a_n), c>0, a_k>0, n>=2.  M(lam) := i int_0^oo ds prod_k (1 + i s lam_k)^(-1/2)
 (= the Gaussian average of 1/(sigma - i0) with sigma = sum lam_k x_k^2, window weight prod exp(-x_k^2)/sqrt(pi)).  Rotating s = -i u (4th quadrant, no singularity, decay u^{-(n+1)/2})
   M = int_0^oo du (1 - c u - i0)^(-1/2) prod (1 + a_k u)^(-1/2),
 and (1 - c u - i0)^(-1/2) is real for u<1/c and equal to +i (cu-1)^(-1/2) for u>1/c.  With u = (1 -+ v^2)/c:
   Re M = (2/c) int_0^1 dv prod_k (1 + a_k (1-v^2)/c)^(-1/2)  > 0 ,   Im M = (2/c) int_0^oo dv prod_k (1 + a_k (1+v^2)/c)^(-1/2) > 0 .
Check against direct contour evaluation, the isotropic closed form 2/(a+c) (n=3), and 4000 random samples (025 scan)."""
import numpy as np
from scipy.integrate import quad
rng = np.random.default_rng(11)
ph = np.exp(-1j*np.pi/4)
def M_contour(lam):
    f = lambda t, part: ((1j*ph*np.prod([(1 + 1j*t*ph*l)**-0.5 for l in lam])).real if part == 0 else (1j*ph*np.prod([(1 + 1j*t*ph*l)**-0.5 for l in lam])).imag)
    return quad(f, 0, np.inf, args=(0,), limit=400)[0] + 1j*quad(f, 0, np.inf, args=(1,), limit=400)[0]
def M_formula(c, a):
    re = (2/c)*quad(lambda v: np.prod([(1 + ak*(1 - v*v)/c)**-0.5 for ak in a]), 0, 1)[0]
    im = (2/c)*quad(lambda v: np.prod([(1 + ak*(1 + v*v)/c)**-0.5 for ak in a]), 0, np.inf)[0]
    return re + 1j*im
mx = 0
for k in range(300):
    c = 10**rng.uniform(-1, 1); a = 10**rng.uniform(-2, 2, size=3)
    m1 = M_contour([-c, *a]); m2 = M_formula(c, a)
    mx = max(mx, abs(m1 - m2)/abs(m2))
print("300 random spectra: max relative difference, contour integral vs (Re,Im) formula:", mx)
for c, a in [(1, 1), (2, 5), (0.5, 3), (0.5, 0.7271)]:
    print("isotropic c=%.2f a=%.3f: formula %s  closed form Re = 2/(a+c) = %.10f" % (c, a, np.round(M_formula(c, [a]*3), 10), 2/(a + c)))
mn = 1e9; neg = 0; imneg = 0
for k in range(4000):
    c = 10**rng.uniform(-1, 1); a = 10**rng.uniform(-3, 3, size=3)
    m = M_formula(c, a); neg += m.real <= 0; imneg += m.imag <= 0
print("4000 spectra: Re<=0:", neg, " Im<=0:", imneg)
# upper/lower bounds:  Re M >= (2/c) prod (1+a_k/c)^(-1/2) (v^2 in [0,1], factors decreasing in 1-v^2 ... ) crude bound check
ok = 0
for k in range(200):
    c = 10**rng.uniform(-1, 1); a = 10**rng.uniform(-2, 2, size=3)
    lo = (2/c)*np.prod([(1 + ak/c)**-0.5 for ak in a]); ok += M_formula(c, a).real >= lo - 1e-12
print("crude lower bound Re M >= (2/c) prod (1+a_k/c)^(-1/2) holds in", ok, "of 200")
