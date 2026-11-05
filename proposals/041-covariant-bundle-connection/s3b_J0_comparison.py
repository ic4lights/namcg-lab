"""s3b: same comparison as s3 on Poisson-class 3-jets constrained to J = 0 and dJ = 0 at the point (20 equations), found by least squares
over the quadratic and cubic coefficients of the potential A (omega = omega_bar + dA).  Prints the J-size and the operator mismatch."""
import sys, io, contextlib
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
from tj import Jets
J = s3.J; D = 4

def build_bg(params, w0, etad):
    A = np.zeros((D, J.M)); n = 0
    sel = [i for i, m in enumerate(J.mons) if 2 <= sum(m) <= 3]
    for mu in range(D):
        for i in sel:
            A[mu, i] = params[n]; n += 1
    om = np.zeros((D, D, J.M)); om[:, :, 0] = w0
    for m in range(D):
        for k in range(D):
            om[m, k] += J.d(A[k], m) - J.d(A[m], k)
    Th = J.inv_series(om)
    eta = np.diag(np.array(etad, float))
    etaJ = np.zeros((D, D, J.M)); etaJ[:, :, 0] = eta
    Pf = J.mul(om[0, 1], om[2, 3]) - J.mul(om[0, 2], om[1, 3]) + J.mul(om[0, 3], om[1, 2])
    sg = np.sign(Pf[0]); rho = sg*Pf; rhoi = s3.scal_inv(rho)
    K = J.matmul(J.matmul(np.transpose(Th, (1, 0, 2)), etaJ), Th)
    G = J.inv_series(K)
    return dict(eta=eta, etaJ=etaJ, om=om, Th=Th, rho=rho, rhoi=rhoi, K=K, G=G, sg=sg, Pf=Pf)

def resid(params, w0, etad):
    bg = build_bg(params, w0, etad)
    Jv = s3.Jvec(bg)
    r = list(Jv[:, 0]) + [J.d(Jv[nu], k)[0] for nu in range(D) for k in range(D)]
    return np.array(r)

q = np.array([0.3, -0.5, 0.7, 0.2])
for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for seed in (1, 2, 3):
        rng = np.random.default_rng(seed)
        while True:
            w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
            if abs(np.linalg.det(w0)) > 0.1: break
        n = 4*sum(1 for m in J.mons if 2 <= sum(m) <= 3)
        p0 = 0.15*rng.uniform(-1, 1, n)
        sol = least_squares(resid, p0, args=(w0, etad), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=60)
        bg = build_bg(sol.x, w0, etad)
        Jr = resid(sol.x, w0, etad)
        print(f'eta={etad} seed={seed}: residual |J(0), dJ(0)| = {np.linalg.norm(Jr):.2e}, |params|={np.linalg.norm(sol.x):.3f}')
        H, bjet = s3.H_jets(bg)
        opV = lambda A: s3.S_apply(bg, s3.Ov_apply(bg, s3.Sinv_apply(bg, A)))
        CV, aV, bV = s3.extract(opV)
        def make_opM(c, kappa):
            def op(A):
                P = s3.P_apply(bg, H, c, A)
                out = np.zeros_like(P)
                for lam in range(D):
                    for nu in range(D):
                        out[lam] += J.mul(J.mul(bg['G'][lam, nu], bg['rhoi']), P[nu])/kappa
                return out
            return op
        CM, aM, bM = s3.extract(make_opM(4.0, 4.0))
        print(f'   principal |C_V-C_M|={np.linalg.norm(CV-CM):.1e}; first-order |a_V-a_M|/|a_V|={np.linalg.norm(aV-aM)/np.linalg.norm(aV):.2e} (|a_V|={np.linalg.norm(aV):.2f}); '
              f'zeroth |b_V-b_M|/|b_V|={np.linalg.norm(bV-bM)/np.linalg.norm(bV):.2e} (|b_V|={np.linalg.norm(bV):.2f})')
