"""081 s3_r2: exact facts for rho_p(mu) = p! h_p(mu) / (sum mu)^p.

Supersedes s3_profile_concentration.py (its bound claim (4) is FALSE: that
script fails its own assert with 384 violations on its own profiles; the
counterexample (9/10,1/10) at p=3 is reproduced below). Corrected facts:
 (1) 1 < rho_p <= p! for every profile and p >= 2; both ends sharp in the
     limit sense: p! at a single nonzero slot, and inf = 1 as D_eff -> inf;
     exact elementary proof: p! h_p - S1^p = sum_{|alpha|=p}(p! - p!/alpha!) mu^alpha > 0
     and (sum mu)^p >= h_p term-by-term, equality only at p <= 1.
 (2) rho_p = sum_{lambda |- p} (p!/z_lambda) prod_k (s_k/S1^k)^{m_k}, exact
     (h_p = sum_lambda p_lambda/z_lambda); check on random profiles p<=6.
 (3) exact lower bound on the concentration defect: rho_p - 1 >= C(p,2)/D_eff,
     D_eff = S1^2/s_2; equality of the p=2 term is the identity rho_2 =
     1 + 1/D_eff; also rho_3 = 1 + 3/D_eff + 2 s_3/S1^3 (exact).
 (4) uniform profiles attain rho_p = prod_{i=1}^{p-1}(1 + i/D) exactly and are
     the sampled minimisers; violations of rho_p >= prod(1+i/D) and of (3)
     must both count 0.
 (5) audit of the superseded bound rho_p <= prod(1+i/D_eff): counterexample
     and reproduction of the superseded script's own violation count (384) on
     its profile list, same seed and order.
 (6) fuzzy-sphere-type proxy profiles mu_l = f(l) with multiplicity 2l+1:
     D_eff table for f = nu l/2 and f = l(l+1)/4 over l_c = 10..640.

Run: python -I proposals/081-g-edge-moments/s3_profile_concentration_r2.py
Expected invariants: bound violations 0 (both (3) and (4)); partition-identity
failures 0; counterexample p=3 excess 123/25 - 3003/625 > 0; reproduced
superseded violation count 384; last line 'PASS s3'.
"""
from fractions import Fraction
from math import comb, factorial

import numpy as np


def hcf(m, xs):
    pw = [sum(x ** t for x in xs) for t in range(m + 1)]
    h = [Fraction(1)]
    for m2 in range(1, m + 1):
        h.append(sum(pw[t] * h[m2 - t] for t in range(1, m2 + 1)) / m2)
    return h[m]


def rho(p, mu):
    return factorial(p) * hcf(p, mu) / sum(mu) ** p


def deff(mu):
    return sum(mu) ** 2 / sum(x * x for x in mu)


def uprod(p, D):
    out = Fraction(1)
    for i in range(1, p):
        out *= 1 + Fraction(i, D)
    return out


def partition_terms(p):
    out = []

    def rec(rem, maxpart, m):
        if rem == 0:
            out.append(tuple(m))
            return
        for k in range(min(maxpart, rem), 0, -1):
            m[k - 1] += 1
            rec(rem - k, k, m)
            m[k - 1] -= 1
    rec(p, p, [0] * p)
    return out


def z_lambda(m):
    z = 1
    for k, mk in enumerate(m, start=1):
        z *= (k ** mk) * factorial(mk)
    return z


def rho_partition(p, mu):
    """sum_lambda (p!/z_lambda) prod_k (s_k/S1^k)^{m_k} -- should equal rho(p)."""
    S1 = sum(mu)
    sk = {k: sum(x ** k for x in mu) for k in range(1, p + 1)}
    tot = Fraction(0)
    for m in partition_terms(p):
        term = Fraction(factorial(p), z_lambda(m))
        for k, mk in enumerate(m, start=1):
            term *= (Fraction(sk[k], 1) / S1 ** k) ** mk
        tot += term
    return tot


def draft_profiles(rng):
    """The superseded script's profile list, same seed and construction order."""
    profiles = []
    for D in (2, 3, 7, 40, 120):
        profiles.append(('uniform', D, [Fraction(1, D)] * D))
    for D in (2, 3, 7, 40, 120):
        profiles.append(('single+tail', D, [Fraction(1, 2)] + [Fraction(1, 2 * (D - 1))] * (D - 1)))
    for D in (4, 10, 60):
        profiles.append(('geometric', D, [Fraction(2, 3) ** i for i in range(D)]))
    for D in (4, 10, 60):
        profiles.append(('arithmetic', D, [Fraction(i + 1) for i in range(D)]))
    for t in range(40):
        x = rng.dirichlet(np.ones(17))
        profiles.append(('dirichlet', 17, [Fraction(int(round(v * 10 ** 6)), 10 ** 6) for v in x]))
    for t in range(40):
        x = np.exp(rng.standard_normal(23))
        x = x / x.sum()
        profiles.append(('lognormal', 23, [Fraction(int(round(v * 10 ** 6)), 10 ** 6) for v in x]))
    for lc in (10, 40, 160):
        for name, f in (('nu_l2', lambda l: l / 2), ('ll1_4', lambda l: l * (l + 1) / 4)):
            mu = []
            for l in range(1, lc + 1):
                mu += [Fraction(int(f(l) * 1000), 1000)] * (2 * l + 1)
            profiles.append((f'fuzzy {name} lc={lc}', len(mu), mu))
    return profiles


