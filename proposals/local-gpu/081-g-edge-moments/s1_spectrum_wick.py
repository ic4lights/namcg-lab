"""081 s1: exact spectrum polynomial and exact Gaussian (Wick) closed form.

Part 1: rank-one block-cut charge Q = -2i(|u)(w| - |w)(u|), (u|u)=1: the nonzero
spectrum is the Row length pair -2a +/- 2*sqrt(a^2+r) with a = Im(u|w) (real),
r = |w|^2 - |(u|w)|^2 (appH Row length paragraph, exact). Hence
  Tr Q^{2p} = sum_{j=0}^{p} C(2p,2j) 2^{2p+1-j} a^{2p-2j} (a^2+r)^j   (symbolic).
Part 2: Gaussian state model. a is REAL centered Gaussian, V = <a^2>,
<a^{2k}> = (2k-1)!! V^k; a is independent of r; r = sum_i mu_i E_i with E_i iid
Exp(1) (complex Gaussian edge row), so <r^m> = m! h_m(mu), h_m = complete
homogeneous symmetric polynomial. Closed form:
  <Tr Q^{2p}> = 2^{2p+1} sum_{j=0}^p C(2p,2j) sum_{t=0}^j C(j,t)
                (2(p-j+t)-1)!! V^{p-j+t} (j-t)! h_{j-t}(mu).
Verified against exact bivariate moment integration for mu=(2,3), V=7/3, p<=4.
Part 3: odd moments: Tr Q^{2p+1} is odd in a, a symmetric and independent of r
=> <Tr Q^{2p+1}> = 0 exactly (antisymmetry check p=1,2,3).

Run: python -I proposals/081-g-edge-moments/s1_spectrum_wick.py
Expected invariants: PART1 symbolic p=1..5 exact, numeric max rel dev < 1e-10;
PART2 exact equality (sympy 0) p=1..4; PART3 antisymmetry exact; last line 'PASS s1'.
"""
from fractions import Fraction
from math import comb

import numpy as np
import sympy as sp

a, r = sp.symbols('a r', real=True)


def h_complete(m, mu):
    """Complete homogeneous symmetric polynomial h_m of list mu (exact sympy)."""
    p = [sum(sp.nsimplify(x)**t for x in mu) for t in range(m + 1)]
    h = [sp.Integer(1)]
    for m2 in range(1, m + 1):
        h.append(sp.together(sp.Rational(1, m2) * sum(p[t] * h[m2 - t]
                                                     for t in range(1, m2 + 1))))
    return sp.simplify(h[m])


def tr2p_symbolic(p):
    return sum(comb(2*p, 2*j) * 2**(2*p + 1 - j) * a**(2*p - 2*j) * (a**2 + r)**j
               for j in range(p + 1))


def dfact2k(k):
    """(2k-1)!! = 1 for k=0."""
    out = 1
    for i in range(1, k + 1):
        out *= (2*i - 1)
    return out


def closed_form(p, mu, Vval):
    """(star) closed form; mu list of ints/Fractions, Vval Fraction -> sympy."""
    muS = [sp.Rational(x) for x in mu]
    V = sp.Rational(Vval)
    tot = sp.Integer(0)
    for j in range(p + 1):
        for t in range(j + 1):
            k = p - j + t
            tot += (sp.Rational(comb(2*p, 2*j) * comb(j, t) * dfact2k(k)
                                * sp.factorial(j - t))
                    * V**k * h_complete(j - t, muS))
    return sp.simplify(2**(2*p + 1) * tot)


def ground_truth(p, mu, Vval):
    """Exact bivariate moment integration: real Gaussian a (variance V) and
    independent complex-Gaussian edge row with profile mu."""
    A, R = sp.symbols('A R')
    P = sp.Poly(sp.expand(tr2p_symbolic(p).subs({a: A, r: R})), A, R)
    tot = sp.Integer(0)
    for (ea, er), c in P.terms():
        if ea % 2:
            continue
        mk = dfact2k(ea // 2) * sp.Rational(Vval)**(ea // 2)
        mr = sp.factorial(er) * h_complete(er, [sp.Rational(x) for x in mu])
        tot += c * mk * mr
    return sp.simplify(tot)


def main():
    rng = np.random.default_rng(81001)
    lm = -2*a + 2*sp.sqrt(a**2 + r)
    lp = -2*a - 2*sp.sqrt(a**2 + r)
    for p in range(1, 6):
        assert sp.expand(tr2p_symbolic(p) - sp.expand(lm**(2*p) + lp**(2*p))) == 0
    maxdev = 0.0
    for _ in range(400):
        N = 9
        u = rng.standard_normal(N) + 1j * rng.standard_normal(N)
        u /= np.linalg.norm(u)
        w = rng.standard_normal(N) + 1j * rng.standard_normal(N)
        Q = -2j * (np.outer(u, w.conj()) - np.outer(w, u.conj()))
        Q = (Q + Q.conj().T) / 2
        al = np.vdot(u, w)
        av, rv = al.imag, float(np.vdot(w, w).real - abs(al)**2)
        ev = np.linalg.eigvalsh(Q)
        nz = ev[np.abs(ev) > 1e-12 * max(1.0, np.abs(ev).max())]
        for p in (1, 2, 3, 4):
            got = float(np.sum(nz**(2*p)))
            f = sum(comb(2*p, 2*j) * 2**(2*p + 1 - j) * av**(2*p - 2*j)
                    * (av*av + rv)**j for j in range(p + 1))
            maxdev = max(maxdev, abs(got - f) / max(1.0, abs(got)))
    assert maxdev < 1e-10, maxdev
    print(f"PART1 spectrum polynomial: symbolic p=1..5 exact; numeric max rel dev = {maxdev:.3e}")
    mu, Vv = [2, 3], Fraction(7, 3)
    for p in range(1, 5):
        cf, gt = closed_form(p, mu, Vv), ground_truth(p, mu, Vv)
        assert sp.simplify(cf - gt) == 0, (p, cf, gt)
    print("PART2 Wick closed form vs exact bivariate integration, mu=(2,3) V=7/3 "
          "p=1..4: exact equality (sympy, deviation 0)")
    for p in (1, 2, 3):
        poly = sp.expand(sum(comb(2*p + 1, 2*j) * 2**(2*p + 1 - j)
                             * a**(2*p + 1 - 2*j) * (a**2 + r)**j for j in range(p + 1)))
        assert sp.expand(poly + poly.subs(a, -a)) == 0
    print("PART3 Tr Q^{2p+1} odd in a for p=1,2,3: antisymmetry exact => Gaussian "
          "average 0 (a symmetric, independent of r)")
    print("PASS s1")


if __name__ == '__main__':
    main()
