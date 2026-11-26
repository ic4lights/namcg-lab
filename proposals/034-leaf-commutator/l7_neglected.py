"""034 script 7: size of the terms dropped at the nilpotent order, relative to the kept flux commutator.
Exact: [W_a,Y] = -q^a V has no vertical part (V horizontal).  In the frame (W_a,Z_k): vertical part 0 = y^c S_ac^k + (W_a y^k) + y^l (vertical part of [W_a,Z_l]);
the model keeps Y central.  Dropped weight-1 terms: horizontal part h_a of [W_a,Y].  Ratio r = |h| / |y^c S_ac| has dimension 1/(centre momentum): the dropped term is small iff |zeta| >> r (and omega small).
Also: |y^c S_ac| / (|y||S|)."""
import numpy as np, sys
sys.dont_write_bytecode = True
from leafdata import *
rng = np.random.default_rng(3)
print("pt | |vertical part of [W_a,Y]| | |horizontal part| | |y^c S_ac^k| (per unit zeta) | r = |h|/|yS| ")
for t in range(6):
    M0 = rand_point(rng); q = rng.normal(size=4)
    d = leaf_data(M0, q)
    vert = max(np.abs(d['WY'][a][1]).max() for a in range(4))
    hor = np.linalg.norm([d['WY'][a][0] for a in range(4)])
    yS = np.linalg.norm(np.einsum('c,ack->ak', d['y'], d['S']))
    print("%d | %.1e | %.3e | %.3e | %.3e" % (t, vert, hor, yS, hor / yS))
