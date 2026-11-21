"""081-088 r2, v1: single-cap charge moments and the profile factor rho_p.

Checks (exact unless stated):
 A  roots of lam^2+4a lam-4r are -2a +- 2(a^2+r)^(1/2) (Row length pair);
 B  Tr Q^m = (-1)^m 2^(m+1) sum_k C(m,2k) sum_j C(k,j) a^(m-2k+2j) r^(k-j), m=1..12;
 C  a -> -a sends every odd power sum to minus itself (sign flip of the momenta);
 D  at a=0: even power sums 2(4r)^p = 2 l^(2p), l = 2 r^(1/2); odd ones vanish;
 E  E[(sum g_i E_i)^p] = p! h_p(g) for unit exponentials (MGF prod (1-g_i t)^-1), D=3 symbolic, p<=5;
 F  partition form p! h_p / W^p = sum_lambda (p!/z_lambda) prod (s_k/W^k)^m_k, symbolic D=3, p<=6;
 G  rho_2 - 1 = s_2/W^2 = 1/D_eff (symbolic);
 H  rho_p - 1 >= C(p,2)/D_eff and rho_p <= p! (single row equality), exact rationals, 2000 profiles;
 I  pair identity behind the sharp bound rho_p >= prod_{k<p}(1+k/D), symbolic p=2..7, |Z|=2;
    uniform value p! h_p(1/D..)=prod_{k<p}(D+k)/D^p; bound + strictness on 2000 exact profiles;
 J  Monte Carlo sanity of <Tr Q^4> = 2*16*s^4*2 h_2 at a=0 (numerical).
Run: python -I proposals/local-gpu/081-088-r2/v1_moment_map.py   Last line: PASS v1
"""
import random
from fractions import Fraction
from math import comb, factorial, prod

import numpy as np
import sympy as sp

a, r, lam, t = sp.symbols('a r lam t')
ok = True

# A
roots = sp.solve(sp.Eq(lam**2 + 4*a*lam - 4*r, 0), lam)
exp_roots = {-2*a + 2*sp.sqrt(a**2 + r), -2*a - 2*sp.sqrt(a**2 + r)}
A = {sp.simplify(x) for x in roots} == {sp.simplify(x) for x in exp_roots}
print('A roots = Row length pair:', A); ok &= A

