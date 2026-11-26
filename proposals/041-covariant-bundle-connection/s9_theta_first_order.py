"""s9: first-order variation of the invariants rho and theta~ = rho*b (s2) under the plane-wave perturbation of the Poisson class about constant omega_bar:
omega = omega_bar + eps*(p_mu a_nu - p_nu a_mu) cos(p.x)  [a^mu = u^mu cos(p.x) with a_nu = omega_bar-lowered, i.e. the Moser form of the matrix fluctuation u].
Report the linear maps  u -> delta ln rho,  u -> delta theta~  (4 -> 1), their kernels, and whether delta theta~ vanishes on delta rho = 0 modes."""
import numpy as np
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
def pf(W): return W[0,1]*W[2,3]-W[0,2]*W[1,3]+W[0,3]*W[1,2]
def theta_t(W, eta):
    Th = np.linalg.inv(W)
    I1 = np.einsum('ac,bd,ab,cd->', eta, eta, Th, Th)
    b = -np.sign(pf(Th))*I1/8
    return abs(pf(W))*b, abs(pf(W))
rng = np.random.default_rng(0)
for etad in [(1,1,1,1), (-1,1,1,1)]:
    eta = np.diag(np.array(etad, float))
    for t in range(3):
        w0 = rng.uniform(-1,1,(4,4)); w0 = w0 - w0.T
        if abs(pf(w0)) < 0.2: continue
        p = rng.normal(size=4)
        # delta omega = eps (p_mu A_nu - p_nu A_mu),  A_nu = u^mu omega_{mu nu}
        def dth(u, eps=1e-6):
            A = u @ w0
            dw = np.outer(p, A) - np.outer(A, p)
            t1, r1 = theta_t(w0 + eps*dw, eta); t0, r0 = theta_t(w0 - eps*dw, eta)
            return (t1 - t0)/(2*eps), (np.log(r1) - np.log(r0))/(2*eps)
        Mt = np.zeros(4); Mr = np.zeros(4)
        for k in range(4):
            u = np.zeros(4); u[k] = 1.0
            Mt[k], Mr[k] = dth(u)
        q = np.linalg.inv(w0) @ p   # Theta p direction (gauge: u ~ q gives zero)
        print(f'eta={etad}: |delta theta~ on u=q| = {abs(Mt@(np.linalg.inv(w0)@p)):.1e}; delta ln rho vs p.u: ratio = {Mr/p}  (should be constant)')
        # kernel of delta ln rho (p.u = 0) intersect gauge quotient: does delta theta~ vanish there?
        # null space of Mr (3-dim) contains q; dimension of the intersection of ker(Mr) and ker(Mt):
        S = np.vstack([Mr, Mt]); sv = np.linalg.svd(S, compute_uv=False)
        print(f'   rank[d ln rho; d theta~] = {np.sum(sv > 1e-6*sv[0])} (of 2): d theta~ is {"independent of" if np.sum(sv>1e-6*sv[0])==2 else "proportional to"} d ln rho on the 4-dim u-space')
        # components: d theta~ = c . u ; in terms of p: express Mt in basis
        print('   d theta~ / (p) componentwise ratio:', Mt/p)
