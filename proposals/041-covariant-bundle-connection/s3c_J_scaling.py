"""s3c: the mismatch between the matrix vector operator (Moser variables) and the covariant Maxwell-axion operator is first order in J.
Start from a J = dJ = 0 jet (s3b), add t * (random jet direction); report |J(0)|, |dJ(0)| and the relative coefficient mismatches."""
import sys, io, contextlib
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
    import s3b_J0_comparison as s3b
J = s3.J; D = 4
etad = (1, 1, 1, 1); seed = 2
rng = np.random.default_rng(seed)
while True:
    w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
    if abs(np.linalg.det(w0)) > 0.1: break
n = 4*sum(1 for m in J.mons if 2 <= sum(m) <= 3)
sol = least_squares(s3b.resid, 0.15*rng.uniform(-1, 1, n), args=(w0, etad), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=60)
dirn = rng.normal(size=n); dirn /= np.linalg.norm(dirn)
print('base residual', np.linalg.norm(s3b.resid(sol.x, w0, etad)))
for t in (0.0, 1e-3, 3e-3, 1e-2, 3e-2):
    p = sol.x + t*dirn
    bg = s3b.build_bg(p, w0, etad)
    H, bj = s3.H_jets(bg)
    Jr = s3b.resid(p, w0, etad)
    opV = lambda A: s3.S_apply(bg, s3.Ov_apply(bg, s3.Sinv_apply(bg, A)))
    CV, aV, bV = s3.extract(opV)
    def op(A):
        P = s3.P_apply(bg, H, 4.0, A); out = np.zeros_like(P)
        for lam in range(D):
            for nu in range(D):
                out[lam] += J.mul(J.mul(bg['G'][lam, nu], bg['rhoi']), P[nu])/4.0
        return out
    CM, aM, bM = s3.extract(op)
    print(f't={t:7.0e}: |J(0)|={np.linalg.norm(Jr[:4]):.2e} |dJ(0)|={np.linalg.norm(Jr[4:]):.2e}  |aV-aM|={np.linalg.norm(aV-aM):.2e}  |bV-bM|={np.linalg.norm(bV-bM):.2e}  |C_V-C_M|={np.linalg.norm(CV-CM):.1e}')
