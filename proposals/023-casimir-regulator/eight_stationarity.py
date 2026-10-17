"""023 script 9: exact stationarity coefficients for the eight-matrix set {T^a=M^{a4}, y^a=M^{a5}}, a=0..3, with contraction weights (eta on T, lam*eta on y):
sum_J w_J {X^J,{X^J,X^I}} = c_I X^I.  c_T(lam), c_y(lam) in the polynomial Lie-Poisson algebra (both signs s)."""
import sympy as sp
eta6=[-1,1,1,1,1,-1]; e4=[-1,1,1,1]
pairs=[(A,B) for A in range(6) for B in range(A+1,6)]
Ms={p:sp.Symbol('M%d%d'%p) for p in pairs}
def M(A,B):
    if A==B: return 0
    return Ms[(A,B)] if A<B else -Ms[(B,A)]
lam=sp.Symbol('lam')
for s in (1,-1):
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
    T=[M(a,4) for a in range(4)]; Y=[M(a,5) for a in range(4)]
    res={}
    for name,X in (("T",T),("y",Y)):
        vals=set()
        for a in range(4):
            tot=sum(e4[b]*PB(T[b],PB(T[b],X[a])) for b in range(4))+lam*sum(e4[b]*PB(Y[b],PB(Y[b],X[a])) for b in range(4))
            vals.add(sp.simplify(sp.expand(tot)/X[a]))
        res[name]=vals
    print("s=%+d  c_T(lam)="%s,res["T"]," c_y(lam)=",res["y"])
    cT=list(res["T"])[0]; cy=list(res["y"])[0]
    print("      common bilinear coefficient requires c_T=c_y at lam =",sp.solve(sp.Eq(cT,cy),lam),"; there c =",[cT.subs(lam,l) for l in sp.solve(sp.Eq(cT,cy),lam)])
