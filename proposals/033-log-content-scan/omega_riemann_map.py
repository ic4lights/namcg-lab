"""Second-jet dependence of the vector bundle curvature Omega^v versus the Levi-Civita curvature R^r_{l s t} (chart components).
Hold omega(0), d omega(0) fixed; vary the second jet (cubic part of the potential).  For the form pair (s,t)=(0,1) collect the
variations dOmega[a][b] (16 numbers) and dR[r][l] (16 numbers) over K samples and solve for the linear map dOmega = M (dR) (exact rational least squares).
Residual zero  <=>  the second-jet part of Omega^v is a fixed linear image of the Riemann tensor at fixed first jet."""
import sys
import sympy as sp
from common import *
import omega_vs_riemann as O
K = 20
base_data = O.data(O.A_jets(11, 21, 31))
rows_O = []; rows_R = []
for k in range(K):
    d = O.data(O.A_jets(11, 100 + k, 31))
    Th0, Rl, Om = d
    rows_O.append([Om[0][1][a, b] - base_data[2][0][1][a, b] for a in range(4) for b in range(4)])
    rows_R.append([Rl[(r, l, 0, 1)] - base_data[1][(r, l, 0, 1)] for r in range(4) for l in range(4)])
    print('sample', k); sys.stdout.flush()
MO = sp.Matrix(rows_O); MR = sp.Matrix(rows_R)          # K x 16
print('rank dOmega', MO.rank(), ' rank dR', MR.rank())
# solve MR * X = MO  (X 16x16) exactly if consistent
aug = MR.row_join(MO)
print('rank [dR | dOmega] =', aug.rank(), ' (equal to rank dR iff dOmega is a linear image of dR)')
