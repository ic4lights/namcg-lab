# verify_treecurve_129.py -- item 129, held block 48 "Tree curve and the ratio of the
# one-loop to the tree terms" + "Exchange of the scale of K" paragraphs (F-area cubic branch).
# Run:  python -I proposals/129-rc-held-recheck/verify_treecurve_129.py
# Expected invariant output: last line  TREECURVE_129 PASS
#
# Held setting: V_t = abar(chi^4 - (2/3) c3 chi^3), r3 = c3/(2 chi), kappa3 = 2 - c3/chi = 2(1-r3),
# Utilde = rho_M abar chi^4/g^2 (written U~), U'_loop = dU_loop/dlnchi, delta = (d2U_loop/dlnchi2)/(4 U~).
# Stationarity of the quartic+cubic terms: 4U~(1-r3) + U'_loop = 0.
import sympy as sp

chi, a, c3, L, d, Up, Uch, m, Ub, r3 = sp.symbols('chi a c3 L delta U_p U_chi m U~ r3', real=True)

def D(e):
    return chi * sp.diff(e, chi)

V_t = a * (chi**4 - sp.Rational(2, 3) * c3 * chi**3)
# (I1) dV_t/dlnchi = 4 abar chi^4 (1-r3) with r3 = c3/(2chi)   [this is WHY r3 = c3/2chi]
e1 = sp.simplify(D(V_t).subs(c3, 2 * r3 * chi) - 4 * a * chi**4 * (1 - r3))
assert e1 == 0, e1
# (I2) d2V_t/dlnchi2 = 4 abar chi^4 (4-3 r3)
e2 = sp.simplify(D(D(V_t)).subs(c3, 2 * r3 * chi) - 4 * a * chi**4 * (4 - 3 * r3))
assert e2 == 0, e2

# (I3) stationarity: L := U'_loop = -4U~(1-r3);  beta_K = 2L/(4U~(4-3r3+delta)) = 2(r3-1)/(4-3r3+delta)
Lsol = -4 * Ub * (1 - r3)
beta = sp.simplify(2 * Lsol / (4 * Ub * (4 - 3 * r3 + d)) - 2 * (r3 - 1) / (4 - 3 * r3 + d))
assert beta == 0, beta

# (I4) beta_K = 1  =>  r3 = (6+delta)/5 ;  V/T = (1-r3)^2 = (1+delta)^2/25 there
sol = sp.solve(sp.Eq(2 * (r3 - 1) / (4 - 3 * r3 + d), 1), r3)
assert sp.simplify(sol[0] - (6 + d) / 5) == 0, sol
assert sp.simplify(((1 - (6 + d) / 5) ** 2) - (1 + d) ** 2 / 25) == 0
# (I5) beta_K(r3=2) = 2/(delta-2)
assert sp.simplify(2 * (2 - 1) / (4 - 3 * 2 + d) - 2 / (d - 2)) == 0
# (I6) V/T identity: (1-r3)^2 = kappa3^2/4 with kappa3 = 2(1-r3)  (held Vhat/Thehat -> kappa3^2/4)
assert sp.simplify((1 - r3) ** 2 - (2 - 2 * r3) ** 2 / 4) == 0
# (I7) V=T at large N iff r3 = 0 or r3 = 2
assert sorted(sp.solve(sp.Eq((1 - r3) ** 2, 1), r3)) == [0, 2]
# (I8) bounded no-go: no-negative-mode range -1 <= kappa3 <= 2 reads 0 <= r3 <= 3/2;
#      with c3 != 0 (r3 > 0) the set {V=T} ∩ {no negative mode} = empty
assert 2 not in [x for x in [sp.Rational(0), 2] if -1 <= 2 * (1 - x) <= 2]
# (r3=0 excluded at c3 != 0; r3=2 gives kappa3=-2: negative mode -2 chi^2, see verify_hessian_129)
# (I9) r3 -> 1 limit: V/T -> 0 and beta_K -> 0 (case S2)
assert sp.limit((1 - r3) ** 2, r3, 1) == 0
assert sp.limit(2 * (r3 - 1) / (4 - 3 * r3 + d), r3, 1) == 0
# (I10) exchange identity: with beta_K = 2 U'_loop/U_chichi,
#       q_*^2|_chi = -beta_K U'_loop L/(8 m^4) = -L U_p^2/(4 m^4 U_chichi)
lhs = -sp.Rational(1, 8) * (2 * Up / Uch) * Up * L / m ** 4
rhs = -L * Up ** 2 / (4 * m ** 4 * Uch)
assert sp.simplify(lhs - rhs) == 0
# and the eliminated quadratic min: 1/2 Uch x^2 + U' x sigma at x* gives -U'^2 sigma^2/(2 Uch)
x, s1, U4 = sp.symbols('x sigma_1 U_4', real=True)
xmin = sp.solve(sp.Eq(Uch * x + Up * s1, 0), x)[0]
el = sp.simplify(sp.Rational(1, 2) * Uch * xmin ** 2 + Up * s1 * xmin + U4 * s1 ** 2 - (U4 - sp.Rational(1, 4) * (2 * Up / Uch) * Up) * s1 ** 2)
assert el == 0, el   # = (U4 - 1/4 beta_K U'_loop) sigma_1^2, held coefficient
print("TREECURVE_129 PASS")
