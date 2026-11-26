import sympy as sp
# W1 identities and Hadamard witness (n=2), fast
p=sp.symbols('p1:17',complex=True)
P=sp.Matrix([[p[0],p[1]],[p[2],p[3]]]); Pd=P.adjoint()
C=P*Pd-Pd*P
W1=sp.expand((C*C).trace())          # Tr C^2 (C Hermitian)
W1f=sp.expand((C.adjoint()*C).trace())
print('W1 = Tr(C^dag C) = Tr(C^2):', sp.simplify(W1-W1f)==0)
w2=sp.expand((P*Pd*P*Pd).trace()); w3=sp.expand((P*P*Pd*Pd).trace())
print('W1 = 2Tr(P Pd P Pd) - 2Tr(P^2 Pd^2):', sp.simplify(W1-(2*w2-2*w3))==0)
# shift invariance of W1 under Phi->Phi+sI: C invariant
s=sp.Symbol('s',complex=True)
Cs=(P+s*sp.eye(2))*(Pd+sp.conjugate(s)*sp.eye(2))-(Pd+sp.conjugate(s)*sp.eye(2))*(P+s*sp.eye(2))
Cs=sp.simplify(Cs.subs(sp.conjugate(s),sp.Symbol('sb',complex=True)))
print('C shift-invariant:', sp.simplify(Cs-C)==sp.zeros(2))
# Hadamard witness
p1,p2=sp.symbols('p1 p2',positive=True)
D=sp.diag(p1,p2); H=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
HD=H*D
W1H=sp.simplify((sp.simplify(HD*HD.adjoint()-HD.adjoint()*HD)**2).trace())
W1D=sp.simplify((sp.simplify(D*D.adjoint()-D.adjoint()*D)**2).trace())
print('W1(D)=0:', W1D==0, '| W1(HD)=', sp.expand(W1H))
X1=sp.simplify((HD.adjoint()*HD)-(D.adjoint()*D)); print('X preserved by H:', X1==sp.zeros(2))
# numeric: p=(2,1): expect W1 = 9? per proposal T7b
print('W1(HD) at p=2,1:', W1H.subs({p1:2,p2:1}))
# general U(2) with real params preserves X up to norm
a1,a2,a3,a4=sp.symbols('a1 a2 a3 a4',real=True)
U=sp.Matrix([[a1+sp.I*a2,a3+sp.I*a4],[-(a3-sp.I*a4),a1-sp.I*a2]])
nz=a1**2+a2**2+a3**2+a4**2
Pg=sp.Matrix([[sp.Symbol('q%d'%i,complex=True) for _ in range(2)] for _ in range(2)])
dU=sp.expand((U*Pg).adjoint()*(U*Pg)-nz*(Pg.adjoint()*Pg))
print('general U(2): (UP)^dag(UP)=norm P^dagP:', dU==sp.zeros(2))
dU2=sp.expand((U*Pg).adjoint()*(U*Pg)-(Pg.adjoint()*Pg))
print('unscaled U does NOT preserve X:', dU2!=sp.zeros(2))
# K-type: manuscript K^{mu nu}=eta_{ab}Th^{am}Th^{bn}; solve K=c*eta
eta=sp.diag(-1,1,1,1)
e=sp.symbols('E1:4',real=True); b=sp.symbols('B1:4',real=True)
Th=sp.zeros(4)
Th[0,1]=e[0];Th[1,0]=-e[0];Th[0,2]=e[1];Th[2,0]=-e[1];Th[0,3]=e[2];Th[3,0]=-e[2]
Th[1,2]=b[2];Th[2,1]=-b[2];Th[1,3]=b[1];Th[3,1]=-b[1];Th[2,3]=b[0];Th[3,2]=-b[0]
K=sp.zeros(4)
for mu in range(4):
    for nu in range(4):
        K[mu,nu]=sp.expand(sum(eta[al,al]*Th[al,mu]*Th[al,nu] for al in range(4) if eta[al,al]!=0)* (1 if True else 1) if False else sum(eta[al,al]*Th[al,mu]*Th[al,nu] for al in range(4)))
c=sp.Symbol('c',real=True)
sol=sp.solve(list(K-c*eta).args if hasattr(K-c*eta,'args') else [(K-c*eta)[i,j] for i in range(4) for j in range(i,4)]+[e[0]**2+b[0]**2-1],[c]+list(e)+list(b),dict=True)
print('K=c g solutions (with normalization e.b sphere to kill trivial 0):', sol)
# kinetic tensor of quadratic lift: C^{ac} = g^{mu nu} Th_{mu}{}^{a} Th_{nu}{}^{b} vs K
Thlo=eta*Th*eta  # Theta_{mu nu}
g=eta
Ct=sp.zeros(4)
for aa in range(4):
    for bb in range(4):
        Ct[aa,bb]=sp.expand(sum(g[mu,nu]*sum(Thlo[mu,r]*g[r,aa] for r in range(4))*sum(Thlo[nu,q]*g[q,bb] for q in range(4)) for mu in range(4) for nu in range(4)))
r2=sp.simplify(Ct+K); r1=sp.simplify(Ct-K)
print('Ckin == -K:', r2==sp.zeros(4), '| Ckin == +K:', r1==sp.zeros(4))
# purely spatial Theta: e=0 -> K^{0 mu}=0
Ksp=K.subs({e[0]:0,e[1]:0,e[2]:0})
print('spatial Theta: K^{0mu}=0:', all(Ksp[0,i]==0 for i in range(4)), 'det K:', sp.factor(sp.simplify(Ksp.det())))
