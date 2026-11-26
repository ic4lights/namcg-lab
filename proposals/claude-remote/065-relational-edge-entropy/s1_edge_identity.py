"""
065 s1: exact finite-N identity for the classical edge datum of a matrix block.

For Hermitian X^a (a=1..d), a positive symmetric contraction G_ab and an orthogonal projector Theta of rank M,
with X_{SS'} = Theta X (1-Theta),
    sum_ab G_ab Tr(X^a_{SS'} X^b_{S'S}) = 1/2 sum_ab G_ab Tr([X^a,Theta]^dag [X^b,Theta])
                                       = 1/2 Tr(Theta Box_G(Theta)),   Box_G(Y) = sum_ab G_ab [X^a,[X^b,Y]].
Random tests at several N, M, d. Output to stdout only.
"""
import numpy as np

rng = np.random.default_rng(65001)

def herm(n):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (a + a.conj().T) / 2

def comm(a, b):
    return a @ b - b @ a

worst = 0.0
for N in (3, 7, 16, 40):
    for M in sorted({1, N // 3, N // 2, N - 1}):
        if M < 1:
            continue
        for d in (1, 3, 6):
            X = [herm(N) for _ in range(d)]
            B = rng.normal(size=(d, d)); G = B @ B.T + 0.1 * np.eye(d)
            U, _ = np.linalg.qr(rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)))
            P = U[:, :M] @ U[:, :M].conj().T
            Q = np.eye(N) - P
            lhs = sum(G[a, b] * np.trace((P @ X[a] @ Q) @ (Q @ X[b] @ P)) for a in range(d) for b in range(d))
            mid = 0.5 * sum(G[a, b] * np.trace(comm(X[a], P).conj().T @ comm(X[b], P)) for a in range(d) for b in range(d))
            box = sum(G[a, b] * comm(X[a], comm(X[b], P)) for a in range(d) for b in range(d))
            rhs = 0.5 * np.trace(P @ box)
            err = max(abs(lhs - mid), abs(lhs - rhs)) / max(1.0, abs(lhs))
            worst = max(worst, err)
            assert abs(lhs.imag) < 1e-9 * max(1, abs(lhs)) and lhs.real > 0
print('identity sum G Tr(X_SS\' X_S\'S) = 1/2 sum G Tr([X,T]^+[X,T]) = 1/2 Tr(T Box_G T): max rel. error %.2e' % worst)
assert worst < 1e-10
print('PASS s1')
