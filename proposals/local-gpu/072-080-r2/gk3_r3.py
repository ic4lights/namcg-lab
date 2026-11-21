import math
from math import lgamma, log
# log dim U(M) of partition via Weyl formula: prod_{i<j} (l_i-l_j+j-i)/(j-i)
def logdim(lam,M):
    lam=list(lam)+[0]*(M-len(lam))
    # use hook-content: sum over boxes log(M+c-r) - log hook
    s=0.0
    conj=[sum(1 for x in lam if x>=c) for c in range(1,(lam[0] if lam else 0)+1)]
    for r,row in enumerate(lam,1):
        for c in range(1,row+1):
            hook=row-c+conj[c-1]-r+1
            s+=log(M+c-r)-log(hook)
    return s
def G(m,u): return (m+u)*log(m+u)-m*log(m)-u
def resid(N,m1,m2,u1,u2,q):
    M1,M2=round(m1*N),round(m2*N); l1,l2=round(u1*N),round(u2*N)
    D=logdim([l1]*q+[l2]*q,M1+M2)-logdim([l1]*q,M1)-logdim([l2]*q,M2)
    m1e,m2e,u1e,u2e=M1/N,M2/N,l1/N,l2/N
    Lam=q*(G(m1e+m2e,u1e)-G(m1e,u1e))+q*(G(m1e+m2e,u2e)-G(m2e,u2e))
    return N*Lam-D
for args in [(.5,.5,.5,.5),(.5,.5,.5,.3),(.5,.5,.3,.3)]:
  for q in (1,2):
    print(args,q,[round(resid(N,*args,q),3) for N in (200,400,800,1600)])
# R6 check
M1=M2=10**4;l1,l2=1000,500;M=M1+M2
ex=logdim([l1,l2],M)-logdim([l1],M1)-logdim([l2],M2)
ap=l1*log(M/M1)+l2*log(M/M2)
print('R6 exact-approx',ex-ap, ' l^2/M pred', -(l1**2/2)*(1/M1-1/M)-(l2**2/2)*(1/M2-1/M), 'log', -log((l1+1)/(l1-l2+1)))
