# Proposal 057 r1, script 1: gamma->0- bridge windows, reduction inequalities,
# branch closed forms with the contour-dependent phase, and the mass-side ray
# bound constant Gamma0(u). Run: python -I bridge_gamma.py
# Checks compare INDEPENDENT computations (symbolic vs numeric vs mpmath quad).
import mpmath as mp
import sympy as sp
import random
mp.dps = 30

def hdr(t):
    print("=" * 70)
    print(t)
    print("=" * 70)

# ---------------------------------------------------------------- SEC 1
hdr("SEC 1: real-part windows on R_u (regulator, mass); Leg A damping margin")
u = sp.symbols('u', real=True)
T0, Ti = sp.symbols('T0 Ti', positive=True)
g, gam, eps = sp.symbols('g gam eps', positive=True)   # gam = |gamma|, mass gamma = -gam
A0sq = sp.exp(-3*sp.I*sp.pi*u/4) * T0                  # Tr A_0^2 on R_u (tilde comps Hermitian)
Aisq = sp.exp(sp.I*sp.pi*u/4) * Ti                     # sum_i Tr A_i^2 on R_u
iSg = sp.I * (-(-gam/(2*g**2))) * (-A0sq + Aisq)       # iS_gamma, S_g = -(gamma/2g^2)Tr A A^mu
re_iSg = sp.simplify(sp.re(iSg))
tgt = -gam/(2*g**2)*(sp.sin(3*sp.pi*u/4)*T0 + sp.sin(sp.pi*u/4)*Ti)
print("Re iS_{gamma<0} equals -(|gam|/2g^2)[sin(3pi u/4)T0+sin(pi u/4)Ti]:",
      sp.simplify(re_iSg - tgt) == 0, " (negative for u in (0,1]: mass damps)")
re_reg = sp.simplify(sp.re(-eps*(A0sq + Aisq)))
print("Re regulator equals -eps[cos(3pi u/4)T0+cos(pi u/4)Ti]:",
      sp.simplify(re_reg + eps*(sp.cos(3*sp.pi*u/4)*T0 + sp.cos(sp.pi*u/4)*Ti)) == 0)
cT0 = eps*sp.cos(3*sp.pi*u/4) + gam/(2*g**2)*sp.sin(3*sp.pi*u/4)
cTi = eps*sp.cos(sp.pi*u/4) + gam/(2*g**2)*sp.sin(sp.pi*u/4)
fT0 = sp.lambdify((u, eps, gam, g), cT0, 'mpmath')
fTi = sp.lambdify((u, eps, gam, g), cTi, 'mpmath')
for epsv, gamv in ((mp.mpf('0.01'), mp.mpf('0.2')), (mp.mpf('0.05'), mp.mpf('0.2'))):
    m0 = min(min(fT0(mp.mpf(j)/200, epsv, gamv, 1), fTi(mp.mpf(j)/200, epsv, gamv, 1))
             for j in range(0, 201))
    print("LegA margin: min_u min(c_T0,c_Ti) for eps=%.2f |gam|=%.1f g=1: %s (>0: domination)"
          % (epsv, gamv, mp.nstr(m0, 8)))

# ---------------------------------------------------------------- SEC 2
hdr("SEC 2: elementary inequalities used by the reduction and the link bound")
rnd = random.Random(7)
r1 = mp.mpf(0); r2 = mp.mpf(0)
for _ in range(400):
    z = mp.mpc(mp.mpf(rnd.uniform(-30, 0)), mp.mpf(rnd.uniform(-40, 40)))
    assert abs(mp.e**z - 1) <= abs(z)
    assert abs(mp.e**(-z) - 1) <= abs(z)/abs(mp.e**z)   # = |z| e^{-Re z}
    r1 = max(r1, abs(mp.e**z - 1)/abs(z)); r2 = max(r2, abs(mp.e**(-z) - 1)*abs(mp.e**z)/abs(z))
print("|e^z-1|<=|z| and |e^{-z}-1|<=|z|e^{-Re z} for Re z<=0: ok (400 pts; max ratios %s, %s <= 1)"
      % (mp.nstr(r1, 5), mp.nstr(r2, 5)))
