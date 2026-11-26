"""Log-order delta-completion bookkeeping and its calibration against universal anomaly values.

Rule (Fursaev-Solodukhin): to first order in (1-n), the surface part of the s^0 heat coefficient on the n-cone is the
cross term of the bulk a_2 with the conical delta parts
   R -> 4 pi (1-n) d_S,  Ric^{ab} -> 2 pi (1-n) P_N^{ab} d_S,  Riem^{abcd} -> 2 pi (1-n)(P^{ac}P^{bd}-P^{ad}P^{bc}) d_S,
   Omega_12 -> 2 pi (1-n) J_12 d_S   (bundle curvature delta, only if the bundle has it),  E -> E_reg + (1-n) E_delta d_S.
a_2 (Vassilevich/Gilkey, D = -(nabla^2 + E)): (1/360) tr[60 R E + 180 E^2 + 30 Omega^2 + 5 R^2 - 2 Ric^2 + 2 Riem^2].
S_log (coefficient of ln Lambda in the replica entropy) = [coefficient of (1-n) int_Sigma in Tr K s^0 term] / (16 pi^2).
"""
import sympy as sp
pi = sp.pi
R, Rii, Rj, W = sp.symbols('R Rii Rijij W')           # Rj = R_ijij (sum over normal i,j)
Rs = R - 2*Rii + Rj                                    # R_Sigma for totally geodesic Sigma
Wdef = Rj - Rii + R/3                                  # Weyl projection C_ijij (4D)

def cross(nfib, trE, trE_d, trEE_d, trJOm, Rgeom=True):
    """first-order-in-(1-n) delta cross terms (per unit of (1-n) int_Sigma), divided by 16 pi^2.
    trE: tr E_reg (Gilkey sign), trE_d: tr E_delta (coefficient of (1-n) d_S), trEE_d: tr(E_reg E_delta),
    trJOm: tr(J_12 Omega_12^reg) (so that Omega_delta,12 = 2 pi J_12)."""
    t = 60*(4*pi*trE + R*trE_d) + 360*trEE_d + 30*8*pi*trJOm
    if Rgeom:
        t += nfib*(5*8*pi*R - 2*4*pi*Rii + 2*8*pi*Rj)
    return sp.simplify(t/360/(16*pi**2))

# ---- scalar, periodic component, smooth E (Gilkey sign: E_G = -E_pos)
E = sp.symbols('E')
S_scalar = cross(1, -E, 0, 0, 0)
S_eq70 = (R/6 - E)/(24*pi) - (Rii - 2*Rj)/(720*pi)
print('scalar: delta-rule minus eq(70):', sp.simplify(S_scalar - S_eq70))
# conformal scalar E_pos = R/6
Sc = sp.simplify(S_eq70.subs(E, R/6))
print('conformal scalar = ', sp.simplify(Sc - (-(Rs - 3*Wdef)/(720*pi))), ' (0 means -(R_Sigma - 3W)/(720 pi))')

# ---- Hodge Maxwell on the cone (Feynman gauge): 4 comps with E_pos = Ric, Omega = Riemann (delta J), ghosts: 2 scalars (weight -2)
# E_G = -Ric : tr E_reg = -R ; E_delta = -2 pi P_N : tr E_d = -4 pi ; tr(E_reg E_d) = +2 pi R_ii ; tr(J Om) = -R_ijij
vec_M0 = cross(4, -R, 0, 0, 0)
vec_CE = cross(4, 0, -4*pi, 2*pi*Rii, 0, Rgeom=False) - 0
vec_COm = cross(4, 0, 0, 0, -Rj, Rgeom=False)
ghost = cross(1, 0, 0, 0, 0)
M0 = sp.simplify(vec_M0 - 2*ghost)
CE = sp.simplify(vec_CE)
COm = sp.simplify(vec_COm)
tot = sp.simplify(M0 + CE + COm)
print('Maxwell M0 (no deltas)      =', sp.expand(M0*pi))
print('Maxwell C_E (Ricci delta)   =', sp.expand(CE*pi))
print('Maxwell C_Omega (Riem delta)=', sp.expand(COm*pi))
a_, b_ = sp.symbols('alpha beta')
sol = sp.solve(sp.Poly(sp.expand((tot*pi) - (a_*Rs + b_*Wdef)), R, Rii, Rj).coeffs(), [a_, b_], dict=True)
print('Maxwell total * pi =', sp.expand(tot*pi), '; fit alpha R_Sigma + beta W:', sol)
# scalar analog for comparison of ratios
print('conformal scalar alpha,beta *pi: -1/720, 3/720.   Maxwell/scalar ratios:', [sp.nsimplify(sol[0][a_]/sp.Rational(-1,720)), sp.nsimplify(sol[0][b_]/sp.Rational(3,720))] if sol else None)
# sphere S^4 branched on great S^2: R=12, R_ii=6, R_ijij=2 (sum over i,j), R_Sigma=2, area 4 pi
vals = {R: 12, Rii: 6, Rj: 2}
A = 4*pi
for name, expr in [('M0', M0), ('C_E', CE), ('C_Omega', COm), ('total', tot), ('M0+C_E', M0 + CE)]:
    print('S^4/S^2  ', name, '=', sp.nsimplify(expr.subs(vals)*A), '=', sp.nsimplify(expr.subs(vals)*A*90), '/90')
# contact = total - M0
print('contact C_E+C_Omega * 24 pi =', sp.expand((CE + COm)*24*pi), ' ; compare -(R_Sigma - R_ii) =', sp.expand(-(Rs - Rii)))
# Donnelly-Wall edge: -R_Sigma/(24 pi) ; remainder
edge = -Rs/(24*pi)
print('contact - DW edge =', sp.expand((CE + COm - edge)*24*pi), ' (= R_ii)')
bulk = sp.simplify(tot - edge)
print('total - edge: alpha_bulk*pi:', sp.nsimplify(sp.Rational(-31,360) + sp.Rational(1,24)), ' i.e. -16/360 ; on S^4/S^2 bulk =', sp.nsimplify(bulk.subs(vals)*A*90), '/90')

# ---- Hodge Dirac (Levi-Civita), periodic unrotated gluing, for orientation only
# E_pos = R/4 -> E_G = -R/4 (x1 on 4 comps); E_delta = -pi (x 1_4);  Omega_ab = (1/4) R_abcd gamma^cd ; J = (1/2) gamma^12
# tr(J Om_12) = (1/2)(1/2) R_1212 tr(g12 g12) = (1/4) R_1212 (-4) = -R_1212 = -R_ijij/2
trE = -R; trE_d = -4*pi*sp.Rational(1,4)*1  # tr over 4 comps of (-(R_delta/4)) with R_delta=4pi -> -pi each -> -4 pi total
trEE = (-R/4)*(-pi)*4
D_per = cross(4, trE, -4*pi*sp.Rational(1,4), trEE/1, -Rj/2)
D_per_noDelta = cross(4, trE, 0, 0, 0)
print('Dirac LC periodic with deltas *pi :', sp.expand(D_per*pi), ' (weight -1 per Dirac field applies on top)')
print('Dirac anomaly targets (per Dirac field, weight included): alpha=-11/720, beta=+1/40 (c=1/20, beta=c/2) ->', sp.Rational(-11,720), sp.Rational(1,40))
