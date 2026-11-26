import numpy as np, sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as cm
t0=time.time()
G0 = cm.rand_G(3, 3)
A0 = cm.A_of_G(G0)
for nmax in [9, 11]:
    rho, Z = cm.rho_fock(A0, nmax)
    Gr = cm.cov_from_rho(rho, 3, nmax)
    sc = np.max(np.abs(G0))
    print("nmax=%d relcov=%.3e t=%.1fs" % (nmax, np.max(np.abs(Gr-G0))/sc, time.time()-t0))
