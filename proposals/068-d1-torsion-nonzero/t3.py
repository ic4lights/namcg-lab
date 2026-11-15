import numpy as np, itertools
from core import *
def forms(c,w,dirs=(0,1,2,3)):
    M0,M1,M2=M_coeffs(c,w,dirs)
    n=NF; I=np.eye(n)
    rows=[]
    # vec(G) row-major: (G X)_{ij}=sum_k G_ik X_kj ; (X^T G)_{ij}=sum_k X_ki G_kj
    def L(X): return np.kron(I,X.T)      # G -> G X
    def Rr(X): return np.kron(X.T,I)     # G -> X^T G
    rows.append(L(M0)-Rr(M0))
    for m in dirs: rows.append(L(M1[m])+Rr(M1[m]))
    for k in M2: rows.append(L(M2[k])-Rr(M2[k]))
    A=np.vstack(rows)
    AtA=A.T@A
    ev,V=np.linalg.eigh(AtA)
    k=int((ev<1e-9*ev[-1]).sum())
    return V[:,:k].T.reshape(k,n,n),ev[:k+3]
for name,bg in [('flat',flat()),('null g2',null_rotation_g2())]:
    Gs,ev=forms(*bg)
    k=len(Gs)
    sym=[(G+G.T)/2 for G in Gs]; asym=[(G-G.T)/2 for G in Gs]
    rs=np.linalg.matrix_rank(np.array(sym).reshape(k,-1),tol=1e-7); ra=np.linalg.matrix_rank(np.array(asym).reshape(k,-1),tol=1e-7)
    hh=max(np.abs(G[:16,:16]).max() for G in Gs); hw=max(max(np.abs(G[:16,16:]).max(),np.abs(G[16:,:16]).max()) for G in Gs)
    # maximal rank of a generic combination
    g=np.random.default_rng(0); Gc=sum(g.normal()*G for G in Gs)
    print(name,'dim',k,'sym',rs,'antisym',ra,'next eigenvalues',ev[-3:],'max |G_hh|',hh,'max |G_hw|',hw,'rank generic G',np.linalg.matrix_rank(Gc,tol=1e-7))
    np.save('forms_%s.npy'%name.replace(' ','_'),Gs)
