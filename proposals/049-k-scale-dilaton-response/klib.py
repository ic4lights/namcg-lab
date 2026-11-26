"""Finite-matrix K functionals used by the 049 scripts.

K is a list of six Hermitian d x d matrices Lambda^i (zero blocks allowed).
Operators act on Mat_d, vectorised column-wise: vec(AB - BA) = adc(A) vec(B).

  H0 = sum_i adc(Lambda^i)^2
  HV = H0 delta_ij + 2 adc([Lambda^i,Lambda^j])         (vector, six components)
  HD = (sum_i gamma_i adc(Lambda^i))^2                  (Dirac of so(6), 4 + 4bar)

v(s) = tr exp(-s HV) - 6 tr exp(-s H0),  tau(s) = tr exp(-s HD) - 8 tr exp(-s H0).
"""
import numpy as np


def comm(a, b):
    return a @ b - b @ a


def adc(a):
    d = a.shape[0]
    return np.kron(np.eye(d), a) - np.kron(a.T, np.eye(d))


def gamma6():
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    e = np.eye(2, dtype=complex)

    def k3(a, b, c):
        return np.kron(np.kron(a, b), c)

    return [k3(s1, e, e), k3(s2, e, e), k3(s3, s1, e), k3(s3, s2, e), k3(s3, s3, s1), k3(s3, s3, s2)]


def operators(L):
    ads = [adc(x) for x in L]
    D2 = ads[0].shape[0]
    H0 = sum(a @ a for a in ads)
    HV = np.zeros((6 * D2, 6 * D2), dtype=complex)
    for i in range(6):
        for j in range(6):
            blk = 2 * adc(comm(L[i], L[j]))
            if i == j:
                blk = blk + H0
            HV[i * D2:(i + 1) * D2, j * D2:(j + 1) * D2] = blk
    Dirac = sum(np.kron(g, a) for g, a in zip(gamma6(), ads))
    HD = Dirac @ Dirac
    return H0, HV, HD


def spectra(L):
    """Eigenvalues (lam0, lamV, lamD) for the six matrices L."""
    H0, HV, HD = operators(L)
    w0 = np.linalg.eigvalsh((H0 + H0.conj().T) / 2)
    wV = np.linalg.eigvalsh((HV + HV.conj().T) / 2)
    wD = np.linalg.eigvalsh((HD + HD.conj().T) / 2)
    return w0, wV, wD


def _pw(w, p, tol):
    w = np.where(np.abs(w) < tol, 0.0, w)
    out = np.zeros_like(w)
    m = w > 0
    out[m] = w[m] ** p * np.log(w[m])
    return out.sum()


def moments_from_spectra(w0, wV, wD, tol=1e-8):
    """V, T and Uhat at unit scale.

    V = int ds s^-2 v(s), T = int ds s^-2 tau(s), Uhat = int ds s^-3 (v - tau)(s).
    With sum c_i = sum c_i w_i = 0: int_0^oo ds s^-2 sum c_i exp(-s w_i) = sum c_i w_i ln w_i.
    With also sum c_i w_i^2 = 0: int_0^oo ds s^-3 sum c_i exp(-s w_i) = -(1/2) sum c_i w_i^2 ln w_i.
    Each is finite only if no w_i is negative.
    """
    V = _pw(wV, 1, tol) - 6 * _pw(w0, 1, tol)
    T = _pw(wD, 1, tol) - 8 * _pw(w0, 1, tol)
    U = -0.5 * (_pw(wV, 2, tol) - _pw(wD, 2, tol) + 2 * _pw(w0, 2, tol))
    return V, T, U


def moments(L, tol=1e-8):
    w0, wV, wD = spectra(L)
    V, T, U = moments_from_spectra(w0, wV, wD, tol)
    return V, T, U, dict(minV=wV.min(), minD=wD.min())


def str_moment(w0, wV, wD, k):
    return (wV ** k).sum() - (wD ** k).sum() + 2 * (w0 ** k).sum()


def tree_data(L):
    """abar = -(1/4) tr [L^i,L^j]^2 >= 0 and nbar = tr L^i L^i."""
    a = 0.0
    for i in range(6):
        for j in range(6):
            c = comm(L[i], L[j])
            a += -0.25 * np.trace(c @ c).real
    n = sum(np.trace(x @ x).real for x in L)
    return a, n


def su2(N):
    """Spin (N-1)/2 generators, N x N."""
    j = (N - 1) / 2
    m = np.arange(j, -j - 1, -1)
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((N, N), dtype=complex)
    for k in range(N - 1):
        Jp[k, k + 1] = np.sqrt(j * (j + 1) - m[k + 1] * (m[k + 1] + 1))
    return (Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, Jz


def K_sphere(N):
    a, b, c = su2(N)
    z = np.zeros((N, N), dtype=complex)
    return [a, b, c, z, z, z]


def K_two_spheres(N1, N2, r1=1.0, r2=1.0):
    a = su2(N1)
    b = su2(N2)
    e1, e2 = np.eye(N1), np.eye(N2)
    return [r1 * np.kron(x, e2) for x in a] + [r2 * np.kron(e1, x) for x in b]


def su3_rep(p):
    """Symmetric rep (p,0) of su(3), dimension (p+1)(p+2)/2. Returns the ladder operators E_ij."""
    states = [(a, b, p - a - b) for a in range(p + 1) for b in range(p + 1 - a)]
    idx = {s: k for k, s in enumerate(states)}
    d = len(states)
    E = {}
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            M = np.zeros((d, d), dtype=complex)
            for s in states:
                if s[j] > 0:
                    t = list(s)
                    t[j] -= 1
                    t[i] += 1
                    M[idx[tuple(t)], idx[s]] = np.sqrt(s[j] * (s[i] + 1))
            E[(i, j)] = M
    return E


def K_squashed(E, c=(1.0, 1.0, 1.0)):
    """Six root generators of su(3) with the Cartan generators dropped (squashed coadjoint orbit)."""
    L = []
    for (i, j), w in zip([(0, 1), (1, 2), (2, 0)], c):
        x = E[(i, j)]
        y = E[(j, i)]
        L.append(w * (x + y) / np.sqrt(2))
        L.append(w * (x - y) / (np.sqrt(2) * 1j))
    return L


def su3_mixed(p, q):
    """Irreducible rep (p,q): top Casimir block of (p,0) x (0,q). Returns (E, dim)."""
    Ep = su3_rep(p)
    Eq = su3_rep(q)
    Eqb = {k: -Eq[(k[1], k[0])].T.conj().T if False else -Eq[k].T for k in Eq}
    dp = next(iter(Ep.values())).shape[0]
    dq = next(iter(Eq.values())).shape[0]
    E = {k: np.kron(Ep[k], np.eye(dq)) + np.kron(np.eye(dp), Eqb[k]) for k in Ep}
    H = [sum(comm(E[(i, j)], E[(j, i)]) for j in range(3) if j != i) / 3 for i in range(3)]
    Cas = sum(E[(i, j)] @ E[(j, i)] for i in range(3) for j in range(3) if i != j) + sum(h @ h for h in H)
    w, U = np.linalg.eigh((Cas + Cas.conj().T) / 2)
    sel = np.abs(w - w.max()) < 1e-8
    P = U[:, sel]
    return {k: P.conj().T @ v @ P for k, v in E.items()}, P.shape[1]
