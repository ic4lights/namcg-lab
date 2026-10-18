import numpy as np, sys
sys.dont_write_bytecode = True
from engine_e import second_order_e
B, kappa, t = 0.8, 1.7, 0.35
alpha = np.array([0.6, -0.9]); y2 = 1.1
eta = np.eye(2); F = np.array([[0, B], [-B, 0.]]); Theta = B / (4 * np.pi * np.sinh(t * B))
for c0, ref in ((0.0, 0.08491501), (0.7, 0.08262229)):
    T = second_order_e(F, eta, np.array([kappa, 0.]), alpha, np.array([0., y2]), c0, -1j * t, nquad=24)
    print("c0=%.1f engine_e: %.8f %+.1ej   direct: %.8f" % (c0, (Theta * T).real, (Theta * T).imag, ref))
