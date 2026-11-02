#!/usr/bin/env python3
"""N=2 exact reduction of the regulated Lorentzian integral (Definition A) to three real variables.

Variables: a in R^3 (the su(2) components of A_0), B in R^{d x 3} (those of A_i), W=B^T B, D=d+1.
Facts used:  G=-a a^T+W ; S_b=lam e2(G), lam=1/(4 g^2) ; Pf = c det(G)^{p}, p=D/2-1 with fermions, p=0 without.
Measure dB -> const det(W)^{(d-4)/2} dW ; W=O diag(w) O^T -> const |V(w)| d^3w ; O acts on a by a rotation.
Contour Gamma_u: a=e^{-i al} at, B=e^{i be} Bt, al=3 pi u/8, be=pi u/8.
After the rotation the a-integral is Gaussian in each at_k with Q_k below, and all a-moments are exact.
Output weight: exp(i lam e^{4 i be} e2(w) - eps e^{2 i be} T - i (gam/2) e^{2 i be} T), T=w1+w2+w3,
               Q_k = eps e^{-2 i al} + i lam e^{2 i (be-al)} (T-w_k) - i (gam/2) e^{-2 i al}.
Ordered w1>=w2>=w3 parametrised w1=e^s, w2=w1 e^{-v}, w3=w2 e^{-z}.
"""
import numpy as np, sys, math, itertools
from scipy.special import gamma as Gam
LAM=0.5
def nodes(n,lo,hi):
    x,w=np.polynomial.legendre.leggauss(n)
    return 0.5*(hi-lo)*x+0.5*(hi+lo),0.5*(hi-lo)*w
