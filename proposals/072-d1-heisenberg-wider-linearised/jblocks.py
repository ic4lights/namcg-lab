"""Exact helpers for 072: J-blocks of the forty linearised equations (and of the order-zero operator Q) on
the wider Heisenberg family at zeta = x = 0, where J = n + (helicity in the 1-3 plane) commutes with the
operator.  The oscillator basis is rescaled, |n>' = sqrt(n!)|n>, so a|n>' = n|n-1>', a^dag|n>' = |n+1>'
(a similarity: ranks and determinantal divisors unchanged up to constants), and all matrix entries are
Gaussian rationals when kappa p / 2 = s^2 with s rational.  The double-precision entries of core068.M_op /
lin.Qop are reconstructed as rationals (denominator <= 1e5, residual < 1e-10 asserted); every later step
(helicity basis, compressions, determinants, interpolation, gcd, division) is exact over QQ(i)."""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
from common import K, Tl, lin, wider
import numpy as np
import sympy as sp
from sympy import QQ_I, Poly
from sympy.polys.matrices import DomainMatrix

q = sp.Symbol('q0')
R13 = np.zeros((4, 4)); R13[1, 3] = 1; R13[3, 1] = -1


def _rho(v):
    h, w = K.unpack(v, 1)
    h2 = np.einsum('ax,xcn->acn', R13, h) + np.einsum('cx,axn->acn', R13, h)
    w2 = (np.einsum('ax,xcdn->acdn', R13, w) + np.einsum('cx,axdn->acdn', R13, w)
          + np.einsum('dx,acxn->acdn', R13, w))
    return K.pack_hw(h2, w2)


def rho40():
    return np.array([_rho(np.eye(40)[i]) for i in range(40)]).T


def helicity_basis(Rho):
    nc = Rho.shape[0]
    iR = sp.Matrix(nc, nc, lambda i, j: int(round((1j * Rho[i, j]).real)) + sp.I * int(round((1j * Rho[i, j]).imag)))
    assert max(abs(complex(iR[i, j]) - 1j * Rho[i, j]) for i in range(nc) for j in range(nc)) < 1e-12
    P = []; lams = []
    for lam in range(-3, 4):
        ns = (iR - lam * sp.eye(nc)).nullspace(); P += ns; lams += [lam] * len(ns)
    assert len(lams) == nc
    P = sp.Matrix.hstack(*P)
    return np.array(P.evalf(), dtype=complex), np.array(P.inv().evalf(), dtype=complex), lams


def rat(x):
    fr = Fraction(x.real).limit_denominator(10 ** 5); fi = Fraction(x.imag).limit_denominator(10 ** 5)
    assert abs(float(fr) - x.real) < 1e-10 and abs(float(fi) - x.imag) < 1e-10, x
    return QQ_I(sp.Rational(fr.numerator, fr.denominator), sp.Rational(fi.numerator, fi.denominator))


def modes_resc(p, q0, N, kappa):
    a = np.diag(np.arange(1, N), 1).astype(complex); ad = np.diag(np.ones(N - 1), -1).astype(complex)
    I = np.eye(N, dtype=complex); s = np.sqrt(kappa * p / 2.0)
    return np.array([1j * q0 * I, s * (a - ad), 1j * p * I, -1j * s * (a + ad)])


def block(opfun, ncomp, basis, kap, p, chi, J, N):
    """Quadratic coefficients (A, B, C) of the J-block of opfun on C^ncomp (x) C^N, the selected
    (helicity component, level) pairs, and the largest entry coupling the block to other rows
    (rows of the exact levels only: the top two levels carry the truncation defect)."""
    Pn, Pin, lams = basis
    C, W = wider(kap, chi, 0, 0)
    Mf = lambda q0: opfun(C, W, modes_resc(p, q0, N, kap))
    A0, B0, C0 = Tl.quad_coeffs(Mf)
    sel = [(j, J - lams[j]) for j in range(ncomp) if 0 <= J - lams[j] <= N - 3]
    BigP = np.kron(Pn, np.eye(N)); BigPi = np.kron(Pin, np.eye(N))
    ids = [j * N + n for (j, n) in sel]
    other = [i for i in range(ncomp * N) if i not in ids and (i % N) <= N - 3]
    out = []; leak = 0.0
    for X in (A0, B0, C0):
        Y = BigPi @ X @ BigP
        out.append(Y[np.ix_(ids, ids)])
        if other and ids:
            leak = max(leak, float(np.abs(Y[np.ix_(other, ids)]).max()))
    return out, sel, leak


def interp(xs, ys):
    n = len(xs); c = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            c[i] = (c[i] - c[i - 1]) / (xs[i] - xs[i - j])
    P = Poly(QQ_I.to_sympy(c[-1]), q, domain=QQ_I)
    for i in range(n - 2, -1, -1):
        P = P * Poly(q - QQ_I.to_sympy(xs[i]), q, domain=QQ_I) + Poly(QQ_I.to_sympy(c[i]), q, domain=QQ_I)
    return P


def det_divisor(mats, seeds=(0, 1)):
    """gcd of det(X M(q0) Y) over two random integer compressions to the generic rank r: with probability
    one the r-th determinantal divisor of M(q0) (product of its invariant factors), exact over QQ(i)."""
    n = mats[0].shape[0]
    z = 0.371 + 0.12j
    r = K.rank(mats[0] + z * mats[1] + z * z * mats[2])
    A, B, C = [DomainMatrix([[rat(m[i, j]) for j in range(n)] for i in range(n)], (n, n), QQ_I) for m in mats]
    polys = []
    for sd in seeds:
        rng = np.random.default_rng(sd)
        X = DomainMatrix([[QQ_I(int(v)) for v in rng.integers(-3, 4, size=n)] for _ in range(r)], (r, n), QQ_I)
        Y = DomainMatrix([[QQ_I(int(v)) for v in rng.integers(-3, 4, size=r)] for _ in range(n)], (n, r), QQ_I)
        a, b, c = X * A * Y, X * B * Y, X * C * Y
        xs = [QQ_I(k - r) for k in range(2 * r + 1)]
        ys = [(a + b * x + c * (x * x)).det() for x in xs]
        polys.append(interp(xs, ys))
    return r, n, polys[0].gcd(polys[1]), polys


def factor_on_levels(g, kap, p, chi, cs=(-1, 1, 3), lmax=15):
    rem = g; found = []
    for c in cs:
        for l in range(-1, lmax + 1, 2):
            Pc = Poly(q ** 2 - p ** 2 + sp.I * c * chi * (q - p) - kap * p * l, q, domain=QQ_I); m = 0
            while True:
                qq, rr = rem.div(Pc)
                if rr.is_zero:
                    rem = qq; m += 1
                else:
                    break
            if m:
                found.append((c, l, m))
    return found, rem
