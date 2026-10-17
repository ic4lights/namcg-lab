"""025 script 4: Seeley-DeWitt coefficient a_1 of Box = rho^{-1} d_mu (rho m^2 eta^{mu nu} d_nu) on fibre-constant functions (appendix operator),
computed independently of the H^4 x H^3 kernel expansion.  G^{mu nu}=m^2 eta^{mu nu}, rho=1/m, m^2=-y.y-ell^2, formal (Lorentzian) evaluation.
Also checks Box = d_tau^2 + 3 tanh tau d_tau - tanh^2 tau Delta_H3 on a test function f(tau)."""
import sympy as sp
y = sp.symbols('y0:4', real=True); ell = sp.symbols('ell', positive=True)
eta = sp.diag(-1, 1, 1, 1)
m2 = -sum(eta[i, i]*y[i]**2 for i in range(4)) - ell**2
m = sp.sqrt(m2)
rho = 1/m
# operator on a test function
f = sp.Function('f')
def Box(F):
    return sum(sp.diff(rho*m2*eta[i, i]*sp.diff(F, y[i]), y[i]) for i in range(4))/rho
# a_1 via conformal-flat formulas: G_{mu nu}=e^{2 Om} eta, e^{Om}=1/m
Om = -sp.log(m)
box_flat = lambda F: sum(eta[i, i]*sp.diff(F, y[i], 2) for i in range(4))
dsq = lambda F, H: sum(eta[i, i]*sp.diff(F, y[i])*sp.diff(H, y[i]) for i in range(4))
R = -6*sp.exp(-2*Om)*(box_flat(Om) + dsq(Om, Om))
phi = 3*sp.log(m)               # rho = sqrt|G| e^phi, sqrt|G| = m^-4
# omega_mu = (1/2) d_mu phi ; omega^2 = G^{mu nu} om om ; div: nabla_mu omega^mu = (1/sqrt G) d_mu (sqrt G G^{mu nu} omega_nu)
om = [sp.diff(phi, y[i])/2 for i in range(4)]
sqrtG = m**-4
om2 = sum(m2*eta[i, i]*om[i]**2 for i in range(4))
div = sum(sp.diff(sqrtG*m2*eta[i, i]*om[i], y[i]) for i in range(4))/sqrtG
a1 = sp.simplify(R/6 - om2 - div)
a1_m = sp.simplify(a1.subs(y[0], sp.sqrt(m2.subs(y[0], 0)*0 + 0)) if False else a1)
mm = sp.symbols('mm', positive=True)
# express in m: use y1=y2=y3=0, y0 chosen so that m^2 = y0^2 - ell^2
a1_pt = sp.simplify(a1.subs({y[1]: 0, y[2]: 0, y[3]: 0}))
y0 = y[0]
a1_m = sp.simplify(a1_pt.subs(y0, sp.sqrt(mm**2 + ell**2)))
print("a_1(m) =", sp.factor(a1_m), "  ; appendix density times m^4 / ... : (5 m^2 - 3 ell^2)/(4 m^2) =", sp.factor((5*mm**2 - 3*ell**2)/(4*mm**2)), " difference:", sp.simplify(a1_m - (5*mm**2 - 3*ell**2)/(4*mm**2)))
# radial form of Box on f(tau): y_mu = ell cosh(tau) u_mu, at u=(1,0,0,0)->y0=ell cosh tau, y4=ell sinh tau
tau = sp.symbols('tau', real=True)
F = sp.Function('F')
# function of m only: F(m(y)); in tau: m = ell sinh tau
Fm = F(m)
lhs = sp.simplify(Box(Fm).subs({y[1]: 0, y[2]: 0, y[3]: 0}))
ft = sp.Function('ft')(tau)
# Box in tau coordinates acting on ft(tau) = F(ell sinh tau): d_tau^2 + 3 tanh d_tau
G = sp.Function('G')
tt = sp.symbols('tt', real=True)
Fg = sp.Function('Fg')
test = sp.exp(-m)   # concrete test function of m
lhs = sp.simplify(Box(test).subs({y[1]: 0, y[2]: 0, y[3]: 0}).subs(y0, ell*sp.cosh(tt)).subs(ell, 1))
tst = sp.exp(-sp.sinh(tt))
rhs = sp.simplify(sp.diff(tst, tt, 2) + 3*sp.tanh(tt)*sp.diff(tst, tt))
print("Box(f(m)) + (d_tau^2 + 3 tanh d_tau) f at ell=1, tau>0 (should vanish: Box = -(Delta_H4 - Delta_H3) on tau-functions):", sp.simplify((lhs + rhs).subs(sp.Abs(sp.sinh(tt)), sp.sinh(tt))))
