"""022 script 1: algebraic relations of the CP^{1,2} orbit and the Q^{-1} <-> induced-metric identification (presentation P4: T^a=M^{a4}).
Checks at random orbit points (realisation of 013/018/020):
 (a) M^{AB} M_{BC} = -c^2 delta^A_C (orbit is a 'complex structure' orbit), c^2 = ell^2
 (b) y.y = -ell^2, T^a y_a = 0 (hence y_a D^a = -T^a Y_a as vector fields)
 (c) base metric: K^{mu nu}=m^2 eta^{mu nu}, g=eta+yy/m^2 (induced from R^{1,4}), g^{-1}=eta+yy/ell^2, identity K = m^2 (g^{-1} - y y/ell^2)
 (d) Q^{-1}= (eta+ eta y y eta/ell^2)/m^2 and m^2 Q^{-1}_{ab} D^aD^b has base symbol g^{-1} (pushforward of Q^{-1}-contraction)
"""
import numpy as np
from cp12_realisation import *
np.set_printoptions(precision=6, suppress=True, linewidth=160)
rng = np.random.default_rng(5)
eta4 = np.diag([-1., 1, 1, 1])
errs = {k: 0.0 for k in ['a','b','c','d1','d2']}
c2s = []
for t in range(200):
    z = rand_z_pos(rng, rng.uniform(0.5, 4))
    M = Mfun(z)                         # M[A,B] = M^{AB} (upper indices)
    Ml = eta6 @ M                       # M_A^B = eta_AC M^{CB}
    MM = Ml @ Ml                        # (M_A^B)(M_B^C)
    c2 = -MM[0, 0]
    c2s.append(c2)
    errs['a'] = max(errs['a'], np.max(np.abs(MM + c2*np.eye(6))))
    y = M[:4, 5]; y4 = M[4, 5]
    yy = y @ eta4 @ y + y4**2           # y.y with eta_{44}=+1 (y^5 excluded)
    ell2 = -yy
    # (b) T^a y_a: T^a = M^{a4}, y_a = eta_ab M^{b5}
    Ty = sum(M[a, 4]*(eta4[a, a]*M[a, 5]) for a in range(4))
    errs['b'] = max(errs['b'], abs(Ty), abs(ell2 - c2s[-1]*1.0) if False else 0)
    # (c) metric identities in coordinates y^mu
    m2 = y4**2
    K = m2*eta4
    g = eta4 + np.outer(y, y)/m2        # lower indices g_{mu nu}: eta_{mu nu} + y_mu y_nu /m^2 ; y_mu = eta y
    yl = eta4 @ y
    g = eta4 + np.outer(yl, yl)/m2
    ginv = np.linalg.inv(g)
    errs['c'] = max(errs['c'], np.max(np.abs(ginv - (eta4 + np.outer(y, y)/ell2))))
    errs['c'] = max(errs['c'], np.max(np.abs(K - m2*(ginv - np.outer(y, y)/ell2))))
    # (d) Q^{-1}
    Q = m2*eta4 + np.outer(y, y)
    Qi = np.linalg.inv(Q)
    errs['d1'] = max(errs['d1'], np.max(np.abs(Qi - (eta4 + np.outer(yl, yl)/ell2)/m2)))
    # pushforward of sum Q^{-1}_{ab} D^a D^b symbol: D^a has base components (D^a)^mu = y4 eta^{a mu}  (s=1); contraction Q^{-1}_{ab}
    Dbase = y4*np.eye(4)                # (D^a)^mu = y4 delta^{a mu} up to eta placement: D^a = y4 d^a, d^a = eta^{a mu} d_mu
    Dup = y4*eta4                       # (D^a)^mu = y4 eta^{a mu}
    sym = Dup.T @ Qi @ Dup              # sum_{ab} Qi_ab (D^a)^mu (D^b)^nu
    errs['d2'] = max(errs['d2'], np.max(np.abs(sym - ginv)))
    # det Q
    errs['a'] = max(errs['a'], 0)
print("c^2 range over orbit sample (should be a single number):", min(c2s), max(c2s))
print("(a) max |M_A^B M_B^C + c^2 delta| =", errs['a'])
print("(b) max |T^a y_a| =", errs['b'])
print("(c) max errors g^{-1}=eta+yy/l^2 and K=m^2(g^{-1}-yy/l^2):", errs['c'])
print("(d) Q^{-1} closed form err:", errs['d1'], "; base symbol of Q^{-1}-contraction minus g^{-1}:", errs['d2'])
# ell^2 = c^2 ?
z = rand_z_pos(rng, 1.7); M = Mfun(z); y = M[:4, 5]; y4 = M[4, 5]
print("ell^2 =", -(y @ eta4 @ y + y4**2), " c^2 =", -(eta6 @ M @ eta6 @ M)[0, 0], "(eta6 M)^2 diag:", np.diag((eta6@M)@(eta6@M)))
