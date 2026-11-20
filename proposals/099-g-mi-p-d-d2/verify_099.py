# verify_099.py -- item 099: MI(p,d) at D=2 in the named Gram classes.
# Run from repo root:  python -I proposals/099-g-mi-p-d-d2/verify_099.py
import numpy as np, sympy as sp
from numpy.polynomial.legendre import leggauss
rng = np.random.default_rng(20261119)
FAIL=[]
def chk(tag, cond, info=""):
    print(("PASS " if cond else "FAIL ")+tag+"  "+info, flush=True)
    if not cond: FAIL.append(tag)

# ---------- S1 exact D=2 constant-variance closed forms (M=2), sympy ----------
u,d,t = sp.symbols('u d t', positive=True)
fU2 = 6*(1-2*u)**2; fd2 = 6*d*(1-d); ft2 = sp.Rational(3,2)*(1-t**2)
chk("S1.norm", all(sp.integrate(g,(v,0,sp.Rational(1,2) if v is u else 1))-1==0
                   for g,v in [(fU2,u),(fd2,d),(ft2,t)]), "norms of f_U, f(d1), f(t) exactly 1")
chk("S1.fold", sp.simplify(ft2.subs(t**2,(2*d-1)**2)-fd2)==0, "fold f(t->|2d-1|) equals f(d1) exactly")
Hd2=-sp.integrate(fd2*sp.log(fd2),(d,0,1)); Ht2=-sp.integrate(ft2*sp.log(ft2),(t,0,1))
El2=sp.integrate(fU2*sp.log(1-2*u),(u,0,sp.Rational(1,2))); MI2=sp.simplify(Hd2-El2)
chk("S1.Hd", sp.simplify(Hd2-(sp.Rational(5,3)-sp.log(6)))==0, "h(d1)=5/3-ln6=%.10f"%sp.N(Hd2,12))
chk("S1.Ht", sp.simplify(Ht2-(sp.Rational(5,3)-sp.log(6)))==0, "h(t)=5/3-ln6 (fold Jacobian cancels)")
chk("S1.Elog", sp.simplify(El2+sp.Rational(1,3))==0, "E log(1-2U)=-1/3")
chk("S1.MI", MI2==2-sp.log(6), "I(p;d1)=I(p;t)=I(p;P2)=2-ln6=%.10f nats"%sp.N(MI2,12))
for M in (3,4):
    e=(u*(1-u))**(M-2)*(1-2*u)**2; C=1/sp.integrate(e,(u,0,sp.Rational(1,2)))
    eL=sp.integrate(C*e*sp.log(1-2*u),(u,0,sp.Rational(1,2)))
    print("S1.gen: M=%d: f_U=%s*(u(1-u))^(%d)*(1-2u)^2, E log(1-2U)=%s = %.10f"%(M,C,M-2,sp.simplify(eL),sp.N(eL,12)))
S=sp.symbols('S',positive=True)
chk("S1.091x", sp.integrate(3*S**2,(S,0,1))==1 and sp.integrate(3*S**4,(S,0,1))==sp.Rational(3,5),
    "sep density 3S^2: E S^2=3/5, Var(exch p1)=3/20=3/(8a+12) at a=1 (091 convention, para L3195)")

# ---------- S2 MC constant-variance: x ~ U[0,1] independent of spectrum ----------
def gram(a): return np.einsum('mji,mjk->mik', a.conj(), a)
def hmi(a,b,rngs):
    C=np.histogram2d(a,b,bins=[60,60],range=rngs)[0]; N=C.sum()
    P=C/N; Pr=P.sum(1,keepdims=True); Pc=P.sum(0,keepdims=True)
    ok=P>0
    return float(np.sum(P[ok]*np.log(P[ok]/(Pr*Pc)[ok])))
md=sp.symbols('md',nonnegative=True)
polyd={}
for MM in (2,3,4):
    eM=(u*(1-u))**(MM-2)*(1-2*u)**2; CM=1/sp.integrate(eM,(u,0,sp.Rational(1,2)))
    polyd[MM]=sp.lambdify(md,sp.simplify(sp.integrate(CM*eM/(1-2*u),(u,0,md))))
