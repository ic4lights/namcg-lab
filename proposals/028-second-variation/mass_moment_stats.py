"""028 script 4: statistics of the signature of Q_ab = d^2 Re N / d eps^2 (mass-moment Hessian along alpha) over random orbit points and random q, window kappa=3/4;
and Q along the gauge-like direction alpha^a = q^a (index raised with eta)."""
import numpy as np
from mass_moment_hessian import *
rng = np.random.default_rng(21)
cnt = {"pos": 0, "neg": 0, "indef": 0}; gauge = []
nt = 60
for t in range(nt):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); q = rng.normal(size=4)
    W, Yq, P, wf = setup(M0, q)
    n00 = Nmoment(W, P).real
    if n00 < 1e-12: continue
    Q = np.zeros((4, 4))
    for i in range(4):
        for j in range(i, 4):
            ei = np.eye(4)[i]; ej = np.eye(4)[j]
            Qi = derivs(W, Yq, P, ei)[2].real; Qj = derivs(W, Yq, P, ej)[2].real; Qij = derivs(W, Yq, P, ei + ej)[2].real
            Q[i, j] = Q[j, i] = (Qij - Qi - Qj)/2 if i != j else Qi
    ev = np.linalg.eigvalsh(Q)
    if ev.min() > 0: cnt["pos"] += 1
    elif ev.max() < 0: cnt["neg"] += 1
    else: cnt["indef"] += 1
    qup = eta4 @ q
    gauge.append(derivs(W, Yq, P, qup)[2].real/(n00*(qup @ qup + 1e-300)) if abs(qup @ qup) > 1e-3 else np.nan)
print("signature of Q over %d (point,q) draws:" % sum(cnt.values()), cnt)
g = np.array([x for x in gauge if np.isfinite(x)])
print("Q(alpha=q^a)/(Re N(0) |q|^2_eta): min %.3f median %.3f max %.3f ; nonzero in all cases: %s" % (g.min(), np.median(g), g.max(), bool(np.all(np.abs(g) > 1e-6))))
