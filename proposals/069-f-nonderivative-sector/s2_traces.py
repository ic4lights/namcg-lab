"""s2: one-loop K traces on S^2_N with the cubic Hessian, kappa = 2 - c/chi (units chi = 1).

Towers (verified in s1 for the vector):
  scalar  : l(l+1), mult 2l+1
  vector  : l(l+1)-kappa*l (2l+3), l(l+1)+kappa (2l+1, l>=1), l(l+1)+kappa(l+1) (2l-1, l>=1)
  spinor  : l^2 (2l+2), (l+1)^2 (2l)      [unchanged by the cubic term]
  v = vector - 3 scalar,  tau = 4 (spinor - 2 scalar)
  That  = int ds s^-2 tau,  Vhat = int ds s^-2 v,  Uhat = int ds s^-3 (v - tau)
Closed forms (moments sum w = sum w lam = 0):
  int ds s^-2 sum w e^{-s lam} = sum w lam ln lam
  int_eps ds s^-3 sum w e^{-s lam} = -1/2 sum w lam^2 ln lam + 1/2 (sum w lam^2)(ln(1/eps) - gamma + 3/2) + O(eps)
"""
import numpy as np, mpmath as mp
EG = 0.5772156649015329

def towers(N, kap):
    sc, ve, sp = [], [], []
    for l in range(N):
        sc.append((2 * l + 1, l * (l + 1)))
        ve.append((2 * l + 3, l * (l + 1) - kap * l))
        if l >= 1:
            ve.append((2 * l + 1, l * (l + 1) + kap))
            ve.append((2 * l - 1, l * (l + 1) + kap * (l + 1)))
        sp.append((2 * l + 2, l * l))
        if l >= 1: sp.append((2 * l, (l + 1) ** 2))
    return sc, ve, sp

def wl(N, kap, which):
    sc, ve, sp = towers(N, kap)
    out = []
    if which in ("v", "v-tau"):
        out += [(w, x) for w, x in ve] + [(-3 * w, x) for w, x in sc]
    if which == "tau":
        out += [(4 * w, x) for w, x in sp] + [(-8 * w, x) for w, x in sc]
    if which == "v-tau":
        out += [(-4 * w, x) for w, x in sp] + [(8 * w, x) for w, x in sc]
    w = np.array([a for a, _ in out], float); x = np.array([b for _, b in out], float)
    return w, x

def xlogx(x, p):
    y = np.zeros_like(x); m = x > 0
    y[m] = x[m] ** p * np.log(x[m]); return y

def I2(N, kap, which):
    w, x = wl(N, kap, which); return float(np.sum(w * xlogx(x, 1)))
def mom(N, kap, which, p):
    w, x = wl(N, kap, which); return float(np.sum(w * x ** p))
def Ufin(N, kap):
    w, x = wl(N, kap, "v-tau"); return float(-0.5 * np.sum(w * xlogx(x, 2)))
def Ureg(N, kap, eps):
    return Ufin(N, kap) + 0.5 * mom(N, kap, "v-tau", 2) * (np.log(1 / eps) - EG + 1.5)

print("A. closed forms against quadrature (N=3)")
mp.mp.dps = 40
d0 = mp.mpf('1e-7')   # quadrature starts at d0 (roundoff below); the omitted piece is O(d0)
for kap in (2.0, 0.0, -0.3365):
    w, x = wl(3, kap, "v"); f = lambda s: sum(mp.mpf(float(a)) * mp.e ** (-s * mp.mpf(float(b))) for a, b in zip(w, x))
    q = mp.quad(lambda s: f(s) / s**2, [d0, 1e-3, 1, 10, mp.inf])
    print(f"  kappa={kap:+.4f}  Vhat quad={float(q):.10f} closed={I2(3,kap,'v'):.10f}")
    w, x = wl(3, kap, "v-tau"); f = lambda s: sum(mp.mpf(float(a)) * mp.e ** (-s * mp.mpf(float(b))) for a, b in zip(w, x))
    eps = mp.mpf("1e-4")
    q = mp.quad(lambda s: f(s) / s**3, [eps, 1e-2, 1, 10, mp.inf])
    print(f"               Uhat_eps quad={float(q):.8f} closed={Ureg(3,kap,1e-4):.8f}  (eps=1e-4)")

