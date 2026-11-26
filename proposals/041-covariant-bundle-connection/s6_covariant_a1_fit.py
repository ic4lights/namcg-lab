"""s6: heat-kernel coefficient a_1 = tr(E + R/6) (Gilkey sign: manuscript tr(R/6 - E)) of
   (V) the matrix vector operator O_v (a variables) and (M) the covariant Maxwell(G, weight rho) + axion(b) operator in A variables,
 on Poisson-class 3-jets with J = 0 and dJ = 0 at the point.  Fit of a_1 (scalar, not density) to the covariant invariants
   R_G, V^2 = |d ln rho|^2_G, box ln rho, |d theta~|^2_G, theta~ = rho*b (s2/s4).
"""
import sys, io, contextlib
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
    import s3b_J0_comparison as s3b
    from s4_axial_torsion_is_dual_gradient import theta_tilde
from geom import *

def invariants(bg):
    G, rho, rhoi, K = bg['G'], bg['rho'], bg['rhoi'], bg['K']
    Gam, gi = christoffel_jets(G)
    dr = np.array([J.d(rho, k) for k in range(D)])          # [k,M]
    Vj = np.array([J.mul(dr[k], rhoi) for k in range(D)])    # V_k jets
    Kz = K[..., 0]
    V2 = Vj[:, 0] @ Kz @ Vj[:, 0]
    box = 0.0
    for m in range(D):
        for n in range(D):
            box += Kz[m, n]*(J.d(Vj[n], m)[0] - sum(Gam[l, m, n, 0]*Vj[l, 0] for l in range(D)))
    tt, I1, b = theta_tilde(bg)
    dth = np.array([J.d(tt, k)[0] for k in range(D)])
    th2 = dth @ Kz @ dth
    R = ricci_scalar_at0(G)
    return dict(R=R, V2=V2, box=box, th2=th2, theta=tt[0])

def a1_V(bg):
    a4, b4 = apply_to_jets(lambda A: s3.Ov_apply(bg, A), 4)
    return gilkey_a1(a4, b4, bg['G'], 4)[0]

def a1_M(bg, kappa=4.0, c=4.0):
    H, bjet = s3.H_jets(bg)
    G, rhoi = bg['G'], bg['rhoi']
    def op(A):
        P = s3.P_apply(bg, H, c, A)
        out = np.zeros_like(P)
        for lam in range(D):
            for nu in range(D):
                out[lam] += J.mul(J.mul(G[lam, nu], rhoi), P[nu])/kappa
        return out
    a, b = apply_to_jets(op, 4)
    return gilkey_a1(a, b, bg['G'], 4)[0]

if __name__ == '__main__':
    for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        rows = []; ys = []; yM = []
        for seed in range(1, 25):
            rng = np.random.default_rng(100+seed)
            while True:
                w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
                if abs(np.linalg.det(w0)) > 0.1: break
            n = 4*sum(1 for m in J.mons if 2 <= sum(m) <= 3)
            p0 = 0.12*rng.uniform(-1, 1, n)
            sol = least_squares(s3b.resid, p0, args=(w0, etad), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=60)
            if np.linalg.norm(s3b.resid(sol.x, w0, etad)) > 1e-10: continue
            bg = s3b.build_bg(sol.x, w0, etad)
            inv = invariants(bg)
            aV = a1_V(bg); aM = a1_M(bg)
            rows.append([inv['R'], inv['V2'], inv['box'], inv['th2']]); ys.append(aV); yM.append(aM)
        rows = np.array(rows); ys = np.array(ys); yM = np.array(yM)
        print(f'eta={etad}: {len(ys)} J=0 samples;  max |a1(V)-a1(M)| = {np.max(np.abs(ys-yM)):.2e}   (max |a1| = {np.max(np.abs(ys)):.2f})')
        for name, y in (('V', ys), ('M', yM)):
            coef, res, rk, sv = np.linalg.lstsq(rows, y, rcond=None)
            r = y - rows@coef
            print(f'   fit a1({name}) = cR R + cV V2 + cbox box + cth |dth|^2 :  cR={coef[0]:+.5f} cV={coef[1]:+.5f} cbox={coef[2]:+.5f} cth={coef[3]:+.5f};  max resid {np.max(np.abs(r)):.2e}, rank {rk}')
