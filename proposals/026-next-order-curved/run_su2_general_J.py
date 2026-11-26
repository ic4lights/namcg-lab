"""J(0) for the general SU(2)-invariant family, reduced by the right-SU(2)/scaling gauge at r0=1:
h(r0) = (p,0,0), h'(r0) = (q,s,0), h''(r0) = (x,y,z).  Symbols p,q,s,x,y,z over Q."""
import sympy as sp
from sympy import QQ
import jetlib as jl
from jetlib import Jet
from common import theta_from_omega
import su2_general as SG
import geom
p, q, s, x, y, z = sp.symbols('p q s x y z')
K = QQ.frac_field(p, q, s, x, y, z)
jl.set_field(K.one, K.zero); jl.set_order(3)
zero = K.zero
c = [[K.convert(p), K.convert(q), K.convert(x), zero],
     [zero, K.convert(s), K.convert(y), zero],
     [zero, zero, K.convert(z), zero]]
w = SG.build_omega(K, c)
geom.SIGN_OVERRIDE = 1
Th = theta_from_omega(w)
print('Pf omega =', sp.factor(K.to_sympy(jl.pf4(w).c0())))
J = [sum((Th[m][r]*Th[m][n].diff(r) for m in range(4) for r in range(4)), Jet()) for n in range(4)]
import pickle
Js = []
for n in range(4):
    e = sp.factor(K.to_sympy(J[n].c0()))
    Js.append(e)
    print('J_%d =' % (n+1), e)
pickle.dump(Js, open('su2_general_J.pkl', 'wb'))
