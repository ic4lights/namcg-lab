# S3: exact closed forms for the frame-averaged coupling of the integrated
# fuzzy variance proxy profiles f = nu*l/2 (l = 1..L, multiplicity 2l+1,
# slot count D = (L+1)^2 - 1 = L(L+2): the s5/s6 convention B of proposal 085)
# and their precise asymptotics. Exact rational/symbolic throughout; the only
# floats are cross-checks against shipped integrated numerals.
import sympy as sp
from sympy import Rational, simplify, together, apart, symbols, factor, Poly

L, nu, Wv = symbols('L nu W', positive=True)

def sums(Lv):
    Wp = sum((2 * l + 1) * sp.Rational(l, 2) for l in range(1, Lv + 1))
    S2 = sum((2 * l + 1) * sp.Rational(l, 2)**2 for l in range(1, Lv + 1))
    return Wp, S2

# --- (1) closed forms
Wc = L * (L + 1) * (4 * L + 5) / 12                      # nu = 1
S2c = L * (L + 1) * (3 * L**2 + 5 * L + 1) / 24          # nu = 1
Dc = L * (L + 2)
for Lv in range(1, 21):
    Wp, S2 = sums(Lv)
    assert Wp == Wc.subs(L, Lv) and S2 == S2c.subs(L, Lv)
    assert Dc.subs(L, Lv) == (Lv + 1)**2 - 1
print("S3.1 proxy sums W = L(L+1)(4L+5)/12, sum g^2 = L(L+1)(3L^2+5L+1)/24, "
      "D = L(L+2): exact for L=1..20 OK")

# --- (2) effective dimension, off-uniformity, limit 8/9
Deff = together(Wc**2 / S2c)
Deff = sp.simplify(Deff)
Deff_target = L * (L + 1) * (4 * L + 5)**2 / (6 * (3 * L**2 + 5 * L + 1))
assert simplify(Deff - Deff_target) == 0
ratio = sp.simplify(Deff_target / Dc)
assert sp.limit(ratio, L, sp.oo) - sp.Rational(8, 9) == 0
gap = sp.together(1 - ratio)
num, den = sp.fraction(gap)
numr, denr = sp.fraction(sp.together(1 - ratio))
for Lv in range(2, 201):
    assert sp.sign(numr.subs(L, Lv)) == 1 and sp.sign(denr.subs(L, Lv)) == 1
print("S3.2 D_eff = L(L+1)(4L+5)^2/(6(3L^2+5L+1)) exact; D_eff/D -> 8/9; "
      "1 - D_eff/D = %s / (%s), strictly positive for L >= 2: the proxies are"
      " strictly off the uniformity locus at every cutoff with limiting"
      " shortfall 1/9" % (sp.expand(factor(num)), sp.expand(den)))

# --- (3) fixed-nu frame-averaged coupling, closed form + exact division
Egnu = sp.simplify((Dc * S2c - Wc**2) / (Dc * (Dc + 1)))
Egnu_target = L * (L - 1) * (2 * L**2 + 12 * L + 13) / (144 * (L + 1) * (L + 2))
assert simplify(Egnu - Egnu_target) == 0
for Lv in range(1, 21):
    Wp, S2 = sums(Lv)
    Dl = Lv * (Lv + 2)
    assert sp.nsimplify((Dl * S2 - Wp**2) / (Dl * (Dl + 1))) == Egnu.subs(L, Lv)
div = sp.apart(Egnu_target, L)
exact_div = sp.Rational(1, 144) * (2 * L**2 + 4 * L - 15) \
    + (24 * L + 30) / (144 * (L + 1) * (L + 2))
assert simplify(Egnu_target - exact_div) == 0
print("S3.3 fixed-nu=1: E_u Gamma = L(L-1)(2L^2+12L+13)/(144(L+1)(L+2)) exact"
      " for L=1..20; exact division E_u Gamma = L^2/72 + L/36 - 5/48 +"
      " (24L+30)/(144(L+1)(L+2)): leading term L^2/72 with positive O(1/L)"
      " remainder -- fixed-nu averaged decoupling FAILS at leading order")

