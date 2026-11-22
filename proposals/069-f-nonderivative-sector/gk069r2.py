# Independent GK check (069 r2): exact regulated U via mpmath expint (50 digits), example values, slopes, U_2.
import mpmath as mp
mp.mp.dps = 50
def spec(N, k):
    out = {}
    def add(lam, w):
        out[lam] = out.get(lam, 0) + w
    for l in range(N):
        L = mp.mpf(l*(l+1))
        add(L, 8*(2*l+1))            # +8 scalar (v - tau: -3 scalar from v, +8 scalar from -tau)
        add(L, -3*(2*l+1))
        add(L - k*l, 2*l+3)
        if l >= 1:
            add(L + k, 2*l+1); add(L + k*(l+1), 2*l-1)
        add(mp.mpf(l*l), -4*(2*l+2))
        if l >= 1: add(mp.mpf((l+1)**2), -4*(2*l))
    return out
def U(N, k, eps):
    s = mp.mpf(0)
    for lam, w in spec(N, k).items():
        z = eps*lam
        s += w*(mp.expint(3, z) if z > 0 else mp.mpf(1)/2)
    return s/eps**2
def moms(N, k):
    sp = spec(N, k); return [sum(w*lam**p for lam, w in sp.items()) for p in (0,1,2)]
k = mp.mpf(-0.3365)
print("moments N=16 k=-0.3365:", [mp.nstr(m, 10) for m in moms(16, k)], " (k^2-4)N^2(N^2-1)=", mp.nstr((k**2-4)*256*255, 10))
for e in (0.9, 0.5, 0.1):
    print("N=128 per N^4 eps N^2=", e, mp.nstr(U(128, k, mp.mpf(e)/128**2)/128**4, 6))
# example
r = mp.mpf('1.168241965973535'); chis = mp.sqrt(mp.mpf('0.3')); c = 2*r*chis
def P(chi, N, sL): return -chi**4*U(N, 2 - c/chi, sL*chi**2)/N**2
h = mp.mpf('1e-8')
for N in (16, 64):
    for e in (0.5,):
        sL = mp.mpf(e)/(chis**2*N**2)
        p = P(chis, N, sL); d = (P(chis*mp.e**h, N, sL) - P(chis*mp.e**-h, N, sL))/(2*h)
        print(f"N={N} e={e}: P={mp.nstr(p,6)} dP={mp.nstr(d,6)}")
# slope at large cutoff end and a few extra (off-grid) points, N=16
for e in (20, 25, 30, 40, 60, 100):
    sL = mp.mpf(e)/(chis**2*16**2)
    d = (P(chis*mp.e**h, 16, sL) - P(chis*mp.e**-h, 16, sL))/(2*h)
    print(f"N=16 e={e}: dP={mp.nstr(d,6)}")
# sign near kappa 1.9/1.95 at N=16, a few points
import itertools
for kk in (1.9, 1.92, 1.95):
    vals = [(e, U(16, mp.mpf(kk), mp.mpf(e)/256)/16**4) for e in (1e-3, 0.01, 0.1, 0.5, 1, 3, 10, 30)]
    print("kappa", kk, " ".join(f"{e}:{mp.nstr(v,3)}" for e, v in vals))
# U_2 with Hessian, theta=1, large N analytic
kap = 2 - 2*r
U2 = (2 - mp.mpf(5)/4*kap**2)*mp.mpf('0.3')
dU2 = 2*U2 + (-mp.mpf(5)/2*kap*(2*r))*mp.mpf('0.3')
print("kappa3", mp.nstr(kap,6), "U2", mp.nstr(U2,6), "dU2", mp.nstr(dU2,6), "dU2+Y", mp.nstr(dU2+7.5,6), "V/T", mp.nstr((1-r)**2,6))
print("tree slope 4*7.935+3*(-12.36)=", 4*7.935+3*(-12.36), " merged loop slope 4U4+2U2+Y=", 4*(-0.09)+2*(-0.9)+7.5)
print("r3 from tree ratio: (3/4)(12.36/7.935)=", 0.75*12.36/7.935)
