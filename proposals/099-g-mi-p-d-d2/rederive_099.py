# rederive_099.py -- independent re-derivation of all insert-r1.tex claims (item 099).
# Joint (u,x): G=A^dag A, A Mx2 CN(0,sig^2 g_j); exact tau integration (int tau^(2M-1)e^{-Lam tau}=Gamma(2M)/Lam^(2M))
# gives f ~ [u(1-u)]^(M-2) s^2 (a+b(u+sx))^(-2M); a=1/(sig g2), b=1/(sig g1)-1/(sig g2), s=1-2u.
# I(p;P2)=I(u;t), t=s|2x-1|, = E[ln f_{T|U}(t|u)]+H(T); fT(t) by split-panel GL quadrature per t-node
# of the analytic kernel (no mask discontinuity): fT(t)=int [f(u,x+)+f(u,x-)]/(2s) du, x+-=(1+-t/s)/2.
# Run: python -I proposals/099-g-mi-p-d-d2/rederive_099.py
import numpy as np, sympy as sp
n=1200; xn,xwc=np.polynomial.legendre.leggauss(n); xu,xw=xn/4+0.25,xwc/4
m=2400; xm1,xwm=np.polynomial.legendre.leggauss(m); xx,xw2=xm1/2+0.5,xwm/2
def fmat(M,a,b,U,X):
    s=1-2*U; return np.clip((U*(1-U))**(M-2)*s**2/(a+b*(U+s*X))**(2*M),1e-300,None)
def cases(M,g1,g2,sig):
    a=1/(sig*g2); b=1/(sig*g1)-1/(sig*g2); U=xu[:,None]; X=xx[None,:]
    fraw=fmat(M,a,b,U,X); W=np.outer(xw,xw2); Z=np.sum(W*fraw); f=fraw/Z
    fU=f@xw2; fX=xw@f; s=1-2*xu; fUr=fraw@xw2
    Ix=np.sum(W*f*np.log(f/(fU[:,None]*fX[None,:])))
    A=np.log((fmat(M,a,b,U,1-X)+fraw)/(2*np.clip(s,1e-300,None)[:,None]*fUr[:,None]))
    E1=np.sum(W*f*A)
    Nt=3201; tg1=np.linspace(0,1,Nt); T=tg1[:,None]; us=(1-T)/2
    def panel(lo,hi):
        mid=(lo+hi)/2; hw=(hi-lo)/2; Um=mid+hw*xn[None,:]; S=np.maximum(1-2*Um,1e-300)
        Xp=(1+T/S)/2; R=(fmat(M,a,b,Um,Xp)+fmat(M,a,b,Um,1-Xp))*hw*xwc[None,:]/(2*S)
        return np.where(S>T,R,0.0)
    with np.errstate(divide='ignore',invalid='ignore'):
        fT=(panel(0.0,us)+panel(us,0.5)).sum(1)/Z
    Ht=-np.trapezoid(fT*np.log(np.maximum(fT,1e-300)),tg1)
    return Ix,E1+Ht
exact=2-np.log(6); bad=[]; r={}
for key in [(2,1,1,1),(4,1,1,1),(2,1,2,1),(4,1,2,1),(2,1,2,2),(4,1,2,2),(2,2,1,1),(4,2,1,1)]:
    M,g1,g2,sig=key; r[key]=cases(M,g1,g2,sig)
    print("M=%d g=(%g,%g) sig=%g: I(p;x)=%.8f I(p;P2)=%.9f"%(M,g1,g2,sig,r[key][0],r[key][1]))
tgt={(2,1,2,1):(0.01089907,0.2679875),(4,1,2,1):(0.03270741,0.4752657)}
for k,(ix,it) in tgt.items():
    if not np.isfinite(r[k][0]) or not np.isfinite(r[k][1]): bad.append("nan %s"%(k,))
    elif abs(r[k][0]-ix)>3e-5 or abs(r[k][1]-it)>3e-5: bad.append("target %s"%(k,))
if abs(r[(2,1,1,1)][0])>1e-10: bad.append("cvM2 Ix")
if abs(r[(2,1,1,1)][1]-exact)>1e-6: bad.append("cvM2 It")
if abs(r[(4,1,1,1)][0])>1e-10: bad.append("cvM4 Ix")
if max(abs(r[k][j]-r[(2,1,2,1)][j]) for k in [(2,1,2,2),(2,2,1,1)] for j in(0,1))>1e-8: bad.append("sig/swap")
print("exact 2-ln6 = %.10f  (M=2 g=(1,1) quadrature: %.10f)"%(exact,r[(2,1,1,1)][1]))
t=sp.Symbol('t',positive=True)
hd=-sp.integrate(6*t*(1-t)*sp.log(6*t*(1-t)),(t,0,1))
ht=-sp.integrate(sp.Rational(3,2)*(1-t**2)*sp.log(sp.Rational(3,2)*(1-t**2)),(t,0,1))
els=sp.integrate(3*t**2*sp.log(t),(t,0,1))
print("h(d1)=5/3-ln6:",sp.simplify(hd-(sp.Rational(5,3)-sp.log(6)))==0)
print("h(t)=5/3-ln6:",sp.simplify(ht-(sp.Rational(5,3)-sp.log(6)))==0)
print("Eln s=-1/3:",els==sp.Rational(-1,3)," I=h(t)-Elns=2-ln6:",sp.simplify(ht-els-(2-sp.log(6)))==0)
print("SUMMARY","ALL PASS" if not bad else "FAILURES "+",".join(bad))
