import sys, os
sys.path.insert(0, os.getcwd())
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=100)
import _common as cm

def cutG(L, mu, N, s=4):
    C, P = cm.restrict(L, mu, np.arange(s, s + N))
    return cm.G_block(C, P)

# single-mode squeezed exact check A0 = h*nu*G^{-1}
for r in [1.0, 2.0]:
    nu = 0.9
    G = np.array([[nu / r**2, 0.0], [0.0, nu * r**2]])
    h = np.log((nu + 0.5) / (nu - 0.5))
    A = cm.A_of_G(G)
    print("sqz r=%.1f |A0 - h nu G^{-1}|=%.2e" % (r, np.max(np.abs(A - h * nu * np.linalg.inv(G)))))

# first law (with c0) and Fock covariance roundtrip
for n, seed in [(1, 1), (2, 2)]:
    G = cm.rand_G(n, seed)
    A = cm.A_of_G(G)
    S0 = cm.entropy_from_G(G)
    lhs = 0.5 * np.trace(A @ G) - cm.c0_from_nus(cm.nus(G))
    rho, Z = cm.rho_fock(A, 16 if n == 1 else 10)
    Gr = cm.cov_from_rho(rho, n, 16 if n == 1 else 10)
    print("n=%d firstlaw diff=%.2e  cov roundtrip=%.2e  lnZ+c0=%.2e"
          % (n, abs(lhs - S0), np.max(np.abs(Gr - G)), abs(np.log(Z) + cm.c0_from_nus(cm.nus(G)))))

# S_rel vs Fock ground truth
for n, seed in [(1, 1), (2, 2)]:
    G0, G1 = cm.rand_G(n, seed), cm.rand_G(n, seed + 5)
    nmax = 16 if n == 1 else 10
    sf = cm.S_rel_formula(G1, G0)
    sk = cm.S_rel_fock(cm.A_of_G(G1), cm.A_of_G(G0), nmax)
    print("n=%d S_rel form=%.6f fock=%.6f diff=%.2e" % (n, sf, sk, abs(sf - sk)))
G0, G1 = cutG(17, 0.7, 2), cutG(17, 0.9, 2)
sf, sk = cm.S_rel_formula(G1, G0), cm.S_rel_fock(cm.A_of_G(G1), cm.A_of_G(G0), 12)
print("cut2 S_rel form=%.6f fock=%.6f diff=%.2e self=%.2e"
      % (sf, sk, abs(sf - sk), cm.S_rel_formula(G0, G0)))

# near-pure cuts
for (L, mu, N) in [(31, 0.05, 8), (41, 0.01, 12)]:
    G = cutG(L, mu, N, s=6)
    A = cm.A_of_G(G)
    t = cm.S_rel_terms(G, G)
    print("L=%d mu=%.2f N=%d A0min=%.3e firstlaw=%.2e self=%.2e"
          % (L, mu, N, np.linalg.eigvalsh(A).min(), abs(t["tA0"] - t["c0"] - t["S0"]),
             cm.S_rel_formula(G, G)))

# old B-route agreement at moderate states (regression vs dead pass)
def A_old(G):
    n = G.shape[0] // 2
    O = cm.omega(n); Oi = -O
    w, U = np.linalg.eigh(G)
    sq = U @ np.diag(np.sqrt(w)) @ U.T
    isq = U @ np.diag(1.0 / np.sqrt(w)) @ U.T
    B = (-0.5j) * np.linalg.inv(sq @ Oi @ sq)
    bw, BV = np.linalg.eigh((B + B.conj().T) / 2)
    fB = BV @ np.diag(np.arctanh(np.clip(bw, -1 + 1e-12, 1 - 1e-12))) @ BV.conj().T
    return (2j * ((isq @ fB @ sq) @ Oi)).real
for (L, mu, N) in [(17, 0.7, 1), (19, 0.4, 2), (23, 0.25, 3)]:
    G = cutG(L, mu, N)
    print("regress L=%d mu=%.2f N=%d |Anew-Aold|=%.2e" % (L, mu, N, np.max(np.abs(cm.A_of_G(G) - A_old(G)))))
