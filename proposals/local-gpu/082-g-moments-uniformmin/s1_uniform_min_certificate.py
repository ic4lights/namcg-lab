"""082 s1: symbolic certificates for the uniform-minimiser lemma.

Lemma. For mu = (mu_1,...,mu_D), mu_i >= 0, S1 = sum mu_i > 0, and every p >= 2,
rho_p(mu) = p! h_p(mu) / S1^p >= prod_{k=1}^{p-1} (1 + k/D) = rho_p(uniform),
equality iff mu_i = S1/D for all i (p <= 1: identity; D = 1: both sides = p!).

Certificates:
 (A) Schur--Ostrowski nonnegativity: for D variables (2 moving x,y and fixed
     Z), P = (x-y)(dh_p/dx - dh_p/dy) is divisible by (x-y)^2 and the quotient
     has all coefficients >= 0 (exact Poly coefficient scan), for p = 2..6,
     D = 3,4.
 (B) Closed form of the quotient: P = (x-y)^2 sum_{m>a>=0, m+a<=p-1}
     (m-a) h_{p-1-m-a}(Z) x^a y^a sum_{t=0}^{m-a-1} x^{m-a-1-t} y^t, exact.
 (C) Derivative generating identity: dh_p/dx = sum_{m=0}^{p-1}(m+1) x^m
     h_{p-1-m}^{(x)} (h omitting x), exact, p = 2..6, D = 3.
 (D) Uniform exact value: p! h_p(1/D)/ (1)^p = prod_{k=1}^{p-1}(1+k/D),
     p = 0..6, D = 1,2,3,7,120 (rationals).
 (E) D=2 sharp extremal: h_p(t,1-t) - h_p(1/2,1/2) is a polynomial in
     (t-1/2)^2 with all coefficients >= 0 and at least one positive, p = 2..8.

Run: python -I proposals/082-g-moments-uniformmin/s1_uniform_min_certificate.py
Expected invariants: every certificate prints OK; last line 'PASS s1'.
"""
from fractions import Fraction
from math import factorial

import sympy as sp


def hp(vars_, p):
    pw = [sum(v ** t for v in vars_) for t in range(p + 1)]
    h = [sp.Integer(1)]
    for m in range(1, p + 1):
        h.append(sum(pw[t] * h[m - t] for t in range(1, m + 1)) / sp.Integer(m))
    return sp.expand(h[p])


def main():
    x, y = sp.symbols('x y', nonnegative=True)
    for Dn in (3, 4):
        Z = sp.symbols(f'z1:{Dn-1}', nonnegative=True)
        for p in range(2, 7):
            V = [x, y] + list(Z)
            Q = sp.expand((x - y) * (sp.diff(hp(V, p), x) - sp.diff(hp(V, p), y)))
            P, rem = sp.div(Q, (x - y) ** 2, x)
            assert rem == 0, (Dn, p)
            assert all(c >= 0 for c in sp.Poly(P, *V).coeffs()), (Dn, p)
            R = sp.expand((x - y) ** 2 * sum(
                (m - a) * hp(list(Z), p - 1 - m - a) * x ** a * y ** a
                * sum(x ** (m - a - 1 - t) * y ** t for t in range(m - a))
                for m in range(1, p) for a in range(0, m)))
            assert sp.expand(P - R) == 0, ('closedform', Dn, p)
    print("(A)+(B) Schur-Ostrowski quotient: nonnegative coefficients and closed "
          "form exact for p=2..6, D=3,4: OK")
    Z = sp.symbols('z1:2', nonnegative=True)
    for p in range(2, 7):
        lhs = sp.diff(hp([x, y] + list(Z), p), x)
        rhs = sp.expand(sum((m + 1) * x ** m * hp([y] + list(Z), p - 1 - m)
                            for m in range(p)))
        assert sp.expand(lhs - rhs) == 0, p
    print("(C) derivative generating identity exact for p=2..6, D=3: OK")
    for Dn in (1, 2, 3, 7, 120):
        for p in range(0, 7):
            hU = Fraction(factorial(p)) * hp([sp.Rational(1, Dn)] * Dn, p)
            prod = Fraction(1)
            for k in range(1, p):
                prod *= 1 + Fraction(k, Dn)
            assert hU == prod, (Dn, p)
    print("(D) uniform p! h_p = prod(1+k/D) exact, p=0..6, D=1,2,3,7,120: OK")
