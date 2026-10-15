"""
Bookkeeping for proposal 017.  Inputs (all from verified computations, see the folder):
  eigenvalues of the one-loop a_1 quadratic form relative to rho_bar^2 p^2 M on the two delta-rho=0 modes (TT) and the delta-rho != 0 mode (3),
  per sector with weight 1 (hk_eval.py runs, fitted exact forms for the gauge family):
    scalar       e_TT = -1/24      e_3 = -1/8                          (a_1 = rho R/6)
    connection   e_TT = 5/6 - (al-1)/24 ,  e_3 = 1/2 - (al-1)/8 + (al^2-1)/4        (al = 1/(1-kappa))
    Dirac (4c)   e_TT = 1/3        e_3 = 0                             (a_1 = (4/6) rho R + (1/2) rho^2 X)
  statistical weights: scalar +1 (N_s), connection +1, ghost -2 (scalar operator), Dirac -1 (n_D).
  cone coefficients c_A (units where a scalar component gives 1/6): scalar 1/6, connection (3+al)/6 (unrotated, intertwining), ghost -2/6,
    Dirac +1/3 (antiperiodic polar frame, cone_twist_zeta.py); rotated connection: -1 (n<1 branch).
Induced form: -(Lambda^2/32 pi^2) sum_i w_i e_i (rho_bar^2 p^2 M);  Einstein eigenvalue of c*rho R[g_rho] is -c/4  =>  c_T = -4 E_TT.
"""
import sympy as sp

Ns, nD, al = sp.symbols('N_s n_D alpha')
Rat = sp.Rational
e_s, e3_s = -Rat(1, 24), -Rat(1, 8)
e_v, e3_v = Rat(5, 6) - (al - 1) / 24, Rat(1, 2) - (al - 1) / 8 + (al**2 - 1) / 4
e_D, e3_D = Rat(1, 3), 0

E_TT = Ns * e_s + e_v - 2 * e_s - nD * e_D
E_3 = Ns * e3_s + e3_v - 2 * e3_s - nD * e3_D
c_T = sp.expand(-4 * E_TT)
c2 = sp.expand(2 * (E_3 - 3 * E_TT))          # coefficient of rho (grad ln rho)^2 beyond the Einstein-in-g_rho ratio (0 <=> third-mode ratio 3)
cA_unrot = sp.expand(Ns / 6 + (3 + al) / 6 - 2 / sp.Integer(6) + nD * Rat(1, 3))
cA_rot = sp.expand(cA_unrot - 1)
print('c_T          =', c_T)
print('c_A (unrot)  =', cA_unrot)
print('gap = c_A - c_T (unrot) =', sp.simplify(cA_unrot - c_T), '   (rotated connection:', sp.simplify(cA_rot - c_T), ')')
print('c2 (third-mode / Einstein-in-g_rho test) =', c2)
print()
print('Feynman gauge al=1, no fermions: c_T =', c_T.subs({al: 1, nD: 0}), ' c_A =', cA_unrot.subs({al: 1, nD: 0}), ' gap =', sp.simplify((cA_unrot - c_T).subs({al: 1, nD: 0})), ' c2 =', c2.subs({al: 1, nD: 0}))
print('solve c2 = 0 for al (n_D = 0):', sp.solve(c2.subs(nD, 0), al))
print('solve gap = 0 for n_D (unrotated / rotated):', sp.solve(cA_unrot - c_T, nD), sp.solve(cA_rot - c_T, nD))
print('solve c2 = 0 for n_D at al = 1:', sp.solve(c2.subs(al, 1), nD))
print()
print('Maximally supersymmetric content (matrix model with D coordinates, 4 with Poisson background, N_s = D-4):')
for D, nd in [(4, Rat(1, 2)), (6, 1), (10, 2)]:
    sub = {Ns: D - 4, nD: nd, al: 1}
    print(f'  D={D}: n_D={nd}: c_R-part(N_s+2-4 n_D)/6 = {sp.simplify((Ns + 2 - 4 * nD).subs(sub) / 6)}, c_T={c_T.subs(sub)}, c_A(unrot)={cA_unrot.subs(sub)}, gap={sp.simplify((cA_unrot - c_T).subs(sub))}, c2={c2.subs(sub)}')
print()
print('1/G_A - 1/G_T = gap * Lambda^2/(2 pi)  (1/(16 pi G) = c Lambda^2/(32 pi^2));  gap=4 -> 2 Lambda^2/pi as in proposal 015')

# replica (II) of proposal 015 (singular rho; Q = 1/4 in every sector, branch-conditional, not used): c_A^(II) = -(1/12) W, W = N_s + 2 - 4 n_D  (alpha = 1)
W = Ns + 2 - 4 * nD
cA_II = -W / 12
print()
print('replica (II), alpha=1: c_A =', sp.simplify(cA_II), '; gap_II = c_A - c_T =', sp.simplify((cA_II - c_T).subs(al, 1)), '; equality at W =', sp.solve(sp.Eq(cA_II, c_T.subs(al, 1)), Ns), ' (n_D=0: N_tot = 16; n_D=2: W=0, i.e. N_s=6, both sides vanish)')
print('positivity of c_T at n_D=4, al=1:', sp.simplify(c_T.subs({al: 1, nD: 4})), ' c2 =', c2.subs({al: 1, nD: 4}))
