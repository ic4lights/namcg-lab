"""023 script 1: leading symbols of the matrix-built Casimir-type operators on the six-dimensional leaf CP^{1,2}.
Quadratic form of an operator  sum_I w_I (J_I)^2  (J_I = Hamiltonian vector field of M^{AB}) is K = sum_I w_I v_I v_I^T on the 15-dim ambient
tangent coordinates, restricted to the 6-dim tangent space of the leaf (v_I span it).  Reports signatures at random orbit points."""
import numpy as np
from symbol_tools import *
rng = np.random.default_rng(5)
e6 = np.diag(eta6)
def forms(M0):
    V = {p: vec(M0, *p) for p in pairs}
    T = np.array([V[p] for p in pairs])                  # (15,15)
    u, sv, vh = np.linalg.svd(T); rk = int(np.sum(sv > 1e-9 * sv[0]))
    E = vh[:rk]                                          # orthonormal basis of tangent space
    c = {p: E @ V[p] for p in pairs}                     # coordinates in R^rk
    def K(sel, wfun):
        return sum(wfun(p) * np.outer(c[p], c[p]) for p in pairs if sel(p))
    eta = lambda p: eta6[p[0], p[0]] * eta6[p[1], p[1]]
    out = {}
    out['C42'] = K(lambda p: True, eta)
    out['C41'] = K(lambda p: p[1] <= 4, eta)
    out['C31'] = K(lambda p: p[1] <= 3, eta)
    out['Box4'] = K(lambda p: p[1] == 4 and p[0] <= 3, eta)    # sum_a eta_a (D^a)^2 ; eta(p)=eta_a*eta_4=eta_a
    out['Box4E'] = K(lambda p: p[1] == 4 and p[0] <= 3, lambda p: 1.0)
    out['C42-C41'] = out['C42'] - out['C41']
    out['Ccomp'] = K(lambda p: (p[0] >= 1 and p[1] <= 4) or p == (0, 5), lambda p: 1.0)   # sum of squares of maximal compact so(4)+so(2) generators (J^{ij}, i,j in 1..4 and J^{05})
    out['Sum15'] = K(lambda p: True, lambda p: 1.0)
    return rk, out
def sig(Kf):
    w = np.linalg.eigvalsh(Kf); tol = 1e-9 * max(1, np.max(np.abs(w)))
    return (int(np.sum(w > tol)), int(np.sum(w < -tol)), int(np.sum(np.abs(w) <= tol)))
if __name__ == "__main__":
    stats = {}
    best = []
    for t in range(40):
        z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
        rk, F = forms(M0)
        assert rk == 6
        for k, Kf in F.items():
            stats.setdefault(k, {}); s_ = sig(Kf); stats[k][s_] = stats[k].get(s_, 0) + 1
        # does a definite combination of {C42, C41, C31, Box4, Box4E} exist?  maximise lambda_min over unit coefficient vectors
        from scipy.optimize import minimize
        names = ['C42', 'C41', 'C31', 'Box4E']
        def f(c):
            c = c / np.linalg.norm(c)
            return -np.linalg.eigvalsh(sum(ci * F[n] for ci, n in zip(c, names)))[0]
        m = min((minimize(f, rng.normal(size=4), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 4000}) for _ in range(6)), key=lambda r: r.fun)
        best.append(-m.fun)
    print("signatures (n_plus, n_minus, n_zero) of the symbol forms at 40 random orbit points:")
    for k, v in stats.items(): print("  ", k, v)
    print("max over unit coefficient vectors of lambda_min(sum c_i K_i), i in {C42,C41,C31,Box4E}: max over points of the best value =", max(best), "(<=0 means no definite combination)")
