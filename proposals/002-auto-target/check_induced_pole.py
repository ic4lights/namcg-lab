"""Induced Weyl and R^2 coefficients versus the induced R coefficient,
and the location of the extra spin-2 zero relative to the cutoff.

Inputs (all from the manuscript's conditional truncated identity):
  W_E  ⊃ -(1/(32 pi^2)) [ A1 (Lam^2-mu^2) ∫sqrt(g) R_E + L ∫sqrt(g) a2 ],
  a2 ⊃ Wc C^2 + Rc R^2 + (Euler),  L = ln(Lam^2/mu^2),
  continuation of App. A: L_L = -L_E for scalar densities, curvature
  invariants continued without sign.
Here A1 = sum_s w_s A_{1,R,s}, Wc = sum_s w_s (C^2 coeff of tr a_{2,s}),
Rc = sum_s w_s (R^2 coeff of tr a_{2,s}).
"""
import sympy as sp
import mpmath as mp

A1, Wc, Rc, Lam, mu, L, G = sp.symbols('A1 Wc Rc Lambda mu L G', positive=True)

# Lorentzian coefficients
inv16piG = A1 * (Lam**2 - mu**2) / (32 * sp.pi**2)
cW = Wc * L / (32 * sp.pi**2)
cR = Rc * L / (32 * sp.pi**2)
Gval = sp.solve(sp.Eq(1 / (16 * sp.pi * G), inv16piG), G)[0]
print('G_eff =', sp.simplify(Gval), '  (1/G =', sp.simplify(1 / Gval), ')')

m2sq = sp.simplify(-1 / (32 * sp.pi * Gval * cW))
m0sq = sp.simplify(1 / (96 * sp.pi * Gval * cR))
print('m_2^2 (extra spin-2, ghost residue) =', m2sq)
print('m_0^2 (extra spin-0, healthy residue) =', m0sq)
xi = sp.simplify(32 * sp.pi * Gval * cW)
print('TT expansion parameter 32 pi G c_W k^2 / k^2 =', xi)

# Minimally coupled real scalars: A_{1,R} = 1/6, Weyl coeff 1/120,
# R^2 coeff (1/2)(1/6)^2 = 1/72 per component.  a2 Weyl coefficient:
# (1/180)(Riem^2 - Ric^2) = C^2/120 - E_GB/360 + 0*R^2.
Riem2, Ric2, R2, C2, EGB = sp.symbols('Riem2 Ric2 R2 C2 EGB')
sol = sp.solve([sp.Eq(C2, Riem2 - 2 * Ric2 + R2 / 3), sp.Eq(EGB, Riem2 - 4 * Ric2 + R2)],
               [Riem2, Ric2])
expr = sp.expand(sp.Rational(1, 180) * (sol[Riem2] - sol[Ric2]))
print('(Riem^2-Ric^2)/180 in (C2,EGB,R2) basis:', expr)
E0, Q, R = sp.symbols('E0 Q R')
Rpart = sp.expand(sp.Rational(1, 180) * sp.Rational(5, 2) * R**2
                  + sp.Rational(1, 2) * (E0 + Q * R)**2 - sp.Rational(1, 6) * R * (E0 + Q * R))
print('R^2 coefficient of a2 for E=E0+QR:', sp.factor(Rpart.coeff(R, 2)),
      ' equals (1/2)(1/6-Q)^2 ?', sp.simplify(Rpart.coeff(R, 2) - sp.Rational(1, 2) * (sp.Rational(1, 6) - Q)**2) == 0)

N0 = sp.Symbol('N0', positive=True)
sc = {A1: N0 / 6, Wc: N0 / 120, Rc: N0 / 72}
print('scalars, mu<<Lam: m_2^2/Lam^2 =', sp.simplify((m2sq / Lam**2).subs(sc).subs(mu, 0)))
print('scalars, mu<<Lam: m_0^2/Lam^2 =', sp.simplify((m0sq / Lam**2).subs(sc).subs(mu, 0)))
print('a = A1/(2 Wc) for scalars =', (A1 / (2 * Wc)).subs(sc))

# ---- momentum-resolved logarithm: L -> ln(Lam^2/z) + c, z = k_E^2 = k^2 (mostly plus)
# zero of TT coefficient:  1 - (1/a) x (ln(1/x) + c) = 0,  x = z/Lam^2.
mp.mp.dps = 30
def roots(a, c):
    out = []
    for br in (0, -1):
        W = mp.lambertw(-a * mp.e**(-c), br)
        x = -a / W
        # principal-sheet check: ln x must equal W + c ... verify residual
        res = x * (-mp.log(x) + c) - a
        out.append((br, x, abs(x), abs(res)))
    return out

print('\nTT zeros on principal sheet, x = k^2/Lam^2 (mostly plus):')
for a in (10, 1, mp.mpf(1) / mp.e, 0.2):
    for c in (0, 2 - mp.euler, -2, 2):
        for br, x, ax, res in roots(a, c):
            print(f'  a={mp.nstr(a,4):>6} c={mp.nstr(c,4):>6} branch={br:>2} x={mp.nstr(x,6):>28} |x|={mp.nstr(ax,5):>8} residual={mp.nstr(res,3)}')

# critical c for which |x|=1 at a=10 (complex pair)
def absx_minus1(c, a=10):
    return abs(-a / mp.lambertw(-a * mp.e**(-c), 0)) - 1
cstar = mp.findroot(lambda c: absx_minus1(c), 2.0)
print('\na=10: |x|=1 at c* =', mp.nstr(cstar, 8), ' (|x|<1 for c > c*? check:)',
      mp.nstr(absx_minus1(cstar + 0.5) + 1, 6), mp.nstr(absx_minus1(cstar - 0.5) + 1, 6))
# critical a at c=0
astar = mp.findroot(lambda a: abs(-a / mp.lambertw(-a, 0)) - 1, 1.0)
print('c=0: |x|=1 at a* =', mp.nstr(astar, 8))
for a in (astar * 0.9, astar * 1.1):
    print('   a=', mp.nstr(a, 6), ' |x|=', mp.nstr(abs(-a / mp.lambertw(-a, 0)), 6))

# ---- mu-independence of a second-order proper-time form factor (illustration)
# I(k) = ∫_{1/Lam^2}^{1/mu^2} ds/s ∫_0^1 dal exp(-al(1-al) s k^2)
def I(k, Lam_, mu_):
    f = lambda al: mp.e1(al * (1 - al) * k**2 / Lam_**2) - mp.e1(al * (1 - al) * k**2 / mu_**2)
    return mp.quad(f, [0, 0.5, 1])
print('\nform-factor illustration (Lam=1):')
for k in (1e-2, 1e-3):
    for mu_ in (1e-5, 1e-7, 1e-9):
        val = I(mp.mpf(k), 1, mp.mpf(mu_))
        print(f'  k={k:g} mu={mu_:g}  I - ln(Lam^2/k^2) = {mp.nstr(val - mp.log(1 / k**2), 8)}   (2 - gamma_E = {mp.nstr(2 - mp.euler, 8)})')
    print(f'  local value ln(Lam^2/mu^2) would be: {[mp.nstr(mp.log(1/m**2),5) for m in (1e-5,1e-7,1e-9)]}')
