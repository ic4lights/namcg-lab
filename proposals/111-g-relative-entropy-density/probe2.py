import sys, os
sys.path.insert(0, os.getcwd())
import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=100)
import _common as cm

# (a) S_rel closed form vs Fock ground truth
for n, seed in [(1, 1), (2, 2)]:
    G0 = cm.rand_G(n, seed)
    G1 = cm.rand_G(n, seed + 5)
    A0, A1 = cm.A_of_G(G0), cm.A_of_G(G1)
    nmax = 16 if n == 1 else 10
    sf = cm.S_rel_formula(G1, G0)
    sk = cm.S_rel_fock(A1, A0, nmax)
    print("n=%d S_rel form=%.6f fock=%.6f diff=%.2e" % (n, sf, sk, abs(sf - sk)))

# chain-cut pair, N=2
def cutG(L, mu, N, s=4):
    C, P = cm.restrict(L, mu, np.arange(s, s + N))
    return cm.G_block(C, P)
G0 = cutG(17, 0.7, 2); G1 = cutG(17, 0.9, 2)
sf = cm.S_rel_formula(G1, G0)
sk = cm.S_rel_fock(cm.A_of_G(G1), cm.A_of_G(G0), 12)
print("cut2 S_rel form=%.6f fock=%.6f diff=%.2e" % (sf, sk, abs(sf - sk)))
# self
print("self S_rel=%.2e" % cm.S_rel_formula(G0, G0))

# (b) manuscript anchor: saturation entropy vs (1/3)ln(1/mu)+b(mu)
for mu in [0.3, 0.1]:
    for L, N in [(401, 48), (401, 96), (801, 96)]:
        S = cm.entropy_from_G(cutG(L, mu, N))
        print("mu=%.2f L=%d N=%d S=%.6f target=%.6f" %
              (mu, L, N, S, (1/3)*np.log(1/mu) + (0.01740 if mu == 0.3 else 0.00263)))

# (c) near-pure cuts: A_of_G + first law now work?
for (L, mu, N) in [(31, 0.05, 8), (41, 0.01, 12)]:
    G0 = cutG(L, mu, N, s=6)
    A0 = cm.A_of_G(G0)
    ev = np.linalg.eigvalsh(A0)
    t = cm.S_rel_terms(G0, G0)
    print("L=%d mu=%.2f N=%d A0min=%.3e firstlaw=%.2e" % (L, mu, N, ev.min(), abs(t["tA0"] - t["S0"])))
