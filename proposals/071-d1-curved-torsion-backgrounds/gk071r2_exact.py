"""Gatekeeper r2 independent EXACT operator check of the wider Heisenberg family.
Literal L1519: D_a = u_a^b(E_b - u_f^g om_b^c_g d/du_f^c) + t_a, om = -w (snippet A), t_a = (1/2) divergence.
Symbolic kappa,a,zeta,x and symbolic y; exact rational Lorentz u (Cayley).  All residuals must be identically 0."""
import itertools, sympy as sp
eta=sp.diag(-1,1,1,1)
y=sp.symbols('y0:4'); U=sp.Matrix(4,4,lambda i,j: sp.Symbol('u%d%d'%(i,j))); coords=list(y)+list(U)
kap,a,z,x=sp.symbols('kappa a zeta x',real=True)
def gen(d):
    M=sp.zeros(4,4)
    for (c,e),v in d.items(): M[c,e]=v; M[e,c]=-v
    return M
B=gen({(0,2):1}); N=gen({(0,1):1,(1,2):1}); Np=gen({(0,3):1,(2,3):-1}); k=[1,0,1,0]
M=a*B+z*N+x*Np
class VF:
    def __init__(s,c,f=0): s.c=[sp.sympify(t) for t in c]; s.f=sp.sympify(f)
    def act(s,g): return sp.expand(sum(s.c[i]*sp.diff(g,coords[i]) for i in range(20)))
def comm(A,Bv): return VF([A.act(Bv.c[i])-Bv.act(A.c[i]) for i in range(20)], A.act(Bv.f)-Bv.act(A.f))
def lin(ts): return VF([sp.expand(sum(c*t.c[i] for c,t in ts)) for i in range(20)], sp.expand(sum(c*t.f for c,t in ts)))
Ey=[[1,0,0,0],[0,1,kap*y[3]/2,0],[0,0,1,0],[0,0,-kap*y[1]/2,1]]
om=[-(k[b]*M) for b in range(4)]
D=[]
for A_ in range(4):
    comp=[0]*20; dv=0
    for b in range(4):
        omg=om[b]*eta
        Yb=list(Ey[b])+[-sum(U[f,g]*omg[c,g] for g in range(4)) for f in range(4) for c in range(4)]
        for i in range(20): comp[i]+=U[A_,b]*Yb[i]
        dv+=VF(Yb).act(U[A_,b])+U[A_,b]*sum(sp.diff(Ey[b][i],y[i]) for i in range(4))
    D.append(VF(comp, sp.expand(dv/2)))
S={}
for c,d in itertools.combinations(range(4),2):
    comp=[0]*20
    for A_ in range(4):
        for b in range(4): comp[4+4*A_+b]=eta[A_,d]*U[c,b]-eta[A_,c]*U[d,b]
    S[(c,d)]=VF(comp)
# exact rational Lorentz u (Cayley)
Aa=sp.Matrix([[0,sp.Rational(1,3),sp.Rational(-1,5),sp.Rational(2,7)],[0,0,sp.Rational(1,4),sp.Rational(-1,6)],[0,0,0,sp.Rational(3,8)],[0,0,0,0]]); Aa=Aa-Aa.T
X=eta*Aa; L=(sp.eye(4)-X).inv()*(sp.eye(4)+X)
assert sp.simplify(L.T*eta*L-eta)==sp.zeros(4,4)
subU={U[i,j]:L[i,j] for i in range(4) for j in range(4)}
sub1={U[i,j]:(1 if i==j else 0) for i in range(4) for j in range(4)}
def ev(V,sub): return [sp.simplify(t.subs(sub)) for t in V.c]+[sp.simplify(V.f.subs(sub))]
# first relation (exact, at Cayley u, symbolic y)
r1=set()
for (c,d),Sv in S.items():
    for A_ in range(4):
        lhs=comm(Sv,D[A_]); rhs=lin([(eta[A_,d],D[c]),(-eta[A_,c],D[d])])
        r1|=set(sp.simplify(p-q) for p,q in zip(ev(lhs,subU),ev(rhs,subU)))
print('first relation residual set:',r1)
F={(p,q):comm(D[p],D[q]) for p in range(4) for q in range(4) if p!=q}
res=set()
for b in range(4):
    tot=lin([(eta[A_,A_],comm(D[A_],F[(A_,b)])) for A_ in range(4) if A_!=b])
    res|=set(ev(tot,subU))
print('matrix equation [D^a,[D_a,D_b]] at Cayley u, all 21 components, symbolic y,kappa,a,zeta,x:',res)
# read-off at u=1: [D_a,D_b] = -T_ab^c D_c + 1/2 R_ab^{cd} S_cd + F_ab ; solve exactly
cs=sp.symbols('c0:10'); keys=list(S.keys())
Tt={}; R={}; FF={}
for p in range(4):
    for q in range(p+1,4):
        V=comm(D[p],D[q]); comb=lin([(-cs[i],D[i]) for i in range(4)]+[(cs[4+j],S[keys[j]]) for j in range(6)])
        eqs=[sp.expand((V.c[i]-comb.c[i]).subs(sub1)) for i in range(20)]
        sol=sp.solve(eqs,cs,dict=True); assert len(sol)==1; sol=sol[0]
        Tt[(p,q)]=[sp.simplify(sol[cs[i]]) for i in range(4)]
        R[(p,q)]={keys[j]:sp.simplify(sol[cs[4+j]]) for j in range(6)}   # coefficient of S_cd (c<d) = R_pq^{cd}
        # multiplication part: V.f - (-T^c t_c)  => F = V.f + T_pq^c t_c
        tc=[D[i].f.subs(sub1) for i in range(4)]
        FF[(p,q)]=sp.simplify(V.f.subs(sub1)+sum(Tt[(p,q)][i]*tc[i] for i in range(4)))
print('t_a at u=1:',[sp.simplify(D[i].f.subs(sub1)) for i in range(4)])
print('nonzero F pairs:',{k_:v for k_,v in FF.items() if v!=0})
print('nonzero R pairs:',{k_:{kk:vv for kk,vv in v.items() if vv!=0} for k_,v in R.items() if any(vv!=0 for vv in v.values())})
T=[[[0]*4 for _ in range(4)] for _ in range(4)]
for (p,q),v in Tt.items():
    for c in range(4): T[p][q][c]=v[c]; T[q][p][c]=-v[c]
print('trace T_ac^c:',[sp.simplify(sum(T[p][c][c] for c in range(4))) for p in range(4)])
T2=sp.simplify(sum(T[p][q][c]*T[p][q][c]*eta[p,p]*eta[q,q]*eta[c,c] for p in range(4) for q in range(4) for c in range(4)))
print('T_abc T^abc:',T2)
Rf=lambda p,q,c,d: (0 if p==q or c==d else (R[(p,q)][(c,d)] if p<q and c<d else (-Rf(q,p,c,d) if p>q else -Rf(p,q,d,c))))
R2=sp.simplify(sum(Rf(p,q,c,d)**2*eta[p,p]*eta[q,q]*eta[c,c]*eta[d,d] for p in range(4) for q in range(4) for c in range(4) for d in range(4)))
sc=sp.simplify(sum(Rf(p,q,p,q) for p in range(4) for q in range(4)))
print('R_abcd R^abcd:',R2,' ; R_ab^{ab}:',sc)
