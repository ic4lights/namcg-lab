# s3_mc_checks_v3.py - Monte Carlo confirmation (numerical, not proof) for proposal 091.
# (1) Wishart edge Gram, M=2, N-M=4 (a=3): u=|p1-p2| CDF exponent ~3 near 0 (density exponent 2);
#     rescaled block, tau-density exponent near 0 ~ 2a = 6; E[u^2] flat across tau deciles (=1/3).
# (2) Kinematic universality: heterogeneous column variances keep u-CDF exponent ~3 (density 2).
# (3) Rank-one slot law: normalized squared moduli of 3 iid complex normals = flat Dirichlet moments.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s3_mc_checks_v3.py
import numpy as np
rng = np.random.default_rng(93)
n = 1_500_000

def block(M, cols, scales):
    A = (rng.standard_normal((n, M, cols)) + 1j*rng.standard_normal((n, M, cols)))/np.sqrt(2)
    return A * np.sqrt(scales)

def eig2(A):
    G = A @ A.conj().transpose(0, 2, 1)
    tr = np.trace(G, axis1=1, axis2=2); dt = np.linalg.det(G)
    rad = np.sqrt(np.maximum(tr**2/4 - dt, 0))
    return tr/2 + rad, tr/2 - rad

def cdf_slope(vals, lo, hi, nb=9):
    xs = np.logspace(np.log10(lo), np.log10(hi), nb)
    cnt = np.array([np.mean(vals < x) for x in xs]); ok = cnt > 0
    return np.polyfit(np.log(xs[ok]), np.log(cnt[ok]), 1)[0]

A = block(2, 4, np.ones(4)); l1, l2 = eig2(A)
tau = l1 + l2; uu = (l1 - l2)/tau
print("(1a) CDF exponent of u in [0.02,0.2] (expect ~3 = density exponent 2 + 1):",
      round(cdf_slope(uu, 0.02, 0.2), 3))
A = block(2, 4, np.full(4, 0.01)); l1, l2 = eig2(A)
tau_s = l1 + l2
xs = np.logspace(-3, np.log10(0.25), 22)
cnt = np.array([np.mean(tau_s < x) for x in xs]); ok = cnt > 0
print("(1b) tau-CDF exponent near 0, scale 0.01 block (expect ~2a+1 = 7):",
      round(np.polyfit(np.log(xs[ok]), np.log(cnt[ok]), 1)[0], 3))
order = np.argsort(tau); dec = np.array_split(order, 12)
print("(1c) E[u^2] by tau-decile (expect flat = 3/(2a+3) = 0.3333):",
      np.round([np.mean(uu[d]**2) for d in dec], 3))
A = block(2, 4, np.array([1.0, 4.0, 9.0, 16.0])); l1, l2 = eig2(A)
uu2 = (l1 - l2)/(l1 + l2)
print("(2) u-CDF exponent, heterogeneous column variances (expect ~3):",
      round(cdf_slope(uu2, 0.02, 0.2), 3))
w = rng.standard_normal((200_000, 3)) + 1j*rng.standard_normal((200_000, 3))
E = np.abs(w)**2; p = E/E.sum(1, keepdims=True)
print("(3) rank-one slot moments (expect 0.3333, 0.1667, 0.0833):",
      np.round([p[:, 0].mean(), (p[:, 0]**2).mean(), (p[:, 0]*p[:, 1]).mean()], 4))
print("S3-V3 DONE")
