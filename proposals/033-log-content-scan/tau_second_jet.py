"""Second-jet dependence of the normal-plane scalar tau = tr_V(J Omega^v_12) at generic closed omega.
Hold omega(0), d omega(0) fixed, vary the second jet; regress delta tau on delta of the curvature scalars (R, R_ii, R_ijij) and of the
endomorphism data (e, X', tr_N E_G).  Exact rational solve.  If delta tau lies in the span, tau = (combination of curvature) + (function of the first jet)."""
import sys
import sympy as sp
from common import *
import omega_vs_riemann as O
import jetlib as jl
import sector_data as S
use_gaussian(3)
base_vals = None
rows = []
names = ['R', 'Rii', 'Rijij', 'e', 'Xp', 'trN_EG']
K = 12
for k in range(K):
    Aj = O.A_jets(11, 100 + k, 31)
    w = omega_from_A(Aj)
    w = [[w[m][n] + jl.Jet.const(O.base[m][n]) for n in range(4)] for m in range(4)]
    d = S.run_jets(w)
    vec = [d[n] for n in names] + [d['trJOm_v'], d['tau']]
    if base_vals is None:
        base_vals = vec
    rows.append([vec[i] - base_vals[i] for i in range(len(vec))])
    print('sample', k); sys.stdout.flush()
M = sp.Matrix(rows[1:])
X = M[:, :6]; yv = M[:, 6]; yt = M[:, 7]
print('rank of curvature/endomorphism variations:', X.rank(), 'of', X.cols)
print('rank [X | dtau_v]:', X.row_join(yv).rank())
print('rank [X | dtau_f]:', X.row_join(yt).rank())
# try subsets
import itertools
for sub in itertools.combinations(range(6), 3):
    Xs = X[:, list(sub)]
    print('subset', [names[i] for i in sub], ' rank', Xs.rank(), ' rank with dtau_v', Xs.row_join(yv).rank())
