"""Total a_2 density (mod explicit box terms) of the D=10 content (N_s=6, n_D=2) on RANDOM (off-shell, J != 0) Poisson bivectors."""
import random
import jetlib as jl
from jetlib import Jet
from common import *
import geom
use_gaussian(3)
gm = gam_mn_domain()
y = [Jet.var(i) for i in range(4)]
def rpoly(deg, rq):
    t = Jet()
    for mon in itertools.product(range(deg+1), repeat=4):
        if 1 <= sum(mon) <= deg:
            m = Jet.const(rq())
            for i, e in enumerate(mon):
                for _ in range(e): m = m * y[i]
            t = t + m
    return t
c = [[0,2,0,1],[-2,0,3,0],[0,-3,0,1],[-1,0,-1,0]]
for seed in range(3):
    random.seed(100 + seed)
    rq = lambda: Q(random.randint(-6, 6), random.randint(1, 5))
    A = [rpoly(4, rq) for _ in range(4)]
    w = omega_from_A(A)
    w = [[w[m][n] + Jet.const(Q(c[m][n])) for n in range(4)] for m in range(4)]
    Th = theta_from_omega(w)
    out, sqrtG, base = geom.sector_all(Th, gm)
    for (Ns, nD) in ((6, 2),):
        tot1 = sqrtG*((Ns-2)*out['scalar'][0] + out['vector'][0] - nD*out['dirac'][0])
        tot2 = sqrtG*((Ns-2)*out['scalar'][1] + out['vector'][1] - nD*out['dirac'][1])
        print('seed', seed, 'a1 total', tot1, ' a2 total (float)', float(tot2.x), ' scalar a2 (float)', float((sqrtG*out['scalar'][1]).x))
    parts = {k: out[k][2] for k in out}
    # decomposition of the total into its pieces
    for pname in ('trE', 'trE2', 'trOm2', 'cur'):
        val = sqrtG*((Ns-2)*parts['scalar'][pname] + parts['vector'][pname] - nD*parts['dirac'][pname])
        print('   piece', pname, float(val.x))
