"""X2 (round 2). Time x Heisenberg, [E_3,E_1] = kappa E_2, with the wider ansatz
  w_a^{cd} = k_a (a B^{cd} + zeta N^{cd} + x N'^{cd}),  k_a = (1,0,1,0),
in the normalisation of bg.py / symgeom.py (first-order part E_a + 1/2 w S at u = 1,
i.e. e^mu omega_mu = -w in the coordinate form of the manuscript).
Part 1 (exact, sympy, symbolic kappa, a, zeta, x): first two brackets B1, B2; solution set;
  trace T, T^2, R^2, the Lorentz scalar R_ab^{ab} (= sum_b Ric_b^b, no metric weight), and the
  third bracket nabla^a F_ab - T_ab^c F^a_c with F_ab = -c_ab^c t_c, t = T_ac^c / 2.
Part 2: the weighted sum sum_b Ric_b^b eta_bb that symgeom.py prints as 'scal' (not a Lorentz
  scalar) versus the true scalar, on family (i) and on (ii).
Run: python -I x2_heisenberg_kB.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from symgeom import geometry, gen, zeroC, W_from, PA

R4 = range(4)
eta = sp.diag(-1, 1, 1, 1)
kap = sp.symbols('kappa', positive=True)
a, z, x, s, tau = sp.symbols('a zeta x s tau', real=True)
B = gen({(0, 2): 1}); N1 = gen({(0, 1): 1, (1, 2): 1}); N2 = gen({(0, 3): 1, (2, 3): -1})
k = [1, 0, 1, 0]


def third_bracket(C, g):
    Om, T = g['Om'], g['T']
    t = [sp.Rational(1, 2) * g['trace'][c] for c in R4]
    F = [[-sum(C[p][q][c] * t[c] for c in R4) for q in R4] for p in R4]
    nF = [[[sum(Om[xx][p][zz] * F[zz][q] + Om[xx][q][zz] * F[p][zz] for zz in R4) for q in R4] for p in R4] for xx in R4]
    etai = eta.inv()
    Fup = [[sum(etai[p, r] * F[r][q] for r in R4) for q in R4] for p in R4]   # F^p_q
    Q = [sp.simplify(sum(etai[xx, p] * nF[xx][p][q] for xx in R4 for p in R4)
                     - sum(T[p][q][c] * Fup[p][c] for p in R4 for c in R4)) for q in R4]
    return F, Q


def true_scalar(g):
    return sp.simplify(sum(g['Ric'][b, b] for b in R4))


CH = zeroC(); CH[3][1][2] = kap; CH[1][3][2] = -kap
g = geometry(CH, W_from([(k, a * B + z * N1 + x * N2)]), eta)
print('== Heisenberg, w = k (a B + zeta N + x N\'), symbolic')
e1 = sorted(set(sp.factor(v) for v in g['B1'] if sp.simplify(v) != 0), key=str)
e2 = sorted(set(sp.factor(v) for v in g['B2'].values() if sp.simplify(v) != 0), key=str)
print('  B1 nonzero entries:', e1)
print('  B2 nonzero entries:', e2)
print('  so the first two brackets hold for all kappa, a, zeta, x' if not e1 and not e2 else '  constraints present')
for sol in [{a: a}, {a: kap}, {a: -kap}, {a: 0}]:
    gg = geometry(CH, W_from([(k, (sol[a]) * B + z * N1 + x * N2)]), eta)
    b1 = all(sp.simplify(v) == 0 for v in gg['B1']); b2 = all(sp.simplify(v) == 0 for v in gg['B2'].values())
    F, Q = third_bracket(CH, gg)
    print('-- a =', sol[a], ': B1 = 0:', b1, '; B2 = 0:', b2)
    print('   trace T =', [sp.simplify(v) for v in gg['trace']], '; T_abc T^abc =', sp.simplify(gg['TT']))
    print('   R_abcd R^abcd =', sp.simplify(gg['RR']), '; scalar R_ab^ab =', true_scalar(gg))
    print('   F_ab nonzero (a<b):', {(p, q): sp.simplify(F[p][q]) for p in R4 for q in R4 if p < q and sp.simplify(F[p][q]) != 0})
    print('   third bracket nabla^a F_ab - T_ab^c F^a_c =', Q)
    nzR = [((p, q), cd, sp.simplify(gg['Rup'][p][q][cd[0]][cd[1]])) for p in R4 for q in R4 if p < q
           for cd in PA if sp.simplify(gg['Rup'][p][q][cd[0]][cd[1]]) != 0]
    print('   nonzero R_ab^{cd} (a<b, c<d):', nzR)
    print('   Ricci R_ab^{ae} (row b):', [[sp.simplify(v) for v in row] for row in gg['Ric'].tolist()])
    print('   rank of R as map pairs->so(3,1):', gg['Rmat'].rank(simplify=True))
print('== scalar check on family (i): w = s k B + m N on the hyperbola (flat frame)')
m = [0, s * (1 + (tau + 1 / tau) / 2), 0, s * (tau - 1 / tau) / 2]
gF = geometry(zeroC(), W_from([(k, s * B), (m, N1)]), eta)
print('  true scalar sum_b Ric_b^b =', true_scalar(gF), '; weighted sum_b Ric_b^b eta_bb (symgeom scal) =', sp.factor(gF['scal_weighted']),
      '; -2 s m_1 =', sp.factor(-2 * s * m[1]))
gH = geometry(CH, W_from([(k, z * N1 + x * N2)]), eta)
print('  family (ii): true scalar =', true_scalar(gH), '; weighted =', sp.simplify(gH['scal_weighted']))
