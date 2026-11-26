import numpy as np
from explore1 import *
# vertical quotient basis: project J onto complement of horizontal span
Q,_=np.linalg.qr(Hm.T)            # orthonormal basis of horizontal span (15x4)
def perp(v): return v-Q@(Q.T@v)
Jp={k:perp(v) for k,v in J.items()}
Mv=np.array(list(Jp.values()))
u,sv,vh=np.linalg.svd(Mv)
print("sv of vertical parts",sv)
Z=vh[:2]               # orthonormal vertical basis (2x15)
S=np.zeros((4,4,2))
for (a,b),v in Jp.items():
    c=Z@v; S[a,b]=c; S[b,a]=-c
# [D^a,D^b] = +-s S^{ab}_k Z_k : F_zeta[a,b]=sum_k zeta_k S[a,b,k]
def Fz(zeta): return np.tensordot(S,zeta,axes=([2],[0]))
for ph in np.linspace(0,np.pi,5):
    zeta=np.array([np.cos(ph),np.sin(ph)])
    F=Fz(zeta)
    ev=np.linalg.eigvals(F)
    # eta contraction: F^a_b = F_{ac} eta^{cb}
    eta=np.diag([-1,1,1,1.])
    evE=np.abs(ev.imag)
    evL=np.linalg.eigvals(F@eta)
    print("phi=%.2f  delta-contraction |im eig|:"%ph,np.sort(evE),"  eta-contraction eig:",np.round(np.sort_complex(evL),4))
