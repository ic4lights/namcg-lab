from sympy import *
r,ph,t=symbols('r ph t'); X=[r,ph]
g=Matrix.diag(1,r**2)
xi=[r*cos(ph)**2,-sin(ph)*cos(ph)]
def ch(g,gi):
    Gm={}
    for rr in range(2):
        for m in range(2):
            for q in range(m,2):
                v=simplify(Rational(1,2)*sum(gi[rr,k]*(diff(g[m,k],X[q])+diff(g[q,k],X[m])-diff(g[m,q],X[k])) for k in range(2)))
                Gm[(rr,m,q)]=v;Gm[(rr,q,m)]=v
    return Gm
# lie
def lie(g,xi):
    K=Matrix.zeros(2,2)
    for a in range(2):
        for b in range(a,2):
            v=expand(sum(xi[p]*diff(g[a,b],X[p]) for p in range(2))+sum(g[p,b]*diff(xi[p],X[a]) for p in range(2))+sum(g[a,p]*diff(xi[p],X[b]) for p in range(2)))
            K[a,b]=v;K[b,a]=v
    return K
h=lie(g,xi)
def Gam(gm):
    gi=gm.inv().applyfunc(simplify); return ch(gm,gi),gi
Gb,gb=Gam(g)
gt_=g+t*h
Gt,giT=Gam(gt_)
Ft=[simplify(sum(giT[a,b]*(Gt[(mu,a,b)]-Gb[(mu,a,b)]) for a in range(2) for b in range(2))) for mu in range(2)]
dFtild=[simplify(diff(v,t).subs(t,0)) for v in Ft]
print("dFtilde =",dFtild)
# direct tensor route: gb^{ab} delta Gamma(h)
def nabT(hh,Gm):
    # nab_a h_bc
    return {(a,b,c):simplify(diff(hh[b,c],X[a])-sum(Gm[(p,b,a)]*0 for p in range(2))+ -sum(Gm[(p,a,b)]*0 for p in range(2))) for a in range(2) for b in range(2) for c in range(2)}
# use proper covariant derivative of (0,2):
def cD(hh,Gm,a,b,c):
    return simplify(diff(hh[b,c],X[a])-sum(Gm[(p,a,b)]*hh[p,c] for p in range(2))-sum(Gm[(p,a,c)]*hh[b,p] for p in range(2)))
dG=[simplify(sum(gb[a,b]*Rational(1,2)*sum(gb[mu,s]*(cD(h,Gb,a,b,s)+cD(h,Gb,b,a,s)-cD(h,Gb,s,a,b)) for s in range(2)) for a in range(2) for b in range(2))) for mu in range(2)]
print("gb^{ab} dGamma(h) =",dG)
# bare dF t-route
Fb=[simplify(sum(giT[a,b]*Gt[(mu,a,b)] for a in range(2) for b in range(2))) for mu in range(2)]
dFb=[simplify(diff(v,t).subs(t,0)) for v in Fb]
print("dF bare =",dFb)
hu=gb*h*gb
GTv=[simplify(-sum(hu[a,b]*Gb[(mu,a,b)] for a in range(2) for b in range(2))) for mu in range(2)]
print("GT =",GTv)
