"""Non-collinear SU(2)-invariant J=0 solutions: reduce to ODE for h_i(r); chirality data (l,r) of the connection b and S = 8 tr a tr b + 16 tr(c c^T)."""
import numpy as np, sympy as sp
from sympy import QQ_I, Rational
import jetlib as jl
from jetlib import Jet
from common import use_gaussian, theta_from_omega
import su2_general as SG
import geom, lib
use_gaussian(3)
eta = [np.array(e.tolist(), dtype=float) for e in lib.eta3()]
etab = [np.array(e.tolist(), dtype=float) for e in lib.etabar()]
class Wrap:
    one = QQ_I(1); zero = QQ_I(0)
    @staticmethod
    def convert(x): return QQ_I.from_sympy(sp.Rational(x))
def solve_h2(p, q, s):
    x = -(10*p**2*q + 4*p*q**2 + 4*p*s**2 + q**3 + q*s**2)/(2*p**2)
    y = (-10*p**2*s + p*s*x + q**2*s + s**3)/(2*p**2 + p*q)
    return x, y, sp.Integer(0)

def data(p, q, s):
    x, y, z = solve_h2(p, q, s)
    c = [[p, q, x, 0], [0, s, y, 0], [0, 0, z, 0]]
    cc = [[Wrap.convert(sp.Rational(v)) for v in row] for row in c]
    w = SG.build_omega(Wrap, cc)
    geom.SIGN_OVERRIDE = None
    Th = theta_from_omega(w)
    J = [sum((Th[m][r]*Th[m][n].diff(r) for m in range(4) for r in range(4)), Jet()).c0() for n in range(4)]
    Ginv, G, rho = geom.metric_data(Th)
    f = lambda v: float(getattr(v, 'x', v))
    G0 = np.array([[f(G[i][j].c0()) for j in range(4)] for i in range(4)])
    Gi0 = np.linalg.inv(G0)
    B = np.zeros((4, 4, 4))
    for t in range(4):
        for m in range(4):
            for n in range(4):
                B[t, m, n] = f(sum((Th[r][t]*Th[m][n].diff(r) for r in range(4)), Jet()).c0())
    b = np.einsum('st,tmn->smn', G0, B)
    l = np.array([[0.25*np.sum(eta[k]*b[s_]) for k in range(3)] for s_ in range(4)])
    r = np.array([[0.25*np.sum(etab[k]*b[s_]) for k in range(3)] for s_ in range(4)])
    a_ = l.T@Gi0@l; b_ = r.T@Gi0@r; c_ = l.T@Gi0@r
    S = 8*np.trace(a_)*np.trace(b_) + 16*np.trace(c_@c_.T)
    return [str(j) for j in J], np.trace(a_), np.trace(b_), np.linalg.norm(c_), S, f(rho.c0())
print('collinear s=0 (chiral):')
for (p, q, s) in [(1, sp.Rational(-1, 2), 0), (1, sp.Rational(1, 3), 0)]:
    print(' ', (p, q, s), data(sp.Integer(p), sp.Rational(q), sp.Integer(s)))
print('non-collinear s != 0:')
for (p, q, s) in [(1, sp.Rational(-1, 2), sp.Rational(1, 2)), (1, sp.Rational(1, 3), sp.Rational(1)), (1, sp.Rational(-1), sp.Rational(2, 3)), (2, sp.Rational(1), sp.Rational(1))]:
    print(' ', (p, q, s), data(sp.Integer(p), sp.Rational(q), sp.Rational(s)))
