"""
Quartic torsion invariant that survives the weighted traces at four-derivative order (a_2 level).
Fields (017): vector a^mu (4 comps, weight +1), N_s inert scalars, ghosts (-2, no beta), n_D Dirac (4 comps, weight -1 each).
beta_sigma = B_sigma = spinor/vector lift of the rotation generator N^sigma_{ab} (antisymmetric in ab, sigma = 1..4).
Checks: (i) tr beta.beta: vector -X, Dirac -X/2 -> index weight 1 - n_D/2;
        (ii) any trace quadratic in algebra elements (tr [B_s,B_t]^2, tr dB dB) has the same weight 1-n_D/2 ('index');
        (iii) tr (B_s B_s)^2 weighted: W4 = tr_V (B.B)^2 - n_D tr_D (B.B)^2 at n_D=2: >=0, zero iff N^sigma self-dual (or anti-self-dual) for all sigma.
"""
import numpy as np
rng=np.random.default_rng(7)
s0=np.eye(2); sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1])
g=[np.kron(sx,s0),np.kron(sy,s0),np.kron(sz,sx),np.kron(sz,sy)]
for a in range(4):
    for b in range(4): assert np.allclose(g[a]@g[b]+g[b]@g[a],2*(a==b)*np.eye(4))
def S(M): return 0.25*sum(M[a,b]*g[a]@g[b] for a in range(4) for b in range(4))
def eps4():
    import itertools
    e=np.zeros((4,4,4,4))
    for p in itertools.permutations(range(4)):
        sgn=np.linalg.det(np.eye(4)[list(p)]); e[p]=sgn
    return e
E4=eps4()
def dual(M): return 0.5*np.einsum('abcd,cd->ab',E4,M)
def rand_N(kind='generic'):
    out=[]
    for s in range(4):
        A=rng.normal(size=(4,4)); A=A-A.T
        if kind=='SD': A=(A+dual(A))/2
        if kind=='ASD': A=(A-dual(A))/2
        out.append(A)
    return out
def invs(N,nD=2):
    BV=N; BD=[S(A) for A in N]
    cV=sum(b@b for b in BV); cD=sum(b@b for b in BD)
    tr2V=np.trace(cV).real; tr2D=np.trace(cD).real
    W4=np.trace(cV@cV).real-nD*np.trace(cD@cD).real
    com=lambda B:sum(np.trace((B[s]@B[t]-B[t]@B[s])@(B[s]@B[t]-B[t]@B[s])) for s in range(4) for t in range(4))
    q2=com(BV).real-nD*com(BD).real
    cub=lambda B:sum(np.trace(B[s]@(B[t]@B[u]-B[u]@B[t])) for s in range(4) for t in range(4) for u in range(4))
    q3=cub(BV)-nD*cub(BD)
    return tr2V,tr2D,W4,q2,q3
for kind in ('generic','generic','SD','ASD'):
    N=rand_N(kind); tV,tD,W4,q2,q3=invs(N)
    print('%-8s tr_V(B.B)=%.5f  tr_D(B.B)=%.5f  ratio D/V=%.6f | weighted tr[B_s,B_t]^2 (nD=2) = %.2e | weighted cubic = %.2e | W4 (nD=2) = %.6f' % (kind,tV,tD,tD/tV,q2,abs(q3),W4))
vals=[invs(rand_N())[2] for _ in range(2000)]
print('min W4 over 2000 generic draws: %.3e (>=0 expected)' % min(vals))
# closed form check in SU(2)xSU(2) variables: W4 = (1/2)|l|^2|r|^2 + c*|K|^2 ; fit
rows=[];rhs=[]
for _ in range(200):
    N=rand_N()
    # l_s^a, r_s^a : SD/ASD components of N_s (up to normalisation): use norms
    SDc=[(A+dual(A))/2 for A in N]; ASc=[(A-dual(A))/2 for A in N]
    L2=sum(np.sum(x*x) for x in SDc); R2=sum(np.sum(x*x) for x in ASc)
    # K_{ab} = sum_s l_s^a r_s^b with orthonormal bases of SD / ASD 2-forms
    basisSD=[];basisAS=[]
    for (i,j) in [(0,1),(0,2),(0,3)]:
        e=np.zeros((4,4)); e[i,j]=1; e[j,i]=-1
        basisSD.append((e+dual(e))/2); basisAS.append((e-dual(e))/2)
    gs=lambda X,Bs: np.array([np.sum(X*b) for b in Bs])
    K=sum(np.outer(gs(SDc[s],basisSD),gs(ASc[s],basisAS)) for s in range(4))
    rows.append([L2*R2, np.sum(K*K)]); rhs.append(invs(N)[2])
rows=np.array(rows); rhs=np.array(rhs)
coef,res,rk,sv=np.linalg.lstsq(rows,rhs,rcond=None)
print('W4 = c1 |l|^2|r|^2 + c2 |K|^2 fit: c1=%.6f c2=%.6f  max residual %.2e' % (coef[0],coef[1],np.max(np.abs(rows@coef-rhs))))
