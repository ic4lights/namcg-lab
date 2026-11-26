"""
Sector-by-sector bookkeeping for proposal 015 (symbolic).  Units: a real component of weight w and fibre trace t
contributes to the replica entropy  S = (Lambda^2 A / 8 pi) * w * t * c  where c is the coefficient of R_G in tr(R_G/6 - E)
in the stated set of independent variables (c = 1/6 gives S = Lambda^2 A/(48 pi) per component).
Inputs (verified in the other scripts of this folder):
  scalar     E_s = (1/4) R_G + torsion terms (verify_E_torsion.py);  Q_s = 0 in (G, rho, dTheta), 1/4 in (G, torsion)
  connection E_v : tr E_v = 4 E_s + tr(B^2),  tr B = 0,  tr(B_s B^s) = -X = -T_{lmn}T^{lmn} (operator_identities.py)
  ghost      weight -2, operator -O_s
TT quadratic form (tt_quadratic_forms.py): relative to M, rho R[g_rho] -> -1/4 on the two delta-rho=0 modes (-3/4 on the third),
rho^2 X -> +1 on all three; induced density = -(Lambda^2/32 pi^2) [ (N_tot/6) rho R[g_rho] + rho^2 X ].
"""
import sympy as sp

Ns = sp.symbols('N_s')
Lam, A = sp.symbols('Lambda A', positive=True)
one6 = sp.Rational(1, 6)
Q_scalar_torsion = sp.Rational(1, 4)

c_G = {  # variables (G, rho, dTheta): no explicit curvature in E
    'scalar (N_s comps, w=1)': Ns * one6,
    'connection (4 comps, w=1)': 4 * one6,
    'ghost (1 comp, w=-2)': -2 * one6,
}
c_T = {  # variables (G, torsion): E_s = R/4 + ..., tr E_v = 4 E_s + tr B^2 (tr B^2 = -T^2, no curvature)
    'scalar (N_s comps, w=1)': Ns * (one6 - Q_scalar_torsion),
    'connection (4 comps, w=1)': 4 * (one6 - Q_scalar_torsion),
    'ghost (1 comp, w=-2)': -2 * (one6 - Q_scalar_torsion),
}
print("sector | c in (G,rho,dTheta) = S^(I) in units Lambda^2 A/(8 pi) | c in (G,torsion) = S^(II)")
for k in c_G:
    print(f"  {k}: {sp.simplify(c_G[k])} | {sp.simplify(c_T[k])}")
Ntot = Ns + 2
tot_G = sp.simplify(sum(c_G.values()))
tot_T = sp.simplify(sum(c_T.values()))
print("total:", tot_G, "=", sp.simplify(tot_G - Ntot / 6) == 0 and "N_tot/6", "|", tot_T, "=", sp.simplify(tot_T + Ntot / 12) == 0 and "-N_tot/12")
print("ratio (II)/(I) =", sp.simplify(tot_T / tot_G * 1))

# TT quadratic form
eigR_TT, eigR_3rd, eigX = -sp.Rational(1, 4), -sp.Rational(3, 4), 1
form_TT = sp.simplify(tot_G * eigR_TT + eigX)
print("TT eigenvalue (rho_bar^2 p^2 M units):", form_TT, " expected 1 - N_tot/24:", sp.simplify(form_TT - (1 - Ntot / 24)) == 0)
form_3 = sp.simplify(tot_G * eigR_3rd + eigX)
print("third mode:", form_3)
c_TT = sp.simplify(-4 * form_TT)
print("c_TT = -4 * TT eigenvalue =", c_TT, " ; c_cone = N_tot/6; difference c_cone - c_TT =", sp.simplify(Ntot / 6 - c_TT))
# Newton constants, common cutoff Lambda:  1/(16 pi G) = c Lambda^2 / (32 pi^2)
invG = lambda c: sp.simplify(c * Lam ** 2 / (2 * sp.pi))
print("1/G_cone =", invG(Ntot / 6), "; 1/G_TT =", invG(c_TT), "; difference =", sp.simplify(invG(Ntot / 6) - invG(c_TT)))
# separate cutoffs: scalar+ghost sector cutoff L_s, connection sector cutoff L_v (all cone and induced pieces use their own)
Ls, Lv = sp.symbols('Lambda_s Lambda_v', positive=True)
cone = (Ns * Ls**2 + 4 * Lv**2 - 2 * Ls**2) / (12 * sp.pi)   # ghost shares the scalar operator and cutoff
TTc = (Ns * Ls**2 + 4 * Lv**2 - 2 * Ls**2 - 24 * Lv**2) / (12 * sp.pi)
print("separate cutoffs: 1/G_cone =", sp.simplify(cone), " 1/G_TT =", sp.simplify(TTc), " difference =", sp.simplify(cone - TTc))
print("scalar-only content (no connection, no ghost): c_TT - c_cone =", sp.simplify((Ns * one6 * eigR_TT) * -4 - Ns * one6))
