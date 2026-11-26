# s1: stationary-kernel identity for the frame-averaged decoupling functional
# Q_pi[g] = E_pi Gamma = g^T Sigma_pi g, Sigma_pi = E_pi(diag(q) - q q^T).
# Exact arithmetic (sympy/Fraction) + one deterministic Monte-Carlo Haar check.
# Run: python -I s1_stationary_kernel.py   (deterministic; seed 88)
import sys, random
from fractions import Fraction as F
import sympy as sp

def sigma_finite(law):  # law = [(weight Fractions, [q_i] Fractions, sum q_i = 1)]
    D = len(law[0][1]); M = sp.Matrix.zeros(D, D)
    for w, q in law:
        wq = sp.Rational(w.numerator, w.denominator)
        qv = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in q])
        M += wq * (sp.diag(*qv) - qv * qv.T)
    return M

def coincidence_graph(law, D):  # edge (i,j) iff positive-weight frame has q_i q_j > 0
    adj = {i: set() for i in range(D)}
    for w, q in law:
        if w <= 0: continue
        supp = [i for i in range(D) if q[i] > 0]
        for a in supp:
            for b in supp:
                if a != b: adj[a].add(b)
    comps = []; seen = set()
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
    print("%-46s %s %s" % (name, "OK" if cond else "FAIL", extra)); ok = ok and cond

D = 4
law = [(F(1, 2), [F(1, 2), F(1, 2), F(0), F(0)]), (F(1, 2), [F(0), F(0), F(1, 2), F(1, 2)])]
S = sigma_finite(law)
g = sp.Matrix(sp.symbols("g0:%d" % D))

# (1) Sigma annihilates constants and 1^T Sigma g = 0 identically (forces lambda = 0)
chk("sigma annihilates constants", (S * sp.ones(D, 1)) == sp.Matrix.zeros(D, 1))
chk("one^T Sigma g vanishes identically", sp.expand((sp.ones(1, D) * S * g)[0]) == 0)

# (2) kernel = piecewise constants on coincidence-graph components (several laws)
laws = {
  "two-block-087": (D, law),
  "chain123+45+14": (6, [(F(1, 3), [F(1, 2), F(1, 2), F(0), F(0), F(0), F(0)]),
                          (F(1, 3), [F(0), F(1, 2), F(1, 2), F(0), F(0), F(0)]),
                          (F(1, 6), [F(0), F(0), F(0), F(1, 2), F(1, 2), F(0)]),
                          (F(1, 6), [F(1, 2), F(0), F(0), F(1, 2), F(0), F(0)])]),
  "vertices-0": (4, [(F(1, 2), [F(1), F(0), F(0), F(0)]), (F(1, 2), [F(0), F(1), F(0), F(0)])]),
  "full-support": (4, [(F(1, 2), [F(5, 8), F(1, 8), F(1, 8), F(1, 8)]),
                        (F(1, 2), [F(0), F(1, 3), F(1, 3), F(1, 3)])]),
}
for nm, (d, L) in laws.items():
    M = sigma_finite(L); comps = coincidence_graph(L, d)
    chk("kernel=piecewise %s" % nm, same_span(M.nullspace(), piecewise_basis(comps, d)),
        "comps=%s rank=%d" % (comps, M.rank()))

# (3) Lagrange system  2 S g = lambda 1,  sum g = W  ==>  lambda = 0 on every solution.
# Solved as an exact linear system in (g, lambda) via linsolve; lambda is the last unknown.
W = F(7, 3)
A = sp.Matrix.hstack(2 * S, -sp.ones(D, 1))
A = sp.Matrix.vstack(A, sp.Matrix([[1] * D + [0]]))
b = sp.Matrix([0] * D + [sp.Rational(W.numerator, W.denominator)])
solset = sp.linsolve((A, b))
lam_ok = all(row[D] == 0 for row in solset)
chk("lagrange forces lambda=0 (two-block)", lam_ok, "solset dim in (g,lambda): %s" % len(solset.args))
# every solution must satisfy S g = 0 and be piecewise constant
sg_ok = True; pw_ok = True
for row in solset.args:
    gv = sp.Matrix(list(row[:D]))
    sg_ok = sg_ok and (S * gv == sp.Matrix.zeros(D, 1))
    pw_ok = pw_ok and (gv[0] == gv[1] and gv[2] == gv[3])
chk("lagrange solutions: Sg=0", sg_ok)
chk("lagrange solutions piecewise constant", pw_ok)

# (4) off-kernel mean-zero displacement: Q > 0 and S g != 0 (exact)
r = sp.Matrix([F(1, 4), F(-1, 4), F(0), 0])
Q = sp.expand((r.T * S * r)[0])
chk("mean-zero off-kernel: Q>0 and Sg!=0", Q > 0 and (S * r) != sp.Matrix.zeros(D, 1), "Q=%s" % Q)

# (5) Haar covariance: Dirichlet(1) moments reproduce Sigma = (I - J/D)/(D+1) exactly
for d in (3, 4, 5):
    Sh = sp.Matrix([[(sp.Rational(1, d) - sp.Rational(2, d * (d + 1))) if i == j
                     else -sp.Rational(1, d * (d + 1)) for j in range(d)] for i in range(d)])
    target = (sp.eye(d) - sp.ones(d, d) / d) / sp.Rational(d + 1)
    chk("haar sigma exact D=%d" % d, sp.simplify(Sh - target) == sp.Matrix.zeros(d, d))

# (6) deterministic Monte-Carlo Haar frame check (complex gaussian -> |u|^2 Dirichlet(1))
random.seed(88)
d = 4; N = 200000
acc = [[0.0 for _ in range(d)] for _ in range(d)]
for _ in range(N):
    z = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(d)]
    nrm = sum(zi.real ** 2 + zi.imag ** 2 for zi in z)
    q = [(zi.real ** 2 + zi.imag ** 2) / nrm for zi in z]
    for i in range(d):
        for j in range(d):
            acc[i][j] += (q[i] if i == j else 0.0) - q[i] * q[j]
target = [[((1.0 if i == j else 0.0) - 1.0 / d) / (d + 1) for j in range(d)] for i in range(d)]
err = max(abs(acc[i][j] / N - target[i][j]) for i in range(d) for j in range(d))
chk("MC haar sigma within 3e-3 (N=2e5, seed 88)", err < 3e-3, "maxerr=%.2e" % err)

print("s1 overall", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
