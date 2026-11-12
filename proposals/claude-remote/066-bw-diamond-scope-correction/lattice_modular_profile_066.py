"""Proposal 066 illustration (not a proof).
Free-fermion chain H = -1/2 sum (c_i^+ c_{i+1} + h.c.) + m sum (-1)^i n_i, ground state at half filling.
Entanglement (modular) Hamiltonian of an interval of l sites via Peschel: h = ln[(1-C)/C]^T, C_ij=<c_i^+ c_j>.
Compares the nearest-neighbour coefficient profile with the local conformal (diamond) profile
beta(x)=2*pi*x*(l-x)/l times the hopping 1/2, and measures the weight of longer-range terms.
Massless: close to the local parabolic (diamond / conformal-Killing) form, up to known lattice corrections.
Massive: the profile departs from the parabola. This illustrates only that the geometric diamond form
is a massless feature in a lattice model; it proves nothing about the continuum theorem.
"""
import numpy as np

def interval_h(m, N=1200, l=12):
    H = np.zeros((N, N))
    for i in range(N - 1):
        H[i, i + 1] = H[i + 1, i] = -0.5
    for i in range(N):
        H[i, i] = m * (-1) ** i
    e, U = np.linalg.eigh(H)
    occ = U[:, : N // 2]
    C = occ @ occ.T
    s = N // 2 - l // 2
    Cl = C[s:s + l, s:s + l]
    z, V = np.linalg.eigh(Cl)
    z = np.clip(z, 1e-15, 1 - 1e-15)
    eps = np.log((1 - z) / z)
    return V @ np.diag(eps) @ V.T, float(np.max(np.abs(eps)))

l = 12
for m in [0.0, 0.2, 0.5]:
    h, emax = interval_h(m, l=l)
    nn = np.array([h[i, i + 1] for i in range(l - 1)])
    x = np.arange(1, l)
    beta_hop = -0.5 * 2 * np.pi * x * (l - x) / l
    rel = np.max(np.abs(nn - beta_hop)) / np.max(np.abs(beta_hop))
    mask = np.abs(np.subtract.outer(np.arange(l), np.arange(l))) >= 2
    off = np.linalg.norm(h[mask]) / np.linalg.norm(h)
    print(f"m={m:4.2f} max|eps|={emax:6.2f}  NN profile rel.dev from conformal parabola={rel:6.3f}  "
          f"weight of |i-j|>=2 terms={off:6.3f}")
    print("   NN/beta_hop:", np.round(nn / beta_hop, 3))