# B, C, D
lp, lm = -2*a + 2*sp.sqrt(a**2 + r), -2*a - 2*sp.sqrt(a**2 + r)
Bok = Cok = Dok = True
for m in range(1, 13):
    ps = sp.expand(lp**m + lm**m)
    form = (-1)**m * 2**(m + 1) * sum(comb(m, 2*k) * sum(comb(k, j) * a**(m - 2*k + 2*j) * r**(k - j)
                                                          for j in range(k + 1)) for k in range(m // 2 + 1))
    Bok &= sp.simplify(ps - form) == 0
    if m % 2:
        Cok &= sp.simplify(form.subs(a, -a) + form) == 0
        Dok &= form.subs(a, 0) == 0
    else:
        Dok &= sp.simplify(form.subs(a, 0) - 2*(4*r)**(m // 2)) == 0
print('B power-sum formula m=1..12:', Bok, '| C odd under a->-a:', Cok, '| D a=0 moments 2 l^2p:', Dok)
ok &= Bok and Cok and Dok

# E, F, G
g = sp.symbols('g1:4', positive=True)
W = sum(g)
mgf = sp.prod([1/(1 - gi*t) for gi in g])
ser = sp.series(mgf, t, 0, 7).removeO()


def h(p, xs):
    return sum(sp.prod(c) for c in sp.utilities.iterables.combinations_with_replacement(xs, p))


Eok = True
for p in range(1, 6):
    Eok &= sp.expand(ser.coeff(t, p) - h(p, g)) == 0
print('E E r^p = p! h_p (MGF coefficient = h_p), p<=5:', Eok); ok &= Eok


def partitions(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield []
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield [k] + rest


Fok = True
pk = {k: sum(gi**k for gi in g) for k in range(1, 7)}
for p in range(1, 7):
    tot = 0
    for lamb in partitions(p):
        mult = {k: lamb.count(k) for k in set(lamb)}
        z = prod(k**mk * factorial(mk) for k, mk in mult.items())
        tot += sp.Rational(factorial(p), z) * sp.prod([(pk[k] / W**k)**mk for k, mk in mult.items()])
    Fok &= sp.simplify(tot - factorial(p) * h(p, g) / W**p) == 0
print('F partition form p<=6:', Fok); ok &= Fok
Gok = sp.simplify(2*h(2, g)/W**2 - 1 - pk[2]/W**2) == 0
print('G rho_2 - 1 = 1/D_eff:', Gok); ok &= Gok


# H, I numerics (exact rationals)
def hF(p, xs):
    pw = [sum(x**k for x in xs) for k in range(p + 1)]
    hh = [Fraction(1)]
    for n in range(1, p + 1):
        hh.append(sum(pw[k] * hh[n - k] for k in range(1, n + 1)) / n)
    return hh[p]


def rho(p, xs):
    return factorial(p) * hF(p, xs) / sum(xs)**p


random.seed(881)
viol_H = viol_I = strict_fail = 0
for _ in range(2000):
    D = random.randint(1, 7)
    xs = [Fraction(random.randint(0, 9), random.randint(1, 5)) for _ in range(D)]
    if sum(xs) == 0:
        continue
    Wx = sum(xs); deff = Wx**2 / sum(x*x for x in xs)
    for p in range(2, 7):
        rp = rho(p, xs)
        if rp - 1 < Fraction(comb(p, 2)) / deff or rp > factorial(p):
            viol_H += 1
        lb = prod(1 + Fraction(k, D) for k in range(1, p))
        if rp < lb:
            viol_I += 1
        if rp == lb and len(set(xs)) > 1:
            strict_fail += 1
single = all(rho(p, [Fraction(0), Fraction(3), Fraction(0)]) == factorial(p) for p in range(2, 7))
print('H violations:', viol_H, '| single row rho_p = p!:', single)
ok &= viol_H == 0 and single
uni = all(factorial(p) * hF(p, [Fraction(1, D)] * D) == Fraction(prod(D + k for k in range(p)), D**p)
          for D in range(1, 9) for p in range(1, 7))
print('I uniform value:', uni, '| bound violations:', viol_I, '| equality off uniform:', strict_fail)
ok &= uni and viol_I == 0 and strict_fail == 0

x, y = sp.symbols('x y', nonnegative=True)
Z = sp.symbols('z1:3', nonnegative=True)
pair_ok = True
for p in range(2, 8):
    hp = h(p, (x, y) + Z)
    lhs = sp.expand((x - y) * (sp.diff(hp, x) - sp.diff(hp, y)))
    rhs = (x - y)**2 * sum((m - aa) * h(p - 1 - m - aa, Z) * x**aa * y**aa *
                           sum(x**(m - aa - 1 - tt) * y**tt for tt in range(m - aa))
                           for m in range(1, p) for aa in range(0, min(m - 1, p - 1 - m) + 1))
    pair_ok &= sp.expand(lhs - rhs) == 0
print('I pair identity p=2..7:', pair_ok); ok &= pair_ok

# J
rng = np.random.default_rng(88)
gg = np.array([1.0, 2.0, 0.5, 3.0]); s2 = 0.7
Ev = rng.exponential(size=(400000, 4))
rr = s2 * (Ev * gg).sum(1)
mc = np.mean(2 * (4 * rr)**2)
ex = 2 * 16 * s2**2 * 2 * float(hF(2, [Fraction(v) for v in [1, 2, 1/2, 3]]))
print('J MC <Tr Q^4> at a=0: %.4f vs exact %.4f (rel %.1e)' % (mc, ex, abs(mc/ex - 1)))
ok &= abs(mc/ex - 1) < 1e-2
print('PASS v1' if ok else 'FAIL v1')
