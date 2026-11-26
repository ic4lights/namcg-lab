"""Table of the log-order replica variants on J=0 backgrounds (24 pi units).
 R1 = fixed-state (029)               : s24 = (4/3)R + 2Rii - 2Rj + 2W - 12e + (3/2)X' - tau
 CE_H  = -(R + 3 tr_N E_G)           : vector Ricci-type delta, Hodge distribution (normal block)
 CE_U  = -(R + (3/2) tr E_G)         : vector delta uniformly distributed (trace 4 pi), cf. the Q = 1/4 contact of 021
 COm   = tr(J Omega_12)_vector        : bundle-curvature delta (rotation of the internal normal plane)
 variants:  R1 ; R1+CE ; R1+COm ; R1+CE+COm (E_delta Hodge or uniform).
Families: (a) 029 example; (b) rotation-invariant SD family (random data); (c) non-self-dual J=0 family d(h Lambda^3), h = 1 +- sqrt(1 - C/r^4)."""
import sys, random
import sympy as sp
from common import *
import sd_family, sd_rot_family, nonsd_family as NF, sector_data as S
use_gaussian(3)
x1, x2, x3, x4 = sd_family.X
def line(tag, d, g=None):
    R, Rii, Rj, e = d['R'], d['Rii'], d['Rijij'], d['e']
    W = Rj - Rii + R/3
    s24 = sp.Rational(4, 3)*R + 2*Rii - 2*Rj + 2*W - 12*e + sp.Rational(3, 2)*d['Xp'] - d['tau']
    CE_H = -(R + 3*d['trN_EG']); CE_U = -(R + sp.Rational(3, 2)*d['trEv_G']); COm = d['trJOm_v']
    out = dict(W=W, e_minus_R6=sp.simplify(e - R/6), s24=sp.nsimplify(s24), CE_H=CE_H, CE_U=CE_U, COm=COm, tau=d['tau'], Xp=d['Xp'],
               R1_CE_H=sp.simplify(s24 + CE_H), R1_COm=sp.simplify(s24 + COm), TOT_H=sp.simplify(s24 + CE_H + COm), TOT_U=sp.simplify(s24 + CE_U + COm),
               RSig=d['Rsig'])
    if g is not None:
        out['g'] = g
        out['chk_s24=1.5g-RSig'] = sp.simplify(s24 - (sp.Rational(3, 2)*g - d['Rsig']))
        out['chk_CE=-1.5X'] = sp.simplify(CE_H + sp.Rational(3, 2)*d['Xp'])
        out['chk_COm=tau'] = sp.simplify(COm - d['tau'])
        out['chk_CE_H=CE_U'] = sp.simplify(CE_H - CE_U)
    print(tag); [print('   ', k, '=', v) for k, v in out.items()]; sys.stdout.flush()
# (a) 029 example
b1 = -(x1*x3 + x2*x4); b2 = x1*x4 - x2*x3; b3 = 1 + x3**2 - x4**2
eta = sd_family.lib.eta3()
for x0 in [(0, 0, sp.Rational(1, 3), sp.Rational(1, 5)), (0, 0, sp.Rational(1, 2), sp.Rational(-1, 3)), (0, 0, sp.Rational(2, 3), sp.Rational(1, 7))]:
    d = S.run(x0, [b1, b2, b3], eta)
    g = ((sp.diff(b3**2, x3)**2 + sp.diff(b3**2, x4)**2)/(b3**2)**3).subs({x1: 0, x2: 0, x3: x0[2], x4: x0[3]})
    line('029 example %s' % (x0,), d, g)
    print('    ratio (CE+COm)/RSig =', sp.simplify((d['trJOm_v'] - (d['R'] + 3*d['trN_EG']))/24/d['Rsig']), '(expected -1/(12) in units 1/pi on the example)')
# (b) rotation-invariant SD family
for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 2):
    bsol, eta2, nf = sd_rot_family.rot_solution(4, seed)
    rho = sp.expand(bsol[0]**2 + bsol[1]**2 + bsol[2]**2)
    random.seed(90 + seed)
    for t in range(2):
        p3 = sp.Rational(random.randint(-4, 4), random.randint(2, 6)); p4 = sp.Rational(random.randint(1, 4), random.randint(2, 6))
        sub = {x1: 0, x2: 0, x3: p3, x4: p4}
        rho0 = rho.subs(sub)
        if rho0 == 0: continue
        g = sp.together((sp.diff(rho, x3).subs(sub)**2 + sp.diff(rho, x4).subs(sub)**2)/rho0**3)
        d = S.run((0, 0, p3, p4), bsol, eta2)
        line('SD rot-family seed %d pt %s' % (seed, (p3, p4)), d, g)
# (c) non-SD J=0
r = NF.r
C0 = sp.Rational(16, 25)
for sign in (+1, -1):
    h = 1 + sign*sp.sqrt(1 - C0/r**4)
    for x0 in [(0, 0, sp.Rational(3, 5), sp.Rational(4, 5))]:
        d = S.run_jets(NF.omega_jets(h, x0))
        line('non-SD J=0 sign %+d pt %s' % (sign, x0), d)
