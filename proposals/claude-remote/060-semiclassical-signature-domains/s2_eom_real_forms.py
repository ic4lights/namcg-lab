"""
060 / s2: exact Lie-algebra identity behind the equation of motion for four generators T^a = M^{a c0}.

Bracket convention of the manuscript / cp12_realisation (Hermitian generators):
  [M^{AB}, M^{CD}] = i( eta^{BC} M^{AD} - eta^{AC} M^{BD} - eta^{BD} M^{AC} + eta^{AD} M^{BC} ).
Defining representation (non-unitary for noncompact forms, which is irrelevant for a Lie-algebra identity):
  (M^{AB})^C_D = +i( eta^{AC} delta^B_D - eta^{BC} delta^A_D ).
(The identity is odd under M -> -M on both sides, so it does not depend on the sign of i in the bracket.)
Claim: for a symmetric 4x4 H on an index set S (c0 not in S),
  sum_{c,c' in S} H_{cc'} [T^c,[T^{c'},T^a]] = eta^{c0 c0} [ tr(eta_S^{-1} H) T^a - (eta_S^{-1} H)^a_b T^b ].
Hence [A^mu,[A_mu,A_nu]] = gamma A_nu (h0-contracted, A = L T, H = L^T h0 L) holds iff eta_S^{-1} H = c 1,
with gamma = 3 c eta^{c0 c0}.
Also: the six so(1,3) generators with the Euclidean sum satisfy sum_B [J_B,[J_B,J_A]] = 0 (2512.03161).
And: the Killing forms of so(4,2), so(4,1) are indefinite (no finite-dim Hermitian representation).
"""
import sympy as sp
import itertools

def gens(eta):
    n = len(eta)
    M = {}
    for A in range(n):
        for B in range(n):
            m = sp.zeros(n, n)
            for C in range(n):
                for D in range(n):
                    m[C, D] = sp.I*(eta[A]*(1 if (A == C) else 0)*(1 if B == D else 0)
                                     - eta[B]*(1 if B == C else 0)*(1 if A == D else 0))
            M[(A, B)] = m
    return M

def comm(X, Y):
    return X*Y - Y*X

def check_bracket(eta):
    M = gens(eta); n = len(eta); ok = True
    for A, B, C, D in itertools.product(range(n), repeat=4):
        lhs = comm(M[(A, B)], M[(C, D)])
        d = lambda i, j: eta[i] if i == j else 0
        rhs = sp.I*(d(B, C)*M[(A, D)] - d(A, C)*M[(B, D)] - d(B, D)*M[(A, C)] + d(A, D)*M[(B, C)])
        if sp.simplify(lhs - rhs) != sp.zeros(n, n):
            ok = False; break
    return ok

Hs = sp.symbols('h00 h01 h02 h03 h11 h12 h13 h22 h23 h33', real=True)
def Hmat():
    h00, h01, h02, h03, h11, h12, h13, h22, h23, h33 = Hs
    return sp.Matrix([[h00, h01, h02, h03], [h01, h11, h12, h13], [h02, h12, h22, h23], [h03, h13, h23, h33]])

def identity_check(eta, S, c0, label):
    M = gens(eta)
    T = [M[(a, c0)] for a in S]
    H = Hmat()
    etaS = sp.diag(*[eta[a] for a in S])
    P = etaS.inv()*H
    trP = P.trace()
    ok = True
    for ia in range(4):
        lhs = sp.zeros(len(eta), len(eta))
        for ic in range(4):
            for jc in range(4):
                lhs += H[ic, jc]*comm(T[ic], comm(T[jc], T[ia]))
        rhs = eta[c0]*(trP*T[ia] - sum((P[ia, b]*T[b] for b in range(4)), sp.zeros(len(eta), len(eta))))
        if sp.expand(lhs - rhs) != sp.zeros(len(eta), len(eta)):
            ok = False
    print(f"  {label}: identity holds for symbolic symmetric H: {ok};  eta^(c0c0) = {eta[c0]}")
    # proportional case
    c = sp.symbols('c', real=True)
    Hc = c*etaS
    lhs0 = sp.zeros(len(eta), len(eta))
    for ic in range(4):
        for jc in range(4):
            lhs0 += Hc[ic, jc]*comm(T[ic], comm(T[jc], T[0]))
    gam = sp.simplify((lhs0[[i for i in range(len(eta)**2) if T[0][i] != 0][0]]) / T[0][[i for i in range(len(eta)**2) if T[0][i] != 0][0]])
    print(f"     H = c eta_S  ->  box T^a = ({gam}) T^a  (expected 3 c eta^(c0c0) = {3*c*eta[c0]})")
    return ok

