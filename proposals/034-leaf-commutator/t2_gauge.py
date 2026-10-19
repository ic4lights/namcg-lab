"""034 test 2: invariance of T2(s) under alpha -> alpha + lam*kappa (the leaf gauge transformation delta A^a = {Lambda, T^a}, Lambda = lam sin(phi)).
Central-Y model: exact (H(alpha+lam kappa) = U H(alpha) U^-1, U = exp(-i eps lam cos(phi) Y)).  Interleaved model (Y -> y^c omega_c + c0 inside V1, as in 032): violated at F != 0 when y != 0."""
import numpy as np, sys
sys.dont_write_bytecode = True
from engine import second_order, eta
from engine_c import second_order_central
rng = np.random.default_rng(5)
kappa = rng.normal(size=4); kup = eta @ kappa
y = rng.normal(size=4); y = y - kup * (y @ kappa) / (kup @ kappa)
alpha = rng.normal(size=4); c0 = 0.8; lam = 0.37
def inter(F, al, s):
    return second_order(F, kappa, -np.outer(al, y), -al * c0, s, nquad=30)
def cent(F, al, s):
    return second_order_central(F, kappa, al, y, c0, s, nquad=30)
for (a, b) in ((0.0, 0.0), (0.7, 1.3), (1.9, 1.0)):
    F = np.zeros((4, 4)); F[0, 1] = a; F[1, 0] = -a; F[2, 3] = b; F[3, 2] = -b
    for s in (0.4, 0.9 - 0.3j):
        al2 = alpha + lam * kappa
        # quadratic form differences: T2 is a quadratic form in alpha
        di = abs(inter(F, al2, s) - inter(F, alpha, s)) / abs(inter(F, alpha, s))
        dc = abs(cent(F, al2, s) - cent(F, alpha, s)) / abs(cent(F, alpha, s))
        print("(a,b)=(%.1f,%.1f) s=%s: relative change under alpha->alpha+lam*kappa:  interleaved %.2e   central %.2e" % (a, b, s, di, dc))
