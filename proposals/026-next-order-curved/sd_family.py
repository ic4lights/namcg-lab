"""Self-dual closed 2-forms omega = b_i eta^i (eta^i 't Hooft symbols), polynomial solutions of d omega = 0.
Returns jets of omega about a chosen point."""
import itertools, random
import sympy as sp
from sympy import Rational
import jetlib as jl
from jetlib import Jet
from common import *
import lib

X = sp.symbols('x1:5')

def sd_solution(deg=3, seed=0, anti=False, b0=(1, 2, 3)):
    """Return sympy polynomials b_1..b_3 in x with d(b_i eta^i)=0, b(0)=b0."""
    random.seed(seed)
    mons = [m for m in itertools.product(range(deg+1), repeat=4) if sum(m) <= deg]
    syms = sp.symbols('c0:%d' % (3*len(mons)))
    b = []
    for i in range(3):
        b.append(sum(syms[i*len(mons)+k]*sp.prod([X[a]**mons[k][a] for a in range(4)]) for k in range(len(mons))))
    eta = lib.etabar() if anti else lib.eta3()
    omega = sum((b[i]*eta[i] for i in range(3)), sp.zeros(4, 4))
    # closure: d omega = 0 : d_a w_bc + d_b w_ca + d_c w_ab = 0
    eqs = []
    for a, bb, c in itertools.combinations(range(4), 3):
        e = sp.diff(omega[bb, c], X[a]) + sp.diff(omega[c, a], X[bb]) + sp.diff(omega[a, bb], X[c])
        eqs.append(sp.expand(e))
    lin = []
    for e in eqs:
        P = sp.Poly(e, *X)
        lin += list(P.coeffs())
    # b(0)=b0 : coefficient of constant monomial
    zero_idx = mons.index((0, 0, 0, 0))
    cons = [syms[i*len(mons)+zero_idx] - b0[i] for i in range(3)]
    sol = sp.linsolve(lin + cons, *syms)
    sol = list(sol)[0]
    free = sorted(set().union(*[s.free_symbols for s in sol]), key=lambda s: str(s))
    sub = {f: Rational(random.randint(-4, 4), random.randint(1, 4)) for f in free}
    vals = [s.subs(sub) for s in sol]
    bsol = [sp.expand(b[i].subs(dict(zip(syms, vals)))) for i in range(3)]
    return bsol, eta

def omega_jets(bsol, eta, x0):
    """omega as 4x4 of Jets about the point x0 (tuple of rationals)."""
    out = []
    sh = {X[i]: X[i] + x0[i] for i in range(4)}
    w = sp.zeros(4, 4)
    for i in range(3):
        w += sp.expand(bsol[i].subs(sh, simultaneous=True)) * eta[i]
    Y = sp.symbols('y1:5')
    res = [[Jet() for _ in range(4)] for _ in range(4)]
    for m in range(4):
        for n in range(4):
            e = sp.expand(w[m, n].subs({X[i]: Y[i] for i in range(4)}, simultaneous=True))
            if e == 0: continue
            P = sp.Poly(e, *Y)
            d = {}
            for mon, co in P.terms():
                if sum(mon) <= jl.N:
                    d[mon] = QQ_I.from_sympy(sp.Rational(co))
            res[m][n] = Jet(d)
    return res
