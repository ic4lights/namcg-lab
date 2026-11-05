#!/usr/bin/env python3
"""Checks the Pfaffian facts used in 053.

(1) N=2, D=4,6,10: Pf M(A) = c_D det(G)^{D/2-1}, G_ab = eta^{mu nu} A^a_mu A^b_nu, at random COMPLEX A,
    with explicit real symmetric sigma^mu (sigma^0 = 1) satisfying the Clifford relation.
(2) Cauchy-Binet: |det G(rotated)| <= det G_E(tilde A) pointwise (N=2).
(3) N=3, D=10: along a flat direction, x_1 in the Cartan generator J commuting with su(2)', the
    size of Pf with Gamma^0 multiplied by a phase scales with the same power of omega (the J-F block
    of the other matrices) as at phase 1: |Pf| ~ omega^16 at fixed y.  This tests the input of the
    Austing-Wheater induction step, the 2(D-2) xi-zero modes saturated by omega, for phases.
"""
import numpy as np, itertools, math
rng=np.random.default_rng(53)
s0=np.eye(2); sx=np.array([[0,1],[1,0.]]); sz=np.diag([1.,-1]); e=np.array([[0,1],[-1,0.]])
def kron(*a):
    r=np.eye(1)
    for x in a: r=np.kron(r,x)
    return r
def real_sym_gammas(D):
    """D-1 mutually anticommuting real symmetric matrices squaring to 1, size 2^{..}"""
    if D==4:
        return [kron(sx,s0), kron(sz,s0), kron(e,e)]          # 4x4, three
    if D==6:
        return [kron(sx,s0,s0),kron(sz,s0,s0),kron(e,sx,e),kron(e,sz,e),kron(e,e,s0)]  # 8x8, five
    if D==10:
        return [kron(sx,s0,s0,s0),kron(sz,s0,s0,s0),
                kron(e,sx,e,s0),kron(e,sz,e,s0),kron(e,e,s0,sx),kron(e,e,s0,sz),
                kron(e,s0,sx,e),kron(e,s0,sz,e),kron(e,e,e,e)]  # 16x16, nine
    raise ValueError
def check_cliff(g):
    n=g[0].shape[0]
    for i,j in itertools.product(range(len(g)),repeat=2):
        ac=g[i]@g[j]+g[j]@g[i]
        assert np.allclose(ac,2*np.eye(n)*(i==j)),(i,j)
    for x in g: assert np.allclose(x,x.T)
def pfaffian(A):
    """Parlett-Reid style elimination with pivoting, complex antisymmetric."""
    A=A.astype(complex).copy(); n=A.shape[0]; assert n%2==0
    pf=1.0+0j
    for k in range(0,n-1,2):
        kp=k+1+np.argmax(np.abs(A[k+1:,k]))
        if kp!=k+1:
            A[[k+1,kp],:]=A[[kp,k+1],:]; A[:,[k+1,kp]]=A[:,[kp,k+1]]; pf=-pf
        if A[k+1,k]==0: return 0j
        pf*=A[k,k+1]
        if k+2<n:
            tau=A[k,k+2:]/A[k,k+1]
            A[k+2:,k+2:]+= np.outer(tau,A[k+2:,k+1])-np.outer(A[k+2:,k+1],tau)
    return pf
def su_f(N):
    """Real structure constants f_abc in Hermitian basis, Tr t_a t_b = delta_ab/2 , [t_a,t_b]= i f_abc t_c"""
    t=[]
    for i in range(N):
        for j in range(i+1,N):
            m=np.zeros((N,N),complex); m[i,j]=m[j,i]=.5; t.append(m)
            m=np.zeros((N,N),complex); m[i,j]=-.5j; m[j,i]=.5j; t.append(m)
    for l in range(1,N):
        m=np.zeros((N,N),complex)
        for i in range(l): m[i,i]=1
        m[l,l]=-l
        t.append(m/np.sqrt(2*l*(l+1)))
    g=len(t); f=np.zeros((g,g,g))
    for a,b,c in itertools.product(range(g),repeat=3):
        f[a,b,c]=(-2j*np.trace((t[a]@t[b]-t[b]@t[a])@t[c])).real
    return t,f
