"""027 script 16: closed forms of the mass-type and spin-type invariant-sector integrals (exact rotation x=-iu; (1-u-i0)^(-1/2) = (1-u)^(-1/2) for u<1, = +i (u-1)^(-1/2) for u>1).
 J(a)  := int_0^oo (1-u)^{-1/2} (1+a^2 u)^{-3/2} du  = 2/(1+a^2) + 2i/(a(1+a^2))                    ( Q_mu = -mu^2 J )
 Ksp(a):= int_0^oo u (1-u)^{-1/2} (1+a^2 u)^{-5/2} du = (4/3)/(1+a^2) + i * (...)                    ( Q_sp = -6 (1+a^2) Ksp )
Verified symbolically (sympy) and against direct quadrature."""
import sympy as sp, numpy as np
from scipy.integrate import quad
a = sp.symbols('a', positive=True); u, v = sp.symbols('u v', positive=True)
Jre = sp.integrate((1 - u)**sp.Rational(-1, 2)*(1 + a**2*u)**sp.Rational(-3, 2), (u, 0, 1))
Jim = sp.integrate(2*(1 + a**2 + a**2*v**2)**sp.Rational(-3, 2), (v, 0, sp.oo))
print("J_re =", sp.simplify(Jre), "; J_im =", sp.simplify(Jim))
Kre = sp.integrate(u*(1 - u)**sp.Rational(-1, 2)*(1 + a**2*u)**sp.Rational(-5, 2), (u, 0, 1))
Kim = sp.integrate(2*(1 + v**2)*(1 + a**2 + a**2*v**2)**sp.Rational(-5, 2), (v, 0, sp.oo))
print("Ksp_re =", sp.simplify(Kre), "; Ksp_im =", sp.simplify(Kim))
print("-6(1+a^2) Ksp_re =", sp.simplify(-6*(1 + a**2)*Kre), "; -6(1+a^2) Ksp_im =", sp.simplify(-6*(1 + a**2)*Kim))
for av in (0.3, 1.0, 3.0):
    jr = quad(lambda x: (1 - x)**-0.5*(1 + av**2*x)**-1.5, 0, 1)[0]; ji = quad(lambda x: (x - 1)**-0.5*(1 + av**2*x)**-1.5, 1, np.inf)[0]
    kr = quad(lambda x: x*(1 - x)**-0.5*(1 + av**2*x)**-2.5, 0, 1)[0]; ki = quad(lambda x: x*(x - 1)**-0.5*(1 + av**2*x)**-2.5, 1, np.inf)[0]
    print("a=%.1f quad: J=(%.6f,%.6f) Ksp=(%.6f,%.6f) | formulas: J=(%.6f,%.6f) Ksp=(%.6f,%.6f)" % (av, jr, ji, kr, ki, float(Jre.subs(a, av)), float(Jim.subs(a, av)), float(Kre.subs(a, av)), float(Kim.subs(a, av))))
print("closed forms:  Re Ksp = 4/(3(1+a^2)^2) :", [abs(quad(lambda x: x*(1 - x)**-0.5*(1 + av**2*x)**-2.5, 0, 1)[0] - 4/(3*(1 + av**2)**2)) < 1e-9 for av in (0.1, 0.3, 0.7, 1.0, 3.0, 9.0)])
print("Re Q_sp = -8/(1+a^2), Im Q_sp = -4(3a^2+1)/(a^3(1+a^2)), Re Q_mu = -2 mu^2/(1+a^2), Im Q_mu = -2 mu^2/(a(1+a^2))")
