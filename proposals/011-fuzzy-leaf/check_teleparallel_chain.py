"""
Chain of the analytic derivation of  rho^2 X = -2 h - r + (3/2) rho^2 I_S + td  (see proposal):
 (a) V_mu = G^{l n} T_{l|mu n}  equals  +- d_mu ln rho  (pointwise, exact perturbative class): coefficient of |V -+ dlnrho|^2.
 (b) teleparallel identity  sqrt|G| R[G] = -sqrt|G| (I_A/4 + I_B/2 - I_V) + total derivative  (G = eta_{AB} e^A e^B, e = eta^{-1} omega):
     coefficient of rho^2 R_G + rho^2 (I_A/4 + I_B/2 - I_V) at cubic order, zero total momentum, must vanish.
 (c) sqrt|G| = rho^2 and  rho^2 R_G = h + (3/2) r  mod td at cubic order.
 (d) S^2 = (I_A - 2 I_B)/3 (algebra; checked as pointwise residual of rho^2 (I_S - (I_A-2I_B)/3)).
"""
import numpy as np
import check_torsion_decomposition as C
rng = np.random.default_rng(99)
mx = {'Vm': 0.0, 'Vp': 0.0, 'tele': 0.0, 'c': 0.0, 'S': 0.0}
sc = {'tele': 0.0, 'c': 0.0}
for s in range(25):
    sig = rng.choice([1.0, -1.0]); ab = rng.uniform(0.5, 2.5, 2)
    p1 = rng.integers(-3, 4, 4).astype(float); p2 = rng.integers(-3, 4, 4).astype(float); p3 = -p1 - p2
    us = [rng.normal(size=4) for _ in range(3)]
    o = C.build(sig, ab, [p1, p2, p3], us, [1, 2, 3, 4, 5, 6, 7])
    for mk in range(1, 8):
        mx['Vm'] = max(mx['Vm'], abs(o['Vm2'][mk])); mx['Vp'] = max(mx['Vp'], abs(o['Vp2'][mk]))
    mx['tele'] = max(mx['tele'], abs(o['tele'][7])); sc['tele'] = max(sc['tele'], abs(o['RG2'][7]))
    cc = o['RG2'][7] - o['h'][7] - 1.5*o['r'][7]
    mx['c'] = max(mx['c'], abs(cc)); sc['c'] = max(sc['c'], abs(o['RG2'][7]))
    # algebra check, all orders in this class
    for mk in range(1, 8):
        mx['S'] = max(mx['S'], abs(o['S'][mk] - (o['A'][mk] - 2*o['B'][mk])/3))
print('(a) max coefficient of |V - dlnrho|^2 (all masks):', mx['Vm'], '   of |V + dlnrho|^2:', mx['Vp'])
print('(b) teleparallel: max |cubic coeff of rho^2 R_G + rho^2(I_A/4+I_B/2-I_V)| =', mx['tele'], ' typical |rho^2 R_G| cubic coeff:', sc['tele'])
print('(c) max |cubic coeff of rho^2 R_G - h - 3/2 r| =', mx['c'], ' typical:', sc['c'])
print('(d) max |rho^2 (I_S - (I_A - 2 I_B)/3)| over all masks =', mx['S'])

import sympy as sp
a,b,s_,v,h,r=sp.symbols('a b s v h r')
# (b)+(c): h + 3/2 r = -a/4 - b/2 + v (mod td);  (d) s = (a-2b)/3;  (a) v = r
sol=sp.solve([sp.Eq(h+sp.Rational(3,2)*r, -a/4-b/2+v), sp.Eq(s_,(a-2*b)/3), sp.Eq(v,r)],[a,b,v])
print('algebra: rho^2 X = a =', sp.simplify(sol[a]))
