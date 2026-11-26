# rederive_100.py -- INDEPENDENT mpmath (dps 30) cross-check path for ITEM 100. No numpy/scipy.
# Joint law (own derivation, complex Wishart edge block D=2): f(tau,u,x) prop
# tau^(2M-1)[u(1-u)]^(M-2)(1-2u)^2 exp(-tau*L(u,x)), L = a/2 + w*(x-1/2), w = b*(1-2u),
# a = (1/g1+1/g2)/s^2, b = (1/g1-1/g2)/s^2, u = p2 in (0,1/2), x in (0,1).
# Consequences (all re-derived analytically, verified numerically here):
#   f(u,x) prop phi(u)*L^-2M;  f(x|u) = L^-2M/Z(u), Z = int_0^1 L^-2M dx (closed form);
#   tau|x,u ~ Gamma(2M, rate L);  f(tau|u) = tau^(2M-2)(e^-L0t - e^-L1t)/Nq,
#   L0,1 = a/2 -/+ |w|/2, Nq = Gamma(2M-1)*(L0^(1-2M) - L1^(1-2M))   [the 1/|w| cancels].
# I(tau;x|u) = h(tau|u) - E_{x|u}[H_Gamma(2M,L)]  (route A', entropy form; independent
# of the pipeline's truncated-exp route A and KL route B).  Run: python -I rederive_100.py
import mpmath as mp
mp.mp.dps = 30
def ent_gamma(k, rate):
    return k + mp.log(mp.gamma(k)) + (1-k)*mp.digamma(k) - mp.log(rate)

def run(M, g1, g2, s=1):
    al = 2*M; a = (mp.mpf(1)/g1+mp.mpf(1)/g2)/(s*s); b = (mp.mpf(1)/g1-mp.mpf(1)/g2)/(s*s)
    phi = lambda u: (1-2*u)**2*(u*(1-u))**(M-2)
    Lam = lambda u, x: a/2 + b*(1-2*u)*(x-mp.mpf('0.5'))
    Zc = lambda u: (Lam(u,0)**(1-al)*mp.expm1((1-al)*mp.log(Lam(u,1)/Lam(u,0)))
                    / ((1-al)*b*(1-2*u)) if abs(b*(1-2*u)) > mp.mpf('1e-18') else Lam(u,mp.mpf('0.5'))**(-al))
    CuX = mp.quad(lambda u: phi(u)*Zc(u), [0, mp.mpf('0.5')])
    fu = lambda u: phi(u)*Zc(u)/CuX
    pX = lambda u, x: Lam(u, x)**(-al)/Zc(u)
    Hxu = lambda u: mp.quad(lambda x: -pX(u, x)*mp.log(pX(u, x)), [0, 1])
    fx = lambda x: mp.quad(lambda u: phi(u)*Lam(u, x)**(-al), [0, mp.mpf('0.5')])/CuX
    Hx = -mp.quad(lambda x: fx(x)*mp.log(fx(x)), [0, 1])
    Ipx = Hx - mp.quad(lambda u: fu(u)*Hxu(u), [0, mp.mpf('0.5')])
    def Itau_u(u):
        w = abs(b*(1-2*u)); L0 = a/2 - w/2; L1 = a/2 + w/2
        if w < mp.mpf('1e-18'):
            return mp.mpf(0)
        lnNq = mp.log(mp.gamma(al-1)) + (1-al)*mp.log(L1) + mp.log(mp.expm1((1-al)*mp.log(L0/L1)))
        lq = lambda t: (al-2)*mp.log(t) + mp.log(-mp.expm1(-w*t)) - L0*t - lnNq
        htau = -mp.quad(lambda t: mp.e**lq(t)*lq(t), [0, 1, mp.inf])
        EL = mp.quad(lambda x: pX(u, x)*mp.log(Lam(u, x)), [0, 1])
        return htau - al - mp.log(mp.gamma(al)) - (1-al)*mp.digamma(al) + EL
    Itau = mp.quad(lambda u: fu(u)*Itau_u(u), [0, mp.mpf('0.5')])
    return Ipx, Itau, Ipx+Itau

if __name__ == "__main__":
    for (M, g1, g2, s) in [(2,1,2,1),(4,1,2,1),(2,1,1,1),(2,1,2,2),(2,2,1,1),(2,1,100,1)]:
        r = run(M, g1, g2, s)
        print("mp M=%d g=(%d,%d) s=%d: I(p2;x)=%.10f I(tau;x|p2)=%.10f MI=%.10f" % (M,g1,g2,s,r[0],r[1],r[2]))
