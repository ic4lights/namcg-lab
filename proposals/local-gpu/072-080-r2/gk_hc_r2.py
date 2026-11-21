# independent: hook-content dims, two-row and stacked defect, residuals at u1=u2 and u1!=u2
from math import lgamma, log
from fractions import Fraction
import itertools
def logdim(M, rows):
    rows=[r for r in rows if r>0]
    cols=[sum(1 for r in rows if r>=c) for c in range(1,(rows[0] if rows else 0)+1)]
    s=0.0
    for i,r in enumerate(rows):
        for c in range(1,r+1):
            hook=(r-c)+(cols[c-1]-(i+1))+1
            s+=log(M+c-(i+1))-log(hook)
    return s
def dimF(M, rows):
    rows=[r for r in rows if r>0]
    cols=[sum(1 for r in rows if r>=c) for c in range(1,(rows[0] if rows else 0)+1)]
    v=Fraction(1)
    for i,r in enumerate(rows):
        for c in range(1,r+1):
            v*=Fraction(M+c-(i+1),(r-c)+(cols[c-1]-(i+1))+1)
    return v
# closed form check
bad=0
for M1,M2,l1,l2 in itertools.product(range(2,6),range(2,6),range(0,7),range(0,7)):
    if l2>l1: continue
    M=M1+M2
    ex=dimF(M,[l1,l2])/(dimF(M1,[l1])*dimF(M2,[l2]))
    cf=Fraction(1)
    for c in range(1,l1+1): cf*=Fraction(M-1+c,M1-1+c)
    for c in range(1,l2+1): cf*=Fraction(M-2+c,M2-1+c)
    cf*=Fraction(l1-l2+1,l1+1)
    bad+= ex!=cf
print('two-row closed form failures',bad)
# stacked
bad=0;n=0
for M1,M2,q1,q2,l1,l2 in itertools.product(range(3,6),range(3,6),range(1,3),range(1,3),range(1,5),range(0,5)):
    if l2>l1: continue
    M=M1+M2
    ex=dimF(M,[l1]*q1+[l2]*q2)/(dimF(M1,[l1]*q1)*dimF(M2,[l2]*q2))
    cf=Fraction(1)
    for r in range(1,q1+1):
        for c in range(1,l1+1): cf*=Fraction(M+c-r,M1+c-r)
    for r in range(1,q2+1):
        for c in range(1,l2+1): cf*=Fraction(M-q1+c-r,M2+c-r)
    for r in range(1,q1+1):
        for c in range(1,l2+1): cf*=Fraction(l1-c+q1-r+1,l1-c+q1+q2-r+1)
    bad+= ex!=cf; n+=1
print('stacked failures',bad,'of',n)
print('37/72 check', dimF(26,[13,13])/(dimF(2,[13])*dimF(24,[13])) / (dimF(26,[13,12])/(dimF(2,[13])*dimF(24,[12]))))
def G(m,u): return (m+u)*log(m+u)-m*log(m)-u if m>0 else 0
def resid(N,m1,m2,u1,u2,q):
    M1,M2=round(m1*N),round(m2*N); l1,l2=round(u1*N),round(u2*N)
    D=logdim(M1+M2,[l1]*q+[l2]*q)-logdim(M1,[l1]*q)-logdim(M2,[l2]*q)
    Lam=q*(G(m1+m2,u1)-G(m1,u1))+q*(G(m1+m2,u2)-G(m2,u2))
    return N*Lam-D
for (m1,m2,u1,u2) in [(0.5,0.5,0.5,0.5),(0.5,0.5,0.5,0.3),(0.5,1/3,0.4,0.25)]:
    for q in (1,2,3):
        r=[resid(N,m1,m2,u1,u2,q) for N in (400,800,1600,3200)]
        print((m1,m2,u1,u2),q,['%.3f'%x for x in r],'incr',['%.3f'%(b-a) for a,b in zip(r,r[1:])])
