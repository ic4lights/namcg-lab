"""
Index check for the connection (X) weight.  With (B^sigma) = (1/2) N^sigma_{ab} R^{ab} in a representation R of so(4) (J for the vector,
S^{ab} = (1/4)[gamma^a,gamma^b] for spinors), tr_R(B_sigma B^sigma) = -(index_R/index_vec) * |N|^2 with |N|^2 = N_{ab}N_{ab}.
Checks: vector: -|N|^2 ; Dirac 4: -(1/2)|N|^2 ; 10D spinor restricted to so(4): ratio 8 to the 4D Dirac (32 = 4 x 8).
"""
import numpy as np
rng = np.random.default_rng(1)
N = rng.normal(size=(4, 4)); N = N - N.T
N2 = (N * N).sum()
J = np.zeros((4, 4, 4, 4))
for a in range(4):
    for b in range(4):
        J[a, b, a, b] += 1; J[a, b, b, a] -= 1
Bv = 0.5 * np.einsum('ab,abmn->mn', N, J)
print('vector: tr B^2 / |N|^2 =', np.trace(Bv @ Bv) / N2)
s0 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
g = [np.kron(s1, s0), np.kron(s2, s0), np.kron(s3, s1), np.kron(s3, s2)]
Sab = lambda a, b, G: 0.25 * (G[a] @ G[b] - G[b] @ G[a])
Bs = 0.5 * sum(N[a, b] * Sab(a, b, g) for a in range(4) for b in range(4))
print('Dirac 4: tr B^2 / |N|^2 =', np.trace(Bs @ Bs).real / N2)
# 10D Euclidean gamma (32x32) via tensor products, restricted to indices 0..3
def kron(*ms):
    out = np.eye(1)
    for m in ms:
        out = np.kron(out, m)
    return out
G10 = []
for k in range(5):
    G10.append(kron(*([s3] * k + [s1] + [s0] * (4 - k))))
    G10.append(kron(*([s3] * k + [s2] + [s0] * (4 - k))))
assert all(np.allclose(G10[a] @ G10[b] + G10[b] @ G10[a], 2 * (a == b) * np.eye(32)) for a in range(10) for b in range(10))
B32 = 0.5 * sum(N[a, b] * Sab(a, b, G10) for a in range(4) for b in range(4))
print('10D spinor (32) restricted to so(4): tr B^2 / |N|^2 =', np.trace(B32 @ B32).real / N2, ' -> 16-dim Weyl half =', np.trace(B32 @ B32).real / N2 / 2)
t16 = np.trace(B32 @ B32).real / N2 / 2
print('b contribution = w * (-tr B^2/|N|^2):  vector (w=+1):', 1 * (1.0), '; Dirac (w=-1):', -1 * (0.5), '; 16-real MW (w=-1/2):', -0.5 * (-t16))
