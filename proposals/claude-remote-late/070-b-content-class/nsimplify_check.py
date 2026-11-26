"""070 r3 (m-b): behaviour of sympy.nsimplify on exact Rationals. Re-run: python -I proposals/070-b-content-class/nsimplify_check.py"""
import sympy as sp
print("sympy", sp.__version__)
for p, q in [(4093, 72), (81811, 27648), (1, 3), (-26, 81)]:
    r = sp.Rational(p, q); n = sp.nsimplify(r)
    print(r, type(r).__name__, "->", n, "| identity:", n == r)
print("integer short-circuit:", sp.nsimplify(sp.Integer(7)) == 7)
