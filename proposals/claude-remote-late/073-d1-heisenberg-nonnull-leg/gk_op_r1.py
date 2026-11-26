# Gatekeeper independent operator-level check (073 r1). Literal L1519 fields:
# D_a = u_a^b E_b^mu(d_mu - u_f^g om_b^c_g d/du_f^c) + t_a, om_b^{cd} = -w_b^{cd}, t_a = 1/2 div (flat d^4y d^16u, = Haar-compatible).
import sympy as sp, itertools, sys, time
t0=time.time()
eta=sp.diag(-1,1,1,1); r4=range(4)
y=sp.symbols('y0:4'); U=sp.Matrix(4,4,lambda i,j:sp.Symbol('u%d%d'%(i,j))); X=list(y)+list(U)
kap=sp.Symbol('kappa',positive=True)
def act(c,g): return sp.expand(sum(c[i]*sp.diff(g,X[i]) for i in range(20) if c[i]!=0))
def comm(A,B):
    return ([act(A[0],B[0][i])-act(B[0],A[0][i]) for i in range(20)], act(A[0],B[1])-act(B[0],A[1]))
def lc(ts): return ([sp.expand(sum(c*t[0][i] for c,t in ts)) for i in range(20)], sp.expand(sum(c*t[1] for c,t in ts)))
def wedge(u,v): return sp.Matrix(4,4,lambda c,d:u[c]*v[d]-u[d]*v[c])
def W_of(s,c,chi,th,ze,x,al,be,ga):
    n=[1,s,-c,0]; e=[0,c,s,0]; f=[0,0,0,1]; nh=[0,s,-c,0]; d0=[1,0,0,0]
    low=lambda v:[eta[a,a]*v[a] for a in r4]
    k=[-z for z in low(n)]; eL=low(e); fL=low(f)
    Bn=wedge(d0,[-z for z in nh]); Jn=wedge(e,f); Ne=wedge(n,e); Nf=wedge(n,f)
    P=[ze*k[a]+al*eL[a]+(be+th)*fL[a] for a in r4]; Q=[x*k[a]+be*eL[a]+ga*fL[a] for a in r4]
    return [k[a]*(chi*Bn+th*Jn)+P[a]*Ne+Q[a]*Nf for a in r4], k, n
E=[[1,0,0,0],[0,1,kap*y[3]/2,0],[0,0,1,0],[0,0,-kap*y[1]/2,1]]   # E_b^mu
# different Cayley generator from S2
A=sp.Matrix([[0,sp.Rational(2,9),sp.Rational(1,7),sp.Rational(-1,4)],[0,0,sp.Rational(-2,5),sp.Rational(1,3)],[0,0,0,sp.Rational(1,6)],[0,0,0,0]]); A=A-A.T
M=eta*A; L=(sp.eye(4)-M).inv()*(sp.eye(4)+M); assert sp.simplify(L.T*eta*L-eta)==sp.zeros(4,4)
subU={U[i,j]:L[i,j] for i in r4 for j in r4}
def run(name,s,c,chi,th,ze,x,al,be,ga):
    con=sp.expand(th**2-2*th*be-2*be**2-al**2-ga**2+2*chi*(al+ga)); tau=sp.simplify(chi+al+ga)
    Wm,k,n=W_of(s,c,chi,th,ze,x,al,be,ga)
    # W_a n = lambda n and L^2 = 0 (vector action (W_a)^c_d = w_a^{ce} eta_ed)
    Wv=[Wm[a]*eta for a in r4]
    nul=all(sp.simplify((Wv[a]*sp.Matrix(n)).cross(sp.Matrix(n[:3]+[0])[:3,:]) if False else 0)==0 for a in r4)
    Lop=sp.simplify(sum((eta[a,a]*Wv[a]*Wv[a] for a in r4),sp.zeros(4,4)))
    D=[]
    for a in r4:
        comp=[0]*20; fn=0
        for b in r4:
            om=-Wm[b]*eta   # om_b^c_g
            Yb=list(E[b])+[-sum(U[ff,g]*om[cc,g] for g in r4) for ff in r4 for cc in r4]
            for i in range(20): comp[i]+=U[a,b]*Yb[i]
        comp=[sp.expand(z) for z in comp]
        div=sum(sp.diff(comp[i],X[i]) for i in range(20))
        D.append((comp,sp.expand(div/2)))
    Fc={(p,q):comm(D[p],D[q]) for p in r4 for q in r4 if p<q}
    def F(p,q):
        if p<q: return Fc[(p,q)]
        z=Fc[(q,p)]; return ([-t for t in z[0]],-z[1])
    res=set()
    for b in r4:
        tot=lc([(eta[a,a],comm(D[a],F(a,b))) for a in r4 if a!=b])
        res|=set(sp.simplify(sp.expand(t.subs(subU))) for t in tot[0]+[tot[1]])
    print(name,'con=',sp.simplify(con),'tau=',tau,'| [D^a,[D_a,D_b]] residual set:',res if len(res)<4 else ('%d distinct nonzero'%len(res-{0})),
          '| L^2==0:',sp.simplify(Lop*Lop)==sp.zeros(4,4),'| L==0:',Lop==sp.zeros(4,4),'[%.0fs]'%(time.time()-t0),flush=True)
R=sp.Rational; s13=sp.sqrt(13)
which=sys.argv[1]
if which=='A':   # tilted, chi != 0, tau = 0, zeta,x != 0 ; X=2be+th=1, Y=2ga+chi=sqrt13/3
    chi=R(1,3); ga=(s13/3-chi)/2
    run('TA(s=3/5,chi=1/3)',R(3,5),R(4,5),chi,1,R(2,3),R(-1,4),-chi-ga,0,ga)
if which=='B':   # negative control: tilted, constraint ok, tau=7/5 != 0
    run('NEG(s=3/5,tau!=0)',R(3,5),R(4,5),0,1,R(1,2),R(1,3),R(3,5),0,R(4,5))
if which=='C':   # untilted, chi != 0, tau free, be != 0 : con: th^2-2th be-2be^2-al^2-ga^2+2chi(al+ga)=0
    chi=R(1,2); th=R(1); be=R(-1,2); al=R(1,2)
    # solve for ga rational? con = 1+1-1/2-1/4-ga^2+1/2+ga = 7/4 + ga - ga^2 -> ga=(1+sqrt(8))/2
    ga=(1+sp.sqrt(8))/2
    run('UC(s=0,chi=1/2,be=-1/2)',0,1,chi,th,R(1,3),R(-2,7),al,be,ga)
if which=='D':   # 072 wider family limit
    run('W072(s=0,th=al=be=ga=0)',0,1,R(2,5),0,R(1,3),R(-1,2),0,0,0)
