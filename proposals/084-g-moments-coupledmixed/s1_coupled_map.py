# s1_coupled_map.py (084) Unconditional mixed-moment master map + flip symmetry.
# For ANY joint law of real a and r >= 0:
#  <Tr Q^m> = (-1)^m 2^(m+1) sum_{k<=m/2} C(m,2k) sum_{j=0}^k C(k,j) M_{m-2k+2j, k-j},
#  M_{n,j} = E[a^n r^j],  spectrum -2a +/- 2*sqrt(a^2+r)  (081 convention, r = |w_perp|^2).
# 083's map is the product subcase M_{n,j} -> A_n H_j (a _||_ r).  Flip: TrQ^m(-a,r) =
# (-1)^m TrQ^m(a,r), so averaged odd moments vanish for ANY flip-symmetric joint law
# (no independence, no Gaussianity).  Run from repo root:
#   python -I proposals/084-g-moments-coupledmixed/s1_coupled_map.py
import sympy as sp
from sympy import binomial, expand, I
x, r, tt = sp.symbols('x r tt', real=True)
def trP(m):
    Q = sp.Matrix([[-4*x, -2*I*tt], [2*I*tt, 0]])
    p = sp.Poly(expand((Q**m)[0, 0] + (Q**m)[1, 1]), x, tt)
    assert all(mt % 2 == 0 for (_, mt) in p.monoms())
    return sum(c * x**mx * r**(mt // 2) for (mx, mt), c in zip(p.monoms(), p.coeffs()))
M = sp.Function('M')
def map_m(m):
    return (-1)**m * 2**(m+1) * sum(binomial(m, 2*k) *
        sum(binomial(k, j) * M(m - 2*k + 2*j, k - j) for j in range(k + 1))
        for k in range(m // 2 + 1))
def functional(expr):
    p = sp.Poly(sp.expand(expr), x, r)
    return sum(c * M(mx, mt) for (mx, mt), c in zip(p.monoms(), p.coeffs()))
f1 = f2 = 0
for m in range(1, 10):
    ok1 = sp.simplify(functional(trP(m)) - map_m(m)) == 0
    ok2 = sp.simplify(trP(m).subs(x, -x) - (-1)**m * trP(m)) == 0
    print('mixed map m=%d: %s | flip m=%d: %s' % (m, ok1, m, ok2))
    f1 += (not ok1); f2 += (not ok2)
print('TrQ^2  =', expand(trP(2)))
print('TrQ^4  =', expand(trP(4)))
print('TrQ^6  =', expand(trP(6)))
# explicit m=4 mixed-moment form: 32*(M02 + 8*M21 + 8*M40)
p4 = sp.Poly(expand(trP(4)), x, r)
print('m=4 coeffs M(n,j):', {p4.monoms()[i]: int(p4.coeffs()[i]) for i in range(p4.length())})
print('S1 invariant 1: mixed-map fail count =', f1)
print('S1 invariant 2: flip fail count =', f2)
print('S1 OK' if f1 + f2 == 0 else 'S1 FAIL')
