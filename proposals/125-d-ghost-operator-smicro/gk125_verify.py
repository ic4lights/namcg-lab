#!/usr/bin/env python3
# Independent gatekeeper re-derivation for proposal 125 (written from scratch;
# conventions: Gamma^r_mn = 1/2 g^{rs}(dm g_ns + dn g_ms - ds g_mn);
# R^r_s m n = dn G^r_ms - dm G^r_ns ... -> use (v^r);;m;n - ;;n;m = R^r_s m n v^s
# i.e. R[r,s,m,n] = dm G[r,n,s] - dn G[r,m,s] + G[r,m,l]G[l,n,s] - G[r,n,l]G[l,m,s]
# Ric[s,n] = R[m,s,m,n]; box = g^{ab} nab_a nab_b (connection Laplacian).
import sys, time
from sympy import (symbols, Function, Matrix, Rational, simplify, sin, cos,
                   sinh, diff, Poly, sqrt, expand)
T0=time.time()
def log(*a): print("[%6.1fs]"%(time.time()-T0),*a); sys.stdout.flush()
def ch(g,gi,n):
    G={}
    for r in range(n):
        for m in range(n):
            for q in range(m,n):
                s=sum(gi[r,k]*(diff(g[m,k],X[q])+diff(g[q,k],X[m])-diff(g[m,q],X[k])) for k in range(n))
                v=simplify(Rational(1,2)*s); G[(r,m,q)]=v; G[(r,q,m)]=v
    return G
def ric(G,gi,n):
    R=Matrix.zeros(n,n)
    for s_ in range(n):
        for q in range(n):
            t=0
            for m in range(n):
                t+=diff(G[(m,q,s_)],X[m])-diff(G[(m,m,s_)],X[q])
                t+=sum(G[(m,m,l)]*G[(l,q,s_)]-G[(m,q,l)]*G[(l,m,s_)] for l in range(n))
            R[s_,q]=simplify(t)
    return R
def geo(g,n):
    gi=g.inv(); gi=gi.applyfunc(simplify)
    G=ch(g,gi,n); return gi,G,ric(G,gi,n)
def nabV(G,xi,n,a):  # (nabla_a xi)^mu
    return [simplify(sum(diff(xi[mu],X[a])+G[(mu,a,b)]*xi[b] for b in range(n)) ) if False else simplify(diff(xi[mu],X[a])+sum(G[(mu,a,b)]*xi[b] for b in range(n))) for mu in range(n)]
def box(G,gi,xi,n):
    out=[]
    for mu in range(n):
        s=0
        for a in range(n):
            for b in range(n):
                # g^{ab} ( nab_a nab_b xi )^mu : first T = nab xi is (1,1)
                # (nab_a T)^mu_b with T^mu_b = (nab_b xi)^mu
                Ta=[0]*n
                for bb in range(n):
                    Tb=sum(diff(nabV(G,xi,n,bb)[mu],X[a])) if False else 0
                    tt=diff(nabV(G,xi,n,bb)[mu],X[a])+sum(G[(mu,a,l)]*nabV(G,xi,n,bb)[l] for l in range(n))-sum(G[(l,a,bb)]*nabV(G,xi,n,l)[mu] for l in range(n))
                    Ta[bb]=tt
                s+=gi[a,b]*sum(simplify(Ta[bb]) if False else Ta[bb] for bb in [b])
        out.append(simplify(s))
    return out
def ricv(gi,ric_,xi,n):
    return [simplify(sum(gi[mu,s]*ric_[s,nu]*xi[nu] for s in range(n) for nu in range(n))) for mu in range(n)]
def lie(g,xi,n):
    K=Matrix.zeros(n,n)
    for a in range(n):
        for b in range(a,n):
            v=expand(sum(xi[p]*diff(g[a,b],X[p]) for p in range(n))+sum(g[p,b]*diff(xi[p],X[a]) for p in range(n))+sum(g[a,p]*diff(xi[p],X[b]) for p in range(n)))
            K[a,b]=v; K[b,a]=v
    return K
def Fof(g,n):
    gi=g.inv(); gi=gi.applyfunc(simplify)
    G=ch(g,gi,n)
    return [simplify(sum(gi[a,b]*G[(mu,a,b)] for a in range(n) for b in range(n))) for mu in range(n)]
def dFt(g,h,n,t):
    Fv=Fof(g+t*h,n)
    return [simplify(diff(Fv[mu],t).subs(t,0)) for mu in range(n)]
def dFtilde(g,h,n,t,Gbar):
    # F~(g) = g^{ab}(Gamma[g]-Gamma[bar]) ; full t-differentiation (Gamma[bar] fixed)
    gg=g+t*h; gi=gg.inv(); gi=gi.applyfunc(simplify)
    G=ch(gg,gi,n)
    Fv=[simplify(sum(gi[a,b]*(G[(mu,a,b)]-Gbar[(mu,a,b)]) for a in range(n) for b in range(n))) for mu in range(n)]
    return [simplify(diff(Fv[mu],t).subs(t,0)) for mu in range(n)]
