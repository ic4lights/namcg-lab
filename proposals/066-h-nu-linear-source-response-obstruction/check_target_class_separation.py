"""Proposal 066, check 1.

Separation of the target interpolator nu_sqrt (ch13 eq:nu-sqrt, ch17 eq:nu-target)
from the affine-gap / exponential-linear class (appE eq:appE-exp, realised by a
gap Delta k = b + c x with x = g_N/g_s).

Every printed statement is an exact sympy computation; symbolic output is a
check, not a proof. The proof obligations are the short arguments quoted in
proposal-r1.md.
"""
import sympy as sp

x = sp.symbols('x', positive=True)          # x = g_N / g_s
t = sp.symbols('t', positive=True)          # x = t^2, for Puiseux series
b, c = sp.symbols('b c', positive=True)     # affine-gap constants
alpha = sp.symbols('alpha', positive=True)  # family amplitude of eq:appE-exp
B, C = sp.symbols('B C', real=True)

nu_sqrt = 1/(1 - sp.exp(-sp.sqrt(x)))                 # target, eq:nu-target
nu_aff  = 1/(1 - sp.exp(-(b + c*x)))                  # affine-gap response
nu_exp  = 1/(1 - alpha*sp.exp(-c*x))                  # retired family eq:appE-exp

def report(name, expr):
    ser_t = sp.series(expr.subs(x, t**2), t, 0, 3)
    print(name, "  x -> 0 (Puiseux in t = sqrt x):")
    print("   ", ser_t.removeO())

report("nu_sqrt", nu_sqrt)
report("nu_aff (b>0)", nu_aff.subs(b, sp.Rational(3, 2)).subs(c, 1))
report("nu_aff (b=0, i.e. alpha=1)", nu_aff.subs(b, 0).subs(c, 1))
report("nu_exp (alpha=1/2)", nu_exp.subs(alpha, sp.Rational(1, 2)).subs(c, 1))
report("nu_exp (alpha=1)", nu_exp.subs(alpha, 1).subs(c, 1))

# 1. Deep-regime divergence exponents.
print()
print("lim x->0  nu_sqrt * sqrt(x)      =", sp.limit(nu_sqrt*sp.sqrt(x), x, 0))
print("lim x->0  nu_aff(b=0) * x        =", sp.limit(nu_aff.subs(b, 0).subs(c, 1)*x, x, 0))
print("lim x->0  nu_exp(alpha=1/2)      =", sp.limit(nu_exp.subs(alpha, sp.Rational(1, 2)).subs(c, 1), x, 0))

# 2. Newtonian-side decay exponents (x -> infinity); numeric constants used
#    to keep the parametrised limit elementary.
print()
print("lim x->oo (nu_sqrt - 1) * exp(sqrt(x)) =", sp.limit((nu_sqrt - 1)*sp.exp(sp.sqrt(x)), x, sp.oo))
print("lim x->oo (nu_aff - 1) * exp(x)  (b=1, c=1) =",
      sp.limit((nu_aff - 1).subs([(b, 1), (c, 1)])*sp.exp(x), x, sp.oo))
print("lim x->oo (nu_aff - 1)/(nu_sqrt - 1)  (b=1, c=1) =",
      sp.limit(((nu_aff - 1)/(nu_sqrt - 1)).subs([(b, 1), (c, 1)]), x, sp.oo))

# 3. Functional obstruction: equality of the two Bose-form denominators for all
#    x > 0 would force sqrt(x) = B + C*x.
sol = sp.solve([sp.sqrt(1) - (B + C*1),
                sp.sqrt(4) - (B + C*4),
                sp.sqrt(9) - (B + C*9)], [B, C], dict=True)
print()
print("sqrt(x) = B + C*x fitted at x = 1, 4, 9 ->", sol)
d2 = sp.diff(sp.sqrt(x) - (B + C*x), x, 2)
print("d^2/dx^2 [sqrt(x) - B - C*x] =", d2,
      "; vanishing would require", sp.solve(sp.Eq(d2, 0), x, dict=True) or "no solution")

# 4. Exact match of the affine-gap response with the retired family.
ident = sp.simplify(nu_aff.subs(b, -sp.log(alpha)))
print()
print("nu_aff with b = ln(1/alpha), g_s-scale = 1/c  ==  nu_exp :",
      sp.simplify(ident - nu_exp) == 0)
