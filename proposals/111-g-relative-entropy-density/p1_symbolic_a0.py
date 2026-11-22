"""P1: symbolic n=1 identity A0 = (h/nu) * cof(G), hence A0 > 0 exactly at n=1.
Print: 4 scalar booleans/values. Run: python -I p1_symbolic_a0.py"""
import sympy as sp

x, r, p = sp.symbols('x r p', positive=True)
G = sp.Matrix([[x, r], [r, p]])
nu = sp.sqrt(x*p - r**2)
h = sp.log((nu + sp.Rational(1, 2))/(nu - sp.Rational(1, 2)))
O = sp.Matrix([[0, 1], [-1, 0]])
# closed form of _common.A_of_G_raw specialized to n=1:
# Kh = -i G (since sq O sq = G at n=1 with O^2=-I up to convention); map eig +-nu -> +-h;
# Kf = (h/nu)*Kh; A0 = -i * Kf * O evaluated through the matrix formula:
J = sp.symbols('J')  # sign eigenvalue placeholder not needed: Kf = (h/nu) Kh = (h/nu)*(-I*G)
# Use A0 = -i * isq Kf sq O = -i*(h/nu)*(O G)*(-i O)... do it directly in the code's algebra:
# isq*sq = I, sq*sq = G  =>  isq Kf sq = (h/nu)*(-I)*O*G   (I = imaginary unit here spelled sp.I)
Kf_term = (h/nu)*(-sp.I)*(O*G)          # = isq Kf sq (code order)
A0 = (-sp.I)*(Kf_term*O)
A0 = sp.simplify(A0)
cof = sp.Matrix([[p, -r], [-r, x]])
target = (h/nu)*cof
print('A0_minus_target_is_zero:', sp.simplify(A0 - target) == sp.zeros(2, 2))
print('A0_equals_neg_h_over_nu_OGO:', sp.simplify(A0 - (-(h/nu)*(O*G*O))) == sp.zeros(2, 2))
# positive definiteness of cof(G) for G>0: det(cof)=det(G), trace(cof)=x+p
print('det_cof_eq_det_G:', sp.simplify(cof.det() - (x*p - r**2)) == 0)
print('trace_cof_positive:', (x + p).is_positive)
