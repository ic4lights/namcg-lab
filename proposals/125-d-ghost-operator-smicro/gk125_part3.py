from sympy import *
RES=[]
def run(met,names,xilist,tag):
    global X; X=[symbols(nm) for nm in names]
    g=met
    gi=g.inv().applyfunc(simplify)
    def ch(gm,gi_):
        Gm={}
        for rr in range(len(X)):
            for m in range(len(X)):
                for q in range(m,len(X)):
                    v=simplify(Rational(1,2)*sum(gi_[rr,k]*(diff(gm[m,k],X[q])+diff(gm[q,k],X[m])-diff(gm[m,q],X[k])) for k in range(len(X))))
                    Gm[(rr,m,q)]=v;Gm[(rr,q,m)]=v
        return Gm
    N=len(X)
    G=ch(g,gi)
    Ric=Matrix.zeros(N,N)
    for s_ in range(N):
        for q in range(N):
            tt=0
            for m in range(N):
                tt+=diff(G[(m,q,s_)],X[m])-diff(G[(m,m,s_)],X[q])+sum(G[(m,m,l)]*G[(l,q,s_)]-G[(m,q,l)]*G[(l,m,s_)] for l in range(N))
            Ric[s_,q]=simplify(tt)
    def nV(V,a): return [simplify(diff(V[mu],X[a])+sum(G[(mu,a,b)]*V[b] for b in range(N))) for mu in range(N)]
    def boxv(xi):
        out=[]
        for mu in range(N):
            ssum=0
            for a in range(N):
                for b in range(N):
                    T=nV(xi,b)
                    Ta=simplify(diff(T[mu],X[a])+sum(G[(mu,a,l)]*T[l] for l in range(N))-sum(G[(l,a,b)]*nV(xi,l)[mu] for l in range(N)))
                    ssum+=gi[a,b]*Ta
            out.append(ssum)
        return out
    def ricv(xi): return [simplify(sum(gi[mu,s]*Ric[s,nu]*xi[nu] for s in range(N) for nu in range(N))) for mu in range(N)]
    def lie(xi):
        K=Matrix.zeros(N,N)
        for a in range(N):
            for b in range(a,N):
                v=expand(sum(xi[p]*diff(g[a,b],X[p]) for p in range(N))+sum(g[p,b]*diff(xi[p],X[a]) for p in range(N))+sum(g[a,p]*diff(xi[p],X[b]) for p in range(N)))
                K[a,b]=v;K[b,a]=v
        return K
    def cD(hh,a,b,c):
        return simplify(diff(hh[b,c],X[a])-sum(G[(p,a,b)]*hh[p,c] for p in range(N))-sum(G[(p,a,c)]*hh[b,p] for p in range(N)))
    ok=True
    for j,xi in enumerate(xilist):
        h=lie(xi)
        dG=[simplify(sum(gi[a,b]*Rational(1,2)*sum(gi[mu,s]*(cD(h,a,b,s)+cD(h,b,a,s)-cD(h,s,a,b)) for s in range(N)) for a in range(N) for b in range(N))) for mu in range(N)]
        cov=[simplify(b_+c_) for b_,c_ in zip(boxv(xi),ricv(xi))]
        r=[simplify(p-q) for p,q in zip(dG,cov)]
        z=all(v==0 for v in r)
        print("[%s] xi%d: g^{ab}dGamma(L_xi g) == (box+Ric)xi : %s"%(tag,j,z))
        if not z: print("   residual:",r)
        ok=ok and z
    RES.append(ok)
    return locals()
