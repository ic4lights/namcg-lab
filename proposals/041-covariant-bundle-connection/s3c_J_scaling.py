"""s3c: the mismatch between the matrix vector operator (Moser variables) and the covariant Maxwell-axion operator is first order in J.
Start from a J = dJ = 0 jet (two-stage sampler of s6b), add t * (random jet direction); report |J(0)|, |dJ(0)| and the coefficient mismatches."""
import sys, io, contextlib
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
    import s3b_J0_comparison as s3b
    import s6b_covariant_a1_fit as m6
J = s3.J; D = 4
etad = (1, 1, 1, 1); seed = 2
rng = np.random.default_rng(1000+seed)
while True:
    w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
    if abs(np.linalg.det(w0)) > 0.1: break
nq, nc = 4*len(m6.sel2), 4*len(m6.sel3)
c0 = np.zeros(nc)
f1 = lambda q: s3b.resid(m6.pack(q, c0), w0, etad)[:4]
sol = least_squares(f1, 0.2*rng.uniform(-1, 1, nq), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=600)
q = sol.x
r0 = s3b.resid(m6.pack(q, c0), w0, etad)[4:]
Mx = np.zeros((16, nc))
for k in range(nc):
    e = np.zeros(nc); e[k] = 1.0
    Mx[:, k] = s3b.resid(m6.pack(q, e), w0, etad)[4:] - r0
cc, *_ = np.linalg.lstsq(Mx, -r0, rcond=None)
base = m6.pack(q, cc)
print('base residual (J, dJ)', np.linalg.norm(s3b.resid(base, w0, etad)), flush=True)
dirn = rng.normal(size=base.size); dirn /= np.linalg.norm(dirn)
for t in (0.0, 1e-3, 3e-3, 1e-2, 3e-2):
    p = base + t*dirn
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
    print(f't={t:7.0e}: |J(0)|={np.linalg.norm(Jr[:4]):.2e} |dJ(0)|={np.linalg.norm(Jr[4:]):.2e}  |aV-aM|={np.linalg.norm(aV-aM):.2e}  |bV-bM|={np.linalg.norm(bV-bM):.2e}  |C_V-C_M|={np.linalg.norm(CV-CM):.1e}', flush=True)
