"""
060 / s1: the semi-classical criterion of arXiv:2605.13294 (Eqs. 13, 16, 17 of v2) at the commuting
(flat) point of the first-order equivariant class, tree level, background Feynman gauge.

Setting (proposal Sec. 2.2): X_a = multiplication by -ptilde_a on L^2(R^4 x fibre), ptilde = u p,
unit Jacobian.  Gaussian weight per complex kernel entry:
  Euclidean contraction, e^{-S}:            <|A_a(m,m')|^2> = g^2 / |Q|^2
  Lorentzian eta, Definition (A), e^{iS-eps}: <|A_a(m,m')|^2> = +- i g^2 / (Q.Q + i eps)
with Q = ptilde - ptilde'.  For a normalised state with |psi|^2 Gaussian N(t, sigma^2 I_4) in ptilde,
  <|<psi|A_a|psi>|^2> = g^2 E[ G(delta) ],  delta = ptilde - ptilde' ~ N(0, s^2 I_4), s^2 = 2 sigma^2.
Checks:
 (a) Euclidean E[1/|delta|^2] = 1/(2 s^2) = 1/(4 sigma^2): closed form, quadrature, Monte Carlo.
 (b) Lorentzian E[i/(delta_eta^2 + i eps)] -> (1+i)/(2 s^2) as eps -> 0: Schwinger closed form and
     numerical lambda-integral; the integral formula of 2605.13294 Eq. (integral-formula).
 (c) maximum over t' (shift d of the second state): Euclidean decreasing in |d|; Lorentzian modulus
     on |d| < sigma (Eq. 17 restriction).
"""
import numpy as np
from scipy import integrate

rng = np.random.default_rng(60)
print("(a) Euclidean, s^2 = 2 sigma^2")
for sigma in [0.5, 1.0, 2.0]:
    s2 = 2*sigma**2
    closed = 1/(2*s2)
    quad = integrate.quad(lambda lam: (1+2*lam*s2)**-2, 0, np.inf)[0]
    d = rng.normal(scale=np.sqrt(s2), size=(2_000_000, 4))
    mc = np.mean(1/np.sum(d**2, axis=1))
    print(f"  sigma={sigma}: closed {closed:.6f}  quad {quad:.6f}  MC {mc:.6f}  1/(4 sigma^2) {1/(4*sigma**2):.6f}")
print("  ratio Delta^Q/Delta_T = sqrt(g^2/(4 sigma^2))/sigma = g/(2 sigma^2)")

print("(b) Lorentzian: E[i/(delta_eta^2 + i0)] via Schwinger, eta = diag(-1,1,1,1)")
def lor_mean(s2, dvec=np.zeros(4), eps=0.0):
    # i/(x+i eps) = int_0^inf dlam e^{i lam (x + i eps)};  E[e^{i lam eta_mu (d_mu+delta_mu)^2}]
    eta = np.array([-1., 1, 1, 1])
    def f(lam):
        a = lam*eta
        val = np.prod((1-2j*a*s2)**-0.5*np.exp(1j*a*dvec**2/(1-2j*a*s2)))
        return val*np.exp(-lam*eps)
    re = integrate.quad(lambda l: np.real(f(l)), 0, np.inf, limit=800)[0]
    im = integrate.quad(lambda l: np.imag(f(l)), 0, np.inf, limit=800)[0]
    return re + 1j*im
for sigma in [0.5, 1.0]:
    s2 = 2*sigma**2
    val = lor_mean(s2)
    print(f"  sigma={sigma}: numeric {val:.6f}   closed (1+i)/(2 s^2) = {(1+1j)/(2*s2):.6f}   modulus {abs(val):.6f} vs 1/(2 sqrt2 sigma^2) {1/(2*np.sqrt(2)*sigma**2):.6f}")
print("  closed form: K = int_0^inf (1+iu)^(-1/2)(1-iu)^(-3/2) du = -i[((1+iu)/(1-iu))^(1/2)]_0^inf = -i(i-1) = 1+i")
u = np.logspace(-6, 8, 200001)
Kint = np.trapezoid((1+1j*u)**-0.5*(1-1j*u)**-1.5, u)
print(f"  numeric K (log grid trapezoid, truncated at 1e8): {Kint:.5f}")
print("  ratio Delta^Q/Delta_T = sqrt(g^2/(2 sqrt2 sigma^2))/sigma = 2^(-3/4) g/sigma^2 =", 2**-0.75, "* g/sigma^2")

print("(b') integral formula of 2605.13294: int d^4k e^{-k.k/2}/(k_eta^2 - i eps)")
# = (2 pi)^2 E_{N(0,1)}[1/(x - i0)] = (2pi)^2 * conj(E[1/(x+i0)]) = (2pi)^2 * conj(-i * (1+i)/2)
val = lor_mean(1.0)
E_plus = val/1j  # E[1/(x+i0)]
I_formula = (2*np.pi)**2*np.conj(E_plus)
print(f"  numeric: {I_formula:.6f}   = {I_formula/np.pi**2:.6f} pi^2   (printed in 2605.13294: pi^2 (1+i))")
# independent check of the imaginary part by the delta function: Im = pi * int d^4k e^{-k^2/2} delta(k_eta^2) = 2 pi^2
imag_delta = np.pi*4*np.pi*integrate.quad(lambda k0: 0.5*abs(k0)*np.exp(-k0**2), -np.inf, np.inf)[0]
print(f"  Im part from pi*delta(k_eta^2): {imag_delta:.6f} = {imag_delta/np.pi**2:.6f} pi^2")

print("(c) maximum over the second state (shift d), sigma = 1, s^2 = 2")
s2 = 2.0
def eu_mean(dvec):
    def f(lam):
        return np.prod((1+2*lam*s2)**-0.5*np.exp(-lam*dvec**2/(1+2*lam*s2)))
    return integrate.quad(f, 0, np.inf)[0]
for dn in [0.0, 0.5, 1.0, 2.0, 4.0]:
    print(f"  Euclidean |d|={dn}: {eu_mean(np.array([dn,0,0,0])):.6f}")
best = 0
for dn in np.linspace(0, 1.0, 11):
    for direction in [np.array([1., 0, 0, 0]), np.array([0, 1., 0, 0]), np.array([1., 1, 0, 0])/np.sqrt(2)]:
        v = abs(lor_mean(s2, dn*direction))
        best = max(best, v)
print(f"  Lorentzian modulus at d=0: {abs(lor_mean(s2)):.6f};  max over |d|<=sigma on time, space, null-type axes: {best:.6f};  ratio {best/abs(lor_mean(s2)):.4f}")
print("Unit Jacobian of p -> u p for u in SO(3,1):")
def boost(b, axis):
    L = np.eye(4); ch, sh = np.cosh(b), np.sinh(b); L[0, 0] = L[axis, axis] = ch; L[0, axis] = L[axis, 0] = sh; return L
u_ = boost(0.7, 1) @ boost(-1.3, 2) @ boost(0.4, 3)
print("  det u =", np.linalg.det(u_), "; u^T eta u = eta:", np.allclose(u_.T @ np.diag([-1., 1, 1, 1]) @ u_, np.diag([-1., 1, 1, 1])))
