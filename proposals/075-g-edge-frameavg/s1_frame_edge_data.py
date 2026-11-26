"""075 s1: exact finite-N verification of the frame dependence of the cap edge data.

Class: the single-factor edge datum of the 065 block (appH Problem G, Edge datum
paragraph): X^a = A^a_b J^b on the N-dimensional irreducible representation of
su(2) (Jhbar = 1), Theta the spectral projector of n.J on its M largest
eigenvalues, s^2(n) = sum_a || Theta X^a (1-Theta) ||_F^2.

Claim under test (the paragraph's exact formula, general axis n):
    s^2(n) = (1/4) M (N-M) (sigma_1^2 + sigma_2^2),
    sigma_1^2 + sigma_2^2 = tr(B) - n^T B n,   B = A^T A, |n| = 1
    (trace of B restricted to the plane orthogonal to n).

Sections:
(1) A = I, several (N, M): s^2 = M(N-M)/2 to roundoff.
(2) general real invertible A, general unit n: prediction above (8 trials,
    deterministic seed 75001).
(3) convention-free ratio form: s^2(n) / s^2(e3) = (tr B - n^T B n)/(tr B - B_33),
    independent of any overall normalisation convention.
(4) sphere mean of s^2(n) = (1/4) M (N-M) (2 tr B / 3) on a fixed Gauss-Legendre
    x uniform-phi product grid (deterministic).
(5) edge-datum identity sum_a Tr(X_{S b} X_{b S}) = (1/2) Tr(Theta Box Theta),
    Box = sum_a [X^a,[X^a, .]], for a general axis (the identity that makes s^2
    the quadratic form of the projector in the kinetic operator).

Deterministic; numpy floats only. Run:
  python -I proposals/075-g-edge-frameavg/s1_frame_edge_data.py
Expected invariants: all relative deviations <= 1e-10; last line 'PASS s1'.
"""
import math

import numpy as np


def su2(N):
    j = (N - 1) / 2.0
    Jp = np.zeros((N, N), dtype=complex)
    for k in range(1, N):
        mk = j - k
        Jp[k - 1, k] = math.sqrt(j * (j + 1) - mk * (mk + 1))
    Jm = Jp.conj().T
    m = np.array([j - k for k in range(N)], dtype=float)
    return 0.5 * (Jp + Jm), -0.5j * (Jp - Jm), np.diag(m)


def cap_projector(N, M, n):
    Jx, Jy, Jz = su2(N)
    Hn = n[0] * Jx + n[1] * Jy + n[2] * Jz
    w, v = np.linalg.eigh(Hn)
    idx = np.argsort(w)[::-1][:M]
    return v[:, idx] @ v[:, idx].conj().T


def s2_frame(N, M, A, n):
    n = np.asarray(n, dtype=float)
    n = n / np.linalg.norm(n)
    P = cap_projector(N, M, n)
    Q = np.eye(N, dtype=complex) - P
    J = su2(N)
    s2 = 0.0
    for a in range(3):
        Xa = sum(A[a, b] * J[b] for b in range(3))
        s2 += np.linalg.norm(P @ Xa @ Q, 'fro') ** 2
    return float(np.real(s2))


# ---------- (1) A = I ----------
print('(1) A=I: s^2 vs M(N-M)/2')
worst = 0.0
for N, M in ((6, 2), (6, 3), (10, 4), (10, 7), (14, 5)):
    s2 = s2_frame(N, M, np.eye(3), (0, 0, 1))
    pred = 0.5 * M * (N - M)
    rel = abs(s2 - pred) / pred
    worst = max(worst, rel)
    print('    N=%2d M=%2d  s2=%.12f pred=%.12f rel=%.2e' % (N, M, s2, pred, rel))
assert worst <= 1e-10
print('(1) worst rel %.2e  PASS s1(1)' % worst)

# ---------- (2) general A, general n ----------
print('(2) general A, general n: s^2 vs (1/4) M(N-M)(tr B - n^T B n)')
rng = np.random.default_rng(75001)
worst = 0.0
for trial in range(8):
    A = rng.normal(size=(3, 3))
    while abs(np.linalg.det(A)) < 0.3:
        A = rng.normal(size=(3, 3))
    n = rng.normal(size=3)
    N, M = 10, 4
    s2 = s2_frame(N, M, A, n)
    B = A.T @ A
    pred = 0.25 * M * (N - M) * (np.trace(B) - n @ B @ n / (n @ n))
    rel = abs(s2 - pred) / pred
    worst = max(worst, rel)
print('    worst rel dev over 8 trials: %.3e' % worst)
assert worst <= 1e-10
print('(2) PASS s1(2)')

# ---------- (3) convention-free ratio form ----------
print('(3) ratio form vs e3 axis (normalisation-convention free)')
A = np.array([[2.0, 0.5, 0.1], [0.3, 1.1, 0.4], [0.2, 0.0, 1.7]])
B = A.T @ A
tau = float(np.trace(B))
s2e3 = s2_frame(12, 5, A, (0, 0, 1))
worst = 0.0
for n in ((1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1), (0.2, -0.7, 0.66)):
    n = np.asarray(n, float)
    n /= np.linalg.norm(n)
    s2 = s2_frame(12, 5, A, n)
    pred = s2e3 * (tau - n @ B @ n) / (tau - B[2, 2])
    rel = abs(s2 - pred) / abs(pred)
    worst = max(worst, rel)
print('    worst rel dev: %.3e' % worst)
assert worst <= 1e-10
print('(3) PASS s1(3)')

# ---------- (4) sphere mean ----------
print('(4) sphere mean of s^2(n): mean = (1/4) M(N-M) (2 tr B / 3)')
zg, wg = np.polynomial.legendre.leggauss(40)
z = 0.5 * (zg + 1.0)          # z = cos(theta) in [0,1], measure dz (even in cos)
w = 0.5 * wg
phi = np.linspace(0.0, 2.0 * math.pi, 16, endpoint=False)
N, M = 10, 4
mean = 0.0
for zi, wi in zip(z, w):
    th = math.acos(zi)
    acc = 0.0
    for p in phi:
        nn = (math.sin(th) * math.cos(p), math.sin(th) * math.sin(p), math.cos(th))
        acc += s2_frame(N, M, A, nn)
    mean += wi * acc / len(phi)
pred = 0.25 * M * (N - M) * (2.0 * tau / 3.0)
rel = abs(mean - pred) / pred
print('    mean=%.10f pred=%.10f rel=%.2e' % (mean, pred, rel))
assert rel <= 1e-10
print('(4) PASS s1(4)')

# ---------- (5) edge-datum identity ----------
print('(5) edge-datum identity: sum Tr(X_Sb X_bS) = (1/2) Tr(Theta Box Theta)')
N, M = 8, 3
n = np.array((0.2, -0.7, 0.66))
n /= np.linalg.norm(n)
P = cap_projector(N, M, n)
Q = np.eye(N, dtype=complex) - P
J = su2(N)
X = [sum(A[a, b] * J[b] for b in range(3)) for a in range(3)]
lhs = sum(np.trace(P @ Xa @ Q @ Xa.conj().T) for Xa in X)
rhs = 0.0
for Xa in X:
    innera = Xa @ (Xa @ P - P @ Xa) - (Xa @ P - P @ Xa) @ Xa
    rhs += 0.5 * np.trace(P @ innera @ P)
rel = abs(lhs - rhs) / abs(rhs)
print('    lhs=%.12f rhs=%.12f rel=%.2e' % (np.real(lhs), np.real(rhs), rel))
assert rel <= 1e-10
print('(5) PASS s1(5)')

print('PASS s1')