# --- (4) fixed-W normalized coupling, closed form + approach to 1/8
EgW = sp.simplify((Dc * S2c / Wc**2 - 1) / (Dc * (Dc + 1)))
EgW_target = (2 * L**3 + 10 * L**2 + L - 13) / \
    (L * (L + 1)**3 * (L + 2) * (4 * L + 5)**2)
assert simplify(EgW - EgW_target) == 0
for Lv in range(2, 21):
    Wp, S2 = sums(Lv)
    Dl = Lv * (Lv + 2)
    assert sp.nsimplify((Dl * S2 / Wp**2 - 1) / (Dl * (Dl + 1))) \
        == EgW_target.subs(L, Lv)
sd = sp.simplify(EgW_target * Dc**2)  # -> 1/8
d2 = sp.together(sd - sp.Rational(1, 8))
nn, dd = sp.fraction(d2)
nnf = sp.factor(sp.expand(nn))
corr = sp.together(sd - sp.Rational(1, 8))
cn, cd = sp.fraction(sp.expand(sp.numer(sp.together(corr))), )
cn = sp.expand(sp.numer(corr) * 8) if False else sp.expand(
    8 * (2 * L**3 + 10 * L**2 + L - 13) * L * (L + 2) - (L + 1)**3 * (4 * L + 5)**2)
assert cn == 24 * L**4 - 25 * L**3 - 299 * L**2 - 323 * L - 25
for Lv in range(5, 401):
    assert sp.Rational(cn.subs(L, Lv)) > 0
for Lv in (2, 3, 4):
    assert sp.simplify((sd - sp.Rational(1, 8)).subs(L, Lv)) < 0
rel = sp.simplify((sd / sp.Rational(1, 8) - 1) * L)
assert sp.limit(rel, L, sp.oo) == sp.Rational(3, 2)
print("S3.4 fixed-W=1: E_u Gamma = (2L^3+10L^2+L-13)/(L(L+1)^3(L+2)(4L+5)^2)"
      " exact for L=2..20; E_u Gamma * D^2 / W^2 = 1/8 + (24L^4-25L^3-299L^2-323L-25)"
      "/(8(L+1)^3(4L+5)^2): correction strictly positive for L=5..400,"
      " negative at L=2,3,4; L * (relative correction) -> 3/2 exactly")

# --- (5) cross-checks against shipped integrated numerals (081/085)
chk = {40: 23.233, 80: 91.009, 160: 359.9, 320: 1431.0}
for Lv, ref in chk.items():
    got = float(Egnu_target.subs(L, Lv))
    assert abs(got / ref - 1) < 2e-3
print("S3.5 fixed-nu ramp matches shipped gatekeeper ramp 23.233/91.009/359.9"
      "/1431 at L=40/80/160/320 (rel dev < 2e-3)")
chkW = {40: 4.57e-8, 320: 1.18e-11}
for Lv, ref in chkW.items():
    got = float(EgW_target.subs(L, Lv))
    assert abs(got / ref - 1) < 5e-3
print("S3.6 fixed-W ramp matches shipped 4.57e-8 / 1.18e-11 at L=40/320")
for Lv, ref in ((40, 1488), (160, 23017)):
    got = float(Deff_target.subs(L, Lv))
    assert abs(got / ref - 1) < 5e-3 and abs(got - round(got)) > 0.0
print("S3.7 D_eff reproduces integrated L3177 numerals 1488 (L=40) and 23017"
      " (L=160); fourth-moment excess 1/D_eff = %.3e / %.3e vs integrated"
      " 6.7e-4 / 4.3e-5"
      % (1 / float(Deff_target.subs(L, 40)), 1 / float(Deff_target.subs(L, 160))))
assert abs(1 / float(Deff_target.subs(L, 40)) - 6.7e-4) / 6.7e-4 < 5e-3
assert abs(1 / float(Deff_target.subs(L, 160)) - 4.3e-5) / 4.3e-5 < 2e-2  # integrated numeral quoted to 2 s.f.
print("S3 DONE")
