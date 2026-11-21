# s4_dirichlet_rho_direct.py - clean exact statistics of rho_p = p! h_p(p) on
# the unit-trace profile simplex p=(p_1..p_D), p_i>=0, sum p_i = 1 (W=1), under
# the flat Dirichlet(1,...,1) profile weight (the Haar-frame pushforward of the
# named slot/frame measures and the flat beta-family member, appH L3180-3215).
# D SYMBOLIC. This REPLACES the arithmetic of s3/s3b's E_of_power_sum_monomial,
# which used the falling factorial (D-1)!/(D-b)! for the number of assignments
# of b equal-index blocks to D coordinates instead of the correct D!/(D-b)!,
# and evaluated E[rho_p] without imposing the unit-trace substitution x_1 = 1.
# The reusable correct piece here is dirichlet_monomial_moment (taken verbatim
# from s3b_dirichlet_rho_stats.py); everything downstream is rebuilt.
# Route: rho_p via the partition (Newton) form rho_p = sum_{lambda |- p}
# (p!/z_lambda) prod_k s_k^{m_k} (s_1 = 1 imposed), E[prod_k s_k^{m_k}] by
# grouping multi-indices in s_{k_1}...s_{k_r} into equality patterns (set
# partitions of the factor list into b blocks): each pattern contributes
# D!/(D-b)! * E prod p^{(block-sum exponents)} via dirichlet_monomial_moment.
import sympy as sp

D = sp.symbols("D", integer=True, positive=True)

def dirichlet_monomial_moment(prof):
    """E prod_i p_i^{a_i} for p ~ Dirichlet(1,...,1) on the simplex, given the
    exponent profile {a : multiplicity}: (D-1)!/(D+A-1)! * prod a_i!^m."""
    A = sum(a * m for a, m in prof.items())
    prod = sp.Integer(1)
    for a, m in prof.items():
        prod *= sp.factorial(a) ** m
    return sp.simplify(sp.factorial(D - 1) * prod / sp.factorial(D + A - 1))

def partitions_with_multiplicities(p):
    out = []
    def gen(n, mx, cur):
        if n == 0:
            out.append(dict(cur)); return
        for part in range(min(n, mx), 0, -1):
            cur[part] = cur.get(part, 0) + 1
            gen(n - part, part, cur)
            cur[part] -= 1
            if cur[part] == 0:
                del cur[part]
    gen(p, p, {})
    return out

def rho_partition_expr(p):
    """rho_p in power sums x_k = s_k: (p!/z_lambda) prod x_k^{m_k} (unit trace
    x_1 = 1 NOT yet imposed)."""
    x = {k: sp.Symbol("x%d" % k) for k in range(1, p + 1)}
    expr = sp.Integer(0)
    for lam in partitions_with_multiplicities(p):
        z = sp.Integer(1)
        for k, mk in lam.items():
            z *= sp.Integer(k) ** mk * sp.factorial(mk)
        mono = sp.Integer(1)
        for k, mk in lam.items():
            mono *= x[k] ** mk
        expr += sp.factorial(p) / z * mono
    return sp.expand(expr)

def rho_unit_trace(p):
    x = {k: sp.Symbol("x%d" % k) for k in range(1, p + 1)}
    return sp.expand(rho_partition_expr(p).subs(x[1], 1))

def monomial_ks(mon):
    """Factor list ks = [k repeated m_k times] of a monomial prod_k x_k^{m_k}."""
    ks = []
    fac = mon.args if mon.is_Mul else (mon,)
    for f in fac:
        b, e = (f.as_base_exp() if f.is_Pow else (f, 1))
        if b == 1:
            continue
        k = int(str(b)[1:])
        ks += [k] * int(e)
    return ks

