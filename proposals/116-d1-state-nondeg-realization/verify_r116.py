# verify_r116.py -- verification pack for proposal 116-d1-state-nondeg-realization
# Checks for the manuscript function V(Phi) = (lambda/4) Tr(Phi^dag Phi - v^2 I)^2
# (label eq:V, chapters/ch03-matrix-action.tex L240-244, live tree):
#  N1  Procrustes identity d(Phi) := min_U ||Phi - vU||_op = max_i |sigma_i - v|
#      (polar factor attains; Weyl lower bound; Frobenius analogue).
#  N2  sharp two-sided estimate (lambda/4) d^2 (2v-d)^2 <= V <= lambda d^2 (2v+d)^2, d<=v.
#  N3  attainment: sup_{d=delta} V = lambda delta^2 (2v+delta)^2 at Phi=(v+delta)U;
#      inf_{d=delta} V = (lambda/4) delta^2 (2v-delta)^2 at sigma=(v-delta,v,v,v).
#  N4  sublevel localization: V <= eps  ==>  d <= d_eps = v - sqrt(v^2 - 2 sqrt(eps/lambda)).
#  N5  radius: sup_{d<=delta} V = lambda delta^2 (2v+delta)^2 is < lambda v^4/4 iff
#      delta < delta_* = (sqrt6-2)v/2; equality of the supremum at delta_*.
#  N6  volume bound: mu{det e = 0} <= 4 E_V/(lambda v^4), E_V = int V dmu; equality
#      for a uniform sigma=(0,v,v,v) patch.
#  N7  compatibility: for V <= eps the distance bound |det e| >= (1-d_eps/v)^4 equals
#      the integrated (1 - sqrt(4 eps/lambda)/v^2)^2 of the ordinal-43 paragraph.
#  N8  quadratic consistency with the recorded V^(2)(d=vB)=2 lambda v^4 (appH L2160):
#      the two-sided estimate brackets it; single-sigma and uniform deviations bracket.
# Symbolic (sympy): S1 d_eps identity, S2 delta_* identity, S3 bound identity N7,
# S4 series expansion. Deterministic seed 116. Run: python -I -B verify_r116.py
import numpy as np
import sympy as sp

np.random.seed(116)
PASS = 0
FAIL = 0

def check(name, ok, extra=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + (" " + extra if extra else ""))

def Vval(S, v, lam):
    # V depends only on singular values: (lam/4) sum (s^2-v^2)^2  (identity checked in 115)
    return (lam / 4.0) * np.sum((S**2 - v**2)**2)

def randmat(n=4, scale=3.0):
    A = np.random.randn(n, n) + 1j * np.random.randn(n, n)
    return A * (10.0 ** (np.random.uniform(-scale, scale, 1))[0])

def randU(n=4):
    Q, R = np.linalg.qr(np.random.randn(n, n) + 1j * np.random.randn(n, n))
    d = np.diag(R)
    return Q @ np.diag(np.conj(d) / np.abs(d))

def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]

print("== proposal 116 verification pack, seed 116 ==")

# ---------- N1 Procrustes identity ----------
v0, lam0 = 1.7, 1.3
worst_eq = 0.0
worst_ge = 0.0
worst_fr = 0.0
for k in range(300):
    A = randmat()
    W, s, Zh = np.linalg.svd(A)
    P = W @ Zh                      # polar factor (unitary)
    lhs = np.linalg.norm(A - v0 * P, 2)
    rhs = np.max(np.abs(s - v0))
    worst_eq = max(worst_eq, abs(lhs - rhs) / max(1.0, rhs))
    lhsF = np.linalg.norm(A - v0 * P, 'fro')
    rhsF = np.sqrt(np.sum((s - v0)**2))
    worst_fr = max(worst_fr, abs(lhsF - rhsF) / max(1.0, rhsF))
    for _ in range(10):
        U = randU()
        worst_ge = max(worst_ge, max(0.0, rhs - np.linalg.norm(A - v0 * U, 2)) / max(1.0, rhs))
check("N1 polar attains d = max|sigma-v| (op norm)", worst_eq < 1e-9, "rel-err %.2e" % worst_eq)
check("N1 no unitary beats polar (Weyl lower bound)", worst_ge < 1e-9, "rel-viol %.2e" % worst_ge)
check("N1 Frobenius analogue", worst_fr < 1e-9, "rel-err %.2e" % worst_fr)

