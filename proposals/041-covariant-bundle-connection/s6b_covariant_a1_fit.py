"""s6b: faster J=0 sampling (two-stage) and fit of a_1 of the matrix vector operator (V) and of the covariant operator (M) to covariant invariants.
Stage 1: quadratic coefficients of the potential A fixed by J(0)=0 (Newton / least squares, 40 unknowns).
Stage 2: cubic coefficients enter dJ(0)=0 linearly (16 equations, 80 unknowns): min-norm solution plus a random null-space component.
Invariants at the point (G = Theta-built metric, rho = |Pf omega|, theta~ = rho*b of s2):
   R, V2 = |d ln rho|^2, box = box_G ln rho, th2 = |d theta~|^2, vth = theta~ V.d theta~, t2V2 = theta~^2 V2.
Analytic prediction of the covariant operator (Euclid): a_1 = -R/3 - 2 box - V2 + 6 |d theta~ - theta~ V|^2 ; (Lorentz: last term sign flips)."""
import sys, io, contextlib, pickle, os
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
    import s3b_J0_comparison as s3b
    from s4_axial_torsion_is_dual_gradient import theta_tilde
from geom import *
sel = [i for i, m in enumerate(J.mons) if 2 <= sum(m) <= 3]
sel2 = [i for i, m in enumerate(J.mons) if sum(m) == 2]
sel3 = [i for i, m in enumerate(J.mons) if sum(m) == 3]

def pack(q, c):
    p = []
    for mu in range(D):
        for i in sel:
            if i in sel2: p.append(q[mu*len(sel2) + sel2.index(i)])
            else: p.append(c[mu*len(sel3) + sel3.index(i)])
    return np.array(p)

def invariants(bg):
    G, rho, rhoi, K = bg['G'], bg['rho'], bg['rhoi'], bg['K']
    Gam, gi = christoffel_jets(G)
    dr = np.array([J.d(rho, k) for k in range(D)])
    Vj = np.array([J.mul(dr[k], rhoi) for k in range(D)])
    Kz = K[..., 0]; V0 = Vj[:, 0]
    V2 = V0 @ Kz @ V0
    box = sum(Kz[m, n]*(J.d(Vj[n], m)[0] - sum(Gam[l, m, n, 0]*Vj[l, 0] for l in range(D))) for m in range(D) for n in range(D))
    tt, I1, b = theta_tilde(bg)
    dth = np.array([J.d(tt, k)[0] for k in range(D)])
    return dict(R=ricci_scalar_at0(G), V2=V2, box=box, th2=dth @ Kz @ dth, vth=tt[0]*(V0 @ Kz @ dth), t2V2=tt[0]**2*V2, theta=tt[0])

def a1_V(bg):
    a4, b4 = apply_to_jets(lambda A: s3.Ov_apply(bg, A), 4)
    return gilkey_a1(a4, b4, bg['G'], 4)[0]

def a1_M(bg, kappa=4.0, c=4.0):
    H, bjet = s3.H_jets(bg)
    G, rhoi = bg['G'], bg['rhoi']
    def op(A):
        P = s3.P_apply(bg, H, c, A); out = np.zeros_like(P)
        for lam in range(D):
            for nu in range(D):
                out[lam] += J.mul(J.mul(G[lam, nu], rhoi), P[nu])/kappa
        return out
    a, b = apply_to_jets(op, 4)
    return gilkey_a1(a, b, bg['G'], 4)[0]

def sample(etad, seed):
    rng = np.random.default_rng(1000+seed)
    while True:
        w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
        if abs(np.linalg.det(w0)) > 0.1: break
    nq, nc = 4*len(sel2), 4*len(sel3)
    c0 = np.zeros(nc)
    f1 = lambda q: s3b.resid(pack(q, c0), w0, etad)[:4]
    sol = least_squares(f1, 0.2*rng.uniform(-1, 1, nq), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=400)
    q = sol.x
    if np.linalg.norm(f1(q)) > 1e-10: return None
    r0 = s3b.resid(pack(q, c0), w0, etad)[4:]
    Mx = np.zeros((16, nc))
    for k in range(nc):
        e = np.zeros(nc); e[k] = 1.0
        Mx[:, k] = s3b.resid(pack(q, e), w0, etad)[4:] - r0
    sol_c, *_ = np.linalg.lstsq(Mx, -r0, rcond=None)
    # null space component
    u, s, vt = np.linalg.svd(Mx)
    null = vt[16:]
    c = sol_c + 0.3*rng.normal(size=null.shape[0]) @ null
    res = np.linalg.norm(s3b.resid(pack(q, c), w0, etad))
    if res > 1e-9: return None
    return s3b.build_bg(pack(q, c), w0, etad), res

if __name__ == '__main__':
    nsamp = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    out = {}
    for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        rows = []; yV = []; yM = []
        for seed in range(nsamp):
            r = sample(etad, seed)
            if r is None: continue
            bg, res = r
            inv = invariants(bg)
            rows.append([inv[k] for k in ('R', 'V2', 'box', 'th2', 'vth', 't2V2')]); yV.append(a1_V(bg)); yM.append(a1_M(bg))
            print(f'  eta={etad} seed {seed}: residual {res:.1e}  a1(V)={yV[-1]:+.6f} a1(M)={yM[-1]:+.6f}', flush=True)
        out[etad] = (np.array(rows), np.array(yV), np.array(yM))
        pickle.dump(out, open('s6b_samples.pkl', 'wb'))
    names = ['R', 'V2', 'box', 'th2', 'vth', 't2V2']
    for etad, (rows, yV, yM) in out.items():
        print(f'eta={etad}: {len(yV)} samples; max|a1(V)-a1(M)| = {np.max(np.abs(yV-yM)):.2e}')
        for nm, y in (('V', yV), ('M', yM)):
            coef, res, rk, sv = np.linalg.lstsq(rows, y, rcond=None)
            r = y - rows@coef
            print(f'   a1({nm}) fit: ' + ', '.join(f'{n}={c:+.5f}' for n, c in zip(names, coef)) + f';  max resid {np.max(np.abs(r)):.1e}, rank {rk}')
        pred = np.array([-1/3, -1.0, -2.0, 6.0, -12.0, 6.0]) * np.array([1, 1, 1, 1, 1, 1])
        sgn = 1.0 if etad[0] > 0 else -1.0
        pred[3:] = pred[3:]*sgn
        print('   analytic prediction (Euclid / Lorentz-sign-flipped axion):', pred.tolist(), ' max|a1(M) - pred.rows| =', np.max(np.abs(yM - rows@pred)))
