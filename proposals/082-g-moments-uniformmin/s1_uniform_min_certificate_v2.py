"""082 s1 v2: symbolic certificates for the uniform-minimiser lemma.

Supersedes s1_uniform_min_certificate.py (kept as lineage): that script's
assertion compared the quotient P against (x-y)^2 times the claimed sum
(wrong scale) and summed a beyond a <= p-1-m, so hp(Z, negative) silently
returned 1; its closedform assert failed at D=3,p=2. v2 caps a at
min(m-1, p-1-m) and compares P to the sum directly.

Lemma (proved in proposal-r1.md). For mu = (mu_1,...,mu_D), mu_i >= 0,
S1 = sum mu_i > 0, integer p >= 1, rho_p(mu) = p! h_p(mu)/S1^p, with h_p the
complete homogeneous symmetric polynomial:
    rho_p(mu) >= prod_{k=1}^{p-1}(1 + k/D),
equality iff all mu_i are equal (for p >= 2; p = 1 gives equality always,
D = 1 gives both sides = p!). Certificates:
 (A) pair Schur quotient: (x-y)(dh_p/dx - dh_p/dy) is divisible by (x-y)^2
     and the quotient has all coefficients >= 0 (exact scan), p=2..6, D=3,4.
 (B) closed form of the quotient P = sum_{m=1}^{p-1} sum_{a=0}^{min(m-1,p-1-m)}
     (m-a) h_{p-1-m-a}(Z) x^a y^a sum_{t=0}^{m-a-1} x^{m-a-1-t} y^t, exact.
 (C) derivative generating identity: dh_p/dx = sum_{m=0}^{p-1}(m+1) x^m
     h_{p-1-m}^{(x)}, exact, p=2..6, D=3.
 (D) uniform exact value: p! h_p(1/D,...,1/D) = prod_{k=1}^{p-1}(1+k/D),
     p=0..6, D=1,2,3,7,120 (exact rationals).
 (E) D=2 two-slot closed form: h_p(t,1-t) - (p+1)/2^p =
     2^(-p) sum_{r=1..floor(p/2)} C(p+1,2r+1) (2t-1)^(2r), all coeffs > 0,
     p=2..8.
 (F) random exact-rational profiles, both directions: rho_p(g) >= uniform
     value always, equality only for uniform profiles; single-slot rho_p = p!;
     r equal slots + D-r zeros give the r-slot uniform value;
     400 seeded trials D=1..6,p=2..6, plus all D=1..7 boundaries, p=2..6.
 (G) prod_{k=1}^{p-1}(1+k/D) >= 1 + C(p,2)/D exact, D=1..120, p=2..8.
Run: python -I proposals/082-g-moments-uniformmin/s1_uniform_min_certificate_v2.py
Expected invariants: every certificate prints OK; last line 'PASS s1'.
"""
from fractions import Fraction
from math import comb, factorial
import random

import sympy as sp


def hp(vars_, p):
    assert p >= 0
    pw = [sum(v ** t for v in vars_) for t in range(p + 1)]
    h = [sp.Integer(1)]
    for m in range(1, p + 1):
        h.append(sum(pw[t] * h[m - t] for t in range(1, m + 1)) / sp.Integer(m))
    return sp.expand(h[p])


def hp_frac(vals, p):
    assert p >= 0
    pw = [sum(v ** t for v in vals) for t in range(p + 1)]
    h = [Fraction(1)]
    for m in range(1, p + 1):
        h.append(sum(pw[t] * h[m - t] for t in range(1, m + 1)) / m)
    return h[p]


def unif(D, p):
    r = Fraction(1)
    for k in range(1, p):
        r *= 1 + Fraction(k, D)
    return r


def certs_AB():
    x, y = sp.symbols('x y', nonnegative=True)
    for Dn in (3, 4):
        Z = sp.symbols('z1:%d' % (Dn - 1), nonnegative=True)
        for p in range(2, 7):
            V = [x, y] + list(Z)
            Q = sp.expand((x - y) * (sp.diff(hp(V, p), x) - sp.diff(hp(V, p), y)))
            P, rem = sp.div(Q, (x - y) ** 2, x)
            assert rem == 0, ('div', Dn, p)
            assert all(c >= 0 for c in sp.Poly(P, *V).coeffs()), ('coeffs', Dn, p)
            R = sum((m - a) * hp(list(Z), p - 1 - m - a) * x ** a * y ** a
                    * sum(x ** (m - a - 1 - t) * y ** t for t in range(m - a))
                    for m in range(1, p)
                    for a in range(0, min(m - 1, p - 1 - m) + 1))
            assert sp.expand(P - sp.expand(R)) == 0, ('closedform', Dn, p)
    print("(A)+(B) Schur-Ostrowski quotient coeffs >= 0 and closed form P == "
          "sum exact for p=2..6, D=3,4: OK")


