# remainder_rouche.py -- proposal 067, round 2.
# Checks for the "named completion class" analysis of the Problem N block:
#  (i)  symbolic identity: F(x; d) + eps*x = F(x; d - U*eps): every analytic O(x)
#       completion reparametrizes delta_W (header comment fixed in r2 per review
#       finding 4; the code always implemented d - U*eps);
#  (ii) counterexample to unconditional stability inside the named class: the completion
#       G = F - c*x^2 (no logarithm: the O(p^4) log coefficient and delta_W are unchanged)
#       puts a zero of the factor at 0 < x < 1 whenever c > c*, with c* = inf_{0<x<1} F(x)/x^2;
#       computed threshold at U=10, d=0;
#  (iii) the conditional (Rouche-on-the-slit-disc) hypothesis:
#       m(U,d) = min over the boundary of the slit disc {|x|<1} \ (-inf,0] of |F|:
#       circle part, cut part, and the combined min;
#  (iv) direct root counts of G = F - c*x^2 in the slit disc for c below (0.5) and above
#       (1.2) the threshold, by dense-seed Newton root finding (a check, not a proof).
# Run: python -I remainder_rouche.py
import sympy as sp
import mpmath as mp

mp.mp.dps = 30

print("=" * 72)
print("(i) symbolic identity: F(x;d) + eps*x = F(x; d - U*eps)")
print("=" * 72)
x, U, d, eps = sp.symbols("x Upsilon delta_W epsilon")
Fsym = lambda dv: 1 - (x / U) * (sp.log(1 / x) + dv)
print("residual:", sp.simplify(Fsym(d) + eps * x - Fsym(d - U * eps)))
print("(F(x)+R(x), R = (x/U) r(x), r(0)=0 for the massless sector by threshold)")

print()
print("=" * 72)
print("(iii) margin m(U,d) over the slit-disc boundary, U=10, d=0")
print("=" * 72)

def Fnum(xv, Uv, dv):
    return 1 - (xv / Uv) * (mp.log(1 / xv) + dv)

def circle_min(Uv, dv):
    f = lambda th: abs(Fnum(mp.e**(1j * th), Uv, dv))
    best, bth = mp.inf, None
    N = 4000
    for i in range(N + 1):
        th = mp.mpf(i) * 2 * mp.pi / N
        if abs(th - mp.pi) < 1e-3:      # x = -1 is on the branch cut
            continue
        v = f(th)
        if v < best:
            best, bth = v, th
    return best, bth

def cut_min(Uv, dv):
    # both sides of the cut: x = -r +- i0, r in (0,1); principal log(1/x) = ln(1/r) -/+ i pi
    best = mp.inf
    N = 4000
    for i in range(1, N + 1):
        r = mp.mpf(i) / N
        lp = mp.log(1 / r) - mp.pi * 1j
        lm = mp.log(1 / r) + mp.pi * 1j
        for L in (lp, lm):
            v = abs(1 - (-r / Uv) * (L + dv))
            if v < best:
                best = v
    return best

m10, th10 = circle_min(10, 0)
mc = cut_min(10, 0)
print("circle part:  min |F(e^{i th})| =", mp.nstr(m10, 8), " at theta =", mp.nstr(th10, 8),
      " (and 2pi - theta)")
print("cut part:     min over both sides =", mp.nstr(mc, 8))
mtil = min(m10, mc)
print("combined slit-disc boundary margin m(10,0) =", mp.nstr(mtil, 8))
for Uv, dv in [(2.0, 0.0), (1.5707963, 0.0), (3.0, 2.0)]:
    m1, _ = circle_min(Uv, dv)
    print(f"  m({Uv},{dv}) circle part =", mp.nstr(m1, 8),
          "(~0 at the crossing U=pi/2)" if abs(Uv - mp.pi / 2) < 1e-3 else "")

print()
print("=" * 72)
print("(ii) counterexample threshold: G = F - c*x^2, U=10, d=0")
print("=" * 72)
def Fs(r):
    return 1 - (r / 10) * mp.log(1 / r)
# a root in (0,1) exists iff c is in the range of F(x)/x^2 on (0,1);
# F(x)/x^2 -> +inf as x->0 and equals 1 at x=1; infimum over (0,1) is 1 (monotone
# decreasing: check d/dx [F/x^2] < 0 on a sample grid).
gder = lambda r: (-(mp.log(1/r)/10 + 1/10) * r * r - 2 * r * Fs(r)) / r**4
bad = [r for r in (mp.mpf(i)/200 for i in range(1,200)) if gder(r) >= 0]
print("d/dx (F/x^2) < 0 on (0,1) sample grid:", not bad)
best = mp.inf; bxt = None
for i in range(1, 20001):
    r = mp.mpf(i) / 20000
    v = Fs(r) / r ** 2
    if v < best:
        best, bxt = v, r
print("inf_{(0,1)} F(x)/x^2 =", mp.nstr(best, 8), " at x =", mp.nstr(bxt, 6),
      "; threshold c* = 1 (attained at the endpoint x=1)")
for c in (0.5, 0.9, 1.0, 1.2, 2.0):
    # root in (0,1)? G(0+)=1>0, G(1)=1-c
    G = lambda r: Fs(r) - c * r ** 2
    if G(1) < 0:
        rt = mp.findroot(G, mp.mpf("0.9"))
        print(f"  c = {c}: zero of G at x = {mp.nstr(rt, 10)} (inside |x|<1)")
    else:
        print(f"  c = {c}: G(1) = {mp.nstr(G(1), 6)} > 0, no forced root in (0,1)")

print()
print("=" * 72)
print("(iv) direct zero count of G = F - c x^2 in the slit disc (check, not proof)")
print("=" * 72)
def Gnum(z, c):
    return Fnum(z, 10, 0) - c * z ** 2

def count_zeros(c, rmax=0.999):
    seeds = []
    for ri in range(1, 40):
        r = mp.mpf(ri) / 40
        for tj in range(60):
            th = -mp.pi + mp.pi * 2 * tj / 60
            z = r * mp.e**(1j * th)
            if abs(z + 1) < 0.02:
                continue
            seeds.append(z)
    zs = []
    for z0 in seeds:
        try:
            z = mp.findroot(lambda zz: Gnum(zz, c), z0, solver="mnewton",
                            maxsteps=60, tol=mp.mpf("1e-24"))
        except Exception:
            continue
        if not mp.isfinite(z):
            continue
        if abs(z) >= rmax or abs(mp.im(z)) < 1e-12 and z.real < 0:
            continue
        dup = any(abs(z - w) < 1e-7 for w in zs)
        if not dup:
            zs.append(z)
    return zs

for c in (0.5, 1.2):
    zs = count_zeros(c)
    print(f"c = {c}: distinct zeros found in the slit disc: {len(zs)}")
    for z in sorted(zs, key=abs):
        print("   x =", mp.nstr(z, 10), " |x| =", mp.nstr(abs(z), 8))
print("expected: c=0.5 < m(10,0)=0.822: 0 zeros (Rouche hypothesis on the slit-disc")
print("          boundary holds); c=1.2 > c*=1: the real zero in (0,1) plus a")
print("          conjugate pair near the cut edge -- the completion destabilises the")
print("          zero-free disc, as claimed.")
print("DONE")
