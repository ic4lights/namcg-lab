# mc100r.py -- item 100 r1: DIRECT Wishart Monte-Carlo cross-check of the exact joint law used in
# mi_tau_100r.py. Simulates A (M x 2, rows iid complex gaussian, column variances s^2 g_j), G=A^H A,
# u=p2=min eig/trace, x=(G11-lam2)/(lam1-lam2), rho=b*(1-2u)*tau. Compares simulated means of test
# functions phi(u,x), phi(tau|x,u) and E[h(rho)] to independent numpy-Gauss quadrature references of
# the SAME closed forms (different code path from mi_tau_100r.py). z-scores must be |z| < 4.
# Run: python -I proposals/100-g-mi-tau-conditioning-d2/mc100r.py
import numpy as np
rng = np.random.default_rng(20261119)
def quad(f, lo, hi, n=400):
    t, w = np.polynomial.legendre.leggauss(n)
    x = lo + (hi-lo)*(t+1)/2
    return (f(x)*w*(hi-lo)/2).sum() if callable(f) else (f*w*(hi-lo)/2).sum()
def refs(M, g1, g2, s):
    a = 1.0/(s*s*g1)+1.0/(s*s*g2); b = 1.0/(s*s*g1)-1.0/(s*s*g2)
    def L(u,x): return a/2 + b*(1-2*u)*(x-0.5)
    def Zf(u):
        d = b*(1-2*u)
        if abs(d) < 1e-14: return (a/2)**(-2*M)
        e = 1-2*M
        return ((a/2+d/2)**e-(a/2-d/2)**e)/(e*d)
    phi = lambda u: (1-2*u)**2*(u*(1-u))**(M-2)
    Cu = quad(lambda u: phi(u)*Zf(u), 0, 0.5, 400)
    fu = lambda u: phi(u)*Zf(u)/Cu
    def fx(x):
        return quad(lambda u: phi(u)*L(u,x)**(-2*M), 0, 0.5, 400)/Cu
    return a,b,L,Zf,fu,fx
def run(M, g1, g2, s, N=400_000):
    a,b,L,Zf,fu,fx = refs(M,g1,g2,s)
    A = (rng.standard_normal((N,M,2)) + 1j*rng.standard_normal((N,M,2)))/np.sqrt(2.0)
    A *= np.sqrt(s*s*np.array([g1,g2]))[None,None,:]
    G = np.einsum('nmi,nmj->nij', A.conj(), A)
    tr = G[:,0,0].real+G[:,1,1].real
    det = G[:,0,0].real*G[:,1,1].real - np.abs(G[:,0,1])**2
    s2 = np.sqrt(np.maximum(tr*tr/4-det,0))
    lam2 = tr/2-s2; lam1 = tr/2+s2
    u = lam2/tr
    x = (G[:,0,0].real-lam2)/np.maximum(lam1-lam2,1e-300)
    tau = tr
    # test 1: E[x | u in bin] vs closed form
    edges = np.linspace(0,0.5,6)
    out=[]
    for i in range(5):
        m = (u>=edges[i])&(u<edges[i+1])
        if m.sum() < 200: continue
        ub = 0.5*(edges[i]+edges[i+1])
        ref = quad(lambda xx: xx*L(ub,xx)**(-2*M)/Zf(ub), 0,1, 400)
        se = x[m].std()/np.sqrt(m.sum())
        out.append(("E[x|u~%.2f]"%ub, x[m].mean(), ref, (x[m].mean()-ref)/se))
    # test 2: E[tau | u,x bin] vs 2M/L
    mu_, mx_ = 0.25, 0.5
    m = (u>mu_-0.03)&(u<mu_+0.03)&(x>mx_-0.05)&(x<mx_+0.05)
    ref = 2*M/L(mu_,mx_)
    se = tau[m].std()/np.sqrt(m.sum())
    out.append(("E[tau|u~.25,x~.5]", tau[m].mean(), ref, (tau[m].mean()-ref)/se))
    # test 3: E[h(rho)] vs quadrature
    h = lambda r: np.where(r<1e-12, 0.0, np.log(np.abs(1-np.exp(-r))/r)+1-r/np.expm1(r))
    r_sim = b*(1-2*u)*tau
    hs = h(r_sim); sim = hs.mean()
    def Ehx_ref():
        def inner(xv):
            lam = L(0.25,xv) if False else None
            return None
        # nested quadrature with Gauss-Laguerre in tau at fixed (u,x)
        z,wz = np.polynomial.legendre.gauss_laguerre(... ) if False else (None,None)
        return None
    # do E[h] reference as 3-nested GL: u,x,tau(GL)
    nT = 600; zt,wt = np.polynomial.legendre.leggauss(nT)
    tl = (zt+1)*40; tw = wt*40  # tau in (0,80)
    uh,wh = np.polynomial.legendre.leggauss(120); um = (uh+1)*0.25; wu = wh*0.25
    xh,wx = np.polynomial.legendre.leggauss(60); xm = (xh+1)*0.5; wxx = wx*0.5
    E = 0.0
    for uu,wu_ in zip(um,wu):
        if uu<=0 or uu>=0.5: continue
        d = b*(1-2*uu); phi_u = (1-2*uu)**2*(uu*(1-uu))**(M-2)
        for xx,wx_ in zip(xm,wxx):
            lam = a/2+d*(xx-0.5)
            pdfu = phi_u*L(uu,xx)**(-2*M)
            gt = tl**(2*M-2)*np.exp(-lam*tl)*lam**(2*M)/(np.math.gamma(2*M) if False else float(np.prod(np.arange(1,2*M))))
            E += wu_*wx_*pdfu*np.sum(wt*gt*h(d*tl))
    Cu = quad(lambda uu: (1-2*uu)**2*(uu*(1-uu))**(M-2)*Zf(uu), 0,0.5,400)
    Eref = E/Cu
    se = hs.std()/np.sqrt(N)
    out.append(("E[h(rho)]", sim, Eref, (sim-Eref)/se))
    return out
if __name__ == "__main__":
    for (M,g1,g2,s) in [(2,1,2,1),(4,1,2,1)]:
        print("MC M=%d g=(%d,%d) s=%d" % (M,g1,g2,s))
        for name,sim,ref,z in run(M,g1,g2,s):
            print("  %-18s sim=%.6f ref=%.6f z=%+.2f" % (name,sim,ref,z))
    print("expect: |z| < 4 for every row")
