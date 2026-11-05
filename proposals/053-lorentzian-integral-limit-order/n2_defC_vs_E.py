#!/usr/bin/env python3
"""N=2, D=d+1: Definition C (the Faddeev-Popov formula of 2404.14045, 2501.17798) against the Euclidean model,
both reduced exactly to three real variables, at gamma<=0.

Reduction of C for d>=4.  Delta_FP prod_i delta(tr A_0 A_i) with a=su(2) components of A_0 forces a.B_i=0, so with a=r e_3:
   B_i=(x_i,y_i,0); G=diag(g+,g-,-r^2) after an SO(2) rotation of (x,y); Delta_FP=(r^2/2)^{d-2}(r^2+g+)(r^2+g-)/4.
The a=0 sector (spacelike G) has FP -> 0 against delta(0), and it drops out as the delta smearing is removed (see proposal).
   Z_C ~ int dr r^{d-2} dg+ dg- |g+-g-| (g+g-)^{(d-3)/2} (r^2+g+)(r^2+g-) (g+ g- r^2)^{p} exp(i lam e2(G) - i (gam/2) trG)
with g3=r^2: r^{d-2}dr = g3^{(d-3)/2} dg3 /2.  p=D/2-1 with fermions (Pf=c det(G)^p, with det G=-g+g-r^2), p=0 without.
Euclidean model: Z_E ~ int d^3g (g1g2g3)^{(d-3)/2+p} |V(g)| exp(i lam e2(g)-i(gam/2) tr g) in the Hermitian contour.
Under a=3pi u/8,b=pi u/8, C maps to the same integrand as E with |g_+-g_3||g_--g_3| -> (g_+-g_3)(g_--g_3) at u=1.
Observable tr A_mu A^mu=(1/2)tr G, lam=1/2.
"""
import numpy as np
LAM=0.5
def nodes(n,lo,hi):
    x,w=np.polynomial.legendre.leggauss(n)
    return 0.5*(hi-lo)*x+0.5*(hi+lo),0.5*(hi-lo)*w
def grids(n,R):
    s,ws=nodes(n,*R); g=np.exp(s); dg=g*ws
    A,B,C=np.meshgrid(g,g,g,indexing='ij',sparse=False)
    W=dg[:,None,None]*dg[None,:,None]*dg[None,None,:]
    return A,B,C,W
def Eval(gam,d,p,n=220,R=(-16.,8.)):
    """E at the Euclidean ray u=1: g -> e^{i pi/4} g, exact real damping."""
    G1,G2,G3,W=grids(n,R)
    ph=np.exp(1j*np.pi/4)
    e2=G1*G2+G1*G3+G2*G3; T=G1+G2+G3
    V=np.abs((G1-G2)*(G1-G3)*(G2-G3))
    dens=(G1*G2*G3)**((d-3)/2+p)*V
    ex=np.exp(-LAM*e2-1j*(gam/2)*ph*T)
    Z=np.sum(W*dens*ex); N=np.sum(W*dens*ex*0.5*T)*ph
    return N/Z,Z
def Cval(gam,d,p,u,n=220,R=(-16.,8.)):
    Gp,Gm,G3,W=grids(n,R)
    a=3*np.pi*u/8; b=np.pi*u/8
    pg=np.exp(2j*b); pr=np.exp(-2j*a)
    FP=(pr*G3+pg*Gp)*(pr*G3+pg*Gm)
    dens=(Gp*Gm*G3)**((d-3)/2+p)*np.abs(Gp-Gm)*FP
    e2=pg**2*Gp*Gm-pg*pr*G3*(Gp+Gm)
    trG=pg*(Gp+Gm)-pr*G3
    ex=np.exp(1j*LAM*e2-1j*(gam/2)*trG)
    Z=np.sum(W*dens*ex); N=np.sum(W*dens*ex*0.5*trG)
    return N/Z,Z
if __name__=="__main__":
    print("(a) N=2,d=4,bosonic: <tr A_mu A^mu>, E at u=1, C at u=1 and at u=0.7, u=0.5 (the Hermitian-side value by Cauchy)")
    print(" gamma    E(u=1)                 C(u=1)                 C(u=0.7)               C(u=0.5)")
    for gam in (-45,-22,-14,-10.1,-7.9,-5.6,-3,-2,-1,-0.5,-0.2,-0.1,-0.05,-0.02):
        e,_=Eval(gam,4,0); c1,_=Cval(gam,4,0,1.0); c7,_=Cval(gam,4,0,0.7,n=260); c5,_=Cval(gam,4,0,0.5,n=260)
        print(f"{gam:7.2f}  {e:.5f}  {c1:.5f}  {c7:.5f}  {c5:.5f}")
    print("(a2) |gamma|^{1/2} |<tr A^2>| as gamma->0-, expected finite limit since k=2 > k_c=1 at N=2, d=4")
    for gam in (-0.2,-0.05,-0.0125,-0.003,-0.0008):
        e,_=Eval(gam,4,0,n=260,R=(-16.,12.)); print(f"  gamma={gam:8.4f}: |<trA^2>|={abs(e):.4f}, |gamma|^(1/2)*|.|={abs(gam)**.5*abs(e):.4f}")
    print("(b) N=2,D=10, Pfaffian included, gamma=0, u=1 and u=0.7: <tr A_mu A^mu> from C and from E")
    e,_=Eval(0.0,9,4); c1,_=Cval(0.0,9,4,1.0); c7,_=Cval(0.0,9,4,0.7,n=260)
    print(f"  E={e:.6f}, C(u=1)={c1:.6f}, C(u=0.7)={c7:.6f}")
    print("(c) N=2, d=5,6,7 bosonic, gamma=-1, u=1: equality of E and C, tr A^2 and (tr A^2)^0")
    for d in (5,6,7):
        e,_=Eval(-1.0,d,0); c,_=Cval(-1.0,d,0,1.0); print(f"  d={d}: E={e:.6f} C={c:.6f}")
