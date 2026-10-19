"""037-a2: dependence of <Omega,R> on the identification of the fibre (matrix) index with the chart index.
Variants: identity (manuscript convention x^mu = X^mu); conjugation by the coframe e = omega-bar = Theta-bar^{-1} (and its inverse)."""
import sympy as sp
from modes_lib import *
for name, Thb in backgrounds():
    ms = modes(Thb, 6, 21)
    e = Thb.inv()  # omega-bar
    print('==', name, 'e =', e.tolist())
    g0 = ms[0]['g0']
    for label, Tm in (('identity', sp.eye(4)), ('e Om e^-1', e/ sp.sqrt(g0)), ('e^-1 Om e', (e/sp.sqrt(g0)).inv())):
        vals = []
        for m in ms:
            Om = {k: Tm*v*Tm.inv() for k, v in m['Om'].items()}
            R = m['Rmat']
            vals.append((sp.simplify(ip(Om, R, m['g0'])/m['C2']), sp.simplify(ip(Om, Om, m['g0'])/m['C2']), sp.simplify((gen(0,1)*Om[(0,1)]).trace()/m['g0'] + m['Rj'])))
        print(' ', label, ': (<Om,R>/C2, <Om,Om>/C2, ell(Om)+R_ijij) values', sorted(set(vals)))
