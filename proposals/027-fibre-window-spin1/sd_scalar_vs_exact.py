"""027 script 1: validate the Seeley-DeWitt route against the exact H^4 x H^3 kernel expansion of proposal 025 (scalar, fibre-constant sector).
P = t*Delta_4 + i s Box on functions of y^mu, eta=diag(-1,1,1,1), m^2=-y.y-ell^2, Delta_4 = ell^2 LB(g4) (unit-radius H^4 Laplacian), Box f = m d(m eta d f).
Compare  E + R/6  (SD first coefficient of exp(P)) with the 025 rational function D_1(z0=t-is, w0=is; a=m/ell)."""
import sympy as sp
from sd_core import *
y = sp.symbols('y0:4', real=True); ell, t, s = sp.symbols('ell t s', positive=True)
eta = sp.diag(-1, 1, 1, 1)
yl = [sum(eta[i, j]*y[j] for j in range(4)) for i in range(4)]
yy = sum(y[i]*yl[i] for i in range(4))
m2 = -yy - ell**2
ginv4 = sp.Matrix(4, 4, lambda i, j: eta[i, j] + y[i]*y[j]/ell**2)
sqrtg4 = ell/sp.sqrt(m2)
g4 = sp.Matrix(4, 4, lambda i, j: eta[i, j] + yl[i]*yl[j]/m2)
print("g4*ginv4 = 1:", sp.simplify(g4*ginv4) == sp.eye(4))
print("det check sqrt|g4| = ell/m:", sp.simplify(-ginv4.det() - m2/ell**2) == 0 or sp.simplify(ginv4.det() + m2/ell**2) == 0, sp.simplify(ginv4.det()))
# Delta_4 first-order coefficient A_D^j = ell^2 (1/sqrt g) d_i(sqrt g g^{ij})
AD = [ell**2*sum(sp.diff(sqrtg4*ginv4[i, j], y[i]) for i in range(4))/sqrtg4 for j in range(4)]
ABox = [-y[j] for j in range(4)]                      # m eta^{ij} d_i m = -y^j
Ginv = t*ell**2*ginv4 + sp.I*s*m2*sp.Matrix(4, 4, lambda i, j: eta[i, j])
A = [t*AD[j] + sp.I*s*ABox[j] for j in range(4)]
pp = t*ell**2 + sp.I*s*m2
Gcov = sp.Matrix(4, 4, lambda i, j: eta[i, j]/pp - t*yl[i]*yl[j]/(pp*m2*(sp.I*s - t)))
print('explicit inverse ok:', sp.simplify((Gcov*Ginv).subs({y[0]: 3, y[1]: 1, y[2]: 2, y[3]: -1, ell: 1, t: sp.Rational(1,3), s: sp.Rational(1,2)})) == sp.eye(4))
# 025 exact first correction
z0, w0, a = sp.symbols('z0 w0 a', positive=True)
C = 1 + a**2; c4 = 8*a**4 + 8*a**2 + 1
D1 = -(-5*w0**2*z0*(c4 - 1) + 16*w0*z0*(w0*C + z0)*(3*C - 2) + (32*w0 + 64*z0)*(w0*C + z0)**2)/(32*(w0*C + z0)**2)
for (tt, ss, ee, y0v) in [(sp.Rational(1, 3), sp.Rational(1, 2), 1, 2), (sp.Rational(2, 1), sp.Rational(-1, 3), sp.Rational(3, 2), 3), (sp.Rational(1, 5), 1, 2, 5)]:
    # point y=(y0,0,0,0): m^2 = y0^2 - ell^2
    pt = {y[0]: y0v, y[1]: 0, y[2]: 0, y[3]: 0, ell: ee, t: tt, s: ss}
    trE, R6, _ = sd_first(Ginv, A, 0, y, pt, Gcov=Gcov)
    m2v = y0v**2 - ee**2
    aval = sp.sqrt(m2v)/ee
    ex = D1.subs({z0: tt - sp.I*ss, w0: sp.I*ss, a: aval})
    print("t=%s s=%s ell=%s y0=%s a^2=%s | SD E+R/6 = %s | 025 exact D1 = %s | diff = %s" % (tt, ss, ee, y0v, sp.nsimplify(aval**2), sp.N(trE + R6, 12), sp.N(ex, 12), sp.N(trE + R6 - ex, 3)))
