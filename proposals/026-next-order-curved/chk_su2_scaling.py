"""Scale covariance of the SU(2) family on shell: at general (r0,h0) with h' = u h/r, h'' = (h/r^2) h2(u), h''' = (h/r^3) h3(u),
  Weyl^2 = (3/2) u^2 (u+4)^2/(h0 r0)^4 ,  R_G = R(u)/(h0 r0)^2 ,  with R(u) = -3 u^2 (3u^2+16u+24)/(8 (u+2)^2),
and the totals a_1, a_2 (N_s=6,n_D=2) vanish.  Exact rational arithmetic at (r0,h0,u) = (2,3,-1/2), (1/2,5,1)."""
import sympy as sp
from sympy import QQ_I
import jetlib as jl
from common import use_gaussian, theta_from_omega, gam_weyl_real
import su2_family as F, geom
use_gaussian(3)
class Wrap:
    one = QQ_I(1); zero = QQ_I(0)
    @staticmethod
    def convert(x): return QQ_I.from_sympy(sp.Rational(x))
for (r0, h0, u) in [(2, 3, sp.Rational(-1, 2)), (sp.Rational(1, 2), 5, sp.Integer(1))]:
    r0 = sp.Rational(r0); h0 = sp.Rational(h0)
    h1 = u*h0/r0
    h2 = h0/r0**2*(-u*(u**2 + 4*u + 10)/2)
    h3 = h0/r0**3*(3*u*(u**4 + 8*u**3 + 26*u**2 + 40*u + 40)/4)
    w = F.omega_jets_su2(Wrap, (r0, h0, h1, h2, h3))
    geom.SIGN_OVERRIDE = None
    Th = theta_from_omega(w)
    out, sqrtG, base = geom.sector_all(Th, None)
    Ginv, G, rho = geom.metric_data(Th)
    Gam = geom.christoffel(G, Ginv)
    tot1 = jl.ZERO; tot2 = jl.ZERO
    gmU = None
    from common import gam_weyl_real
    # Dirac from the two real Weyl blocks
    res_d = []
    Rm, Ric, Rs = geom.riemann(Gam, G, Ginv); riem2, ric2 = geom.curvature_invariants(Rm, Ric, Rs, G, Ginv)
    for blk in ('upper', 'lower'):
        gm = gam_weyl_real(blk, QQ_I)
        A_, B_ = geom.dirac_AB(Th, G, Ginv, rho, gm)
        om, EV, Om = geom.vassilevich(A_, B_, G, Ginv, Gam, 4)
        res_d.append(geom.a_densities(EV, Om, Rs, riem2, ric2, Ginv, 4))
    d1 = (res_d[0][0] + res_d[1][0])/2; d2 = (res_d[0][1] + res_d[1][1])/2
    t1 = sqrtG*(4*out['scalar'][0] + out['vector'][0] - 2*d1)
    t2 = sqrtG*(4*out['scalar'][1] + out['vector'][1] - 2*d2)
    C2 = base['riem2'] - 2*base['ric2'] + base['R']**2/3
    pred_C2 = sp.Rational(3, 2)*u**2*(u + 4)**2/(h0*r0)**4
    pred_R = -3*u**2*(3*u**2 + 16*u + 24)/(8*(u + 2)**2)/(h0*r0)**2
    f = lambda z: sp.Rational(z.x.numerator, z.x.denominator)
    print('(r0,h0,u)=', (r0, h0, u), ' Weyl^2 =', f(C2), 'pred', pred_C2, ' R_G =', f(base['R']), 'pred', pred_R, ' a1_tot, a2_tot =', t1, t2)
