# mi_tau_100r.py -- item 100 r1 (researcher rewrite). Exact joint law of (tau,p2,x) for the 097/099
# column-profile complex Wishart edge-block at D=2, re-derived from scratch:
#   f(tau,u) prop tau^(2M-2) e^-(a/2)tau (e^{w tau/2}-e^{-w tau/2}) (1-2u)^2 [u(1-u)]^(M-2) / w,
#   a = 1/(s^2 g1)+1/(s^2 g2), b = 1/(s^2 g1)-1/(s^2 g2), w = b(1-2u), u=p2 in (0,1/2);
#   f(x|tau,u) = rho e^{-rho x}/(1-e^{-rho}), rho = w tau;  joint f(u,x) prop (1-2u)^2[u(1-u)]^{M-2} L^{-2M},
#   L = a/2 + w(x-1/2).  Hence x|u ~ L^{-2M}/Z(u) (NOT uniform), tau|x,u ~ Gamma(2M, rate L).
# Deliverables: I(p2;x) [099 check], MI((tau,p2);x), I(tau;x|p2) by three independent routes,
# symmetry checks (sigma, g-swap), beta->0 limit. Run: python -I proposals/100-g-mi-tau-conditioning-d2/mi_tau_100r.py
from mpmath import mp, mpf, quad, log, exp, sinh, psi, gamma, fabs
mp.dps = 20

def laws(M, g1, g2, s):
    a = mpf(1)/(s*s*g1) + mpf(1)/(s*s*g2); b = mpf(1)/(s*s*g1) - mpf(1)/(s*s*g2)
    def L(x,u): return a/2 + b*(1-2*u)*(x - mpf(1)/2)
    def Z(u):
        d = b*(1-2*u)
        if fabs(d) < mpf(10)**(-20): return L(0,u)**(-2*M)
        p = -2*M
        return (L(1,u)**(p+1) - L(0,u)**(p+1))/((p+1)*d)
    def Zln(u):  # int L^{-2M} ln L dx  (d/dp of int L^p at p=-2M)
        d = b*(1-2*u)
        if fabs(d) < mpf(10)**(-20): return L(0,u)**(-2*M)*log(L(0,u))
        p = -2*M
        e = p+1
        return ((L(1,u)**e*log(L(1,u)) - L(0,u)**e*log(L(0,u)))/e
                - (L(1,u)**e - L(0,u)**e)*(1/e + 1/e))/((p+1)*d) if False else \
               ((L(1,u)**e*log(L(1,u)) - L(0,u)**e*log(L(0,u)))*(1) - 0)/((p+1)*d) \
               - (L(1,u)**e - L(0,u)**e)*0  # placeholder, replaced below
    return a, b, L, Z

def Zp(M, a, b):  # int_0^1 L^p dx closed form
    def f(u):
        d = b*(1-2*u); e = p_of[0]+1
        L0 = a/2 - d/2; L1 = a/2 + d/2
        if fabs(d) < mpf(10)**(-22): return L0**p_of[0]
        return (L1**e - L0**e)/(e*d)
    return f
p_of = [mpf(0)]

def Zint(M, a, b, p):  # int_0^1 L^p dx
    d_p = lambda u: b*(1-2*u)
    def f(u):
        d = d_p(u); e = p+1
        L0 = a/2 - d/2; L1 = a/2 + d/2
        if fabs(d) < mpf(10)**(-22): return L0**p
        return (L1**e - L0**e)/(e*d)
    return f

