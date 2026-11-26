from sympy import symbols, Function, Matrix, simplify, sin, cos, tan, diff, expand, Rational, sqrt, Poly
th,ph,s=symbols('th ph s')
X=[th,ph]
g=Matrix.diag(1,sin(th)**2)
gi=g.inv()
def ch(g,gi):
    G={}
    for r in range(2):
        for m in range(2):
            for q in range(m,2):
                v=simplify(Rational(1,2)*sum(gi[r,k2]*(diff(g[m,k2],X[q])+diff(g[q,k2],X[m])-diff(g[m,q],X[k2])) for k2 in range(2)))
                G[(r,m,q)]=v; G[(r,q,m)]=v
    return G
G=ch(g,gi)
def ric(G):
    R=Matrix.zeros(2,2)
    for sq in range(2):
        for q in range(2):
            tt=0
            for m in range(2):
                tt+=diff(G[(m,q,sq)],X[m])-diff(G[(m,m,sq)],X[q])+sum(G[(m,m,l)]*G[(l,q,sq)]-G[(m,q,l)]*G[(l,m,sq)] for l in range(2))
            R[sq,q]=simplify(tt)
    return R
Ric=ric(G)
def box(G,gi,xi):
    def nV(V,a): return [simplify(diff(V[mu],X[a])+sum(G[(mu,a,b)]*V[b] for b in range(2))) for mu in range(2)]
    out=[]
    for mu in range(2):
        ssum=0
        for a in range(2):
            for b in range(2):
                T=nV(xi,b)
                Ta=simplify(diff(T[mu],X[a])+sum(G[(mu,a,l)]*T[l] for l in range(2))-sum(G[(l,a,b)]*T[mu] for l in range(2)))
                ssum+=gi[a,b]*Ta
        out.append(simplify(ssum))
    return out
def lie(xi):
    K=Matrix.zeros(2,2)
    for a in range(2):
        for b in range(a,2):
            v=expand(sum(xi[p]*diff(g[a,b],X[p]) for p in range(2))+sum(g[p,b]*diff(xi[p],X[a]) for p in range(2))+sum(g[a,p]*diff(xi[p],X[b]) for p in range(2)))
            K[a,b]=v;K[b,a]=v
    return K
def Fof(g2):
    gi2=g2.inv().applyfunc(simplify); G2=ch(g2,gi2)
    return [simplify(sum(gi2[a,b]*G2[(mu,a,b)] for a in range(2) for b in range(2))) for mu in range(2)]
KILL=[[0,1],[-sin(ph),-cos(ph)*cos(th)/sin(th)],[cos(ph),-sin(ph)*cos(th)/sin(th)]]
for i,k in enumerate(KILL):
    L=lie(k)
    bx=box(G,gi,k)
    rv=[simplify(sum(gi[mu,sq]*Ric[sq,nu]*k[nu] for sq in range(2) for nu in range(2))) for mu in range(2)]
    dF=[simplify(diff(v,s).subs(s,0)) for v in Fof(g+s*L)]
    print("K%d Lie=0: %s | (box+Ric)=0: %s | dF=0: %s"%(i, all(simplify(L[a,b])==0 for a in range(2) for b in range(2)), [simplify(a+b) for a,b in zip(bx,rv)], dF))
