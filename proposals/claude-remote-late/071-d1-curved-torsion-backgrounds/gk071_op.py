"""Gatekeeper independent operator check (071 r1).  Literal L1519 form:
D_a = u_a^b ( E_b - u_f^g om_b^c_g d/du_f^c ) + t_a,  om_b^c_g = om_b^{cd} eta_dg,
t_a = (1/2) div(first term) computed directly; S_cd u_a^b = eta_ad u_c^b - eta_ac u_d^b.
Vector fields on (y,u) with sympy; evaluate at a random Lorentz u and generic y.
Reports: first relation, T,R read off at u=1, full matrix equation incl. order-zero part."""
import itertools, sys
import numpy as np, sympy as sp
from scipy.linalg import expm
eta = sp.diag(-1,1,1,1)
y = sp.symbols('y0:4'); U = sp.Matrix(4,4,lambda i,j: sp.Symbol('u%d%d'%(i,j)))
coords = list(y)+list(U)
def gen(d):
    M = sp.zeros(4,4)
    for (c,e),v in d.items(): M[c,e]=v; M[e,c]=-v
    return M
B = gen({(0,2):1}); N = gen({(0,1):1,(1,2):1}); Np = gen({(0,3):1,(2,3):-1}); k=[1,0,1,0]
class VF:
    def __init__(s, comp, f=0): s.c = [sp.sympify(x) for x in comp]; s.f = sp.sympify(f)  # vector + multiplication part
    def act(s, g): return sum(s.c[i]*sp.diff(g, coords[i]) for i in range(20))
def comm(A,Bv):
    c = [sp.expand(A.act(Bv.c[i]) - Bv.act(A.c[i])) for i in range(20)]
    return VF(c, sp.expand(A.act(Bv.f) - Bv.act(A.f)))
def add(*ts):
    c=[sum(t[0]*t[1].c[i] for t in ts) for i in range(20)]; return VF(c, sum(t[0]*t[1].f for t in ts))
def build(Ey, om, include_t=True):
    # Ey: list of 4 lists (y-components of E_b); om[b] = 4x4 matrix om_b^{cd}
    D=[]
    for a in range(4):
        comp=[0]*20
        for b in range(4):
            for i in range(4): comp[i]+= U[a,b]*Ey[b][i]
            omg = om[b]*eta   # om_b^c_g
            for f in range(4):
                for c in range(4):
                    comp[4+4*f+c] += U[a,b]*(-sum(U[f,g]*omg[c,g] for g in range(4)))
        D.append(VF(comp))
    if include_t:
        # divergence in d^4y dHaar: Haar-divergence of the right-mult fields u->uX vanishes; div(u_a^b Y_b)=Y_b(u_a^b) + u_a^b div_y(E_b)
        for a in range(4):
            dv=0
            for b in range(4):
                omg = om[b]*eta
                Yb = VF(list(Ey[b])+[ -sum(U[f,g]*omg[c,g] for g in range(4)) for f in range(4) for c in range(4)])
                dv += Yb.act(U[a,b]) + U[a,b]*sum(sp.diff(Ey[b][i],y[i]) for i in range(4))
            D[a].f = sp.expand(dv/2)
    S={}
    for c,d in itertools.combinations(range(4),2):
        comp=[0]*20
        for a in range(4):
            for b in range(4): comp[4+4*a+b] = eta[a,d]*U[c,b]-eta[a,c]*U[d,b]
        S[(c,d)]=VF(comp)
    return D,S
def lorentz(seed):
    rng=np.random.default_rng(seed); X=rng.normal(size=(4,4)); e=np.diag([-1,1,1,1.]); A=0.4*(X-e@X.T@e); return expm(A)
def run(name, Ey, om, cH=None):
    D,S = build(Ey, om)
    L = lorentz(7); sub={U[i,j]:sp.Float(L[i,j],30) for i in range(4) for j in range(4)}
    sub.update({y[0]:0.3,y[1]:-0.7,y[2]:0.2,y[3]:1.1})
    num=lambda V: np.array([float(sp.N(x.subs(sub))) for x in V.c]+[float(sp.N(V.f.subs(sub)))])
    # first relation
    e1=0
    for (c,d),Sv in S.items():
        for a in range(4):
            e1=max(e1, np.abs(num(comm(Sv,D[a])) - (float(eta[a,d])*num(D[c]) - float(eta[a,c])*num(D[d]))).max())
    # matrix equation
    Fab={(a,b):comm(D[a],D[b]) for a in range(4) for b in range(4) if a!=b}
    me=0; mef=0
    for b in range(4):
        tot = add(*[(float(eta[a,a]), comm(D[a],Fab[(a,b)])) for a in range(4) if a!=b])
        v=num(tot); me=max(me,np.abs(v[:20]).max()); mef=max(mef,abs(v[20]))
    # read off T at u=1 from [D_a,D_b] at u=1 (y generic)
    sub1={U[i,j]:(1 if i==j else 0) for i in range(4) for j in range(4)}; sub1.update({y[0]:0.3,y[1]:-0.7,y[2]:0.2,y[3]:1.1})
    n1=lambda V: np.array([float(sp.N(x.subs(sub1))) for x in V.c]+[float(sp.N(V.f.subs(sub1)))])
    basis=np.array([n1(D[a])[:20] for a in range(4)]+[n1(S[p])[:20] for p in S]).T
    T=np.zeros((4,4,4)); R={}
    for a in range(4):
        for b in range(4):
            if a<b:
                x,*_=np.linalg.lstsq(basis, n1(Fab[(a,b)])[:20], rcond=None)
                T[a,b]=-x[:4]; T[b,a]=x[:4]; R[(a,b)]=dict(zip(S.keys(), np.round(x[4:],6)))
    tr=[sum(T[a,c,c] for c in range(4)) for a in range(4)]
    print('==',name); print('  first relation %.1e ; matrix eq: vector part %.1e, order-zero part %.1e'%(e1,me,mef))
    print('  trace T_ac^c at u=1:', np.round(tr,6), '; t_a at u=1:', [round(float(sp.N(D[a].f.subs(sub1))),6) for a in range(4)])
    print('  R pairs nonzero:', {p:{q:v for q,v in d.items() if abs(v)>1e-9} for p,d in R.items() if any(abs(v)>1e-9 for v in d.values())})
flat=[[1 if i==b else 0 for i in range(4)] for b in range(4)]
s=1; r3=sp.sqrt(3)
for m,lab in [([0,-s,0,r3*s],'(i) trace-free, om = s k B + m N (literal L1519 sign)'),([0,2,0,0],'(i) tau=1')]:
    om=[s*k[a]*B + m[a]*N for a in range(4)]
    run(lab, flat, om)
# (ii) Heisenberg: E1 = d1 + k/2 y3 d2, E3 = d3 - k/2 y1 d2  => [E3,E1] = kappa E2
kap=1; z=1; xx=sp.Rational(1,2)
EH=[[1,0,0,0],[0,1,kap*y[3]/2,0],[0,0,1,0],[0,0,-kap*y[1]/2,1]]
run('(ii) Heisenberg, om = k(zeta N + x N\'), zeta=1,x=1/2', EH, [k[a]*(z*N+xx*Np) for a in range(4)])
# control
run('control: Heisenberg with om = k B (not claimed)', EH, [k[a]*B for a in range(4)])
