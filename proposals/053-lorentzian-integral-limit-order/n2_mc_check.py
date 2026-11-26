#!/usr/bin/env python3
"""Independent checks of n2_reduced.py on the REAL contour (u=0, Hermitian A) at finite eps.

(i)  D=5, no fermions: raw Monte Carlo of the full 15-dimensional integral, Gaussian exp(-eps sum (A^a_mu)^2), weight exp(i lam e2(G)).
(ii) D=10 with det(G)^4: Monte Carlo over B only (d+8 rows, so that W carries det(W)^{(d-4)/2+4}), with the a-integral done from the
     Gaussian-moment formula in the eigenbasis of W.  Tests the Wishart and Vandermonde reduction of the W integral.
(iii) D=10: the Gaussian-moment formula itself against three-dimensional quadrature in a at one sample W.
"""
import numpy as np, itertools, math, sys
sys.path.insert(0,'.')
from n2_reduced import compute, LAM
from scipy.special import gamma as Gam
def a_terms(w,eps,p=4):
    """returns E_a[det(G)^p e^{...}] and with |a|^2, per sample, at u=0, weights e^{-a_k^2 Q_k}, divided by det(W)^p"""
    w1,w2,w3=w[:,0],w[:,1],w[:,2]
    T=w1+w2+w3
    Q=[eps+1j*LAM*(T-w[:,k]) for k in range(3)]
    tot=0;totA=0
    for n in itertools.product(range(p+1),repeat=3):
        if sum(n)>p: continue
        n0=p-sum(n)
        coef=math.factorial(p)/(math.factorial(n0)*math.factorial(n[0])*math.factorial(n[1])*math.factorial(n[2]))
        mono=coef*np.ones_like(w1,dtype=complex)
        for k in range(3):
            mono=mono*(-1/(w[:,k]*Q[k]))**n[k]*(Gam(n[k]+0.5)/Gam(0.5))
        tot=tot+mono
        totA=totA+mono*sum((n[k]+0.5)/Q[k] for k in range(3))
    base=Gam(0.5)**3/(np.sqrt(Q[0])*np.sqrt(Q[1])*np.sqrt(Q[2]))  # principal branch factor by factor
    return tot*base,totA*base
def mc_d10(eps,nsamp=6_000_000,seed=11,chunk=200_000):
    rng=np.random.default_rng(seed); sig=np.sqrt(1/(2*eps)); out=[]; done=0
    while done<nsamp:
        n=min(chunk,nsamp-done); done+=n
        B=rng.normal(scale=sig,size=(n,9+8,3))
        W=np.einsum('nia,nib->nab',B,B)
        w=np.linalg.eigvalsh(W)
        e2=w[:,0]*w[:,1]+w[:,0]*w[:,2]+w[:,1]*w[:,2]; T=w.sum(axis=1)
        z,za=a_terms(w,eps)
        f=np.exp(1j*LAM*e2)
        out.append((np.mean(f*z),np.mean(f*za),np.mean(f*z*T)))
    b=np.array(out); m=b.mean(axis=0)
    return m[1]/m[0],m[2]/m[0],(b[:,1]/b[:,0]).std()/np.sqrt(len(b)),(b[:,2]/b[:,0]).std()/np.sqrt(len(b))
def mc_d5(eps,nsamp=20_000_000,seed=5,chunk=400_000):
    rng=np.random.default_rng(seed); sig=np.sqrt(1/(2*eps)); out=[]; done=0
    while done<nsamp:
        n=min(chunk,nsamp-done); done+=n
        a=rng.normal(scale=sig,size=(n,3)); B=rng.normal(scale=sig,size=(n,4,3))
        G=np.einsum('nia,nib->nab',B,B)-np.einsum('na,nb->nab',a,a)
        tr=np.trace(G,axis1=1,axis2=2); e2=0.5*(tr**2-np.einsum('nab,nba->n',G,G))
        w=np.exp(1j*LAM*e2); A2=(a**2).sum(axis=1); T=(B**2).sum(axis=(1,2))
        out.append((np.mean(w),np.mean(w*A2),np.mean(w*T)))
    b=np.array(out); m=b.mean(axis=0)
    return m[1]/m[0],m[2]/m[0],(b[:,1]/b[:,0]).std()/np.sqrt(len(b)),(b[:,2]/b[:,0]).std()/np.sqrt(len(b))
if __name__=="__main__":
    O=[(1,0),(0,1)]
    print("(iii) a-moment formula vs quadrature, D=10, sample w=(0.7,1.3,2.9), eps=0.5")
    w=np.array([[0.7,1.3,2.9]]); eps=0.5
    z,za=a_terms(w,eps)
    x,wx=np.polynomial.legendre.leggauss(140); L=9.0; g=L*x; wg=L*wx
    A1,A2,A3=np.meshgrid(g,g,g,indexing='ij'); WW=wg[:,None,None]*wg[None,:,None]*wg[None,None,:]
    T=w.sum(); Q=[eps+1j*LAM*(T-w[0,k]) for k in range(3)]
    ex=np.exp(-Q[0]*A1**2-Q[1]*A2**2-Q[2]*A3**2)
    # det(W - a a^T)/det W = 1 - sum a_k^2/w_k
    d=(1-A1**2/0.7-A2**2/1.3-A3**2/2.9)**4
    print(f"  Z: formula {z[0]:.8f}  quadrature {np.sum(WW*ex*d):.8f}")
    print(f"  <|a|^2>Z: formula {za[0]:.8f}  quadrature {np.sum(WW*ex*d*(A1**2+A2**2+A3**2)):.8f}")
    print("(i) D=5 no fermions, eps=1 and 0.5: raw MC on Hermitian matrices vs reduced u=0 and u=0.3")
    for eps in (1.0,0.5):
        ra,rt,ea,et=mc_d5(eps); print(f"  eps={eps}: MC <|a|^2>={ra:.5f} +- {ea:.5f}  <T>={rt:.5f} +- {et:.5f}")
        for u in (0.0,0.3):
            R=compute(5,False,eps,u,obs=O,ns=1000 if u==0 else 300,nv=90,nz=90,vmax=25.,zmax=25.,srange=(-10.,np.log(100/eps)))
            print(f"           reduced u={u:.1f}: <|a|^2>={R[(1,0)]/R['Z']:.5f}  <T>={R[(0,1)]/R['Z']:.5f}")
    print("(ii) D=10, eps=3 and 1.5: MC over B, a-integral exact, vs reduced u=0 and u=0.3")
    for eps in (3.0,1.5):
        ra,rt,ea,et=mc_d10(eps); print(f"  eps={eps}: MC <|a|^2>={ra:.5f} +- {ea:.5f}  <T>={rt:.5f} +- {et:.5f}")
        for u in (0.0,0.3):
            R=compute(10,True,eps,u,obs=O,ns=1000 if u==0 else 300,nv=90,nz=90,vmax=25.,zmax=25.,srange=(-8.,np.log(120/eps)))
            print(f"           reduced u={u:.1f}: <|a|^2>={R[(1,0)]/R['Z']:.5f}  <T>={R[(0,1)]/R['Z']:.5f}")
