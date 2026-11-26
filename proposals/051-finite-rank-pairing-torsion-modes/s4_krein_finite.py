"""051 s4: finite matrices, general backgrounds. Floating point, seeded; residuals printed.

(M A)_b = [X^a,[X_a,A_b]] - 2 [F_ab, A^a],  F_ab = [X_a,X_b], indices raised with eta: the background-gauge operator.
The form is <A,B>_J = eta^{ab} Tr(A_a^dagger B_b).
 a  M is symmetric for <,>_J at random Hermitian X (no equation of motion is used).
 b  commuting X: M is diagonal, eigenvalues Q^2 = eta^{ab} (x_a(m)-x_a(n))(x_b(m)-x_b(n)), real and Hilbert-Schmidt symmetric.
 c  ad F_0i = 0 (X_0 = x tensor 1, X_i = 1 tensor x_i): M is Hilbert-Schmidt symmetric, so no Jordan block and real spectrum.
 d  generic X: M is not Hilbert-Schmidt symmetric; complex eigenvalues occur.
 f  second variation: for commuting X, S = -(1/4) Tr [X^a,X^b][X_a,X_b] has quadratic part (1/2) eta^{ab} Tr(A_a (E A)_b), with
    (E A)_b = Q.Q A_b - Q_b Q^a A_a on matrix elements, by comparing with a direct expansion.
 e  along X_0 -> t X_0 from t = 0 (case c): at the first complex pair the two colliding eigenvectors have <v,v>_J -> 0 relative to
    <v,v>_HS, which is the neutral eigenvector forced at a Jordan block."""
import numpy as np

np.random.seed(51)
comm = lambda A, B: A @ B - B @ A


def herm(s):
    a = np.random.randn(s, s) + 1j * np.random.randn(s, s)
    return (a + a.conj().T) / 2


def Mmat(Xs, eta):
    D = len(Xs)
    N = Xs[0].shape[0]
    idx = np.eye(N)
    # ad(X) as a matrix on vec(A), column stacking: vec(XA - AX) = (kron(I,X) - kron(X^T,I)) vec(A)
    ad = lambda Y: np.kron(idx, Y) - np.kron(Y.T, idx)
    adX = [ad(x) for x in Xs]
    box = sum(eta[a] * adX[a] @ adX[a] for a in range(D))
    M = np.zeros((D * N * N, D * N * N), dtype=complex)
    for b in range(D):
        M[b * N * N:(b + 1) * N * N, b * N * N:(b + 1) * N * N] += box
        for a in range(D):
            F = comm(Xs[a], Xs[b])
            # -2 [F_ab, A^a], A^a = eta[a] A_a
            M[b * N * N:(b + 1) * N * N, a * N * N:(a + 1) * N * N] += -2 * eta[a] * ad(F)
    Jm = np.kron(np.diag(eta), np.eye(N * N))
    return M, Jm


eta4 = np.array([-1.0, 1, 1, 1])
N = 3
Xs = [herm(N) for _ in range(4)]
M, Jm = Mmat(Xs, eta4)
print('a  || J M - (J M)^dagger || / ||M|| = %.2e' % (np.linalg.norm(Jm @ M - (Jm @ M).conj().T) / np.linalg.norm(M)))
assert np.linalg.norm(Jm @ M - (Jm @ M).conj().T) < 1e-10 * np.linalg.norm(M)

ds = [np.diag(np.random.randn(N)) + 0j for _ in range(4)]
M2, _ = Mmat(ds, eta4)
vals = np.sort(np.linalg.eigvals(M2).real)
pred = sorted(float(sum(eta4[a] * (ds[a][m, m].real - ds[a][n, n].real) ** 2 for a in range(4))) for m in range(N) for n in range(N) for _ in range(4))
print('b  commuting: M diagonal: off-diagonal norm %.2e; eigenvalues vs Q^2: %.2e; ||M-M^dagger|| = %.2e' %
      (np.linalg.norm(M2 - np.diag(np.diag(M2))), np.abs(vals - np.array(pred)).max(), np.linalg.norm(M2 - M2.conj().T)))
assert np.abs(vals - np.array(pred)).max() < 1e-10

