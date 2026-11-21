# Proposal 056 r1, script 1: contour windows, slice eigenvalue identities,
# pointwise bounds, branch closed forms. Run: python -I bridge_r1.py
# Checks compare INDEPENDENT computations (matrix eigenvalues vs Pauli
# contraction, closed form vs 60-term series, exact constants vs numeric min).
import mpmath as mp
import sympy as sp
mp.dps = 30

def hdr(t):
    print("=" * 70)
    print(t)
    print("=" * 70)

# ---------------------------------------------------------------- SEC 1
hdr("SEC 1: regulator/delta real-part windows along R_theta; lambda_* = sqrt(2+sqrt2)")
th = sp.symbols('theta', real=True)
lam = sp.symbols('lam', positive=True)
rA0 = sp.simplify(sp.re(sp.exp(-3*sp.I*sp.pi*th/4)))          # Re A0(theta)^2
rAi = sp.simplify(sp.re(sp.exp(sp.I*sp.pi*th/4)))
dA0 = sp.simplify(sp.re(sp.expand_trig(sp.exp(3*sp.I*sp.pi/8)*sp.exp(-3*sp.I*sp.pi*th/4))))
dAi = sp.simplify(sp.re(sp.expand_trig(sp.exp(-sp.I*sp.pi/8)*sp.exp(sp.I*sp.pi*th/4))))
print("Re A0^2 =", rA0, "   Re Ai^2 =", rAi)
print("Re e^{3pi i/8}A0^2 =", dA0, "   Re e^{-pi i/8}Ai^2 =", dAi)
c0 = sp.simplify(rA0 + lam*dA0)
c1 = sp.simplify(rAi + lam*dAi)
f0 = sp.lambdify((th, lam), c0, 'mpmath')
f1 = sp.lambdify((th, lam), c1, 'mpmath')
lstar = sp.sqrt(2 + sp.sqrt(2))
print("lambda_* closed form sqrt(2+sqrt2) =", mp.nstr(float(lstar), 15))
for L in (mp.mpf('1.5'), lstar - 1e-9, lstar + 1e-9, mp.mpf('2'), mp.mpf('10')):
    ts = [mp.mpf(j)/1000 for j in range(1001)]
    m0 = min(f0(t, L) for t in ts)
    m1 = min(f1(t, L) for t in ts)
    print("lam=%12s: min c0=%12s  min c1=%12s" % (mp.nstr(L, 10), mp.nstr(m0, 10), mp.nstr(m1, 10)))
# verify the closed-form location of the c0 minimum at theta=1 for lam > lambda_*
d0 = sp.simplify(sp.diff(c0, th).subs(th, 1))
print("d/dtheta c0 at theta=1 (lam=2):", mp.nstr(float(d0.subs(lam, 2)), 10), "(<0: min at right end)")

# ---------------------------------------------------------------- SEC 2
hdr("SEC 2: N=2 slice: eigenvalue difference (matrix side) vs Pauli contraction, at R_1")
s1 = mp.matrix([[0, 1], [1, 0]])
s2 = mp.matrix([[0, 1j], [-1j, 0]])
s3 = mp.matrix([[1, 0], [0, -1]])
import random
def rho2_matrix(w):
    M = (w[0]*s1 + w[1]*s2 + w[2]*s3)/2
    tr = M[0, 0] + M[1, 1]
    det = M[0, 0]*M[1, 1] - M[0, 1]*M[1, 0]
    e1 = (tr + mp.sqrt(tr*tr - 4*det))/2
    e2 = (tr - mp.sqrt(tr*tr - 4*det))/2
    return (e1 - e2)**2
