"""S1 (exact, sympy).  Section-value equations of the first-order class on time x Heisenberg with the constant
connection of common073.family, independent sympy re-implementation of the conventions of 071 bg.py:
  Om_ab^c = w_a^{cd} eta_db, T_ab^c = -C_ab^c - Om_ab^c + Om_ba^c,
  R_ab^f_c = Om_ac^d Om_bd^f - Om_bc^d Om_ad^f - C_ab^d Om_dc^f,
  B1_b^e = -nabla^a T_ab^e + T_ab^c T^a_c^e + R_ab^{ae},  B2_b^{de} = nabla^a R_ab^{de} - T_ab^c R^a_c^{de}.
Checks, for symbolic kappa, s (c^2 = 1 - s^2), chi, th, zeta, x, al, be, ga:
 (a) s arbitrary, tau = chi + al + ga = 0 and the constraint: B1 = B2 = 0 identically;
 (b) s = 0, tau free, constraint: B1 = B2 = 0 identically;
 (c) s free, constraint only: every remaining component is divisible by kappa s tau;
 (d) invariants R_abcd R^abcd, R_ab^{ab}, T_abc T^abc, T_ac^c;
 (e) third bracket nabla^a F_ab - T_ab^c F^a_c for F_ab = -C_ab^c t_c, t = T_ac^c / 2 (s = 0, tau free);
 (f) the connection fixes the null line n (W_a n = lambda_a n); the leg operator L = eta^{ab} W_a W_b on vectors
     is -(eta^{ab}(P_a P_b + Q_a Q_b)) n n^flat, so L^2 = 0; the leg form eta^{ab} w_a^{cd} w_b^{ef} is nonzero;
 (g) the linearised third bracket: Q_b - Q_b|_{w=0} = -tau k^a F_ab for every F (no constraint used).
Run: python -I -B s1_family_exact.py"""
import time
import sympy as sp

t0 = time.time()
eta = sp.diag(-1, 1, 1, 1); ei = eta.inv(); r4 = range(4)
kap = sp.Symbol('kappa', positive=True)
cs, sn = sp.symbols('c s', real=True)
chi, th, ze, x, al, be, ga = sp.symbols('chi vartheta zeta x alpha beta gamma', real=True)


def wedge(u, v):
    return [[u[c] * v[d] - u[d] * v[c] for d in r4] for c in r4]


n = [1, sn, -cs, 0]; e = [0, cs, sn, 0]; f = [0, 0, 0, 1]; mnh = [0, -sn, cs, 0]; e0 = [1, 0, 0, 0]
low = lambda v: [sum(eta[a, b] * v[b] for b in r4) for a in r4]
k = [-z for z in low(n)]; eL = low(e); fL = low(f)
Bn, Jn, Ne, Nf = wedge(e0, mnh), wedge(e, f), wedge(n, e), wedge(n, f)
P = [ze * k[a] + al * eL[a] + (be + th) * fL[a] for a in r4]
Q = [x * k[a] + be * eL[a] + ga * fL[a] for a in r4]
W = [[[k[a] * (chi * Bn[c][d] + th * Jn[c][d]) + P[a] * Ne[c][d] + Q[a] * Nf[c][d] for d in r4] for c in r4] for a in r4]
C = [[[sp.S(0)] * 4 for _ in r4] for _ in r4]; C[3][1][2] = kap; C[1][3][2] = -kap

Om = [[[sum(W[a][c][d] * eta[d, b] for d in r4) for c in r4] for b in r4] for a in r4]
T = [[[-C[a][b][c] - Om[a][b][c] + Om[b][a][c] for c in r4] for b in r4] for a in r4]
R = [[[[sum(Om[a][c][d] * Om[b][d][ff] - Om[b][c][d] * Om[a][d][ff] - C[a][b][d] * Om[d][c][ff] for d in r4)
        for ff in r4] for c in r4] for b in r4] for a in r4]
