# mi_tau_100b.py -- item 100 CANONICAL numerics (supersedes mi_tau_100.py: that version mixed f(tau|x,u) over a
# UNIFORM x, but integrating f(tau,x|u) ~ tau^(2M-1) e^{-(c+d x) tau} over tau gives the EXACT marginal
# p(x|u) ~ (c+d x)^{-2M}; Path-A Wishart sampling in mc100b.py confirmed the true law (mean x|u=.11 = .33, not .5).
# Correct structure: x|(tau,u) ~ exp tilt e^{-d tau x} on (0,1) (the 099 rho law); tau|x,u ~ Gamma(a=2M, c+dx);
# p(x|u) = lam^{-a}/Z_u, Z_u=int_0^1 lam^{-a} dx; p(tau|u) = tau^{a-1} e^{-c tau} B(tau)/(Ga Z_u),
# B(tau)=int_0^1 e^{-d tau x} dx = (1-e^{-d tau})/(d tau).  MI(u) = E_{x|u}E_{tau|x,u}[ln f/m]
#   = (a I1 - a d Jx)/Z + lnZ - T,  I1=int lam^{-a} ln lam dx (analytic: d/dp of (c^{1-p}-(c+d)^{1-p})/((p-1)d)|p=a),
#   Jx=int x lam^{-a} dx (analytic), T = E_{x|u} E_{z~Ga(a,1)}[ln B(z/lam)]  (z-lam tau generalized Laguerre).
# Run: python -I proposals/100-g-mi-tau-conditioning-d2/mi_tau_100b.py   (~2 min)
import numpy as np
from scipy.special import roots_genlaguerre, gammaln
def lnB(s):  # ln((1-e^{-s})/s), s real nonzero array, stable; s->0 gives 0
    ap = np.abs(s); out = np.log(-np.expm1(-ap)) - np.log(np.clip(ap, 1e-300, None))
    big = ap > 50.0
    return np.where(big, -np.log(ap), out)
def run(M, g1, g2, sg, nu=1500, nz=128, nx=48, chunk=100):
    a = 1.0/(sg*g2); b = 1.0/(sg*g1)-1.0/(sg*g2); al = 2*M
    xl, wx = np.polynomial.legendre.leggauss(nx); xl, wx = 0.5*(xl+1), 0.5*wx   # x-mixing grid
    ug, wu = np.polynomial.legendre.leggauss(nu); ug, wu = 0.5*ug+0.25, 0.25*wu
    zl, wz = roots_genlaguerre(nz, al-1); wz = wz/np.exp(gammaln(al))
    c = a+b*ug; d = b*(1-2*ug); cd = c+d
    Z = np.where(np.abs(d) > 1e-14, (c**(1-al)-cd**(1-al))/((al-1)*np.where(d == 0, 1, d)), c**(-al))
    I0p = np.where(np.abs(d) > 1e-14, (c**(1-al)-cd**(1-al))/((al-1)*np.where(d == 0, 1, d)), c**(-al))
    # I1 = d/dp I(p)|al,  I(p) = (c^{1-p}-(c+d)^{1-p})/((p-1)d):
    num = np.log(c+d)*cd**(1-al) - np.log(c)*c**(1-al)
    I1 = np.where(np.abs(d) > 1e-14, (num*(al-1) - (c**(1-al)-cd**(1-al)))/((al-1)**2*d), c**(-al)*np.log(c))
    # Jx = int x lam^{-al} dx = (1/d^2)[((c+d)^{2-al}-c^{2-al})/(2-al) - c I0]
    Jx = np.where(np.abs(d) > 1e-14, ((cd**(2-al)-c**(2-al))/(2-al) - c*I0p)/d**2, c**(-al)/2)
    lam = c[:,None] + d[:,None]*xl[None,:]
    lZ = np.log(Z)
    Iu = np.empty(nu)
    for lo in range(0, nu, chunk):
        hi = min(lo+chunk, nu)
        tau = zl[None,None,:]/lam[lo:hi,:,None]
        s = d[lo:hi,None,None]*tau*1.0                      # s = d*tau = d*z/lam
        EJ = lnB(s) @ wz                                     # E_{Gamma}[ln B(tau)]
        KLx = al*np.log(lam[lo:hi]) - al*d[lo:hi,None]*xl[None,:]/lam[lo:hi] - EJ + lZ[lo:hi,None]
        wgt = lam[lo:hi]**(-al)*wx[None,:]
        Iu[lo:hi] = (wgt*KLx).sum(1)/Z[lo:hi]
    pu = (ug*(1-ug))**(M-2)*(1-2*ug)**2*Z
    pu = pu/np.dot(wu, pu)
    return np.dot(wu*pu, Iu), Iu, pu*wu, lam**(-al)*wx/Z[:,None]
if __name__ == "__main__":
    rows = [(2,1.,2.,1.),(4,1.,2.,1.),(2,1.,2.,2.),(2,2.,1.,1.),(2,1.,1.,1.),(4,1.,1.,1.)]
    for M,g1,g2,sg in rows:
        I1,_,_,_ = run(M,g1,g2,sg, nu=750, nz=96)
        I2,Iu,_,pw = run(M,g1,g2,sg)
        print("M=%d g=(%g,%g) sig=%g: I(tau;x|u)=%.7f refine=%.7f d=%.1e minx=%.5f"
              % (M,g1,g2,sg,I2,I1,abs(I2-I1),Iu.min()), flush=True)
    # structural: mean x | u-window 0.10-0.12 from the exact p(x|u) at mid-u vs sampled 0.3322 (Path A)
    M,g1,g2,sg = 2,1.,2.,1.
    _,_,_,pw = run(M,g1,g2,sg)
    _, wu = np.polynomial.legendre.leggauss(1500); ug = 0.5*np.polynomial.legendre.leggauss(1500)[0]+0.25
    print("(structural print omitted: see mc100c Path A/B for the sampled-law check)")
