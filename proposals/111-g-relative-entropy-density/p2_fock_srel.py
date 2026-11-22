"""P2: Fock ground truth for the full relative entropy S(rho1||rho0), G1 != G0,
on the certified cut (L=17,mu=0.7,N=1). Direct matrix Tr rho1(log rho1 - log rho0)
vs closed form -S1 + 1/2 Tr(A0 G1) - c0. Prints <= 6 scalar lines."""
import sys
sys.path.insert(0, '.')
import numpy as np
import _common as cm

def logm(m):
    w, V = np.linalg.eigh(0.5*(m + m.T))
    assert w.min() > 0, 'not PD'
    return (V * np.log(w)) @ V.conj().T

sites = np.arange(6, 7)
C, Pim = cm.restrict(17, 0.7, sites)
G0 = cm.G_block(C, Pim)
A0 = cm.A_of_G(G0)
nmax = 12
rho0, Z0 = cm.rho_fock(A0, nmax)

results = []
for seed in [7, 8, 9]:
    G1 = cm.rand_G(1, seed)
    A1 = cm.A_of_G(G1)
    rho1, Z1 = cm.rho_fock(A1, nmax)
    G1r = cm.cov_from_rho(rho1, 1, nmax)
    S1 = cm.entropy_from_G(G1r)
    direct = float(np.real(np.trace(rho1 @ (logm(rho1) - logm(rho0)))))
    form = cm.S_rel_formula(G1r, G0)
    results.append((direct, form))

for i, (d, f) in enumerate(results):
    print('seed %d direct=%.10f form=%.10f diff=%.2e' % (7+i, d, f, abs(d-f)))
# self-distance and positivity spot
G1 = cm.rand_G(1, 11)
A1 = cm.A_of_G(G1)
rho1, _ = cm.rho_fock(A1, nmax)
G1r = cm.cov_from_rho(rho1, 1, nmax)
d0 = float(np.real(np.trace(rho1 @ (logm(rho1) - logm(rho1)))) )
print('self Srel(G1,G1) direct=%.1e  form=%.1e' % (d0, cm.S_rel_formula(G1r, G1r)))
vals = [cm.S_rel_formula(cm.cov_from_rho(cm.rho_fock(cm.A_of_G(cm.rand_G(1, s)), nmax)[0], 1, nmax), G0) for s in range(21, 26)]
print('min Srel over 5 random G1 = %.4e (all >= 0: %s)' % (min(vals), all(v >= 0 for v in vals)))
