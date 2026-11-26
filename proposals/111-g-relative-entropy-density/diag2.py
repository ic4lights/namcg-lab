import sys, os
sys.path.insert(0, os.getcwd())
import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=100)
import _common as cm

for (L, mu, N) in [(41, 0.01, 12), (61, 0.01, 12), (41, 0.02, 12)]:
    C, P = cm.restrict(L, mu, np.arange(6, 6 + N))
    G = cm.G_block(C, P)
    nu = cm.nus(G)
    O = cm.omega(N)
    wG, U = np.linalg.eigh(0.5 * (G + G.T))
    sq = U @ np.diag(np.sqrt(wG)) @ U.T
    isq = U @ np.diag(1.0 / np.sqrt(wG)) @ U.T
    Kh = -1j * (sq @ O @ sq)
    hw, HV = np.linalg.eigh(Kh)
    Kf = HV @ np.diag(np.sign(hw) * cm.hvec(np.abs(hw))) @ HV.conj().T
    A = -1j * ((isq @ Kf @ sq) @ O)
    sc = np.max(np.abs(A.real))
    print("L=%d mu=%.2f N=%d nu-.5 min=%.2e  |A.im|=%.2e scale=%.2e ratio=%.2e asym=%.2e"
          % (L, mu, N, (nu - 0.5).min(), np.max(np.abs(A.imag)), sc,
             np.max(np.abs(A.imag)) / sc, np.max(np.abs(A.real - A.real.T)) / sc))
