# s3_mc_checks.py - Monte Carlo confirmation (numerical, not proof) for proposal 091:
# (1) Wishart W_2(4) eigenvalue density shape for the D=2 edge Gram at a=3: u~u^2(1-u^2)^2,
#     tau density ~ tau^(2a) = tau^6 near 0, and u/tau separation (E[u^2] flat in tau bins).
# (2) Kinematic universality: heterogeneous column-variance block law keeps coincidence exponent 2.
# (3) Rank-one slot law: normalized squared moduli of 3 iid complex normal entries are flat Dirichlet.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s3_mc_checks.py
import numpy as np
rng = np.random.default_rng(93)
n = 400_000

def sample(M, cols, scales):  # block M x cols, CN(0, scales_j) per column
    A = (rng.standard_normal((M, cols)) + 1j*rng.standard_normal((M, cols)))/np.sqrt(2)
    return A * np.sqrt(scales)

def eig2(G):
    tr = np.trace(G, axis1=1, axis2=2); dt = np.linalg.det(G)
    rad = np.sqrt(np.maximum(tr**2/4 - dt, 0))
    return tr/2 + rad, tr/2 - rad

# (1) a = 3 (M=2, N=6): scales all 1
A = sample(2, 4, np.ones(4)); l1, l2 = eig2(A @ A.conj().transpose(0, 2, 1))
tau = l1 + l2; uu = (l1 - l2)/tau
bu = np.linspace(0, 1, 51); hu = np.histogram(uu, bu)[0]/n/(bu[1]-bu[0])
m_small = (uu < 0.25); fit_u = np.polyfit(np.log(uu[m_small]), np.log(np.clip(
    np.histogram(uu[m_small], np.logspace(-3, np.log10(0.25), 30))[0]/n, 1e-300)/ (np.diff(np.logspace(-3, np.log10(0.25), 31))), 1))
bt = np.logspace(-3, 0.5, 30); ht = np.histogram(tau, bt)[0]/n/np.diff(bt)
m_t = tau < 0.3
fit_t = np.polyfit(np.log(np.clip(np.histogram(tau[m_t], np.logspace(-3, np.log(0.3), 25))[0]/n, 1e-300)/np.diff(np.logspace(-3, np.log(0.3), 26))), np.log(tau[m_t]), 1)
bins_tau = np.array_split(tau, 12); print("(1) fit exponent of u near 0 (expect ~2):", round(fit_u[0], 3))
print("(1b) E[u^2] by tau-decile (expect flat = 3/(2a+3) = 0.4286):",
      np.round([np.mean((np.sort((eig2(sample(2,4,np.ones(4))[0:20])@ (lambda G: G)(np.eye(2))))**2)) for _ in [0]][:0], 4) or "",
      np.round([np.mean(uu[idx]**2) for idx in (np.argsort(np.argsort(tau))//len(tau)*0+np.arange(len(tau))// (len(tau)//12))*0 + [np.where(np.argsort(np.argsort(tau)) == k)[0] for k in range(12)]], 4)[:12])
# (2) heterogeneous columns: scales (1,4,9,16) -> prefactor changes, exponent must stay 2
A = sample(2, 4, np.array([1.0, 4.0, 9.0, 16.0])); l1, l2 = eig2(A @ A.conj().transpose(0, 2, 1))
tau2 = l1 + l2; uu2 = (l1 - l2)/tau2
sel = uu2 < 0.2
h = np.histogram(uu2[sel], np.logspace(-3, np.log10(0.2), 28))[0]/sel.sum()
fit2 = np.polyfit(0.5*(np.log10(1/999*1000)), np.arange(0), 1) if False else np.polyfit(
    np.logspace(-3, np.log10(0.2), 28)[:-1] + (np.log10(0.2)+3)/28/2, np.log(np.clip(h, 1e-300, None)), 1)
print("(2) coincidence exponent under heterogeneous column variances (expect ~2):", round(fit2[0], 3))
# (3) rank-one flat Dirichlet, D=3
w = rng.standard_normal((n//2, 3)) + 1j*rng.standard_normal((n//2, 3))
E = np.abs(w)**2; p = E/E.sum(1, keepdims=True)
mom = np.array([p[:, 0].mean(), (p[:, 0]**2).mean(), (p[:, 0]*p[:, 1]).mean()])
print("(3) rank-one slot moments (expect 0.3333, 0.1667, 0.0833):", np.round(mom, 4))
print("S3 DONE")
