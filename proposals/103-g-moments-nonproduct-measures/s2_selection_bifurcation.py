# s2_selection_bifurcation.py -- proposal 103, selection and bifurcation structure of the
# coherence-induced profile weight at D=2.
#  (A) equal variances: symbolic max at barycenter for every r in (0,1), flat at r=0;
#      coincidence enhancement P(|2p-1|<eps) = eps/sqrt(1-r^2) + O(eps^3) (coefficient exact,
#      quadrature and MC check);
#  (B) exact high-precision moments E[s2](r), E[s2^2](r) at equal variances by 50-digit
#      quadrature (consistency across dps), MC cross-check;
#  (C) unequal variances (g1,g2)=(1,2): right-vertex slope criterion |rho|^2 > g1(g2-g1)/6
#      (symbolic), existence threshold r*^2 = (g2-g1)/(6 g2); fine-grid argmax table vs rhat;
#      global switch from vertex to interior recorded.
# Run from repo root: python -I proposals/103-g-moments-nonproduct-measures/s2_selection_bifurcation.py
import mpmath
import numpy as np
import sympy as sp

mpmath.mp.dps = 50

p, r = sp.symbols("p r", positive=True)

def fdens(g1v, g2v, rhat):
    """closed-form pushforward density as mpmath function of p"""
    g1, g2, rr = sp.Rational(g1v), sp.Rational(g2v), sp.nsimplify(rhat)
    det = g1 * g2 - rr**2
    bb = g2 * p + g1 * (1 - p)
    cc = 2 * rr * sp.sqrt(p * (1 - p))
    f = det * bb / (bb**2 - cc**2) ** sp.Rational(3, 2)
    return sp.lambdify(p, f, "mpmath")

print("=== (A) equal variances: max at barycenter, coincidence enhancement ===")
feq = (1 - r**2) / (1 - 4 * r**2 * p * (1 - p)) ** sp.Rational(3, 2)
d1 = sp.simplify(sp.diff(feq, p).subs(p, sp.Rational(1, 2)))
print("f'(1/2) at equal variance (symbolic, all r):", d1)
d2 = sp.simplify(sp.diff(feq, p, 2).subs(p, sp.Rational(1, 2)))
print("f''(1/2) =", d2, "; at r=1/2:", sp.simplify(d2.subs(r, sp.Rational(1, 2))), " (negative)")
# monotonicity in z = p(1-p): feq as function of z
z = sp.symbols("z", positive=True)
fz = (1 - r**2) / (1 - 4 * r**2 * z) ** sp.Rational(3, 2)
print("d/dz of equal-variance density (symbolic):", sp.simplify(sp.diff(fz, z)), " > 0 for r>0, z<1/4")
print("=> density strictly increasing in p(1-p): unique max at p=1/2 for every r in (0,1);")
print("   at r=0 the density is f=1 (flat):", sp.simplify(feq.subs(r, 0)))
# coincidence coefficient
for rv in [sp.Rational(1, 2), sp.Rational(7, 10), sp.Rational(9, 10)]:
    fv = sp.lambdify(p, feq.subs(r, rv), "mpmath")
    for eps in [mpmath.mpf("0.05"), mpmath.mpf("0.01")]:
        lo = mpmath.mpf("0.5") - eps / 2
        hi = mpmath.mpf("0.5") + eps / 2
        exact = mpmath.quad(fv, [lo, hi])
        lead = eps / mpmath.sqrt(1 - float(rv) ** 2)
        print("r=%s eps=%s: P(|2p-1|<eps) quad %s leading eps/sqrt(1-r^2) %s ratio %s"
              % (rv, eps, mpmath.nstr(exact, 12), mpmath.nstr(lead, 12), mpmath.nstr(exact / lead, 8)))
# MC check of coincidence probability at r=0.5, eps=0.05
rng = np.random.default_rng(1032)