maxdev = mp.mpf(0)
for seed in range(6):
    rnd = random.Random(seed)
    r = [mp.mpc(rnd.uniform(-2, 2)) for _ in range(4)]           # r^mu REAL (slice)
    a = [[mp.mpc(rnd.uniform(-2, 2)) for _ in range(4)] for _ in range(3)]  # tilde A^a_mu REAL Pauli comps
    for aa in range(3):
        for mu in range(4):
            a[aa][mu] = mp.re(a[aa][mu])                          # Hermitian tilde A
    # on R_1 slice: k^mu A_mu(1) = r^mu tilde A_mu : w^a = sum r^mu a^a_mu (real)
    w = [sum(r[mu]*a[aa][mu] for mu in range(4)) for aa in range(3)]
    rho2m = rho2_matrix(w)
    rho2c = sum(w[aa]**2 for aa in range(3))
    maxdev = max(maxdev, abs(rho2m - rho2c)/max(abs(rho2m), abs(rho2c)))
    assert abs(mp.im(rho2m)) < 1e-25 and mp.re(rho2m) >= -1e-25
print("slice rho_X^2: max rel dev matrix-vs-contraction over 6 trials:", mp.nstr(maxdev, 5), "(real, >=0 asserted)")
# m5: deterministic off-slice contrast exhibiting |O_k| > 2 at u=0 fields: k=(0,2i,0,0),
# A^1_1 = 2 only: w^1 = 4i, rho_X^2 = -16, rho_X = 4i, |O_k| = 2 cosh(2) = 7.524 > 2.
kk = [mp.mpc(0), mp.mpc(0, 2), mp.mpc(0), mp.mpc(0)]
aa2 = [[mp.mpc(0)]*4 for _ in range(3)]
aa2[0][1] = mp.mpf(2)
w2 = [sum(kk[mu]*aa2[aa][mu] for mu in range(4)) for aa in range(3)]
rho2b = rho2_matrix(w2)
Omb = abs(2*mp.cos(mp.sqrt(rho2b)/2))
print("off-slice k=(0,2i,0,0), A^1_1=2: rho_X^2 =", mp.nstr(rho2b, 6), " |O_k| =", mp.nstr(Omb, 8), "> 2:", Omb > 2)

# ---------------------------------------------------------------- SEC 3
hdr("SEC 3: pointwise slice modulus: cosh bound and the ray lower bound e^{b rho/2}/(2sqrt2)")
def Omod_ray(u, rho, r0=mp.mpf(1), y=mp.mpf(0)):
    q = (mp.exp(3j*mp.pi*(1-u)/8)*r0*rho + mp.exp(-1j*mp.pi*(1-u)/8)*y)**2
    return abs(2*mp.cos(mp.sqrt(q)/2))
print("u    rho   |O| ray        lower bound    ok")
for u in (mp.mpf('0'), mp.mpf('0.3'), mp.mpf('0.6')):
    b = mp.sin(3*mp.pi*(1-u)/8)
    for rho in (10, 30):
        Om = Omod_ray(u, rho)
        lb = mp.e**(b*rho/2)/(2*mp.sqrt(2))
        print("%.1f %5d  %s  %s  %s" % (u, rho, mp.nstr(Om, 8), mp.nstr(lb, 8), Om >= lb))
# 2cosh(b/2) envelope of |O| for general slice data (x = r0 A0vec, y = r.Avec), see derivation
for u in (mp.mpf('0.5'), mp.mpf('1')):
    x = [mp.mpf('1.5'), mp.mpf('-0.4'), mp.mpf('0.2')]
    y = [mp.mpf('2.0'), mp.mpf('0.5'), mp.mpf('-1.0')]
    q = sum((mp.exp(3j*mp.pi*(1-u)/8)*xx + mp.exp(-1j*mp.pi*(1-u)/8)*yy)**2 for xx, yy in zip(x, y))
    b2 = (abs(q) - mp.re(q))/2
    Om = abs(2*mp.cos(mp.sqrt(q)/2))
    print("u=%s |O|=%s <= 2cosh(sqrt(b2)/2)=%s : %s" % (u, mp.nstr(Om, 8), mp.nstr(2*mp.cosh(mp.sqrt(max(b2,0))/2), 8), Om <= 2*mp.cosh(mp.sqrt(max(b2,0))/2)+1e-25))

# ---------------------------------------------------------------- SEC 4
hdr("SEC 4: branch closed form vs 60-term series (055 formula re-check, incl gamma terms)")
def branch_cf(Q, gc):
    return 2*mp.sqrt(mp.pi/Q)*mp.exp(-gc**2/(4*Q))
