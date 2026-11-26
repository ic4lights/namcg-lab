"""022 script 7: extended matrix sets X^I = M^{C_I D_I} with signs w_I (contraction sum_I w_I ...):
(i) is the background stationary for a single bilinear coefficient, i.e. sum_J w_J {X_J,{X_J,X_I}} = mu^2 w_I X_I for all I ?  (exact, sympy, s=+1)
(ii) rank of span{D^I} on the 6D leaf at random orbit points (numerical, 013 realisation)
Sets: S4 = {T^a}; S5 = {y^A}; S8 = {T^a, y^a} with the y-block signs (+eta, -eta, +delta); S7 = {T^a, y^i}.
"""
import sympy as sp, numpy as np, itertools
import sys
from symbol_tools import *
eta6l=[-1,1,1,1,1,-1]
pairs_=[(A,B) for A in range(6) for B in range(A+1,6)]
Ms={p:sp.Symbol('M%d%d'%p) for p in pairs_}
def Msym(A,B):
    if A==B: return 0
    return Ms[(A,B)] if A<B else -Ms[(B,A)]
def PBsym_factory(s):
    def lie_(A,B,C,D):
        e=lambda X,Y: eta6l[X] if X==Y else 0
        return s*(e(A,C)*Msym(B,D)-e(A,D)*Msym(B,C)-e(B,C)*Msym(A,D)+e(B,D)*Msym(A,C))
    brM={(p,r):sp.expand(lie_(p[0],p[1],r[0],r[1])) for p in pairs_ for r in pairs_}
    def PB(f,g):
        f=sp.sympify(f); g=sp.sympify(g); out=0
        for p in pairs_:
            df=sp.diff(f,Ms[p])
            if df==0: continue
            for r in pairs_:
                dg=sp.diff(g,Ms[r])
                if dg!=0: out+=df*dg*brM[(p,r)]
        return sp.expand(out)
    return PB
PB=PBsym_factory(1)
def eom_coeffs(fields,w):
    X=[Msym(C,D) for (C,D) in fields]
    out=[]
    for I in range(len(fields)):
        v=sum(w[J]*PB(X[J],PB(X[J],X[I])) for J in range(len(fields)))
        v=sp.expand(v)
        # fit v = lam * w_I X_I
        lam=sp.simplify(v/(w[I]*X[I])) if X[I]!=0 else None
        out.append(lam)
    return out
sets={}
eta4=[-1,1,1,1]
sets['S4 {T^a}']=([(a,4) for a in range(4)],eta4)
sets['S5 {y^A}']=([(A,5) for A in range(5)],[-1,1,1,1,1])
for nm,yw in [('+eta',eta4),('-eta',[-x for x in eta4]),('delta',[1,1,1,1])]:
    sets['S8 {T^a,y^a}, y-block '+nm]=([(a,4) for a in range(4)]+[(a,5) for a in range(4)],eta4+yw)
sets['S7 {T^a,y^i}, y^i delta']=([(a,4) for a in range(4)]+[(i,5) for i in (1,2,3)],eta4+[1,1,1])
sets['S9 {T^a,y^a,y^4}, eta,eta,+']=([(a,4) for a in range(4)]+[(a,5) for a in range(4)]+[(4,5)],eta4+eta4+[1])
rng=np.random.default_rng(2)
for nm,(fields,w) in sets.items():
    lam=eom_coeffs(fields,w)
    ranks=set()
    for t in range(15):
        z=rand_z_pos(rng,rng.uniform(0.5,4)); M0=Mfun(z)
        Dv=np.array([vec(M0,C,D) for (C,D) in fields]); sv=np.linalg.svd(Dv,compute_uv=False)
        ranks.add(int(np.sum(sv>1e-9*sv[0])))
    print(f"{nm}: eom coefficients (sum_J w_J {{X_J,{{X_J,X_I}}}} = lam_I w_I X_I): {lam}; rank of span D^I on the leaf: {sorted(ranks)}")
