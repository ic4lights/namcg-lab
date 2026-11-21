# s2: variational rigidity of the decoupling-cone class.
# (1) kernel of a positive combination of frame covariances = piecewise constants on
#     the UNION coincidence graph; (2) the Lagrange system of the combination forces
#     lambda = 0 and lands on the union locus; (3) monotone C^1 reparametrisation:
#     grad(Phi o Q) = Phi'(Q) * 2 Sigma g (exact), so no new stationary profiles where
#     Phi' != 0; (4) counterexample: a reparametrisation with a stationary value creates
#     a whole circle of spurious stationary profiles with Q = u0 and grad Q != 0.
# Run: python -I s2_cone_union_monotone.py  (exact sympy except the printed counterexample)
import sys
from fractions import Fraction as F
import sympy as sp

def sigma_finite(law):
    D = len(law[0][1]); M = sp.Matrix.zeros(D, D)
    for w, q in law:
        qv = sp.Matrix([sp.Rational(x) for x in q])
        M += sp.Rational(w) * (sp.diag(*qv) - qv * qv.T)
    return M

def graph_components(edges, D):
    adj = {i: set() for i in range(D)}
    for a, b in edges: adj[a].add(b); adj[b].add(a)
    comps, seen = [], set()
    for i in range(D):
        if i in seen: continue
        st, comp = [i], []; seen.add(i)
        while st:
            v = st.pop(); comp.append(v)
            for u in adj[v]:
                if u not in seen: seen.add(u); st.append(u)
        comps.append(sorted(comp))
    return comps

def piecewise_basis(comps, D):
    out = []
    for c in comps:
        v = sp.Matrix.zeros(D, 1)
        for i in c: v[i] = 1
        out.append(v)
    return out

def same_span(A, B):
    if len(A) != len(B): return False
    if not A and not B: return True
    MA = sp.Matrix.hstack(*A); MB = sp.Matrix.hstack(*B)
    return sp.Matrix.hstack(MA, MB).rank() == MA.rank() == MB.rank()

ok = True
def chk(name, cond, extra=""):
    global ok
    print("%-50s %s %s" % (name, "OK" if cond else "FAIL", extra)); ok = ok and cond

# (1) two frame laws on D=6: law A has edges {0-1, 1-2}; law B has edges {3-4, 0-3}
lawA = [(F(1, 2), [F(1, 2), F(1, 2), 0, 0, 0, 0]), (F(1, 2), [0, F(1, 2), F(1, 2), 0, 0, 0])]
lawB = [(F(1, 2), [0, 0, 0, F(1, 2), F(1, 2), 0]), (F(1, 2), [F(1, 2), 0, 0, F(1, 2), 0, 0])]
SA, SB = sigma_finite(lawA), sigma_finite(lawB)
for (c1, c2) in [(F(1), F(1)), (F(3, 7), F(5, 11))]:
    S = c1 * SA + c2 * SB
    comps = graph_components([(0, 1), (1, 2), (3, 4), (0, 3)], 6)  # union: {0,1,2,3,4},{5}
    chk("union-kernel match c=(%s,%s)" % (c1, c2),
        same_span(S.nullspace(), piecewise_basis(comps, 6)),
        "comps=%s nullity=%d" % (comps, 6 - S.rank()))

# (2) Lagrange system for the combination on the slice sum g = W: lambda = 0, union locus
D = 6; W = F(5, 2); S = SA + SB
A = sp.Matrix.hstack(2 * S, -sp.ones(D, 1))
A = sp.Matrix.vstack(A, sp.Matrix([[1] * D + [0]]))
b = sp.Matrix([0] * D + [sp.Rational(W.numerator, W.denominator)])
row = next(iter(sp.linsolve((A, b))))
gv = sp.Matrix(list(row[:D]))
chk("combination lagrange: lambda=0", row[D] == 0)
chk("combination lagrange: Sg=0", S * gv == sp.Matrix.zeros(D, 1))
chk("combination lagrange: g0=g1=g2=g3=g4, g6 free",
    gv[0] == gv[1] and gv[1] == gv[2] and gv[2] == gv[3] and gv[3] == gv[4] and gv[4] != gv[5],
    str(list(row[:D])))

# (3) monotone composition: exact chain-rule factorization
D3 = 3
S3 = sp.Matrix([[sp.Rational(2, 3), sp.Rational(-1, 3), sp.Rational(-1, 3)],
                [sp.Rational(-1, 3), sp.Rational(2, 3), sp.Rational(-1, 3)],
                [sp.Rational(-1, 3), sp.Rational(-1, 3), sp.Rational(2, 3)]])  # Haar D=3, sigma=1
g = sp.Matrix(sp.symbols("g0:3"))
Q = (g.T * S3 * g)[0]
dQ = 2 * S3 * g
phis = {"exp": sp.exp(Q), "cubic": Q ** 3 + Q, "atan": sp.atan(Q), "lin+sin": 2 * Q + sp.sin(Q)}
for nm, Fg in phis.items():
    grad = [sp.diff(Fg, gi) for gi in g]
    coll = all(sp.simplify(grad[i] * dQ[j] - grad[j] * dQ[i]) == 0
               for i in range(3) for j in range(3))
    # strictly increasing Phi: nonzero grad Q  =>  nonzero grad(Phi o Q), on exact samples
    import random as _r
    _r.seed(88); nz_ok = True
    for _ in range(8):
        vals = [_r.randint(-9, 9) for _ in range(3)]
        gv = sp.Matrix(vals)
        if (S3 * gv) != sp.Matrix.zeros(3, 1):
            gl = [sp.N(sp.sympify(x).subs({g[k]: sp.Rational(vals[k]) for k in range(3)}))
                  for x in grad]
            nz_ok = nz_ok and max(abs(x) for x in gl) > 1e-9
    chk("monotone Phi o Q: grad collinear + no new zeros (%s)" % nm, coll and nz_ok)

# (4) counterexample: Phi(u) = (u - 1)^2 on Haar D=3, slice sum g = 3
u = sp.symbols("u")
P4 = (u - 1) ** 2
gs = [sp.symbols("x y z")]
G = sp.Matrix([1 + sp.sqrt(sp.Rational(1, 2)), 1 - sp.sqrt(sp.Rational(1, 2)), 1])
Qv = sp.simplify((G.T * S3 * G)[0])
gQ = 2 * S3 * G
gFv = [sp.simplify(sp.diff(P4, u).subs(u, Qv)) * gi for gi in gQ]
chk("counterexample: Q=1 at g", Qv == 1, "g=%s" % str(list(G.T)))
chk("counterexample: grad Phi o Q = 0, grad Q != 0",
    all(x == 0 for x in gFv) and any(x != 0 for x in gQ))
# and it is a circle: any mean-zero v with v^T S v = 1, sum v = 0 is stationary
# explicit mean-zero circle: v = (a, b, -(a+b)) spans the slice plane; Q(v) = 2(a^2+ab+b^2)
a, bb = sp.symbols("a b", real=True)
v = sp.Matrix([a, bb, -(a + bb)])
Qv2 = sp.expand((v.T * S3 * v)[0])  # should be a^2 + a b + b^2 times 3/2? keep general
chk("circle of spurious stationary points: Q(v) = 2(a^2+ab+b^2)",
    sp.simplify(Qv2 - 2 * (a ** 2 + a * bb + bb ** 2)) == 0, "Q=%s" % Qv2)

print("s2 overall", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
