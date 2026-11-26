# s3b_dirichlet_rho_stats.py - rerun of s3_dirichlet_rho_stats.py (proposal 102)
# with ONE script-level defect fixed: line 61-62 of s3 bound fac = mon (a sympy
# Mul) and iterated it; the installed sympy raises TypeError: 'Mul' object is
# not iterable. Fix: iterate mon.args. Every other definition is kept EXACTLY
# as in s3, including the slot-counting factor factorial(D-1)/factorial(D-b) in
# E_of_power_sum_monomial (NOT changed; see findings.md OPEN-1 for the gatekeeper).
# Original docstring (verbatim intent):
# s3_dirichlet_rho_stats.py - exact statistics of the moment-map obstruction
# factor rho_p = p! h_p(p) (unit-trace profile p on the simplex, W = 1) under
# the flat Dirichlet(1,...,1) profile weight - the Haar-frame pushforward of
# the named slot/frame measures (appH L3191) and the flat beta-family member
# (appH L3193) - with D SYMBOLIC, via the integrated partition form
# rho_p = sum_{lambda |- p} (p!/z_lambda) prod_k s_k^{m_k}  (appH L3177).
# Checks: (I) exact E[rho_p], p=1..5, closed form in D; (II) exact E[sigma],
# E[sigma^2], Var[sigma] for sigma = s_2 = 1/D_eff, and the D^-3 rate of Var;
# (III) E[rho_2] - floor(2,D) = (D-1)/(D(D+1)) exact; (IV) deterministic pin
# 1 <= rho_p <= 1 + (p!-1) sigma on random rational profiles, with equality
# for rho_2 - 1 = sigma (pin constant sharp at p=2); (V) Monte Carlo
# corroboration at fixed D (corroboration, not proof).
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
    """rho_p in power sums x_k = s_k (unit trace): (p!/z_lambda) prod x_k^{m_k}."""
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

def E_of_power_sum_monomial(mon, pmax):
    """E[prod_k s_k^{m_k}] for a monomial in x1..x_{pmax}: expand the product
    of power sums by set partitions of the factor list into slot blocks
    (blocks in first-appearance order, counted once), each b-block partition
    contributing the falling factorial D_(b) times the Dirichlet moment of
    the block-sum exponent profile."""
    ks = []
    fac = mon.args if mon.is_Mul else (mon,)   # FIX: iterate Mul args (was `fac = mon`)
    for f in fac:
        b, e = (f.as_base_exp() if f.is_Pow else (f, 1))
        if b == 1:
            continue
        k = int(str(b)[1:])
        ks += [k] * int(e)
    if not ks:
        return sp.Integer(1)
    total = sp.Integer(0)
    def rec(idx, blocks):
        if idx == len(ks):
            prof = {}
            for blk in blocks:
                a = sum(blk)
                prof[a] = prof.get(a, 0) + 1
            b = len(blocks)
            fall = sp.factorial(D - 1) / sp.factorial(D - b)
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

xs = lambda p: [sp.Symbol("x%d" % k) for k in range(1, p + 1)]

print("== exact E[rho_p] under flat Dirichlet(1^D), D symbolic ==")
for p in range(1, 6):
    rp = rho_partition_expr(p)
    E = sp.Integer(0)
    for term in (rp.args if rp.is_Add else (rp,)):
        c, mon = term.as_independent(*xs(p), as_Add=False)
        E += c * E_of_power_sum_monomial(mon, p)
    E = sp.factor(sp.simplify(E))
    jj = sp.Symbol("jj", integer=True, positive=True)
    floorp = sp.simplify(sp.product(1 + jj / D, (jj, 1, p - 1))) if p > 1 else sp.Integer(1)
    print("p=%d: E[rho_p] = %s   (fixed-D uniform floor = %s)" % (p, E, floorp))

