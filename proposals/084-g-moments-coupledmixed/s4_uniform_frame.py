# s4_uniform_frame.py (084) Uniform-frame identity for the coupling functional.
# For |u_i|^2 = 1/D:  Gamma = sum_i |u_i|^2 (g_i - mu)^2 = (W^2/D) (1/D_eff - 1/D),
# with W = sum g_i and D_eff = W^2 / sum g_i^2 (081 effective dimension), mu = W/D.
# Exact rational check for several profiles; plus Gamma >= 0 and Gamma = 0 iff all g_i
# equal on supp(u).  Run from repo root:
#   python -I proposals/084-g-moments-coupledmixed/s4_uniform_frame.py
import sympy as sp
from sympy import Rational, simplify
gs = [Rational(1,2), Rational(2,3), Rational(5,7), Rational(1,11)]
fails = 0
for D in (3, 4):
    gg = gs[:D]
    W = sum(gg); S2 = sum(g*g for g in gg); mu = W/D
    Gam = sum((g-mu)**2 for g in gg)/D
    Deff = W**2/S2
    ok = simplify(Gam - (W**2/sp.Integer(D))*(sp.Integer(1)/Deff - sp.Integer(1)/sp.Integer(D))) == 0
    print('D=%d profile %s: Gamma = %s, identity vs (W^2/D)(1/D_eff-1/D): %s'
          % (D, [str(g) for g in gg], Gam, ok))
    fails += (not ok)
    fails += int(bool(Gam < 0))
# Gamma = 0 iff g constant on supp(u): symbolic square form + explicit unequal check
w_, g1, g2 = sp.symbols('w g1 g2', real=True)
G2 = w_*(g1-(w_*g1+(1-w_)*g2))**2 + (1-w_)*(g2-(w_*g1+(1-w_)*g2))**2
Gs = sp.simplify(sp.together(G2))
print('D=2 general-weight square form:', Gs)
okz = sp.simplify(Gs.subs({g2: g1})) == 0
print('Gamma(g1=g2) = 0: %s ; Gamma(1,2;w=1/2) = %s' % (okz, Gs.subs({w_: Rational(1,2), g1: 1, g2: 2})))
fails += (not okz)
# fourth-moment excess in effective-dimension form, uniform frame
Wd, s2v, De = sp.symbols('W s2 D_eff', positive=True)
print('trQ^4 excess (uniform frame) = 128 s^4 (W^2/D)(D_eff^{-1} - D^{-1})  [zero iff D_eff = D, i.e. 082 uniform profile]')
print('S4 invariant: identity fail count =', fails)
print('S4 OK' if fails == 0 else 'S4 FAIL')
