"""Validate the jet machinery against the manuscript's a_1 identities (sec:status-F, Poisson-limit paragraph):
sqrtG tr(R/6 - E_m) = (n/6) rho R[g_rho] (+ rho^2 X for connection; + 1/2 rho^2 X for Dirac with n=4 weights as in 017)."""
import random
import jetlib as jl
from jetlib import Jet
from common import *
import geom
use_gaussian(3)
random.seed(11)
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
for trial in range(2):
    A = [rpoly(4) for _ in range(4)]
    w = omega_from_A(A)
    w = [[w[m][n] + Jet.const(Q(c[m][n]) * (trial+1)) for n in range(4)] for m in range(4)]
    Th = theta_from_omega(w)
    out, sqrtG, base = geom.sector_all(Th, gam_mn_domain())
    rho = base['rho']
    # g_rho curvature: metric with inverse rho*G^{mn}
    Ginv, G, rhoj = geom.metric_data(Th)
    gr_inv = [[Ginv[i][j]*rhoj for j in range(4)] for i in range(4)]
    gr = jl.minv(gr_inv)
    Gam = geom.christoffel(gr, gr_inv)
    Rm, Ric, Rs = geom.riemann(Gam, gr, gr_inv)
    Rrho = Rs.c0()
    X = jl.ZERO
    for r in range(4):
        for m in range(4):
            for n in range(4):
                X = X + Th[m][n].diff(r).c0()**2 * (Ginv[r][r].c0() * 0 + 1)
    # X = eta^{rho lambda} eta_{mu a} eta_{nu b} d_rho Theta^{mu nu} d_lambda Theta^{a b}, Euclid eta=delta
    print('trial', trial)
    print(' scalar : sqrtG*a1 =', sqrtG*out['scalar'][0], ' rho R[g_rho]/6 =', rho*Rrho/6)
    print(' vector : sqrtG*a1 =', sqrtG*out['vector'][0], ' 4/6 rho R + rho^2 X =', 4*rho*Rrho/6 + rho*rho*X)
    print(' dirac  : sqrtG*a1 =', sqrtG*out['dirac'][0], ' 4/6 rho R + 1/2 rho^2 X =', 4*rho*Rrho/6 + rho*rho*X/2)