def GT(gi,G,h,n):  # -(L_xi g)^{ab} Gam^mu_ab
    hu=(gi*h*gi).applyfunc(simplify)
    return [simplify(-sum(hu[a,b]*G[(mu,a,b)] for a in range(n) for b in range(n))) for mu in range(n)]
def z(v): return simplify(v)==0

t=symbols('t'); RES=[]
# ---- GK1: S^2 rotational family identity, all pieces ---------------------
X=(symbols('th'),symbols('ph'))
met=Matrix.diag(1,sin(X[0])**2)
gi,G,Ric=geo(met,2)
f=Function('f')(X[0]); xi=[0,f]
h=lie(met,xi,2)
dF=dFt(met,h,2,t); bx=box(G,gi,xi,2); rv=ricv(gi,Ric,xi,2); gt=GT(gi,G,h,2)
log("GK1 dF = %s"%dF)
log("GK1 box = %s ; Ric.xi = %s ; GT = %s"%(bx,rv,gt))
ok = z(dF[1]-(f.diff(X[0],2)+f.diff(X[0])/sin(X[0])*cos(X[0]))) and z(bx[1]-(f.diff(X[0],2)+3*f.diff(X[0])/sin(X[0])*cos(X[0])-f)) and z(rv[1]-f) and z(gt[1]+2*f.diff(X[0])/sin(X[0])*cos(X[0])) and all(z(a-b-c-g) for a,b,c,g in zip(dF,bx,rv,gt))
log("GK1 S2-rot: dF=box+Ric+GT, parts match proposal hand-values: %s"%("PASS" if ok else "FAIL")); RES.append(ok)
# ---- GK2: true Killing trio; dead-script K1,K2 non-Killing ---------------
KILL=[[0,1],[-sin(X[1]),-cos(X[0])*cos(X[1])/sin(X[0])],[cos(X[1]),-sin(X[0])*cos(X[1])/sin(X[0])]]
ok=True
for i,k in enumerate(KILL):
    okk=z(lie(met,k,2)[0,0]) and all(z(v) for v in lie(met,k,2)) and z(bx[0]) and all(z(a+b) for a,b in zip(box(G,gi,k,2),ricv(gi,Ric,k,2))) and all(z(v) for v in dFt(met,lie(met,k,2),2,t))
    log("GK2 true Killing K%d: Lie=0, (box+Ric)K=0, dF=0: %s"%(i,"PASS" if okk else "FAIL")); ok=ok and okk; RES.append(okk)
KD=[[-cos(X[0])*sin(X[1]),-sin(X[0])*cos(X[1])],[-cos(X[0])*cos(X[1]),-sin(X[0])*sin(X[1])]]
okn = not z(lie(met,KD[0],2)[0,0])
res0=simplify(lie(met,KD[0],2)[0,0])
log("GK2 dead-script KILLS[1] NOT Killing: (L g)_thth = %s : %s"%(res0,"PASS" if okn else "FAIL")); RES.append(okn)
okn2 = not z(lie(met,KD[1],2)[0,0]); RES.append(okn2)
log("GK2 dead-script KILLS[2] NOT Killing: %s"%("PASS" if okn2 else "FAIL"))
# ---- GK3: H^2 convention + identity + Killing kernel ---------------------
X=(symbols('rho'),symbols('psi'))
mH=Matrix.diag(1,sinh(X[0])**2)
giH,GH,RH=geo(mH,2)
Rsc=simplify(sum(giH[a,b]*RH[a,b] for a in range(2) for b in range(2)))
w=Function('w')(X[0]); xh=[0,w]
hH=lie(mH,xh,2)
okd=all(simplify(a-b-c)==0 for a,b,c in zip(dFt(mH,hH,2,t),box(GH,giH,xh,2),GT(giH,GH,hH,2))) and all(simplify(a-b)==0 for a,b in zip(dFt(mH,hH,2,t),ricv(giH,RH,xh,2)))
# careful: identity is dF = box + Ric + GT; combine properly:
dH=dFt(mH,hH,2,t); bH=box(GH,giH,xh,2); rH=ricv(giH,RH,xh,2); gH=GT(giH,GH,hH,2)
okd=all(simplify(a-b-c-g)==0 for a,b,c,g in zip(dH,bH,rH,gH))
okK=all(simplify(a+b)==0 for a,b in zip(box(GH,giH,[0,1],2),ricv(giH,RH,[0,1],2)))
log("GK3 H^2: R = %s ; rot identity %s ; Killing dpsi kernel %s"%(Rsc,okd,okK))
RES.append(Rsc==-2); RES.append(okd); RES.append(okK)
print("GK PART1: %d/%d PASS"%(sum(RES),len(RES)))