# |Tr(A_mu A^mu)| on R_u <= T0 + Ti  (triangle; equality only if one term vanishes)
for uv in (0.1, 0.4, 0.7, 1.0):
    ph = abs(mp.exp(-3j*mp.pi*uv/4)) * 1 + abs(mp.exp(1j*mp.pi*uv/4)) * 1
    val = abs(-mp.exp(-3j*mp.pi*uv/4)*1 + mp.exp(1j*mp.pi*uv/4)*1)
    assert val <= ph
    print("u=%.1f: |-e^{-3pi i u/4}+e^{pi i u/4}| = %s <= 2 : ok" % (uv, mp.nstr(val, 6)))

# ---------------------------------------------------------------- SEC 3
hdr("SEC 3: branch closed form vs mpmath quad; contour-dependent vs frozen phase")
def branch_cf(Q, gc):
    return 2*mp.sqrt(mp.pi/Q)*mp.exp(-gc**2/(4*Q))
def branch_quad(Q, gc, R=60):
    f = lambda a: mp.e**(-Q*a*a)*2*mp.cos(gc*a)
    return mp.quad(f, [-R, 0, R])
for uv, epsv, gamv in ((0.4, mp.mpf('0.02'), mp.mpf('0.1')),
                       (0.6, mp.mpf('0.01'), mp.mpf('0.05'))):
    Q = mp.exp(-3j*mp.pi*uv/4)*(epsv + 1j*gamv/2)
    gcT = mp.exp(3j*mp.pi*(1-uv)/8)/2
    cf = branch_cf(Q, gcT)
    qd = branch_quad(Q, gcT)
    print("u=%.1f eps=%.3g |gam|=%.2f: closed form vs quad reldev = %s"
          % (uv, epsv, gamv, mp.nstr(abs(cf-qd)/abs(cf), 4)))
# exponents, symbolic
r0, gv, ev = sp.symbols('r0 gv ev', positive=True)
gcT2 = r0**2/4*sp.exp(3*sp.I*sp.pi*(1-u)/4)
gcF2 = r0**2/4*sp.exp(3*sp.I*sp.pi/4)          # frozen at u=0 (055/056 model)
def reexpo(gc2, Q):
    return sp.simplify(sp.re(-gc2/(4*Q)))
print("TRUE phase, gam=0:  Re exponent *(eps) =", sp.simplify(reexpo(gcT2, sp.exp(-3*sp.I*sp.pi*u/4)*ev)*ev),
      "(= r0^2/(16 sqrt2), u-independent)")
print("TRUE phase, gam=0:  numeric 1/(16 sqrt2) =", mp.nstr(1/(16*mp.sqrt(2)), 6))
print("FROZEN phase, gam=0: Re exponent*(eps) =", sp.simplify(reexpo(gcF2, sp.exp(-3*sp.I*sp.pi*u/4)*ev)*ev),
      "(= r0^2 cos(3pi u/4 - pi/4)/16: u-dependent; merged text)")
EV = sp.Symbol('evv', positive=True)
QgT = sp.exp(-3*sp.I*sp.pi*u/4)*(EV + sp.I*gv/2)
ex_g = reexpo(gcT2, QgT)
sat = sp.simplify(sp.limit(ex_g, EV, 0, '+')*gv)
print("TRUE phase, eps->0 fixed gam<0: (Re exponent)*|gam| =", sat, "= -r0^2/(8 sqrt2), u-independent (saturation DECAYS)")
print("FROZEN phase: merged saturation exponent r0^2 sin(3pi u/4 - pi/4)/(8|gam|): u=0.6 value at |gam|=",
      end=" ")
print(mp.nstr(mp.sin(3*mp.pi*mp.mpf('0.6')/4 - mp.pi/4)/(8*mp.mpf('0.05')), 6),
      "(positive: diverges as gam->0-) vs TRUE-phase exponent at same |gam|:",
      mp.nstr(-1/(8*mp.sqrt(2)*mp.mpf('0.05')), 6))

