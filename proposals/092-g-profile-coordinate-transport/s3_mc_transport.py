# s3_mc_transport.py - seeded Monte Carlo end-to-end check:
# (A) draw slots with means s^2 g_i, form charge moments m_{2p}=2*4^p E[T^p] (T=|w|^2, leading-order
#     convention), extract rho_p = 2^{p-1} m_{2p}/m_2^p, reconstruct the profile by the s2 recursion,
#     compare to the true sorted profile;
# (B) draw p from the FLAT simplex law, apply tau_g, check the histogram statistics of the image
#     against the 089 pushforward density via exact numerical quadrature of its P_2 statistic.
# Run: python -I proposals/092-g-profile-coordinate-transport/s3_mc_transport.py
import random, math
import mpmath as mp
mp.mp.dps = 25
random.seed(920)

fails = []
def chk(name, cond):
    print(("OK  " if cond else "FAIL") + " " + name)
    if not cond:
        fails.append(name)

# ---------- (A) charge-moment reconstruction ----------
D = 3
gt = [1.0, 0.5, 2.0]           # general non-uniform profile, W = 3.5
s2 = 0.37                      # variance parameter, will cancel in rho
N = 2000000
W = sum(gt)
m2 = 0.0; m4 = 0.0; m6 = 0.0
for _ in range(N):
    T = sum(-s2 * gt[i] * math.log(random.random()) for i in range(D))
    m2 += T; m4 += T*T; m6 += T**3
m2 *= 8.0/N                    # m_2 = 2*4^1*E[T]
m4 *= 32.0/N                  # m_4 = 2*4^2*2!*E[T^2]
m6 *= 128.0/N                 # m_6 = 2*4^3*3!*E[T^3]
r2 = 2**(2-1)*m4/m2**2         # rho_2
r3 = 2**(3-1)*m6/m2**3         # rho_3
hh = {0: 1.0, 1: 1.0}
hh[2] = r2/2.0
hh[3] = r3/6.0
sig = {1: 1.0}
for k in (2, 3):
    sig[k] = k*hh[k] - sum(sig[i]*hh[k-i] for i in range(1, k))
e = {0: 1.0}
for k in (1, 2, 3):
    e[k] = sum((-1)**(i-1)*e[k-i]*sig[i] for i in range(1, k+1))/k
rts = sorted(mp.polyroots([e[0], -e[1], e[2], -e[3]]))  # monic, ascending coeffs c0..c3
want = sorted(v/W for v in gt)
err = max(abs(a-b) for a, b in zip(rts, want))
# exact reference rho values via the same recursion on true power sums
ps = {k: sum(v**k for v in gt) for k in (1, 2, 3)}
hx = {0: 1.0}
for k in (1, 2, 3):
    hx[k] = sum(ps[i]*hx[k-i] for i in range(1, k+1))/k
print("   empirical rho_2 = %.5f (exact %.5f), rho_3 = %.5f (exact %.5f)" % (
    r2, 2*hx[2]/W**2, r3, 6*hx[3]/W**3))
print("   reconstructed profile/W:", [float(x) for x in rts], " target:", want, " max err %.2e" % err)
chk("(A) profile reconstructed from empirical charge moments (err<5e-3)", err < 5e-3)

# ---------- (B) transport of the flat law by tau_g ----------
# exact reference: E_{mu_g}[P_2], P_2 = sum p_i^2, by quadrature of the 089 density at D=3
gg = [1.0, 0.5, 2.0]
def dens(p1, p2):
    p3 = 1 - p1 - p2
    if p3 <= 0: return mp.mpf('0')
    G = gg[0]*gg[1]*gg[2]
    Lam = p1/gg[0] + p2/gg[1] + p3/gg[2]
    return 2/(G*Lam**3)
def E_P2_exact():
    f = lambda p2: mp.quad(lambda p1: (p1*p1 + p2*p2 + (1-p1-p2)**2)*dens(p1, p2), [0, 1-p2])
    return mp.quad(f, [0, 1])
# MC: flat Dirichlet(1,1,1) samples via normalized exponentials, apply tau_g
M = 400000
acc = 0.0; acc2 = 0.0
for _ in range(M):
    e1, e2, e3 = (-math.log(random.random()) for _ in range(3))
    tt = e1+e2+e3
    q = [e1/tt, e2/tt, e3/tt]
    S = gg[0]*q[0] + gg[1]*q[1] + gg[2]*q[2]
    p = [gg[i]*q[i]/S for i in range(3)]
    P2 = sum(x*x for x in p)
    acc += P2; acc2 += P2*P2
emp = acc/M
se = math.sqrt(acc2/M - emp*emp)/math.sqrt(M)
ref = E_P2_exact()
print("   E[P_2] empirical %.6f +- %.6f (1se), quadrature %.6f" % (emp, se, ref))
chk("(B) flat --tau_g--> law matches 089 density at the P_2 statistic (3 sigma)", abs(emp-ref) < 3*se)

# also mean of p_1: MC vs quadrature
acc = 0.0
for _ in range(200000):
    e1, e2, e3 = (-math.log(random.random()) for _ in range(3))
    tt = e1+e2+e3
    q = [e1/tt, e2/tt, e3/tt]
    S = gg[0]*q[0] + gg[1]*q[1] + gg[2]*q[2]
    acc += gg[0]*q[0]/S
ref1 = mp.quad(lambda p2: mp.quad(lambda p1: p1*dens(p1, p2), [0, 1-p2]), [0, 1])
emp1 = acc/200000
print("   E[p_1] empirical %.6f, quadrature %.6f" % (emp1, ref1))
chk("(B) E[p_1] transport vs quadrature (1e-3)", abs(emp1-ref1) < 1e-3)

print("S3:", "PASS" if not fails else "FAIL " + str(fails))
