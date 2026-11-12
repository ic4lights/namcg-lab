"""s1: compact member of the 060 family at finite N, explicit matrices.

Background: X_a = alpha*M_{a5}, a=1..4, M_AB the so(5) generators on V_n = Sym^n(C^4),
placed along four spacelike target directions of a (9,1) contraction. Mass gamma = 3 alpha^2.
Checks:
 (a) EOM  sum_b [X_b,[X_b,X_a]] = gamma X_a.
 (b) the exact bosonic Hessian of S = Tr(-1/4 [X_mu,X_nu][X^mu,X^nu] - gamma/2 X_mu X^mu)
     plus the background Feynman gauge term equals, on the 4-block,
       K_A = alpha^2 [ C5 - C4ad + s (C4tot - C4ad - 3) ] - gamma
     for one sign s, and on each transverse direction (spacelike or timelike, up to the overall
     sign eta^{ii}) K_perp = alpha^2 (C5 - C4ad) - gamma.
 (c) (Gamma^a ad X_a)^2 restricted to a Weyl spinor of so(4) equals
       alpha^2 [ C5 - C4ad + s' (C4tot - C4ad - 3/2) ].
 (d) ghost operator = box = alpha^2 (C5 - C4ad).
Everything is compared eigenvalue by eigenvalue (sorted spectra).
"""
import itertools, numpy as np
np.set_printoptions(linewidth=160)

def gammas5():
    s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]]); s3=np.diag([1.,-1]).astype(complex); I=np.eye(2)
    g=[np.kron(s1,s1),np.kron(s1,s2),np.kron(s1,s3),np.kron(s2,I),np.kron(s3,I)]
    for i in range(5):
        for j in range(5):
            assert np.allclose(g[i]@g[j]+g[j]@g[i],2*(i==j)*np.eye(4))
    return g

def so5_spinor():
    g=gammas5(); M={}
    for A in range(5):
        for B in range(5):
            M[A,B]=-0.25j*(g[A]@g[B]-g[B]@g[A])
    return M

def sym_power(M4,n):
    # second quantisation on n bosons in 4 modes
    basis=[c for c in itertools.product(range(n+1),repeat=4) if sum(c)==n]
    idx={c:i for i,c in enumerate(basis)}; N=len(basis)
    def op(m):
        R=np.zeros((N,N),complex)
        for c in basis:
            for i in range(4):
                for j in range(4):
                    if m[i,j]==0 or c[j]==0: continue
                    d=list(c); amp=np.sqrt(d[j]); d[j]-=1; amp*=np.sqrt(d[i]+1); d[i]+=1
                    R[idx[tuple(d)],idx[c]]+=m[i,j]*amp
        return R
    return {k:op(v) for k,v in M4.items()},N

def comm(a,b): return a@b-b@a

def herm_basis(N):
    B=[]
    for i in range(N):
        for j in range(i,N):
            E=np.zeros((N,N),complex)
            if i==j: E[i,i]=1
            else: E[i,j]=E[j,i]=1/np.sqrt(2)
            B.append(E)
            if i!=j:
                F=np.zeros((N,N),complex); F[i,j]=-1j/np.sqrt(2); F[j,i]=1j/np.sqrt(2); B.append(F)
    # orthonormal in Tr(AB); project out identity
    B=np.array(B); I=np.eye(N)/np.sqrt(N)
    B=np.array([b-np.trace(b@I)*I for b in B]).reshape(len(B),N*N)
    # orthonormalise real-linearly: work with real vectors of (Re,Im)
    R=np.concatenate([B.real,B.imag],axis=1)
    u,s,vt=np.linalg.svd(R,full_matrices=False)
    keep=s>1e-9
    V=vt[keep]
    out=[ (v[:N*N]+1j*v[N*N:]).reshape(N,N) for v in V]
    return out

def ad(X):
    N=X.shape[0]; I=np.eye(N)
    return np.kron(X,I)-np.kron(I,X.T)   # acts on vec(row-major) of matrices