# ---------- N2 two-sided estimate ----------
viol = 0
tested = 0
for k in range(20000):
    v = np.random.uniform(0.5, 2.0)
    lam = np.random.uniform(0.3, 2.0)
    s = v * (10.0 ** np.random.uniform(-2.5, 2.5, 4))
    Vm = Vval(s, v, lam)
    d = np.max(np.abs(s - v))
    lo = (lam / 4.0) * d * d * (2 * v - d)**2
    hi = lam * d * d * (2 * v + d)**2
    tested += 1
    if Vm > hi * (1 + 1e-12):
        viol += 1
    if d <= v and Vm < lo * (1 - 1e-12):
        viol += 1
check("N2 two-sided estimate, %d draws" % tested, viol == 0, "violations %d" % viol)

# ---------- N3 attainment of both sides ----------
bad = 0
for k in range(500):
    v = np.random.uniform(0.5, 2.0)
    lam = np.random.uniform(0.3, 2.0)
    delta = np.random.uniform(1e-6, 2.0 * v)
    U = randU()
    Sup = Vval(np.full(4, v + delta), v, lam)
    if abs(Sup - lam * delta**2 * (2 * v + delta)**2) > 1e-8 * max(1.0, Sup):
        bad += 1
    if delta <= v:
        s = np.array([v - delta, v, v, v])
        Sin = Vval(s, v, lam)
        if abs(Sin - (lam / 4.0) * delta**2 * (2 * v - delta)**2) > 1e-8 * max(1.0, Sin):
            bad += 1
check("N3 sup and inf on d=delta attained (radial / single-scalar)", bad == 0, "bad %d" % bad)
# and that no draw beats them (monotone sup over ball):
worst = 0.0
for k in range(20000):
    v = np.random.uniform(0.5, 2.0)
    lam = np.random.uniform(0.3, 2.0)
    delta = np.random.uniform(0.01, 2.0)
    s = v + np.random.uniform(-delta, delta, 4)
    s = np.abs(s)  # sigma >= 0; enlarges d only if below 0, recompute d honestly:
    d = np.max(np.abs(s - v))
    Vm = Vval(s, v, lam)
    sup = lam * d * d * (2 * v + d)**2
    worst = max(worst, Vm - sup)
check("N3 no ball point exceeds sup_{d<=delta}", worst <= 1e-9, "max excess %.2e" % worst)

# ---------- N4 sublevel localization ----------
v, lam = 2.0, 1.3
thr = lam * v**4 / 4.0
for eps in [0.5, 1.0, 2.0, 4.0, 5.1]:
    d_eps = v - np.sqrt(v**2 - 2 * np.sqrt(eps / lam))
    worst = 0.0
    n_acc = 0
    for k in range(200000):
        s = v + np.random.uniform(-v, v, 4)
        if np.any(s < 0):
            continue
        if Vval(s, v, lam) > eps:
            continue
        n_acc += 1
        worst = max(worst, np.max(np.abs(s - v)) - d_eps)
        if n_acc >= 5000:
            break
    check("N4 V<=%.1f forces d<=%.6f (thr=%.3f)" % (eps, d_eps, thr),
          worst <= 1e-9, "accepted %d, max excess %.2e" % (n_acc, worst))

# ---------- N5 radius sharpness ----------
delta_star = (np.sqrt(6.0) - 2.0) * v / 2.0
sup_at = lam * delta_star**2 * (2 * v + delta_star)**2
check("N5 sup at delta_* equals threshold", abs(sup_at - thr) < 1e-9,
      "sup %.12f thr %.12f" % (sup_at, thr))
print("delta_*/v = %.16f   (1-delta_*/v)^4 = %.16f" %
      (delta_star / v, (1 - delta_star / v)**4))
bad = 0
for k in range(4000):
    delta = np.random.uniform(0.0, delta_star * (1 - 1e-12))
    s = v + np.random.uniform(-delta, delta, 4)
    s = np.abs(s)
    d = np.max(np.abs(s - v))
    if Vval(s, v, lam) >= thr:
        bad += 1
