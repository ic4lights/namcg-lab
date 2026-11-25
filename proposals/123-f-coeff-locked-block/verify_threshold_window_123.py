# -*- coding: ascii -*-
# Item 123 script 3: threshold/window consistency for the Alternate-scope
# truncation, CONSUMING (not rederiving) the recorded mass-resummed window
# technology of the Problem F ledger: the threshold J(m^2;s_min,s_max) and
# the windows of Equation (eq:appA-Wexp). All checks exact (sympy, no floats).
#
# Recorded inputs consumed (quoted in proposal):
#   J(m2;smin,smax) = e^{-m2 smin}/smin - e^{-m2 smax}/smax
#                     - m2 [E1(m2 smin) - E1(m2 smax)],  E1 = expint(1,.)
#   smin = LUV^-2, smax = mu^-2; massless window L = ln(LUV^2/mu^2);
#   H-block fixed-window coefficient [(LUV^2-mu^2) - m2 ln(LUV^2/mu^2)]
#   (block bookkeeping paragraph); Upsilon_H = 10[e^{-y} - y E1(y)] and
#   |m2|^2/LUV^2 = 10[e^{-y}/E1(y) - y] for mu << m (window paragraph).
#
# Invariant expected outputs:
#   J0_MASSLESS    J(0;smin,smax) = LUV^2 - mu^2 exactly (ghost/K/tensor use)
#   J_SERIES       J = (LUV^2-mu^2) - m2*L + O(m2^2 log m2): the recorded
#                  fixed-window H-block expression is the small-m2 truncation
#   MU_ZERO_T1     mu^2 e^{-m2/mu^2} -> 0 and E1 -> 0 (squeeze bound e^-z/z) as mu -> 0+
#   MU_ZERO_J      J -> LUV^2 (e^{-y} - y E1(y)), y = m2/LUV^2 (mu -> 0+)
#   UPSILON_H      10*J/LUV^2 in that limit = 10[e^{-y} - y E1(y)] = recorded
#   UPSILON_DER    d/dy [e^{-y} - y E1(y)] = -E1(y) < 0 (exact monotonicity)
#   UPSILON_Y0     y -> 0+ limit of e^{-y} - y E1(y) is 1 (recorded 10)
#   POLE_RATIO     [e^{-y} - y E1(y)]/E1(y) = e^{-y}/E1(y) - y (recorded form)
#   Q16_WINDOWED   Q=1/6, n_K=0 windowed trunk C_R = (5/3+e_h)(LUV^2-mu^2)/(32 pi^2)
#                  in the block bookkeeping sign convention (ghost survives)

import sympy as sp

ok = []
def chk(name, cond, val=None):
    ok.append(bool(cond))
    print("%-16s %s%s" % (name, "PASS" if cond else "FAIL",
                          "" if val is None else ("   " + str(val)[:110])))

m2, LUV, mu, y = sp.symbols('m2 Lambda_UV mu y', positive=True)
sm = 1 / LUV**2
sx = 1 / mu**2
E1 = lambda z: sp.expint(1, z)
J = sp.exp(-m2 * sm) / sm - sp.exp(-m2 * sx) / sx - m2 * (E1(m2 * sm) - E1(m2 * sx))

# ---- J at zero mass: exact massless window ---------------------------------
J0 = sp.simplify(sp.limit(J, m2, 0))
chk("J0_MASSLESS", sp.simplify(J0 - (LUV**2 - mu**2)) == 0, J0)

# ---- small-mass series to O(m2): matches recorded fixed-window expression --
EG = sp.EulerGamma
# E1(x) = -EG - log x + x + O(x^2); exponentials to second order are enough
Jman = ((1 / sm) * (1 - m2 * sm + (m2 * sm)**2 / 2)
        - (1 / sx) * (1 - m2 * sx + (m2 * sx)**2 / 2)
        - m2 * ((-EG - sp.log(m2 * sm) + m2 * sm) - (-EG - sp.log(m2 * sx) + m2 * sx)))
c1 = sp.expand_log(sp.expand(Jman).coeff(m2, 1), force=True)
Lwin = sp.log(LUV**2 / mu**2)
chk("J_SERIES", sp.simplify(sp.expand_log(c1 + Lwin, force=True)) == 0, c1)

# ---- mu -> 0+ limit ----------------------------------------------------------
t1 = sp.limit(mu**2 * sp.exp(-m2 / mu**2), mu, 0)
# E1(z) -> 0 as z -> oo: E1(z) = int_z^oo e^-t/t dt is positive and, for
# z >= 1, bounded by e^-z/z (since 1/t <= 1/z on [z,oo)); sympy leaves
# expint(1, oo) unevaluated, so check positivity, the bound at sample
# points, and that the bound vanishes at infinity (squeeze).
zz = sp.Symbol('z', positive=True)
bound_lim = sp.limit(sp.exp(-zz) / zz, zz, sp.oo)
bound_ok = all(bool(sp.N(sp.expint(1, z0) - sp.exp(-z0) / z0) < 0)
               for z0 in (2, 50, 500))
pos_ok = all(bool(sp.N(sp.expint(1, z0)) > 0) for z0 in (2, 50, 500))
chk("MU_ZERO_T1", t1 == 0 and bound_lim == 0 and bound_ok and pos_ok,
    (t1, bound_lim))
Jlim = sp.exp(-m2 / LUV**2) * LUV**2 - m2 * E1(m2 / LUV**2)
Uh = sp.simplify(10 * Jlim.subs(m2, y * LUV**2) / LUV**2)
chk("MU_ZERO_J", sp.simplify(Jlim.subs(m2, y * LUV**2) / LUV**2
                             - (sp.exp(-y) - y * E1(y))) == 0)
chk("UPSILON_H", sp.simplify(Uh - 10 * (sp.exp(-y) - y * E1(y))) == 0, Uh)
dU = sp.simplify(sp.diff(sp.exp(-y) - y * E1(y), y) + E1(y))
chk("UPSILON_DER", dU == 0)
y0 = sp.limit(sp.exp(-y) - y * E1(y), y, 0)
chk("UPSILON_Y0", y0 == 1, y0)
pr = sp.simplify((sp.exp(-y) - y * E1(y)) / E1(y) - (sp.exp(-y) / E1(y) - y))
chk("POLE_RATIO", pr == 0)

# ---- Q = 1/6 windowed trunk ---------------------------------------------------
Q, nK, eh = sp.symbols('Q n_K e_h', real=True)
Jw = sp.Symbol('Jw', positive=True)     # H window, carried symbolically
CR = -(16 * (sp.Rational(1, 6) - Q) * Jw
       + (nK * (sp.Rational(1, 6) - sp.Symbol('QK')) - sp.Rational(5, 3) - eh)
       * (LUV**2 - mu**2)) / (32 * sp.pi**2)
CRc = sp.simplify(CR.subs({Q: sp.Rational(1, 6), nK: 0}))
chk("Q16_WINDOWED", sp.simplify(CRc - (sp.Rational(5, 3) + eh)
                                * (LUV**2 - mu**2) / (32 * sp.pi**2)) == 0, CRc)

print("SCRIPT3 VERDICT:", "PASS" if all(ok) else "FAIL")
raise SystemExit(0 if all(ok) else 1)
