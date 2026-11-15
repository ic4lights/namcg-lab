"""Shared numerical tools: characteristic roots and partial multiplicities."""
import numpy as np
import scipy.linalg as sl
from core import rank


def quad_coeffs(Mfun):
    A = Mfun(0.0); P = Mfun(1.0); Mi = Mfun(-1.0)
    return A, (P - Mi) / 2, (P + Mi) / 2 - A          # M(t) = A + t B + t^2 C


def char_roots(Mfun, r, seeds=(1, 2), tol=2e-3):
    """Values of t at which rank M(t) < r (r = generic rank).  M(t) is compressed to
    r x r by two independent random projections; a root is kept if common to both."""
    A, B, C = quad_coeffs(Mfun)
    res = []
    for sd in seeds:
        g = np.random.default_rng(sd)
        Pr = g.normal(size=(r, A.shape[0])); Vc = g.normal(size=(A.shape[1], r))
        a, b, c = [Pr @ X @ Vc for X in (A, B, C)]
        Z = np.zeros((r, r)); I = np.eye(r)
        ev = sl.eig(np.block([[Z, I], [-a, -b]]), np.block([[I, Z], [Z, c]]), right=False)
        res.append(ev[np.isfinite(ev) & (np.abs(ev) < 1e6)])
    a, b = res
    return np.array([x for x in a if np.abs(b - x).min() < tol * (1 + abs(x))])


def grouped(roots, dec=3, width=3e-3):
    """Cluster roots closer than width (multiple roots split numerically) and return
    [((mean real part, mean imaginary part), count)]."""
    rs = sorted(roots, key=lambda z: (round(z.imag, 2), z.real))
    clusters = []
    for z in rs:
        if clusters and abs(z - np.mean(clusters[-1])) < width * (1 + abs(z)):
            clusters[-1].append(z)
        else:
            clusters.append([z])
    out = [((float(np.mean(c).real) + 0.0, float(np.mean(c).imag) + 0.0), len(c)) for c in clusters]
    return sorted(out)


def partial_mult(Mfun, ngauge, Lmax=4):
    """Cumulative sums sum_i min(m_i, L), L = 1..Lmax, of the partial multiplicities
    m_i of the root t = 0 of M(t), after removing the gauge chains (ngauge per order)."""
    A, B, C = quad_coeffs(Mfun)
    n = A.shape[0]
    out = []
    for L in range(1, Lmax + 1):
        big = np.zeros((n * L, n * L), dtype=complex)
        for i in range(L):
            big[n*i:n*i+n, n*i:n*i+n] = A
            if i + 1 < L: big[n*i:n*i+n, n*(i+1):n*(i+2)] = B
            if i + 2 < L: big[n*i:n*i+n, n*(i+2):n*(i+3)] = C
        out.append(n * L - rank(big, 1e-7) - ngauge * L)
    return out
