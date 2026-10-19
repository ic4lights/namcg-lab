"""034 test 3: gauge invariance alpha -> alpha + lam*kappa of the corrected central-Y engine (4D, Lorentz eta) at F != 0, y != 0, and equality with engine.second_order at F = 0."""
import numpy as np, sys
sys.dont_write_bytecode = True
from engine import second_order, eta
from engine_e import second_order_e
rng = np.random.default_rng(5)
kappa = rng.normal(size=4); kup = eta @ kappa
y = rng.normal(size=4); y = y - kup * (y @ kappa) / (kup @ kappa)
alpha = rng.normal(size=4); c0 = 0.8; lam = 0.37
Z = np.zeros((4, 4))
for s in (0.4, 0.9 - 0.3j):
    t_old = second_order(Z, kappa, -np.outer(alpha, y), -alpha * c0, s, nquad=30)
    t_new = second_order_e(Z + 1e-9 * np.array([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1.3], [0, 0, -1.3, 0]]), eta, kappa, alpha, y, c0, s, nquad=20)
    print("F->0, s=%s: old %s  new %s  rel.diff %.1e" % (s, np.round(t_old, 8), np.round(t_new, 8), abs(t_old - t_new) / abs(t_old)))
for (a, b) in ((0.7, 1.3), (1.9, 1.0)):
    F = np.zeros((4, 4)); F[0, 1] = a; F[1, 0] = -a; F[2, 3] = b; F[3, 2] = -b
    for s in (0.4, 0.9 - 0.3j):
        f = lambda al: second_order_e(F, eta, kappa, al, y, c0, s, nquad=20)
        d = abs(f(alpha + lam * kappa) - f(alpha)) / abs(f(alpha))
        print("(a,b)=(%.1f,%.1f) s=%s: relative change under alpha->alpha+lam kappa: %.2e   T2=%s" % (a, b, s, d, np.round(f(alpha), 8)))
