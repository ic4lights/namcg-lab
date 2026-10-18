"""Minimal truncated 4-variable jets with coefficients in a field (Fraction or sympy FracField elements).
Order N is a module-level setting; products are truncated at total degree N."""
from fractions import Fraction
from itertools import product
import sympy as sp

N = 4
ONE = Fraction(1)
ZERO = Fraction(0)

def isz(v):
    return v == ZERO or v == 0

def set_order(n):
    global N
    N = n

def set_field(one, zero):
    global ONE, ZERO
    ONE, ZERO = one, zero

class Jet:
    __slots__ = ('d',)
    def __init__(self, d=None):
        self.d = d if d is not None else {}
    @staticmethod
    def const(c):
        return Jet({(0, 0, 0, 0): c}) if not isz(c) else Jet()
    @staticmethod
    def var(i, c=None):
        m = [0, 0, 0, 0]; m[i] = 1
        return Jet({tuple(m): ONE if c is None else c})
    def __add__(self, o):
        if not isinstance(o, Jet): o = Jet.const(o)
        d = dict(self.d)
        for k, v in o.d.items():
            nv = d.get(k, 0) + v
            if isz(nv):
                d.pop(k, None)
            else:
                d[k] = nv
        return Jet(d)
    __radd__ = __add__
    def __neg__(self):
        return Jet({k: -v for k, v in self.d.items()})
    def __sub__(self, o):
        if not isinstance(o, Jet): o = Jet.const(o)
        return self + (-o)
    def __rsub__(self, o):
        return (-self) + o
    def __mul__(self, o):
        if not isinstance(o, Jet):
            if isz(o): return Jet()
            return Jet({k: v*o for k, v in self.d.items()})
        d = {}
        for k1, v1 in self.d.items():
            s1 = sum(k1)
            for k2, v2 in o.d.items():
                if s1 + sum(k2) > N: continue
                k = (k1[0]+k2[0], k1[1]+k2[1], k1[2]+k2[2], k1[3]+k2[3])
                nv = d.get(k, 0) + v1*v2
                if isz(nv): d.pop(k, None)
                else: d[k] = nv
        return Jet(d)
    __rmul__ = __mul__
    def c0(self):
        return self.d.get((0, 0, 0, 0), ZERO)
    def inv(self):
        a0 = self.c0()
        dl = (self - a0) * (ONE/a0)
        res = Jet.const(ONE); term = Jet.const(ONE)
        for _ in range(N):
            term = (-term) * dl
            res = res + term
        return res * (ONE/a0)
    def __truediv__(self, o):
        if not isinstance(o, Jet): return self * (ONE/o)
        return self * o.inv()
    def diff(self, i):
        d = {}
        for k, v in self.d.items():
            if k[i] > 0:
                kk = list(k); kk[i] -= 1
                d[tuple(kk)] = v*k[i]
        return Jet(d)
    def powi(self, n):
        r = Jet.const(ONE)
        for _ in range(n): r = r*self
        return r
    def __repr__(self):
        return f"Jet({self.d})"

def jzero(): return Jet()
def jmat(n, m=None):
    m = n if m is None else m
    return [[Jet() for _ in range(m)] for _ in range(n)]

def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][l]*B[l][j] for l in range(k)), Jet()) for j in range(m)] for i in range(n)]

def madd(A, B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A, B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mscal(A, c): return [[A[i][j]*c for j in range(len(A[0]))] for i in range(len(A))]
def mT(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def mtr(A): return sum((A[i][i] for i in range(len(A))), Jet())
def meye(n): return [[Jet.const(ONE) if i == j else Jet() for j in range(n)] for i in range(n)]
def mdiff(A, i): return [[A[a][b].diff(i) for b in range(len(A[0]))] for a in range(len(A))]

def minv(A):
    """Gauss-Jordan inverse of a square matrix of jets; pivots must have non-zero constant part."""
    n = len(A)
    M = [row[:] + [Jet.const(ONE) if i == j else Jet() for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = None
        for r in range(c, n):
            if not isz(M[r][c].c0()):
                p = r; break
        M[c], M[p] = M[p], M[c]
        pinv = M[c][c].inv()
        M[c] = [e*pinv for e in M[c]]
        for r in range(n):
            if r != c and (M[r][c].d):
                f = M[r][c]
                M[r] = [M[r][j] - f*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def pf4(w):
    return w[0][1]*w[2][3] - w[0][2]*w[1][3] + w[0][3]*w[1][2]
