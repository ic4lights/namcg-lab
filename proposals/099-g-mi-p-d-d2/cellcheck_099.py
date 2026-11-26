# cellcheck_099.py -- compare analytic joint candidates to direct Wishart MC histogram, M=2, g=(1,2).
# Run: python -I proposals/099-g-mi-p-d-d2/cellcheck_099.py
import numpy as np
rng=np.random.default_rng(7)
N=1_500_000; M=2; g1,g2,sig=1.0,2.0,1.0
def col(g):
    s=np.sqrt(sig*g/2.0)
    return s*(rng.standard_normal((N,M))+1j*rng.standard_normal((N,M)))
A,B=col(g1),col(g2)
tau=(np.abs(A)**2+np.abs(B)**2).sum(1)
g11=(np.abs(A)**2).sum(1); g22=(np.abs(B)**2).sum(1)
z=(np.conj(A)*B).sum(1); detg=g11*g22-z.real**2-z.imag**2
disc=np.sqrt(np.maximum(tau**2-4*detg,0))
lam2=(tau-disc)/2; u=lam2/tau; x=np.clip((g11-lam2)/np.where(disc>1e-12,disc,1),0,1)
ub=np.linspace(0,0.5,9); xb=np.linspace(0,1,9)
H,_,_=np.histogram2d(u,x,bins=[ub,xb]); P=H/H.sum()
a=1/(sig*g2); b=1/(sig*g1)-1/(sig*g2)
uc=(ub[:-1]+ub[1:])/2; xc=(xb[:-1]+xb[1:])/2; du=0.0625; dx=0.125
U=uc[:,None]; X=xc[None,:]
cands=[("Lam^-3",lambda U,X:(1-2*U)**2/(a+b*(U+(1-2*U)*X))**3),
       ("Lam^-4",lambda U,X:(1-2*U)**2/(a+b*(U+(1-2*U)*X))**4),
       ("Lam^-5",lambda U,X:(1-2*U)**2/(a+b*(U+(1-2*U)*X))**5),
       ("tilt exp mean-tau",lambda U,X:(1-2*U)**2*np.exp(-b*12.0*(1-2*U)*X)),
       ("s^2 only",lambda U,X:(1-2*U)**2*np.ones_like(X)*np.ones_like(U))]
for name,f in cands:
    Fm=f(U,X); Fm/=np.sum(Fm)
    r=(P+1e-12)/(Fm+1e-12)
    print("%-18s max|ratio-1|=%.2f  median ratio=%.3f"%(name,np.max(np.abs(r-1)),np.median(r)))
print("MC P[0,0]=%.5f P[0,4]=%.5f P[7,0]=%.5f P[7,4]=%.5f"%(P[0,0],P[0,4],P[7,0],P[7,4]))
print("MC sd x=%.4f sd u=%.4f; E x=%.4f E u=%.4f"%(x.std(),u.std(),x.mean(),u.mean()))
