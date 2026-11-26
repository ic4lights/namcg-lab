# mi_tau_100.py -- item 100: I(tau;x|u) for the 099 profile-class joint at D=2 via the exact u-conditional
# structure f(tau,x|u): x ~ U(0,1) exactly, tau|x,u ~ Gamma(alpha=2M, rate lam=c+d*x), c=a+beta*u,
# d=beta*(1-2u), a=1/(sig^2 g2), beta=1/(sig^2 g1)-1/(sig^2 g2). Since m_u(tau)=tau^(a-1)e^{-c tau}J(tau)/G(a),
# J(t)=int_0^1(c+dx)^a e^{-dx t}dx, the per-x KL is EXACT without digamma: KL(x)=a ln lam - a + c a/lam
# - E_{Gamma(a,lam)}[ln J(tau)]; E by generalized Gauss-Laguerre in z=lam*tau (weight z^(a-1)e^-z), lnJ by
# positive-integrand x-GL (chunked over u for memory). f_U(u) ~ [u(1-u)]^(M-2)(1-2u)^2 int_0^1(c+dx)^(-a)dx.
# Run from repo root: python -I proposals/100-g-mi-tau-conditioning-d2/mi_tau_100.py   (~2 min)
import numpy as np
from scipy.special import roots_genlaguerre, gammaln
def run(M, g1, g2, sg, nu=1500, nz=128, nl=48, nx=48, chunk=100):
    a = 1.0/(sg*g2); b = 1.0/(sg*g1)-1.0/(sg*g2); al = 2*M
    xl, wx = np.polynomial.legendre.leggauss(nx); xl, wx = 0.5*(xl+1), 0.5*wx    # x-grid for J
    xs, ws = np.polynomial.legendre.leggauss(nl); xs, ws = 0.5*(xs+1), 0.5*ws    # x-grid for KL
    ug, wu = np.polynomial.legendre.leggauss(nu); ug, wu = 0.5*ug+0.25, 0.25*wu  # u on (0,1/2)
    zl, wz = roots_genlaguerre(nz, al-1); wz = wz/np.exp(gammaln(al))            # z=lam*tau, mass 1
    c = a+b*ug; d = b*(1-2*ug)
    lam = c[:,None] + d[:,None]*xs[None,:]                                       # (nu,nl)
    Iu = np.empty(nu)
    for lo in range(0, nu, chunk):
        hi = min(lo+chunk, nu)
        tau = zl[None,None,:]/lam[lo:hi,:,None]                                  # (h,nl,nz)
        if b >= 0:   # decay in x
            arg = np.clip(d[lo:hi,None,None,None]*tau[...,None]*xl[None,None,None,:], 0, 700)
            base = (c[lo:hi,None,None,None] + d[lo:hi,None,None,None]*xl[None,None,None,:])**al
            adj = 0.0
        else:        # d<0: reflect x->1-x so the exponent decays; J = e^{d tau} int (c+d-dy)^a e^{d tau y} dy
            y = 1.0-xl
            arg = np.clip(-d[lo:hi,None,None,None]*tau[...,None]*y[None,None,None,:], 0, 700)
            base = (c[lo:hi,None,None,None] + d[lo:hi,None,None,None]*(1.0-y[None,None,None,:]))**al
            adj = -d[lo:hi,None,None]*tau
        lJ = adj + np.log(np.clip(np.einsum('kmlx,x->kml', base*np.exp(-arg), wx), 1e-300, None))
        EJ = lJ @ wz
        KLx = al*np.log(lam[lo:hi]) - al + c[lo:hi,None]*al/lam[lo:hi] - EJ      # (h,nl) per-x KL
        Iu[lo:hi] = KLx @ ws
    if abs(b) < 1e-13:
        integ = c**(-al)
    else:
        integ = np.where(np.abs(d) > 1e-8, (c**(1-al)-(c+d)**(1-al))/((al-1)*np.where(d == 0, 1, d)), c**(-al))
    pu = (ug*(1-ug))**(M-2)*(1-2*ug)**2*integ
    pu = pu/np.dot(wu, pu)
    return np.dot(wu*pu, Iu), Iu, pu*wu
if __name__ == "__main__":
    rows = [(2,1.,2.,1.),(4,1.,2.,1.),(2,1.,2.,2.),(2,2.,1.,1.),(2,1.,1.,1.),(4,1.,1.,1.)]
    for M,g1,g2,sg in rows:
        I1,_,_ = run(M,g1,g2,sg, nu=750, nz=96)
        I2,Iu,_ = run(M,g1,g2,sg)
        print("M=%d g=(%g,%g) sig=%g: I(tau;x|u)=%.7f refine=%.7f d=%.1e minx=%.5f"
              % (M,g1,g2,sg,I2,I1,abs(I2-I1),Iu.min()))
    print("expect: cv rows I=0 to quadrature noise; sig=2 and swap rows equal M=2 g=(1,2) sig=1")
