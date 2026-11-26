from sympy import *
import sys
X=[]
def mk(gi_,G_):
    pass
# 4D Lorentzian SSS free A(r),B(r),C(r)
tt,rr,th,ph=symbols('t rr th ph'); X=[tt,rr,th,ph]
A,B,C=Function('A')(rr),Function('B')(rr),Function('C')(rr)
g=Matrix.diag(-C,B,rr**2,rr**2*sin(th)**2)
gi=g.inv().applyfunc(simplify)
def ch(gm):
    gi_=gm.inv().applyfunc(simplify); Gm={}
    for r_ in range(4):
        for m in range(4):
            for q in range(m,4):
                v=Rational(1,2)*sum(gi_[r_,k]*(diff(gm[m,k],X[q])+diff(gm[q,k],X[m])-diff(gm[m,q],X[k])) for k in range(4))
                v=simplify(v); Gm[(r_,m,q)]=v;Gm[(r_,q,m)]=v
    return Gm,gi_
G,gi=ch(g)
Ric=Matrix.zeros(4,4)
for s_ in range(4):
    for q in range(4):
        tv=sum(diff(G[(m,q,s_)],X[m])-diff(G[(m,m,s_)],X[q])+sum(G[(m,m,l)]*G[(l,q,s_)]-G[(m,q,l)]*G[(l,m,s_)] for l in range(4)) for m in range(4))
        Ric[s_,q]=simplify(tv)
def nV(V,a): return [expand(diff(V[mu],X[a])+sum(G[(mu,a,b)]*expand(V[b]) for b in range(4))) for mu in range(4)]
def boxv(xi):
    out=[]
    for mu in range(4):
        ssum=0
        for a in range(4):
            for b in range(4):
                T=nV(xi,b)
                Ta=diff(T[mu],X[a])+sum(G[(mu,a,l)]*T[l] for l in range(4))-sum(G[(l,a,b)]*nV(xi,l)[mu] for l in range(4))
                ssum+=gi[a,b]*Ta
        out.append(trigsimp(expand(ssum)))
    return out
def ricv(xi): return [trigsimp(expand(sum(gi[mu,s]*Ric[s,nu]*xi[nu] for s in range(4) for nu in range(4)))) for mu in range(4)]
def lie(xi):
    K=Matrix.zeros(4,4)
    for a in range(4):
        for b in range(a,4):
            v=expand(sum(xi[p]*diff(g[a,b],X[p]) for p in range(4))+sum(g[p,b]*diff(xi[p],X[a]) for p in range(4))+sum(g[a,p]*diff(xi[p],X[b]) for p in range(4)))
            K[a,b]=v;K[b,a]=v
    return K
def cD(hh,a,b,c):
    return expand(diff(hh[b,c],X[a])-sum(G[(p,a,b)]*hh[p,c] for p in range(4))-sum(G[(p,a,c)]*hh[b,p] for p in range(4)))
def trigs(v):
    v=expand_trig(expand(v)); v=v.rewrite(exp)
    return simplify(v.rewrite(sin))
ok=True
for k in range(4):
    cs=[symbols('c%d'%i) for i in range(4)]
    mb=[1,rr,th,ph]
    xi=[0,0,0,0]; xi[k]=sum(cs[i]*mb[i] for i in range(4))
    h=lie(xi)
    dG=[trigs(sum(gi[a,b]*Rational(1,2)*sum(gi[mu,s]*(cD(h,a,b,s)+cD(h,b,a,s)-cD(h,s,a,b)) for s in range(4)) for a in range(4) for b in range(4))) for mu in range(4)]
    cov=[p+q for p,q in zip(boxv(xi),ricv(xi))]
    r=[Poly(trigs(p-q),*cs).coeffs() if trigs(p-q).has(*cs)==False or True else [] for p,q in zip(dG,cov)]
    eqs=[]
    for rr_ in r: eqs+=list(rr_)
    z=all(e==0 for e in eqs)
    print("4D free-A,B,C xi^{%d} affine: g^{ab}dGamma == box+Ric : %s (%d coef eqs)"%(k,z,len(eqs))); sys.stdout.flush()
    ok=ok and z
print("GK PART4:", "ALL PASS" if ok else "FAIL")
