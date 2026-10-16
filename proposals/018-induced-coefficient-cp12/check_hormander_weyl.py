"""Hormander structure and nilpotent (Landau) leading symbol of Box on CP^{1,2}, explicit realisation (floats).
For random orbit points: rank of {D^a=X_{T^a}} (4), rank of {D^a,[D^a,D^b]} (6) ; vertical structure tensor S^{ab}_k ;
Landau data (f1,f2)(zeta) for the delta-contraction (Euclidean section) and the eta-contraction eigenvalues ;
Liouville normalisation nu=|Pf omega(D^0..D^3,Z1,Z2)| ; leading Weyl coefficient c0 = (1/nu)(1/64 pi^4) int dphi phi1 phi2 I(phi),
I=int u^3 du /(sinh(u phi1) sinh(u phi2)),  K(s)=c0 s^-4 (density w.r.t. Liouville measure, Poisson normalisation).
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import zeta
from cp12_realisation import *
np.set_printoptions(precision=4, suppress=True, linewidth=170)
s=-1.0
pairs=[(A,B) for A in range(6) for B in range(A+1,6)]
def vec(M0,C,D): return np.array([s*lie(C,D,A,B,M0) for (A,B) in pairs])
def Wmat(M0): return np.array([[s*lie(*p,*q,M0) for q in pairs] for p in pairs])
def structure(M0):
    D=np.array([vec(M0,a,4) for a in range(4)])
    J={(a,b):vec(M0,a,b) for a in range(4) for b in range(a+1,4)}
    Q,_=np.linalg.qr(D.T)
    Jp={k:v-Q@(Q.T@v) for k,v in J.items()}
    u,sv,vh=np.linalg.svd(np.array(list(Jp.values()))); Z=vh[:2]
    S=np.zeros((4,4,2))
    for (a,b),v in Jp.items():
        c=Z@v; S[a,b]=c; S[b,a]=-c
    G=np.array([vec(M0,A,B) for (A,B) in pairs]); W=Wmat(M0)
    def xi(v): return np.linalg.lstsq(G.T,v,rcond=None)[0]
    E=[xi(d) for d in D]+[xi(z) for z in Z]
    Om=np.array([[a@W@b for b in E] for a in E])
    nu=np.sqrt(abs(np.linalg.det(Om)))
    rk1=np.linalg.matrix_rank(D,tol=1e-9); rk2=np.linalg.matrix_rank(np.vstack([D]+list(J.values())),tol=1e-9)
    return S,nu,rk1,rk2,sv
def phis(S,ph,eta=None):
    F=np.tensordot(S,np.array([np.cos(ph),np.sin(ph)]),axes=([2],[0]))
    return np.sort(np.abs(np.linalg.eigvals(F).imag))[::2]
def c0(S,nu):
    def inner(ph):
        p1,p2=phis(S,ph)
        f=lambda u: u**3*p1*p2/(np.sinh(u*p1)*np.sinh(u*p2)) if u*min(p1,p2)>1e-12 else 0.
        return quad(f,1e-12,60/min(p1,p2),limit=400)[0]
    val=quad(inner,0,2*np.pi,limit=100)[0]
    return val/(64*np.pi**4*nu)
if __name__=="__main__":
    print("self-dual check: c0*nu =", 2*np.pi*quad(lambda u:u**3/np.sinh(u)**2,1e-12,80)[0]/(64*np.pi**4), " 3 zeta(3)/(64 pi^3) =",3*zeta(3)/(64*np.pi**3))
    rng=np.random.default_rng(5)
    rows=[]
    for t in range(12):
        z=rand_z_pos(rng,rng.uniform(0.5,4)); M0=Mfun(z); y=M0[:5,5]
        S,nu,rk1,rk2,sv=structure(M0)
        r=np.array([phis(S,ph) for ph in np.linspace(0,np.pi,9)])
        eta=np.diag([-1,1,1,1.]); F=np.tensordot(S,np.array([1.,0]),axes=([2],[0]))
        ev=np.sort_complex(np.linalg.eigvals(F@eta))
        print("y^a=",np.round(y,2),"rank1=%d rank2=%d nu=%.4g"%(rk1,rk2,nu),"f1/f2 range [%.3f,%.3f]"%((r[:,0]/r[:,1]).min(),(r[:,0]/r[:,1]).max()),"eta-contraction F.eta eig:",np.round(ev,3), "c0=%.4g"%c0(S,nu))
    # approach to y^4 = 0
    print("--- approach to the locus y^4=0 (rank of horizontal fields) ---")
    for Y4 in (3.0,1.0,0.3,0.05):
        n=2*np.sqrt(25-Y4**2); z0,_=point_at_rest(n=n,seed=3); M0=Mfun(z0)
        beta=np.arctanh(Y4/5.0)
        for sg in (1,-1):
            zb=expm(1j*sg*beta*Sig[0,4])@z0; yb=Mfun(zb)[:5,5]
            if abs(abs(yb[4])-Y4)<1e-6: break
        Mb=Mfun(zb); S,nu,rk1,rk2,sv=structure(Mb)
        D=np.array([vec(Mb,a,4) for a in range(4)]); svD=np.linalg.svd(D,compute_uv=False)
        print("y^4=%.2f y^a=%s sv(D^a)=%s rank1=%d rank2=%d"%(Y4,np.round(yb,3),np.round(svD,4),rk1,rk2))
