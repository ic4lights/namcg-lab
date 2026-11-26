import numpy as np, sys
from cp12_realisation import *
np.set_printoptions(precision=5, suppress=True, linewidth=160)
rng=np.random.default_rng(5)
s=-1.0
pairs=[(A,B) for A in range(6) for B in range(A+1,6)]
idx={p:i for i,p in enumerate(pairs)}
def vec(M0,C,D):
    v=np.zeros(15)
    for (A,B) in pairs: v[idx[(A,B)]]=s*lie(C,D,A,B,M0)
    return v
def analyse(M0):
    D=[vec(M0,a,4) for a in range(4)]
    J={(a,b):vec(M0,a,b) for a in range(4) for b in range(a+1,4)}
    Hm=np.array(D); Q,_=np.linalg.qr(Hm.T)
    Jp={k:v-Q@(Q.T@v) for k,v in J.items()}
    Mv=np.array(list(Jp.values())); u,sv,vh=np.linalg.svd(Mv); Z=vh[:2]
    S=np.zeros((4,4,2))
    for (a,b),v in Jp.items():
        c=Z@v; S[a,b]=c; S[b,a]=-c
    return S,sv
def fE(S,zeta,eta):
    F=np.tensordot(S,zeta,axes=([2],[0]))
    return F
res=[]
for t in range(12):
    z=rand_z_pos(rng,rng.uniform(0.5,4)); M0=Mfun(z)
    y=M0[:5,5]; ell2=-(y@np.diag([-1,1,1,1,1.])@y)
    S,sv=analyse(M0)
    r=[]
    for ph in np.linspace(0,np.pi,7):
        zeta=np.array([np.cos(ph),np.sin(ph)])
        F=fE(S,zeta,None)
        ev=np.sort(np.abs(np.linalg.eigvals(F).imag))[::2]
        r.append(ev)
    r=np.array(r)
    print("y=",np.round(y,2)," ell2=%.2f"%ell2," f1/f2 over zeta-angle:",np.round(r[:,0]/r[:,1],3))
