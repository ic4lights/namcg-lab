"""023 script 4: exact checks in the polynomial Lie-Poisson algebra of so(4,2) (both signs s) for the FOUR-matrix class X^a = T^a = M^{a4}, a=0..3.
(1) mu^2 from  sum_b e_b {T_b,{T_b,T_a}} = lam T_a  (expected -3)
(2) Box = e_a D^a D^a = C_{so(4,1)} - C_{so(3,1)}                       (Casimirs of the Lie-Poisson action on functions)
(3) Hessian H_V A_B = L(A)_B - D_B(D.A), L(A)_B = -Box A_B - {T_C,{A^C,T_B}} - {A^C,{T_C,T_B}} + mu^2 A_B   (as in 022 script 4 with y->T)
    fitted as   H_V = x C_G + y C31 + z C41 + w C42 + u (C_Sigma = const) + mu^2     with G = J - Sigma' on vector-valued functions; solve exactly.
(4) commutators [C42, H_V] = [C41, H_V] = 0 on random vector polynomials;  C42 - C41 expressed through J^{A5}.
(5) [C31, Box] != 0 ( C31 alone does not commute) and [C41,Box]=0."""
import sympy as sp, random, itertools
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
    random.seed(11)
    vs=list(Ms.values())
    def rpoly(): return sum(random.randint(-3,3)*sp.Mul(*random.sample(vs,k)) for k in (1,2) for _ in range(2))
    T=[M(a,4) for a in range(4)]; Tl=[e4[a]*T[a] for a in range(4)]
    lam=[sp.simplify(sum(e4[b]*PB(T[b],PB(T[b],T[a])) for b in range(4))/T[a]) for a in range(4)]
    mu2=lam[0]
    print("s=%+d (1) lam_a ="%s,set(lam),"-> mu^2 =",mu2)
    J=lambda A,B,f: PB(M(A,B),f)
    ee=lambda A: eta6[A]
    def C(rng_,f): return sp.expand(sp.Rational(1,2)*sum(ee(A)*ee(B)*J(A,B,J(A,B,f)) for A in rng_ for B in rng_ if A!=B))
    D=lambda a,f: PB(T[a],f)
    Box=lambda f: sp.expand(sum(e4[a]*D(a,D(a,f)) for a in range(4)))
    f=rpoly()
    print("s=%+d (2) Box = C41 - C31:"%s, sp.expand(Box(f)-(C(range(5),f)-C(range(4),f)))==0)
    print("s=%+d (5) [C41,Box]=0:"%s, sp.expand(C(range(5),Box(f))-Box(C(range(5),f)))==0, "; [C31,Box]=0:", sp.expand(C(range(4),Box(f))-Box(C(range(4),f)))==0)
    Av=[rpoly() for _ in range(4)]; Al=[e4[a]*Av[a] for a in range(4)]
    Dl=lambda a,f: e4[a]*D(a,f)
    divA=sum(Dl(a,Av[a]) for a in range(4))
    HV=[]
    for B in range(4):
        L=-Box(Al[B])-sum(PB(T[c],PB(Al[c],Tl[B])) for c in range(4))-sum(PB(Av[c],PB(Tl[c],Tl[B])) for c in range(4))+mu2*Al[B]
        HV.append(sp.expand(L-Dl(B,divA)))
    # fit
    res={}
    for sg in (+1,-1):
        def Sig(c,d,Aup): return [sg*(eta6[c]*(1 if B==c else 0)*Aup[d]-eta6[d]*(1 if B==d else 0)*Aup[c]) for B in range(4)]
        def G(c,d,Aup):
            Sg=Sig(c,d,Aup); return [PB(M(c,d),Aup[B])-Sg[B] for B in range(4)]
        def Cas(op,Aup):
            tot=[0]*4
            for c in range(4):
                for d in range(4):
                    if c==d: continue
                    r=op(c,d,op(c,d,Aup)); tot=[tot[B]+sp.Rational(1,2)*eta6[c]*eta6[d]*r[B] for B in range(4)]
            return [sp.expand(t) for t in tot]
        CG=Cas(G,Av); CS=Cas(Sig,Av)
        C31v=[C(range(4),Av[B]) for B in range(4)]; C41v=[C(range(5),Av[B]) for B in range(4)]; C42v=[C(range(6),Av[B]) for B in range(4)]
        xs=sp.symbols('x y z w u')
        ops=[CG,C31v,C41v,C42v,CS,Av]
        coef=list(xs)+[mu2]
        eqs=[]
        for B in range(4):
            expr=sp.expand(HV[B]-e4[B]*sum(c*o[B] for c,o in zip(coef,ops)))
            eqs+=sp.Poly(expr,*vs).coeffs()
        sol=sp.solve(eqs,list(xs),dict=True)
        res[sg]=sol
    print("s=%+d (3) fit H_V = x C_G + y C31 + z C41 + w C42 + u C_Sigma + mu^2, solutions by Sigma-sign:"%s,res)
    # (4) commutation on a vector polynomial
    for name,rng_ in (("C42",range(6)),("C41",range(5))):
        ok=True
        Av2=[rpoly() for _ in range(4)]; Al2=[e4[a]*Av2[a] for a in range(4)]
        Dl2=lambda a,f: e4[a]*D(a,f)
        def HVop(Aup):
            Alow=[e4[a]*Aup[a] for a in range(4)]; dv=sum(Dl2(a,Aup[a]) for a in range(4)); out=[]
            for B in range(4):
                Lb=-Box(Alow[B])-sum(PB(T[c],PB(Alow[c],Tl[B])) for c in range(4))-sum(PB(Aup[c],PB(Tl[c],Tl[B])) for c in range(4))+mu2*Alow[B]
                out.append(sp.expand(e4[B]*(Lb-Dl2(B,dv))))
            return out
        lhs=HVop([C(rng_,a) for a in Av2]); rhs=[C(rng_,h) for h in HVop(Av2)]
        print("s=%+d (4) [%s, H_V]=0 on random vector polynomial:"%(s,name), all(sp.expand(l-r)==0 for l,r in zip(lhs,rhs)))
    # C42 - C41 in terms of J^{A5}
    g=rpoly()
    d=sp.expand(C(range(6),g)-C(range(5),g)-sum(-ee(A)*J(A,5,J(A,5,g)) for A in range(5)))
    print("s=%+d (4b) C42 - C41 = - sum_{A<=4} eta_A (J^{A5})^2 :"%s, d==0)
for s in (1,-1): run(s)
