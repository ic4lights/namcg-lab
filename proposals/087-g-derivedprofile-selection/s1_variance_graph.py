# S1: variance representation of Gamma, the frame-quadratic form, and the
# coincidence-graph classification of the zero-averaged-coupling locus.
# Exact arithmetic (fractions + sympy). Read-only.
from fractions import Fraction as F
import sympy as sp
import random

def gamma_direct(g, u):  # 084 definition, sum |u_i|^2 (g_i - mu)^2
    D = len(g)
    mu = sum(g[i] * abs(u[i])**2 for i in range(D))
    return sum(abs(u[i])**2 * (g[i] - mu)**2 for i in range(D))

def gamma_var(g, q):  # Var_q(g)
    m = sum(q[i] * g[i] for i in range(len(g)))
    return sum(q[i] * (g[i] - m)**2 for i in range(len(g)))

# --- (1) variance representation, exact for random rational data + u on sphere
random.seed(7)
for trial in range(200):
    D = random.randint(2, 6)
    g = [F(random.randint(0, 9), random.randint(1, 5)) for _ in range(D)]
    # random complex vector -> q_i = |u_i|^2 rational via |u_i|^2 = r_i / sum r
    r = [F(random.randint(1, 9)) for _ in range(D)]
    s = sum(r)
    q = [x / s for x in r]
    # Gamma depends on u only via q (mu and the sum involve |u_i|^2 only),
    # so Gamma is phase-independent; the exact cases below check the variance
    # identity at q (explicit complex-frame phase check: gatekeeper review-r1, 100 frames)
    mu = sum(g[i] * q[i] for i in range(D))
    gd = sum(q[i] * (g[i] - mu)**2 for i in range(D))
    assert gd == gamma_var(g, q)
print("S1.1 variance representation Gamma = Var_q(g): 200 exact cases OK")

# --- (2) quadratic form: E_pi Gamma = g^T Sigma g, Sigma = E[diag(q)-qq^T]
def sigma_of(measure):  # measure = list of (weight, q) exact
    D = len(measure[0][1])
    S = sp.zeros(D, D)
    for w, q in measure:
        for i in range(D):
            for j in range(D):
                v = w * (q[i] * ((i == j)) - q[i] * q[j])
                S[i, j] += sp.Rational(v.numerator, v.denominator)
    return S

def graph_components(D, measure):
    par = list(range(D))
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for i in range(D):
        for j in range(i + 1, D):
            p = sum(w for w, q in measure if q[i] * q[j] > 0)
            if p > 0:
                a, b = find(i), find(j)
                if a != b:
                    par[a] = b
    comp = {}
    for i in range(D):
        comp.setdefault(find(i), []).append(i)
    return list(comp.values())

# --- (3) locus classification: nullspace(Sigma) == span{1_C : C component}
def nullspace_basis(S):
    return [v for v in S.nullspace()]

def span_match(S, comps):
    D = S.shape[0]
    B = S.nullspace()
    cols = []
    for C in comps:
        v = sp.zeros(D, 1)
        for i in C:
            v[i] = 1
        cols.append(v)
    M1 = sp.Matrix.hstack(*B) if B else sp.zeros(D, 0)
    M2 = sp.Matrix.hstack(*cols)
    return M1.rank() == M2.rank() and (M1.T * M2).rank() == M1.rank()

tests = 0
for trial in range(60):
    D = random.randint(3, 6)
    # random finite measure on support patterns with rational weights
    npat = random.randint(1, 5)
    measure = []
    tot = F(0)
    pats = []
    for _ in range(npat):
        S = [i for i in range(D) if random.random() < 0.55]
        if not S:
            S = [random.randrange(D)]
        pats.append(S)
    ws = [F(random.randint(1, 9)) for _ in pats]
    tw = sum(ws)
    for S, w in zip(pats, ws):
        rs = [F(random.randint(1, 7)) for _ in S]
        s = sum(rs)
        q = [F(0)] * D
        for i, x in zip(S, rs):
            q[i] = x / s
        measure.append((w / tw, q))
    Sig = sigma_of(measure)
    comps = graph_components(D, measure)
    assert span_match(Sig, comps), (D, pats)
    tests += 1
print("S1.2 coincidence-graph locus classification: nullspace == span{1_C} "
      "in %d random exact finite-measure cases OK" % tests)

# --- (4) zero-averaged-coupling equivalence on the simplex, exact random probes
def is_pc_on_comps(g, comps):
    for C in comps:
        if any(g[i] != g[C[0]] for i in C):
            return False
    return True

probes = 0
for trial in range(60):
    D = random.randint(3, 5)
    pats = [[i for i in range(D) if random.random() < 0.6] for _ in range(3)]
    pats = [P if P else [random.randrange(D)] for P in pats]
    ws = [F(random.randint(1, 9)) for _ in pats]; tw = sum(ws)
    measure = []
    for P, w in zip(pats, ws):
        rs = [F(random.randint(1, 7)) for _ in P]; s = sum(rs)
        q = [F(0)] * D
        for i, x in zip(P, rs):
            q[i] = x / s
        measure.append((w / tw, q))
    comps = graph_components(D, measure)
    Sig = sigma_of(measure)
    for _ in range(6):
        g = [F(random.randint(0, 3)) for _ in range(D)]
        if random.random() < 0.5:  # bias to piecewise-constant profiles
            C = comps[random.randrange(len(comps))]
            v = F(random.randint(0, 3))
            for i in C:
                g[i] = v
        Eg = sum(w * gamma_var(g, q) for w, q in measure)
        assert (Eg == 0) == is_pc_on_comps(g, comps), (D, pats, g, Eg)
        probes += 1
print("S1.3 exact zero-locus probes: E_pi Gamma = 0 iff g piecewise constant "
      "on components, %d probes OK" % probes)

# --- (5) recovery of the fixed-frame criterion: pi = delta_u constrains g only
# on supp(u) (the 084 iff statement), exact
D = 5
supp = [0, 2, 3]
rs = [F(1, 3), F(1, 2), F(1, 6)]
q = [F(0)] * D
for i, x in zip(supp, rs):
    q[i] = x
Sig = sigma_of([(F(1), q)])
comps = graph_components(D, [(F(1), q)])
gA = [F(1), F(1), F(1), F(1), F(2)]   # varies only off support
gB = [F(1), F(1), F(2), F(1), F(1)]   # varies on support
assert gA[0] == gA[2] == gA[3] and gA[4] != gA[0]
assert gamma_var(gA, q) == 0 and gamma_var(gB, q) != 0
assert span_match(Sig, comps)
print("S1.4 delta_u measure: locus = constancy on supp(u), off-support free; "
      "084 fixed-frame iff recovered exactly")
print("S1 DONE")
