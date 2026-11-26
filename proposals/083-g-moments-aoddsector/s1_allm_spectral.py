# s1_allm_spectral.py  (083) Lemma 1: all-order spectral trace polynomial of the
# 2x2 rank-one block Q(a,r) = [[-4a, -2 i t], [2 i t, 0]], r = t^2.
# Claim: Tr Q^m = (-1)^m 2^(m+1) sum_{k=0}^{floor(m/2)} C(m,2k) a^(m-2k) (a^2+r)^k, m>=1.
# Run from repo root: python -I proposals/083-g-moments-aoddsector/s1_allm_spectral.py
import sympy as sp
from sympy import I, binomial, expand
a, r, t = sp.symbols('a r t', real=True)
Q = sp.Matrix([[-4*a, -2*I*t], [2*I*t, 0]])
def trQ(m):
    p = sp.Poly(expand((Q**m)[0, 0] + (Q**m)[1, 1]), a, t)
    assert all(mt % 2 == 0 for (ma, mt) in p.monoms()), 'odd t power in Tr Q^m'
    return sum(c * a**ma * r**(mt//2) for (ma, mt), c in zip(p.monoms(), p.coeffs()))
fail = 0
for m in range(1, 15):
    rhs = expand((-1)**m * 2**(m+1) * sum(binomial(m, 2*k) * a**(m-2*k) * (a**2+r)**k
                                          for k in range(m//2 + 1)))
    ok = (expand(trQ(m) - rhs) == 0)
    fail += (not ok)
    print('m=%2d identity=%s' % (m, ok))
for p in range(0, 7):
    e = expand(2**(2*p+1) * sum(binomial(2*p, 2*k) * a**(2*p-2*k) * (a**2+r)**k for k in range(p+1)))
    print('p=%d even-corollary=%s' % (p, expand(e - trQ(2*p)) == 0))
for p in range(0, 5):
    o = expand(-2**(2*p+2) * sum(binomial(2*p+1, 2*k) * a**(2*p+1-2*k) * (a**2+r)**k for k in range(p+1)))
    print('p=%d odd-corollary=%s' % (p, expand(o - trQ(2*p+1)) == 0))
print('p=1 odd trace:', expand(trQ(3)))
print('a=0 pointwise Tr Q^{2p}:', [expand(trQ(2*p).subs(a, 0)) for p in (1, 2, 3)])
print('S1 invariant: fail count =', fail)
print('S1 OK' if fail == 0 else 'S1 FAIL')
