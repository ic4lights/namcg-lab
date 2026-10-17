"""025 script 2: (a) structure of the pencils on the leaf: vertical/base splitting, kernel of the Lorentzian four-matrix symbol K_H=sigma(Box),
admissible cone -sigma(C42)>=0; (b) closed-form Gaussian-window Lorentzian moments  <(sigma - i0)^{-1}>  with window exp(-W/Lambda^2), W=-sigma(Delta_kappa),
compared with the Euclidean contraction; (c) sign scan of the Lorentzian principal-value moment over generalised-eigenvalue data."""
import sys, numpy as np, scipy.linalg as sl
from scipy.integrate import quad
sys.path.insert(0, r'../023-casimir-regulator')
from symbol_tools import *
from sym_signatures import forms
rng = np.random.default_rng(11)

def P_lor(s, lam):
    return np.prod([(1 + 1j*s*l)**-0.5 for l in lam])
def mom1(lam):
    """<1/(sigma - i0)> over the Gaussian window normalised to int exp(-W)=1 on the 4 nonzero directions: i * int_0^inf ds prod (1+ i s lam)^(-1/2) ; contour s=t e^{-i pi/4}."""
    ph = np.exp(-1j*np.pi/4)
    f = lambda t, part: (1j*ph*P_lor(t*ph, lam)).real if part == 0 else (1j*ph*P_lor(t*ph, lam)).imag
    re = quad(f, 0, np.inf, args=(0,), limit=400)[0]; im = quad(f, 0, np.inf, args=(1,), limit=400)[0]
    return re + 1j*im
def mom1_euc(lam):
    return quad(lambda s: np.prod([(1 + s*l)**-0.5 for l in lam]), 0, np.inf, limit=400)[0]
# analytic isotropic check: window exp(-|u|^2), sigma = -c u0^2 + a |u|^2 ; PV angular integral pi/(a+c) -> <1/sigma> = (int d^4u e^{-u^2}/sigma)/pi^2 
def iso_closed(c, a):
    # int d^4u e^{-u^2}/sigma = (1/2) * Omega_PV = (1/2)*4 pi * pi/(a+c) ; divide by pi^2
    return 2*np.pi**2/(a+c)/np.pi**2
print("(0) isotropic check of the angular principal value pi/(a+c): numeric Gaussian moment vs closed form")
for c, a in [(1, 1), (2, 5), (0.5, 3), (3, 0.2)]:
    print("   c=%.2f a=%.2f   numeric %s   closed form %.10f" % (c, a, np.round(mom1([-c, a, a, a]), 10), iso_closed(c, a)))
print("(a) pencil structure at random orbit points (kappa=3/4)")
e5 = np.diag([-1., 1, 1, 1, 1]); rows = []
for t in range(8):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
    y = M0[:5, 5]; ell2 = -(y @ e5 @ y); y4 = y[4]
    rk, F = forms(M0)
    lam, V = sl.eig(F['C41'], F['C42']); lam = np.real(lam); V = np.real(V)
    vert = V[:, np.abs(lam - 1) < 1e-6]; base = V[:, np.abs(lam - 0.5) < 1e-6]
    KH = F['Box4']; kerH = np.max(np.abs(vert.T @ KH @ vert))/np.max(np.abs(KH))
    # K42 on base negative, on vertical positive
    kb = np.linalg.eigvalsh(base.T @ F['C42'] @ base); kv = np.linalg.eigvalsh(vert.T @ F['C42'] @ vert)
    kappa = 0.75; W = F['C41'] - kappa*F['C42']
    ev = np.sort(np.real(sl.eig(KH, W)[0])); nz = ev[np.abs(ev) > 1e-8]
    # does K_H vanish exactly on the vertical plane?  also on the 2-dim kernel of K_H: overlap with vertical plane
    kerKH = sl.null_space(KH, rcond=1e-9); ov = np.linalg.svd(np.linalg.pinv(np.hstack([vert]))@kerKH)[1] if kerKH.shape[1] else None
    print("  y4^2=%8.4f ell^2=%7.4f | K_H|vert max rel=%.2e | K42|base eig %s  K42|vert eig %s | nonzero gen.eig %s" % (y4**2, ell2, kerH, np.round(kb,3), np.round(kv,3), np.round(nz,4)))
    rows.append((y4**2, ell2, nz, F, W))
print("(b) Gaussian-window moments <1/(sigma-i0)> (units of Lambda^2, per normalised Gaussian in the 4 nonzero directions): Lorentzian vs Euclid contraction (eta->delta)")
for y42, ell2, nz, F, W in rows:
    # Euclid: generalised eigenvalues of (Box4E, W)
    evE = np.sort(np.real(sl.eig(F['Box4E'], W)[0])); nzE = evE[np.abs(evE) > 1e-8]
    mL = mom1(list(nz)); mE = mom1_euc(list(nzE))
    print("  y4^2=%8.4f  Lorentz: Re=%9.5f Im=%9.5f   Euclid=%9.5f   Re_L/Euc=%7.4f" % (y42, mL.real, mL.imag, mE, mL.real/mE))
print("(c) sign scan of Re<1/(sigma-i0)> for lam=(-c,a1,a2,a3), c in [0.1,10], a_i in [1e-3,1e3] log-uniform; 4000 samples")
neg = 0; mn = 1e9
for k in range(4000):
    c = 10**rng.uniform(-1, 1); a = 10**rng.uniform(-3, 3, size=3)
    m = mom1([-c, *a]).real
    mn = min(mn, m*np.prod(np.sqrt(np.abs([c, *a])))); neg += m <= 0
print("   number with Re<=0:", neg, "; min of Re*sqrt(prod|lam|):", mn)
