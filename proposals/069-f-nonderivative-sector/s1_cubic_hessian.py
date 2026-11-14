"""s1: Hessian of the K part of eq:Smatrix with the cubic term, about X^i = chi J^i (fuzzy sphere S^2_N).

Action (K block, three Hermitian matrices, coupling 1/g^2 factored out):
    S[X] = -1/4 sum_{ij} Tr [X_i,X_j]^2 + (i c/3) eps_ijk Tr X_i X_j X_k
which is (1/3!) Tr(C_ijk [X^i,X^j] X^k) with C_ijk = i c eps_ijk.
Background Feynman gauge: add  -1/2 Tr (sum_i [X_i,a_i])^2  to the quadratic form.
Claim checked: the gauge-fixed Hessian is chi^2 [ L^2 - kappa S.L ],  kappa = 2 - c/chi,
with eigenvalues chi^2 (l(l+1) - kappa*l), chi^2 (l(l+1)+kappa), chi^2 (l(l+1)+kappa(l+1))
and multiplicities 2l+3, 2l+1, 2l-1  (l = 0..N-1; only the first tower at l=0).
"""
import numpy as np, itertools, sys

def spin(N):
    j = (N - 1) / 2
    m = np.arange(j, -j - 1, -1)
    Jp = np.zeros((N, N), complex)
    for a in range(N - 1):
        Jp[a, a + 1] = np.sqrt(j * (j + 1) - m[a + 1] * (m[a + 1] + 1))
    Jm = Jp.conj().T
    return [(Jp + Jm) / 2, (Jp - Jm) / 2j, np.diag(m).astype(complex)]

eps = np.zeros((3, 3, 3))
for a, b, c_ in itertools.permutations(range(3)):
    eps[a, b, c_] = np.linalg.det(np.eye(3)[[a, b, c_]])

def com(A, B): return A @ B - B @ A

def S(X, c):
    q = 0
    for i in range(3):
        for j in range(3):
            C = com(X[i], X[j]); q += -0.25 * np.trace(C @ C)
    cub = 0
    for i, j, k in itertools.permutations(range(3)):
        cub += eps[i, j, k] * np.trace(X[i] @ X[j] @ X[k])
    return (q + 1j * c / 3 * cub)

def herm_basis(N):
    B = []
    for a in range(N):
        E = np.zeros((N, N), complex); E[a, a] = 1; B.append(E)
    for a in range(N):
        for b in range(a + 1, N):
            E = np.zeros((N, N), complex); E[a, b] = E[b, a] = 1 / np.sqrt(2); B.append(E)
            E = np.zeros((N, N), complex); E[a, b] = -1j / np.sqrt(2); E[b, a] = 1j / np.sqrt(2); B.append(E)
    return B

def quad(X, a, c, gf=True):
    """exact second-order part of S(X+t a) in t (S is quartic), plus gauge fixing"""
    f = lambda t: S([X[i] + t * a[i] for i in range(3)], c)
    f2 = (-f(2) + 16 * f(1) - 30 * f(0) + 16 * f(-1) - f(-2)) / 24
    if gf:
        G = sum(com(X[i], a[i]) for i in range(3))
        f2 += -0.5 * np.trace(G @ G)
    return f2

def hessian(N, chi, c, gf=True):
    X = [chi * J for J in spin(N)]
    B = herm_basis(N)
    vecs = []
    for i in range(3):
        for E in B:
            a = [np.zeros((N, N), complex)] * 3
            a = list(a); a[i] = E; vecs.append(a)
    n = len(vecs)
    Q = np.zeros(n)
    imag = 0
    for p in range(n):
        v = quad(X, vecs[p], c, gf); Q[p] = v.real; imag = max(imag, abs(v.imag))
    H = np.zeros((n, n))
    for p in range(n):
        H[p, p] = 2 * Q[p]
        for q in range(p + 1, n):
            s = [vecs[p][i] + vecs[q][i] for i in range(3)]
            v = quad(X, s, c, gf); imag = max(imag, abs(v.imag))
            H[p, q] = H[q, p] = v.real - Q[p] - Q[q]
    return H, imag

def predicted(N, chi, c):
    kap = 2 - c / chi
    ev = []
    for l in range(N):
        ev += [chi**2 * (l * (l + 1) - kap * l)] * (2 * l + 3)
        if l >= 1:
            ev += [chi**2 * (l * (l + 1) + kap)] * (2 * l + 1)
            ev += [chi**2 * (l * (l + 1) + kap * (l + 1))] * (2 * l - 1)
    return np.sort(np.array(ev))

worst = 0
print("N  chi   c     kappa    max|eig - predicted|   max|Im Q|")
for N in (2, 3, 4, 5):
    for chi, c in ((1.0, 0.0), (1.0, 2.0), (0.7, 1.4), (0.7, 1.6355), (1.3, 0.9), (1.0, 3.0)):
        H, im = hessian(N, chi, c)
        ev = np.sort(np.linalg.eigvalsh(H))
        d = np.max(np.abs(ev - predicted(N, chi, c)))
        worst = max(worst, d, im)
        print(f"{N}  {chi:.2f}  {c:.4f}  {2-c/chi:+.4f}   {d:.2e}              {im:.1e}")
print("worst residual:", f"{worst:.2e}")

# stationarity of the tree action at chi = c/2 and gauge modes of the unfixed Hessian
print("\nfirst variation at chi=c/2 (max over basis directions), and unfixed Hessian on gauge modes:")
for N in (3, 4):
    c = 1.7; chi = c / 2
    X = [chi * J for J in spin(N)]
    B = herm_basis(N)
    g1 = 0
    for i in range(3):
        for E in B:
            a = [np.zeros((N, N), complex)] * 3; a = list(a); a[i] = E
            f = lambda t: S([X[k] + t * a[k] for k in range(3)], c)
            f1 = (f(-2) - 8 * f(-1) + 8 * f(1) - f(2)) / 12   # exact first-order part up to cubic contamination
            f3 = (f(2) - 2 * f(1) + 2 * f(-1) - f(-2)) / 12
            f1 = (f(1) - f(-1)) / 2 - f3
            g1 = max(g1, abs(f1))
    Hu, _ = hessian(N, chi, c, gf=False)
    # gauge direction a_i = i[X_i, lam]
    rng = np.random.default_rng(3)
    M = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); lam = M + M.conj().T
    a = [1j * com(X[i], lam) for i in range(3)]
    coords = np.array([np.trace(E.conj().T @ a[i]).real for i in range(3) for E in B])
    print(f"N={N}: |dS| = {g1:.2e};  |H_unfixed . gauge| / |gauge| = {np.linalg.norm(Hu @ coords)/np.linalg.norm(coords):.2e}")
    # off the stationary point the gauge direction is not null
    Hu2, _ = hessian(N, chi, 0.0, gf=False)
    print(f"      same with c=0 (not a solution): {np.linalg.norm(Hu2 @ coords)/np.linalg.norm(coords):.2e}")
    # value of the tree potential: abar(chi^4 - (2c/3) chi^3), abar = N(N^2-1)/8
    ab = N * (N * N - 1) / 8
    print(f"      S = {S(X,c).real:.10f}, abar(chi^4-(2c/3)chi^3) = {ab*(chi**4-(2*c/3)*chi**3):.10f}, Im S = {S(X,c).imag:.1e}")
print("\nPASS" if worst < 1e-9 else "\nFAIL")