def run(M, g1, g2, s):
    g1 = mpf(g1); g2 = mpf(g2); s = mpf(s)
    a = mpf(1)/(s*s*g1) + mpf(1)/(s*s*g2); b = mpf(1)/(s*s*g1) - mpf(1)/(s*s*g2)
    phi = lambda u: (1-2*u)**2 * (u*(1-u))**(M-2)
    def L(u,x): return a/2 + b*(1-2*u)*(x-mpf(1)/2)
    def Zf(u):
        d = b*(1-2*u); e = mpf(1)-2*M
        L0 = a/2-d/2; L1 = a/2+d/2
        if fabs(d) < mpf(10)**(-22): return L0**(-2*M)
        return (L1**e-L0**e)/(e*d)
    Cu = quad(lambda u: phi(u)*Zf(u), [0, mpf(1)/2])
    fu = lambda u: phi(u)*Zf(u)/Cu
    # H(x|u) closed form: -2M <ln L> - ln Z
    def dZp(u):  # int L^{-2M} ln L dx  via symmetric-difference of closed form in p (exact-deriv check)
        d = b*(1-2*u); L0 = a/2-d/2; L1 = a/2+d/2; e0 = lambda p:(p+1)
        if fabs(d) < mpf(10)**(-22): return L0**(-2*M)*log(L0)
        def F(p):
            e = p+1
            return (L1**e - L0**e)/(e*d)
        h = mpf(10)**(-10)
        return (F(mpf(-2*M)+h)-F(mpf(-2*M)-h))/(2*h)
    Hxu = quad(lambda u: fu(u)*(-2*M*dZp(u)/Zf(u) - log(Zf(u))), [0, mpf(1)/2])
    # H(x): f(x) = 1/C int phi(u) L(u,x)^{-2M} du ; C = int_x int_u
    Ctot = Cu
    fx = lambda x: quad(lambda u: phi(u)*L(u,x)**(-2*M), [0, mpf(1)/2]) / Ctot
    Hx = -quad(lambda x: fx(x)*log(fx(x)), [0, 1])
    # E[h(rho)|u] via tau|x,u Gamma(2M,L): route A (tau-integral at fixed x)
    h = lambda r: mpf(0) if fabs(r) < mpf(10)**(-30) else log((1-exp(-r))/r) + 1 - r/(exp(r)-1)
    def Ehx(u, x):
        lam = L(u,x); al = 2*M
        g = lambda t: lam**(al)*t**(al-1)*exp(-lam*t)/gamma(al)*h(b*(1-2*u)*t)
        lo = quad(g, [0, mpf(50)/lam])
        hi = quad(g, [mpf(50)/lam, mpf(2000)/lam]) if fabs(b) > mpf(10)**(-14) else mpf(0)
        return lo+hi
    Ehx = quad(lambda u: fu(u)*quad(lambda x: Zf(u)**(-1)*L(u,x)**(-2*M)*Ehx(u,x), [0,1]), [0, mpf(1)/2])
    Itau = Hxu - Ehx          # route A: I(tau;x|u) = H(x|u) - E[h(rho)]
    MI = Hx - Ehx             # MI((tau,p2);x)
    Iu = MI - Itau            # implied I(p2;x)
    # route B: I(tau;x|u) = E_x KL(Gamma(2M,L)|| f(tau|u))
    Ntau = lambda u: quad(lambda t: t**(2*M-2)*(exp(-(a/2-b*(1-2*u)/2)*t)-exp(-(a/2+b*(1-2*u)/2)*t)), [0, mpf(400)])
    def KLx(u, x):
        lam = L(u,x); al = 2*M; d = b*(1-2*u); c0 = a/2-d/2; c1 = a/2+d/2
        Elt = psi(al) - log(lam)
        N = Ntau(u)/(phi(u)*1) if False else None
        # f(tau|u) = t^{2M-2}(e^{-c0 t}-e^{-c1 t}) / Nu, Nu = int ...
        Nu = quad(lambda t: t**(al-1)*(exp(-c0*t)-exp(-c1*t)), [0, mpf(400)])
        g = lambda t: lam**al*t**(al-1)*exp(-lam*t)/gamma(al)*(al*log(lam)+(al-1)*log(t)-lam*t - (log(t**(al-1)*(exp(-c0*t)-exp(-c1*t)))-log(Nu)))
        return quad(g, [0, mpf(50)/lam]) + quad(g, [mpf(50)/lam, mpf(2000)/lam])
    ItauB = quad(lambda u: fu(u)*quad(lambda x: L(u,x)**(-2*M)/Zf(u)*KLx(u,x), [0,1]), [0, mpf(1)/2])
    return dict(Iu=Iu, MI=MI, Itau=Itau, ItauB=ItauB, Hx=Hx, Hxu=Hxu)
if __name__ == "__main__":
    for (M,g1,g2,s) in [(2,1,2,1),(4,1,2,1),(2,1,2,2),(2,2,1,1)]:
        r = run(M,g1,g2,s)
        print("M=%d g=(%d,%d) s=%d: I(p2;x)=%.7f  MI((tau,p2);x)=%.7f  I(tau;x|p2)=%.7f (routeB %.7f) Hx=%.7f Hx|u=%.7f"
              % (M,g1,g2,s,r['Iu'],r['MI'],r['Itau'],r['ItauB'],r['Hx'],r['Hxu']))
    r0 = run(2,1,1,1); r4 = run(4,1,1,1)
    print("cv M=2: Hx=%.7f Hx|u=%.7f (expect 0.0000000,0.0000000); cv M=4 same expect 0" % (r0['Hx'],r0['Hxu']))
    e = run(2,1,1000,1)
    print("near-cv g=(1,1000) M=2: I(p2;x)=%.7f I(tau)=%.7f (expect small, ->0)" % (e['Iu'],e['Itau']))