print()
print("== sigma = s_2 = 1/D_eff: exact moments and rates ==")
x2 = sp.Symbol("x2")
Es2 = E_of_power_sum_monomial(x2, 2)
Es2sq = E_of_power_sum_monomial(x2 ** 2, 2)
Vs2 = sp.factor(sp.simplify(Es2sq - Es2 ** 2))
print("E[sigma]   =", Es2)
print("E[sigma^2] =", sp.factor(Es2sq))
print("Var[sigma] =", Vs2)
print("D^3 * Var[sigma] ->", sp.limit(D ** 3 * Vs2, D, sp.oo), "as D -> oo")
print("D * E[sigma] ->", sp.limit(D * Es2, D, sp.oo), "  (concentration: sigma -> 0 in L2, rate 1/sqrt(D^3))")
print("E[rho_2] - floor(2,D) =", sp.factor(sp.simplify(1 + Es2 - (1 + 1 / D))))

print()
print("== deterministic pin 1 <= rho_p - 1 <= (p!-1)*sigma, sigma = s_2 (unit trace) ==")
import random
from fractions import Fraction
random.seed(102)
pinok = True
for trial in range(40):
    Dn = random.randint(2, 5)
    gg = [Fraction(random.randint(1, 50), random.randint(1, 50)) for _ in range(Dn)]
    Wn = sum(gg)
    gp = [x / Wn for x in gg]
    s2 = sum(x * x for x in gp)
    for p in (2, 3, 4, 5):
        hp = sp.Rational(0)
        # complete homogeneous h_p via generating product (exact rationals)
        h = [sp.Rational(0)] * (p + 1); h[0] = sp.Rational(1)
        for x in gp:
            for n in range(1, p + 1):
                h[n] += h[n - 1] * sp.Rational(x)
        rho = sp.factorial(p) * h[p]
        lhs = sp.Rational(1) <= rho
        rhs = sp.simplify(rho - 1 - (sp.factorial(p) - 1) * sp.Rational(s2)) <= 0
        pinok = pinok and lhs and rhs
        if p == 2:
            eq2 = sp.simplify(rho - 1 - sp.Rational(s2)) == 0
            pinok = pinok and eq2
print("pin 1 <= rho_p <= 1+(p!-1)/D_eff on 40 random rational profiles (p=2..5), "
      "equality rho_2-1 = 1/D_eff:", pinok)

print()
print("== Monte Carlo corroboration (fixed D; corroboration, not proof) ==")
import numpy as np
rng = np.random.default_rng(102)
for Dn in (3, 6, 24):
    P = rng.exponential(1.0, size=(400000, Dn))
    P /= P.sum(axis=1, keepdims=True)
    s2 = (P * P).sum(axis=1)
    s3 = (P ** 3).sum(axis=1)
    r2 = 1 + s2
    r3 = 1 + 3 * s2 + 2 * s3
    ex2 = sp.Rational(Dn + 3, Dn + 1)
    # FIX 2 (echoed by the dead finisher agent, applied verbatim as byte
    # surgery by the orchestrator; gatekeeper to re-derive): s3 passed the Add
    # 1+3*x2+2*x3 to the monomial-only E_of_power_sum_monomial (ValueError;
    # s3 crashed earlier so this was never reached). Same quantity by linearity
    # of E over the sum rho_3 = 1 + 3*s_2 + 2*s_3, term by term.
    x3 = sp.Symbol("x3")
    ex3 = sp.simplify(sp.Integer(1) + 3 * E_of_power_sum_monomial(x2, 3)
                      + 2 * E_of_power_sum_monomial(x3, 3)).subs(D, Dn)
    print("D=%d: mean rho_2 %.6f (exact %s=%.6f) | mean rho_3 %.6f (exact %s) | mean sigma %.6f (exact %s)"
          % (Dn, r2.mean(), ex2, float(ex2), r3.mean(), ex3, s2.mean(), float(sp.Rational(2, Dn + 1))))
