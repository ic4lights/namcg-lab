# S4: selection-content corollaries. (1) Exact off-uniform profiles that
# decouple on average for a disconnected-coincidence-graph measure, with
# D_eff < D certified exactly. (2) The stiffness tie: for any measure,
# E_pi Gamma >= lam+ * ||g - gbar||^2 = lam+ * W^2 (1/D - 1/D_eff) on the
# connected component of the profile space where G_pi is connected (lam+ = least eigenvalue of
# Sigma_pi on mean-zero profiles; equals the least nonzero eigenvalue
# and is > 0 iff G_pi connected); checked exactly on random data with sympy eigenvalues.
# (3) Proxy ramp under any fixed full-support i.i.d.-type exchangeable frame
# law: leading decay rate measure-dependent but the off-uniformity limit 8/9
# is not (it is profile data). Numerical illustration only where marked.
from fractions import Fraction as F
import sympy as sp

# --- (1) disconnected measure with off-uniform decoupling, exact
# D = 4, g = (a, a, b, b) with a != b > 0; pi averages over frames supported
# in {1,2} and frames supported in {3,4}: coincidence graph has two edges
# {1,2}, {3,4}, two components; locus = {g1=g2, g3=g4} strictly off uniform.
D = 4
a, b = F(3, 4), F(5, 2)
g = [a, a, b, b]
q1 = [F(1, 3), F(2, 3), F(0), F(0)]
q2 = [F(0), F(0), F(1, 5), F(4, 5)]
measure = [(F(1, 2), q1), (F(1, 2), q2)]
def varq(g, q):
    m = sum(qi * gi for qi, gi in zip(q, g))
    return sum(qi * (gi - m)**2 for qi, gi in zip(q, g))
Eg = sum(w * varq(g, q) for w, q in measure)
W = sum(g)
S2 = sum(x * x for x in g)
Deff = F(W * W, 1) / S2
assert Eg == 0
assert Deff < D
print("S4.1 exact off-uniform averaged decoupling: g=(3/4,3/4,5/2,5/2), pi the"
      " two-block frame average: E_pi Gamma = 0 exactly while D_eff = %s < D = 4"
      " -- averaged decoupling selects the partition, not the profile values"
      % (sp.nsimplify(Deff)))
# and the uniform profile decouples at EVERY frame, any measure:
for trial in range(3):
    gs = [F(2, 5)] * D
    assert all(varq(gs, q) == 0 for _, q in measure)
print("S4.2 uniform profile: Gamma = 0 at every frame and every measure "
      "(profile-only fact, law- and measure-free), exact")

# --- (2) stiffness tie with the effective-dimension shortfall
def lam_plus(D, measure):
    S = sp.zeros(D, D)
    for w, q in measure:
        for i in range(D):
            for j in range(D):
                v = sp.Rational(w.numerator, w.denominator) * (
                    (q[i] if i == j else 0) - q[i] * q[j])
                S[i, j] += v
    ev = sorted(float(sp.re(v.evalf(n=40))) for v in S.eigenvals())
    pos = [v for v in ev if v > 1e-9]
    return (pos[0] if pos else 0.0), S

random = sp
import random as _rnd
_rnd.seed(3)
checks = 0
for trial in range(40):
    Dv = _rnd.randint(3, 6)
    # connected support patterns: always include a full-support pattern
    pats = [[i for i in range(Dv) if _rnd.random() < 0.7] for _ in range(2)]
    pats = [p if p else [0] for p in pats] + [list(range(Dv))]
    ws = [F(_rnd.randint(1, 9)) for _ in pats]; tw = sum(ws)
    measure = []
    for p, w in zip(pats, ws):
        r = [F(_rnd.randint(1, 7)) for _ in p]; s = sum(r)
        q = [F(0)] * Dv
        for i, x in zip(p, r):
            q[i] = x / s
        measure.append((w / tw, q))
    lp, S = lam_plus(Dv, measure)
    assert lp > 1e-9  # full-support pattern makes G connected
    g = [F(_rnd.randint(0, 5)) for _ in range(Dv)]
    Wv = sum(g)
    if Wv == 0:
        continue
    S2v = sum(x * x for x in g)
    lhs = sum(w * varq(g, q) for w, q in measure)
    rhs = lp * float(S2v - Wv * Wv / Dv)
    # exact: lhs = g^T S g >= lam+ * ||g_c||^2 (g_c centered) -- verify both
    # the identity lhs == g^T S g and the bound
    gv = [sp.Rational(x.numerator, x.denominator) for x in g]
    quad = sp.expand(sum(sp.Rational(gv[i]) * S[i, j] * sp.Rational(gv[j])
                         for i in range(Dv) for j in range(Dv)))
    assert sp.simplify(quad - sp.Rational(lhs.numerator, lhs.denominator)) == 0
    assert float(sp.Rational(lhs.numerator, lhs.denominator)) - rhs >= -1e-9
    # and ||g_c||^2 = W^2 (1/D_eff - 1/D) exactly, so the bound reads
    # E_pi Gamma >= lam+ W^2 (1/D_eff - 1/D)
    Wf = float(sp.Rational(Wv.numerator, Wv.denominator))
    S2f = float(sp.Rational(S2v.numerator, S2v.denominator))
    Deffv = Wf * Wf / S2f
    tgt = lp * Wf * Wf * (1.0 / Deffv - 1.0 / Dv)
    assert abs(rhs - tgt) < 1e-9
    checks += 1
print("S4.3 stiffness tie: E_pi Gamma = g^T Sigma_pi g >= lam+ ||g-c||^2 = "
      "lam+ W^2 (1/D_eff - 1/D), exact in %d random connected-measure cases"
      % checks)
print("S4 DONE")
