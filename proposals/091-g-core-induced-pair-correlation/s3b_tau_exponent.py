# s3b_tau_exponent.py - tau = tr G small-value exponent for the rescaled Wishart edge block
# (M=2, cols=4, sigma^2=0.01). Theory: joint eigenvalue density ~ (l1 l2)^2 (l1-l2)^2 e^{-(l1+l2)/s2},
# so tau-density ~ tau^7 e^{-tau/s2} (Gamma(8)) and the tau-CDF exponent near 0 is 8.
# Also checks E[u^2] flat across tau-deciles for this rescaled sample.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s3b_tau_exponent.py
import numpy as np
rng = np.random.default_rng(97)
n = 400_000
A = (rng.standard_normal((n, 2, 4)) + 1j*rng.standard_normal((n, 2, 4)))/np.sqrt(2)*0.1
G = A @ A.conj().transpose(0, 2, 1)
tr = np.trace(G, axis1=1, axis2=2).real
dt = np.linalg.det(G).real
rad = np.sqrt(np.maximum(tr**2/4 - dt, 0))
tau = tr; uu = (2*rad)/tr
xs = np.logspace(-3, np.log10(0.02), 20)
cnt = np.array([np.mean(tau < x) for x in xs]); ok = cnt > 0
print("(1b') tau-CDF exponent near 0, window [1e-3,0.02] (expect ~8 = Gamma(8) shape):",
      round(np.polyfit(np.log(xs[ok]), np.log(cnt[ok]), 1)[0], 3))
order = np.argsort(tau); dec = np.array_split(order, 10)
print("(1b'') E[u^2] by tau-decile (expect flat ~1/3):",
      np.round(np.real([np.mean(uu[d]**2) for d in dec]), 3))
print("S3B DONE")