def run(n,alpha=1.0):
    M4=so5_spinor(); M,N=sym_power(M4,n)
    # index 4 plays the role of c0 ("5")
    X=[alpha*M[a,4] for a in range(4)]
    gam=3*alpha**2
    eom=max(np.abs(sum(comm(X[b],comm(X[b],X[a])) for b in range(4))-gam*X[a]).max() for a in range(4))
    # Casimirs in the adjoint action on End(V)
    adM={k:ad(v) for k,v in M.items()}
    C5=sum(adM[A,B]@adM[A,B] for A in range(5) for B in range(A+1,5))
    C4=sum(adM[a,b]@adM[a,b] for a in range(4) for b in range(a+1,4))
    box=sum(ad(x)@ad(x) for x in X)
    r_box=np.abs(box-alpha**2*(C5-C4)).max()
    # basis of traceless hermitian
    Hb=herm_basis(N); d=len(Hb)
    Bmat=np.array([h.reshape(-1) for h in Hb]).T   # N^2 x d
    def proj(Op):  # real symmetric matrix of Re Tr(h_i^dag Op h_j)
        return np.real(Bmat.conj().T@Op@Bmat)
    # (b) bosonic Hessian on the 4-block by polarisation of the t^2 coefficient
    def S2(A):  # A list of 4 matrices; euclidean contraction on the block
        tot=0
        for mu in range(4):
            for nu in range(4):
                C0=comm(X[mu],X[nu]); C1=comm(X[mu],A[nu])+comm(A[mu],X[nu]); C2=comm(A[mu],A[nu])
                tot+=-0.25*np.trace(C1@C1+2*C0@C2)
        tot+=-0.5*gam*sum(np.trace(a@a) for a in A)
        return np.real(tot)
    def G2(A,sgn):
        g=sum(comm(X[mu],A[mu]) for mu in range(4))
        return np.real(sgn*0.5*np.trace(g@g))
    D=4*d
    Hb_arr=np.array(Hb)
    # C1_{mu nu}(e) for basis element e=(rho,i): A_rho = h_i, others 0
    C1=np.zeros((4,d,4,4,N,N),complex)
    for rho in range(4):
        for i in range(d):
            h=Hb[i]
            for nu in range(4):
                c=comm(X[rho],h)          # [X_rho, h]: appears in C1_{nu rho} with A_rho=h as [X_nu,A_rho]? build directly
            for mu in range(4):
                for nu in range(4):
                    val=np.zeros((N,N),complex)
                    if nu==rho: val+=comm(X[mu],h)
                    if mu==rho: val+=comm(h,X[nu])
                    C1[rho,i,mu,nu]=val
    C1f=C1.reshape(D,16,N*N)
    C1T=np.transpose(C1.reshape(D,16,N,N),(0,1,3,2)).reshape(D,16,N*N)
    H1=np.real(np.einsum('ipk,jpk->ij',C1f,C1T))      # sum_{mu nu} Tr(C1(e_i) C1(e_j))
    # C0 C2 term: Tr(C0_{mu nu}[A_mu,A_nu]); bilinear in (e_i,e_j)
    H2=np.zeros((D,D))
    for mu in range(4):
        for nu in range(4):
            C0=comm(X[mu],X[nu])
            # q contribution 2*Tr(C0 [A_mu,A_nu]) -> bilinear B(a,b)=Tr(C0([a_mu,b_nu]+[b_mu,a_nu]))
            T=np.einsum('xy,iyz,jzx->ij',C0,Hb_arr,Hb_arr)   # Tr(C0 h_i h_j)
            Mx=T-T.T                                          # Tr(C0[h_i,h_j])
            blk=np.real(Mx)
            H2[mu*d:(mu+1)*d,nu*d:(nu+1)*d]+=blk
            H2[nu*d:(nu+1)*d,mu*d:(mu+1)*d]+=blk.T
    # S2 = -1/4 sum Tr(C1^2+2 C0 C2) - gam/2 sum Tr A^2 ; <v,Kv> = 2 S2
    Hs=2*(-0.25*H1-0.25*H2)-gam*np.eye(D)
    # gauge term: g=sum_mu [X_mu,A_mu]
    Gv=np.zeros((D,N*N),complex)
    for mu in range(4):
        for i in range(d):
            Gv[mu*d+i]=comm(X[mu],Hb[i]).reshape(-1)
    GvT=np.transpose(Gv.reshape(D,N,N),(0,2,1)).reshape(D,N*N)
    Gm=np.real(Gv@GvT.T)                                     # Tr(g_i g_j)
    res={}
    for sgn in (+1,-1):
        H=Hs+2*sgn*0.5*Gm
        H=0.5*(H+H.T)
        res[sgn]=np.sort(np.linalg.eigvalsh(H))
    # Casimir prediction for the 4-block: build on vector (x) End
    vecS={}
    for a in range(4):
        for b in range(4):
            S=np.zeros((4,4),complex); S[a,b]=-1j; S[b,a]=1j
            vecS[a,b]=S
    I4=np.eye(4); IE=np.eye(N*N)
    C4tot=sum((np.kron(vecS[a,b],IE)+np.kron(I4,adM[a,b]))@(np.kron(vecS[a,b],IE)+np.kron(I4,adM[a,b])) for a in range(4) for b in range(a+1,4))
    base=np.kron(I4,alpha**2*(C5-C4))
    C4adI=np.kron(I4,C4)
    pred={}
    for s in (+1,-1):
        K=base+s*alpha**2*(C4tot-C4adI-3*np.eye(4*N*N))-gam*np.eye(4*N*N)
        # restrict to traceless: project vector (x) traceless
        P=np.kron(I4,Bmat)
        pred[s]=np.sort(np.linalg.eigvalsh(np.real(P.conj().T@K@P)))
    print(f"n={n} N={N} EOM residual {eom:.1e} box-Casimir residual {r_box:.1e}")
    for sgn in res:
        for s in pred:
            print(f"  gauge-term sign {sgn:+d} vs Casimir sign s={s:+d}: max|diff| = {np.abs(res[sgn]-pred[s]).max():.2e}")
    # transverse
    Kp=np.sort(np.linalg.eigvalsh(proj(alpha**2*(C5-C4)-gam*np.eye(N*N))))
    print("  transverse spectrum min, #neg, #zero:",Kp.min().round(6),int((Kp<-1e-9).sum()),int((abs(Kp)<1e-9).sum()))
    # (c) fermions: 4d Euclidean gammas for the block
    s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]]); s3=np.diag([1.,-1]).astype(complex); I2=np.eye(2)
    g4=[np.kron(s1,s1),np.kron(s1,s2),np.kron(s1,s3),np.kron(s2,I2)]
    chir=g4[0]@g4[1]@g4[2]@g4[3]
    Dop=sum(np.kron(g4[a],ad(X[a])) for a in range(4))
    D2=Dop@Dop
    spS={}
    for a in range(4):
        for b in range(4):
            spS[a,b]=-0.25j*(g4[a]@g4[b]-g4[b]@g4[a])
    C4sp=sum((np.kron(spS[a,b],IE)+np.kron(np.eye(4),adM[a,b]))@(np.kron(spS[a,b],IE)+np.kron(np.eye(4),adM[a,b])) for a in range(4) for b in range(a+1,4))
    Pq=np.kron(np.eye(4),Bmat)
    ev=np.sort(np.linalg.eigvalsh(Pq.conj().T@D2@Pq))
    for s in (+1,-1):
        Kf=np.kron(np.eye(4),alpha**2*(C5-C4))+s*alpha**2*(C4sp-np.kron(np.eye(4),C4)-1.5*np.eye(4*N*N))
        evp=np.sort(np.linalg.eigvalsh(Pq.conj().T@Kf@Pq))
        print(f"  Dirac^2 vs Casimir sign s'={s:+d}: max|diff| = {np.abs(ev-evp).max():.2e}")
    print("  Dirac^2 min eigenvalue:",ev.min().round(8)," #zero:",int((ev<1e-9).sum()))
    # chirality commutes with D^2 ?
    print("  [chirality, D^2] residual:",np.abs(np.kron(chir,IE)@D2-D2@np.kron(chir,IE)).max().round(12))
    return res