print("\nB. calibration at c=0 (kappa=2) against the merged values That/N^2->4, Vhat-That~4lnN+1.016, Uhat/N^2->1")
for N in (64, 256, 512):
    T = I2(N, 2, "tau"); V = I2(N, 2, "v")
    print(f"  N={N:4d} That/N^2={T/N**2:.6f}  Vhat-That-4lnN={V-T-4*np.log(N):.4f}  Uhat/N^2={Ufin(N,2)/N**2:.6f}  moments(v-tau) p=0,1,2: {mom(N,2,'v-tau',0):.1e} {mom(N,2,'v-tau',1):.1e} {mom(N,2,'v-tau',2):.1e}")

print("\nC. second moment with the cubic term: sum w lam^2 (v-tau) = (kappa^2-4) N^2 (N^2-1)")
for N in (5, 40):
    for kap in (2.0, 1.0, 0.0, -0.3365, -1.0):
        m2 = mom(N, kap, "v-tau", 2)
        print(f"  N={N:3d} kappa={kap:+.4f}  m2={m2:.6f}  (kappa^2-4)N^2(N^2-1)={(kap**2-4)*N**2*(N**2-1):.6f}  m0={mom(N,kap,'v-tau',0):.1e} m1={mom(N,kap,'v-tau',1):.1e}")

print("\nD. V/T with the cubic term: Vhat/That -> kappa^2/4 = (1 - c/2chi)^2 ; lowest vector eigenvalue")
print("   kappa    N    Vhat        That        Vhat/That   kappa^2/4   min vector eig")
for kap in (2.0, 1.0, 0.5, 0.0, -0.3365, -1.0, -2.0):
    for N in (64, 512):
        V = I2(N, kap, "v"); T = I2(N, kap, "tau")
        mn = min(x for _, x in towers(N, kap)[1])
        print(f"  {kap:+.4f} {N:4d} {V:12.3f} {T:12.3f}  {V/T:.6f}   {kap**2/4:.6f}   {mn:+.3f}")
print("   kappa=0 (c=2chi): v vanishes identically, Vhat = 0 exactly:", I2(100, 0.0, "v"))

print("\nE. regulated Uhat with the cubic term, eps = lower proper-time limit in units chi^-2")
print("   kappa    N    Ufin/N^4     m2/N^4      Ureg/N^4 at eps=1/N^2, 1e-2/N^2, 1e-4/N^2")
for kap in (0.0, -0.3365, 1.0, 1.9):
    for N in (64, 512):
        print(f"  {kap:+.4f} {N:4d} {Ufin(N,kap)/N**4:+.5f}  {mom(N,kap,'v-tau',2)/N**4:+.5f}   " +
              "  ".join(f"{Ureg(N,kap,e/N**2)/N**4:+.5f}" for e in (1, 1e-2, 1e-4)))
print("   sign: Ureg < 0 at eps <= 0.9/N^2 for the sampled kappa in (-1,2):",
      all(Ureg(N, k, 0.9 / N**2) < 0 for N in (16, 64, 256, 512) for k in np.linspace(-0.99, 1.9, 30)))
# largest eps*N^2 at which Ureg changes sign
for kap in (0.0, -0.3365, 1.0, 1.9):
    N = 512; m2 = mom(N, kap, 'v-tau', 2)
    e0 = np.exp(-(-Ufin(N, kap) / (0.5 * m2) + EG - 1.5))
    print(f"   kappa={kap:+.4f} N=512: Ureg=0 at eps*N^2 = {e0*N**2:.4f}")
