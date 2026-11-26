"""
074 / s1.  Matrix-level check of the one-component rescaling identity.

For S(X) = -(1/4) sum_{a,b} eta_aa eta_bb Tr [X_a,X_b]^2 + (1/2) sum_a mu_a^2 eta_aa Tr X_a^2
(quartic of eq:Smatrix with C=0, contracted with a diagonal eta, plus any diagonal bilinear term),
rescale one component X_u -> lam X_u.  Every term contains X_u at most twice and the term [X_u,X_u]
vanishes, so S(lam) = S_perp + lam^2 S_u exactly.  At a stationary point dS/dlam(1) = 2 S_u = 0,
hence S(lam) = S(1) for every lam.  For a second rescaling X_perp -> mu X_perp of the complement,
S = a lam^2 mu^2 + b mu^4 + c lam^2 + d mu^2 and the Hessian at a stationary point is [[0,4a],[4a,8b]].

Checks: (1) random Hermitian matrices, the polynomial identity in lam (exact up to float rounding);
(2) a stationary point: the fuzzy sphere X_i = J_i (spin j) with the bilinear coefficient fixed by the
field equation, for the Euclidean and for a Lorentzian contraction; flatness to all orders and the
2x2 Hessian.
Run:  python -I s1_matrix_flat_direction.py
"""
import numpy as np

rng = np.random.default_rng(7)


def comm(a, b):
    return a @ b - b @ a


def action(X, eta, mu2):
    n = len(X)
    s = 0.0
    for a in range(n):
        for b in range(n):
            c = comm(X[a], X[b])
            s += -0.25 * eta[a] * eta[b] * np.trace(c @ c).real
    for a in range(n):
        s += 0.5 * mu2[a] * eta[a] * np.trace(X[a] @ X[a]).real
    return s


def herm(N):
    A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    return (A + A.conj().T) / 2


# (1) polynomial identity for random matrices
N = 6
for eta in ([-1, 1, 1, 1], [1, 1, 1, 1]):
    X = [herm(N) for _ in range(4)]
    mu2 = list(rng.normal(size=4))
    u = 0
    lams = [0.3, 0.7, 1.0, 1.9, -2.2]
    vals = []
    for lam in lams:
        Y = [x.copy() for x in X]
        Y[u] = lam * Y[u]
        vals.append(action(Y, eta, mu2))
    # fit S = p0 + p1 lam + p2 lam^2 + p3 lam^3 + p4 lam^4
    V = np.vander(lams, 5, increasing=True)
    coef = np.linalg.solve(V, vals)
    print("eta", eta, "coefficients of lam^0..lam^4:", np.round(coef, 10))
    assert abs(coef[1]) < 1e-8 and abs(coef[3]) < 1e-8 and abs(coef[4]) < 1e-8
print("(1) S(lam) = S_perp + lam^2 S_u for random matrices: OK")


# (2) fuzzy sphere stationary point
def spin(j):
    m = np.arange(j, -j - 1, -1)
    d = len(m)
    Jz = np.diag(m)
    Jp = np.zeros((d, d))
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    Jx = (Jp + Jp.T) / 2
    Jy = (Jp - Jp.T) / 2j
    return [Jx.astype(complex), Jy.astype(complex), Jz.astype(complex)]


def eom(X, eta, mu2):
    # dS/dX_a  ~  sum_b eta_a eta_b [X_b,[X_b,X_a]] + mu_a^2 eta_a X_a  (up to an overall factor)
    out = []
    for a in range(len(X)):
        e = mu2[a] * eta[a] * X[a]
        for b in range(len(X)):
            e = e + eta[a] * eta[b] * comm(X[b], comm(X[b], X[a]))
        out.append(e)
    return out


for j in (1, 2.5, 4):
    J = spin(j)
    for eta in ([1, 1, 1], [-1, 1, 1]):
        # the field equation sum_b eta_b [J_b,[J_b,J_a]] = -mu_a^2 J_a fixes mu_a^2 per component
        mu2 = []
        for a in range(3):
            lhs = sum(eta[a] * eta[b] * comm(J[b], comm(J[b], J[a])) for b in range(3))
            r = np.trace(lhs @ J[a].conj().T).real / np.trace(J[a] @ J[a].conj().T).real
            mu2.append(-r / eta[a])
        res = max(np.abs(e).max() for e in eom(J, eta, mu2))
        S1 = action(J, eta, mu2)
        dev = max(abs(action([lam * J[0], J[1], J[2]], eta, mu2) - S1) for lam in (0.2, 0.9, 1.5, 3.0, -1.0))
        # two-parameter family X_0 -> lam X_0, X_{1,2} -> nu X_{1,2}
        def S2(lam, nu):
            return action([lam * J[0], nu * J[1], nu * J[2]], eta, mu2)
        h = 1e-3
        Hll = (S2(1 + h, 1) - 2 * S2(1, 1) + S2(1 - h, 1)) / h**2
        Hnn = (S2(1, 1 + h) - 2 * S2(1, 1) + S2(1, 1 - h)) / h**2
        Hln = (S2(1 + h, 1 + h) - S2(1 + h, 1 - h) - S2(1 - h, 1 + h) + S2(1 - h, 1 - h)) / (4 * h * h)
        print(f"j={j} eta={eta} mu^2={np.round(mu2,6)} |EOM|={res:.1e} max|S(lam)-S(1)|={dev:.1e} "
              f"Hessian [[{Hll:.4f},{Hln:.4f}],[{Hln:.4f},{Hnn:.4f}]] det={Hll*Hnn-Hln**2:.4f}")
        assert res < 1e-9 and dev < 1e-8 and abs(Hll) < 1e-4 and Hll * Hnn - Hln**2 < 0
print("(2) at a stationary point the one-component rescaling is flat to all orders; the Hessian with the")
print("    complementary rescaling is [[0,4a],[4a,8b]] with det = -16 a^2 < 0: OK")
