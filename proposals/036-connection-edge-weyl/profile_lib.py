"""Helpers shared by gap_profile.py and hodge_maxwell_check.py: delta Riemann tensor of the diagonal profile and the (W, Rsig) fit."""
import itertools, sympy as sp
from sympy import Rational as Q

def Rprime(ca_, cb_):
    Rp = {}
    N, P = (0, 1), (2, 3)
    for (m, n, r, s) in itertools.product(range(4), repeat=4):
        v = 0
        if all(i in N for i in (m, n, r, s)):
            v = ca_ * (int(m == r)*int(n == s) - int(m == s)*int(n == r))
        else:
            # R'_{a i b j} = (cb/2) d_ab d_ij with a,b normal, i,j parallel; fix by (anti)symmetries
            def comp(a, i, b, j): return Q(1, 2)*cb_*int(a == b)*int(i == j)
            if m in N and n in P and r in N and s in P: v = comp(m, n, r, s)
            elif m in P and n in N and r in P and s in N: v = comp(n, m, s, r)
            elif m in N and n in P and r in P and s in N: v = -comp(m, n, s, r)
            elif m in P and n in N and r in N and s in P: v = -comp(n, m, r, s)
        Rp[(m, n, r, s)] = v
    return Rp
def fit(ms, vals):
    aW, aS = sp.symbols('aW aS')
    sol = sp.solve([vals[i]-aW*ms[i]['W']-aS*ms[i]['Rsig'] for i in range(2)], [aW, aS], dict=True)[0]
    res = {sp.simplify(vals[i]-sol[aW]*ms[i]['W']-sol[aS]*ms[i]['Rsig']) for i in range(2, len(ms))}
    assert res == {0}, res
    return sp.simplify(sol[aW]), sp.simplify(sol[aS])
