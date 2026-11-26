"""022 script 10: formal polynomial spectrum of the gauge-fixed vector operator H_V in the noncompact presentation X^A=M^{A5} (mu^2=+4 there)
on the invariant space of vector-valued polynomials of degree 1 in the M^{AB} (75-dim), and Weyl-formula check of the Casimir completion
    C_6(k,k,0) - C_5(k+1,k) + C_5(1,0) = 0   for all k,   with C_6(l1,l2,l3)=sum l_i(l_i+2(3-i)),  C_5(l1,l2)=l1(l1+3)+l2(l2+1).
"""
import sympy as sp, numpy as np, random
eta6=[-1,1,1,1,1,-1]; e5=[-1,1,1,1,1]
pairs=[(A,B) for A in range(6) for B in range(A+1,6)]
Ms={p:sp.Symbol('M%d%d'%p) for p in pairs}
def M(A,B):
    if A==B: return 0
    return Ms[(A,B)] if A<B else -Ms[(B,A)]
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
    y=[M(A,5) for A in range(5)]; yl=[e5[A]*y[A] for A in range(5)]
    mu2=4
    Dl=lambda A,f: e5[A]*PB(y[A],f)
    Box=lambda f: sp.expand(sum(e5[A]*PB(y[A],PB(y[A],f)) for A in range(5)))
    def HV(Av):
        Al=[e5[A]*Av[A] for A in range(5)]
        divA=sum(Dl(A,Av[A]) for A in range(5))
        out=[]
        for B in range(5):
            L=-Box(Al[B])-sum(PB(y[C],PB(Al[C],yl[B])) for C in range(5))-sum(PB(Av[C],PB(yl[C],yl[B])) for C in range(5))+mu2*Al[B]
            out.append(sp.expand(e5[B]*(L-Dl(B,divA))))     # back to upper index
        return out
    basis=[(B,p) for B in range(5) for p in pairs]
    idx={b:i for i,b in enumerate(basis)}
    Hm=np.zeros((75,75))
    for j,(B,p) in enumerate(basis):
        Av=[0]*5; Av[B]=Ms[p]
        out=HV(Av)
        for B2 in range(5):
            poly=sp.Poly(out[B2],*Ms.values()) if out[B2]!=0 else None
            if poly is None: continue
            for mon,co in poly.terms():
                q=[pairs[i] for i,e in enumerate(mon) if e==1]
                assert len(q)==1 and sum(mon)==1
                Hm[idx[(B2,q[0])],j]+=float(co)
    ev=np.sort(np.linalg.eigvals(Hm).real)
    vals,cnt=np.unique(np.round(ev,6),return_counts=True)
    print("s=%+d: eigenvalues of H_V on degree-1 vector polynomials (noncompact, mu^2=+4):"%s,dict(zip(vals,cnt)))
print()
def C6(l): return sum(li*(li+2*(3-i)) for i,li in enumerate(l,1))
def C5(l): return l[0]*(l[0]+3)+l[1]*(l[1]+1)
print("Weyl check C6(k,k,0) - C5(k+1,k) + C5(1,0) for k=0..12:",[C6((k,k,0))-C5((k+1,k))+C5((1,0)) for k in range(13)])
print("dim so(5) (k+1,k) = (2k+1)(2k+3)(2k+5)/3 for k=1..4:",[(2*k+1)*(2*k+3)*(2*k+5)//3 for k in range(1,5)],"; cumulative:",np.cumsum([(2*k+1)*(2*k+3)*(2*k+5)//3 for k in range(1,5)]))