Rup = [[[[sum(eta[c, ee] * R[a][b][c][ff] for c in r4) for ee in r4] for ff in r4] for b in r4] for a in r4]
nT = [[[[sum(Om[xx][a][z] * T[z][b][ee] + Om[xx][b][z] * T[a][z][ee] - Om[xx][z][ee] * T[a][b][z] for z in r4)
         for ee in r4] for b in r4] for a in r4] for xx in r4]
B1 = [sp.expand(-sum(ei[xx, a] * nT[xx][a][b][ee] for xx in r4 for a in r4)
                + sum(T[a][b][c] * ei[a, xx] * T[xx][c][ee] for a in r4 for xx in r4 for c in r4)
                + sum(Rup[a][b][a][ee] for a in r4)) for b in r4 for ee in r4]
nR = [[[[[sum(Om[xx][a][z] * Rup[z][b][d][ee] + Om[xx][b][z] * Rup[a][z][d][ee] - Om[xx][z][d] * Rup[a][b][z][ee]
           - Om[xx][z][ee] * Rup[a][b][d][z] for z in r4) for ee in r4] for d in r4] for b in r4] for a in r4]
      for xx in r4]
B2 = [sp.expand(sum(ei[xx, a] * nR[xx][a][b][d][ee] for xx in r4 for a in r4)
                - sum(T[a][b][c] * ei[a, xx] * Rup[xx][c][d][ee] for a in r4 for xx in r4 for c in r4))
      for b in r4 for d in r4 for ee in r4]
eqs = [q for q in B1 + B2 if q != 0]
con = th ** 2 - 2 * th * be - 2 * be ** 2 - al ** 2 - ga ** 2 + 2 * chi * (al + ga)
tau = chi + al + ga


def red_c(p):
    return sp.expand(sp.rem(sp.Poly(sp.expand(p), cs), sp.Poly(cs ** 2 + sn ** 2 - 1, cs)).as_expr())


def red_con(p, cn):
    return sp.expand(sp.rem(sp.Poly(sp.expand(p), be), sp.Poly(sp.expand(cn), be)).as_expr())


print('nonzero bracket components before reduction:', len(eqs), '[%.0fs]' % (time.time() - t0))
ra = set(sp.simplify(red_c(red_con(red_c(q.subs(al, -chi - ga)), con.subs(al, -chi - ga)))) for q in eqs)
print('(a) s arbitrary, tau = 0, constraint: residual set', ra)
rb = set(sp.simplify(red_con(q.subs({cs: 1, sn: 0}), con)) for q in eqs)
print('(b) s = 0, tau free, constraint: residual set', rb)
rc = set(sp.expand(red_c(red_con(red_c(q), con))) for q in eqs) - {0}
divisible = all(sp.rem(sp.Poly(r, al), sp.Poly(tau, al)).is_zero and sp.Poly(r, sn).eval(0) == 0 for r in rc)
print('(c) s free, constraint only: every remainder vanishes at tau = 0 and at s = 0:', divisible,
      '; distinct remainders', len(rc))
RR = sp.expand(sum(Rup[a][b][c][d] ** 2 * eta[a, a] * eta[b, b] * eta[c, c] * eta[d, d]
                   for a in r4 for b in r4 for c in r4 for d in r4))
Rsc = sp.expand(sum(Rup[a][b][a][b] for a in r4 for b in r4))
TT = sp.expand(sum(T[a][b][c] ** 2 * eta[a, a] * eta[b, b] * eta[c, c] for a in r4 for b in r4 for c in r4))
trT = [sp.factor(red_c(sum(T[a][c][c] for c in r4))) for a in r4]
print('(d) R_abcd R^abcd - 4 kappa^2 c^2 (th^2 - chi^2) =', sp.simplify(red_c(RR - 4 * kap ** 2 * cs ** 2 * (th ** 2 - chi ** 2))))
print('    R_ab^{ab} =', sp.factor(red_c(Rsc)), ' ; T_abc T^abc =', sp.factor(red_c(TT)))
print('    T_ac^c - tau k_a =', [sp.simplify(trT[a] - tau * k[a]) for a in r4], ' ; k_a =', k)
sub0 = {cs: 1, sn: 0}
Om0 = [[[Om[a][b][c].subs(sub0) for c in r4] for b in r4] for a in r4]
T0 = [[[T[a][b][c].subs(sub0) for c in r4] for b in r4] for a in r4]
t = [sp.Rational(1, 2) * sum(T0[a][c][c] for c in r4) for a in r4]
F = [[-sum(C[a][b][c] * t[c] for c in r4) for b in r4] for a in r4]
nF = [[[sum(Om0[xx][a][z] * F[z][b] + Om0[xx][b][z] * F[a][z] for z in r4) for b in r4] for a in r4] for xx in r4]
third = [sp.expand(sum(ei[xx, a] * nF[xx][a][b] for xx in r4 for a in r4)
                   - sum(T0[a][b][c] * ei[a, xx] * F[xx][c] for a in r4 for xx in r4 for c in r4)) for b in r4]
