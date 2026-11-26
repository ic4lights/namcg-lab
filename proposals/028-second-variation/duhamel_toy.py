"""028 script 8: toy check of the factorisation lemma with ARBITRARY (non-commuting, random) operators.
H: random symmetric N x N; Zop_ab: 16 random N x N matrices (no algebra imposed); window chi: random symmetric positive matrix (non-commuting with H).
Species (weights, Z-tensors, masses) as in tensors_lemma, with masses  vector mu2, extra scalars mi2, ghost 0, fermion 0.
f(t) = sum_i w_i Tr[ chi * exp(-(H (x) 1 + t Z_i + t^2 m_i)) ] , Z_i = sum_ab Zmat_i^{ab} (x) Zop_ab.
Claim: f(t) = f0 + t^2 * ( -sum_i w_i d_i m_i ) Tr[chi * ( -...)]  i.e. coefficients of t^0, t^1, t^3 vanish and the t^2 coefficient equals
   -M_str * Tr[chi e^{-H}]   (for Phi = exp(-.): first-order mass insertion is -m Tr[chi e^{-H}] ) ,  M_str = sum w_i d_i m_i ,
the t^4 coefficient is NOT of the form (species constants) x (common trace) only through (M_2, c_12, T_4) -- listed separately."""
import numpy as np, scipy.linalg as sl
from numpy.polynomial import chebyshev as Ch
import tensors_lemma as TL
rng = np.random.default_rng(8)
N = 5
H = rng.normal(size=(N, N)); H = H + H.T; H = H/np.linalg.norm(H, 2)
chi = rng.normal(size=(N, N)); chi = chi @ chi.T + np.eye(N)
Zop = {(a, b): 0.3*rng.normal(size=(N, N)) for a in range(4) for b in range(4)}
mu2, mi2 = -3.0, 0.7
masses = {"vector": mu2, "6 extra scalars": mi2, "ghost": 0.0, "16 real fermion comps": 0.0}
def f(t):
    tot = 0.0
    for w, Zt, d, name in TL.SP:
        dim = d
        Z = sum(np.kron(Zt[(a, b)], Zop[(a, b)]) for a in range(4) for b in range(4) if a != b)
        Hfull = np.kron(np.eye(dim), H) + t*Z + t**2*masses[name]*np.eye(dim*N)
        tot += w*np.trace(np.kron(np.eye(dim), chi) @ sl.expm(-Hfull))
    return tot
ts = np.linspace(-0.4, 0.4, 41)
vals = np.array([f(t) for t in ts])
deg = 14
V = np.vander(ts, deg + 1, increasing=True)
coef = np.linalg.lstsq(V, vals, rcond=None)[0]
Mstr = sum(w*d*masses[name] for w, Zt, d, name in TL.SP)
pred2 = -Mstr*np.trace(chi @ sl.expm(-H))
print("fit of f(t) = sum c_k t^k (degree 14, 41 nodes in [-0.4,0.4]):")
for k in range(6): print("  c_%d = %.3e" % (k, coef[k]))
print("M_str = sum w d m = %.4f ;  predicted c_2 = -M_str Tr[chi e^-H] = %.6e ;  fitted c_2 = %.6e" % (Mstr, pred2, coef[2]))