def M_matrix(A,sig,f):
    """A[mu,a] ; sig list length D with sig[0]=1 ; M = sum_mu sig^mu kron (A^b_mu f_bca)"""
    g=f.shape[0]; n=sig[0].shape[0]
    ad=np.einsum('mb,bca->mca',A,f)
    M=np.zeros((n*g,n*g),complex)
    for mu,s in enumerate(sig):
        M+=np.kron(s,ad[mu])
    return M
def main():
    print("(1) Pf = c det(G)^{D/2-1} at random complex A, N=2")
    t,f=su_f(2)
    for D in (4,6,10):
        gam=real_sym_gammas(D); check_cliff(gam)
        n=gam[0].shape[0]
        sig=[np.eye(n)]+gam
        eta=np.diag([-1.]+[1.]*(D-1))
        cs=[]
        for _ in range(6):
            A=rng.normal(size=(D,3))+1j*rng.normal(size=(D,3))
            M=M_matrix(A,sig,f)
            assert np.allclose(M,-M.T)
            pf=pfaffian(M); G=A.T@eta@A
            cs.append(pf/np.linalg.det(G)**(D//2-1))
        cs=np.array(cs)
        print(f"  D={D}: c={cs[0]:.10g}, max rel spread {np.max(np.abs(cs/cs[0]-1)):.2e}, sqrt(det M)/Pf check at last A: {abs(np.linalg.det(M)/pf**2-1):.2e}")
    print("(2) Cauchy-Binet: |det G(u)| <= det G_E on 20000 random real A~, D=10, u in (0,1]")
    D=10; worst=0
    for _ in range(20000):
        At=rng.normal(size=(D,3))*rng.lognormal(0,1.5,size=(D,1))
        u=rng.uniform(0,1); a=3*np.pi*u/8; b=np.pi*u/8
        ph=np.array([np.exp(-1j*a)]+[np.exp(1j*b)]*9)[:,None]
        A=ph*At; eta=np.diag([-1.]+[1.]*9)
        lhs=abs(np.linalg.det(A.T@eta@A)); rhs=np.linalg.det(At.T@At)
        worst=max(worst,lhs/rhs)
    print(f"  max ratio |det G(u)|/det G_E = {worst:.6f} (bound 1)")
    print("(3) N=3, D=10: scaling of |Pf| with omega at fixed y, flat direction, phase on Gamma^0")
    t,f=su_f(3); g=8
    gam=real_sym_gammas(10); sig=[np.eye(16)]+gam
    # su(2)' = indices of lambda_1,2,3 : basis order here (0,1),(0,1)im,(0,2),(0,2)im,(1,2),(1,2)im,d1,d2
    idx_su2=[0,1,6]; idx_J=[7]; idx_F=[2,3,4,5]
    for theta,label in ((0.,'phase 1'),(-np.pi/2,'Wick phase -i'),(-np.pi/4,'phase e^{-i pi/4}')):
        ph=np.array([np.exp(1j*theta)]+[1.]*9)[:,None]
        y=np.random.default_rng(7).normal(size=(10,3))
        rho=np.random.default_rng(8).normal(size=(10,1)); rho[1,0]=3.0  # x_1 along J, ad-mass on F
        om0=np.random.default_rng(9).normal(size=(10,4)); om0[1,:]=0
        vals=[]
        wl=[1e-1,3e-2,1e-2,3e-3]
        for w in wl:
            A=np.zeros((10,8)); A[:,idx_su2]=y; A[:,idx_J]=rho; A[:,idx_F]=w*om0
            A[1,idx_su2]=0  # x_1 purely Cartan J
            A=ph*A
            sgn,ld=np.linalg.slogdet(M_matrix(A,sig,f))
            vals.append(0.5*ld)
        slopes=np.diff(vals)/np.diff(np.log(wl))
        print(f"  {label:20s} d log|Pf| / d log omega = {np.round(slopes,3)} (leading power >=16 expected)")
if __name__=="__main__":
    main()
