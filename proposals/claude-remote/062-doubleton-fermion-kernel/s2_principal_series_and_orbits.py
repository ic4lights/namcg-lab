"""
062 / s2: representation-theoretic inputs, checked independently.

 (i)  Casimirs of the SL(2,C) principal series in the realisation of Freidel-Livine hep-th/0205268, Eq. (6.3):
        (R(g) f)(z) = |bz+d|^(-2-2i rho) ((bz+d)/|bz+d|)^(2j) f((az+c)/(bz+d)),  g = [[a,b],[c,d]],
      i.e. weights alpha = -1 - i rho + j (in z) and beta = -1 - i rho - j (in zbar).
      The real generators J_k (rotations) and K_k (boosts) are computed as differential operators on a generic
      f(z, zbar) and J.J - K.K and J.K are compared with  k^2 - p^2 - 1  and  +-k p  (Martin-Dussaud
      1902.08439, Eq. (297): (K^2 - J^2) = p^2 - k^2 + 1, K.J = p k), with (p, k) = (rho, j).
      Also the left/right (holomorphic/antiholomorphic) Casimirs: 4 J_L^2 = (j - i rho)^2 - 1 etc.
 (ii) The kernel condition derived in the proposal: P = 0 and 1 + C4 = (A+1)^2 >= 0 with A real.
      On the principal series (p real, k in Z/2) this forces p = 0.  On the complementary series
      (k = 0, p = i r, 0 < |r| < 1) it can hold (excluded from L^2 by the Plancherel support, not by algebra).
 (iii) so(4,2), eta = diag(-1,1,1,1,1,-1): {M^{mu nu}, M^{mu 4} + s M^{mu 5}} (s = +-1) are Poincare subalgebras
      containing the so(3,1) of the member (vector representation, exact).
 (iv) Pairs of non-collinear future null vectors in R^{3,1}: the stabiliser in so(3,1) is one-dimensional and
      compact (rotation generator), the stabiliser of p acts transitively on {q null, future, p.q = -s}
      (rank of the orbit map), and the open set of such pairs has full measure.
"""
import sympy as sp, numpy as np, itertools
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

# ---------------- (i) principal series Casimirs ----------------
z, zb, t, rho = sp.symbols('z zb t rho')
j = sp.symbols('j')
f = sp.Function('f')
alpha = -1 - sp.I * rho + j
beta = -1 - sp.I * rho - j

# work with operators acting on an arbitrary function: implement as first-order differential operators
def gen_op(X):
    g = sp.eye(2) + t * X
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    conj = lambda e: sp.conjugate(e).subs(sp.conjugate(t), t)
    ac, bc, cc, dc = conj(a), conj(b), conj(c), conj(d)
    w = b * z + d; wb = bc * zb + dc
    mz = sp.diff((a * z + c) / w, t).subs(t, 0)
    mzb = sp.diff((ac * zb + cc) / wb, t).subs(t, 0)
    pref = sp.diff(w**alpha * wb**beta, t).subs(t, 0)
    pref = sp.simplify(pref)
    return lambda F: sp.expand(pref * F + mz * sp.diff(F, z) + mzb * sp.diff(F, zb))

sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
F = f(z, zb)
# Hermitian generators on the unitary representation: J_k = i * dR(i sigma_k / 2), K_k = i * dR(sigma_k / 2)
Jop = [lambda G, k=k: sp.I * gen_op(sp.I * sig[k] / 2)(G) for k in range(3)]
Kop = [lambda G, k=k: sp.I * gen_op(sig[k] / 2)(G) for k in range(3)]
JJ = sum(Jop[k](Jop[k](F)) for k in range(3))
KK = sum(Kop[k](Kop[k](F)) for k in range(3))
JK = sum(Jop[k](Kop[k](F)) for k in range(3))
c1 = sp.simplify(sp.expand(JJ - KK) / F)
c2 = sp.simplify(sp.expand(JK) / F)
log('(i) principal series in the Freidel-Livine realisation:')
log('    (J.J - K.K) f / f =', sp.factor(c1))
log('    (J.K) f / f       =', sp.factor(c2))
okc1 = sp.simplify(c1 - (j**2 - rho**2 - 1)) == 0
okc2 = sp.simplify(c2 - j * rho) == 0 or sp.simplify(c2 + j * rho) == 0
log('    equals k^2 - p^2 - 1 with (p,k) = (rho, j):', okc1, '; equals +- k p:', okc2)
assert okc1 and okc2
JL2 = sp.simplify((c1 - 2 * sp.I * c2) / 4); JR2 = sp.simplify((c1 + 2 * sp.I * c2) / 4)
log('    4 J_L^2 = C4 - 2i P =', sp.factor(sp.expand(4 * JL2)), ';  4 J_R^2 = C4 + 2i P =', sp.factor(sp.expand(4 * JR2)))
log('    [equal to (j -+ i rho)^2 - 1 up to the sign convention of P:', sp.simplify(4 * JL2 - ((j + sp.I * rho)**2 - 1)) == 0 or sp.simplify(4 * JL2 - ((j - sp.I * rho)**2 - 1)) == 0, ']')

