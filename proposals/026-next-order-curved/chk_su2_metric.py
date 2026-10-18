"""G^{-1}(x0) for the SU(2) family at r0=h0=1: expect diag(1/(u+2)^2, 1/(u+2)^2, 1/4, 1/4) in the Cartesian basis at x0=(1,0,0,0)
(radial and e^3 directions carry alpha = r h' + 2h = u+2; e^1,e^2 carry beta = 2h = 2); Weyl^2, R_G from the symbolic run (su2_a2_unit.pkl)."""
import pickle, sympy as sp
from sympy import QQ_I
import jetlib as jl
from common import use_gaussian, theta_from_omega
import su2_family as F, geom
use_gaussian(3)
class Wrap:
    one = QQ_I(1); zero = QQ_I(0)
    @staticmethod
    def convert(x): return QQ_I.from_sympy(sp.Rational(x))
for u in (sp.Rational(-1, 2), sp.Rational(1), sp.Rational(-3)):
    h1 = u; h2 = -u*(u**2 + 4*u + 10)/2; h3 = 3*u*(u**4 + 8*u**3 + 26*u**2 + 40*u + 40)/4
    w = F.omega_jets_su2(Wrap, (sp.Integer(1), sp.Integer(1), h1, h2, h3))
    geom.SIGN_OVERRIDE = None
    Th = theta_from_omega(w)
    Ginv, G, rho = geom.metric_data(Th)
    print('u =', u, ' G^{-1}(0) diag =', [str(Ginv[i][i].c0()) for i in range(4)], ' offdiag zero:', all(jl.isz(Ginv[i][j].c0()) for i in range(4) for j in range(4) if i != j),
          ' expected diag:', [str(1/(u+2)**2)]*2 + ['1/4', '1/4'])
res = pickle.load(open('su2_a2_unit.pkl', 'rb'))
h1, h2, h3, u = sp.symbols('h1 h2 h3 u')
sub = {h2: -h1*(h1**2 + 4*h1 + 10)/2, h3: 3*h1*(h1**4 + 8*h1**3 + 26*h1**2 + 40*h1 + 40)/4}
R = sp.factor(sp.simplify(res['R'].subs(sub)))
C2 = sp.factor(sp.simplify((res['riem2'] - 2*res['ric2'] + res['R']**2/3).subs(sub)))
print('R_G(u) =', R, '   Weyl^2(u) =', C2)
