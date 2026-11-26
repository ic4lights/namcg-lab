#!/usr/bin/env python3
"""Round 2 checks of the two review replacements that carry mathematical content.  Writes nothing; stdout is saved as s2_s4_check_r2.out.

S2: for m(s)=sum_a s_a sigma_a (x) L_a, (L_a)_bc=-i eps_abc, the 6x6 determinant is exact degree six, vanishes to second order in each
    singular value and is nonzero at s=(1,1,1).  Exact (sympy).
S4: at N=2, gamma<=0, (C) with the convergence factor exp(-eps sum_mu Tr A_mu^2), removed last, against the Euclidean model at the same phases
    in the form of 2501.17798 Eq. Euclidean-ikkt (A_0=-i A_D, A_D Hermitian, weight exp(i(S_b+S_m))) with A_mu=exp(i phi) At_mu, mu=1..D.
    Quadrature on the ordered triple x>y>z in log variables, where the integrands are smooth; this is independent of the grids of
    n2_defC_vs_E.py, which integrate across the kinks of |V|.  Numerical check, not a proof.  Coarse grids fail at small u: at n=110 the u and f
    columns disagree by up to about 1.4, at n=290 they agree to about 1e-5, so the default is n=290 (several GB of memory, some minutes).
    lam=1/2 and S_m=-(gamma/2) tr G are 2501.17798 at N=2.  The factor is exp(-eps reg/2), reg=sum_a sum_mu (A^a_mu)^2 on the contour.
"""
import numpy as np, sympy as sp, sys
LAM=0.5
def s2():
    s1,s2_,s3=sp.symbols('s1 s2 s3')
    sig=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.Matrix([[1,0],[0,-1]])]
    L=[sp.zeros(3,3) for _ in range(3)]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                L[a][b,c]=-sp.I*sp.LeviCivita(a,b,c)
    m=sp.zeros(6,6)
    for a,s in enumerate((s1,s2_,s3)):
        m+=s*sp.kronecker_product(sig[a],L[a])
    d=sp.factor(m.det())
    print("S2: det m =",d)
    P=sp.Poly(sp.expand(d),s1,s2_,s3)
    print("S2: total degree",P.total_degree(),"; monomials",P.monoms())
    for s in (s1,s2_,s3):
        print(f"S2: at {s}=0: det={sp.expand(d.subs(s,0))}, d/d{s} at 0={sp.expand(sp.diff(d,s).subs(s,0))}, d2/d{s}2 at 0 nonzero={sp.expand(sp.diff(d,s,2).subs(s,0))!=0}, rank m={m.subs(s,0).rank()}")
    print("S2: value at (1,1,1) =",d.subs({s1:1,s2_:1,s3:1}))
    print("S2: eigenvalues of sigma.L =",m.subs({s1:1,s2_:1,s3:1}).eigenvals())
def phases():
    t=sp.symbols('t',positive=True)
    print("S4 phases: -i e^{i pi/8} e^{3 pi i/8} =",sp.simplify(-sp.I*sp.exp(sp.I*sp.pi/8)*sp.exp(3*sp.I*sp.pi/8)),"(1 means A_0=-i A_D with A_D=e^{i pi/8} At is the R_1 value e^{-3 pi i/8} At)")
    print("S4 phases: -e^{-3 pi i/4}/e^{i pi/4} =",sp.simplify(-sp.exp(-3*sp.I*sp.pi/4)/sp.exp(sp.I*sp.pi/4)),"(1 means eta-contraction on R_1 equals e^{i pi/4} times the Euclidean one)")
def ordered(n,tr=(-14.,7.),xr=(0.,14.)):
    a,wa=np.polynomial.legendre.leggauss(n)
    t=0.5*(tr[1]-tr[0])*a+0.5*(tr[1]+tr[0]); wt=0.5*(tr[1]-tr[0])*wa
    x=0.5*(xr[1]-xr[0])*a+0.5*(xr[1]+xr[0]); wx=0.5*(xr[1]-xr[0])*wa
    T,X,Y=np.meshgrid(t,x,x,indexing='ij',sparse=True)
    z=np.exp(T); y=np.exp(T+X); h=np.exp(T+X+Y)
    W=wt[:,None,None]*wx[None,:,None]*wx[None,None,:]*z*y*h
    return h,y,z,W
