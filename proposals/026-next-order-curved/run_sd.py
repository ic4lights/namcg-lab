import sys
import jetlib as jl
from jetlib import Jet
from common import *
import geom, sd_family
use_gaussian(3)
gm = gam_mn_domain()
for anti in (False, True):
    for seed in (1, 2):
        bsol, eta = sd_family.sd_solution(deg=3, seed=seed, anti=anti, b0=(1, 2, 3))
        for x0 in [(0, 0, 0, 0), (Rational(1, 3), Rational(-1, 5), Rational(1, 2), Rational(1, 7))]:
            w = sd_family.omega_jets(bsol, eta, x0)
            Th = theta_from_omega(w)
            J = [sum((Th[m][r]*Th[m][n].diff(r) for m in range(4) for r in range(4)), Jet()) for n in range(4)]
            Jv = [j.c0() for j in J]
            out, sqrtG, base = geom.sector_all(Th, gm)
            Ns, nD = 6, 2
            tot = sqrtG*((Ns-2)*out['scalar'][1] + out['vector'][1] - nD*out['dirac'][1])
            tot1 = sqrtG*((Ns-2)*out['scalar'][0] + out['vector'][0] - nD*out['dirac'][0])
            print('anti' if anti else 'self', 'seed', seed, 'x0', x0)
            print('  J(0) =', Jv, ' R_G =', base['R'], ' Weyl-type: riem2-2ric2+R2/3 =', base['riem2'] - 2*base['ric2'] + base['R']**2/3)
            print('  a1 total (N_s=6,n_D=2):', tot1, ' a2 total:', tot)
            print('  per-sector sqrtG*a2: scalar', sqrtG*out['scalar'][1], ' vector', sqrtG*out['vector'][1], ' dirac', sqrtG*out['dirac'][1])
