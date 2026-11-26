import sympy as sp
from common import *
import sd_family, sd_rot_family, base_a_side as B
use_gaussian(3)
bsol, eta, nf = sd_rot_family.rot_solution(4, 2)
d = B.run((0, 0, sp.Rational(0), sp.Rational(1)), bsol=bsol, eta=eta)
for k, v in d.items(): print(k, v, type(v))
