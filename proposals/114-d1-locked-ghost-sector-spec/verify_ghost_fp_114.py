# -*- coding: ascii -*-
# R114 verification: local-Lorentz Fadeev-Popov operator for the locked
# Presentation-B block is a fiber endomorphism; exact determinant identity,
# vacuum value, admissibility domain, class-function structure.
# Strategy: exact diagonal proof of the eigenvalue formula; exact weighted-
# degree-6 reduction of prod(r_i+r_j)/64 to elementary symmetric polynomials;
# exact integer-sampling check that detM(Phi) equals that polynomial for
# general Phi; both sides are polynomials of total degree 6 in the entries of
# Phi and agree on diagonalizable matrices (dense), so sampling supports the
# identity that the diagonal case proves.
# Run:  python -I -B verify_ghost_fp_114.py     (sympy; seed 114)
import sys, numpy as np, sympy as sp
from itertools import combinations

SEED = 114
def P(*a):
    print(*a); sys.stdout.flush()

P("R114 local-Lorentz FP-operator checks (sympy %s, numpy %s, seed %d)"
  % (sp.__version__, np.__version__, SEED))

eta = sp.diag(-1, 1, 1, 1)
PAIRS = [(i, j) for i in range(4) for j in range(i + 1, 4)]

def antisym6(M):
    return [sp.Rational(1, 2) * (M[i, j] - M[j, i]) for i, j in PAIRS]

def fp_matrix(Phi):
    # delta Phi = Phi*omega, omega = eta*a (so(3,1) generator), a antisym;
    # gauge fixing F := antisym(eta*Phi) (6 components). M = dF/da.
    a = sp.zeros(4, 4); s = {}
    for k, (i, j) in enumerate(PAIRS):
        s[k] = sp.Symbol("a%d" % k)
        a[i, j] = s[k]; a[j, i] = -s[k]
    B = eta * Phi * eta * a
    F = antisym6(B)
    return sp.Matrix([[sp.diff(F[k], s[m]) for m in range(6)] for k in range(6)])

# S1: general Phi; detM has polynomial entries, total degree <= 6
Phi = sp.Matrix(4, 4, lambda i, j: sp.Symbol("P%d%d" % (i, j)))
detM = sp.expand(fp_matrix(Phi).det())
deg = sp.Poly(detM, *Phi).total_degree()
P("S1 detM(Phi) polynomial, total degree %d (expect 6):" % deg, deg == 6)

# S2: exact diagonal case: detM = prod_{i<j} (r_i + r_j) / 64
r = list(sp.symbols("r0:4"))
prod2 = sp.expand(sp.Mul(*[sp.Rational(1, 2) * (r[i] + r[j]) for i, j in PAIRS]))
detM_D = sp.expand(fp_matrix(sp.diag(*r)).det())
P("S2 exact diag identity detM == prod(r_i+r_j)/64:", sp.expand(detM_D - prod2) == 0)

# S3: exact reduction of prod(r_i+r_j)/64 to elementary symmetric polys E_i
def eel(k):
    return sp.Add(*[sp.Mul(*[r[i] for i in c]) for c in combinations(range(4), k)])
mons = [(a1, a2, a3, a4) for a1 in range(7) for a2 in range(4)
        for a3 in range(3) for a4 in range(2)
        if a1 + 2 * a2 + 3 * a3 + 4 * a4 == 6]
E1, E2, E3, E4 = sp.symbols("E1 E2 E3 E4")
symE = {E1: eel(1), E2: eel(2), E3: eel(3), E4: eel(4)}
basisE = [sp.Mul(*[vE ** m[k] for k, vE in enumerate([E1, E2, E3, E4]) if m[k]])
          if any(m) else sp.Integer(1) for m in mons]
basis = [sp.expand(b.subs(symE)) for b in basisE]
q = [sp.Symbol("q%d" % i) for i in range(len(basis))]
expr = sp.expand(sum(q[i] * basis[i] for i in range(len(basis))) - prod2)
Pe = sp.Poly(expr, *r)
sol = sp.solve([Pe.coeff_monomial(m) for m in Pe.monoms()], q, dict=True)
P("S3a unique weighted-degree-6 reduction:", len(sol) == 1)
Pexpr = sp.factor(sp.expand(sum(sol[0][qq] * b for qq, b in zip(q, basisE))))
P("S3b prod(r_i+r_j)/64 =", Pexpr, "(in E_i = char-poly coefficients of Phi)")
# exact integer-sampling: detM(Phi) == Pexpr(E_i(Phi)) on general integer Phi
Eall = list(Phi)
fM = sp.lambdify(Eall, detM, modules=["math", "sympy"])
ch = Phi.charpoly(sp.Symbol("t")).all_coeffs()
Esub = {E1: sp.expand(-ch[1]), E2: sp.expand(ch[2]),
        E3: sp.expand(-ch[3]), E4: sp.expand(ch[4])}
