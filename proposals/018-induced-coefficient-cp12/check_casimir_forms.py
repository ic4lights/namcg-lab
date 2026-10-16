"""Exact checks in the polynomial Lie-Poisson algebra of so(4,2), s=+-1.
(1) Box = C_{so(4,1)'} - C_{so(3,1)}  (indices 0..4 resp. 0..3), Box = eta_ab D^a D^b, D^a={T^a,.}, T^a=M^{a4}.
(2) [Box, J^{AB}]=0 for A,B in 0..4 (so(4,1)' generators); [Box,D^a]!=0.
(3) gauge-fixed vector operator H_V A_a = L(A)_a - D_a(D.A) equals -Box A_a - 2 s J_ab A^b + mu^2 A_a.
(4) fibre-constant sector: {T^a,y^mu}= s eta^{a mu} M^45, {T^a,M^45} = -s y^a (y^a=M^{a5}), so on functions of y^A, A=0..4,
    D^a = s (y^4 d^a - y^a d_4), a so(4,1) rotation field of the hyperboloid y.y=-ell^2.
"""
import sympy as sp, random
eta6=[-1,1,1,1,1,-1]; e4=[-1,1,1,1]
pairs=[(A,B) for A in range(6) for B in range(A+1,6)]
Ms={p:sp.Symbol('M%d%d'%p) for p in pairs}
def M(A,B):
    if A==B: return 0
    return Ms[(A,B)] if A<B else -Ms[(B,A)]
def run(s):
    def lie(A,B,C,D):
        e=lambda X,Y: eta6[X] if X==Y else 0
        return s*(e(A,C)*M(B,D)-e(A,D)*M(B,C)-e(B,C)*M(A,D)+e(B,D)*M(A,C))
    brM={(p,r):sp.expand(lie(p[0],p[1],r[0],r[1])) for p in pairs for r in pairs}
    def PB(f,g):
        f=sp.sympify(f); g=sp.sympify(g); out=0
        for p in pairs:
            df=sp.diff(f,Ms[p])
            if df==0: continue
            for r in pairs:
                dg=sp.diff(g,Ms[r])
                if dg!=0: out+=df*dg*brM[(p,r)]
        return sp.expand(out)
    random.seed(3)
    vs=list(Ms.values())
    def rpoly(): return sum(random.randint(-3,3)*sp.Mul(*random.sample(vs,k)) for k in (1,2) for _ in range(3))
    T=[M(a,4) for a in range(4)]
    J=lambda A,B,f: PB(M(A,B),f)           # J^{AB} f
    ee=lambda A: eta6[A]
    Dp=lambda a,f: PB(T[a],f)
    Box=lambda f: sp.expand(sum(e4[a]*Dp(a,Dp(a,f)) for a in range(4)))
    C=lambda rng,f: sp.expand(sp.Rational(1,2)*sum(ee(A)*ee(B)*J(A,B,J(A,B,f)) for A in rng for B in rng if A!=B))
    f=rpoly()
    ok1=sp.expand(Box(f)-(C(range(5),f)-C(range(4),f)))==0
    print("s=%+d (1) Box = C41' - C31:"%s,ok1)
    ok2=all(sp.expand(Box(J(A,B,f))-J(A,B,Box(f)))==0 for (A,B) in [(0,1),(1,2),(0,3),(2,3)])
    nz=sp.expand(Box(Dp(0,f))-Dp(0,Box(f)))!=0
    print("s=%+d (2) [Box,J^ab]=0 (a,b<=3): %s ; [Box,D^0]!=0: %s"%(s,ok2,nz))
    mu2=-3
    A=[rpoly() for _ in range(4)]; Al=[e4[a]*A[a] for a in range(4)]
    Tl=[e4[a]*T[a] for a in range(4)]
    Dl=lambda a,f: e4[a]*Dp(a,f)
    Jl=lambda a,b,f: PB(e4[a]*e4[b]*M(a,b),f)
    ok3=True
    for a in range(4):
        L=-sum(e4[b]*PB(T[b],PB(T[b],Al[a])) for b in range(4))-sum(PB(T[b],PB(Al[b],Tl[a])) for b in range(4))-sum(PB(A[b],PB(Tl[b],Tl[a])) for b in range(4))+mu2*Al[a]
        divA=sum(Dl(b,A[b]) for b in range(4))
        HV=sp.expand(L-Dl(a,divA))
        R=-Box(Al[a])-2*s*sum(Jl(a,b,A[b]) for b in range(4))+mu2*Al[a]
        ok3=ok3 and sp.expand(HV-R)==0
    print("s=%+d (3) H_V = -Box - 2 s J.A + mu^2 (gauge-fixed, background Feynman):"%s,ok3)
    # ghost: delta(D.A) under A_a={Lam,T_a}
    Lam=rpoly()
    gv=sp.expand(sum(Dl(b,PB(Lam,T[b])) for b in range(4))+Box(Lam))
    print("s=%+d     delta(D.A) = -Box Lam (ghost operator -Box):"%s,gv==0)
    y=[M(a,5) for a in range(5)]
    ok4=all(sp.expand(PB(T[a],y[mu])-s*e4[a]*(1 if a==mu else 0)*M(4,5))==0 for a in range(4) for mu in range(4))
    ok4b=all(sp.expand(PB(T[a],y[4])+s*y[a])==0 for a in range(4))
    # D^a on a polynomial g(y^0..y^4)
    ys=sp.symbols('u0:5'); g=ys[0]**2*ys[4]+ys[1]*ys[2]*ys[0]+ys[4]**3+ys[3]**2*ys[1]
    gg=g.subs({ys[i]:y[i] for i in range(5)})
    ok4c=True
    for a in range(4):
        rhs=s*(y[4]*e4[a]*sp.diff(g,ys[a]) - y[a]*sp.diff(g,ys[4]))   # eta^{aa} d_a = d^a
        rhs=rhs.subs({ys[i]:y[i] for i in range(5)})
        ok4c=ok4c and sp.expand(PB(T[a],gg)-rhs)==0
    print("s=%+d (4) {T,y^mu},{T,y^4}:"%s,ok4,ok4b," D^a g(y)= s(y^4 d^a - y^a d_4)g:",ok4c)
for s in (1,-1): run(s)
