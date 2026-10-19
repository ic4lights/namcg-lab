import numpy as np, sys
sys.dont_write_bytecode = True
from engine_d import second_order_gen
from toy2d_direct import T2_direct
B, kappa, t = 0.02, 1.7, 0.35
alpha = np.array([0.6, -0.9]); y2 = 1.1; c0=0.0
eta = np.eye(2); F = np.array([[0, B], [-B, 0.]])
Theta = B / (4 * np.pi * np.sinh(t * B))
T = second_order_gen(F, eta, np.array([kappa, 0.]), alpha, np.array([0., y2]), c0, -1j*t, nquad=40)
print("seam", Theta*T)
print("direct", T2_direct(B, kappa, alpha, y2, c0, t, nphi=4, nk=60, kmax=None))
