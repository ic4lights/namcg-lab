"""Explicit rotation-invariant self-dual example:  omega = b_i eta^i,
   b_1 + i b_2 = -(x1 + i x2)(x3 - i x4),  b_3 = 1 + x3^2 - x4^2.
Checks (exact rational arithmetic, jets): d omega = 0 (Jacobi), J = 0, G = rho*delta with rho = |b|^2 (so g_rho flat),
curvature of G (R_G != 0 on Sigma={x1=x2=0}), Weyl^2 = 0, a_1 and a_2 totals at (N_s, n_D) = (6,2) vanish,
sector a_2 densities nonzero, invariance of Theta under the (12)-rotation (checked at a point)."""
import sympy as sp
import jetlib as jl
from jetlib import Jet
from common import *
import geom, sd_family, lib
use_gaussian(3)
gm = gam_mn_domain()
X = sd_family.X
b1 = -(X[0]*X[2] + X[1]*X[3]); b2 = X[0]*X[3] - X[1]*X[2]; b3 = 1 + X[2]**2 - X[3]**2
bsol = [b1, b2, b3]
eta = lib.eta3()
# check closure symbolically
w = sum((bsol[i]*eta[i] for i in range(3)), sp.zeros(4, 4))
cl = [sp.simplify(sp.diff(w[bb, c], X[a]) + sp.diff(w[c, a], X[bb]) + sp.diff(w[a, bb], X[c])) for a in range(4) for bb in range(4) for c in range(4)]
print('d omega = 0 :', all(e == 0 for e in cl))
rho_sym = sp.expand(bsol[0]**2 + bsol[1]**2 + bsol[2]**2)
print('rho = |b|^2 =', rho_sym)
pts = [(0, 0, sp.Rational(1, 3), sp.Rational(1, 5)), (0, 0, 0, 0), (sp.Rational(1, 2), sp.Rational(1, 7), sp.Rational(1, 3), sp.Rational(-1, 4))]
for x0 in pts:
    wj = sd_family.omega_jets(bsol, eta, x0)
    Th = theta_from_omega(wj)
    J = [sum((Th[m][r]*Th[m][n].diff(r) for m in range(4) for r in range(4)), Jet()).c0() for n in range(4)]
    out, sqrtG, base = geom.sector_all(Th, gm)
    Ginv, G, rho = geom.metric_data(Th)
    rho_expected = rho_sym.subs({X[i]: x0[i] for i in range(4)})
    cf = all((G[i][j].c0() == (QQ_I.from_sympy(sp.Rational(rho_expected)) if i == j else QQ_I(0))) for i in range(4) for j in range(4))
    # g_rho = G/rho flat: Weyl-type combination and Ricci of g_rho
    gr_inv = [[Ginv[i][j]*rho for j in range(4)] for i in range(4)]
    gr = jl.minv(gr_inv)
    Gam = geom.christoffel(gr, gr_inv); Rm, Ric, Rs = geom.riemann(Gam, gr, gr_inv)
    flat = all(jl.isz(v.c0()) for v in Rm.values())
    Ns, nD = 6, 2
    tot1 = sqrtG*((Ns-2)*out['scalar'][0] + out['vector'][0] - nD*out['dirac'][0])
    tot2 = sqrtG*((Ns-2)*out['scalar'][1] + out['vector'][1] - nD*out['dirac'][1])
    print('x0 =', x0)
    print('   J(0) =', [str(j) for j in J], ' G = rho*delta:', cf, ' g_rho flat (Riemann=0):', flat)
    print('   R_G =', base['R'], '  Weyl^2-type =', base['riem2'] - 2*base['ric2'] + base['R']**2/3, '  rho=', base['rho'])
    print('   a1_total =', tot1, ' a2_total =', tot2, '  sector a2:', [str(sqrtG*out[k][1]) for k in ('scalar', 'vector', 'dirac')])
# rotation invariance: Theta^{mn}(R x) = R Theta(x) R^T for R = rotation by pi/2 in (12): (x1,x2)->(-x2,x1)
Rm_ = sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
xx = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 7), sp.Rational(1, 3), sp.Rational(-1, 4)])
def Theta_at(x):
    wmat = sum((bsol[i].subs({X[k]: x[k] for k in range(4)}, simultaneous=True)*eta[i] for i in range(3)), sp.zeros(4, 4))
    return wmat.inv()
print('rotation invariance Theta(Rx) = R Theta(x) R^T :', sp.simplify(Theta_at(Rm_*xx) - Rm_*Theta_at(xx)*Rm_.T) == sp.zeros(4, 4))
