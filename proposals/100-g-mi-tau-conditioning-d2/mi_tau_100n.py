# mi_tau_100n.py -- ITEM 100 PRIMARY exact-quadrature script (float64 high-order Gauss; mpmath twin
# mi_tau_100r.py kept as slow backup). Joint law of (tau,p2,x), 097/099 complex Wishart edge block, D=2:
#   f(u,x) prop phi(u) L(x,u)^{-2M}, phi=(1-2u)^2[u(1-u)]^{M-2}, L=a/2+w(x-1/2), w=b(1-2u),
#   a=c1'+c2', b=c1'-c2', c_j'=1/(s^2 g_j);  x|u ~ L^{-2M}/Z(u)  (NON-uniform for b!=0);
#   tau|x,u ~ Gamma(2M, rate L)  (=> tau|u density prop tau^{2M-2}(e^{-c0 tau}-e^{-c1 tau}), c0,1=a/2-+|w|/2);
#   f(x|tau,u) = rho e^{-rho x}/(1-e^{-rho}), rho=w tau (h = its entropy, even in rho).
# MI((tau,p2);x)=H(x)-E[h] ; I(tau;x|p2)=H(x|p2)-E[h] (route A) = E KL(Gamma(2M,L)||tau|p2) (route B);
# implied I(p2;x)=MI-I(tau;x|p2) must reproduce 099: 0.0108991 (M=2), 0.0327074 (M=4), g=(1,2).
import numpy as np
from scipy.special import roots_genlaguerre, digamma, gammaln
def gl(n, lo, hi):
    t, w = np.polynomial.legendre.leggauss(n); return w*(hi-lo)/2, lo+(hi-lo)*(t+1)/2
def h(r):
    r = np.abs(np.asarray(r, float)); out = np.log(np.expm1(r)/r) - r + 1 - r/np.expm1(r)
    return np.where(r < 1e-6, -(r**2)/24.0, out)
def run(M, g1, g2, s, nu=500, nx=400, nt=200):
    a = 1/(s*s*g1)+1/(s*s*g2); b = 1/(s*s*g1)-1/(s*s*g2); e = 1-2*M; al = 2*M
    wu, xu = gl(nu, 0, .5); wx, xx = gl(nx, 0, 1)
    zt, wt = roots_genlaguerre(nt, al-1); wt = wt/np.exp(gammaln(al))
    phi = lambda u: (1-2*u)**2*(u*(1-u))**(M-2)
    W = lambda u: b*(1-2*u)
    Zf = lambda u: np.where(np.abs(W(u)) < 1e-13, (a/2)**e*1.0,
        ((a/2+W(u)/2)**e-(a/2-W(u)/2)**e)/(e*W(u)))
    fu = phi(xu)*Zf(xu); Cu = np.sum(wu*fu); fu = fu/Cu
    Lm = a/2 + W(xu)[:, None]*(xx[None, :]-.5); pX = Lm**(-al)/Zf(xu)[:, None]
    Hxu = float(np.sum(wu*fu*(-np.sum(wx*(pX*np.log(pX)), 1))))
    Ehv = np.array([float(np.sum(wx*pX[i]*np.sum(wt*h(abs(W(xu[i]))*zt[None, :]/Lm[i, :, None]), 1)))
                    for i in range(nu)])
    Eh = float(np.sum(wu*fu*Ehv)); ItauA = Hxu - Eh
    fx = (wu*phi(xu)) @ Lm**(-al) / Cu; Hx = float(-np.sum(wx*fx*np.log(fx))); MI = Hx - Eh
    lnNu = gammaln(al-1) + np.log(np.abs(( (a/2-abs(W(xu))/2)**(1-al)-(a/2+abs(W(xu))/2)**(1-al) )/abs(W(xu)+1e-300)))
    Elnq = np.array([float(np.sum(wt*np.log(np.maximum(-np.expm1(-abs(W(xu[i]))*zt/Lm[i, :, None]), 1e-300)), 1))
                     for i in range(nu)])
    KL = (al-1)*np.log(Lm)+digamma(al)-al-gammaln(al)+2*M*(a/2-abs(W(xu))[:, None]/2)/Lm+lnNu[:, None]-Elnq
    ItauB = float(np.sum(wu*fu*np.sum(wx*pX*KL, 1)))
    return dict(Iu=MI-ItauA, MI=MI, ItauA=ItauA, ItauB=ItauB, Hx=Hx, Hxu=Hxu, Eh=Eh)
if __name__ == "__main__":
    assert abs(h(1e-3)-(-(1e-3)**2/24)) < 1e-12 and abs(h(0.0004)+6.6666667e-9) < 1e-14
    ref = {2: 0.0108991, 4: 0.0327074}
    for M in (2, 4):
        for (g1, g2, s, tag) in [(1, 2, 1, "base"), (1, 2, 2, "sig2"), (2, 1, 1, "swap")]:
            r1 = run(M, g1, g2, s); r2 = run(M, g1, g2, s, nu=800, nx=600, nt=400)
            df = abs(r2['Iu']-r1['Iu'])+abs(r2['ItauA']-r1['ItauA'])+abs(r2['ItauA']-r2['ItauB'])
            print("M=%d g=(%d,%d) s=%d %s: I(p2;x)=%.7f MI=%.7f I(tau;x|p2)=%.7f rB=%.7f Hx=%.6f Hx|u=%.6f Eh=%.6f refine+A/B=%.1e"
                  % (M, g1, g2, s, tag, r2['Iu'], r2['MI'], r2['ItauA'], r2['ItauB'], r2['Hx'], r2['Hxu'], r2['Eh'], df))
            if (g1, g2, s) == (1, 2, 1): print("   vs 099 %.7f -> |diff|=%.1e" % (ref[M], abs(r2['Iu']-ref[M])))
    for M in (2, 4):
        r = run(M, 1, 1, 1); print("cv g=(1,1) M=%d: Hx=%.2e Hx|u=%.2e Itau=%.2e MI=%.2e (expect ~0)" % (M, r['Hx'], r['Hxu'], r['ItauA'], r['MI']))
    e = run(2, 1, 100, 1); print("weak g=(1,100) M=2: I(p2;x)=%.7f Itau=%.7f (both ->0 as b->0)" % (e['Iu'], e['ItauA']))
