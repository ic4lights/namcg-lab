"""
065 s2: the cap block of a linearly deformed fuzzy sphere X^a = A^a_b J^b (N-dim irrep of su(2)).

Theta = spectral projector of n.J onto its M largest eigenvalues (n a unit vector). Checks, exactly at finite N:
 (a) every X^a_{SS'} = Theta X^a (1-Theta) is supported on one common rank-one matrix unit |u)(v|,
     u = eigenvector M-1, v = eigenvector M (0-based, eigenvalues in decreasing order);
 (b) s^2 := sum_a ||X^a_{SS'}||_HS^2 = (1/4) M (N-M) tr(A P_n A^T), P_n = 1 - n n^T,
     and tr(A P_n A^T) = sigma_1^2 + sigma_2^2, the singular values of A restricted to the plane n^perp.
Poisson-limit comparison (exact for the ellipse family): with M(N-M) -> (N sin(theta)/2)^2, the image of the
boundary circle of the cap under x = (N/2) A omega is an ellipse with semi-axes (N/2) sin(theta) sigma_i, and
 (c) s^2 = (1/4pi) oint |d x/d phi|^2 d phi (phi = rotation angle about n, the Hamiltonian angle of n.x);
 (d) its target-space perimeter P obeys P <= 2 sqrt(2) pi s, with equality iff sigma_1 = sigma_2.
Output to stdout only.
"""
import numpy as np
from scipy.special import ellipe

rng = np.random.default_rng(65002)

def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]

def check(N, M, A, n):
    J = su2(N)
    nJ = sum(n[k] * J[k] for k in range(3))
    w, V = np.linalg.eigh(nJ)
    V = V[:, ::-1]; w = w[::-1]
    Jr = [V.conj().T @ Jk @ V for Jk in J]          # rotated basis: n.J diagonal, decreasing
    X = [sum(A[a, b] * Jr[b] for b in range(3)) for a in range(3)]
    blocks = [Xa[:M, M:] for Xa in X]
    # (a) support: only entry (M-1, 0) of the S x S' block, i.e. matrix unit |M-1)(M|
    off = 0.0
    for B in blocks:
        Bm = B.copy(); Bm[M - 1, 0] = 0
        off = max(off, np.abs(Bm).max())
    s2 = sum(np.sum(np.abs(B) ** 2) for B in blocks)
    Pn = np.eye(3) - np.outer(n, n)
    pred = 0.25 * M * (N - M) * np.trace(A @ Pn @ A.T)
    e1 = np.linalg.svd(Pn)[0][:, :2]                 # orthonormal basis of n^perp
    sig = np.linalg.svd(A @ e1, compute_uv=False)
    return off, s2, pred, sig

worst_off = 0.0; worst_rel = 0.0
for N in (2, 5, 12, 33, 80):
    for M in sorted({1, N // 2, N - 1}):
        for trial in range(4):
            A = rng.normal(size=(3, 3))
            n = rng.normal(size=3); n /= np.linalg.norm(n)
            off, s2, pred, sig = check(N, M, A, n)
            worst_off = max(worst_off, off / max(1, np.sqrt(s2)))
            worst_rel = max(worst_rel, abs(s2 - pred) / pred)
            assert abs(np.sum(sig ** 2) - np.trace(A @ (np.eye(3) - np.outer(n, n)) @ A.T)) < 1e-9 * np.sum(sig ** 2)
print('(a) entries of X_SS\' outside the single matrix unit |M-1)(M|: max %.2e (relative to s)' % worst_off)
print('(b) s^2 vs (1/4) M (N-M) tr(A P_n A^T): max rel. error %.2e' % worst_rel)
assert worst_off < 1e-10 and worst_rel < 1e-10

# (c), (d): Poisson-limit ellipse comparison
def perimeter(a, b):
    a, b = max(a, b), min(a, b)
    return 4 * a * ellipe(1 - (b / a) ** 2)

print('(c)/(d) sigma1 sigma2 | s^2/(1/4pi oint|x_phi|^2) | 2 sqrt2 pi s / P  (round value 1)')
for (s1v, s2v) in [(1, 1), (1, 0.9), (1, 0.5), (1, 0.2), (2, 0.01)]:
    th = 0.7; N = 1000.0
    R = N / 2 * np.sin(th)
    phi = np.linspace(0, 2 * np.pi, 200001)
    dx = np.stack([-R * s1v * np.sin(phi), R * s2v * np.cos(phi)])
    dirich = np.trapezoid(np.sum(dx ** 2, axis=0), phi) / (4 * np.pi)
    s = np.sqrt((N * np.sin(th) / 2) ** 2 / 4 * (s1v ** 2 + s2v ** 2))
    P = R * perimeter(s1v, s2v)
    print('   %.2f %.2f | %.12f | %.6f' % (s1v, s2v, s ** 2 / dirich, 2 * np.sqrt(2) * np.pi * s / P))
    assert abs(s ** 2 / dirich - 1) < 1e-9 and 2 * np.sqrt(2) * np.pi * s / P >= 1 - 1e-12
print('PASS s2')
