"""081 s1_r2: exact rank-one charge spectrum polynomial and Gaussian (Wick) form.

Supersedes s1_spectrum_wick.py (buggy 2**(2*p+1-j); see manifest lineage).
Corrected facts, all exact:
 Part 1. Q = -2i(|u)(w| - |w)(u|), (u|u)=1: nonzero spectrum is the pair
   lambda_pm = -2a +/- 2*sqrt(a^2+r), a = Im(u|w) real, r = |w|^2 - |(u|w)|^2.
   EVEN: Tr Q^{2p} = sum_{j=0}^p C(2p,2j) 2^(2p+1) a^(2p-2j) (a^2+r)^j
   (the 2^(2p+1) is j-INDEPENDENT; the superseded draft had 2^(2p+1-j)).
   ODD:  Tr Q^{2p+1} = -sum_{j=0}^p C(2p+1,2j) 2^(2p+2) a^(2p+1-2j) (a^2+r)^j.
 Part 2. Gaussian state model: a real centered Gaussian, V = <a^2>, independent
   of r = sum_i mu_i E_i with E_i iid Exp(1), so <r^m> = m! h_m(mu). Closed form:
   <Tr Q^{2p}> = 2^(2p+1) sum_{j=0}^p C(2p,2j) sum_{t=0}^j C(j,t)
                 (2(p-j+t)-1)!! V^(p-j+t) (j-t)! h_{j-t}(mu).
   Checked against exact bivariate moment integration, mu=(2,3), V=7/3, p=1..4.
 Part 3. Odd moments: polynomial odd in a; a symmetric and independent of r
   => <Tr Q^{2p+1}> = 0 exactly (exact antisymmetry + Monte-Carlo confirmation).

Run: python -I proposals/081-g-edge-moments/s1_spectrum_wick_r2.py
Expected invariants: PART1 symbolic p=1..6 exact (even), p=0..4 exact (odd),
numeric max rel dev < 1e-10; PART2 exact equality (sympy 0) p=1..4;
PART3 antisymmetry exact and |MC mean| < 1e-2 at p=1; last line 'PASS s1'.
"""
from fractions import Fraction
from math import comb

import numpy as np
import sympy as sp

a, r = sp.symbols('a r', real=True)


def h_complete(m, mu):
    """Complete homogeneous symmetric polynomial h_m of list mu (exact sympy)."""
    pw = [sum(sp.nsimplify(x) ** t for x in mu) for t in range(m + 1)]
    h = [sp.Integer(1)]
    for m2 in range(1, m + 1):
        h.append(sp.together(sp.Rational(1, m2) * sum(pw[t] * h[m2 - t]
                                                      for t in range(1, m2 + 1))))
    return sp.simplify(h[m])


def tr2p_exact(p):
    """Correct j-INDEPENDENT even spectral trace polynomial in a, a^2+r."""
    return sum(comb(2 * p, 2 * j) * 2 ** (2 * p + 1) * a ** (2 * p - 2 * j)
               * (a ** 2 + r) ** j for j in range(p + 1))


def tr_odd_exact(p):
    """Correct exact odd spectral trace polynomial (odd in a)."""
    return -sum(comb(2 * p + 1, 2 * j) * 2 ** (2 * p + 2) * a ** (2 * p + 1 - 2 * j)
                * (a ** 2 + r) ** j for j in range(p + 1))


def dfact2k(k):
    out = 1
    for i in range(1, k + 1):
        out *= (2 * i - 1)
    return out


def closed_form(p, mu, Vval):
    """(star) Gaussian closed form; mu list of ints/Fractions, Vval Fraction."""
    muS = [sp.Rational(x) for x in mu]
    V = sp.Rational(Vval)
    tot = sp.Integer(0)
    for j in range(p + 1):
        for t in range(j + 1):
            k = p - j + t
            tot += (sp.Rational(comb(2 * p, 2 * j) * comb(j, t) * dfact2k(k)
                                * sp.factorial(j - t))
                    * V ** k * h_complete(j - t, muS))
    return sp.simplify(2 ** (2 * p + 1) * tot)


