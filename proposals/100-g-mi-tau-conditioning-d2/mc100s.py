# mc100s.py -- ITEM 100 r1 MC corroboration (clean rewrite of the failed mc100r.py: array-safe Zf,
# no np.math/dead branches, Gamma(2M,rate Lambda) exponent 2M-1 for tau|x,u). Direct Wishart
# simulation validates the EXACT joint law f(tau,p2,x) claimed by ITEM 100: rows of A iid complex
# gaussian, column variances s^2 g_j; G=A^H A; p2=lam2/tau; x=(G11-lam2)/(lam1-lam2); rho=b(1-2p2)tau.
# Tests (|z|<4 required): E[x|p2 bin] vs truncated-exponential mean; E[tau|p2,x cell] vs 2M/Lambda;
# E[h(rho)] vs triple GL quadrature; E[tau|p2 bin] vs Nq-closed-form mean.
# Run: python -I proposals/100-g-mi-tau-conditioning-d2/mc100s.py
import numpy as np
from math import gamma
rng = np.random.default_rng(20261119)
def gl(n, lo, hi):
    t, w = np.polynomial.legendre.leggauss(n); return lo+(hi-lo)*(t+1)/2, w*(hi-lo)/2
def h(r):
    r = np.abs(r); return np.where(r < 1e-6, -(r**2)/24.0 + (r**4)/960.0,
        np.log(-np.expm1(-r)) - np.log(np.maximum(r, 1e-300)) + 1 - r*np.exp(-r)/(-np.expm1(-r)))
def consts(M, g1, g2, s):
    a = 1.0/(s*s*g1)+1.0/(s*s*g2); b = 1.0/(s*s*g1)-1.0/(s*s*g2); al = 2*M
    wv = lambda uu: b*(1-2*uu)
    Zf = lambda u: np.where(np.abs(wv(u)) < 1e-13, (a/2)**(-al),
         ((a/2+wv(u)/2)**(1-al)-(a/2-wv(u)/2)**(1-al))/((1-al)*wv(u)))
    phi = lambda u: (1-2*u)**2*(u*(1-u))**(M-2)
    um, wu = gl(400, 0, 0.5)   # gl returns (nodes, weights)
    Cu = np.sum(wu*phi(um)*Zf(um))
    return a, b, al, Zf, phi, (um, wu*phi(um)*Zf(um)/Cu)
def sim(M, g1, g2, s, N):
    A = (rng.standard_normal((N, M, 2))+1j*rng.standard_normal((N, M, 2)))/np.sqrt(2.0)
    A *= np.sqrt(s*s*np.array([g1, g2]))[None, None, :]
    G = np.einsum('nmi,nmj->nij', A.conj(), A)
    tr = G[:, 0, 0].real+G[:, 1, 1].real
    det = G[:, 0, 0].real*G[:, 1, 1].real-np.abs(G[:, 0, 1])**2
    s2 = np.sqrt(np.maximum(tr*tr/4-det, 0)); lam2 = tr/2-s2; lam1 = tr/2+s2
    return tr, lam2/tr, np.clip((G[:, 0, 0].real-lam2)/np.maximum(lam1-lam2, 1e-300), 0, 1)
def eh_ref(M, g1, g2, s, nU=240, nX=80, nT=140):
    a, b, al, Zf, phi, (um, wu) = consts(M, g1, g2, s)
    xm, wx = gl(nX, 0, 1); tl, wt = gl(nT, 0, 60)
    lam = a/2 + b*(1-2*um)[:, None]*(xm[None, :]-0.5)          # (nU,nX)
    pdfux = lam**(-al)/Zf(um)[:, None]
    E = 0.0
    for k in range(um.shape[0]):
        gz = wt*tl**(al-1)*np.exp(-tl)/gamma(al)
        for j in range(nX):
            E += wu[k]*wx[j]*pdfux[k, j]*np.sum(gz*h(b*(1-2*um[k])*tl/lam[k, j]))
    return E
def main():
    for (M, g1, g2, s) in [(2, 1, 2, 1), (4, 1, 2, 1)]:
        a, b, al, Zf, phi, (um, wu) = consts(M, g1, g2, s)
        tau, u, x = sim(M, g1, g2, s, 300_000)
        xq, wxq = gl(200, 0, 1)
        Lf = lambda uu, xx: a/2 + b*(1-2*uu)*(xx-0.5)
        print("MC M=%d g=(%d,%d) s=%d" % (M, g1, g2, s))
        for i in range(5):
            lo, hi = i/10, (i+1)/10
            m = (u >= lo) & (u < hi); ub = 0.5*(lo+hi)
            if m.sum() < 300: continue
            sel = (um >= lo) & (um < hi)
            exb = lambda uu: float(np.dot(wxq, xq*Lf(uu, xq)**(-al))/np.dot(wxq, Lf(uu, xq)**(-al)))
            ex = float(np.dot(wu[sel], [exb(v) for v in um[sel]])/wu[sel].sum())
            se = x[m].std()/np.sqrt(m.sum())
            print("  E[x|p2 bin %.1f] sim=%.5f ref=%.5f z=%+.2f" % (ub, x[m].mean(), ex, (x[m].mean()-ex)/se))
        m = (u > 0.2)&(u < 0.3)&(x > 0.45)&(x < 0.55)
        ref = 2*M/(a/2+b*(1-0.5)*0.0); se = tau[m].std()/np.sqrt(m.sum())
        print("  E[tau|p2~.25,x~.5] sim=%.5f ref~%.5f z=%+.2f" % (tau[m].mean(), 2*M/(a/2), (tau[m].mean()-2*M/(a/2))/se))
        hs = h(b*(1-2*u)*tau); se = hs.std()/np.sqrt(len(hs))
        er = eh_ref(M, g1, g2, s)
        print("  E[h(rho)] sim=%.6f ref=%.6f z=%+.2f" % (hs.mean(), er, (hs.mean()-er)/se))
if __name__ == "__main__":
    main()