n0, n1 = 2, 3
x0 = herm(n0)
Xc = [np.kron(x0, np.eye(n1))] + [np.kron(np.eye(n0), herm(n1)) for _ in range(3)]
M3, _ = Mmat(Xc, eta4)
print('c  ad F_0i = 0: ||M - M^dagger|| / ||M|| = %.2e; max |Im eigenvalue| = %.2e' %
      (np.linalg.norm(M3 - M3.conj().T) / np.linalg.norm(M3), np.abs(np.linalg.eigvals(M3).imag).max()))
assert np.linalg.norm(M3 - M3.conj().T) < 1e-10 * np.linalg.norm(M3)

imax = np.abs(np.linalg.eigvals(M).imag).max()
print('d  generic: ||M - M^dagger|| / ||M|| = %.3f; max |Im eigenvalue| = %.4f' % (np.linalg.norm(M - M.conj().T) / np.linalg.norm(M), imax))
assert imax > 1e-6

# e
base = [herm(N) for _ in range(3)]
x0 = herm(N)
def at(t):
    Y = [t * x0] + base
    return Mmat(Y, eta4)
def imag_max(t):
    m, _ = at(t)
    return np.abs(np.linalg.eigvals(m).imag).max()
ts = np.linspace(0, 1.5, 3001)
t_on = None
for t in ts:
    if imag_max(t) > 1e-6:
        t_on = t
        break
print('e  first t on the grid with a complex pair (threshold 1e-6):', t_on)
assert t_on is not None and t_on > 0
lo, hi = t_on - (ts[1] - ts[0]), t_on
for _ in range(40):
    mid = (lo + hi) / 2
    if imag_max(mid) > 1e-6:
        hi = mid
    else:
        lo = mid
for lab, t in (('just below', lo - 1e-3), ('closer', lo - 1e-5), ('closest', lo)):
    m, Jq = at(t)
    w, V = np.linalg.eig(m)
    # the pair with smallest gap away from the (degenerate) kernel of M
    order = np.argsort(w.real)
    best = None
    for i in range(len(w)):
        for j in range(i + 1, len(w)):
            if abs(w[i]) > 1e-3 and abs(w[j]) > 1e-3:
                g = abs(w[i] - w[j])
                if best is None or g < best[0]:
                    best = (g, i, j)
    g, i, j = best
    kr = [abs((V[:, q].conj() @ Jq @ V[:, q]) / (V[:, q].conj() @ V[:, q])) for q in (i, j)]
    print('   %-10s t=%.6f  smallest gap %.3e  |<v,v>_J|/<v,v>_HS = %.3e, %.3e' % (lab, t, g, kr[0], kr[1]))
# f
def Squart(Y):
    v = 0
    for a in range(4):
        for b in range(4):
            Cm = comm(Y[a], Y[b])
            v = v - 0.25 * eta4[a] * eta4[b] * np.trace(Cm @ Cm)
    return v
As = [herm(N) for _ in range(4)]
h = 1e-3
second = (Squart([d_ + h * a_ for d_, a_ in zip(ds, As)]) + Squart([d_ - h * a_ for d_, a_ in zip(ds, As)]) - 2 * Squart(ds)) / (2 * h * h)
xs = [np.diag(d_).real for d_ in ds]
EA = []
for b in range(4):
    out = np.zeros((N, N), dtype=complex)
    for m_ in range(N):
        for n_ in range(N):
            Q_ = np.array([xs[a][m_] - xs[a][n_] for a in range(4)])
            QQ = (eta4 * Q_ * Q_).sum()
            QA = sum(eta4[a] * Q_[a] * As[a][m_, n_] for a in range(4))
            out[m_, n_] = QQ * As[b][m_, n_] - Q_[b] * QA
    EA.append(out)
pred = 0.5 * sum(eta4[b] * np.trace(As[b] @ EA[b]) for b in range(4))
print('f  quadratic part: direct %.8f, (1/2) eta Tr(A E A) %.8f, difference %.2e' % (second.real, pred.real, abs(second - pred)))
assert abs(second - pred) < 1e-5
print('ALL ASSERTIONS PASSED')
