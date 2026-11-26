# Independent gatekeeper check: Q on Landau sector of wider Heisenberg family, own implementation.
import numpy as np, itertools
eta=np.diag([-1.,1,1,1]); ei=eta
def setup(kap,chi,ze,x):
    M=np.zeros((4,4))
    def put(c,d,v): M[c,d]+=v; M[d,c]-=v
    put(0,2,chi); put(0,1,ze); put(1,2,ze); put(0,3,x); put(2,3,-x)
    k=np.array([1.,0,1,0])
    W=np.einsum('a,cd->acd',k,M)
    Om=np.einsum('acd,db->abc',W,eta)   # Om_ab^c = w_a^{cd} eta_db
    C=np.zeros((4,4,4)); C[3,1,2]=kap; C[1,3,2]=-kap
    T=-C-Om+np.transpose(Om,(1,0,2))
    return Om,T,C
def Qmat(kap,chi,ze,x,p,q0,N):
    Om,T,C=setup(kap,chi,ze,x)
    a=np.diag(np.sqrt(np.arange(1,N)),1); ad=a.T; I=np.eye(N); s=np.sqrt(kap*p/2)
    E=[1j*q0*I, s*(a-ad), 1j*p*I, -1j*s*(a+ad)]
    # A_b in C^4 x C^N ; build F_ab as operator, then Q
    Z=np.zeros((N,N),complex)
    def blk(b):  # projector-like embedding: A -> A_b
        P=np.zeros((N,4*N),complex); P[:,b*N:(b+1)*N]=I; return P
    Pb=[blk(b) for b in range(4)]
    nA=[[E[aa]@Pb[b]+sum(Om[aa,b,z]*Pb[z] for z in range(4)) for b in range(4)] for aa in range(4)]
    F=[[nA[aa][b]-nA[b][aa]+sum(T[aa,b,c]*Pb[c] for c in range(4)) for b in range(4)] for aa in range(4)]
    Q=[]
    for b in range(4):
        tot=np.zeros((N,4*N),complex)
        for xx in range(4):
            nF=E[xx]@F[xx][b]+sum(Om[xx,xx,z]*F[z][b]+Om[xx,b,z]*F[xx][z] for z in range(4))
            tot+=ei[xx,xx]*nF
        for aa in range(4):
            for c in range(4):
                tot-=T[aa,b,c]*ei[aa,aa]*F[aa][c]
        Q.append(tot)
    return np.vstack(Q)
# Check Q - Q0 + chi k^a F_ab = 0 as matrices
kap,chi,ze,x,p,q0,N=1.3,0.7,0.4,-0.9,0.45,0.3+0.2j,12
Qw=Qmat(kap,chi,ze,x,p,q0,N); Q0=Qmat(kap,0,0,0,p,q0,N)
# k^a F_ab with k^a=(-1,0,1,0): build F at w=0 (F has no w)
print('zeta,x independence', np.abs(Qmat(kap,chi,ze,x,p,q0,N)-Qmat(kap,chi,0,0,p,q0,N)).max())
# roots of Q: column cut device, columns levels<=L
def roots(kap,chi,p,N=24,L=8):
    cols=[b*N+n for b in range(4) for n in range(L+1)]
    f=lambda z: Qmat(kap,chi,0.3,0.2,p,z,N)[:,cols]
    A0=f(0); A1=(f(1)-f(-1))/2; A2=(f(1)+f(-1))/2-A0
    # generalized: rank drop of A0+zA1+z^2A2 ; use random left compression to square, linearize
    r=np.linalg.matrix_rank(f(0.37+0.11j))
    rng=np.random.default_rng(1); X=rng.normal(size=(r,A0.shape[0])); Y=rng.normal(size=(A0.shape[1],r))
    a0,a1,a2=X@A0@Y,X@A1@Y,X@A2@Y
    n=r; Lb=np.block([[np.zeros((n,n)),np.eye(n)],[-a0,-a1]]); Mb=np.block([[np.eye(n),np.zeros((n,n))],[np.zeros((n,n)),a2]])
    import scipy.linalg as sl
    ev=sl.eigvals(Lb,Mb); ev=ev[np.isfinite(ev)&(np.abs(ev)<50)]
    good=[]
    for z in ev:
        sv=np.linalg.svd(f(z),compute_uv=False)
        if sv[r-1]/sv[0]<1e-8: good.append(z)
    return good
for chi_ in (0.6,-0.4):
    p=0.35;kap=1.2
    out={}
    for z in roots(kap,chi_,p):
        v=z**2-p**2+1j*chi_*(z-p)
        l=v/(kap*p); out[round(l.real,6)+1j*round(l.imag,6)]=out.get(round(l.real,6)+1j*round(l.imag,6),0)+1
    print('chi',chi_,sorted(out.items(),key=lambda t:t[0].real))
# growth: l>=1 small-p limit of |Im q0|
for c,ch,kap in [(1,0.5,1.0),(3,0.5,1.0)]:
    g=c*ch/2
    for pp in (1e-6,1e-3,1e3):
        Z=(pp+1j*g)**2+kap*pp*1; r=np.sqrt(Z); print('c',c,'p',pp,'Im q0',(-1j*g+r).imag,(-1j*g-r).imag)