def Cv(gam,d,p,u,eps,G):
    """(C) on R_u with the factor; the three positions of g3 in x>y>z, wedge g+>g-."""
    h,y,z,W=G
    a=3*np.pi*u/8; b=np.pi*u/8; pg=np.exp(2j*b); pr=np.exp(-2j*a)
    Z=0; N=0
    for gp,gm,g3 in ((y,z,h),(h,z,y),(h,y,z)):
        FP=(pr*g3+pg*gp)*(pr*g3+pg*gm)
        dens=(gp*gm*g3)**((d-3)/2+p)*(gp-gm)*FP
        e2=pg**2*gp*gm-pg*pr*g3*(gp+gm)
        trG=pg*(gp+gm)-pr*g3
        reg=pg*(gp+gm)+pr*g3
        ex=np.exp(1j*LAM*e2-1j*(gam/2)*trG-eps*reg/2)
        Z=Z+np.sum(W*dens*ex); N=N+np.sum(W*dens*ex*0.5*trG)
    return N/Z,Z
def Ev(gam,d,p,f,eps,G):
    """Euclidean model of 2501.17798 form, A_mu=e^{i phi}At_mu, phi=f pi/8, with the same factor form.  f=1, eps=0 is e^{-S_E}, the (A)-limit form."""
    h,y,z,W=G
    ph=np.exp(2j*f*np.pi/8)
    e2=ph**2*(h*y+h*z+y*z); T=h+y+z
    dens=(h*y*z)**((d-3)/2+p)*(h-y)*(h-z)*(y-z)
    ex=np.exp(1j*LAM*e2-1j*(gam/2)*ph*T-eps*ph*T/2)
    Z=np.sum(W*dens*ex); N=np.sum(W*dens*ex*0.5*ph*T)
    return N/Z,Z
def table(gam,d,p,G,eps_list):
    e0,ze=Ev(gam,d,p,1.0,0.0,G); c1,zc=Cv(gam,d,p,1.0,0.0,G)
    print(f"gamma={gam}, d={d}, p={p}: E(f=1,eps=0)={e0:.7f}; C(u=1,eps=0)={c1:.7f}; |C-E|={abs(c1-e0):.2e}; |Z_C/Z_E| on the ordered triple={abs(zc/ze):.8f}; |Z_E|={abs(ze):.5g}")
    print("  eps      C_eps(u=0.45)            C_eps(u=0.6)             |diff u|   |C_eps-E|  E_eps(f=0.5)            E_eps(f=0.75)           |diff f|   |E_eps-E|")
    prev=None
    for eps in eps_list:
        c3,_=Cv(gam,d,p,0.45,eps,G); c5,_=Cv(gam,d,p,0.6,eps,G)
        e5,_=Ev(gam,d,p,0.5,eps,G); e7,_=Ev(gam,d,p,0.75,eps,G)
        print(f"  {eps:7.4f}  {c3:.6f}  {c5:.6f}  {abs(c3-c5):.1e}  {abs(c5-e0):.5f}  {e5:.6f}  {e7:.6f}  {abs(e5-e7):.1e}  {abs(e7-e0):.5f}")
        if prev is not None:
            r=2*c5-prev; print(f"           Richardson of C_eps(u=0.6) at this and 2*eps: {r:.6f}, distance to E {abs(r-e0):.2e}")
        prev=c5
if __name__=="__main__":
    s2(); phases()
    n=int(sys.argv[1]) if len(sys.argv)>1 else 290
    print(f"S4 quadrature nodes per axis: {n}")
    G=ordered(n)
    E=(0.2,0.1,0.05,0.025,0.0125,0.00625)
    table(-2.0,4,0,G,E)
    table(-5.6,4,0,G,E)
    table(0.0,9,4,G,(0.1,0.05,0.025,0.0125,0.00625))
