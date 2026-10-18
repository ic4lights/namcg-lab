"""027 script 7: invariant-sector weight-two functions for scalar, spin term, mass term, vector, ghost, and the supertrace combination.
Notation (025): D = D_0 (1 + t d1(x) + ...),  x = s/t,  D_0 = (4 pi)^-2 (t-is)^{-1/2}(t+i s a^2)^{-3/2},  g(x) = (1-ix)^{-1/2}(1+i x a^2)^{-3/2},  a = sinh(tau) = y4/ell.
Weight-two part of  sum ln(lambda - i0) = -(4 pi)^-2 Lam^2 Q,  Q[d1] = int_0^oo dx/x g d1  with the 025 subtraction of the window mode-count d1(0)=-2 per component on x<1.
Species:   scalar (also ghost, weight -1 each, and extra scalars)    d1_sc(x) = D1(1-ix, ix; a)
           spin term of a vector (4 components, Lorentz Sigma_V)      d1_sp(x) = 6 x^2 (1+a^2)/(1+i x a^2)
           mass term mu^2 per component                              d1_mu(x) = -i x mu^2
Exact rotation x=-iu:  Re Q_sp = -6(1+a^2) int_0^1 u (1-u)^(-1/2) (1+a^2 u)^(-5/2) du  (<0);   Q_mu = -mu^2 J,  Re J = int_0^1 (1-u)^(-1/2)(1+a^2u)^(-3/2) du = 2/(1+a^2)."""
import numpy as np, sympy as sp
from scipy.integrate import quad
z0, w0, aa = sp.symbols('z0 w0 aa', positive=True)
C = 1 + aa**2; c4 = 8*aa**4 + 8*aa**2 + 1
D1 = -(-5*w0**2*z0*(c4 - 1) + 16*w0*z0*(w0*C + z0)*(3*C - 2) + (32*w0 + 64*z0)*(w0*C + z0)**2)/(32*(w0*C + z0)**2)
f_D1 = sp.lambdify((z0, w0, aa), D1, 'numpy')
def g(x, a): return (1 - 1j*x)**-0.5*(1 + 1j*x*a**2)**-1.5
d1_sc = lambda x, a: f_D1(1 - 1j*x, 1j*x, a)
d1_sp = lambda x, a: 6*x**2*(1 + a**2)/(1 + 1j*x*a**2)
d1_mu = lambda x, a: -1j*x
ph = np.exp(-1j*np.pi/4)
def Q_generic(d1, a, d10=0.0):
    """Q = int_0^1 dx/x [g d1 - d10] + int_1^oo dx/x g d1, evaluated on the contour x = u e^{-i pi/4} (no singularities in the 4th quadrant); arc term d10*(i pi/4)... as in 025."""
    def sub(u, part):
        xx = u*ph; val = ph*(g(xx, a)*d1(xx, a) - d10)/xx
        return val.real if part == 0 else val.imag
    def tail(u, part):
        xx = u*ph; val = ph*g(xx, a)*d1(xx, a)/xx
        return val.real if part == 0 else val.imag
    re = quad(sub, 0, 1, args=(0,), limit=300)[0] + quad(tail, 1, np.inf, args=(0,), limit=300)[0]
    im = quad(sub, 0, 1, args=(1,), limit=300)[0] + quad(tail, 1, np.inf, args=(1,), limit=300)[0]
    arc = -d10*(1j*np.pi/4)          # int along the real segment minus rotated segment of  -d10 dx/x  : -d10 [ln 1 - ln e^{-i pi/4}] = -d10 (i pi/4)
    return re + 1j*im + arc
if __name__ == "__main__":
    print("check against 025 table of Q_sc (d10=-2):")
    for a in (0.5, 1.0, 2.0):
        print("  a=%.2f  Q_sc = %s   (025: a=0.5 -0.32630+2.71300i ; a=1 1.11371+3.0i ; a=2 3.44629+3.09950i)" % (a, np.round(Q_generic(d1_sc, a, -2.0), 5)))
    print("exact-rotation checks:")
    for a in (0.3, 1.0, 3.0):
        Qsp = Q_generic(d1_sp, a); Qmu = Q_generic(d1_mu, a)
        rsp = -6*(1 + a**2)*quad(lambda u: u*(1 - u)**-0.5*(1 + a**2*u)**-2.5, 0, 1)[0]
        Jre = quad(lambda u: (1 - u)**-0.5*(1 + a**2*u)**-1.5, 0, 1)[0]
        Jim = quad(lambda u: (u - 1)**-0.5*(1 + a**2*u)**-1.5, 1, np.inf)[0]
        print("  a=%.1f Re Q_sp = %.6f (rotation formula %.6f) | Re Q_mu(mu2=1) = %.6f (-J_re=%.6f, 2/(1+a^2) = %.6f) | Im Q_mu = %.6f (-J_im = %.6f)" % (a, Qsp.real, rsp, Qmu.real, -Jre, -2/(1 + a**2), Qmu.imag, -Jim))
    print()
    print("Weight-two functions Q (Re, Im).  columns: a | Q_sc | Q_sp | Q_mu(mu2=1) | bosonic vec(4)+gh(-2) with mu_v^2=-3 : 2 Q_sc + Q_sp - 12 Q_mu | + n_ex=6 scalars with mu_i^2=0 | IKKT supertrace (N_b=N_f, spin cancels): 6*mu_i^2 Q_mu - 12 Q_mu")
    for a in (0.3, 0.5, 0.775, 1.0, 1.5, 2.0, 4.0, 8.0):
        Qs = Q_generic(d1_sc, a, -2.0); Qp = Q_generic(d1_sp, a); Qm = Q_generic(d1_mu, a)
        bos = 2*Qs + Qp - 12*Qm
        bos6 = bos + 6*Qs
        for mi in (0.0, 2.0):
            pass
        print("%6.3f | (%8.4f,%8.4f) | (%8.4f,%8.4f) | (%8.4f,%8.4f) | (%8.4f,%8.4f) | (%8.4f,%8.4f) | mu_i^2=0: (%8.4f,%8.4f)  mu_i^2=1: (%8.4f,%8.4f)" % (a, Qs.real, Qs.imag, Qp.real, Qp.imag, Qm.real, Qm.imag, bos.real, bos.imag, bos6.real, bos6.imag, (-12*Qm).real, (-12*Qm).imag, (6*Qm - 12*Qm).real, (6*Qm - 12*Qm).imag))
