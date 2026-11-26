# s1_wall_jacobian_v8.py  -- proposal 093, round 1 (authoritative version)
# Run from repo root:  python -I proposals/093-g-orbit-rigidity-vandermonde-walls/s1_wall_jacobian_v8.py
# Deterministic; no randomness. Sympy for exact identities, plain floats for rate checks.
import itertools, math
import sympy as sp

def h_seq(syms):
    # syms[k] = power sum s_{k+1}; returns [h_0..h_p] symbolic via Newton recursion
    P = len(syms)
    h = [sp.Integer(1)]
    for p in range(1, P + 1):
        tot = sp.Integer(0)
        for k in range(1, p + 1):
            tot += syms[k - 1] * h[p - k]
        h.append(sp.expand(tot / p))
    return h

def rho_from_g(gs, W, D):
    # gs: list of D sympy profile entries summing to W; returns [rho_1..rho_D]
    s = [sum(x ** k for x in gs) for k in range(1, D + 1)]
    h = h_seq(s)[: D + 1]
    return [sp.simplify(sp.factorial(p) * h[p] / W ** p) for p in range(1, D + 1)]

print("== PART A: chamber Jacobian factorization ==")
okA = True
for D in (2, 3):
    W = sp.Symbol("W", positive=True)
    g = [sp.Symbol("g%d" % (i + 1)) for i in range(D - 1)]
    gD = W - sum(g)
    gg = g + [gD]
    rho = rho_from_g(gg, W, D)[1:]
    J = sp.Matrix([[sp.diff(rho[i], g[j]) for j in range(D - 1)] for i in range(D - 1)])
    detJ = sp.simplify(J.det())
    V = sp.prod(gg[i] - gg[j] for i, j in itertools.combinations(range(D), 2))
    cD = 1
    for k in range(1, D + 1):
        cD *= sp.factorial(k)
    target = cD * V / W ** (D * (D + 1) // 2 - 1)
    d2 = sp.simplify((detJ ** 2) - (target ** 2))
    sgn = sp.simplify(detJ / target)
    ok = (d2 == 0) and (sgn ** 2 == 1)
    okA = okA and ok
    print("D=%d: det(J)^2 - (prod(k!)V/W^(D(D+1)/2-1))^2 == 0 : %s ; det/target = %s"
          % (D, d2 == 0, sgn))
# D=4: symbolic then substitute (exact rationals)
Wsym = sp.Symbol("W")
gsym = [sp.Symbol("u%d" % (i + 1)) for i in range(3)]
gg_sym = gsym + [Wsym - sum(gsym)]
rho4 = rho_from_g(gg_sym, Wsym, 4)[1:]
J4 = sp.Matrix([[sp.diff(rho4[i], gsym[j]) for j in range(3)] for i in range(3)])
det4sym = J4.det()
for trial in [(1, 3, 5, 7, 20), (2, 1, 6, 4, 30), (1, 1, 1, 1, 12)]:
    Wv = sp.Integer(trial[4])
    subd = {Wsym: Wv}
    for i in range(3):
        subd[gsym[i]] = sp.Integer(trial[i])
    detJ = sp.simplify(det4sym.subs(subd))
    gi = [sp.Integer(x) for x in trial[:3]]
    gg4 = gi + [Wv - sum(gi)]
    V = sp.prod(gg4[i] - gg4[j] for i, j in itertools.combinations(range(4), 2))
    target = (sp.factorial(1) * sp.factorial(2) * sp.factorial(3) * sp.factorial(4)) * V / Wv ** 9
    ok = sp.simplify(detJ ** 2 - target ** 2) == 0
    okA = okA and ok
    print("D=4 trial %s: exact match: %s" % (str(trial), ok))
print("PART A RESULT:", "PASS" if okA else "FAIL")

print("== PART B: D=2 exact fold normal form ==")
W = sp.Symbol("W", positive=True)
g1 = sp.Symbol("g1")
g2 = W - g1
r2 = rho_from_g([g1, g2], W, 2)[1]
delta = sp.symbols("delta", nonnegative=True)
nf = (3 * W ** 2 + delta ** 2) / (2 * W ** 2)
okB1 = sp.simplify(r2 - nf.subs(delta, g1 - g2)) == 0
print("rho_2 = (3W^2+(g1-g2)^2)/(2W^2) : %s" % okB1)
okB2 = (r2.subs(g1, W / 2) == sp.Rational(3, 2)) and (sp.simplify(r2.subs(g1, W) - 2) == 0)
print("wall value rho_2(uniform)=3/2 ; single-row limit rho_2=2 : %s" % okB2)
inv = sp.simplify(2 * W ** 2 * (nf - sp.Rational(3, 2)) - delta ** 2)
print("exact inversion (g1-g2)^2 = 2W^2(rho_2-3/2) : %s" % (inv == 0))
okB4 = True
for a in range(17):
    for b in range(17):
        dd, ddp = sp.Rational(a, 16) * W, sp.Rational(b, 16) * W
        rr = abs((nf.subs(delta, dd)) - (nf.subs(delta, ddp)))
        if sp.simplify(abs(dd - ddp) - sp.sqrt(2 * W ** 2 * rr)) > 0:
            okB4 = False
print("global 1/2-Holder, constant sqrt(2)*W, 17x17 grid : %s" % okB4)
inv_slope = sp.simplify(1 / sp.diff(nf, delta) - W ** 2 / delta)
okB5 = inv_slope == 0
print("D=2 inverse slope d(delta)/d(rho_2) = W^2/(g1-g2): %s (so <= W^2/delta on |g1-g2|>=delta)" % okB5)
print("PART B RESULT:", "PASS" if (okB1 and okB2 and (inv == 0) and okB4 and okB5) else "FAIL")

print("== PART C: general-D transverse wall normal form ==")
okC = True
c, u = sp.symbols("c u")
for k in range(2, 7):
    lhs = (c + u) ** k + (c - u) ** k - 2 * c ** k
    rhs = 2 * sum(sp.binomial(k, 2 * j) * c ** (k - 2 * j) * u ** (2 * j) for j in range(1, k // 2 + 1))
    ok = sp.expand(lhs - rhs) == 0
    okC = okC and ok
print("s_k transverse even polynomial identity (k=2..6): %s" % okC)
odd = sp.expand(sum(sp.diff(((c + u) ** k + (c - u) ** k - 2 * c ** k), u).subs(u, 0) for k in range(2, 7)))
print("odd transverse first-derivative coefficients vanish at u=0 (k=2..6): %s" % (odd == 0))
okC2 = True
for D in (2, 3, 4):
    rest = [sp.Symbol("r%d" % (i + 3)) for i in range(D - 2)]
    gg = [c + u, c - u] + rest
    Wsub = sum(gg)
    rr = [sp.simplify(x) for x in rho_from_g(gg, Wsub, D)][1]
    r0 = sp.simplify(rr.subs(u, 0))
    dif = sp.expand(rr - r0)
    coef = sp.simplify(sp.diff(dif, u, 2).subs(u, 0) / 2)
    lin = sp.simplify(dif - coef * u ** 2)
    ok = (sp.simplify(lin) == 0) and (sp.simplify(coef - 2 / Wsub ** 2) == 0)
    okC2 = okC2 and ok
    print("D=%d: rho_2 deviation exactly (2/W^2) u^2 : %s (coeff %s)" % (D, ok, sp.simplify(coef)))
okC3 = True
for D in (3, 4):
    rest = [sp.Symbol("q%d" % (i + 3)) for i in range(D - 2)]
    Wt = 2 * c + sum(rest)
    for k in range(2, 6):
        sdev = ((c + u) ** k + (c - u) ** k - 2 * c ** k) / Wt ** k
        ck = sp.simplify(sp.diff(sdev, u, 2).subs(u, 0) / 2)
        target = k * (k - 1) * c ** (k - 2) / Wt ** k
        ok = sp.simplify(ck - target) == 0
        okC3 = okC3 and ok
print("power-sum ray coefficients k(k-1)c^(k-2)/W^k (D=3,4; k=2..5): %s" % okC3)
print("PART C RESULT:", "PASS" if (okC and odd == 0 and okC2 and okC3) else "FAIL")

print("== PART D: numerical inverse-regularity rates ==")
def rho_num(gvec):
    D = len(gvec)
    Wv = sum(gvec)
    s = [sum(x ** k for x in gvec) for k in range(1, D + 1)]
    h = [1.0]
    for p in range(1, D + 1):
        h.append(sum(s[k - 1] * h[p - k] for k in range(1, p + 1)) / p)
    return [math.factorial(p) * h[p] / Wv ** p for p in range(1, D + 1)]

def jac_num(gvec, eps=1e-6):
    D = len(gvec)
    cols = []
    for j in range(D - 1):
        gp = list(gvec); gm = list(gvec)
        gp[j] += eps; gm[j] -= eps
        gp[-1] -= eps; gm[-1] += eps
        cols.append([(rho_num(gp)[i + 1] - rho_num(gm)[i + 1]) / (2 * eps) for i in range(D - 1)])
    return cols

import numpy as np

def sigma_min(J):
    M = np.array([[J[a][i] for a in range(len(J))] for i in range(len(J))], dtype=float)
    return float(np.linalg.svd(M, compute_uv=False)[-1])

def prof_simple(delta):
    v = (1.0 - 0.5) / 2
    return [0.5, v + delta / 2, v - delta / 2]

deltas = [2.0 ** (-e) for e in range(3, 10)]
sm = [sigma_min(jac_num(prof_simple(d))) for d in deltas]
r_simple = [sm[i] / sm[i + 1] for i in range(len(deltas) - 1)]
okD1 = all(abs(r / 2.0 - 1) < 0.05 for r in r_simple[-4:])
print("D=3 simple wall: sigma_min(delta)/sigma_min(2delta) -> 2 = 2^1 (one wall factor in V)? last ratios:", ["%.4f" % r for r in r_simple[-3:]])

def prof_total(t):
    y = [1 / math.sqrt(2), 0.0, -1 / math.sqrt(2)]
    return [1 / 3 + t * yi for yi in y]

st = [sigma_min(jac_num(prof_total(d))) for d in deltas]
r_tot = [st[i] / st[i + 1] for i in range(len(deltas) - 1)]
okD2 = all(abs(r / 4.0 - 1) < 0.08 for r in r_tot[-4:])
print("D=3 near-total coincidence: sigma_min ratio -> 4 = 2^(D-1)? last ratios:", ["%.4f" % r for r in r_tot[-3:]])

tvals = [10.0 ** (-e) for e in range(1, 6)]
base = rho_num([1 / 3.0] * 3)[1:]
rd = []
for t in tvals:
    rvec = rho_num(prof_total(t))[1:]
    rd.append(math.sqrt(sum((rvec[i] - base[i]) ** 2 for i in range(2))))
slopes = [math.log(rd[i + 1] / rd[i]) / math.log(tvals[i + 1] / tvals[i]) for i in range(len(tvals) - 1)]
okD3 = all(abs(s - 2) < 0.05 for s in slopes[-2:])
print("D=3 triple approach: log-log slope of rho-distance vs gap t -> 2 (= exponent 1/2):", ["%.4f" % s for s in slopes])
print("PART D RESULT:", "PASS" if (okD1 and okD2 and okD3) else "FAIL")

allres = okA and okB1 and okB2 and (inv == 0) and okB4 and okB5 and okC and (odd == 0) and okC2 and okC3 and okD1 and okD2 and okD3
print("S1 OVERALL:", "PASS" if allres else "FAIL")
