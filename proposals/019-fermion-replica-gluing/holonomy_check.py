"""
R-a3 (bounded): effect of an R-symmetry holonomy mu = m (n-1) added to the replica twist a_k -> a_k + mu, on the n->1 derivative.
Dirac domain:  per 2D block  sum_k (a_k+mu)^2 = sum a_k^2 + n mu^2   (cross term cancels by k -> -k symmetry of the anti set).
Scalar-like (componentwise regular domain): sum_{k=0}^{n-1} B2({k/n+mu}) = B2({n mu})/n  (multiplication theorem).
"""
import sympy as sp
from fractions import Fraction as Fr
n,m=sp.symbols('n m',real=True)
B2=lambda x:x**2-x+sp.Rational(1,6)
# Dirac
F=(n**2-1)/(12*n)+n*(m*(n-1))**2
c=sp.simplify((F-n*sp.diff(F,n)).subs(n,1))
print('Dirac block, (1-n d_n)[sum (a_k+mu)^2] at n=1 :',c,' (independent of m)')
# numerical check of the cross-term cancellation at integer n
for N in (2,3,4,5):
    mu=Fr(1,7)
    A=[Fr(2*j-(N-1),2*N) for j in range(N)]
    lhs=sum((x+mu)**2 for x in A); rhs=sum(x*x for x in A)+N*mu**2
    assert lhs==rhs
print('cross-term cancellation verified for n=2..5')
# scalar-like: multiplication theorem check
import math
def b2frac(x): x=x-math.floor(x); return x*x-x+1/6
for N in (2,3,5):
    mu=0.0137
    lhs=sum(b2frac(k/N+mu) for k in range(N)); rhs=b2frac(N*mu)/N
    assert abs(lhs-rhs)<1e-12
print('multiplication theorem verified (n=2,3,5)')
# one-sided slopes at n=1 for mu=m(n-1): B2({n mu})/n, x=n m (n-1)
x=n*m*(n-1)
right=B2(x)/n          # n>1, m>0 : {x}=x
left=B2(1+x)/n         # n<1, m>0 : x<0, {x}=1+x
for name,ex in (('n>1',right),('n<1',left)):
    f=ex-n*ex.subs(n,1)
    print('scalar-like complex component, %s branch: (1-n d_n) f at n=1 = %s' % (name,sp.simplify((f-n*sp.diff(f,n)).subs(n,1))))
print('=> linear |mu| term: slopes differ by 2m (kink); absent in the Dirac-domain fermion block')