def main():
    # exact sharp two-sided fact, and uniform exact product
    assert rho(6, [Fraction(1)]) == 720
    assert rho(4, [Fraction(1, 120)] * 120) == uprod(4, 120)
    assert rho(6, [Fraction(1, 120)] * 120) == uprod(6, 120)
    print(f"bounds: rho_6(single slot) = {rho(6, [Fraction(1)])} = 6! (sharp max); "
          f"uniform D=120 attains prod(1+i/120) exactly: rho_4 = "
          f"{rho(4, [Fraction(1,120)]*120)} = {uprod(4, 120)}")
    rng = np.random.default_rng(81004)
    bad2 = bad3 = badP = violB = violU = strictfail = 0
    for t in range(1000):
        D = int(rng.integers(1, 10))
        x = rng.random(D) ** rng.choice([1.0, 1.0, 3.0, 0.3])
        mu = [Fraction(int(v * 10 ** 5), 10 ** 5) for v in x / x.sum()]
        S1 = sum(mu)
        s2 = sum(v * v for v in mu)
        s3 = sum(v ** 3 for v in mu)
        if rho(2, mu) != 1 + s2 / S1 ** 2:
            bad2 += 1
        if rho(3, mu) != 1 + 3 * s2 / S1 ** 2 + 2 * s3 / S1 ** 3:
            bad3 += 1
        for p in range(2, 7):
            rp = rho(p, mu)
            if rp <= 1 or rp > factorial(p):
                strictfail += 1
            if rp - 1 < Fraction(p * (p - 1), 2) * s2 / S1 ** 2:
                violB += 1
            if rho_partition(p, mu) != rp:
                badP += 1
        for p in range(1, 7):
            if rho(p, mu) < uprod(p, D):
                violU += 1
    print(f"1000 random profiles p=1..6: rho_2 identity failures {bad2}; rho_3 "
          f"identity failures {bad3}; partition-identity failures {badP}; strict "
          f"1 < rho_p <= p! failures {strictfail}; defect-bound rho_p-1 >= "
          f"C(p,2)/D_eff violations {violB}; uniform-minimiser rho_p >= prod(1+i/D) "
          f"violations {violU}")
    assert bad2 == 0 and bad3 == 0 and badP == 0 and strictfail == 0
    assert violB == 0 and violU == 0
    # audit of the superseded bound rho_p <= prod(1+i/D_eff): counterexample,
    # then reproduction of the superseded script's own violation count
    xs = [Fraction(9, 10), Fraction(1, 10)]
    ex3 = rho(3, xs) - uprod(3, Fraction(1, 1) / (sum(x * x for x in xs)))
    print(f"superseded bound audit: counterexample (9/10,1/10), D_eff = "
          f"{deff(xs)}: rho_3 = {rho(3, xs)}, superseded bound = "
          f"{uprod(3, deff(xs))}, excess = {ex3} > 0; also p=4 excess = "
          f"{rho(4, xs) - uprod(4, deff(xs))} > 0")
    assert ex3 > 0
    rngd = np.random.default_rng(81003)
    profiles = draft_profiles(rngd)
    viol = 0
    for name, D, mu in profiles:
        if sum(mu) <= 0:
            continue
        d = deff(mu)
        for p in range(2, 7):
            if rho(p, mu) > uprod(p, d):
                viol += 1
    print(f"reproduction of superseded profile list (102 profiles, seed 81003, "
          f"p=2..6): violations of the superseded bound = {viol} (superseded "
          f"script asserted 0 and fails its own assert)")
    assert viol == 384, viol
    # fuzzy proxy D_eff table
    for name, f in (('nu_l2', lambda l: l / 2), ('ll1_4', lambda l: l * (l + 1) / 4)):
        row = []
        for lc in (10, 40, 160, 640):
            mu = []
            for l in range(1, lc + 1):
                mu += [Fraction(int(f(l) * 1000), 1000)] * (2 * l + 1)
            row.append(f"lc={lc}:D_eff={float(deff(mu)):.1f}")
        print(f"D_eff {name}: " + " ".join(row))
    print("PASS s3")


if __name__ == '__main__':
    main()
