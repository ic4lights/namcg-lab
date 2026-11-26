"""052 s2: the reflected pairing on a finite model of the flat point, with exact matrices.

Model: d = 2 Euclidean index, momenta on a symmetric grid, fibre the rotation group C4 of the square, H = C^(grid) x C^(C4),
X_a = -(u p)_a diagonal.  theta = diag(-1,1).  U_theta permutes the basis, (p,u) -> (theta p, theta u theta).
Checked exactly or to rounding:
  1. U X_a U^-1 = theta_a^c X_c; R[A]_a = theta_a^c U A_c U^-1 is a unitary involution of the Hilbert-Schmidt space preserving the full quartic action
     about X0 (random Hermitian A), so it is a symmetry of the matrix model, and [A,B]_theta = HS(A, R B) is a nondegenerate indefinite form.
  2. For the fibre-diagonal probes built from the mean momentum with a weight w(pbar) invariant under theta,
     HS(O_g, U O_h U^-1) = theta_g G_gh, with G_gh the positive moments of w.
  2b. Fibre probes built from the right translation: U R_k U^-1 = R_{-k}, so the combination odd in k has reflected pairing minus its norm.
  3. In the no-fibre model the map on kernels (Q, pbar) -> (theta Q, pbar) with polarisation sign, the unreflected-colour reflection, preserves the quadratic form Q^2 |A|^2 -
     (Q.A)^2 and does not preserve the quartic term of the action.
This is a check of the algebra at one finite model, not a proof.  Seeded.  Requires numpy only."""
import itertools
import numpy as np

rng = np.random.default_rng(52002)
theta = np.diag([-1.0, 1.0])
J = np.array([[0.0, -1.0], [1.0, 0.0]])
C4 = [np.linalg.matrix_power(J, k) for k in range(4)]
grid = list(itertools.product((-1, 0, 1), repeat=2))
basis = [(p, k) for p in grid for k in range(4)]
idx = {b: i for i, b in enumerate(basis)}
N = len(basis)
print('N =', N)


def Xa(a):
    return np.diag([-(C4[k] @ np.array(p))[a] for p, k in basis]).astype(complex)


X0 = [Xa(0), Xa(1)]


def fibre_conj(k):
    M = theta @ C4[k] @ theta
    for j in range(4):
        if np.allclose(M, C4[j]):
            return j
    raise AssertionError


U = np.zeros((N, N))
for (p, k), i in idx.items():
    q = tuple(int(v) for v in theta @ np.array(p))
    U[idx[(q, fibre_conj(k))], i] = 1.0
assert np.allclose(U @ U.T, np.eye(N)) and np.allclose(U @ U, np.eye(N))


def refl_op(O):
    return U @ O @ U.T


for a in range(2):
    rhs = sum(theta[a, c] * X0[c] for c in range(2))
    assert np.allclose(refl_op(X0[a]), rhs)
print('1a. U X_a U^-1 = theta_a^c X_c: ok')


def R(A):
    return [sum(theta[a, c] * refl_op(A[c]) for c in range(2)) for a in range(2)]


def herm():
    M = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    return (M + M.conj().T) / 2


def S(X):
    c = X[0] @ X[1] - X[1] @ X[0]
    return (-0.25 * 2 * np.trace(c @ c)).real


A = [0.1 * herm(), 0.1 * herm()]
B = [0.1 * herm(), 0.1 * herm()]
sA = S([X0[a] + A[a] for a in range(2)])
RA = R(A)
sR = S([X0[a] + RA[a] for a in range(2)])
print('1b. quartic action S[X0+A], S[X0+RA]:', sA, sR)
assert abs(sA - sR) < 1e-9 * abs(sA)
RRA = R(RA)
assert all(np.allclose(RRA[a], A[a]) for a in range(2))


def hs(A, B):
    return sum(np.trace(A[a].conj().T @ B[a]) for a in range(2))


assert abs(hs(R(A), R(B)) - hs(A, B)) < 1e-9
# signature of the reflected pairing on End(H)^2: the involution R has eigenvalues +1, -1
Rmat_trace = 0.0
for a in range(2):
    # trace of A -> theta_aa U A U^T on End(H): theta_aa (tr U)^2, U real
    Rmat_trace += theta[a, a] * np.trace(U) ** 2
total = 2 * N * N
print('1c. dim of End(H)^2 =', total, '; trace of R =', Rmat_trace, '; multiplicities +1, -1:', (total + Rmat_trace) / 2, (total - Rmat_trace) / 2)
assert (total + Rmat_trace) / 2 > 0 and (total - Rmat_trace) / 2 > 0

# 2. probes: fibre-diagonal, charge q (in the frame of the label), mean momentum
w = {p: np.exp(-0.5 * (p[0] ** 2 + p[1] ** 2)) for p in grid}


def probe(g, q=(0, 0)):
    """kernel between (p,k) and (p+q,k), coefficient pbar_g w(pbar)^(1/2); q = 0 used for the parity test, which fixes y-dependence."""
    O = np.zeros((N, N), dtype=complex)
    for (p, k), i in idx.items():
        pp = (p[0] + q[0], p[1] + q[1])
        if (pp, k) in idx:
            pbar = np.array(p, dtype=float) + np.array(q, dtype=float) / 2
            O[i, idx[(pp, k)]] = pbar[g] * np.exp(-0.25 * (pbar @ pbar))
    return O


G = np.array([[np.trace(probe(g).conj().T @ probe(h)).real for h in range(2)] for g in range(2)])
Gr = np.array([[np.trace(probe(g).conj().T @ refl_op(probe(h))).real for h in range(2)] for g in range(2)])
print('2. G_gh =\n', G, '\n   reflected pairing =\n', Gr, '\n   theta G =\n', theta @ G)
assert np.allclose(Gr, theta @ G)
assert np.all(np.linalg.eigvalsh(G) > 0)
assert Gr[0, 0] < 0 < Gr[1, 1]