# ---------------- (ii) the kernel condition on the unitary dual ----------------
p, k, A = sp.symbols('p k A', real=True)
c4 = k**2 - p**2 - 1; P = k * p
log('(ii) kernel condition: P = 0 and 1 + C4 = (A+1)^2, A real')
log('    principal series: 1 + C4 =', sp.expand(1 + c4), '; P =', P)
# case analysis: P = 0 means k = 0 or p = 0
log('    k = 0: 1 + C4 = -p^2 >= 0 forces p = 0;  p = 0: 1 + C4 = k^2 >= 0, any k (then A = -1 +- k).')
log('    => on the principal series the kernel condition holds only at p = 0 (a countable set of irreducibles).')
r = sp.symbols('r', real=True)
log('    complementary series (k = 0, p = i r, 0<|r|<1): 1 + C4 =', sp.expand((1 + c4).subs({k: 0, p: sp.I * r})), '>= 0, P = 0: the algebra alone does not exclude it;')
log('    it is excluded for HS(H_n) because the restriction lies in a multiple of the regular representation.')

# ---------------- (iii) Poincare subalgebras of so(4,2) containing M^{mu nu} ----------------
eta6 = np.diag([-1., 1, 1, 1, 1, -1])
def Mgen(A, B):
    X = np.zeros((6, 6), complex)
    # (M^{AB})^C_D = -i (eta^{AC} delta^B_D - eta^{BC} delta^A_D)  (vector representation)
    for C in range(6):
        for Dd in range(6):
            X[C, Dd] = -1j * (eta6[A, C] * (B == Dd) - eta6[B, C] * (A == Dd))
    return X
def comm(X, Y): return X @ Y - Y @ X
for s in (+1, -1):
    Pm = [Mgen(m, 4) + s * Mgen(m, 5) for m in range(4)]
    e1 = max(np.abs(comm(Pm[a], Pm[b])).max() for a in range(4) for b in range(4))
    # Lorentz action closes on P
    e2 = 0
    for a, b, m in itertools.product(range(4), repeat=3):
        Cm = comm(Mgen(a, b), Pm[m])
        # project on span of Pm: least squares
        Amat = np.array([x.ravel() for x in Pm]).T
        coef, *_ = np.linalg.lstsq(Amat, Cm.ravel(), rcond=None)
        e2 = max(e2, np.abs(Amat @ coef - Cm.ravel()).max())
    log(f'(iii) s={s:+d}: max |[P_mu,P_nu]| = {e1:.1e}; [M^(ab), P_mu] in span(P): residual {e2:.1e}')
    assert e1 < 1e-12 and e2 < 1e-12

# ---------------- (iv) stabiliser of a pair of null vectors ----------------
rng = np.random.default_rng(1)
eta4 = np.diag([-1., 1, 1, 1])
def lor_gens():
    G = []
    for a in range(4):
        for b in range(a + 1, 4):
            X = np.zeros((4, 4))
            X[a, b] = 1; X[b, a] = -1
            X = X @ eta4  # X^mu_nu = Omega^{mu rho} eta_{rho nu}, Omega antisymmetric
            G.append(X)
    return G
G = lor_gens()
def null_future():
    v = rng.normal(size=3); return np.array([np.linalg.norm(v), *v])
worst_dim = set(); compact = True; ranks = set()
for trial in range(200):
    pv, qv = null_future(), null_future()
    Amat = np.array([np.concatenate([X @ pv, X @ qv]) for X in G]).T
    sv = np.linalg.svd(Amat, compute_uv=False)
    kdim = int(np.sum(sv < 1e-9 * sv.max()))
    worst_dim.add(kdim)
    _, _, Vt = np.linalg.svd(Amat)
    Y = sum(c * X for c, X in zip(Vt[-1], G))
    ev = np.linalg.eigvals(Y)
    if np.abs(ev.real).max() > 1e-8 * np.abs(ev).max():
        compact = False
    # transitivity of Stab(p) on {q null future, p.q = -s}: tangent rank of q -> X q for X in stab(p) is 2
    Ap = np.array([X @ pv for X in G]).T
    _, svp, Vtp = np.linalg.svd(Ap)
    stab_p = [sum(c * X for c, X in zip(Vtp[i], G)) for i in range(len(G)) if i >= np.sum(svp > 1e-9 * svp.max())]
    Q = np.array([X @ qv for X in stab_p]).T
    ranks.add(int(np.linalg.matrix_rank(Q, tol=1e-9)))
log('(iv) random non-collinear future null pairs (200): stabiliser dimension in so(3,1):', sorted(worst_dim),
    '; stabiliser generator has purely imaginary eigenvalues (compact):', compact,
    '; dim stab(p) = 3, rank of its orbit map at q:', sorted(ranks), '(= dim of the level set {q: q^2=0, p.q=-s} = 2)')
assert worst_dim == {1} and compact and ranks == {2}
open(__file__.replace('.py', '.out.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
