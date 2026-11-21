import sympy as sp
th,ph,ps=sp.symbols('theta phi psi',real=True)
X=(th,ph,ps)
def app(V,f): return sum(V[i]*sp.diff(f,X[i]) for i in range(3))
def br(A,B): return [sp.simplify(app(A,B[i])-app(B,A[i])) for i in range(3)]
c,s=sp.cos(ps),sp.sin(ps)
e1=[1,0,0]; e2=[0,1/sp.sin(th),sp.cot(th)]  # e_a - omega(e_a) xi, omega(e2)=-cot
D1=[c*e1[i]-s*e2[i] for i in range(3)]; D2=[s*e1[i]+c*e2[i] for i in range(3)]
xi=[0,0,1]
print('[xi,D1]+D2',[sp.simplify(a+b) for a,b in zip(br(xi,D1),D2)])
print('[xi,D2]-D1',[sp.simplify(a-b) for a,b in zip(br(xi,D2),D1)])
print('[D1,D2]+xi',[sp.simplify(a+b) for a,b in zip(br(D1,D2),xi)])
# divergence wrt sin th
for D in (D1,D2): print('div',sp.simplify(sum(sp.diff(sp.sin(th)*D[i],X[i]) for i in range(3))/sp.sin(th)))
rho=[[0,-sp.sin(ph),-sp.cot(th)*sp.cos(ph)],[0,sp.cos(ph),-sp.cot(th)*sp.sin(ph)],[0,0,1]]
rho=[[r[1],r[2],0] for r in rho]
cc=[-sp.cos(ph)/sp.sin(th),-sp.sin(ph)/sp.sin(th),0]
rt=[[rho[i][0],rho[i][1],cc[i]] for i in range(3)]
for i in range(3):
  print('rho',i,br(rt[i],D1),br(rt[i],D2))
x=[sp.sin(th)*sp.cos(ph),sp.sin(th)*sp.sin(ph),sp.cos(th)]
print('sum x rho~',[sp.simplify(sum(x[i]*rt[i][k] for i in range(3))) for k in range(3)])
f=sp.Function('f')(th,ph,ps)
lhs=sum(app(rt[i],app(rt[i],f)) for i in range(3))
rhs=app(D1,app(D1,f))+app(D2,app(D2,f))+sp.diff(f,ps,2)
print('casimir',sp.simplify(sp.expand(lhs-rhs)))
# check rho_i are eps_ijk x_j d_k : rho_i(x_m)=eps_ijm x_j
for i in range(3):
  print([sp.simplify(app(rt[i],x[m])-sum(sp.LeviCivita(i,j,m)*x[j] for j in range(3))) for m in range(3)])
# local rotation with lambda(th,ph)
lam=sp.Function('l')(th,ph)
LS=[0,0,lam]
print('locrot1',[sp.simplify(a-(-lam*b-app(D1,lam)*cxi)) for a,b,cxi in zip(br(LS,D1),D2,xi)])
print('locrot2',[sp.simplify(a-(lam*b-app(D2,lam)*cxi)) for a,b,cxi in zip(br(LS,D2),D1,xi)])