fP = sp.lambdify(Eall, sp.expand(Pexpr.subs(Esub)), modules=["math", "sympy"])
rng = np.random.default_rng(SEED)
bad = 0
for _ in range(300):
    A = [int(x) for x in rng.integers(-6, 7, size=16)]
    if fM(*A) != fP(*A):
        bad += 1
P("S3c exact integer sampling, 300 general 4x4 Phi (seed 114), mismatches:", bad)

# S4: vacuum Phi = v*I
v = sp.symbols("v", positive=True)
P("S4 detM(v*I) == v**6:", sp.simplify(fp_matrix(v * sp.eye(4)).det() - v**6) == 0)

# S5: order-zero transformation law (infinitesimal): Lambda(x) = I + eps(x)*w0
eps = sp.symbols("eps")
d_eps = sp.symbols("epsprime")
w0 = eta * sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 2], [0, 0, -2, 0]])
gen = sp.simplify(w0.T * eta + eta * w0)
P("S5a w0 in so(3,1):", gen == sp.zeros(4, 4))
Ffin = antisym6(eta * Phi * (sp.eye(4) + eps * w0))
P("S5b F(Phi*Lambda) is linear in eps with Phi-only coefficients (order 0):",
  all(sp.simplify(f - f.subs(eps, 0) - eps * sp.diff(f, eps)) == 0 for f in Ffin))

# S6: admissibility: detM vanishes at an eta-orthogonal pi/2-rotation frame
th = sp.pi / 2
Rot = sp.Matrix([[1, 0, 0, 0],
                 [0, sp.cos(th), -sp.sin(th), 0],
                 [0, sp.sin(th), sp.cos(th), 0],
                 [0, 0, 0, 1]])
P("S6a Rot eta-orthogonal:", sp.simplify(Rot.T * eta * Rot - eta) == sp.zeros(4, 4),
  "| S6b detM(Rot) == 0:", sp.simplify(fp_matrix(Rot).det()) == 0)

# S7: not a function of det Phi (exact rational witness)
Dw = sp.diag(sp.Integer(2), sp.Rational(1, 2), 1, 1)
val = sp.nsimplify(fp_matrix(Dw).det())
P("S7 detM(diag(2,1/2,1,1)) =", val, "| det Phi = 1 | val != 1:", val != 1)

# S8: linear response at the vacuum. S1 proves detM is a polynomial of total
# degree 6 in the entries of Phi, so its derivative at v*I is a LINEAR function
# of H; checking it on the 16 matrix units E_ij is equivalent to the general
# statement. Matrix units keep entries in {0, 1, v, t}: the determinant stays
# cheap, unlike the general-H symbolic Poly.
tp = sp.symbols("t")
ok8 = True
for i in range(4):
    for j in range(4):
        Eij = sp.zeros(4, 4)
        Eij[i, j] = 1
        di = sp.expand(sp.Poly(fp_matrix(v * sp.eye(4) + tp * Eij).det(), tp)
                       .coeff_monomial(tp))
        want = sp.Rational(3, 2) * v**5 * (1 if i == j else 0)
        if sp.simplify(di - want) != 0:
            ok8 = False
P("S8 linear response d/dt detM(v*I+t*E_ij)|0 == (3/2) v^5 (E_ij) for all 16 i,j:", ok8)

# S9: float class-function spot check, 200 random Phi (seed 114)
fnum = sp.lambdify(list(Phi), detM, modules="numpy")
rng = np.random.default_rng(SEED)
mx = 0.0
for _ in range(200):
    A = rng.normal(size=(4, 4))
    ev = np.linalg.eigvals(A)
    p = np.prod([(ev[i] + ev[j]) / 2 for i, j in PAIRS])
    d = complex(fnum(*A.flatten()))
    mx = max(mx, abs(d - p) / max(1e-12, abs(p)))
P("S9 max rel err, 200 random Phi (seed 114): %.3e" % mx)
P("ALL CHECKS DONE")
