"""034 test 1: engine_c (central Y at the seam) against engine.second_order (interleaved factors) at F = 0, where they must coincide (Y commutes with omega); and at F != 0 where they differ."""
import numpy as np, sys
sys.dont_write_bytecode = True
from engine import second_order, eta
from engine_c import second_order_central
rng = np.random.default_rng(3)
kappa = rng.normal(size=4); kup = eta @ kappa
y = rng.normal(size=4); y = y - kup * (y @ kappa) / (kup @ kappa)       # y.kappa = 0
alpha = rng.normal(size=4); c0 = 0.8
m = -np.outer(alpha, y); n = -alpha * c0
for F0 in (0.0, 1e-6):
    Fm = np.zeros((4, 4)); Fm[0, 1] = F0; Fm[1, 0] = -F0; Fm[2, 3] = 1.3 * F0; Fm[3, 2] = -1.3 * F0
    for s in (0.3, 0.9 - 0.2j):
        t_old = second_order(Fm, kappa, m, n, s, nquad=30)
        t_new = second_order_central(Fm, kappa, alpha, y, c0, s, nquad=30)
        print("F=%g s=%s  interleaved %s   central %s   rel.diff %.2e" % (F0, s, np.round(t_old, 10), np.round(t_new, 10), abs(t_old - t_new) / abs(t_old)))
Fm = np.zeros((4, 4)); Fm[0, 1] = 0.7; Fm[1, 0] = -0.7; Fm[2, 3] = 1.3; Fm[3, 2] = -1.3
for s in (0.3, 0.9 - 0.2j):
    t_old = second_order(Fm, kappa, m, n, s, nquad=30); t_new = second_order_central(Fm, kappa, alpha, y, c0, s, nquad=30)
    print("F=(0.7,1.3) s=%s: interleaved %s central %s rel.diff %.2e" % (s, np.round(t_old, 8), np.round(t_new, 8), abs(t_old - t_new) / abs(t_old)))
