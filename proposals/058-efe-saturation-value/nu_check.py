#!/usr/bin/env python3
"""058: numerical and symbolic checks of the external-field saturation value.
Manuscript inputs only: g_dagger = g_s = 1.20e-10 m/s^2 (ch13 eq:nu-sqrt, McGaugh2016),
g_gal = 2.2e-10 m/s^2 (ch13 L254, appE L47), appI range (1.5-2.2)e-10, g_N = 1e-11 (ch16 L206).
Literature inputs (verified, see proposal): Chae 2023 gamma=1.43+-0.06; Banik et al. 2024 ~20% velocity.
"""
import math
import sympy as sp

gs = 1.20e-10
def nu_sqrt(g): return 1.0/(1.0-math.exp(-math.sqrt(g/gs)))
def L_e(g):            # d ln nu / d ln g_N for nu_sqrt
    s = math.sqrt(g/gs); return -(s/2.0)*(nu_sqrt(g)-1.0)
def nu_simple(g):      # simple MOND nu(y)=(1+sqrt(1+4/y))/2
    y = g/gs; return 0.5*(1+math.sqrt(1+4/y))
def nu_standard(g):    # standard MOND mu=x/sqrt(1+x^2) -> nu(y)=sqrt(1/2+sqrt(1/4+1/y^2))
    y = g/gs; return math.sqrt(0.5+math.sqrt(0.25+1/y**2))

print("== 1. nu_sqrt at the manuscript arguments ==")
for g in (2.2e-10, 1.5e-10, 1e-11):
    print(f"g={g:.2e}  g/gs={g/gs:.4f}  nu_sqrt={nu_sqrt(g):.4f}  sqrt(nu)-1={math.sqrt(nu_sqrt(g))-1:.4f}  L_e={L_e(g):.4f}")
print("ch13/ch16/appE claim: nu_sqrt(g_gal) ~ 1.1  ->", "FALSE" if abs(nu_sqrt(2.2e-10)-1.1)>0.05 else "ok")

print("\n== 2. Is there a reading under which 1.1 is right? ==")
x = math.log(11.0)            # nu=1.1 <=> exp(-sqrt(y))=1/11
print(f"nu_sqrt=1.1 requires g_N/g_s={x**2:.3f}, g_N={x**2*gs:.3e} m/s^2")
print(f"sqrt(nu_sqrt(2.2e-10)) (velocity factor) = {math.sqrt(nu_sqrt(2.2e-10)):.4f}")
print(f"simple-MOND nu at 2.2e-10   = {nu_simple(2.2e-10):.4f}")
print(f"standard-MOND nu at 2.2e-10 = {nu_standard(2.2e-10):.4f}  (the only listed reading near 1.1)")
# argument read as Newtonian baryonic field: invert g_obs = nu_sqrt(gN) gN = 2.2e-10
lo, hi = 1e-12, 2.2e-10
for _ in range(200):
    mid = 0.5*(lo+hi)
    if nu_sqrt(mid)*mid < 2.2e-10: lo = mid
    else: hi = mid
gNsun = 0.5*(lo+hi)
print(f"if 2.2e-10 = v^2/R0 is the observed field, eq:appE-RAR gives baryonic g_N={gNsun:.4e}, nu_sqrt(g_N)={nu_sqrt(gNsun):.4f}")

print("\n== 3. literature comparison ==")
print(f"Chae 2023 gamma=1.43 -> velocity factor sqrt = {math.sqrt(1.43):.4f}")
print(f"Banik et al. 2024 ~20% velocity -> acceleration factor 1.2^2 = {1.2**2:.2f}")
print(f"appI range: nu_sqrt in [{nu_sqrt(2.2e-10):.3f}, {nu_sqrt(1.5e-10):.3f}], velocity excess in [{math.sqrt(nu_sqrt(2.2e-10))-1:.3f}, {math.sqrt(nu_sqrt(1.5e-10))-1:.3f}]")
print(f"isolated map at 1e-11: acceleration {nu_sqrt(1e-11):.3f}, velocity {math.sqrt(nu_sqrt(1e-11)):.3f}")

