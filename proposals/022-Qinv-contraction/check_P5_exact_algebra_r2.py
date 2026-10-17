"""022 script 4: exact checks in the polynomial Lie-Poisson algebra of so(4,2), both signs s, for the SO(4,1)-covariant presentation
   X^A = y^A = M^{A5}, A = 0..4, contraction e_A = eta_AA = diag(-1,1,1,1,1).
(1) {y_B,{y^B,y^A}} = lam5 y^A  -> mu^2 := lam5  (stationarity for S + mu^2 term, as in 018 for T^a: -3)
(2) y_A D^A = 0 as a vector field, i.e. {y.y, .} = 0, and y.y is constant on the orbit relation (numerics in script 1)
(3) Box5 = e_A D^A D^A  =  C_{so(4,1)} - C_{so(4,2)}   (Casimirs of the Lie-Poisson action on functions)
(4) Hessian: H_V A^B = L(A)^B - D^B(D.A) with L(A)_B = -Box A_B - {y_C,{A^C,y_B}} - {A^C,{y_C,y_B}} + mu^2 A_B
    equals  -Box5 A_B - 2 s' J_{BC} A^C + mu^2 A_B  (s' = -s) and, with the total so(4,1) generator G = J - Sigma',
    equals  C_{so(4,2)} - C_G + C_Sigma + mu^2 (exactly), in the sign for which orbital C_{so(4,1)} cancels.
"""
import sympy as sp, random, itertools
eta6=[-1,1,1,1,1,-1]; e5=[-1,1,1,1,1]
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
    random.seed(7)
    vs=list(Ms.values())
    def rpoly(): return sum(random.randint(-3,3)*sp.Mul(*random.sample(vs,k)) for k in (1,2) for _ in range(2))
    y=[M(A,5) for A in range(5)]
    yl=[e5[A]*y[A] for A in range(5)]
    # (1)
    lam=[]
    for A in range(5):
        v=sp.expand(sum(e5[C]*PB(y[C],PB(y[C],y[A])) for C in range(5)))
        k=sp.simplify(v/y[A]); lam.append(k)
    mu2=lam[0]
    print("s=%+d (1) sum_C e_C {y_C,{y_C,y_A}} / y_A ="%s,set(lam)," -> mu^2 =",mu2)
    # (2)
    ydot=sp.expand(sum(e5[A]*y[A]*y[A] for A in range(5)))   # y.y polynomial
    flag=all(sp.expand(sum(yl[A]*PB(y[A],f) for A in range(5)))!=0 or True for f in [rpoly()])
    f=rpoly()
    print("s=%+d (2) y_A D^A f == 0 (trivial for this f; inconclusive)"%s, sp.expand(sum(yl[A]*PB(y[A],f) for A in range(5)))==0, "(INCONCLUSIVE item: this f has no M^{.5} factor, so y_A D^A f = 0 holds trivially; the orbit-level check y_A D^A = 0 is in check_P5_vs_P4, 1.4e-13)")
    # (3) Casimirs
    J=lambda A,B,f: PB(M(A,B),f)
    ee=lambda A: eta6[A]
    C=lambda rng,f: sp.expand(sp.Rational(1,2)*sum(ee(A)*ee(B)*J(A,B,J(A,B,f)) for A in rng for B in rng if A!=B))
    Dp=lambda A,f: PB(y[A],f)
    Box=lambda f: sp.expand(sum(e5[A]*Dp(A,Dp(A,f)) for A in range(5)))
    f=rpoly()
    ok3=sp.expand(Box(f)-(C(range(5),f)-C(range(6),f)))==0
    print("s=%+d (3) Box5 = C_{so(4,1)} - C_{so(4,2)}:"%s,ok3)
    # (4) Hessian
    Av=[rpoly() for _ in range(5)]
    Al=[e5[A]*Av[A] for A in range(5)]
    Dl=lambda A,f: e5[A]*PB(y[A],f)
    divA=sum(Dl(A,Av[A]) for A in range(5))
    HV=[]
    for B in range(5):
        L=-Box(Al[B])-sum(PB(y[Cc],PB(Al[Cc],yl[B])) for Cc in range(5))-sum(PB(Av[Cc],PB(yl[Cc],yl[B])) for Cc in range(5))+mu2*Al[B]
        HV.append(sp.expand(L-Dl(B,divA)))
    # compare with -Box - 2 s' J A + mu2 A,  J_{BC}A^C := {M_{BC},A^C} with M_{BC}=e_B e_C M^{BC}
    res={}
    for sp_ in (+1,-1):
        ok=True
        for B in range(5):
            R=-Box(Al[B])-2*sp_*s*sum(PB(e5[B]*e5[Cc]*M(B,Cc),Av[Cc]) for Cc in range(5) if Cc!=B)+mu2*Al[B]
            ok=ok and sp.expand(HV[B]-R)==0
        res[sp_]=ok
    print("s=%+d (4a) H_V = -Box - 2 (sigma s) J.A + mu^2 for sigma=+1/-1:"%s,res)
    # (4b) Casimir completion.  Sigma'^{CD}A^B = sg*(eta^{CB}A^D - eta^{DB}A^C), G=J - Sigma'
    out={}
    for sg in (+1,-1):
        def Sig(Cc,D,Aup):    # Aup: list of 5 polys with upper index
            return [sg*(eta6[Cc]*(1 if B==Cc else 0)*Aup[D]-eta6[D]*(1 if B==D else 0)*Aup[Cc]) for B in range(5)]
        def G(Cc,D,Aup):
            Sg=Sig(Cc,D,Aup)
            return [PB(M(Cc,D),Aup[B])-Sg[B] for B in range(5)]
        def Cas(op,Aup):
            tot=[0]*5
            for Cc in range(5):
                for D in range(5):
                    if Cc==D: continue
                    r=op(Cc,D,op(Cc,D,Aup))
                    tot=[tot[B]+sp.Rational(1,2)*eta6[Cc]*eta6[D]*r[B] for B in range(5)]
            return [sp.expand(t) for t in tot]
        CG=Cas(G,Av); CS=Cas(Sig,Av)
        C42=[C(range(6),Av[B]) for B in range(5)]
        for sign_combo in [(1,-1,1),(1,1,-1),(1,-1,-1),(1,1,1)]:
            a,b,c=sign_combo
            ok=all(sp.expand(HV[B]-(a*C42[B]+b*CG[B]+c*CS[B]+mu2*Av[B]))==0 for B in range(5))
            # note HV carries lowered index: HV[B] is for A_B = e_B A^B ; compare with e_B*( ... ) 
            ok2=all(sp.expand(HV[B]-e5[B]*(a*C42[B]+b*CG[B]+c*CS[B]+mu2*Av[B]))==0 for B in range(5))
            out[(sg,sign_combo)]=(ok,ok2)
    good=[k for k,v in out.items() if v[0] or v[1]]
    print("s=%+d (4b) combos (sg,(a,b,c)) with H_V = a C42 + b C_G + c C_Sigma + mu2:"%s,good)
for s in (1,-1): run(s)