# probes at q != 0 transverse to the reflected axis keep q under the reflection
O0 = probe(0, (0, 1))
O1 = probe(1, (0, 1))
print('   q=(0,1): HS(O_0, R O_0) / HS(O_0,O_0) =', np.trace(O0.conj().T @ refl_op(O0)).real / np.trace(O0.conj().T @ O0).real,
      '; HS(O_1, R O_1) / HS(O_1,O_1) =', np.trace(O1.conj().T @ refl_op(O1)).real / np.trace(O1.conj().T @ O1).real)
assert abs(np.trace(O0.conj().T @ refl_op(O0)).real / np.trace(O0.conj().T @ O0).real + 1) < 1e-12
assert abs(np.trace(O1.conj().T @ refl_op(O1)).real / np.trace(O1.conj().T @ O1).real - 1) < 1e-12

# 2b. fibre probes: right translation R_k of u; U R_k U^-1 = R_{-k}; the combination odd under k -> -k has negative reflected pairing
def right(k0):
    Rm = np.zeros((N, N))
    for (p, k), i in idx.items():
        Rm[idx[(p, (k + k0) % 4)], i] = 1.0
    return Rm


assert np.allclose(refl_op(right(1)), right(3))
Podd = (right(1) - right(3)) @ np.diag([np.exp(-0.25 * (np.array(p) @ np.array(p))) for p, k in basis])
Peven = (right(1) + right(3)) @ np.diag([np.exp(-0.25 * (np.array(p) @ np.array(p))) for p, k in basis])
print('2b. reflected pairing / norm, fibre probes: odd', np.trace(Podd.conj().T @ refl_op(Podd)).real / np.trace(Podd.conj().T @ Podd).real, ', even', np.trace(Peven.conj().T @ refl_op(Peven)).real / np.trace(Peven.conj().T @ Peven).real)
assert abs(np.trace(Podd.conj().T @ refl_op(Podd)).real / np.trace(Podd.conj().T @ Podd).real + 1) < 1e-12
assert abs(np.trace(Peven.conj().T @ refl_op(Peven)).real / np.trace(Peven.conj().T @ Peven).real - 1) < 1e-12

# 3. no-fibre model on a grid wide enough, unreflected-colour map defined where it stays on the grid
grid3 = list(itertools.product(range(-3, 4), repeat=2))
ix = {p: i for i, p in enumerate(grid3)}
M = len(grid3)
P0 = [np.diag([-p[a] for p in grid3]).astype(complex) for a in range(2)]


def kernel_map(A_a, sign):
    """(p1,p2) -> (pbar + theta Q / 2, pbar - theta Q / 2), with pbar = (p1+p2)/2, Q = p1-p2, sign theta_a; a kernel leaving the grid is set to zero."""
    out = np.zeros_like(A_a)
    for p1 in grid3:
        for p2 in grid3:
            Q = np.array(p1) - np.array(p2)
            pb = (np.array(p1) + np.array(p2)) / 2
            tQ = theta @ Q
            n1 = pb + tQ / 2
            n2 = pb - tQ / 2
            t1, t2 = tuple(int(round(v)) for v in n1), tuple(int(round(v)) for v in n2)
            if t1 in ix and t2 in ix and np.allclose(n1, t1) and np.allclose(n2, t2):
                out[ix[t1], ix[t2]] = sign * A_a[ix[p1], ix[p2]]
    return out


def sparse_herm(radius=2):
    """Hermitian kernels with support on the points within |p|_inf <= radius, for which the map stays on the grid."""
    Z = (rng.normal(size=(M, M)) + 1j * rng.normal(size=(M, M)))
    Z = (Z + Z.conj().T) / 2
    mask = np.array([[max(abs(v) for v in p1) <= radius and max(abs(v) for v in p2) <= radius for p2 in grid3] for p1 in grid3])
    return Z * mask


Aa = [sparse_herm(1), sparse_herm(1)]
Am = [kernel_map(Aa[0], -1.0), kernel_map(Aa[1], 1.0)]


def S2_form(A):
    """the quadratic form sum_{p1,p2} (Q.Q |A|^2 - |Q.A|^2) on kernels, Q = p1 - p2."""
    tot = 0.0
    for p1 in grid3:
        for p2 in grid3:
            Q = np.array(p1, dtype=float) - np.array(p2, dtype=float)
            a = np.array([A[0][ix[p1], ix[p2]], A[1][ix[p1], ix[p2]]])
            tot += (Q @ Q) * np.vdot(a, a).real - abs(Q @ a) ** 2
    return tot


def quartic(A):
    c = A[0] @ A[1] - A[1] @ A[0]
    return (-0.5 * np.trace(c @ c)).real


def cubic(A):
    c = A[0] @ A[1] - A[1] @ A[0]
    d = (P0[0] @ A[1] - A[1] @ P0[0]) - (P0[1] @ A[0] - A[0] @ P0[1])
    return (-np.trace(c @ d)).real


print('3. no fibre: quadratic form', S2_form(Aa), S2_form(Am), '; cubic term', cubic(Aa), cubic(Am), '; quartic term', quartic(Aa), quartic(Am))
assert abs(S2_form(Aa) - S2_form(Am)) < 1e-8 * abs(S2_form(Aa))
assert abs(quartic(Aa) - quartic(Am)) > 1e-3 * abs(quartic(Aa))
print('ALL ASSERTIONS PASSED')