import sys
if __name__=='__main__':
  for n in [int(a) for a in sys.argv[1:]] or (1,2):
    run(n)

# (e) full ten-dimensional check of the fermion zero modes: kernel of sum_a Gamma^a ad X_a
#     on a chiral 16 (x) traceless End(V_n), Gamma^a for four of the spatial directions.
def gammas10():
    s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]]); s3=np.diag([1.,-1]).astype(complex); I=np.eye(2)
    G=[]
    for k in range(5):
        for s in (s1,s2):
            m=np.array([[1]],complex)
            for j in range(5):
                m=np.kron(m, s3 if j<k else (s if j==k else I))
            G.append(m)
    return G
def check10(n):
    G=gammas10(); g11=np.eye(32,dtype=complex)
    for g in G: g11=g11@g
    g11=g11*(1j**5)   # (-i)^5... normalise to square 1
    if not np.allclose(g11@g11,np.eye(32)): g11=g11*1j
    assert np.allclose(g11@g11,np.eye(32))
    w,v=np.linalg.eigh(g11); Pp=v[:,w>0]; Pm=v[:,w<0]
    M4=so5_spinor(); M,N=sym_power(M4,n); X=[M[a,4] for a in range(4)]
    Hb=herm_basis(N); Bm=np.array([h.reshape(-1) for h in Hb]).T
    Dfull=sum(np.kron(Pm.conj().T@G[a]@Pp, Bm.conj().T@ad(X[a])@Bm) for a in range(4))  # 16 -> 16'
    sv=np.linalg.svd(Dfull,compute_uv=False)
    print(f"  10D check n={n}: dim 16x(N^2-1)={Dfull.shape[1]}, kernel dim = {int((sv<1e-9).sum())}")
if __name__=='__main__':
  for n in [int(a) for a in sys.argv[1:]] or (1,2):
    check10(n)
