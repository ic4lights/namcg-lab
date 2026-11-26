# s1_naive_associator.py -- proposal 105 r1, step 1.
# Exact symbolic computation (sympy, rational arithmetic) of the order-Theta^2
# associator of the NAIVE variable-coefficient Moyal truncation on R^4:
#   f *_naive g := f g + (i/2) Theta^{ab}(x) d_a f d_b g ,
#   A2(f,g,h) := (f *_naive g) *_naive h - f *_naive (g *_naive h)  at order 2
#              = B1(B1(f,g),h) - B1(f,B1(g,h)),  B1(p,q)=(i/2) Theta^{ab} d_a p d_b q,
# evaluated as a polynomial at x=0 in the 1- and 2-jets at 0 of polynomial test
# functions f,g,h of degree <=2 (all jets independent), with coefficients
# polynomial in the 2-jets at 0 of generic Theta^{ab}(x).
# Output checks:
#  (a) the (1,1,1) part of the associator is proportional to the Schouten
#      bracket [Theta,Theta]^{abc} d_a f d_b g d_c h  (058 obstruction);
#  (b) under Schouten closure the (2,1,1)-type part does NOT vanish in general
#      (explicit Schouten-closed examples: Theta = x3 d_1^wedge d_2, and the
#      so(3) Lie-Poisson bivector), so closure alone does not fix the naive
#      truncation;
#  (c) at constant Theta the defect equals minus the Hochschild coboundary of
#      the Moyal order-Theta^2 bidifferential operator
#      B2M(f,g) = -(1/8) Theta^{ab} Theta^{cd} d_ac f d_bd g.
# Run from repo root:  python -I proposals/105-a-map-order2-associator-correction/s1_naive_associator.py
import itertools
import sys
import sympy as sp

d = 4
x = sp.symbols("x0:4")
I = sp.I

# ---- generic Theta^{ab}(x), a<b, polynomial of degree<=2 with independent jets
TH = {}
TA = {}
TB = {}
TQ = {}
for a, b in itertools.combinations(range(d), 2):
    A = sp.symbols("TA_%d%d" % (a, b))
    Bc = sp.symbols("TB_%d%d_0:%d" % (a, b, d))
    q = sp.S.Zero
    for c in range(d):
        for dd in range(c, d):
            qc = sp.symbols("TQ_%d%d_%d%d" % (a, b, c, dd))
            fac = sp.S.One if c == dd else sp.S(2)
            q += fac * qc * x[c] * x[dd]
            TQ[(a, b, c, dd)] = qc
    TH[(a, b)] = A + sum(Bc[c] * x[c] for c in range(d)) + sp.Rational(1, 2) * q
    TA[(a, b)] = A
    for c in range(d):
        TB[(a, b, c)] = Bc[c]

def thmat(a, b):
    if a == b:
        return sp.S.Zero
    if a < b:
        return TH[(a, b)]
    return -TH[(b, a)]

def thjet(a, b):  # value at 0
    if a == b:
        return sp.S.Zero
    if a < b:
        return TA[(a, b)]
    return -TA[(b, a)]

def thd(a, b, c):  # d_c Theta^{ab} at 0
    if a == b:
        return sp.S.Zero
    if a < b:
        return TB[(a, b, c)]
    return -TB[(b, a, c)]

def thdd(a, b, c, dd):  # d_c d_dd Theta^{ab} at 0
    if a == b:
        return sp.S.Zero
    if a < b:
        return TQ[(a, b, c, dd)] if c <= dd else TQ[(a, b, dd, c)]
    return -TQ[(b, a, c, dd)] if c <= dd else -TQ[(b, a, dd, c)]

# ---- test functions: degree<=2 polynomials with independent coefficients
def mkf(pref):
    # convention (matches jval): f = c0 + c_i x_i + sum_{a<=b} c_{5+t} x_a x_b,
    # so d_i d_i f(0) = 2 c_{5+t} for a==b and d_i d_j f(0) = c_{5+t} for i!=j.
    cs = sp.symbols(pref + "0:15")
    f = cs[0]
    for i in range(4):
        f += cs[1 + i] * x[i]
    k = 5
    for a in range(4):
        for b in range(a, 4):
            f += cs[k] * x[a] * x[b]
            k += 1
    return f, cs

f, cf = mkf("u")
g, cg = mkf("v")
h, ch = mkf("w")

def B1(p, q):
    s = sp.S.Zero
    for a in range(d):
        for b in range(d):
            s += sp.Rational(1, 2) * I * thmat(a, b) * sp.diff(p, x[a]) * sp.diff(q, x[b])
    return s

def eval0(e):
    return e.subs({xi: 0 for xi in x})