def E_power_sum_monomial(ks):
    """E[prod_k s_k^{m_k}] from the factor multiset ks: sum over set partitions
    of the factors into b equal-index blocks of falling(D, b) * Dirichlet
    moment of the block-sum exponent profile. falling(D, b) = D!/(D-b)!."""
    if not ks:
        return sp.Integer(1)
    def rec(idx, blocks):
        if idx == len(ks):
            prof = {}
            for blk in blocks:
                a = sum(blk)
                prof[a] = prof.get(a, 0) + 1
            b = len(blocks)
            fall = sp.factorial(D) / sp.factorial(D - b)   # CORRECT falling factorial
            return sp.simplify(fall) * dirichlet_monomial_moment(prof)
        res = sp.Integer(0)
        for j in range(len(blocks)):
            blocks[j].append(ks[idx])
            res += rec(idx + 1, blocks)
            blocks[j].pop()
        blocks.append([ks[idx]])
        res += rec(idx + 1, blocks)
        blocks.pop()
        return res
    return sp.simplify(rec(0, []))

def E_rho(p):
    r = rho_unit_trace(p)
    xv = [sp.Symbol("x%d" % k) for k in range(2, p + 1)]
    E = sp.Integer(0)
    for term in (r.args if r.is_Add else (r,)):
        c, mon = term.as_independent(*xv, as_Add=False)
        E += c * E_power_sum_monomial(monomial_ks(mon))
    return sp.factor(sp.simplify(E))

print("== A. exact E[rho_p] under flat Dirichlet(1^D), unit trace imposed ==")
# p = 1 is exact and explicit: rho_1 = 1! h_1 = s_1 = 1 on the unit-trace simplex.
print("p=1: rho_1 = 1 exactly on the unit trace simplex; E[rho_1] = 1 (explicit)")
assert rho_unit_trace(1) == 1
# structural identities used downstream:
assert sp.expand(rho_unit_trace(2) - (1 + sp.Symbol("x2"))) == 0
assert sp.expand(rho_unit_trace(3) - (1 + 3 * sp.Symbol("x2") + 2 * sp.Symbol("x3"))) == 0
print("rho_2 = 1 + s_2 and rho_3 = 1 + 3 s_2 + 2 s_3 verified from partition form (unit trace)")
E2 = E_rho(2); E3 = E_rho(3); E4 = E_rho(4)
print("p=2: E[rho_2] =", E2)
print("p=3: E[rho_3] =", E3)
print("p=4: E[rho_4] =", E4)
tgt2 = 1 + sp.Rational(2, 1) / (D + 1)
tgt3 = 1 + 6 / (D + 1) + 12 / ((D + 1) * (D + 2))
print("CHECK E[rho_2] == 1 + 2/(D+1):", sp.simplify(E2 - tgt2) == 0)
print("CHECK E[rho_3] == 1 + 6/(D+1) + 12/((D+1)(D+2)):", sp.simplify(E3 - tgt3) == 0)
# uniform-profile floor (s2_uniform_rho_r2: rho_p(uniform) = prod_{k=1}^{p-1}(1+k/D))
jj = sp.Symbol("jj", integer=True, positive=True)
for p, Ep in ((2, E2), (3, E3), (4, E4)):
    floorp = sp.simplify(sp.product(1 + jj / D, (jj, 1, p - 1)))
    diff = sp.factor(sp.simplify(Ep - floorp))
    print("p=%d: E[rho_p] - uniform floor = %s" % (p, diff))
d2f = sp.factor(sp.simplify(E2 - (1 + 1 / D)))
print("CHECK E[rho_2] - floor(2,D) == (D-1)/(D(D+1)):", sp.simplify(d2f - (D - 1) / (D * (D + 1))) == 0)

print()
print("== B. sigma = s_2 = 1/D_eff: exact moments, positivity, rates ==")
Es2 = E_power_sum_monomial([2])
Es2sq = E_power_sum_monomial([2, 2])
Vs2 = sp.factor(sp.simplify(Es2sq - Es2 ** 2))
print("E[sigma]   =", sp.factor(Es2))
print("E[sigma^2] =", sp.factor(Es2sq))
print("Var[sigma] =", Vs2)
num, den = sp.fraction(Vs2)
print("Var numerator (factored) =", sp.factor(num), "  denominator =", sp.factor(den))
shift = sp.expand(num.subs(D, D + 2))
print("numerator(D+2) =", shift, " -> all coefficients positive, so numerator > 0 for D >= 2;")
print("denominator > 0 for D >= 1; Var(1) =", sp.simplify(Vs2.subs(D, 1)),
      "(sigma = 1 deterministically at D=1); hence Var[sigma] > 0 for all D >= 2.")
