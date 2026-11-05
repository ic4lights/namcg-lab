#!/usr/bin/env python3
"""Definition C at N=2, d=4, bosonic, on the REAL contour with a convergence factor exp(-eps(g+ + g- + g3)),
no contour rotation: the g3 integral and the m=x(1-x) integral are done in closed form, leaving one integral over
sigma=g+ + g-.  Used (i) against the rotated values of n2_defC_vs_E.py at gamma<0 and (ii) against the plotted points of
2501.17798 at gamma>0, where no rotation is available.  Richardson extrapolation in eps.
"""
import numpy as np
from scipy.special import gamma as Gam
LAM=0.5
def Fj(a,kap):
    """int_0^{1/4} m^{a-1} exp(i kap m) dm for arrays kap>=0"""
    b=0.25; out=np.zeros_like(kap,dtype=complex)
    small=kap<80.0
    x,w=np.polynomial.legendre.leggauss(200)
    # substitute m=b t^2 to remove the endpoint power
    t=0.5*(x+1); wt=0.5*w
    m=b*t**2; jac=2*b*t
    out[small]=np.sum((m**(a-1)*jac*wt)[None,:]*np.exp(1j*kap[small][:,None]*m[None,:]),axis=1)
    K=kap[~small]
    lead=Gam(a)*(-1j*K)**(-a)
    s=np.zeros_like(K,dtype=complex); term=np.ones_like(K,dtype=complex)
    for n in range(0,12):
        s+=term
        term=term*(a-1-n)/( -1j*K*b)*(-1) if False else term*(-(a-1-n))/(1j*K*b)
    out[~small]=lead+np.exp(1j*K*b)*b**(a-1)/(1j*K)*s
    return out
def C_real(gam,eps,smax=None,ngrid=400000):
    smax=smax or min(90.0/eps,400.0)
    # composite grid, dense near the pole sigma=gam for gam>0
    x,w=np.polynomial.legendre.leggauss(8)
    edges=np.unique(np.concatenate([np.linspace(0,smax,ngrid//8+1),
             (np.linspace(max(gam-6,0),gam+6,6001) if gam>0 else np.array([0.]))]))
    a=edges[:-1];b=edges[1:]
    sig=(0.5*(b-a)[:,None]*x[None,:]+0.5*(b+a)[:,None]).ravel(); ws=(0.5*(b-a)[:,None]*w[None,:]).ravel()
    Y=eps+1j*LAM*sig-1j*gam/2
    kap=LAM*sig**2
    F0=Fj(1.5,kap); F1=Fj(2.5,kap)
    pre=ws*sig**3*np.exp(-eps*sig-1j*gam*sig/2)
    g=lambda q:Gam(q)*Y**(-q)
    Z=np.sum(pre*(2*F0*(g(3.5)+sig*g(2.5))+2*F1*sig**2*g(1.5)))
    Ng3=np.sum(pre*(2*F0*(g(4.5)+sig*g(3.5))+2*F1*sig**2*g(2.5)))
    Ns=np.sum(pre*sig*(2*F0*(g(3.5)+sig*g(2.5))+2*F1*sig**2*g(1.5)))
    return 0.5*(Ns-Ng3)/Z,Z
if __name__=="__main__":
    print("<tr A_mu A^mu> on the real contour of Definition C at N=2,d=4,bosonic; last column is Richardson in eps")
    print("Precision: at eps<=0.05 and |gamma|>=5 double precision is lost to cancellation; compare columns before using an entry.")
    print("gamma   eps=0.4            eps=0.2            eps=0.1            eps=0.05           Richardson(0.1,0.05)")
    for gam in (-10.1,-5.6,-2.0,-1.0,-0.5,1.0,2.0,3.3,5.6,7.8,10.0):
        v=[C_real(gam,e)[0] for e in (0.4,0.2,0.1,0.05)]
        rich=2*v[3]-v[2]
        print(f"{gam:6.2f} "+" ".join(f"{z:.4f}" for z in v)+f"  {rich:.4f}")
