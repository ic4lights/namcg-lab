import itertools
from quantum_compact_hessian import *
from collections import Counter
def eps5():
    out={}
    for p in itertools.permutations(range(5)):
        out[p]=np.linalg.det(np.eye(5)[list(p)])
    return out
EPS=eps5()
def quintic_E(X):
    E=[np.zeros_like(X[0]) for _ in range(5)]
    for p,sg in EPS.items():
        A,B,C,D,Ee=p
        E[A]=E[A]+sg*(X[B]@X[C]@X[D]@X[Ee])
    return E
def hessian_quintic(X):
    dd=X[0].shape[0]; I=np.eye(dd); n2=dd*dd
    H=np.zeros((5*n2,5*n2),complex)
    # dE^A = sum eps_{ABCDE}( a^B X^C X^D X^E + X^B a^C X^D X^E + X^B X^C a^D X^E + X^B X^C X^D a^E )
    # superoperators: L(P)=kron(P,I) acts a->P a ; R(Q)=kron(I,Q^T) acts a->a Q  (row-major vec)
    for p,sg in EPS.items():
        A,B,C,D,Ee=p
        # position 1: a^B at slot, left =1, right = X^C X^D X^E
        H[A*n2:(A+1)*n2,B*n2:(B+1)*n2]+=sg*np.kron(I,(X[C]@X[D]@X[Ee]).T)
        H[A*n2:(A+1)*n2,C*n2:(C+1)*n2]+=sg*np.kron(X[B],(X[D]@X[Ee]).T)
        H[A*n2:(A+1)*n2,D*n2:(D+1)*n2]+=sg*np.kron(X[B]@X[C],X[Ee].T)
        H[A*n2:(A+1)*n2,Ee*n2:(Ee+1)*n2]+=sg*np.kron(X[B]@X[C]@X[D],I)
    return H
N=int(sys.argv[1]) if len(sys.argv)>1 else 2
mats=[Sig[A,5] for A in range(5)]
X,dd=sym_power_ops(mats,N)
E=quintic_E(X)
kap=np.vdot(X[0],E[0])/np.vdot(X[0],X[0])
print("eps X^4 = kappa X:",kap, np.allclose(E[0],kap*X[0],atol=1e-8))
# YM eom: [X^B,[X^B,X^A]] = 4 X^A (lam).  Total E^A = YMeom + c*E5 =0 -> c = -4/kap
lam=4.0
c=-lam/kap.real
H0=hessian(X,0.0)
Hq=hessian_quintic(X)
H=H0+c*Hq
print("herm",np.max(np.abs(H-H.conj().T)))
ev=np.linalg.eigvalsh((H+H.conj().T)/2)
cn=Counter(np.round(ev,3))
print("c=",c,"d=",dd)
print(sorted(cn.items()))
