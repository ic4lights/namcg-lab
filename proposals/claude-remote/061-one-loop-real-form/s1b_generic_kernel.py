"""s1b: control. Kernel of sum_a Gamma^a ad X_a on a chiral 16 (x) su(N) for random Hermitian
X_1..X_4 (N=4, 10, and the dimensions of the reps tested in s1), and for the compact member
in a reducible representation V_1 (+) V_1 and V_1 (+) V_0, and for a rotated/rescaled frame."""
import numpy as np, sys
from s1_explicit_hessian import *
rng=np.random.default_rng(1)
def kernel_dim(X):
    G=gammas10(); g11=np.eye(32,dtype=complex)
    for g in G: g11=g11@g
    g11=g11*(1j**5)
    if not np.allclose(g11@g11,np.eye(32)): g11=g11*1j
    w,v=np.linalg.eigh(g11); Pp=v[:,w>0]; Pm=v[:,w<0]
    N=X[0].shape[0]; Hb=herm_basis(N); Bm=np.array([h.reshape(-1) for h in Hb]).T
    D=sum(np.kron(Pm.conj().T@G[a]@Pp, Bm.conj().T@ad(X[a])@Bm) for a in range(4))
    sv=np.linalg.svd(D,compute_uv=False); return int((sv<1e-9*sv.max()).sum()), D.shape[1]
for N in (4,6,10):
    X=[]
    for a in range(4):
        Z=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)); X.append((Z+Z.conj().T)/2)
    print(f"random Hermitian X_1..X_4, N={N}: kernel {kernel_dim(X)}")
M4=so5_spinor(); M,N=sym_power(M4,1)
Xc=[M[a,4] for a in range(4)]
blk=lambda A,B: np.block([[A,np.zeros((A.shape[0],B.shape[1]))],[np.zeros((B.shape[0],A.shape[1])),B]])
print("compact member V_1+V_1 (N=8):",kernel_dim([blk(x,x) for x in Xc]))
print("compact member V_1+V_0 (N=5):",kernel_dim([blk(x,np.zeros((1,1))) for x in Xc]))
R=np.linalg.qr(rng.normal(size=(4,4)))[0]
print("compact member V_1, rotated and scaled frame 2.7*R:",kernel_dim([2.7*sum(R[a,b]*Xc[b] for b in range(4)) for a in range(4)]))