print("S2.poly: f(d1) at d=0.5: "+" ".join("M%d=%.6f"%(MM,polyd[MM](0.5)) for MM in (2,3,4)), flush=True)
for M in (2,3,4):
    N=1_500_000 if M==2 else 700_000
    A=(rng.standard_normal((N,M,2))+1j*rng.standard_normal((N,M,2)))/np.sqrt(2)
    G=gram(A); ev=np.linalg.eigvalsh(G); lam1,lam2=ev[...,1],ev[...,0]
    tau=lam1+lam2; uu=lam2/tau; xq=(G[:,0,0].real-lam2)/(lam1-lam2)
    dd=G[:,0,0].real/tau; tt=np.abs(2*dd-1)
    ks=np.max(np.abs(np.cumsum(np.histogram(xq,bins=200,range=(0,1))[0])/N-np.arange(1,201)/200))
    corr=np.corrcoef(xq,np.log(np.maximum(1e-9,1-2*uu)))[0,1]
    edg=np.linspace(0,1,101)[:-1]+0.005
    hd,_=np.histogram(dd,bins=100,range=(0,1),density=True)
    ht,_=np.histogram(tt,bins=100,range=(0,1),density=True)
    chk("S2.M%d.xunif"%M, ks<0.012, "KS(x,U)=%.5f n=%d"%(ks,N))
    chk("S2.M%d.indep"%M, abs(corr)<0.01, "corr(x,log(1-2u))=%+.5f"%corr)
    fdm=polyd[M](np.minimum(edg,1-edg)); ftm=0.5*(polyd[M](np.minimum((1+edg)/2,1-(1+edg)/2))+polyd[M](np.minimum((1-edg)/2,1-(1-edg)/2)))
    chk("S2.M%d.fd"%M, np.max(np.abs(hd-fdm))<0.07, "maxdev f(d1)=%.4f (peak %.3f)"%(np.max(np.abs(hd-fdm)),fdm.max()))
    chk("S2.M%d.ft"%M, np.max(np.abs(ht-ftm))<0.07, "maxdev f(t)=%.4f (peak %.3f)"%(np.max(np.abs(ht-ftm)),ftm.max()))
    if M==2:
        v1=hmi(np.clip(uu,1e-9,.5-1e-9),np.clip(xq,1e-9,1-1e-9),[[0,.5],[0,1]])
        v2=hmi(np.clip(uu,1e-9,.5-1e-9),np.clip(tt,1e-9,1-1e-9),[[0,.5],[0,1]])
        chk("S2.M2.MIx", abs(v1)<0.012, "MC I(u;x)=%.5f vs exact 0"%v1)
        chk("S2.M2.MIt", abs(v2-(2-np.log(6)))<0.02, "MC I(u;t)=%.5f vs 2-ln6=0.208241"%v2)

# ---------- S3 profile-class exact joint density: symbolic checks ----------
tau,x = sp.symbols('tau x', positive=True); g1,g2,sg2=sp.symbols('g1 g2 sigma2',positive=True)
lam1,lam2 = tau*(1-u), tau*u; beta=1/(sg2*g1)-1/(sg2*g2); rho=sp.simplify(beta*(lam1-lam2))
G11=lam2+(lam1-lam2)*x; expn=-G11/(sg2*g1)-(tau-G11)/(sg2*g2)
aU=u/(sg2*g1)+(1-u)/(sg2*g2)
chk("S3.lnexp", sp.simplify(sp.expand(expn-(-tau*aU-rho*x)))==0, "exponent = -tau*a(u)-rho*x exactly")
rp=sp.symbols('rp',positive=True)
chk("S3.Z", sp.simplify(sp.integrate(sp.exp(-rp*x),(x,0,1))-(1-sp.exp(-rp))/rp)==0, "int_0^1 e^{-rho x}=(1-e^{-rho})/rho, rho>0")
rm=sp.symbols('rm',negative=True)
chk("S3.Zneg", sp.simplify(sp.integrate(sp.exp(-rm*x),(x,0,1))-(1-sp.exp(-rm))/rm)==0, "same formula for rho<0 (swap profile)")
chk("S3.beta0", sp.simplify(rho.subs(g1,g2))==0, "rho vanishes exactly at g1=g2")
z=sp.symbols('z'); hx_sym=1+sp.log((1-sp.exp(-z))/z)-z/(sp.exp(z)-1)
chk("S3.hx0", sp.limit(hx_sym,z,0)==0, "truncated-exp entropy h_x(0)=0 (uniform): continuity at beta->0")

# ---------- S4 profile-class MI(p;x), MI(p;t): nested quadrature ----------
def hx_an(rho):  # analytic entropy of rho e^{-rho x}/(1-e^{-rho}) on [0,1], rho real
    rho=np.asarray(rho,float); out=np.zeros_like(rho); m=np.abs(rho)<1e-5
    r=rho[~m]; em1=np.expm1(-r)
    out[~m]=1+np.log(np.where(em1!=0,-em1/r,1))-r/np.expm1(r)
    out[m]=-rho[m]**2/24  # series: h=-rho^2/24+O(rho^3) (max at uniform rho=0)
    return out
def hy_num(rho,ng=300):  # entropy of |2x-1| when x ~ truncated exp rate rho on [0,1]; rho array
    yg,wyg=leggauss(ng); yg=0.5*(yg+1); wyg=0.5*wyg
    rho=np.asarray(rho,float)[:,None]
    W=np.where(np.abs(rho)<1e-10,1.0,(1-np.exp(-rho))/rho)
    g=np.exp(-rho/2)*np.cosh(rho*yg[None,:]/2)/W
    with np.errstate(divide='ignore'):
        return np.sum(wyg[None,:]*(-g*np.log(np.maximum(g,1e-300))),axis=1)
