import sympy as sp
import sympy
# general U(2) with real params preserves X up to norm
a1,a2,a3,a4=sp.symbols('a1 a2 a3 a4',real=True)
U=sp.Matrix([[a1+sp.I*a2,a3+sp.I*a4],[-(a3-sp.I*a4),a1-sp.I*a2]])
nz=a1**2+a2**2+a3**2+a4**2
Pg=sp.Matrix([[sp.Symbol('q%d_%d'%(r,c),complex=True) for c in range(2)] for r in range(2)])
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