# associator of naive truncation at order Theta^2
A2 = sp.expand(eval0(B1(B1(f, g), h) - B1(f, B1(g, h))))

# jet dictionaries: for test function with coefficients cs,
# value = cs[0]; d_i = cs[1+i]; d_i d_j (i!=j) = cs[5+t]; d_i d_i = 2*cs[5+t]
def jval(cs, alpha):
    # alpha tuple of indices, |alpha| in {0,1,2}
    if len(alpha) == 0:
        return cs[0]
    if len(alpha) == 1:
        return cs[1 + alpha[0]]
    i, j = sorted(alpha)
    t = 0
    for a in range(4):
        for b in range(a, 4):
            if (a, b) == (i, j):
                return cs[5 + t] * (sp.S(2) if i == j else sp.S(1))
            t += 1
    raise ValueError

def monom(af, ag, ah):
    return jval(cf, af) * jval(cg, ag) * jval(ch, ah)

# ---- Schouten components at 0 (fully antisymmetric)
def schouten(a, b, c):
    s = sp.S.Zero
    for e in range(d):
        s += thjet(a, e) * thd(e, b, c)  # Theta^{ae} d_e Theta^{bc}  (note d_e Theta^{bc} vs [Theta,Theta]^{abc}=Theta^{ad}d_d Theta^{bc}+cyc)
    for e in range(d):
        s += thjet(b, e) * thd(e, c, a)
    for e in range(d):
        s += thjet(c, e) * thd(e, a, b)
    return s

# ---- (a) (1,1,1) part: coefficient of d_p f d_q g d_r h
print("=== (a) (1,1,1) part of the naive order-2 associator vs Schouten ===")
T = {}
for p, q, r in itertools.product(range(d), repeat=3):
    T[(p, q, r)] = sp.expand(A2.coeff(monom((p,), (q,), (r,))))
# antisymmetrize over (p,q,r)
AS = {}
for p, q, r in itertools.permutations(range(4), 3):
    if len({p, q, r}) < 3:
        continue
    AS[(p, q, r)] = sp.expand(
        T[(p, q, r)] + T[(q, r, p)] + T[(r, p, q)]
        - T[(p, r, q)] - T[(r, q, p)] - T[(q, p, r)])
# compare with Schouten on independent components
ratios = set()
for p, q, r in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
    sh = sp.expand(schouten(p, q, r))
    a = AS[(p, q, r)]
    rr = sp.simplify(sp.together(a / sh))
    ratios.add(sp.nsimplify(rr))
    print("component (%d,%d,%d): associator-antisym / Schouten =" % (p, q, r), sp.nsimplify(rr))
print("(a) CHECK antisym part proportional to Schouten with constant ratio:",
      "PASS" if len(ratios) == 1 else "FAIL", "ratio =", ratios)

# also verify full 64-component identity: AS[p,q,r] = ratio * Schouten[p,q,r] for ALL p,q,r
ratio0 = ratios.pop() if len(ratios) == 1 else None
ok_full = True
if ratio0 is not None:
    for p, q, r in itertools.product(range(d), repeat=3):
        sh = sp.expand(schouten(p, q, r))
        diff = sp.expand(AS.get((p, q, r), sp.S.Zero) - ratio0 * sh)
        if diff != 0:
            ok_full = False
            print("FULL FAIL at", (p, q, r), diff)
print("(a) full antisymmetric-tensor identity:", "PASS" if ok_full else "FAIL")

# ---- (b) closure does not kill the (2,1,1)-type terms
print()
print("=== (b) Schouten-closed examples with nonzero naive associator ===")
# extract (2,1,1)-type coefficients, e.g. monomials u_{dd} v_i w_j (i,j singles)
def coeff_of(m):
    return sp.expand(A2.coeff(m))

# substitution for a given bivector field: Theta^{ab}(x) given as sympy expression
def norm_theta(dct):
    """normalize keys to a<b with sign absorbed"""
    nd = {}
    for (a, b), expr in dct.items():
        if a < b:
            nd[(a, b)] = expr
        elif a > b:
            nd[(b, a)] = -expr
    return nd

def subst_theta(dct):
    """dct maps (a,b) (any order) to sympy expression in x; returns substitution of
    TA/TB/TQ jets at x=0 from exact derivatives."""
    dct = norm_theta(dct)
    subs = {}
    # all jets of all components default zero
    for (a, b) in itertools.combinations(range(d), 2):
        subs[TA[(a, b)]] = sp.S.Zero
        for c in range(d):
            subs[TB[(a, b, c)]] = sp.S.Zero
            for dd in range(c, d):
                subs[TQ[(a, b, c, dd)]] = sp.S.Zero
    for (a, b), expr in dct.items():
        subs[TA[(a, b)]] = expr.subs({xi: 0 for xi in x})
        for c in range(d):
            subs[TB[(a, b, c)]] = sp.diff(expr, x[c]).subs({xi: 0 for xi in x})
            for dd in range(c, d):
                subs[TQ[(a, b, c, dd)]] = sp.diff(expr, x[c], x[dd]).subs({xi: 0 for xi in x})
    return subs