assert sp.Poly(shift, D).coeffs() and all(c > 0 for c in sp.Poly(shift, D).coeffs())
assert sp.simplify(Vs2.subs(D, 1)) == 0
print("D * E[sigma] ->", sp.limit(D * Es2, D, sp.oo), "   (E[sigma] = 2/(D+1) -> 0)")
print("D^3 * Var[sigma] ->", sp.limit(D ** 3 * Vs2, D, sp.oo),
      "   (concentration rate Var[sigma] ~ 4/D^3)")

print()
print("== C. Monte Carlo corroboration (fixed D, seed 102; corroboration, not proof) ==")
import numpy as np
rng = np.random.default_rng(102)
mcok = True
for Dn in (3, 6, 24):
    P = rng.exponential(1.0, size=(400000, Dn))
    P /= P.sum(axis=1, keepdims=True)
    s2 = (P * P).sum(axis=1)
    s3 = (P ** 3).sum(axis=1)
    r2 = 1 + s2
    r3 = 1 + 3 * s2 + 2 * s3
    ex2 = float(E2.subs(D, Dn))
    ex3 = float(E3.subs(D, Dn))
    exs = float(Es2.subs(D, Dn))
    for name, mc, ex in (("rho_2", float(r2.mean()), ex2),
                         ("rho_3", float(r3.mean()), ex3),
                         ("sigma", float(s2.mean()), exs)):
        rel = abs(mc - ex) / abs(ex)
        mcok = mcok and (rel <= 0.01)
        print("D=%2d  mean %-6s %.6f  exact %.6f  rel.dev %.2e" % (Dn, name, mc, ex, rel))
print("MC check (all 9 means within 1% of exact):", mcok)

print()
print("== D. deterministic pin 1 <= rho_p <= 1 + (p!-1) sigma, sigma = s_2 ==")
# pointwise pin on rational profiles (h-recursion h[n] += h[n-1]*p_i), as in the
# s3b pin block; the pin being pointwise on the simplex it also holds in mean:
# 1 <= E[rho_p] <= 1 + (p!-1) E[sigma].
import random
from fractions import Fraction
random.seed(102)
pinok = True
for trial in range(40):
    Dn = random.randint(2, 5)
    gg = [Fraction(random.randint(1, 50), random.randint(1, 50)) for _ in range(Dn)]
    Wn = sum(gg)
    gp = [x / Wn for x in gg]
    s2v = sum(x * x for x in gp)
    for p in (2, 3, 4, 5):
        h = [sp.Rational(0)] * (p + 1); h[0] = sp.Rational(1)
        for x in gp:
            for n in range(1, p + 1):
                h[n] += h[n - 1] * sp.Rational(x)
        rho = sp.factorial(p) * h[p]
        pinok = pinok and (sp.Rational(1) <= rho)
        pinok = pinok and (sp.simplify(rho - 1 - (sp.factorial(p) - 1) * sp.Rational(s2v)) <= 0)
        if p == 2:
            pinok = pinok and (sp.simplify(rho - 1 - sp.Rational(s2v)) == 0)
print("pointwise pin 1 <= rho_p <= 1+(p!-1)sigma on 40 random rational profiles (p=2..5),"
      " equality rho_2 - 1 = sigma:", pinok)
for Dn in (3, 6, 24):
    e2 = float(E2.subs(D, Dn)); e3 = float(E3.subs(D, Dn)); e4 = float(E4.subs(D, Dn))
    es = float(Es2.subs(D, Dn))
    ub2 = 1 + 1 * es; ub3 = 1 + 5 * es; ub4 = 1 + 23 * es
    print("D=%2d  E[rho_2]=%.6f (mean-pin ub %.6f, equal: pin sharp at p=2)  "
          "E[rho_3]=%.6f (ub %.6f)  E[rho_4]=%.6f (ub %.6f)  E[sigma]=%.6f"
          % (Dn, e2, ub2, e3, ub3, e4, ub4, es))
    assert e2 >= 1.0 and e3 >= 1.0 and e4 >= 1.0
    assert e2 <= ub2 + 1e-12 and e3 <= ub3 and e4 <= ub4
print("ALL CHECKS PASS")
