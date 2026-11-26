"""Collect exact single-sector data at points of the families used in 026/029/031 and store them (strings of exact rationals)
for the content scan.  Per point:
  geometry : R, Rii, Rijij, Rsig, W (Weyl projection), riem2, ric2 (4D), rho
  sector data (G-orthonormal): e, X', trEv_G, trEf_G, trN_EG, tau, trJOm_v
  single-sector heat data (no sqrt G): a1, a2 and parts (trE, trE2, trOm2, cur) for scalar, vector, dirac.
Output: data.json
"""
import sys, json, random, itertools
import sympy as sp
from common import *
import jetlib as jl
from jetlib import Jet
import geom, sd_family, sd_rot_family, nonsd_family as NF, sector_data as S
use_gaussian(3)
gm = gam_mn_domain()

def Cc(z):
    z = z.c0() if hasattr(z, 'c0') else z
    return sp.sympify(QQ_I.to_sympy(z))

def point_record(wj):
    d = S.run_jets(wj)
    Th = theta_from_omega(wj)
    out, sqrtG, base = geom.sector_all(Th, gm)
    rec = {k: str(sp.Rational(sp.simplify(v))) for k, v in d.items()}
    rec['W'] = str(sp.nsimplify(d['Rijij'] - d['Rii'] + d['R'] / 3))
    rec['riem2'] = str(Cc(base['riem2']))
    rec['ric2'] = str(Cc(base['ric2']))
    for k in ('scalar', 'vector', 'dirac'):
        a1, a2, parts = out[k]
        rec[k + '_a1'] = str(Cc(a1)); rec[k + '_a2'] = str(Cc(a2))
        for pk, pv in parts.items():
            rec[k + '_' + pk] = str(Cc(pv))
    rec['sqrtG'] = str(Cc(sqrtG))
    return rec

def random_A_jets(seed, deg=4):
    random.seed(seed)
    A = []
    for mu in range(4):
        dd = {}
        for mon in itertools.product(range(deg + 1), repeat=4):
            if 1 <= sum(mon) <= jl.N + 1 and random.random() < 0.5:
                dd[mon] = Q(random.randint(-3, 3), random.randint(1, 3))
        A.append(Jet({k: v for k, v in dd.items() if not jl.isz(v)}))
    return A

if __name__ == '__main__':
    x1, x2, x3, x4 = sd_family.X
    recs = []
    # (a) 029 example
    b1 = -(x1 * x3 + x2 * x4); b2 = x1 * x4 - x2 * x3; b3 = 1 + x3**2 - x4**2
    eta = sd_family.lib.eta3()
    for x0 in [(0, 0, sp.Rational(1, 3), sp.Rational(1, 5)), (0, 0, sp.Rational(1, 2), sp.Rational(-1, 3)), (0, 0, sp.Rational(2, 3), sp.Rational(1, 7))]:
        wj = sd_family.omega_jets([b1, b2, b3], eta, x0)
        r = point_record(wj); r.update(family='SD example (029)', pt=str(x0), sigma_tg=True)
        rho = b1**2 + b2**2 + b3**2
        sub = {x1: 0, x2: 0, x3: x0[2], x4: x0[3]}
        r['g'] = str(sp.together((sp.diff(rho, x3).subs(sub)**2 + sp.diff(rho, x4).subs(sub)**2) / rho.subs(sub)**3))
        recs.append(r); print(r['family'], r['pt']); sys.stdout.flush()
    # (b) rotation-invariant SD family
    for seed in range(4):
        bsol, eta2, nf = sd_rot_family.rot_solution(4, seed)
        rho = sp.expand(bsol[0]**2 + bsol[1]**2 + bsol[2]**2)
        random.seed(90 + seed)
        for t in range(2):
            p3 = sp.Rational(random.randint(-4, 4), random.randint(2, 6)); p4 = sp.Rational(random.randint(1, 4), random.randint(2, 6))
            sub = {x1: 0, x2: 0, x3: p3, x4: p4}
            rho0 = rho.subs(sub)
            if rho0 == 0: continue
            g = sp.together((sp.diff(rho, x3).subs(sub)**2 + sp.diff(rho, x4).subs(sub)**2) / rho0**3)
            wj = sd_family.omega_jets(bsol, eta2, (0, 0, p3, p4))
            r = point_record(wj); r.update(family='SD rot-invariant', pt=str((0, 0, p3, p4)), seed=seed, sigma_tg=True, g=str(g))
            recs.append(r); print(r['family'], r['pt']); sys.stdout.flush()
    # (c) non-SD J=0 family d(h Lambda^3)
    r_ = NF.r
    C0 = sp.Rational(16, 25)
    for sign in (+1, -1):
        h = 1 + sign * sp.sqrt(1 - C0 / r_**4)
        for x0 in [(0, 0, sp.Rational(3, 5), sp.Rational(4, 5)), (0, 0, sp.Rational(4, 5), sp.Rational(-3, 5))]:
            wj = NF.omega_jets(h, x0)
            r = point_record(wj); r.update(family='non-SD J=0 (h=1%s sqrt(1-C/r^4))' % ('+' if sign > 0 else '-'), pt=str(x0), sigma_tg=True)
            recs.append(r); print(r['family'], r['pt']); sys.stdout.flush()
    # (d) non-SD J != 0 radial profiles (totally geodesic Sigma by symmetry)
    for name, h in (('1+r^2', 1 + r_**2), ('1/(1+r^2)', 1 / (1 + r_**2))):
        x0 = (0, 0, sp.Rational(3, 5), sp.Rational(4, 5))
        wj = NF.omega_jets(h, x0)
        r = point_record(wj); r.update(family='non-SD J!=0 h=' + name, pt=str(x0), sigma_tg=True)
        recs.append(r); print(r['family'], r['pt']); sys.stdout.flush()
    # (e) generic closed omega (algebraic identities only; Sigma not totally geodesic)
    base = [[Q(0), Q(2), Q(1), Q(0)], [Q(-2), Q(0), Q(0), Q(1)], [Q(-1), Q(0), Q(0), Q(3)], [Q(0), Q(-1), Q(-3), Q(0)]]
    for seed in range(3):
        A = random_A_jets(seed)
        w = omega_from_A(A)
        w = [[w[m][n] + Jet.const(base[m][n]) for n in range(4)] for m in range(4)]
        r = point_record(w); r.update(family='generic closed omega (algebraic only)', pt='seed %d' % seed, sigma_tg=False)
        recs.append(r); print(r['family'], r['pt']); sys.stdout.flush()
    json.dump(recs, open('data.json', 'w'), indent=1)
    print('saved', len(recs))
