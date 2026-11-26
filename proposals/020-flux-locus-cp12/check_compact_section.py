"""Compact real form so(6) (delta_AB everywhere): orbit CP^3 of SU(4); T^a=M^{a4}, a=1..4; delta contraction.
Prediction (proposal-r1 sec. A): Q=y4^2 delta + y y^T has eigenvalues (l^2 on yhat, y4^2 x3), so f2/f1=|y4|/l for ALL zeta and
all fibre points; f1=f2 only over the poles y_a=0 (|y4|=l)."""
import numpy as np, itertools
from check_flux_classification import hodge_split, amp, flux_ratio, sqrtm_sym
s1=np.array([[0,1],[1,0]],complex);s2=np.array([[0,-1j],[1j,0]],complex);s3=np.diag([1,-1]).astype(complex);I2=np.eye(2,dtype=complex)
k=lambda *m: __import__('functools').reduce(np.kron,m)
g=[k(s1,I2,I2),k(s2,I2,I2),k(s3,s1,I2),k(s3,s2,I2),k(s3,s3,s1),k(s3,s3,s2)]
chir=np.eye(8,dtype=complex)
for G in g: chir=chir@G
w,v=np.linalg.eig(chir); sel=np.where(abs(w-w[0])<1e-9)[0]; V,_=np.linalg.qr(v[:,sel])
Sig=np.zeros((6,6,4,4),complex)
for A in range(6):
    for B in range(6): Sig[A,B]=V.conj().T@(0.25j*(g[A]@g[B]-g[B]@g[A]))@V
delta=np.eye(6)
def lie(A,B,C,D,M): return delta[A,C]*M[B,D]-delta[A,D]*M[B,C]-delta[B,C]*M[A,D]+delta[B,D]*M[A,C]
def Mfun(z): return np.array([[np.real(z.conj()@Sig[A,B]@z) for B in range(6)] for A in range(6)])
def PB(A,B,C,D,z): return np.real(-1j*(z.conj()@Sig[A,B]@Sig[C,D]@z-z.conj()@Sig[C,D]@Sig[A,B]@z))
rng=np.random.default_rng(1); z=rng.normal(size=4)+1j*rng.normal(size=4); z*=np.sqrt(2/np.real(z.conj()@z)); M=Mfun(z)
rat=[PB(0,1,1,2,z)/lie(0,1,1,2,M),PB(0,4,4,5,z)/lie(0,4,4,5,M),PB(1,2,2,3,z)/lie(1,2,2,3,M)]
print("PB/lie ratios (must be one constant):",np.round(rat,6))
pairs=[(A,B) for A in range(6) for B in range(A+1,6)]
sgn=-1.0
def vec(M0,C,D): return np.array([sgn*lie(C,D,A,B,M0) for (A,B) in pairs])
res=[]
for t in range(200):
    n=rng.uniform(0.5,4); z=rng.normal(size=4)+1j*rng.normal(size=4); z*=np.sqrt(n/np.real(z.conj()@z)); M0=Mfun(z)
    y=M0[:4,5]; y4=M0[4,5]; ell=np.sqrt(y@y+y4**2)
    D=np.array([vec(M0,a,4) for a in range(4)]); J={(a,b):vec(M0,a,b) for a in range(4) for b in range(a+1,4)}
    rk1=np.linalg.matrix_rank(D,tol=1e-9); rk2=np.linalg.matrix_rank(np.vstack([D]+list(J.values())),tol=1e-9)
    Qr,_=np.linalg.qr(D.T); Jp={kk:vv-Qr@(Qr.T@vv) for kk,vv in J.items()}
    u,sv,vh=np.linalg.svd(np.array(list(Jp.values()))); Z=vh[:2]; S=np.zeros((4,4,2))
    for (a,b),vv in Jp.items(): c=Z@vv; S[a,b]=c; S[b,a]=-c
    rr=[]
    for ph in np.linspace(0,np.pi,45):
        F=S[:,:,0]*np.cos(ph)+S[:,:,1]*np.sin(ph); f1,f2,_,p,r=flux_ratio(F); rr.append(f2/f1)
    res.append((rk1,rk2,min(rr),max(rr),abs(y4)/ell))
res=np.array(res)
print("ranks (horizontal, horizontal+J):",set(map(tuple,res[:,:2].astype(int))))
print("max |f2/f1 - |y4|/l| over 200 points x 45 zeta directions:",np.max(np.abs(res[:,2]-res[:,4])),np.max(np.abs(res[:,3]-res[:,4])))
print("f2/f1 range:",res[:,2].min(),res[:,3].max())