def ground_truth(p, mu, Vval):
    """Exact bivariate moment integration with the CORRECTED spectrum."""
    A, R = sp.symbols('A R')
    P = sp.Poly(sp.expand(tr2p_exact(p).subs({a: A, r: R})), A, R)
    tot = sp.Integer(0)
    for (ea, er), c in P.terms():
        if ea % 2:
            continue
        mk = dfact2k(ea // 2) * sp.Rational(Vval) ** (ea // 2)
        mr = sp.factorial(er) * h_complete(er, [sp.Rational(x) for x in mu])
        tot += c * mk * mr
    return sp.simplify(tot)


def main():
    rng = np.random.default_rng(81001)
    lm = -2 * a + 2 * sp.sqrt(a ** 2 + r)
    lp = -2 * a - 2 * sp.sqrt(a ** 2 + r)
    for p in range(1, 7):
        assert sp.expand(tr2p_exact(p) - sp.expand(lm ** (2 * p) + lp ** (2 * p))) == 0
    for p in range(0, 5):
        assert sp.expand(tr_odd_exact(p) - sp.expand(lm ** (2 * p + 1) + lp ** (2 * p + 1))) == 0
    maxdev = 0.0
    for _ in range(400):
        N = 9
        u = rng.standard_normal(N) + 1j * rng.standard_normal(N)
        u /= np.linalg.norm(u)
        w = rng.standard_normal(N) + 1j * rng.standard_normal(N)
        Q = -2j * (np.outer(u, w.conj()) - np.outer(w, u.conj()))
        Q = (Q + Q.conj().T) / 2
        al = np.vdot(u, w)
        av, rv = al.imag, float(np.vdot(w, w).real - abs(al) ** 2)
        ev = np.linalg.eigvalsh(Q)
        nz = ev[np.abs(ev) > 1e-12 * max(1.0, np.abs(ev).max())]
        for p in (1, 2, 3, 4):
            got = float(np.sum(nz ** (2 * p)))
            f = sum(comb(2 * p, 2 * j) * 2 ** (2 * p + 1) * av ** (2 * p - 2 * j)
                    * (av * av + rv) ** j for j in range(p + 1))
            maxdev = max(maxdev, abs(got - f) / max(1.0, abs(got)))
    assert maxdev < 1e-10, maxdev
    print(f"PART1 spectrum polynomials: even symbolic p=1..6 and odd symbolic p=0..4 "
          f"exact (j-independent 2^(2p+1) / 2^(2p+2)); numeric max rel dev = {maxdev:.3e}")
    mu, Vv = [2, 3], Fraction(7, 3)
    for p in range(1, 5):
        cf, gt = closed_form(p, mu, Vv), ground_truth(p, mu, Vv)
        assert sp.simplify(cf - gt) == 0, (p, cf, gt)
    print("PART2 Wick closed form vs exact bivariate integration, mu=(2,3) V=7/3 "
          "p=1..4: exact equality (sympy, deviation 0)")
    for p in (1, 2, 3):
        poly = sp.expand(tr_odd_exact(p))
        assert sp.expand(poly + poly.subs(a, -a)) == 0
    s1sum, s2sum, nmc = 0.0, 0.0, 60000
    for _ in range(nmc):
        aa = np.sqrt(7.0 / 3.0) * rng.standard_normal()
        rr = 2.0 * rng.exponential() + 3.0 * rng.exponential()
        f = lambda x, q=rr: -sum(comb(3, 2 * j) * 2 ** 4 * x ** (3 - 2 * j)
                                  * (x * x + q) ** j for j in range(2))
        tr1 = f(aa)
        s1sum += tr1 + f(-aa)
        s2sum += abs(tr1)
    print("PART3 odd moments: exact antisymmetry in a for p=1,2,3; a-reflected "
          f"pair sum of Tr Q^3 = {s1sum / nmc:.3e} (expected 0 to roundoff) "
          f"against E|Tr Q^3| = {s2sum / nmc:.3f}")
    print("PASS s1")


if __name__ == '__main__':
    main()
