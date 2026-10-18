"""025 script 5: Lorentzian Schwinger integral of the weight-two term in the invariant (s=0) sector with the Gaussian Casimir window exp(t C41-type).
sum_modes ln(lambda - i0) = -int_0^oo ds/s D(t - i s, i s),  D = D0 (1 + D1 + ...),  D0 = (4 pi)^-2 (t-is)^{-1/2} (t+i s a^2)^{-3/2}, a = sinh(tau) = y4/ell.
Weight-two part (coefficient of t^{-1}): -(4 pi)^-2 t^-1 Q(a), Q = int dx/x g(x) d1(x), g=(1-ix)^{-1/2}(1+i x a^2)^{-3/2}, D1 = t d1, s = t x.
The x->0 end is the window mode-count term d1(0) = -2 (= R/6 of H^4): Q is defined with the subtraction  - d1(0) 1_{x<1}; the remainder is d1(0)*(-ln(mu^2 t)+const): a scale-dependent term proportional to the number of modes.
Also the linear-in-s ('Box curvature') piece  i c_s * int g dx  with c_s=(5a^2-3)/(4a^2)."""
import sympy as sp, numpy as np
from scipy.integrate import quad
z0, w0, a = sp.symbols('z0 w0 a', positive=True)
C = 1 + a**2
c4 = 8*a**4 + 8*a**2 + 1                                  # cosh(4 tau) with a = sinh(tau)
D1 = -(-5*w0**2*z0*(c4 - 1) + 16*w0*z0*(w0*C + z0)*(3*C - 2) + (32*w0 + 64*z0)*(w0*C + z0)**2)/(32*(w0*C + z0)**2)
chk = sp.simplify(D1.subs({z0: -sp.I*sp.Symbol('S'), w0: sp.I*sp.Symbol('S')})/(sp.I*sp.Symbol('S')))
print("c_s from this D1:", sp.simplify(chk), "(expected (5a^2-3)/(4a^2))")
print("D1 at w0=0:", sp.simplify(D1.subs(w0, 0)), "(= 2 b1(0) ... : -2 z0)")
f = sp.lambdify((z0, w0, a), D1, 'numpy')
def g(x, aa): return (1 - 1j*x)**-0.5*(1 + 1j*x*aa**2)**-1.5
def d1(x, aa): return f(1 - 1j*x, 1j*x, aa)
def Q(aa):
    ph = np.exp(-1j*np.pi/4)      # contour x = u e^{-i pi/4}  (no singularities in the 4th quadrant)
    def integrand(u, part):
        xx = u*ph
        val = ph*g(xx, aa)*d1(xx, aa)/xx
        if u < 1e-12: val = ph*0
        return val.real if part == 0 else val.imag
    # subtraction of d1(0) on the real axis piece [0,1]: do the whole integral on a rotated contour from delta, and treat 1/x end separately
    delta = 1e-6
    def sub(u, part):
        xx = u*ph
        val = ph*(g(xx, aa)*d1(xx, aa) - (-2.0))/xx
        return val.real if part == 0 else val.imag
    re = quad(sub, 0, 1, args=(0,), limit=300)[0]; im = quad(sub, 0, 1, args=(1,), limit=300)[0]
    re2 = quad(integrand, 1, np.inf, args=(0,), limit=300)[0]; im2 = quad(integrand, 1, np.inf, args=(1,), limit=300)[0]
    # the rotated segment [0,1] e^{-i pi/4} vs the real segment [0,1]: difference of the subtracted constant term -d1(0) int dx/x over the two paths = -d1(0)*(ln of endpoints): add arc term
    # int_{path} dx/x (-(-2)) from  e^{-i pi/4}*1  to 1  -> (-(-2))*(i pi/4) ... handled below
    arc = 2.0*(1j*np.pi/4)    # contributes  +2 * int dx/x over the arc from e^{-i pi/4} to 1 = 2*(i pi/4)
    return (re + re2) + 1j*(im + im2) + arc
def cpiece(aa):
    cs = (5*aa**2 - 3)/(4*aa**2)
    ph = np.exp(-1j*np.pi/4)
    fn = lambda u, part: ((ph*g(u*ph, aa)).real if part == 0 else (ph*g(u*ph, aa)).imag)
    I = quad(fn, 0, np.inf, args=(0,), limit=300)[0] + 1j*quad(fn, 0, np.inf, args=(1,), limit=300)[0]
    return 1j*cs*I
print("   a      c_s      Q(a) (Re, Im)                  window-count term d1(0)   linear-s piece i c_s int g (Re, Im)   Re Q / Re(linear piece)")
for aa in [0.3, 0.5, 0.775, 1.0, 1.5, 2.0, 4.0, 8.0]:
    q = Q(aa); p = cpiece(aa)
    print("%6.3f %8.4f  (%10.5f, %10.5f)        -2        (%10.5f, %10.5f)     %8.3f" % (aa, (5*aa**2 - 3)/(4*aa**2), q.real, q.imag, p.real, p.imag, q.real/p.real if p.real != 0 else np.nan))

print("check of Q by direct integration along the real x axis (tail estimated by the 1/x^2 law):")
def Q_real(aa):
    fr = lambda x, part: ((g(x, aa)*d1(x, aa) + 2.0)/x).real if part == 0 else ((g(x, aa)*d1(x, aa) + 2.0)/x).imag
    fo = lambda x, part: ((g(x, aa)*d1(x, aa))/x).real if part == 0 else ((g(x, aa)*d1(x, aa))/x).imag
    X = 4000.0
    r = [quad(fr, 1e-12, 1, args=(p,), limit=500)[0] + quad(fo, 1, X, args=(p,), limit=4000)[0] for p in (0, 1)]
    # tail: g*d1/x ~ c/x^2 : estimate c from the integrand at X
    tail = (g(X, aa)*d1(X, aa)/X*X)       # c/X ... integrate c/x^2 from X to oo = c/X
    return r[0] + 1j*r[1] + tail*0
for aa in [0.5, 1.0, 2.0]:
    print("  a=%.2f  Q_real-axis = %s   Q_rotated = %s" % (aa, np.round(Q_real(aa), 3), np.round(Q(aa), 3)))