print("\n== 4. 3D QUMOND EFE-dominated anisotropy (Famaey-McGaugh 2012 eqs. 63-64) ==")
for g in (2.2e-10, 1.5e-10):
    nu, L = nu_sqrt(g), L_e(g)
    print(f"g_e={g:.2e}: along field nu_e={nu:.4f}; in plane nu_e(1+L/2)={nu*(1+L/2):.4f}; factor {1+L/2:.4f}")

print("\n== 5. symbolic: 1D QUMOND uniform-field form and sign of the bracket ==")
gN, ge = sp.symbols('g_N g_e', positive=True)
nu = sp.Function('nu')
# QUMOND, 1D: total field = nu(|gN+ge|)(gN+ge); internal = total - nu(ge) ge
internal = nu(gN+ge)*(gN+ge) - nu(ge)*ge
correct = nu(gN+ge)*gN + (nu(gN+ge)-nu(ge))*ge
manuscript = nu(gN+ge)*gN + (nu(ge)-nu(gN+ge))*ge
print("internal - correct   =", sp.simplify(internal-correct))
print("internal - manuscript=", sp.simplify(internal-manuscript))
lin_c = sp.series(correct, gN, 0, 2).removeO()
lin_m = sp.series(manuscript, gN, 0, 2).removeO()
print("d/dgN at gN=0, correct   :", sp.simplify(sp.diff(lin_c, gN)))
print("d/dgN at gN=0, manuscript:", sp.simplify(sp.diff(lin_m, gN)))
g0 = 2.2e-10
s = math.sqrt(g0/gs); nue = nu_sqrt(g0); dnu = -(nue**2)*math.exp(-s)*(s/(2*g0))
print(f"numeric along-field slope at g_e={g0:.1e}: correct {nue+dnu*g0:.4f} = nu_e(1+L) ; manuscript {nue-dnu*g0:.4f} = nu_e(1-L)")

print("\n== 6. symbolic: 3D linearised QUMOND point mass, check of FM12 eq. 63-64 ==")
X, Y, Z, G, m, nue_s, L = sp.symbols('x y z G m nu_e L', real=True)
r = sp.sqrt(X**2+Y**2+Z**2)
phiN = -G*m/r
psi = -G*m*r/2                     # Laplacian(psi) = phiN
lap = lambda f: sp.diff(f, X, 2)+sp.diff(f, Y, 2)+sp.diff(f, Z, 2)
print("Lap(psi)-phiN =", sp.simplify(lap(psi)-phiN))
phi = nue_s*(phiN + L*sp.diff(psi, Z, 2))
target = -G*m*nue_s/r*(1+L/2*(X**2+Y**2)/r**2)
print("phi - FM12 form =", sp.simplify(phi-target))
# phi solves Lap phi = nu_e (Lap phiN + L d_z^2 phiN) away from origin
print("Lap(phi) - nu_e(Lap phiN + L dzz phiN) =", sp.simplify(lap(phi)-nue_s*(lap(phiN)+L*sp.diff(phiN, Z, 2))))

print("\n== 7. vector form of corrected eq:nu-efe, linearised in g_N (g_ext along z) ==")
eps, a, b, c, gE = sp.symbols('epsilon a b c g_E', positive=True)
nuf = sp.Function('nu')
gNv = sp.Matrix([a, b, c])*eps
gEv = sp.Matrix([0, 0, gE])
gtot = sp.sqrt((gNv+gEv).dot(gNv+gEv))
corr = nuf(gtot)*gNv + (nuf(gtot)-nuf(gE))*gEv
lin = sp.simplify(sp.diff(corr, eps).subs(eps, 0))
print("d g/d eps at 0 (corrected):", list(lin))
manu = nuf(gtot)*gNv + (nuf(gE)-nuf(gtot))*gEv
print("d g/d eps at 0 (manuscript):", list(sp.simplify(sp.diff(manu, eps).subs(eps, 0))))
print("=> corrected: transverse nu_e, along nu_e + g_E nu'_e = nu_e(1+L_e); manuscript: along nu_e(1-L_e)")
