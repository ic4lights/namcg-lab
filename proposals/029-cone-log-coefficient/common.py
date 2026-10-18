import sympy as sp
from sympy import QQ_I, Rational
import jetlib as jl
from jetlib import Jet
import itertools, random

def use_gaussian(order=3):
    jl.set_order(order)
    jl.set_field(QQ_I(1), QQ_I(0))

def Q(a, b=1):
    return QQ_I.from_sympy(sp.Rational(a, b))

def hodge_j(w):
    H = [[Jet() for _ in range(4)] for _ in range(4)]
    for m in range(4):
        for n in range(4):
            t = Jet()
            for r in range(4):
                for s in range(4):
                    e = sp.LeviCivita(m, n, r, s)
                    if e != 0:
                        t = t + w[r][s] * (jl.ONE * int(e))
            H[m][n] = t * (jl.ONE / 2)
    return H

def theta_from_omega(w):
    P = jl.pf4(w)
    Pi = P.inv()
    H = hodge_j(w)
    return [[-(H[m][n] * Pi) for n in range(4)] for m in range(4)]

def omega_from_A(A):
    return [[A[n].diff(m) - A[m].diff(n) for n in range(4)] for m in range(4)]

def point_shift(x0):
    # jets for x_i = x0_i + y_i
    return [Jet.var(i) + Jet.const(Q(x0[i][0], x0[i][1]) if isinstance(x0[i], tuple) else Q(x0[i])) for i in range(4)]

def gammas():
    I = sp.I
    s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
    sig = [s1, s2, s3]
    Z = sp.zeros(2, 2); E = sp.eye(2)
    gam = []
    for k in range(3):
        top = sp.Matrix(sp.BlockMatrix([[Z, -I*sig[k]], [I*sig[k], Z]]))
        gam.append(top)
    gam.append(sp.Matrix(sp.BlockMatrix([[Z, E], [E, Z]])))
    # check Clifford
    for a in range(4):
        for b in range(4):
            ac = gam[a]*gam[b] + gam[b]*gam[a]
            assert sp.simplify(ac - (2 if a == b else 0)*sp.eye(4)) == sp.zeros(4, 4)
    return gam

def gam_mn_domain():
    gam = gammas()
    out = [[None]*4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            M = (gam[m]*gam[n] - gam[n]*gam[m]) / 2
            out[m][n] = [[QQ_I.from_sympy(sp.nsimplify(M[i, j])) for j in range(4)] for i in range(4)]
    return out

def quat_L():
    """Real 4x4 matrices of left multiplication by quaternion units i,j,k on basis (1,i,j,k)."""
    import numpy as np
    # multiplication table
    def qmul(a, b):
        a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
        return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
    units = [(0,1,0,0), (0,0,1,0), (0,0,0,1)]
    out = []
    for u in units:
        M = sp.zeros(4, 4)
        for c in range(4):
            e = [0]*4; e[c] = 1
            col = qmul(u, tuple(e))
            for r in range(4):
                M[r, c] = col[r]
        out.append(M)
    # check L_i L_j = eps_ijk L_k
    assert out[0]*out[1] == out[2] and out[1]*out[2] == out[0] and out[2]*out[0] == out[1]
    return out

def gam_weyl_real(block, dom=None):
    """block 'upper': gamma^{mn} = -etabar^k_{mn} tau_k ; 'lower': -eta^k_{mn} tau_k ; tau_k -> L_k (real 4x4)."""
    import lib
    L = quat_L()
    E = lib.etabar() if block == 'upper' else lib.eta3()
    out = [[None]*4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            M = sum((-E[k][m, n]*L[k] for k in range(3)), sp.zeros(4, 4))
            if dom is None:
                out[m][n] = [[sp.Rational(M[i, j]) for j in range(4)] for i in range(4)]
            else:
                out[m][n] = [[dom.from_sympy(sp.Rational(M[i, j])) for j in range(4)] for i in range(4)]
    return out
