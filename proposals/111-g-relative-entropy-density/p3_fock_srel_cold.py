"""P3 (final): decomposition of the direct-vs-form gap of P2 on the certified cut
(L=17,mu=0.7,N=1) for cold covariances nu in [0.55,0.65], nmax=16.
For any rho1 and faithful Gaussian sigma0 = exp(-K0)/Z0:
  S(rho1||sigma0) = -S(rho1) + <K0>_{rho1},  <K0> = 1/2 Tr(A0 G1) - c0  (exact algebra).
Direct uses Fock matrices; form uses spectral entropy of the covariance.
Prints 3 lines: gap sits in the entropy term, not the K0 term.
(First P3 attempt as standalone hit log-underflow nan on cold rho0; clipped eigh below.)"""
import sys
sys.path.insert(0, '.')
import numpy as np
import _common as cm

def trlog(Gother, m):
    w, V = np.linalg.eigh(0.5*(m + m.T))
    lg = np.log(np.clip(w, 1e-300, None))
    return float(np.real(np.trace(Gother @ ((V * lg) @ V.conj().T))))

C, Pim = cm.restrict(17, 0.7, np.arange(6, 7))
G0 = cm.G_block(C, Pim)
A0 = cm.A_of_G(G0)
c0 = cm.c0_from_G_alt(G0)
rho0, _ = cm.rho_fock(A0, 16)
for seed in [7, 8]:
    G1 = cm.rand_G(1, seed, nu_lo=0.55, nu_hi=0.65)
    rho1, _ = cm.rho_fock(cm.A_of_G(G1), 16)
    G1r = cm.cov_from_rho(rho1, 1, 16)
    K0_form = 0.5*float(np.trace(A0 @ G1r)) - c0
    K0_dir = -trlog(rho1, rho0)
    S_dir = -trlog(rho1, rho1)
    S_spec = cm.entropy_from_G(G1r)
    print('seed %d  K0_form=%.8f K0_dir=%.8f gapK=%.1e  |  S_spec=%.8f S_dir=%.8f gapS=%.1e'
          % (seed, K0_form, K0_dir, abs(K0_form-K0_dir), S_spec, S_dir, abs(S_spec-S_dir)))