def pmi(gv,M,sg=1.,nug=500,nt=200,nx=500):
    g1v,g2v=gv; be=1/(sg*sg*g1v)-1/(sg*sg*g2v)
    ug,wug=leggauss(nug); ug=0.25*(ug+1); wug=0.25*wug
    xg,wxg=leggauss(nx); xg=0.5*(xg+1); wxg=0.5*wxg
    st,wt=leggauss(nt)
    bu=(1-2*ug)**2*(ug*(1-ug))**(M-2)
    F=np.zeros((nug,nx)); MU=[]
    for i,uu in enumerate(ug):
        ai=(uu/g1v+(1-uu)/g2v)/sg**2; s=1-2*uu
        lo,hi=np.log(1e-8),np.log(120/ai)
        tv=np.exp(0.5*(hi-lo)*st+0.5*(hi+lo)); jac=0.5*(hi-lo)*tv
        rr=be*tv*s
        with np.errstate(divide='ignore',invalid='ignore'):
            W=np.where(np.abs(rr)<1e-10,1.0,(1-np.exp(-rr))/rr)
        mq=tv**(2*M-1)*np.exp(-tv*ai)*jac*wt
        mW=mq*W
        F[i]=bu[i]*np.sum(mq[:,None]*np.exp(-rr[:,None]*xg[None,:]),axis=0)
        MU.append((tv,rr,mq,mW))
    F/=np.einsum('i,ij,j',wug,F,wxg)
    fu=F@wxg; fx=np.einsum('i,ij',wug,F)
    with np.errstate(divide='ignore'):
        Ix=float(np.einsum('i,ij,j',wug,F*(np.log(F)-np.log(fu[:,None])-np.log(fx[None,:])),wxg))
        hu=float(-np.sum(wug*fu*np.log(fu))); hxm=float(-np.sum(wxg*fx*np.log(fx)))
        Ehx=0.0; Eht=0.0
        for i,uu in enumerate(ug):
            tv,rr,mq,mW=MU[i]; J=np.sum(mW); s=1-2*uu
            hv=hx_an(rr); hY=hy_num(rr)+np.log(max(s,1e-300))
            Ehx+=wug[i]*fu[i]*np.sum(mW*hv)/J; Eht+=wug[i]*fu[i]*np.sum(mW*hY)/J
        tg,wtg=leggauss(120); tg=0.5*(tg+1); wtg=0.5*wtg
        ft=np.zeros_like(tg)
        for k,tv_ in enumerate(tg):
            hi2=(1-tv_)/2
            uu2,ww2=leggauss(120); uu2=hi2*0.5*(uu2+1); ww2=ww2*hi2*0.5
            idx=np.minimum(np.searchsorted(ug,uu2),len(ug)-1)
            row=np.array([0.5*(np.interp(0.5*(1+tv_/(1-2*uuu)),xg,F[j])+np.interp(0.5*(1-tv_/(1-2*uuu)),xg,F[j])) for uuu,j in zip(uu2,idx)])
            ft[k]=np.sum(ww2*row/(1-2*uu2))
        ht=float(-np.sum(wtg*ft*np.log(np.maximum(ft,1e-300))))
    It=ht-Eht
    return dict(Ix=Ix,It=It,tg=tg,ft=ft,F=F,hu=hu,hx=hxm,ht=ht,Ehx=Ehx,Eht=Eht,ug=ug,wug=wug,fu=fu,xg=xg,fx=fx,gv=gv,M=M,sg=sg)
print("S4: nested quadrature (u x tau x t grids), profile instances:")
res={}
for gv,M,sg in [((1.,1.),2,1.),((1.,2.),2,1.),((2.,1.),2,1.),((1.,2.),4,1.),((1.,2.),2,2.),((1.,2.),4,2.),((1.,1.5),2,1.)]:
    r=pmi(gv,M,sg); res[(gv[0],gv[1],M,sg)]=r
    print("S4 g=(%.1f,%.1f) M=%d sg=%.1f: I(p;x)=%.8f I(p;t)=I(p;P2)=%.8f h(x)=%.6f h(t)=%.6f"%(
        gv[0],gv[1],M,sg,r['Ix'],r['It'],r['hx'],r['ht']), flush=True)
chk("S4.swap", abs(res[(1.,2.,2,1.)]['Ix']-res[(2.,1.,2,1.)]['Ix'])<1e-7, "swap g exact symmetry")
chk("S4.siginv", abs(res[(1.,2.,2,1.)]['Ix']-res[(1.,2.,2,2.)]['Ix'])<1e-7 and abs(res[(1.,2.,4,1.)]['Ix']-res[(1.,2.,4,2.)]['Ix'])<1e-7,
    "MI exactly sigma-independent")