print('(e) s = 0: nonzero F pairs', {(a, b): sp.factor(F[a][b]) for a in r4 for b in r4 if a < b and F[a][b] != 0},
      '; third bracket', third)
Mv = [sp.Matrix(4, 4, lambda cc, bb: Om[a][bb][cc]) for a in r4]
nv = sp.Matrix(n)
lam = [sp.simplify(red_c((Mv[a] * nv)[0])) for a in r4]
print('(f) W_a n = lambda_a n for all a:',
      all((Mv[a] * nv - lam[a] * nv).applyfunc(lambda z: sp.simplify(red_c(z))) == sp.zeros(4, 1) for a in r4),
      '; lambda_a =', lam)
Lop = sum((ei[a, a] * Mv[a] * Mv[a] for a in r4), sp.zeros(4, 4)).applyfunc(red_c)
nfl = sp.Matrix(low(n)).T
PQ2 = sp.expand(red_c(sum(ei[a, a] * (P[a] ** 2 + Q[a] ** 2) for a in r4)))
print('    L + (eta^{ab}(P_a P_b + Q_a Q_b)) n n^flat == 0:',
      (Lop + PQ2 * nv * nfl).applyfunc(lambda z: sp.simplify(red_c(z))) == sp.zeros(4, 4),
      '; eta^{ab}(P_a P_b + Q_a Q_b) =', sp.factor(PQ2),
      '; L^2 == 0:', (Lop * Lop).applyfunc(lambda z: sp.simplify(red_c(z))) == sp.zeros(4, 4))
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
G = sp.Matrix(6, 6, lambda i, j: red_c(sum(ei[a, a] * W[a][PAIRS[i][0]][PAIRS[i][1]] * W[a][PAIRS[j][0]][PAIRS[j][1]]
                                           for a in r4)))
print('    leg form at s = 0, chi = th = zeta = x = 0, al = 1, be = ga = 0, nonzero:',
      G.subs({cs: 1, sn: 0, chi: 0, th: 0, ze: 0, x: 0, al: 1, be: 0, ga: 0}) != sp.zeros(6, 6))
Fs = sp.symbols('F0:6'); Fm = [[0] * 4 for _ in r4]
for i, (a, b) in enumerate(PAIRS):
    Fm[a][b] = Fs[i]; Fm[b][a] = -Fs[i]
dQ = [red_c(sum(ei[xx, a] * Om[xx][a][z] * Fm[z][b] for xx in r4 for a in r4 for z in r4)
            + 2 * sum(ei[xx, a] * Om[xx][b][z] * Fm[a][z] for xx in r4 for a in r4 for z in r4)
            - sum(Om[b][a][c] * ei[a, xx] * Fm[xx][c] for a in r4 for xx in r4 for c in r4)) for b in r4]
kup = [sum(ei[a, b] * k[b] for b in r4) for a in r4]
print('(g) [Q_b - Q_b|_{w=0}] + tau k^a F_ab =',
      [sp.factor(red_c(dQ[b] + tau * sum(kup[a] * Fm[a][b] for a in r4))) for b in r4])
print('[%.0fs]' % (time.time() - t0))
