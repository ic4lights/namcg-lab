"""030 script 8 (library + report): large-s expansion K(s) = c0 + c1/s + c2/s^2 + ... of the eps^2 weight-2 integrand.
tail(dat, alpha) returns (c0, c1, c2) by exact polynomial fit in 1/s on s = 2e4 * 2^j (j=0..6), 60 digits.
quadratic forms: Q0^{ab}, Q1^{ab} (symmetric 4x4, K(alpha) = alpha_a alpha_b Q^{ab}) by polarisation."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from gauss_tools import *
mp.mp.dps = 60
terms_r2 = load_terms(name='r2', k=2)
SJ = [mp.mpf(2 * 10 ** 4) * 2 ** j for j in range(7)]

def tail(dat, alpha, terms=terms_r2):
    Ks = [integrand(terms, dat, alpha, s_)[0] for s_ in SJ]
    n = len(SJ)
    A = mp.matrix(n, n)
    for i, s_ in enumerate(SJ):
        for j in range(n):
            A[i, j] = (1 / s_) ** j
    b = mp.matrix(Ks)
    x = mp.lu_solve(A, b)
    return x[0], x[1], x[2]

def forms(dat, terms=terms_r2):
    """returns Q0, Q1, Q2 as 4x4 complex mp matrices"""
    base = {}
    def val(al):
        key = tuple(al)
        if key not in base:
            base[key] = tail(dat, al, terms)
        return base[key]
    Q = [mp.matrix(4, 4) for _ in range(3)]
    E = np.eye(4)
    d = [val(E[i]) for i in range(4)]
    for i in range(4):
        for k in range(3):
            Q[k][i, i] = d[i][k]
    for i in range(4):
        for j in range(i + 1, 4):
            v = val(E[i] + E[j])
            for k in range(3):
                Q[k][i, j] = Q[k][j, i] = (v[k] - d[i][k] - d[j][k]) / 2
    return Q

def to_np(M):
    return np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])