def branch_series(Q, gc, J=80):
    s = mp.mpc(0)
    for j in range(J):
        s += 2*((-1)**j)*gc**(2*j)/mp.factorial(2*j)*mp.sqrt(mp.pi)*mp.factorial(2*j)/(mp.factorial(j)*4**j)*Q**(-(j+mp.mpf(1)/2))
        if abs(s) != 0 and abs(2*gc**(2*j)/mp.factorial(2*j)*mp.sqrt(mp.pi)*mp.factorial(2*j)/(mp.factorial(j)*4**j)*Q**(-(j+mp.mpf(1)/2))) < 1e-28*abs(s):
            return s, j
    return s, J
for u in (mp.mpf('0'), mp.mpf('0.2'), mp.mpf('0.3'), mp.mpf('0.5')):
    for eps, gam in ((mp.mpf('0.02'), mp.mpf(0)), (mp.mpf('0.002'), mp.mpf(0)), (mp.mpf('0.002'), mp.mpf('-0.05'))):
        al = 3*mp.pi*u/8
        Q = mp.exp(-2j*al)*(eps - 1j*gam/2)
        gc = mp.exp(3j*mp.pi/8)/2
        cf = branch_cf(Q, gc)
        se, nj = branch_series(Q, gc)
        print("u=%.1f eps=%.3g gam=%s: |cf|=%s reldev(series after %d terms)=%s" % (u, eps, gam, mp.nstr(abs(cf), 10), nj, mp.nstr(abs(cf-se)/abs(cf), 3)))
# growth/saturation exponents (merged text) reproduced from the closed form
for u in (mp.mpf('0'), mp.mpf('0.3'), mp.mpf('0.6')):
    eps = mp.mpf('1e-6')
    al = 3*mp.pi*u/8
    Q0 = mp.exp(-2j*al)*eps
    gc = mp.exp(3j*mp.pi/8)/2
    g0 = mp.re(-gc**2/(4*Q0))/ (1/eps)
    Qg = mp.exp(-2j*al)*(eps - 1j*mp.mpf('-0.05')/2)
    gs = mp.re(-gc**2/(4*Qg))
    print("u=%.1f: growth*eps=%s (text cos(3pi u/4 - pi/4)/16=%s) ; sat=%s (text sin(3pi u/4 - pi/4)/(8|gam|)=%s)" %
          (u, mp.nstr(g0, 8), mp.nstr(mp.cos(3*mp.pi*u/4 - mp.pi/4)/16, 8), mp.nstr(gs, 8), mp.nstr(mp.sin(3*mp.pi*u/4 - mp.pi/4)/0.4, 8)))

# ---------------------------------------------------------------- SEC 5
hdr("SEC 5: damped-vs-undamped 1D branch model: exact linking failure")
# I(eps)=2 sqrt(pi/eps) e^{-gc^2/(4 eps)} ; J = same with Qd = eps(1+lam cos(3pi/8)) (u=0 Stokes damping)
gc2 = (mp.exp(3j*mp.pi/8)/2)**2
for lamv in (mp.mpf('2'), mp.mpf('10'), mp.mpf('1000')):
    line = "lam=%6s:" % lamv
    for e in (mp.mpf('0.02'), mp.mpf('0.01'), mp.mpf('0.005')):
        Qd = e*(1 + lamv*mp.cos(3*mp.pi/8))
        I = abs(branch_cf(e, mp.exp(3j*mp.pi/8)/2))
        Jv = abs(branch_cf(Qd, mp.exp(3j*mp.pi/8)/2))
        line += "  eps=%.3g |J|/|I|=%s" % (e, mp.nstr(Jv/I, 6))
    print(line)
# the required link |I-J| -> 0 fails since |J|/|I| -> 0 and |I| -> oo: |I-J|/|I| -> 1
print("=> |I-J| ~ |I| = exp(sqrt2/(32 eps))/sqrt(eps) -> oo : linking error is exponentially large")
print("DONE")
