import sympy as sp
import jetlib as jl
from jetlib import Jet
from common import theta_from_omega
import su2_family as F
import geom
K, syms = F.make_field()
F.setup(K, 3)
w = F.omega_jets_su2(K, syms)
geom.SIGN_OVERRIDE = 1
Th = theta_from_omega(w)
# Pf omega at 0
print('Pf(omega)(0) =', K.to_sympy(jl.pf4(w).c0()))
J = [sum((Th[m][r]*Th[m][n].diff(r) for m in range(4) for r in range(4)), Jet()) for n in range(4)]
for n in range(4):
    print('J_%d(0) =' % (n+1), sp.factor(K.to_sympy(J[n].c0())))