check("N5 every point with d<delta_* has V<threshold", bad == 0, "violations %d" % bad)
# sharpness: any delta>delta_* admits ball points at or above threshold
bad = 0
for k in range(200):
    delta = delta_star * (1.0 + 10.0**np.random.uniform(-6, 0))
    Sup = lam * delta**2 * (2 * v + delta)**2
    if not (Sup >= thr * (1 - 1e-12)):
        bad += 1
check("N5 radius is largest possible (radial point (v+delta) reaches sup>=thr)", bad == 0, "bad %d" % bad)

# ---------- N6 volume bound ----------
# lattice field over R = [0,1]^4 toy: sigma fields; one measure cell volume
Npts = 40000
volR = 1.0
dcell = volR / Npts
v, lam = 1.5, 1.1
thr = lam * v**4 / 4.0
s1 = v * (1.0 + 0.02 * np.random.randn(Npts))     # fluctuating vacuum
s2 = v * (1.0 + 0.02 * np.random.randn(Npts))
s3 = v * (1.0 + 0.02 * np.random.randn(Npts))
s4 = v * (1.0 + 0.02 * np.random.randn(Npts))
cell = np.zeros((Npts, 4), dtype=bool)
idx = np.random.rand(Npts) < 0.05                  # 5% defect patch candidates
cell[idx, 0] = True                                # sigma_1 -> 0 on defect cells
S = np.stack([np.where(cell[:, j], 0.0, [s1, s2, s3, s4][j] * 1.0) for j in range(4)], axis=1)
Vf = (lam / 4.0) * np.sum((S**2 - v**2)**2, axis=1)
EV = np.sum(Vf) * dcell
badvol = np.sum(Vf >= thr) * dcell
check("N6 Markov: mu{V>=thr} <= 4 E_V/(lambda v^4)", badvol <= 4 * EV / (lam * v**4) + 1e-12,
      "badvol %.6f bound %.6f" % (badvol, 4 * EV / (lam * v**4)))
# degenerate set is inside {V>=thr}: mu{det e=0} <= mu{V>=thr}
detzero = np.sum(np.any(S == 0.0, axis=1)) * dcell
check("N6 degenerate set <= volume bound (contains test)", detzero <= badvol + 1e-12,
      "detzero %.6f" % detzero)
# equality case: uniform (0,v,v,v) patch of measure f: E_V = f thr, bound = f
for f in [0.01, 0.1, 0.37, 1.0]:
    EV2 = f * thr
    check("N6 equality case f=%.2f: 4 E_V/(lambda v^4) == f" % f,
          abs(4 * EV2 / (lam * v**4) - f) < 1e-12,
          "bound %.15f" % (4 * EV2 / (lam * v**4)))
# refinement: mu{|det e| < (1-2sqrt(eps/lambda)/v^2)^2} <= E_V/eps
worst = 0.0
for eps in np.linspace(0.05 * thr, 0.99 * thr, 20):
    dete = np.prod(S, axis=1) / v**4
    lower = (1 - 2 * np.sqrt(eps / lam) / v**2)**2
    mu_bad = np.sum(dete < lower) * dcell
    EV_bad = EV
    worst = max(worst, mu_bad - EV_bad / eps)
check("N6 refinement mu{|det e|<bound(eps)} <= E_V/eps over 20 eps", worst <= 1e-12,
      "max excess %.2e" % worst)

# ---------- N7 identity of the two |det e| bounds ----------
es, vs, ls = sp.symbols('epsilon v lambda', positive=True)
d_eps = vs - sp.sqrt(vs**2 - 2 * sp.sqrt(es / ls))
mine = (1 - d_eps / vs)**4
theirs = (1 - sp.sqrt(4 * es / ls) / vs**2)**2
check("N7 (1-d_eps/v)^4 == (1-sqrt(4eps/lambda)/v^2)^2",
      sp.simplify(mine - theirs) == 0, "sympy simplify -> 0")

