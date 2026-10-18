"""Full-tensor version of omega_riemann_map.py: is the second-jet part of the vector bundle curvature Omega^v (all 6 form pairs, 16 matrix entries)
a fixed linear image of the second-jet part of the full Levi-Civita Riemann tensor R^r_{l s t} (all 96 chart components, 20 independent)?
Compare ranks: rank dR, rank dOmega, rank of the joint matrix.  K samples with first jet fixed."""
import sys, pickle
import sympy as sp
from common import *
import omega_vs_riemann as O
K = int(sys.argv[1]) if len(sys.argv) > 1 else 45
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
base_data = O.data(O.A_jets(11, 21, 31))
rows_O = []; rows_R = []
for k in range(K):
    Th0, Rl, Om = O.data(O.A_jets(11, 100 + k, 31))
    rows_O.append([Om[s][t][a, b] - base_data[2][s][t][a, b] for (s, t) in pairs for a in range(4) for b in range(4)])
    rows_R.append([Rl[(r, l, s, t)] - base_data[1][(r, l, s, t)] for (s, t) in pairs for r in range(4) for l in range(4)])
    print('sample', k); sys.stdout.flush()
pickle.dump((rows_O, rows_R), open('omega_riemann_full.pkl', 'wb'))
MO = sp.Matrix(rows_O); MR = sp.Matrix(rows_R)
rO, rR, rJ = MO.rank(), MR.rank(), MR.row_join(MO).rank()
print('K =', K, ' rank dR =', rR, ' rank dOmega =', rO, ' rank joint =', rJ)
print('dOmega is a linear image of dR (full tensor) iff joint rank == rank dR:', rJ == rR)
