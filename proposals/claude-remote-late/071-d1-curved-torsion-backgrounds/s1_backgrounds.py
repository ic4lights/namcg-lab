"""S1. Exact backgrounds of the first-order equivariant class with R != 0 and T != 0.
Left-invariant data, eta = diag(-1,1,1,1).  Generators (X^{cd}, antisymmetric):
  B  = J^{02}                       (boost in the 0-2 plane)
  N1 = J^{01} + J^{12},  N2 = J^{03} - J^{23}  (null rotations fixing n^a = (1,0,-1,0)),
  k_a = (1,0,1,0)  (so k^a = (-1,0,1,0) is null, proportional to -n).
Family F_tau (flat frame, C = 0):  w_a = s k_a B + m_a N1,  m = (0, m_1, 0, m_3) with
  m_1 = s (1 + (tau + 1/tau)/2),  m_3 = s (tau - 1/tau)/2,  tau != 0 real,
  i.e. the hyperbola (m_1 - s)^2 - m_3^2 = s^2 (the vanishing locus of B1 in this ansatz).
Family H (time x Heisenberg, [E_3,E_1] = kappa E_2):  w_a = k_a (z N1 + x N2).
Claims (exact, sympy, symbolic parameters): B1 = B2 = 0; R != 0; T != 0; invariants.
Run: python -I s1_backgrounds.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from symgeom import *

eta = sp.diag(-1, 1, 1, 1)
s, kap, z, x = sp.symbols('s kappa zeta x', real=True)
tau = sp.symbols('tau', real=True, nonzero=True)
B = gen({(0, 2): 1}); N1 = gen({(0, 1): 1, (1, 2): 1}); N2 = gen({(0, 3): 1, (2, 3): -1})
k = [1, 0, 1, 0]


def report(name, C, W, assume=None):
    g = geometry(C, W, eta)
    sub = assume or {}
    def S(e): return sp.simplify(sp.trigsimp(sp.sympify(e).subs(sub)))
    b1 = all(S(v) == 0 for v in g['B1'])
    b2 = all(S(v) == 0 for v in g['B2'].values())
    print('==', name)
    print('  B1 == 0 identically:', b1, '; B2 == 0 identically:', b2)
    print('  trace T_ac^c =', [S(t) for t in g['trace']], '; T_abc T^abc =', S(g['TT']))
    print('  R_abcd R^abcd =', S(g['RR']), '; scalar R_ab^ab =', S(g['scal']))
    nzR = [((a, b), cd, S(g['Rup'][a][b][cd[0]][cd[1]])) for a in range(4) for b in range(4) if a < b
           for cd in PA if S(g['Rup'][a][b][cd[0]][cd[1]]) != 0]
    print('  nonzero R_ab^{cd} (a<b, c<d):', nzR)
    print('  Ricci R_ab^{ae} (row b, column e):', [[S(v) for v in row] for row in g['Ric'].tolist()])
    print('  rank of R as map pairs->so(3,1):', g['Rmat'].subs(sub).rank(simplify=True))
    return g


C0 = zeroC()
a1, a3 = sp.symbols('m1 m3', real=True)
gd = geometry(C0, W_from([(k, s * B), ([0, a1, 0, a3], N1)]), eta)
print('== ansatz w = s k B + m N1, m = (0, m1, 0, m3) general:')
print('  B1 nonzero entries:', sorted(set(sp.factor(v) for v in gd['B1'] if sp.simplify(v) != 0), key=str))
print('  B2 nonzero entries:', sorted(set(sp.factor(v) for v in gd['B2'].values() if sp.simplify(v) != 0), key=str))
m = [0, s * (1 + (tau + 1 / tau) / 2), 0, s * (tau - 1 / tau) / 2]
gF = report('F_tau: flat frame, w = s k B + m N1 on the hyperbola', C0, W_from([(k, s * B), (m, N1)]))
for val, lab in [(sp.Integer(1), 'tau = 1 (m = (0,2s,0,0))'), (-2 + sp.sqrt(3), 'tau = -2+sqrt3 (m = (0,-s,0,sqrt3 s), trace-free)')]:
    gg = geometry(C0, W_from([(k, s * B), ([sp.simplify(sp.sympify(mm).subs(tau, val)) for mm in m], N1)]), eta)
    print('  ', lab, ': m =', [sp.simplify(sp.sympify(mm).subs(tau, val)) for mm in m], 'trace =', [sp.simplify(t) for t in gg['trace']],
          'B1,B2 zero:', all(sp.simplify(v) == 0 for v in gg['B1']) and all(sp.simplify(v) == 0 for v in gg['B2'].values()),
          'scalar R_ab^ab:', gg['scal'], '; round-1 weighted sum (not a scalar):', gg['scal_weighted'])
# Heisenberg family
CH = zeroC(); CH[3][1][2] = kap; CH[1][3][2] = -kap
gH = report('H: [E3,E1] = kappa E2, w = k (zeta N1 + x N2)', CH, W_from([(k, z * N1 + x * N2)]))
# Levi-Civita curvature of the frames: F flat (C = 0); H: time x Heisenberg (computed in invariants.py)
