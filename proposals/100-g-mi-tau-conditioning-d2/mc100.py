# mc100.py -- item 100 independent cross-checks of mi_tau_100.py.
# Path A (Wishart sampling, no formulas from this session): draw A M x 2 with CN(0, sig^2 g_j / 2) entries,
#   form tau=G11+G22, eigenvalue u, fibre x; verify the structural fact x|u ~ U(0,1) (windowed moments 1/2,1/3)
#   and tau|x,u ~ Gamma(2M, rate c+d x) (windowed moments 2M/lam, 2M(2M+1)/lam^2).
# Path B (independent quadrature of the same closed-form KL): trapezoid in t for Gamma moments (tau = 12 t/(1-t)
#   scaled by 1/lam), trapezoid x-integrals, u-trapezoid, instead of mi_tau_100.py's GL/Laguerre nodes.
# Run from repo root: python -I proposals/100-g-mi-tau-conditioning-d2/mc100.py   (~2 min)
import numpy as np
from scipy.special import gammaln
rng = np.random.default_rng(101)
def wish(M, g1, g2, sig, N):
    s1, s2 = np.sqrt(sig*g1/2), np.sqrt(sig*g2/2)
    A = s1*(rng.standard_normal((N,M))+1j*rng.standard_normal((N,M)))
    B = s2*(rng.standard_normal((N,M))+1j*rng.standard_normal((N,M)))
    tau = (np.abs(A)**2+np.abs(B)**2).sum(1); g11 = (np.abs(A)**2).sum(1)
    z = (np.conj(A)*B).sum(1); detg = g11*(np.abs(B)**2).sum(1)-z.real**2-z.imag**2
    disc = np.sqrt(np.maximum(tau**2-4*detg, 0)); lam2 = (tau-disc)/2
    return tau, lam2/tau, (g11-lam2)/np.where(disc>1e-12, disc, 1)
def pathA(M, g1, g2, sig):
    a, b = 1/(sig*g2), 1/(sig*g1)-1/(sig*g2)
    tau, u, x = wish(M, g1, g2, sig, 400_000)
    w = (u > 0.10) & (u < 0.12); xw, tw = x[w], tau[w]
    lamc = a+b*0.11+b*(1-0.22)*0.5
    al = 2*M
    print("  window u in (.10,.12): mean x=%.4f var x=%.4f (U:0.5,0.0833) E tau=%.4f E tau^2/E^2=%.4f "
          "(Gamma: %.4f, %.4f)" % (xw.mean(), xw.var(), tw.mean(), (tw**2).mean()/tw.mean()**2,
          al/lamc, (al+1)/(al*1)*1))
def KLtrap(M, g1, g2, sig, nu=30001, nx=3001, nt=4001):
    a, b = 1/(sig*g2), 1/(sig*g1)-1/(sig*g2); al = 2*M
    ug = np.linspace(1e-7, 0.5-1e-7, nu); ugw = np.gradient(ug)
    xg = np.linspace(0, 1, nx)
    t = np.linspace(1e-8, 1-1e-8, nt); jac = 12/(1-t)**2; tauc = 12*t/(1-t); dt = t[1]-t[0]
    # Gamma(alpha, lam) expectation of g(tau): weight w(tau)=lam^a tau^{a-1} e^{-lam tau}/G(a) * jac; tau=12y/(lam)
    tot = 0.0
    for lo in range(0, nu, 500):
        hi = min(lo+500, nu)
        c = a+b*ug[lo:hi]; d = b*(1-2*ug[lo:hi])
        lam = c[:,None]+d[:,None]*xg[None,:]
        tau = tauc[None,None,:]/lam[:,:,None]                       # (h,nl,nt)
        lw = al*np.log(lam)[:,:,None]+(al-1)*np.log(tau)-lam[:,:,None]*tau-gammaln(al)+np.log(jac)[None,None,:]
        pw = np.exp(np.clip(lw, -700, 700))
        y = xg[None,None,None,:]
        if b >= 0:
            J = np.trapezoid((c[:,None,None,None]+d[:,None,None,None]*y)**al*np.exp(-np.clip(d[:,None,None,None]*tau[...,None]*y,0,700)), xg, axis=3)
            lJ = np.log(np.clip(J,1e-300,None))
        else:
            J = np.trapezoid((c[:,None,None,None]+d[:,None,None,None]*(1-y))**al*np.exp(-np.clip(-d[:,None,None,None]*tau[...,None]*(1-y),0,700)), 1-xg, axis=3)
            lJ = -d[:,None,None]*tau + np.log(np.clip(J,1e-300,None))
        ElnJ = (pw*lJ*dt).sum(2)/(pw*dt).sum(2)
        KL = al*np.log(lam)-al+c[:,None]*al/lam-ElnJ
        Iu = np.trapezoid(KL, xg, axis=1)
        integ = c**(-al) if abs(b) < 1e-13 else np.where(np.abs(d)>1e-8,(c**(1-al)-(c+d)**(1-al))/((al-1)*np.where(d==0,1,d)), c**(-al))
        pu = (ug[lo:hi]*(1-ug[lo:hi]))**(M-2)*(1-2*ug[lo:hi])**2*integ
        tot += (pu*np.gradient(ug[lo:hi])*Iu).sum(), pu.sum()*np.gradient(ug).mean()
    return tot[0]/tot[1]
if __name__ == "__main__":
    for M,g1,g2,sg in [(2,1.,2.,1.),(4,1.,2.,1.)]:
        pathA(M,g1,g2,sg)
        v = KLtrap(M,g1,g2,sg)
        print("M=%d g=(%g,%g): trap-path I(tau;x|u)=%.7f" % (M,g1,g2,sg,v))
    print("compare with mi_tau_100: 0.1144322 (M2), 0.2525176 (M4)")
