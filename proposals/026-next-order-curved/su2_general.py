"""General SU(2)-invariant closed 2-forms  omega = d( sum_i h_i(r) Lambda^i ), Lambda^i = eta^i_{mu nu} x^mu dx^nu,
evaluated at x0=(r0,0,0,0).  Symbols: r0 = 1, h_i^{(k)} = c[i][k], k=0..3.
Computes J(0), chirality data (l, r of N^sigma) etc."""
import sympy as sp
from sympy import QQ
import jetlib as jl
from jetlib import Jet
import lib
import su2_family as F

def build_omega(K, c, r0=None, N_A=4):
    """c[i][k] elements of K (h_i^{(k)} at r0); r0 element of K (default 1)."""
    r0 = K.one if r0 is None else r0
    jl.set_order(N_A)
    y = [Jet.var(i) for i in range(4)]
    x = [Jet.const(r0) + y[0], y[1], y[2], y[3]]
    r2 = sum((xi*xi for xi in x), Jet())
    u = (r2 - Jet.const(r0*r0)) * (jl.ONE/(r0*r0))
    r = F.binom_sqrt(u, N_A) * r0
    dr = r - Jet.const(r0)
    eta = lib.eta3()
    A = [Jet() for _ in range(4)]
    for i in range(3):
        h = Jet.const(c[i][0]) + dr*c[i][1] + dr*dr*(c[i][2]/2) + dr*dr*dr*(c[i][3]/6)
        for nu in range(4):
            t = Jet()
            for mu in range(4):
                e = eta[i][mu, nu]
                if e != 0:
                    t = t + x[mu]*(jl.ONE*int(e))
            A[nu] = A[nu] + t*h
    w = [[A[n].diff(m) - A[m].diff(n) for n in range(4)] for m in range(4)]
    jl.set_order(3)
    w = [[Jet({k: v for k, v in w[m][n].d.items() if sum(k) <= 3}) for n in range(4)] for m in range(4)]
    return w