# symbolic Schouten bracket of a bivector field: [Theta,Theta]^{abc}
def schouten_field(dct):
    # full x-dependent Schouten of a bivector given by dct
    dct = norm_theta(dct)
    def thf(a, b):
        if a == b:
            return sp.S.Zero
        if a < b:
            return dct.get((a, b), sp.S.Zero)
        return -dct.get((b, a), sp.S.Zero)
    # formula: [Theta,Theta]^{pqr} = Theta^{pe} d_e Theta^{qr} + cyc(p,q,r)
    res = {}
    for p, q, r in itertools.combinations(range(d), 3):
        s = sp.S.Zero
        for e in range(d):
            s += thf(p, e) * sp.diff(thf(q, r), x[e])
            s += thf(q, e) * sp.diff(thf(r, p), x[e])
            s += thf(r, e) * sp.diff(thf(p, q), x[e])
        res[(p, q, r)] = sp.simplify(sp.expand(s))
    return res

# example 1: Theta^{01} = x2  (i.e. Theta = x3 d_1 wedge d_2 in 1-based)
ex1 = {(0, 1): x[2]}
sch1 = schouten_field(ex1)
print("ex1 Schouten components:", {k: v for k, v in sch1.items() if v != 0} or "all zero -> Schouten-closed")
s1 = subst_theta(ex1)
A2x1 = sp.expand(A2.subs(s1))
# pick explicit f,g,h values: all 15 jets = specific (generic) numbers
import random
rng = random.Random(105)
vals = [rng.randrange(100, 999) / 1000 for _ in range(45)]
valf = {}
for j, cs in enumerate((cf, cg, ch)):
    for i in range(15):
        valf[cs[i]] = vals[15 * j + i]
n1 = complex(A2x1.subs(valf))
print("ex1 naive order-2 associator at random quadratic test triple =", n1)

# example 2: so(3) Lie-Poisson: Theta^{01}=x2, Theta^{12}=x0, Theta^{20}=x1
ex2 = {(0, 1): x[2], (1, 2): x[0], (2, 0): x[1]}
sch2 = schouten_field(ex2)
nz2 = {k: sp.simplify(v) for k, v in sch2.items() if sp.simplify(v) != 0}
print("ex2 (so3 Lie-Poisson) Schouten:", nz2 or "all zero -> Poisson (Jacobi holds)")
s2s = subst_theta(ex2)
A2x2 = sp.expand(A2.subs(s2s))
n2 = complex(A2x2.subs(valf))
print("ex2 naive order-2 associator at random quadratic test triple =", n2)

# ---- (c) constant Theta: defect = -delta B2M
print()
print("=== (c) constant-Theta defect vs Hochschild coboundary of Moyal order-2 operator ===")
const_subs = {}
for (a, b) in itertools.combinations(range(d), 2):
    for c in range(d):
        const_subs[TB[(a, b, c)]] = sp.S.Zero
        for dd in range(c, d):
            const_subs[TQ[(a, b, c, dd)]] = sp.S.Zero
A2c = sp.expand(A2.subs(const_subs))

def B2M(p, q):
    s = sp.S.Zero
    for a in range(d):
        for b in range(d):
            for c2 in range(d):
                for dd in range(d):
                    s += -sp.Rational(1, 8) * thmat(a, b) * thmat(c2, dd) * sp.diff(p, x[a], x[c2]) * sp.diff(q, x[b], x[dd])
    return s

def deltaB2(B2, p, q, r):
    return (B2(p * q, r) + r * B2(p, q) - B2(p, q * r) - p * B2(q, r))

resid = sp.simplify(eval0(deltaB2(B2M, f, g, h) + A2c))
resid = sp.expand(resid)
print("(c) delta(B2M) + A2(constant Theta) expanded residual (expect 0):",
      resid if resid == 0 else "NONZERO: " + str(resid))
print("(c) CHECK:", "PASS" if resid == 0 else "FAIL")

# also report the antisym (1,1,1) ratio found
print()
print("SUMMARY (a): naive (1,1,1) associator part = ratio * [Theta,Theta]^{abc} d_a f d_b g d_c h, ratio =", ratio0)
sys.exit(0 if (len({ratio0}) == 1 and ok_full and resid == 0) else 1)
