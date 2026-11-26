import sympy as sp
from math import comb

# Script 1: plane Moyal bracket at constant Theta, per-order-in-Theta structure.
# 2D block with Theta^{12} = th, Theta^{21} = -th (the general 4D antisymmetric
# constant case reduces by a linear symplectic change of variables; the 2D block
# carries the full structure of the claim).
#
# Checks (symbolic, exact):
#  (a) odd powers of Theta only in the Moyal bracket f*g - g*f;
#  (b) order-Theta coefficient = i {f,g}_Theta;
#  (c) order-Theta^3 coefficient = -(i/24) Theta^3 (third-derivative contraction),
#      matching the displayed -i/24 term of Remark rem:ch3-moyal-check (ch03);
#  (d) exactness: [x1, g]_star = i th d2 g for ANY test symbol g, and
#      [q, g]_star = i {q,g}_Theta exactly for any polynomial q of degree <= 2
#      (this is the "exact at constant Theta" content of the free/Poisson lemma);
#  (e) fluctuating coordinate: [x1 + t(x), g]_star has a first correction
#      i {t,g}_Theta at order Theta (connection-inducing term), and its first
#      higher-derivative correction is order Theta^3 with third derivatives of t.

x1, x2 = sp.symbols('x1 x2', real=True)
th = sp.symbols('theta', real=True)
I = sp.I
f = sp.Function('f', real=True)(x1, x2)
g = sp.Function('g', real=True)(x1, x2)

def moyal_bracket(A, B, max_n=11):
    """(A star B - B star A) with the (i/2)^n factors, summed over odd n up to max_n.
    The n-th bilinear term of A star B is (1/n!)(i/2)^n *
    (th (d1^A d2^B - d2^A d1^B))^n applied to A (x) B."""
    out = 0
    for n in range(1, max_n + 1, 2):
        inner = 0
        for k in range(n + 1):
            inner += comb(n, k) * (-1) ** (n - k) * \
                sp.Derivative(A, x1, k, x2, n - k) * sp.Derivative(B, x2, k, x1, n - k)
        out += 2 * (I * th / 2) ** n * inner / sp.factorial(n)
    return sp.expand(out)

mb = moyal_bracket(f, g, max_n=5)
print("coeff th^1:", sp.simplify(mb.coeff(th, 1)))
print("coeff th^2 (expect 0):", sp.simplify(mb.coeff(th, 2)))
print("coeff th^4 (expect 0):", sp.simplify(mb.coeff(th, 4)))

expected_c1 = I * (sp.Derivative(f, x1) * sp.Derivative(g, x2)
                   - sp.Derivative(f, x2) * sp.Derivative(g, x1))
print("check th^1 == i*Poisson:", sp.simplify(mb.coeff(th, 1) - expected_c1) == 0)

exp3 = -I / 24 * (
    sp.Derivative(f, x1, 3) * sp.Derivative(g, x2, 3)
    - 3 * sp.diff(f, x1, 2, x2) * sp.diff(g, x2, 2, x1)
    + 3 * sp.diff(f, x1, x2, 2) * sp.diff(g, x2, x1, 2)
    - sp.diff(f, x2, 3) * sp.diff(g, x1, 3))
print("check th^3 == -(i/24)*(third-derivative contraction):",
      sp.simplify(sp.expand(mb.coeff(th, 3)) - sp.expand(exp3)) == 0)

# (d) exactness
mb_lin = moyal_bracket(x1, g, max_n=11)
print("[x1,g]_star exact (all n up to 11) == i*th*d2 g:",
      sp.simplify(mb_lin) == I * th * sp.Derivative(g, x2))

q = x1 ** 2 + x1 * x2 + x2 ** 2 + x1 + 5
mb_q = moyal_bracket(q, g, max_n=11)
pois_q = I * th * (sp.Derivative(q, x1) * sp.Derivative(g, x2)
                   - sp.Derivative(q, x2) * sp.Derivative(g, x1))
print("degree-2 symbol exact:", sp.simplify(mb_q - pois_q) == 0)

# (e) fluctuating coordinate
t = sp.Function('t', real=True)(x1, x2)
mb_t = moyal_bracket(x1 + t, g, max_n=7)
c1_t = sp.simplify(mb_t.coeff(th, 1))
print("\norder-Theta term of [x1+t, g]_star:")
sp.pprint(c1_t)
c3_t = sp.simplify(mb_t.coeff(th, 3))
print("order-Theta^3 term of [x1+t, g]_star (first higher-derivative correction):")
sp.pprint(c3_t)
print("\nALL CHECKS:")
print("(a) even powers vanish:", sp.simplify(mb.coeff(th, 2)) == 0 and sp.simplify(mb.coeff(th, 4)) == 0)
print("(b) Poisson at order Theta:", sp.simplify(mb.coeff(th, 1) - expected_c1) == 0)
print("(c) -i/24 at order Theta^3:", sp.simplify(sp.expand(mb.coeff(th, 3)) - sp.expand(exp3)) == 0)
print("(d) linear and quadratic exactness:",
      sp.simplify(mb_lin) == I * th * sp.Derivative(g, x2) and sp.simplify(mb_q - pois_q) == 0)
