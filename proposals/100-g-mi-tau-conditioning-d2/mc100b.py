# mc100b.py -- item 100 INDEPENDENT cross-checks (supersedes mc100.py, whose trapezoid path used infeasible
# 4-D arrays and was killed). Path A: Wishart sampling structural check (x|u ~ U(0,1); tau|x,u ~ Gamma(2M,c+dx)).
# Path B: closed-form J via integration by parts (J = (e^{-c T}S(c) - e^{-(c+d)T}S(c+d))/d, S(y)=sum_k (2M)!/(2M-k)!
#   y^(2M-k) T^-(k+1)), trapezoid grids in u, x and mapped tau (T = Q t/(1-t)), vs mi_tau_100.py's GL/Laguerre.
# Path C: direct Wishart-MC estimator mean[2M ln lam - lam tau + c tau - ln J(tau)], J closed form.
# Run from repo root: python -I proposals/100-g-mi-tau-conditioning-d2/mc100b.py   (~2-3 min)
import numpy as np
from scipy.special import gammaln
rng = np.random.default_rng(707)
AL_F = {}
def facts(al):
    if al not in AL_F:
        import math
        AL_F[al] = (np.array([math.factorial(al)/math.factorial(al-k) for k in range(al+1)]),
                    np.arange(al+1))
    return AL_F[al]
def logJclosed(c, d, T, al):
    cf, k = facts(al)
    def S(y):
        yb, Tb = np.broadcast_arrays(np.asarray(y)[...,None], np.asarray(T)[...,None])
        return np.sum(cf*(yb**(al-k))/Tb**(k+1), axis=-1)
    J = (np.exp(-np.clip(c*T,0,700))*S(c) - np.exp(-np.clip((c+d)*T,0,700))*S(c+d))/d
    return np.log(np.clip(J, 1e-300, None))
def wish(M, g1, g2, sig, N):
    s1, s2 = np.sqrt(sig*g1/2), np.sqrt(sig*g2/2)
    A = s1*(rng.standard_normal((N,M))+1j*rng.standard_normal((N,M)))
    B = s2*(rng.standard_normal((N,M))+1j*rng.standard_normal((N,M)))
    tau = (np.abs(A)**2+np.abs(B)**2).sum(1); g11 = (np.abs(A)**2).sum(1)
    z = (np.conj(A)*B).sum(1); detg = g11*(np.abs(B)**2).sum(1)-z.real**2-z.imag**2
    disc = np.sqrt(np.maximum(tau**2-4*detg, 0)); lam2 = (tau-disc)/2
    return tau, lam2/tau, (g11-lam2)/np.where(disc>1e-12, disc, 1)
def pathA(M, g1, g2, sig, u0=0.11):
    a, b, al = 1/(sig*g2), 1/(sig*g1)-1/(sig*g2), 2*M
    tau, u, x = wish(M, g1, g2, sig, 400_000)
    w = (u > u0-0.01) & (u < u0+0.01); lamc = a+b*u0+b*(1-2*u0)*0.5
    print(" A M%d win u~%.2f: meanx=%.4f varx=%.4f (U .5 .0833); tau/E=%.4f var/E^2=%.4f (Gam %.4f %.4f)"
          % (M, u0, x[w].mean(), x[w].var(), tau[w].mean(), tau[w].var()/tau[w].mean()**2,
             al/lamc, 1/al), flush=True)
def pathB(M, g1, g2, sig, nu=2001, nx=601, nt=801, chunk=40):
    a, b, al = 1/(sig*g2), 1/(sig*g1)-1/(sig*g2), 2*M
    ug = np.linspace(1e-6, 0.5-1e-6, nu); xg = np.linspace(0, 1, nx)
    t = np.linspace(1e-4, 1-1e-6, nt); Q = 60.0
    num = den = 0.0
    for lo in range(0, nu, chunk):
        hi = min(lo+chunk, nu)
        c = a+b*ug[lo:hi]; d = b*(1-2*ug[lo:hi])
        lam = c[:,None]+d[:,None]*xg[None,:]
        T = Q*t[None,None,:]/(1-t[None,None,:])/lam[:,:,None]
        lw = al*np.log(lam)[:,:,None]+(al-1)*np.log(T)-lam[:,:,None]*T-gammaln(al)+np.log(Q/(1-t)**2/(lam*1.0))[None,None,:]
        pw = np.exp(np.clip(lw, -700, 700))*(t[1]-t[0])
        lJ = logJclosed(c[:,None,None], d[:,None,None], T, al)
        KL = al*np.log(lam)-al+c[:,None]*al/lam-(pw*lJ).sum(2)/pw.sum(2)
        Iu = np.trapezoid(KL, xg, axis=1)
        integ = np.where(np.abs(d)>1e-9,(c**(1-al)-(c+d)**(1-al))/((al-1)*np.where(d==0,1,d)), c**(-al))
        pu = (ug[lo:hi]*(1-ug[lo:hi]))**(M-2)*(1-2*ug[lo:hi])**2*integ
        num += np.trapezoid(pu*Iu, ug[lo:hi]); den += np.trapezoid(pu, ug[lo:hi])
    return num/den
def pathC(M, g1, g2, sig, N=400_000):
    a, b, al = 1/(sig*g2), 1/(sig*g1)-1/(sig*g2), 2*M
    tau, u, x = wish(M, g1, g2, sig, N)
    c = a+b*u; lam = c+b*(1-2*u)*x
    est = al*np.log(lam)-lam*tau+c*tau-logJclosed(c, b*(1-2*u), tau, al)
    return est.mean(), est.std()/np.sqrt(N)
if __name__ == "__main__":
    for M,g1,g2,sg in [(2,1.,2.,1.),(4,1.,2.,1.)]:
        pathA(M,g1,g2,sg)
        print(" B M%d trap+closedJ: %.7f | C MC(Wishart): %.7f +-%.7f"
              % ((M,)+pathB(M,g1,g2,sg)[:1]+pathC(M,g1,g2,sg)+ ()), flush=True)
    v = pathB(2,1.,1.2,1.); print(" B beta->0 M2 g=(1,1.2): %.6f (small positive expected)" % v, flush=True)
    print(" reference mi_tau_100.py: 0.1144322 (M2) 0.2525176 (M4)")
