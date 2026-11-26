import numpy as np, itertools
from sympy.combinatorics import Permutation
rng=np.random.default_rng(7); N=5
eta=np.diag([-1.,1,1,1])
eps=np.zeros((4,)*4)
for p in itertools.permutations(range(4)): eps[p]=Permutation(list(p)).signature()
def H():
    a=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)); return (a+a.conj().T)/2
v=rng.normal(size=4)
C=1j*np.einsum('abcs,s->abc',eps,v)  # C_{mu nu lam}, g=1
def com(a,b): return a@b-b@a
def S(X):  # X upper index
    Xl=[sum(eta[m,n]*X[n] for n in range(4)) for m in range(4)]
    s4=-0.25*sum(np.trace(com(X[m],X[n])@com(Xl[m],Xl[n])) for m in range(4) for n in range(4))
    s3=sum(C[m,n,l]*np.trace(com(X[m],X[n])@X[l]) for m in range(4) for n in range(4) for l in range(4))/6
    return s4+s3
X=[H() for _ in range(4)]; dX=[H() for _ in range(4)]
h=1e-6
fd=(S([X[i]+h*dX[i] for i in range(4)])-S([X[i]-h*dX[i] for i in range(4)]))/(2*h)
Xl=[sum(eta[m,n]*X[n] for n in range(4)) for m in range(4)]
G=[sum(com(X[n],com(Xl[n],Xl[l])) for n in range(4)) + 0.5j*sum(eps[l,m,n,s]*v[s]*com(X[m],X[n]) for m in range(4) for n in range(4) for s in range(4)) for l in range(4)]
an=sum(np.trace(dX[l]@G[l]) for l in range(4))
print('Im S',abs(S(X).imag),'fd',fd,'analytic',an)
# lemma numeric on a covariance: random Lambda, D -> Lambda D; check E[Lam D; v] = Lam E[D; Lam^-1 v]
def E(D,v):
    Du=[sum(eta[a,b]*D[b] for b in range(4)) for a in range(4)]
    return [sum(com(Du[a],com(D[a],D[b])) for a in range(4)) + 0.5*sum(eps[b,c,d,f]*v[f]*com(Du[c],Du[d]) for c in range(4) for d in range(4) for f in range(4)) for b in range(4)]
from scipy.linalg import expm
gens=[]
for c in range(4):
  for d in range(c+1,4):
    Lg=np.zeros((4,4)); Lg[c,d]=1; Lg[d,c]=-1; gens.append(Lg@eta)  # generator acting on upper index
A=sum(rng.normal()*g for g in gens); L=expm(A)   # L^a_b upper-lower
print('Lorentz check', np.abs(L.T@eta@L-eta).max(), np.linalg.det(L))
D=[1j*H() for _ in range(4)]  # D_a lower
Lin=np.linalg.inv(L)
Ll=eta@L@eta   # Lambda_a^b = eta_ac L^c_d eta^db
DL=[sum(Ll[a,b]*D[b] for b in range(4)) for a in range(4)]
lhs=E(DL,v); rhs0=E(D,Lin@v); rhs=[sum(Ll[b,c]*rhs0[c] for c in range(4)) for b in range(4)]
print('covariance residual', max(np.abs(lhs[b]-rhs[b]).max() for b in range(4)))
