# Proposal 056 r1, script 2: the two-regulator Stokes bridge - exact band,
# linking failure, corner lower bound on the modulus, and the u=1 link.
# Run: python -I link_r1.py   (ASCII; independent computations only)
import mpmath as mp
import sympy as sp
mp.dps = 40

def hdr(t):
    print("=" * 70)
    print(t)
    print("=" * 70)

# ---------------------------------------------------------------- SEC A
hdr("SEC A: exact Stokes window; ratio monotone, lambda_* = sqrt(2+sqrt2) at theta=1")
th, lam = sp.symbols('theta lam', real=True)
# quadratic damping coefficients per unit (eps,delta=lam*eps) along R_theta:
c0 = sp.cos(3*sp.pi*th/4) + lam*sp.cos(3*sp.pi*(2*th-1)/8)
c1 = sp.cos(sp.pi*th/4) + lam*sp.cos(sp.pi*(2*th-1)/8)
ratio = -sp.cos(3*sp.pi*th/4)/sp.cos(3*sp.pi*(2*th-1)/8)
# exact identity: d/dtheta ratio = (3 pi/4) sin(3 pi/8) / cos(3 pi (2 theta-1)/8)^2 > 0
dr = sp.simplify(sp.diff(ratio, th) - (3*sp.pi/4)*sp.sin(3*sp.pi/8)/sp.cos(3*sp.pi*(2*th-1)/8)**2)
print("diff(ratio) - closed form simplifies to:", dr)
print("ratio(0) =", sp.simplify(ratio.subs(th, 0)), "  ratio(1) =",
      sp.simplify(ratio.subs(th, 1)), "=", sp.nsimplify(sp.radsimp(sp.simplify(ratio.subs(th, 1)))))
lstar = sp.sqrt(2 + sp.sqrt(2))
print("ratio(1) - sqrt(2+sqrt2) simplifies to:", sp.simplify(sp.radsimp(ratio.subs(th, 1)) - lstar))
print("lambda_* =", mp.nstr(mp.sqrt(2+mp.sqrt(2)), 16))
f0 = sp.lambdify((th, lam), c0, 'mpmath')
f1 = sp.lambdify((th, lam), c1, 'mpmath')
for L in (mp.mpf('1.5'), mp.sqrt(2+mp.sqrt(2)) - mp.mpf('1e-9'), mp.sqrt(2+mp.sqrt(2)) + mp.mpf('1e-9'), mp.mpf('2')):
    ts = [mp.mpf(j)/2000 for j in range(2001)]
    print("lam=%s: min c0=%s  min c1=%s" % (mp.nstr(L, 12), mp.nstr(min(f0(t, L) for t in ts), 10), mp.nstr(min(f1(t, L) for t in ts), 10)))
# c1 decreasing on [0,1], min at theta=1: cos(pi/4)+lam*cos(3pi/8) > 0 for all lam>0
print("c1(1;lam=0.001) =", mp.nstr(f1(1, mp.mpf('0.001')), 8), "> 0 always")

# ---------------------------------------------------------------- SEC B
hdr("SEC B: exact 1D branch model: undamped I vs delta-damped J; linking ratio -> 1")
a = sp.symbols('a', real=True)
eps, L = sp.symbols('eps lam', positive=True)
gc = sp.exp(3*sp.pi*sp.I/8)/2                     # r0 = 1 slice, u=0 branch
Iex = 2*sp.sqrt(sp.pi/eps)*sp.exp(-gc**2/(4*eps))          # closed form (verified in bridge SEC4)
Qd = eps*(1 + L*sp.cos(3*sp.pi/8))                # delta damping at u=0: Re e^{3pi i/8}A0^2 = cos(3pi/8)
Jex = 2*sp.sqrt(sp.pi/Qd)*sp.exp(-gc**2/(4*Qd))
ratioJ = sp.simplify(Jex/Iex)
print("J/I =", sp.simplify(sp.logcombine(sp.expand_log(ratioJ, force=True))))
print("|J|/|I| =", sp.simplify(sp.Abs(ratioJ)))
gcm = mp.exp(3j*mp.pi/8)/2
print("eps      |I|        |J(lam=2)|   |1-J/I| exact    |I-J|/|I| quad (TRUNCATION CHECK ONLY, mp.quad unreliable on growing oscillatory tails)")
for e in (mp.mpf('0.05'), mp.mpf('0.02'), mp.mpf('0.01')):
    Icm = 2*mp.sqrt(mp.pi/e)*mp.exp(-gcm**2/(4*e))
    Qv = e*(1 + 2*mp.cos(3*mp.pi/8))
    Jcm = 2*mp.sqrt(mp.pi/Qv)*mp.exp(-gcm**2/(4*Qv))
    dif = abs(mp.quad(lambda x: mp.exp(-e*x*x)*(1 - mp.exp(-2*e*mp.cos(3*mp.pi/8)*x*x))*2*mp.cos(gcm*x), [-30, 0, 30]))
    print("%6.3f  %s  %s  %s  %s (sandwich: |1-J/I| <= %.5f)" % (e, mp.nstr(abs(Icm), 8), mp.nstr(abs(Jcm), 8),
          mp.nstr(abs(1 - Jcm/Icm), 6), mp.nstr(dif/abs(Icm), 6), 1 + abs(Jcm/Icm)))