chk("S4.pos", all(r['Ix']>-1e-9 and r['It']>0 for r in res.values()), "MI(p;x)>=0 (equality at beta=0), MI(p;t)>0 in all instances")
print("S4.dp: I(p;t) vs I(p;x) per instance: " + ", ".join("(%.1f,%.1f)M%d: Ix=%.6f It=%.6f"%(k[0],k[1],k[2],v['Ix'],v['It']) for k,v in res.items()))
chk("S4.b0", abs(res[(1.,1.,2,1.)]['Ix'])<1e-6 and abs(res[(1.,1.,2,1.)]['It']-(2-np.log(6)))<0.01,
    "beta=0 self-test: I(p;x)=0 and I(p;P2)=2-ln6=0.208241 recovered, got Ix=%.2e It=%.6f"%(res[(1.,1.,2,1.)]['Ix'],res[(1.,1.,2,1.)]['It']))
chk("S4.tswap", abs(res[(1.,2.,2,1.)]['It']-res[(2.,1.,2,1.)]['It'])<1e-7, "I(p;t)=I(p;P2) swap g exact (t=s|2x-1| is swap-invariant)")
chk("S4.cvt", res[(1.,2.,2,1.)]['Ix']<0.05, "profile I(p;x)=%.6f small vs const-var I=2-ln6=0.208241"%res[(1.,2.,2,1.)]['Ix'])
chk("S4.beta0", res[(1.,1.5,2,1.)]['Ix']<res[(1.,2.,2,1.)]['Ix'] and res[(1.,1.5,2,1.)]['Ix']>0, "MI increases with |beta| (0.666 vs 0.5 tilt)")

# ---------- S5 independent ground-truth MC: direct profile-class Gram draws ----------
def gram_prof(gv,M,sg,n):
    g1v,g2v=gv; sd=(sg*np.sqrt([g1v,g2v]))[:,None]
    A=(rng.standard_normal((n,2,M))+1j*rng.standard_normal((n,2,M)))*sd/np.sqrt(2.)
    G=np.einsum('mji,mki->mjk',A,A.conj()); ev=np.linalg.eigvalsh(G)
    l1,l2=ev[...,1],ev[...,0]; uq=l2/(l1+l2)
    xq=(G[:,0,0].real-l2)/(l1-l2); return np.clip(uq,1e-9,.5-1e-9),np.clip(xq,1e-9,1-1e-9),np.clip((1-2*uq)*np.abs(2*xq-1),1e-9,1-1e-9)
def cl(v): return np.clip(v,1e-9,None)
for gv,M,sg,tag in [((1.,2.),2,1.,"g"),((2.,1.),2,1.,"sw"),((1.,2.),4,1.,"g4")]:
    uq,xq,tq=gram_prof(gv,M,sg,600_000); r=res[(gv[0],gv[1],M,sg)]
    o=np.argsort(r['ug']); cdf=np.cumsum(r['fu'][o]*r['wug'][o]); cdf/=cdf[-1]
    emp=np.cumsum(np.histogram(uq,bins=200,range=(0,.5))[0]/len(uq))
    cen=np.linspace(0,.5,200)+0.5*0.5/200
    ks=float(np.max(np.abs(emp-np.interp(cen,r['ug'][o],cdf))))
    miX=hmi(uq,xq,[[0,.5],[0,1]]); miT=hmi(uq,tq,[[0,.5],[0,1]])
    chk("S5.%s.ks"%tag, ks<0.012, "MC u vs quadrature f_U: KS=%.5f"%ks)
    chk("S5.%s.Ix"%tag, abs(miX-r['Ix'])<0.02, "MC I(p;x)=%.5f vs quad %.5f"%(miX,r['Ix']))
    chk("S5.%s.It"%tag, abs(miT-r['It'])<0.05, "MC I(p;t)=%.5f vs quad %.5f (60-bin hist bias, ladder-verified)"%(miT,r['It']))
    print("S5.%s: MC u=%.4f x=%.4f t=%.4f (mean/sd)"%(tag,uq.mean(),xq.mean(),tq.mean()), flush=True)
sw=gram_prof((2.,1.),2,1.,600_000); g2v=gram_prof((1.,2.),2,1.,600_000)
chk("S5.swapMC", abs(hmi(sw[0],sw[1],[[0,.5],[0,1]])-hmi(g2v[0],g2v[1],[[0,.5],[0,1]]))<0.015,
    "MC I(p;x) swap g symmetric")
print("SUMMARY", "ALL PASS" if not FAIL else "FAILED: "+",".join(FAIL))
assert not FAIL
print("SUMMARY ALL PASS")