def cert_C():
    x, y = sp.symbols('x y', nonnegative=True)
    Z = sp.symbols('z1:2', nonnegative=True)
    for p in range(2, 7):
        lhs = sp.diff(hp([x, y] + list(Z), p), x)
        rhs = sp.expand(sum((m + 1) * x ** m * hp([y] + list(Z), p - 1 - m)
                            for m in range(p)))
        assert sp.expand(lhs - rhs) == 0, p
    print("(C) derivative generating identity exact for p=2..6, D=3: OK")


def cert_D():
    for Dn in (1, 2, 3, 7, 120):
        for p in range(0, 7):
            val = Fraction(factorial(p)) * hp_frac([Fraction(1, Dn)] * Dn, p)
            assert val == unif(Dn, p), (Dn, p)
    print("(D) uniform p! h_p = prod(1+k/D) exact, p=0..6, D=1,2,3,7,120: OK")


def cert_E():
    s = sp.symbols('s')
    for p in range(2, 9):
        diff_s = sp.expand(hp([(s + 1) / 2, (1 - s) / 2], p)
                           - sp.Rational(p + 1, 2 ** p))
        cf_s = sp.expand(sum(sp.Rational(1, 2 ** p) * comb(p + 1, 2 * r + 1)
                             * s ** (2 * r) for r in range(1, p // 2 + 1)))
        assert sp.expand(diff_s - cf_s) == 0, ('E-closedform', p)
        poly = sp.Poly(diff_s, s)
        for monom, c in zip(poly.monoms(), poly.coeffs()):
            assert monom[0] % 2 == 0 and monom[0] >= 2 and c > 0, ('E-pos', p, monom)
        assert len(poly.monoms()) == p // 2, ('E-nmono', p)
    print("(E) D=2 closed form h_p(t,1-t)-(p+1)/2^p = 2^(-p) sum C(p+1,2r+1)"
          "(2t-1)^(2r), coeffs > 0, p=2..8: OK")


def cert_F():
    rng = random.Random(20261118)
    bad = 0
    for _ in range(400):
        Dn = rng.randint(1, 6)
        vals = [Fraction(rng.randint(0, 20), rng.randint(1, 10)) for _ in range(Dn)]
        if sum(vals) <= 0:
            vals[0] = Fraction(1)
        p = rng.randint(2, 6)
        W = sum(vals)
        rho = Fraction(factorial(p)) * hp_frac(vals, p) / W ** p
        lo = unif(Dn, p)
        if rho < lo or (rho == lo and len(set(vals)) != 1):
            bad += 1
    assert bad == 0, ('F violations', bad)
    for Dn in range(1, 8):
        for p in range(2, 7):
            single = [Fraction(1)] + [Fraction(0)] * (Dn - 1)
            assert Fraction(factorial(p)) * hp_frac(single, p) == factorial(p)
            for r in range(1, Dn + 1):
                v = [Fraction(1, r)] * r + [Fraction(0)] * (Dn - r)
                assert Fraction(factorial(p)) * hp_frac(v, p) == unif(r, p), (Dn, r, p)
    print("(F) 400 seeded exact-rational profiles D=1..6,p=2..6 both directions "
          "OK; single-slot rho_p=p!; r equal slots + zeros = r-slot uniform: OK")


def cert_G():
    for Dn in range(1, 121):
        for p in range(2, 9):
            assert unif(Dn, p) >= 1 + Fraction(p * (p - 1), 2 * Dn), (Dn, p)
    print("(G) prod(1+k/D) >= 1 + C(p,2)/D exact, D=1..120, p=2..8: OK")


def main():
    certs_AB()
    cert_C()
    cert_D()
    cert_E()
    cert_F()
    cert_G()
    print('PASS s1')


if __name__ == '__main__':
    main()