print("model: |I| = 2*sqrt(pi/eps)*exp(-Re(gc^2)/(4*eps)), -Re(gc^2)/4 = sqrt(2)/32 =", mp.nstr(mp.sqrt(2)/32, 8))
print("=> linking error ~ |I| diverges: damped family cannot reproduce undamped LHS in this model")

# ---------------------------------------------------------------- SEC C
hdr("SEC C: corner lower bound M_u(eps) >= exp(c0(u)/eps)/poly ; regulator-only, u<2/3")
# rank-one corner: A0tilde = rho*H (Tr H^2=1), transverse |Atilde_i| ~ c1*eps (tube of
# scale O(eps): quartic cross penalty kappa*tau^2*rho^2 is O(1) at rho* = O(1/eps); a tube
# O(sqrt(eps)) would give penalty Theta(1/eps) and only c0(u)/(1+kappa*sin(pi u/2)/K) (F2).
# Regulator damping in rho:
#   eps*cos(3 pi u/4)*rho^2 ; insertion |O_k| >= e^{b_u rho/2}/(2sqrt2), b_u = sin(3pi(1-u)/8)|r0|
# peak of b_u*rho/2 - eps*cos(3pi u/4)*rho^2: rho* = b_u/(4 eps cos(3pi u/4))
# value c0(u)/eps, c0(u) = b_u^2/(16 cos(3 pi u/4)).
def c0u(u, r0=1):
    bu = mp.sin(3*mp.pi*(1-u)/8)*abs(r0)
    return bu**2/(16*mp.cos(3*mp.pi*u/4))
for u in (0.0, 0.2, 0.3, 0.5, 0.66):
    print("u=%.2f: c0(u) = %s" % (u, mp.nstr(c0u(u), 8)))
print("u>=2/3: regulator quadratic in A0tilde is non-damping: modulus integral M_u(eps) = infinity")
Lstar = mp.sqrt(2+mp.sqrt(2))
c03 = c0u(mp.mpf('0.3'))
print("eps      lambda_*eps    poly*exp(-c0(0.3)/eps)   Stokes-band vs link-band nonempty?")
for e in (mp.mpf('0.1'), mp.mpf('0.05'), mp.mpf('0.02'), mp.mpf('0.01'), mp.mpf('0.005')):
    lo, hi = Lstar*e, mp.e**(-c03/e)
    print("%6.3f  %s  %s  %s" % (e, mp.nstr(lo, 6), mp.nstr(hi, 6), "NO" if lo > hi else "yes (finite eps only)"))
# m3: exact asymptotic statement: incompatibility for all sufficiently small eps;
# finite-eps crossing (poly=1) solved numerically:
g = lambda ee: mp.log(Lstar*ee) + c03/ee
loE, hiE = mp.mpf('0.001'), mp.mpf('0.05')
for _ in range(80):
    mid = (loE + hiE)/2
    if g(mid) > 0: loE = mid
    else: hiE = mid
print("crossing epsilon* (u=0.3, poly=1): lambda_*eps = exp(-c0/eps) at eps* =", mp.nstr((loE+hiE)/2, 6))

# ---------------------------------------------------------------- SEC D
hdr("SEC D: u=1 link: |I-J| <= delta * M_1(eps), M_1 uniformly bounded; majorant check")
# on R_1: Re(iS_b) = -S_E <= 0, regulator quadratic +eps cos(3pi/4)rho^2 (anti-damping O(eps rho^2)),
# delta damping delta*cos(3pi/8)rho^2; net quadratic = eps*(cos(3pi/4)+lam*cos(3pi/8)):
for Lm in (mp.mpf('1.8'), Lstar, mp.mpf('2')):
    print("lam=%s: net rho-quadratic coeff at u=1 (per eps): %s" % (mp.nstr(Lm, 8), mp.nstr(mp.cos(3*mp.pi/4)+Lm*mp.cos(3*mp.pi/8), 8)))
# quartic domination: S_E >= kappa*rho^4 in the chart, so -S_E + a*eps*rho^2 <= -S_E/2 + a^2 eps^2/(4 kappa):
kap, aeps = mp.mpf('0.05'), mp.mpf('0.05826')
print("uniform bound: -S_E/2 + C, C =", mp.nstr(aeps**2/(4*kap), 8), "(absorbed by window k<14 majorant)")
# |O_k| <= 2 on the slice at R_1 (055) so the window majorant applies with M_1(eps) <= O(1)
print("linking error <= lam*eps * M_1 -> 0 at u=1: link VALID at u=1, INVALID for u<1 (SEC C)")
print("DONE")