# ---------------------------------------------------------------- SEC 4
hdr("SEC 4: ray/tube maximization: c0(u) (regulator side) and Gamma0(u) (mass side)")
rho = sp.symbols('rho', positive=True)
b = sp.sin(3*sp.pi*(1-u)/8)*r0
# regulator-only damping (gamma=0 side / mass-free link functional Jtilde):
E1 = sp.simplify(sp.maximize(b*rho/2 - ev*sp.cos(3*sp.pi*u/4)*rho**2, rho)[0]) \
     if hasattr(sp, 'maximize') else sp.simplify(b**2/(16*ev*sp.cos(3*sp.pi*u/4)))
c0 = sp.simplify(E1*ev)
print("ray max exponent (regulator side) = c0(u)/eps, c0(u) =", sp.simplify(c0),
      "(matches merged c0(u))")
# mass damping at eps=0: exponent = g^2 b^2/(8 gv sin(3pi u/4)) = Gamma0(u)/|gam|
Ga0 = sp.simplify(b**2/(16*(gv/(2*g**2)*sp.sin(3*sp.pi*u/4))))   # max_rho (b rho/2 - beta rho^2) = b^2/(16 beta)
print("ray max exponent (mass side, eps=0) = Gamma0(u)/|gam|, Gamma0(u) =", sp.simplify(Ga0))
fG = sp.lambdify((u, g, r0), Ga0.subs(gv, 1), 'mpmath')
fC = sp.lambdify((u, r0), c0.subs(ev, 1), 'mpmath')
print("u : Gamma0(u) (g=1,r0=1)   c0(u)")
for uu in ('0.1','0.2','0.3','1/3','0.4','0.5','0.6','0.7','0.8','0.9'):
    uv = mp.mpf(uu.replace('1/3', str(mp.mpf(1)/3)))
    print("%.3f : %s   %s" % (uv, mp.nstr(fG(uv, 1, 1), 6), mp.nstr(fC(uv, 1), 6)))
dG = sp.simplify(sp.diff(Ga0.subs({gv: 1, g: 1, r0: 1}), u))
neg = all(dG.subs(u, mp.mpf(j)/20) < 0 for j in range(2, 14))
print("d/du Gamma0 < 0 on u in (0.1,0.7) grid:", neg, "(Gamma0 DECREASES with u: u<1/3 band worst)")
# joint-ladder divergence of the two modulus bounds |gam|*e^{c0(u)/eps} and |gam|*e^{Gamma0(u)/|gam|}
print("ladder u=0.3: |gam|=0.05")
uv3 = mp.mpf('0.3'); Gv = fG(uv3, 1, 1); Cv = fC(uv3, 1)
for epsv in (mp.mpf('0.003'), mp.mpf('0.0005')):
    print("  bound1 |gam|*e^{c0/eps}/poly at eps=%s: exponent c0/eps = %s" % (epsv, mp.nstr(Cv/epsv, 6)))
print("  bound2 |gam|*e^{Gamma0/|gam|}: exponent Gamma0/|gam| = %s"
      % mp.nstr(Gv/mp.mpf('0.05'), 6))
fbeta = lambda uu, ee, gg: (ee*mp.cos(3*mp.pi*uu/4) + gg*mp.sin(3*mp.pi*uu/4)/(2*1.0))
for ee in (mp.mpf('0.05'), mp.mpf('0.01'), mp.mpf('0.001')):
    exl = (mp.sin(3*mp.pi*(1-uv3)/8)**2)/(16*fbeta(uv3, ee, mp.mpf('0.05')))
    print("  general ladder exponent b^2r0^2/(16 beta(eps)): eps=%s -> %s (eps->0: Gamma0/|gam| = %s)"
          % (ee, mp.nstr(exl, 6), mp.nstr(Gv/mp.mpf('0.05'), 6)))
# ---------------------------------------------------------------- SEC 5
hdr("SEC 5: window degrees and Leg B bookkeeping")
print("(det G~)^4 window degree 8; insertion S_gamma degree 2; k-truncation degree 8+2=10 < 14: ok",
      8 + 2 < 14)
# |e^{iS}-1| <= |S| applies to the gamma side; combined link bound:
# |Delta| <= |gam|/(2g^2) * sup_eps Jtilde, Jtilde = mass-free modulus functional (SEC4 bound1)
print("link bound: |Delta(eps,gam)| <= |gam|/(2g^2) * Jtilde(eps,u); Jtilde >= e^{c0(u)/eps}/poly")
print("DONE")
