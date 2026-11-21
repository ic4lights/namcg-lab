"""V3. Is a constant recombination K = G M of the forty linearised equations the Euler-Lagrange
operator of a quadratic Lagrangian L = (1/2) phi^T K(d) phi with constant coefficients?
That requires K formally self-adjoint:  (G M0)^T = G M0,  (G M1^mu)^T = -G M1^mu,
(G M2^{mu nu})^T = G M2^{mu nu}, for some constant 40 x 40 matrix G (equation index in columns).
Reports: dimension of the solution space, the maximal rank of a member, and the size of the
columns of G that act on the frame equations B1 (rows 0..15 of M).
Run: python -I v3_forms_EL.py
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import M_coeffs, NF, flat, null_rotation_g2, heisenberg   # noqa: E402

n = NF
P = np.zeros((n * n, n * n))          # vec(G^T) = P vec(G), row-major vec
for i in range(n):
    for j in range(n):
        P[j * n + i, i * n + j] = 1.0
I = np.eye(n)


def right(X):                          # vec(G) -> vec(G X)
    return np.kron(I, X.T)


def tr_of_right(X):                    # vec(G) -> vec((G X)^T)
    return P @ right(X)


for name, bg, dirs in [('flat', flat(), (0, 1, 2, 3)), ('null rotation, constant-connection gauge', null_rotation_g2(), (0, 1, 2, 3)),
                       ('Heisenberg, character directions 0,1,3', heisenberg(), (0, 1, 3))]:
    M0, M1, M2 = M_coeffs(*bg, dirs=dirs)
    rows = [tr_of_right(M0) - right(M0)] + [tr_of_right(M1[m]) + right(M1[m]) for m in M1] \
        + [tr_of_right(M2[k]) - right(M2[k]) for k in M2]
    A = np.vstack(rows)
    ev, V = np.linalg.eigh(A.T @ A)
    k = int((ev < 1e-9 * ev[-1]).sum())
    Gs = V[:, :k].T.reshape(k, n, n)
    g = np.random.default_rng(0)
    Gc = sum(g.normal() * G for G in Gs) if k else np.zeros((n, n))
    frame_cols = max((np.abs(G[:, :16]).max() for G in Gs), default=0.0)
    print('== %s: dim %d; next constraint eigenvalue %.3g; rank of a generic member %d of 40; max |G| on the frame-equation columns %.1e'
          % (name, k, ev[k] if k < len(ev) else float('nan'), np.linalg.matrix_rank(Gc, tol=1e-7), frame_cols))