print("bracket convention reproduced by the defining representation:")
for name, eta in [("so(4,2)", [-1, 1, 1, 1, 1, -1]), ("so(6)", [1]*6), ("so(4,1)", [-1, 1, 1, 1, 1])]:
    print(f"  {name}: {check_bracket(eta)}")

print("identity:")
identity_check([-1, 1, 1, 1, 1, -1], [0, 1, 2, 3], 4, "so(4,2), T^a = M^{a4} (conjugate coordinates, manuscript class)")
identity_check([-1, 1, 1, 1, 1, -1], [0, 1, 2, 3], 5, "so(4,2), y^mu = M^{mu5} as matrices (base coordinates)")
identity_check([1]*6, [0, 1, 2, 3], 4, "so(6), T^a = M^{a4} (compact twin, CP^3 over S^4)")
identity_check([-1, 1, 1, 1, 1], [0, 1, 2, 3], 4, "so(4,1), T^a = M^{a4}")

print("solution condition: (tr P) 1 - P = lambda 1  <=>  P = c 1 (4x4, c = lambda/3):")
P = sp.Matrix(4, 4, sp.symbols('p0:16'))
lam = sp.symbols('lam')
sol = sp.solve(list(P.trace()*sp.eye(4) - P - lam*sp.eye(4)), list(P), dict=True)
print("  ", sol)

print("restrictions of a (9,1) form to 4-planes: possible inertia of L^T eta10 L (random L, rank 4):")
import numpy as np
rng = np.random.default_rng(1)
eta10 = np.diag([-1.] + [1.]*9)
seen = set()
for k in range(20000):
    L = rng.normal(size=(10, 4))
    if k % 3 == 0:
        L[0, :] = 0  # spacelike plane
    ev = np.linalg.eigvalsh(L.T @ eta10 @ L)
    seen.add((int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9))))
print("   (n_+, n_-) observed:", sorted(seen), " (n_- <= 1 always, Cauchy interlacing)")

print("Liao-Maeta check: six so(1,3) generators, Euclidean sum, sum_B [J_B,[J_B,J_A]]:")
eta4 = [1, -1, -1, -1]  # their h = diag(+,-,-,-) for so(1,3); sign of h irrelevant for the check
M = gens(eta4)
J = [M[(a, b)] for a in range(4) for b in range(a+1, 4)]
allzero = all(sp.expand(sum((comm(JB, comm(JB, JA)) for JB in J), sp.zeros(4, 4))) == sp.zeros(4, 4) for JA in J)
print("   all vanish:", allzero)

print("Killing forms (signature) -- a finite-dim Hermitian representation needs a compact image:")
for name, eta in [("so(4,2)", [-1, 1, 1, 1, 1, -1]), ("so(4,1)", [-1, 1, 1, 1, 1]), ("so(6)", [1]*6)]:
    Mg = gens(eta); n = len(eta)
    basis = [Mg[(A, B)] for A in range(n) for B in range(A+1, n)]
    # real Lie algebra elements are i*M (anti-Hermitian in unitary reps); Killing form via ad
    import numpy as np
    def vec(X):
        return np.array([complex(X[i, j]) for i in range(n) for j in range(n)])
    Bv = np.array([vec(sp.I*b) for b in basis]).T
    def ad(X):
        cols = []
        for b in basis:
            Y = comm(X, sp.I*b)
            coef, *_ = np.linalg.lstsq(Bv, vec(Y), rcond=None)
            cols.append(coef)
        return np.array(cols).T
    ads = [ad(sp.I*b) for b in basis]
    K = np.array([[np.trace(a1 @ a2).real for a2 in ads] for a1 in ads])
    ev = np.linalg.eigvalsh(K)
    print(f"   {name}: Killing form eigenvalue signs (+,-) = ({int(np.sum(ev > 1e-9))}, {int(np.sum(ev < -1e-9))})")
