"""SU(2)-invariant family  A = h(r) eta^3_{mu nu} x^mu dx^nu,  omega = dA, evaluated at x0=(r0,0,0,0) with
symbolic h-jet (h0,h1,h2,h3 = h and its r-derivatives at r0) over the field Q(r0,h0,h1,h2,h3)."""
import sympy as sp
from sympy import QQ
import jetlib as jl
from jetlib import Jet
import lib
import geom

def make_field(extra=()):
    syms = sp.symbols('r0 h0 h1 h2 h3') + tuple(extra)
    K = QQ.frac_field(*syms)
    return K, syms

def setup(K, order=3):
    jl.set_field(K.one, K.zero)
    jl.set_order(order)

def binom_sqrt(u, N):
    """sqrt(1+u) as a jet, u a jet with zero constant term."""
    K1 = jl.ONE
    res = Jet.const(K1)
    term = Jet.const(K1)
    coef = K1
    for k in range(1, N+1):
        coef = coef * (K1/2 - (k-1)) / k
        term = term * u
        res = res + term * coef
    return res

def omega_jets_su2(K, syms, hfun=None, anti=False, N_A=4):
    r0, h0, h1, h2, h3 = [K.convert(s) for s in syms[:5]]
    jl.set_order(N_A)
    y = [Jet.var(i) for i in range(4)]
    x = [Jet.const(r0) + y[0], y[1], y[2], y[3]]
    r2 = sum((xi*xi for xi in x), Jet())
    u = (r2 - Jet.const(r0*r0)) * (jl.ONE / (r0*r0))
    r = binom_sqrt(u, N_A) * r0
    dr = r - Jet.const(r0)
    if hfun is None:
        h = Jet.const(h0) + dr*h1 + dr*dr*(h2/2) + dr*dr*dr*(h3/6)
    else:
        h = hfun(dr)
    eta = lib.etabar() if anti else lib.eta3()
    E3 = eta[2]
    A = []
    for nu in range(4):
        t = Jet()
        for mu in range(4):
            e = E3[mu, nu]
            if e != 0:
                t = t + x[mu] * (jl.ONE * int(e))
        A.append(t * h)
    w = [[A[n].diff(m) - A[m].diff(n) for n in range(4)] for m in range(4)]
    jl.set_order(3)
    # truncate to order 3
    w = [[Jet({k: v for k, v in w[m][n].d.items() if sum(k) <= 3}) for n in range(4)] for m in range(4)]
    return w
