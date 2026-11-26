"""
Area-term coefficient of the heat trace on the flat cone C_n for a two-dimensional transverse component with
angular monodromy exp(2 pi i theta) in the Cartesian-like frame (Bessel orders |m+theta|/n, m in Z), by Hurwitz zeta:

   Tr_n - (volume term) = -(1/2) sum_m |m+theta|/n  ->  B_2({theta})/(2 n)      (zeta-regularised; scalar theta=0: 1/(12 n))
   S-coefficient c = (1 - n d/dn)[ C(n) - n C(1) ]_{n=1}  in units where one scalar component gives 1/6.

Cases (theta as a function of n):
  scalar:                theta = 0
  vector component (J=+-1, polar frame periodic, rotated index):  theta = n  (mod 1)
  spinor component (polar frame antiperiodic, spin 1/2 rotation):  theta = (n+1)/2 (mod 1)
Because {theta} is not analytic at n = 1 for the last two, both one-sided derivatives are reported.
"""
import sympy as sp

n = sp.symbols('n', positive=True)
B2 = lambda a: a**2 - a + sp.Rational(1, 6)


def coeff(theta_frac_expr):
    C = B2(theta_frac_expr) / (2 * n)
    f = C - n * C.subs(n, 1)
    return sp.simplify((f - n * sp.diff(f, n)).subs(n, 1))


cases = {
    'scalar': (sp.Integer(0), sp.Integer(0)),
    'vector comp (rotated)': (n, n - 1),            # {n}: n for n<1 ; n-1 for n>1
    'spinor comp (antiperiodic polar frame)': ((n + 1) / 2, (n - 1) / 2),   # {(n+1)/2}: (n+1)/2 for n<1 ; (n-1)/2 for n>1
}
print('component type | n->1^- (frac part branch) | n->1^+')
for name, (below, above) in cases.items():
    print(f'{name}: {coeff(below)} | {coeff(above)}')
print('scalar value 1/6;  ratio to scalar (n<1 branch):')
for name, (below, above) in cases.items():
    print(f'  {name}: {sp.nsimplify(coeff(below) / sp.Rational(1, 6))}')