# S2 general xi
u,v=Function('u')(symbols('th th')) , None
th,ph=symbols('th ph')
th,ph=symbols('th ph')
u,v=Function('u')(th,ph),Function('v')(th,ph)
run(Matrix.diag(1,sin(th)**2),('th','ph'),[[u,v]],'S2gen')
# S2 affine-in-Killing check: (box+Ric) on all 3 Killing fields, direct route already covered; skip
# H2 general xi
rho,psi=symbols('rho psi')
w1,w2=Function('w1')(rho,psi),Function('w2')(rho,psi)
run(Matrix.diag(1,sinh(rho)**2),('rho','psi'),[[w1,w2]],'H2gen')
# 4D Lorentzian SSS with free A,B,C: affine r-component (4 constants) via direct tensor route
tt_,rr,th2,ph2=symbols('t rr th2 ph2')
A,B,C=Function('A')(rr),Function('B')(rr),Function('C')(rr)
met4=Matrix.diag(-C,B,rr**2,rr**2*sin(th2)**2)
cs=[symbols('c%d'%i) for i in range(4)]
xil=[[0,sum(cs[i]*mb for i,mb in enumerate([1,rr])),0,0]]
tt0,rr0,th0,ph0=symbols('t rr th2 ph2')
met4=Matrix.diag(-C,B,rr**2,rr**2*sin(th2)**2)
locs=run(met4,('t','rr','th2','ph2'),xil,'4Daff_r')
# 4D bare t-route with xi = d_r (constant), identity dF = box+Ric+GT
d=symbols('d')
Xi=[rr,0,0,0]  # homothety-like r-component constant = rr? keep constant instead:
Xi=[1,0,0,0]
X=[tt0,rr0,th0,ph2]
g4=met4
gi4=g4.inv().applyfunc(simplify)
def chg(gm,gi_):
    Gm={}
    for r_ in range(4):
        for m in range(4):
            for q in range(m,4):
                vv=simplify(Rational(1,2)*sum(gi_[r_,k]*(diff(gm[m,k],X[q])+diff(gm[q,k],X[m])-diff(gm[m,q],X[k])) for k in range(4)))
                Gm[(r_,m,q)]=vv;Gm[(r_,q,m)]=vv
    return Gm
G4=chg(g4,gi4)
Ric4=Matrix.zeros(4,4)
for s_ in range(4):
    for q in range(4):
        tv=0
        for m in range(4):
            tv+=diff(G4[(m,q,s_)],X[m])-diff(G4[(m,m,s_)],X[q])+sum(G4[(m,m,l)]*G4[(l,q,s_)]-G4[(m,q,l)]*G4[(l,m,s_)] for l in range(4))
        Ric4[s_,q]=simplify(tv)
def nV4(V,a): return [simplify(diff(V[mu],X[a])+sum(G4[(mu,a,b)]*V[b] for b in range(4))) for mu in range(4)]
def boxv4(xi):
    out=[]
    for mu in range(4):
        ssum=0
        for a in range(4):
            for b in range(4):
                T=nV4(xi,b)
                Ta=simplify(diff(T[mu],X[a])+sum(G4[(mu,a,l)]*T[l] for l in range(4))-sum(G4[(l,a,b)]*nV4(xi,l)[mu] for l in range(4)))
                ssum+=gi4[a,b]*Ta
        out.append(ssum)
    return out
def ricv4(xi): return [simplify(sum(gi4[mu,s]*Ric4[s,nu]*xi[nu] for s in range(4) for nu in range(4))) for mu in range(4)]
def lie4(xi):
    K=Matrix.zeros(4,4)
    for a in range(4):
        for b in range(a,4):
            vv=expand(sum(xi[p]*diff(g4[a,b],X[p]) for p in range(4))+sum(g4[p,b]*diff(xi[p],X[a]) for p in range(4))+sum(g4[a,p]*diff(xi[p],X[b]) for p in range(4)))
            K[a,b]=vv;K[b,a]=vv
    return K
h4=lie4(Xi)
gg=g4+d*h4; gig=gg.inv().applyfunc(simplify)
Gg=chg(gg,gig)
Fb=[simplify(sum(gig[a,b]*Gg[(mu,a,b)] for a in range(4) for b in range(4))) for mu in range(4)]
dFb=[simplify(diff(vv,d).subs(d,0)) for vv in Fb]
hu=gi4*h4*gi4
GT4=[simplify(-sum(hu[a,b]*G4[(mu,a,b)] for a in range(4) for b in range(4))) for mu in range(4)]
cov4=[simplify(p+q) for p,q in zip(boxv4(Xi),ricv4(Xi))]
res=[simplify(p-q-r) for p,q,r in zip(dFb,cov4,GT4)]
z4=all(v==0 for v in res)
print("[4D bare xi=d_r] dF == (box+Ric)+GT :",z4)
RES.append(z4)
print("GK PART3: %d/%d PASS"%(sum(RES),len(RES)))
