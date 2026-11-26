"""s2: constitutive tensor of the exact-variation Hessian.

Exact statement (Moser picture): with X^a embedding functions of a fixed symplectic leaf, S[X] = int d^4y L(omega_X), omega_X = (X^{-1})^* omega_leaf,
L(omega) = |Pf omega| eta_{ac} eta_{bd} Theta^{ab} Theta^{cd}, Theta = omega^{-1}.   Variations of X change omega_X by dA (exact 2-form).
L is an ALGEBRAIC function of the six numbers omega_{mu nu}(y), so on the stationary set (first-order term dropped) the Hessian in A is
(1/2) int (dA)_{mu nu} H^{mu nu, rho sigma}(y) (dA)_{rho sigma},  H = d^2 L / d omega d omega  (6x6).
Here: compute H numerically at random omega, both signatures, and test whether H lies in span{ Maxwell_G , F^F } (G = K^{-1}, K = Theta^T eta Theta),
i.e. whether the exact-variation Hessian is a rotation-covariant (G, scalar-weighted) Maxwell + axion form.
"""
import itertools
import numpy as np

pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def omega_from6(w6):
    W = np.zeros((4, 4))
    for v, (i, j) in zip(w6, pairs):
        W[i, j] = v; W[j, i] = -v
    return W


def pf(W):
    return W[0, 1]*W[2, 3] - W[0, 2]*W[1, 3] + W[0, 3]*W[1, 2]


def L(w6, eta):
    W = omega_from6(w6)
    Th = np.linalg.inv(W)
    return abs(pf(W)) * np.einsum('ac,bd,ab,cd->', eta, eta, Th, Th)


def hessian(w6, eta, h=1e-4):
    n = 6
    H = np.zeros((n, n))
    f0 = L(w6, eta)
    for i in range(n):
        for j in range(i, n):
            ei = np.zeros(n); ej = np.zeros(n); ei[i] = h; ej[j] = h
            v = (L(w6+ei+ej, eta) - L(w6+ei-ej, eta) - L(w6-ei+ej, eta) + L(w6-ei-ej, eta))/(4*h*h)
            H[i, j] = H[j, i] = v
    return H


def maxwell_G(w6, eta):
    """quadratic form on F in the 6-basis: rho * G^{mu rho} G^{nu sigma} F_{mu nu} F_{rho sigma}, G^{-1} = K = Theta eta Theta^T"""
    W = omega_from6(w6)
    Th = np.linalg.inv(W)
    K = np.einsum('am,bn,ab->mn', Th, Th, eta)       # K^{mu nu} = eta_{ab} Th^{a mu} Th^{b nu}
    rho = abs(pf(W))
    M = np.zeros((6, 6))
    for I, (a, b) in enumerate(pairs):
        for Jx, (c, d) in enumerate(pairs):
            # F_{mu nu} with unit component on pair (a,b) (antisym): sum over both orderings -> factor 4 absorbed consistently
            M[I, Jx] = 2*rho*(K[a, c]*K[b, d] - K[a, d]*K[b, c])
    return M


def axion(w6):
    """eps^{mu nu rho sigma} F_{mu nu} F_{rho sigma} in 6-basis"""
    A = np.zeros((6, 6))
    for I, (a, b) in enumerate(pairs):
        for Jx, (c, d) in enumerate(pairs):
            if len({a, b, c, d}) == 4:
                perm = [a, b, c, d]
                sign = np.linalg.det(np.eye(4)[perm])
                A[I, Jx] = 8*sign
    return A


rng = np.random.default_rng(3)
for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    eta = np.diag(np.array(etad, float))
    print('eta =', etad)
    for t in range(6):
        w6 = rng.uniform(-1, 1, 6)
        if abs(pf(omega_from6(w6))) < 0.1:
            continue
        H = hessian(w6, eta)
        Mx = maxwell_G(w6, eta); Ax = axion(w6)
        # least squares H ~ a Mx + b Ax
        Amat = np.stack([Mx.ravel(), Ax.ravel()], axis=1)
        coef, *_ = np.linalg.lstsq(Amat, H.ravel(), rcond=None)
        rem = H - coef[0]*Mx - coef[1]*Ax
        # first-order piece alone: rho*eta eta dTheta dTheta with dTheta = -Th dw Th  (equals Maxwell_G/ (some factor))
        # the Maxwell part of L's second variation: 0.5*H vs Mx
        print(f"  draw {t}: a={coef[0]:+.4f} b={coef[1]:+.4f}  |H - a Mx - b Ax|/|H| = {np.linalg.norm(rem)/np.linalg.norm(H):.3e}   (|H|={np.linalg.norm(H):.3f})")
