# s3: what an extra term R in F = Q_pi + R can and cannot do at fixed weight.
# (1) any C^1 permutation-symmetric R has all partials equal at the uniform profile
#     => uniform stays stationary for Q + R; (2) if F is strictly convex on the slice,
#     the stationary profile is UNIQUE and equals the uniform profile; (3) an asymmetric
#     convex addend yields a unique non-uniform stationary profile (exact solve);
#     (4) a symmetric non-convex addend yields a degenerate orbit of minimizers
#     (permutation partners), so the functional alone does not select one.
# All terms R here are SUPPLIED illustrations (not core content). Deterministic.
import sys
from fractions import Fraction as F
import sympy as sp
import numpy as np

ok = True
def chk(name, cond, extra=""):
    global ok
    print("%-52s %s %s" % (name, "OK" if cond else "FAIL", extra)); ok = ok and cond

D = 4
u = sp.symbols("u", real=True)
g = sp.symbols("g0:%d" % D)

# (1) symmetric R: all partials equal at the uniform profile (exact, several R)
def sym_polys(D):
    e2 = sum(g[i] * g[j] for i in range(D) for j in range(i + 1, D))
    return {"sum4": sum(x ** 4 for x in g),
            "sq2": (sum(x ** 2 for x in g)) ** 2,
            "pairdiff4": sum((g[i] - g[j]) ** 4 for i in range(D) for j in range(i + 1, D)),
            "e2sq": e2 ** 2}
for nm, R in sym_polys(D).items():
    subs = {gi: u for gi in g}
    dif = [sp.expand((sp.diff(R, g[i]) - sp.diff(R, g[j])).subs(subs))
           for i in range(D) for j in range(D)]
    chk("symmetric R: equal partials at uniform (%s)" % nm, all(x == 0 for x in dif))

# Haar-type Sigma (sigma = 1): S = I - J/D on mean-zero; slice sum g = W
Sd = np.eye(D) - np.ones((D, D)) / D
Wd = 2.0
ubar = Wd / D

def proj_hess(H):
    d = H.shape[0]
    V = np.linalg.qr(np.eye(d) - np.ones((d, 1)) @ np.ones((1, d)) / d)[0][:, :d - 1]
    return np.linalg.eigvalsh(V.T @ H @ V)

# (2) F = Q + beta * sum(-ln g_i), beta > 0: strictly convex on the interior slice,
#     unique stationary profile = uniform; projected gradient descent from 3 starts.
beta = 0.3
rng = np.random.default_rng(88)
minw = np.inf
for it in range(4000):
    x = rng.random(D) * 2; x *= Wd / x.sum()
    H = 2 * Sd + beta * np.diag(1.0 / x ** 2)
    minw = min(minw, proj_hess(H).min())
chk("projected Hessian of Q - beta*sum ln g PD on slice (min eig over 4000 pts)",
    minw > 0, "min eig = %.3e" % minw)
for s0 in (np.array([1.4, 0.3, 0.2, 0.1]), np.array([0.1, 0.9, 0.9, 0.1]),
           np.array([0.55, 0.55, 0.05, 0.85])):
    gpt = s0 * (Wd / s0.sum())
    for _ in range(20000):
        grad = 2 * Sd @ gpt - beta / gpt
        gp = grad - grad.mean()
        gnew = gpt - 0.05 * gp
        gnew = np.clip(gnew, 1e-12, None); gnew *= Wd / gnew.sum()
        if np.max(np.abs(gnew - gpt)) < 1e-14: gpt = gnew; break
        gpt = gnew
    chk("projected gradient flow -> uniform (start %s)" % str(list(s0)),
        np.max(np.abs(gpt - ubar)) < 1e-6, "|g-unif|=%.2e" % np.max(np.abs(gpt - ubar)))

# (3) asymmetric convex addend: unique stationary profile is NON-uniform (exact)
D3 = 3
S3 = sp.Matrix([[sp.Rational(1, 8), sp.Rational(-1, 8), 0],
                [sp.Rational(-1, 8), sp.Rational(1, 8), 0], [0, 0, 0]])  # law (1/2,1/2,0)
gam = sp.Rational(1, 4); wts = [0, 1, 2]
M3 = 2 * S3 + 2 * gam * sp.diag(*wts)
lam = sp.symbols("lam")
gk = sp.symbols("g0:3")
eqs = list(M3 * sp.Matrix(gk) - lam * sp.ones(3, 1)) + [sum(gk) - 3]
sol = sp.solve(eqs, list(gk) + [lam], dict=True)[0]
gv = [sp.nsimplify(sol[x]) for x in gk]
Hproj = np.array(M3, dtype=float)
pe = proj_hess(Hproj)
Qv = sp.nsimplify(sp.Matrix(gv).T.dot(S3 * sp.Matrix(gv)))
chk("asymmetric addend: projected Hessian PD (unique stationary)", pe.min() > 0,
    "min eig=%.4f" % pe.min())
chk("asymmetric addend: unique stationary is non-uniform and off the locus",
    gv[0] != gv[1] or gv[1] != gv[2], "g*=%s, Q(g*)=%s" % ([str(x) for x in gv], Qv))

# (4) symmetric NON-convex addend on the simplex: degenerate permutation orbit of minima
#     F = g^T (I - J/3) g - delta * sum g_i^4 on the simplex sum g = 1 (grid, exact indices)
delta, n = 3.0, 60
S3n = np.eye(3) - np.ones((3, 3)) / 3
best = np.inf; mins = []
for i in range(n + 1):
    for j in range(n + 1 - i):
        x = np.array([i, j, n - i - j], dtype=float) / n
        val = x @ S3n @ x - delta * (x ** 4).sum()
        if val < best - 1e-12: best, mins = val, [tuple(x)]
        elif abs(val - best) <= 1e-12: mins.append(tuple(x))
distinct = sorted(set(mins))
orbits = len(distinct)
is_perm_orbit = all(sorted(t) == sorted(distinct[0]) for t in distinct)
chk("symmetric non-convex addend: degenerate permutation orbit of minima",
    orbits > 1 and is_perm_orbit, "n_minima=%s, tuple=%s" % (orbits, distinct[0]))

print("s3 overall", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
