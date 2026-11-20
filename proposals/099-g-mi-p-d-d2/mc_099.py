# mc_099.py -- direct Wishart MC arbiter for the analytic joint of rederive_099.py (item 099).
# CN(0,v) sampled as (sqrt(v/2))(n1+i n2). Run: python -I proposals/099-g-mi-p-d-d2/mc_099.py
import numpy as np
rng=np.random.default_rng(7)
def sample(M,g1,g2,sig,N):
    def col(g):
        s=np.sqrt(sig*g/2.0)
        return s*(rng.standard_normal((N,M))+1j*rng.standard_normal((N,M)))
    A,B=col(g1),col(g2)
    tau=(np.abs(A)**2+np.abs(B)**2).sum(1)
    g11=(np.abs(A)**2).sum(1); g22=(np.abs(B)**2).sum(1)
    z=(np.conj(A)*B).sum(1); detg=g11*g22-z.real**2-z.imag**2
    disc=np.sqrt(np.maximum(tau**2-4*detg,0))
    lam2=(tau-disc)/2
    u=lam2/tau; x=np.clip((g11-lam2)/np.where(disc>1e-12,disc,1),0,1)
    return tau,u,x
for (M,g1,g2) in [(2,1.0,2.0),(4,1.0,2.0)]:
    N=400_000; tau,u,x=sample(M,g1,g2,1.0,N)
    H,_,_=np.histogram2d(u,x,bins=[np.linspace(0,0.5,31),np.linspace(0,1,31)])
    p=H/H.sum(); sel=p>0
    mi=np.sum(p[sel]*np.log(p[sel]/(p.sum(1,keepdims=True)@p.sum(0,keepdims=True))[sel]))
    b=1/g1-1/g2; rho=b*tau*(1-2*u)
    print("M=%d g=(%g,%g): tau=%.4f u=%.4f x=%.4f | MI hist=%.5f (bias~+%.4f) | E[x|spec] formula=%.4f vs MC=%.4f"%(
        M,g1,g2,tau.mean(),u.mean(),x.mean(),mi,900/(2*N),(1/rho-1/np.expm1(rho)).mean(),x.mean()))
