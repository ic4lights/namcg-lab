"""081 s3: exact concentration facts for rho_p(mu) = p! h_p(mu) / (sum mu)^p.

r = |w_perp|^2 has moments <r^p> = p! h_p(mu); the leading-order identification
of the charge moment with the single scale (sum mu)^p is exact iff rho_p = 1.
Facts checked in exact rational arithmetic:
 (1) 1 <= rho_p <= p! for every profile (sharp ends: one nonzero slot gives p!;
     uniform profile gives rho_p = prod_{i=1}^{p-1}(1+i/D) -> 1 as D -> infinity).
 (2) rho_2 = 1 + Lambda_1^... exact: rho_2 = 1 + D_eff^{-1}, D_eff = (sum mu)^2/sum mu^2.
 (3) rho_3 = 1 + 3/D_eff + 2 S3/S1^3, S3 = sum mu^3.
 (4) rho_p <= prod_{i=1}^{p-1}(1 + i/D_eff) for all tested profiles, p <= 6,
     D_eff computed from the profile; tested profiles: uniform, single, geometric,
     arithmetic, degenerate fuzzy-type (mu with multiplicities 2l+1, f = nu l/2),
     Dirichlet-random, lognormal-random; violation count must be 0.
 (5) fuzzy-sphere-type profiles: D_eff grows with l_c: table for f = nu l/2 and
     f = l(l+1)/4 over l_c = 10..640.

Run: python -I proposals/081-g-edge-moments/s3_profile_concentration.py
Expected invariants: bound violations 0; exact (2),(3) equalities; last line 'PASS s3'.
"""
from fractions import Fraction
from math import comb, factorial

import numpy as np


def h_complete_frac(m, mu):
    p = [sum(x**t for x in mu) for t in range(m + 1)]
    h = [Fraction(1)]
    for m2 in range(1, m + 1):
        h.append(sum(p[t] * h[m2 - t] for t in range(1, m2 + 1)) / m2)
    return h[m]


def rho(p, mu):
    return factorial(p) * h_complete_frac(p, mu) / sum(mu)**p


def prod_bound(p, deff):
    out = Fraction(1)
    for i in range(1, p):
        out *= (1 + Fraction(i, deff))
    return out


def main():
    rng = np.random.default_rng(81003)
    profiles = []
    for D in (2, 3, 7, 40, 120):
        profiles.append(('uniform', D, [Fraction(1, D)] * D))
    for D in (2, 3, 7, 40, 120):
        profiles.append(('single+tail', D, [Fraction(1, 2)] + [Fraction(1, 2*(D-1))]*(D-1)))
    for D in (4, 10, 60):
        profiles.append(('geometric', D, [Fraction(2, 3)**i for i in range(D)]))
    for D in (4, 10, 60):
        profiles.append(('arithmetic', D, [Fraction(i+1) for i in range(D)]))
    for t in range(40):
        x = rng.dirichlet(np.ones(17))
        profiles.append(('dirichlet', 17, [Fraction(int(round(v*10**6)), 10**6) for v in x]))
    for t in range(40):
        x = np.exp(rng.standard_normal(23))
        x = x / x.sum()
        profiles.append(('lognormal', 23, [Fraction(int(round(v*10**6)), 10**6) for v in x]))
    # fuzzy-type degenerate profile: mu_l = f(l) with multiplicity (2l+1), l<=lc
    for lc in (10, 40, 160):
        for name, f in (('nu_l2', lambda l: l/2), ('ll1_4', lambda l: l*(l+1)/4)):
            mu = []
            for l in range(1, lc + 1):
                mu += [Fraction(int(f(l)*1000), 1000)] * (2*l + 1)
            profiles.append((f'fuzzy {name} lc={lc}', len(mu), mu))
    viol = 0
    bad2 = 0
    bad3 = 0
    maxupper = 0.0
    for name, D, mu in profiles:
        if sum(mu) <= 0:
            continue
        s1, s2 = sum(mu), sum(x*x for x in mu)
        s3 = sum(x**3 for x in mu)
        deff = Fraction(s1*s1, 1) / s2 if s2 else None
        for p in range(1, 7):
            rp = rho(p, mu)
            assert rp >= 1, ('lower', name, p)
            assert rp <= factorial(p), ('upper', name, p)
            if p >= 2 and deff is not None and rp > prod_bound(p, deff):
                viol += 1
        if rho(2, mu) != 1 + Fraction(s2, s1*s1):
            bad2 += 1
        if rho(3, mu) != 1 + 3*Fraction(s2, s1*s1) + 2*Fraction(s3, s1**3):
            bad3 += 1
        maxupper = max(maxupper, float(rho(6, mu)))
    print(f"profiles tested: {len(profiles)}; bound violations of "
          f"rho_p <= prod(1+i/D_eff): {viol}; rho_2 identity failures: {bad2}; "
          f"rho_3 identity failures: {bad3}")
    # sharp ends
    print(f"rho_6(one slot) = {rho(6,[Fraction(1)])} (= 6! = 720: upper sharp); "
          f"rho_6(uniform D=120) = {float(rho(6,[Fraction(1,120)]*120)):.6f} (lower trend)")
    # D_eff growth for fuzzy profiles
    for name, f in (('nu_l2', lambda l: l/2), ('ll1_4', lambda l: l*(l+1)/4)):
        row = []
        for lc in (10, 40, 160, 640):
            mu = []
            for l in range(1, lc + 1):
                mu += [Fraction(int(f(l)*1000), 1000)] * (2*l + 1)
            s1, s2 = sum(mu), sum(x*x for x in mu)
            row.append(f"lc={lc}:D_eff={float(Fraction(s1*s1)/s2):.1f}")
        print(f"D_eff {name}: " + " ".join(row))
    assert viol == 0 and bad2 == 0 and bad3 == 0
    print('PASS s3')


if __name__ == '__main__':
    main()
