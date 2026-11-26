import random
import jetlib as jl
from jetlib import Jet
from common import *
import geom
use_gaussian(3)
random.seed(5)
y = [Jet.var(i) for i in range(4)]
def rq(): return Q(random.randint(-6, 6), random.randint(1, 5))
def rpoly(deg):
    t = Jet()
    for mon in itertools.product(range(deg+1), repeat=4):
        if 1 <= sum(mon) <= deg:
            m = Jet.const(rq())
            for i, e in enumerate(mon):
                for _ in range(e): m = m * y[i]
            t = t + m
    return t
c = [[0,2,0,1],[-2,0,3,0],[0,-3,0,1],[-1,0,-1,0]]
A = [rpoly(4) for _ in range(4)]
w = omega_from_A(A); w = [[w[m][n] + Jet.const(Q(c[m][n])) for n in range(4)] for m in range(4)]
Th = theta_from_omega(w)
out, sqrtG, base = geom.sector_all(Th, gam_mn_domain())
Ginv, G, rho = geom.metric_data(Th)
Gam = geom.christoffel(G, Ginv)
Rm, Ric, Rs = geom.riemann(Gam, G, Ginv)
riem2, ric2 = geom.curvature_invariants(Rm, Ric, Rs, G, Ginv)
tot = [jl.ZERO, jl.ZERO]
for blk in ('upper', 'lower'):
    gm = gam_weyl_real(blk, QQ_I)
    A_, B_ = geom.dirac_AB(Th, G, Ginv, rho, gm)
    om, EV, Om = geom.vassilevich(A_, B_, G, Ginv, Gam, 4)
    a1, a2, parts = geom.a_densities(EV, Om, Rs, riem2, ric2, Ginv, 4)
    tot[0] += a1/2; tot[1] += a2/2
print('complex Dirac a1,a2:', out['dirac'][0], out['dirac'][1])
print('real Weyl-pair  a1,a2:', tot[0], tot[1])
print('match:', out['dirac'][0] == tot[0] and out['dirac'][1] == tot[1])