def sample_p(g1v, g2v, rhat, ph, n):
    mag = rhat * np.sqrt(g1v * g2v)
    Sig = np.array([[g1v, mag * np.exp(1j * ph)], [mag * np.exp(-1j * ph), g2v]])
    L = np.linalg.cholesky(Sig)
    zh = (rng.standard_normal((n, 2)) + 1j * rng.standard_normal((n, 2))) / np.sqrt(2)
    W = zh @ L.T
    E = np.abs(W) ** 2
    return E[:, 0] / E.sum(1)

pMC = sample_p(1.0, 1.0, 0.5, 0.0, 4_000_000)
print("MC P(|2p-1|<0.05) r=0.5: %.6f  leading pred %.6f" % (np.mean(np.abs(2 * pMC - 1) < 0.05), 0.05 / np.sqrt(0.75)))

print()
print("=== (B) exact high-precision moments E[s2](r) at equal variances ===")
for rv in ["0", "1/2", "7/10", "9/10"]:
    rrv = sp.Rational(rv)
    fexpr = (1 - rrv**2) / (1 - 4 * rrv**2 * p * (1 - p)) ** sp.Rational(3, 2)
    fv = sp.lambdify(p, fexpr, "mpmath")
    def es2():
        return mpmath.quad(lambda x: (x**2 + (1 - x) ** 2) * fv(x), [0, "0.5", 1.0])
    v50 = es2()
    mpmath.mp.dps = 30
    v30 = es2()
    mpmath.mp.dps = 50
    def es22():
        return mpmath.quad(lambda x: (x**2 + (1 - x) ** 2) ** 2 * fv(x), [0, "0.5", 1.0])
    w50 = es22()
    print("r=%s: E[s2] %s (dps30 diff %.1e) ; E[rho_2]=1+E[s2]=%s ; E[s2^2]=%s ; E[s2]-2/3=%s"
          % (rv, mpmath.nstr(v50, 20), abs(v50 - v30), mpmath.nstr(1 + v50, 20), mpmath.nstr(w50, 20), mpmath.nstr(v50 - mpmath.mpf(2) / 3, 10)))
pMC = sample_p(1.0, 1.0, 0.9, 0.0, 4_000_000)
print("MC E[s2] r=0.9: %.5f" % np.mean(pMC**2 + (1 - pMC) ** 2))

print()
print("=== (C) unequal variances (1,2): vertex slope, thresholds, argmax table ===")
g1v, g2v = sp.Integer(1), sp.Integer(2)
detu = g1v * g2v - r**2
bu = g2v * p + g1v * (1 - p)
cu = 2 * r * sp.sqrt(p * (1 - p))
fu = detu * bu / (bu**2 - cu**2) ** sp.Rational(3, 2)
Lp = sp.simplify(sp.diff(sp.log(fu), p))
slope0 = sp.simplify(Lp.limit(p, 0, "+"))
thr = sp.solve(sp.Eq(slope0, 0), r**2)[0]
print("d/dp log f at p=0+ (g=(1,2), |rho|=r):", slope0, " > 0 iff |rho|^2 >", thr)
print("=> interior maximum exists iff |rho|^2 > g1(g2-g1)/3 = 1/3, i.e. normalized coherence rhat^2 > (g2-g1)/(3 g2) = 1/6, rhat* =", float(sp.sqrt(sp.Rational(1, 6))))
grid = np.linspace(1e-6, 1 - 1e-6, 200001)
print("|rho| (=r in fu)   argmax(grid p1)   fmax/f(vertex at r=0)   vertex-value f(0)(|rho|)")
for rv in [0.0, 0.2, 0.28, 0.30, 0.35, 0.5, 0.7, 0.9, 0.99]:
    if rv > 0:
        fnum = sp.lambdify(p, fu.subs(r, sp.Float(rv, 30)), "numpy")
    else:
        fnum = sp.lambdify(p, fu.subs(r, 0), "numpy")
    vals = fnum(grid)
    i = int(np.argmax(vals))
    v0r = float(fu.subs({p: 0, r: max(rv, 1e-12)})) if rv > 0 else float(fu.subs({p: 0, r: 0}))
    v0_0 = float(fu.subs({p: 0, r: 0}))
    print("%.2f   %.5f        %.5f              %.5f" % (rv, grid[i], vals[i] / v0_0, v0r))
print("S2 DONE")
