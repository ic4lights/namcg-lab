"""
s4_replica_bookkeeping.py  (proposal 044)

Bookkeeping of the two-derivative coefficients of the K-dependent induced action on M x K at the maximally
supersymmetric content, four-coordinate Poisson class M, Euclidean section, the two modes with delta rho = 0
about constant theta_bar, and the three replica prescriptions recorded in Appendix H (fixed-state, periodic,
first-order smooth).  Units: c, defined by  Gamma_E  contains  -(1/32 pi^2) c  int rho R[g_rho]  (a scalar
component with a common cutoff has c = Lambda^2/6), and S = (A_G/8 pi) c for the area term, so that
G_A = G_T  <=>  c_A = c_T.

Inputs (each from the place stated):
  * factorisation and order counting (s1): K-dependent two-derivative part =
        (1/6) W_R rho R[g_rho]  +  W_X rho^2 X    with
        W_R = int ds s^-2 (v^K - t^K)(s),   W_X = -(1/8) int ds s^-2 v_2^K(s)  (< 0 since v_2^K > 0);
  * Dirac index density at the a_1 level = (1/2) rho^2 X per four-component Dirac field (ledger, fermionic
    content paragraph); vector-normalised spinor index w = rho^2 X (s1: v2M = 2(sig2+ + sig2-));
  * on the delta rho = 0 modes: calT = X/4, (3/2) S^2 = X/2, V = 0 (s2), and R = -calT - 2 div V, so
    rho^2 X ~ -4 rho R[g_rho] (r = -4); teleparallel presentation X = -2R + (3/2)S^2 + 2V^2 (r = -2);
  * cone values per four-component Dirac field, unweighted, in c units (ledger, fermion replica gluing):
    antiperiodic (fixed-state) -1/3, unrotated periodic 4/6 = four scalars; smooth replica: -(1/2) x the
    coefficient of rho R[g_rho] in each sector (ledger, replica prescriptions paragraph);
  * Lambda^2 order: at (N_s, n_D) = (6, 2) the fixed-state area coefficient is 2 per mode, c_T = 0 (ledger).
"""
import sympy as sp
WR, WX, NL = sp.symbols('W_R W_X N_K_Lambda2', real=True)
out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

scalar_bulk = sp.Rational(1, 6); scalar_cone = sp.Rational(1, 6)
dirac_unw_cone = {'fixed-state': sp.Rational(-1, 3), 'periodic': sp.Rational(4, 6)}
dirac_index_cone = {k: v - 4 * scalar_cone for k, v in dirac_unw_cone.items()}
P("Dirac (4 components, unweighted) cone index part:", dirac_index_cone, " (fixed-state -1, periodic 0)")
w_cone = {k: 2 * v for k, v in dirac_index_cone.items()}           # vector-normalised (w = 2 x Dirac index)
w_cone['smooth'] = 0                                                # smooth: -(1/2) x coefficient of rho R in the index density (0 in (G,rho,dTheta))
r_mode = -4                                                         # rho^2 X ~ r rho R on the delta rho = 0 modes (s2)
r_tele = -2
P("vector-normalised index cone values w_cone:", w_cone)
cT = scalar_bulk * WR + r_mode * WX
P("")
P("c_T (tensor modes)            =", cT)
P("R-coefficient, teleparallel   =", scalar_bulk * WR + r_tele * WX, "  (the coefficient called G_N^-1 in the cited construction is the W_X part of this)")
scal_cone = {'fixed-state': scalar_cone * WR, 'periodic': scalar_cone * WR, 'smooth': -sp.Rational(1, 2) * scalar_bulk * WR}
for rep in ('fixed-state', 'periodic', 'smooth'):
    cA = scal_cone[rep] + w_cone[rep] * WX + (2 * NL if rep == 'fixed-state' else 0)
    P(f"{rep:12s}: c_A = {cA} ;  c_A - c_T = {sp.simplify(cA - cT)}")
P("")
P("Criterion: if the delta rho = 0 modes did not source the axial and vector torsion (S = V = 0 there), then")
cT_noS = scalar_bulk * WR + r_tele * WX
P("   c_T would be", cT_noS, "; fixed-state finite part c_A - c_T =", sp.simplify(scalar_cone * WR + w_cone['fixed-state'] * WX - cT_noS), "(Lambda^2 term 2 N_K Lambda^2 remains)")
P("Observation: Dirac fixed-state cone index (-1) = (1/2) x r_tele, i.e. the teleparallel coefficient of the Dirac index density (1/2) rho^2 X.")
P("Signs: W_X < 0, so the mixed contribution -4 W_X to c_T is positive (same sign as a scalar component);")
P("       W_R has no fixed sign (it is the K-supertrace at fourth and higher order in the K flux).")
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
