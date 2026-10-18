import numpy as np, sys
sys.dont_write_bytecode = True
from engine_d import second_order_gen
B, kappa, t = 0.8, 1.7, 0.35
alpha = np.array([0.6, -0.9]); y2 = 1.1
eta = np.eye(2); F = np.array([[0, B], [-B, 0.]])
Theta = B / (4 * np.pi * np.sinh(t * B))
s = -1j * t
for c0 in (0.0, 0.7):
    for pl in ('seam', 'left'):
        T = second_order_gen(F, eta, np.array([kappa, 0.]), alpha, np.array([0., y2]), c0, s, nquad=40, placement=pl)
        print("c0=%.1f placement=%s: Theta*T2/Theta = %.8f %+.2ej" % (c0, pl, (Theta * T).real, (Theta * T).imag))
