import numpy as np, scipy.linalg as sl
from core import *
def quad_roots(Mfun, r, seeds=(1,2)):
    res=[]
    A0=Mfun(0.0); Ap=Mfun(1.0); Am=Mfun(-1.0)
    A=A0; B=(Ap-Am)/2; C=(Ap+Am)/2-A0
    for sd in seeds:
        g=np.random.default_rng(sd)
        Pr=g.normal(size=(r,A.shape[0])); Vc=g.normal(size=(A.shape[1],r))
        a,b,c=[Pr@X@Vc for X in (A,B,C)]
        Z=np.zeros((r,r)); I=np.eye(r)
        ev=sl.eig(np.block([[Z,I],[-a,-b]]),np.block([[I,Z],[Z,c]]),right=False)
        res.append(ev[np.isfinite(ev)&(np.abs(ev)<1e6)])
    a,b=res
    return np.array([x for x in a if np.abs(b-x).min()<1e-5*(1+abs(x))])
c,w=heisenberg()
N=14; L=5
for p in (0.3,2.0):
    def Mfun(q0):
        M=M_op(c,w,heisenberg_modes(p,q0,N))
        cols=[i*N+n for i in range(40) for n in range(L+1)]
        return M[:,cols]
    r=rank(Mfun(0.37))
    rts=quad_roots(Mfun,r)
    sq=np.sort_complex(np.round(rts**2,5))
    vals,cnt=np.unique(np.round((sq-p*p)/p,3),return_counts=True)
    print('p',p,'generic rank',r,'of',40*(L+1),'roots',len(rts))
    for v,k in zip(vals,cnt): print('   (q0^2-p^2)/p =',v,' x',k)