def compute(D,fermions,eps,u,gam=0.0,obs=(),ns=160,nv=70,nz=70,srange=None,vmax=45.,zmax=45.,chunk=40):
    """returns dict with Z and numerators; obs: list of (na,nT) meaning (|a|^2)^na T^nT, na in {0,1}"""
    d=D-1; p=(D//2-1) if fermions else 0
    al=3*np.pi*u/8; be=np.pi*u/8
    ph_meas=np.exp(1j*(3*d*be-3*al))
    if srange is None:
        hi=np.log(80.0/max(eps,1e-9)) if eps>0 else 22.0
        srange=(-10.0,min(hi,24.0))
    s,ws=nodes(ns,*srange); v,wv=nodes(nv,0.0,vmax); z,wz=nodes(nz,0.0,zmax)
    t=np.exp(s)
    # multi-index terms of (D0 - sum c_k x_k)^p
    terms=[n for n in itertools.product(range(p+1),repeat=3) if sum(n)<=p]
    res={k:0j for k in ['Z']+list(obs)}
    for start in range(0,ns,chunk):
        idx=np.arange(start,min(start+chunk,ns))
        T1,V,Z_=np.meshgrid(t[idx],v,z,indexing='ij')
        W_=(t[idx]*ws[idx])[:,None,None]*wv[None,:,None]*wz[None,None,:]
        w1=T1; w2=T1*np.exp(-V); w3=w2*np.exp(-Z_)
        jac=w2*w3  # dw1 dw2 dw3 = w1 w2 w3 ds dv dz ; w1 included in (t*ws)
        Vd=(w1-w2)*(w1-w3)*(w2-w3)
        dens=W_*jac*Vd*(w1*w2*w3)**((d-4)/2)
        T=w1+w2+w3
        e2=w1*w2+w1*w3+w2*w3
        ex=np.exp(1j*LAM*np.exp(4j*be)*e2-eps*np.exp(2j*be)*T-1j*(gam/2)*np.exp(2j*be)*T)
        Tk=[w2+w3,w1+w3,w1+w2]  # T-w_k without cancellation
        Q=[eps*np.exp(-2j*al)+1j*LAM*np.exp(2j*(be-al))*Tk[k]-1j*(gam/2)*np.exp(-2j*al) for k in range(3)]
        D0=np.exp(6j*be)*w1*w2*w3
        pref=np.exp(-2j*al+4j*be)
        # stable form: (D0 - sum c_k x_k)^p gives D0^{n0} prod (r_k)^{n_k} Gamma(n_k+1/2) times prod Q_k^{-1/2}
        rk=[-pref*w2*w3/Q[0],-pref*w1*w3/Q[1],-pref*w1*w2/Q[2]]
        base0=Gam(0.5)**3*Q[0]**(-0.5)*Q[1]**(-0.5)*Q[2]**(-0.5)
        Gr=[Gam(n+0.5)/Gam(0.5) for n in range(p+2)]
        Dpow=[np.ones_like(D0)]
        for j in range(p): Dpow.append(Dpow[-1]*D0)
        rpow=[[np.ones_like(D0)] for k in range(3)]
        for k in range(3):
            for j in range(p): rpow[k].append(rpow[k][-1]*rk[k])
        tot=np.zeros_like(D0); totA=np.zeros_like(D0)
        for n in terms:
            n0=p-sum(n)
            coef=math.factorial(p)/(math.factorial(n0)*math.factorial(n[0])*math.factorial(n[1])*math.factorial(n[2]))
            mono=coef*Dpow[n0]*rpow[0][n[0]]*rpow[1][n[1]]*rpow[2][n[2]]*Gr[n[0]]*Gr[n[1]]*Gr[n[2]]
            tot=tot+mono
            add=(n[0]+0.5)/Q[0]+(n[1]+0.5)/Q[1]+(n[2]+0.5)/Q[2]
            totA=totA+mono*add*np.exp(-2j*al)
        tot=tot*base0; totA=totA*base0
        Tr=np.exp(2j*be)*T
        res['Z']+=np.sum(dens*ex*tot)
        for o in obs:
            na,nT=o
            res[o]+=np.sum(dens*ex*(totA if na else tot)*Tr**nT)
    for k in res: res[k]*=ph_meas
    return res
def euclid(D,fermions,obs=(),**kw):
    return compute(D,fermions,0.0,1.0,obs=obs,srange=(-10.,22.),**kw)
G=dict(ns=500,nv=150,nz=150,vmax=32.,zmax=32.)
def srng(eps,smax=13.0):
    return (-8.0,min(np.log(80.0/eps),smax)) if eps>0 else (-8.0,smax)
if __name__=="__main__":
    O=[(1,0),(0,1)]
    print("=== D=10 with Pfaffian, N=2, lam=1/2 (g^2 N = 1) ===")
    E=compute(10,True,0.0,1.0,obs=O,srange=srng(0),**G)
    Eb=compute(10,True,0.0,1.0,obs=O,srange=(-10.,16.),ns=800,nv=220,nz=220,vmax=44.,zmax=44.)
    ra=E[(1,0)]/E['Z']; rt=E[(0,1)]/E['Z']
    print(f"Euclid u=1: Z={E['Z']:.8e}; phase(Z)/pi={np.angle(E['Z'])/np.pi:.6f}; grid check Z ratio {Eb['Z']/E['Z']:.8f}, <T> {Eb[(0,1)]/Eb['Z']:.8f} vs {rt:.8f}")
    tilde_a=ra/np.exp(-3j*np.pi/4); tilde_t=rt/np.exp(1j*np.pi/4)
    print(f"  tilde: <|at|^2>={tilde_a:.8f}, <Tt>={tilde_t:.8f}; SO(10) predicts ratio 9: {tilde_t/tilde_a:.8f}")
    print("Cauchy at fixed eps: u independence of Z, <|a|^2>, <T>")
    for eps in (1.0,0.3):
        for u in (0.3,0.45,0.6):
            R=compute(10,True,eps,u,obs=O,srange=srng(eps),**G)
            print(f"  eps={eps:5.3f} u={u:.2f}: Z/Z_E={R['Z']/E['Z']:.8f}  <|a|^2>={R[(1,0)]/R['Z']:.8f}  <T>={R[(0,1)]/R['Z']:.8f}")
    trG=tilde_a+tilde_t
    print("eps->0 at u=0.6, targets <|a|^2>=%s <T>=%s"%(np.round(ra,6),np.round(rt,6)))
    print(f"  <tr G_E>={trG:.8f}, predicted (Z/Z_E-1)/eps -> {-np.exp(1j*np.pi/4)*0.8*trG:.6f}")
    for eps in (0.1,0.03,0.01,0.003,0.001,0.0003,0.0001):
        R=compute(10,True,eps,0.6,obs=O,srange=srng(eps),**G)
        z=R['Z']/E['Z']
        print(f"  eps={eps:8.5f}: Z/Z_E={z:.7f}  (Z/Z_E-1)/eps={(z-1)/eps:.5f}  <|a|^2>-E={R[(1,0)]/R['Z']-ra:.3e}  <T>-E={R[(0,1)]/R['Z']-rt:.3e}")
    print("Moments near the bound: |<T^n>| , degree k=2n, at u=0.6, finer range; Euclid column is u=1 at eps=0")
    GM=dict(ns=700,nv=200,nz=200,vmax=44.,zmax=44.)
    Em=compute(10,True,0.0,1.0,obs=[(0,n) for n in (5,6,7,8)],srange=(-8.,20.),**GM)
    for n in (5,6,7,8):
        vals=[]
        for eps in (1e-1,1e-2,1e-3,1e-4,1e-5,1e-6):
            R=compute(10,True,eps,0.6,obs=[(0,n)],srange=(-8.,min(np.log(80/eps),20.)),**GM)
            vals.append(R[(0,n)]/R['Z'])
        print(f"  k={2*n:2d}: "+"  ".join(f"{e:.0e}:{abs(v):.6g}" for e,v in zip((1e-1,1e-2,1e-3,1e-4,1e-5,1e-6),vals))+f"   | Euclid cut at s<20: {abs(Em[(0,n)]/Em['Z']):.6g}")
    print("=== D=5 bosonic, N=2 (k_c=1), Z only ===")
    Ebo=compute(5,False,0.0,1.0,srange=srng(0),**G)
    for eps in (0.1,0.01,0.001,0.0001):
        R=compute(5,False,eps,0.6,srange=srng(eps),**G)
        print(f"  eps={eps:8.5f}: Z/Z_E={R['Z']/Ebo['Z']:.7f}")
    print("=== joint limit window, D=10: gamma = kappa eps, u=0.5 ===")
    for kappa in (-1.0,0.2):
        for eps in (0.1,0.01,0.001,0.0001):
            R=compute(10,True,eps,0.5,gam=kappa*eps,obs=O,srange=srng(eps),**G)
            print(f"  kappa={kappa:5.2f} eps={eps:7.4f}: Z/Z_E={R['Z']/E['Z']:.6f}  <T>-E={R[(0,1)]/R['Z']-rt:.3e}")