# ---------- N8 quadratic consistency with recorded 2 lambda v^4 ----------
# recorded (appH L2160, live): V^(2)(d=vB)=lambda v^2 Tr H^2 = 2 lambda v^4 for B=E01+E10.
# Our estimate at Phi=v(I+tB): sigma = v|1+-t|,v,v: d=vt; check bracket lo<=V<=hi.
v, lam, t = 1.0, 1.0, 1e-4
s = np.array([v * (1 + t), v * (1 - t), v, v])
Vm = Vval(s, v, lam)
d = v * t
lo = (lam / 4.0) * d * d * (2 * v - d)**2
hi = lam * d * d * (2 * v + d)**2
coef = Vm / t**2
check("N8 boost direction: 2 lambda v^4 t^2 coefficient, bracketed by estimate",
      lo <= Vm <= hi and abs(coef - 2 * lam * v**4) < 1e-3, "coef %.6f" % coef)
# single-sigma and uniform radial: exact quadratic identities (limits give the
# sharp quadratic coefficients lambda v^2 and 4 lambda v^2 of the two-sided bound):
dd = 1e-4
val_s = Vval(np.array([v - dd, v, v, v]), v, lam)
val_u = Vval(np.full(4, v + dd), v, lam)
check("N8 single-sigma exact identity V = (lambda/4) dd^2 (2v-dd)^2",
      abs(val_s - (lam / 4.0) * dd**2 * (2 * v - dd)**2) < 1e-14,
      "V/dd^2 = %.9f -> lambda v^2 = %.1f" % (val_s / dd**2, lam * v**2))
check("N8 uniform radial exact identity V = lambda dd^2 (2v+dd)^2",
      abs(val_u - lam * dd**2 * (2 * v + dd)**2) < 1e-14,
      "V/dd^2 = %.9f -> 4 lambda v^2 = %.1f" % (val_u / dd**2, 4 * lam * v**2))

# ---------- S1-S3 symbolic ----------
dvar, vv, ll = sp.symbols('d v lambda', positive=True)
q = sp.sqrt(ll) * dvar * (2 * vv - dvar) / 2      # sqrt(lambda) d(2v-d)/2: V_lo = q^2/... helper
sol = sp.solve(sp.Eq(dvar * (2 * vv - dvar), 2 * sp.sqrt(es / ll)), dvar)
dexpr = [s0 for s0 in sol if s0.subs({vv: 2, ll: 1, es: sp.Rational(1, 2)}) < 2][0]
ok_s1 = True
for _ in range(50):
    subd = {vv: float(np.random.uniform(1.0, 3.0)), ll: float(np.random.uniform(0.5, 2.0))}
    subd[es] = float(np.random.uniform(0.02, 0.999) * subd[vv]**4 * subd[ll] / 4.0)
    a = complex(dexpr.subs(subd)); b = complex((vv - sp.sqrt(vv**2 - 2 * sp.sqrt(es / ll))).subs(subd))
    if abs(a - b) > 1e-9:
        ok_s1 = False
check("S1 d_eps = v - sqrt(v^2 - 2 sqrt(eps/lambda)) is the small root (50 numeric pts)",
      ok_s1, "sympy solve-root equals closed form")
dstar = (sp.sqrt(6) - 2) * vv / 2
check("S2 delta_*(2 v + delta_*) = v^2/2", sp.simplify(dstar * (2 * vv + dstar) - vv**2 / 2) == 0, "")
check("S3 delta_* = v(sqrt(3/2)-1)", sp.simplify(dstar - vv * (sp.sqrt(sp.Rational(3, 2)) - 1)) == 0, "")
tau = sp.symbols('tau')
series_lo = sp.series((ll / 4) * ((vv + tau)**2 - vv**2)**2, tau, 0, 3).removeO()
check("S4 single-deviation series (lambda/4)((v+tau)^2-v^2)^2 = lambda v^2 tau^2 + O(tau^3)",
      sp.simplify(series_lo - ll * vv**2 * tau**2) == sp.expand(series_lo - ll * vv**2 * tau**2).subs(tau, 0) and
      sp.expand(series_lo).coeff(tau, 2) == ll * vv**2, "tau^2 coeff = lambda v^2")

print("----")
print("PASS %d FAIL %d" % (PASS, FAIL))
print("ALL CHECKS DONE 116" if FAIL == 0 else "CHECKS FAILED 116")
raise SystemExit(0 if FAIL == 0 else 1)
