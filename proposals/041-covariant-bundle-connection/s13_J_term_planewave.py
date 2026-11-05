"""s13: cheap companion of s12 (no heat-kernel evaluation): second-order plane-wave averages of J^2 = G_{mu nu} J^mu J^nu (J^nu = rho^{-1} d_mu(rho K^{mu nu})),
|U|^2, ..., on delta rho = 0 modes, to test  a1V - a1M = 3/4 - 6 s|U|^2 (in units where X -> 1, from s12) against c*J^2."""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s12_planewave_decomposition as m12
    import s6b_covariant_a1_fit as m6
    import s5_scalar_and_vector_a1 as m5
from geom import *
e0 = 2e-3
phis = np.arange(6)*2*np.pi/6 + 0.3
def Jup(bg):
    rho, K, rhoi = bg['rho'], bg['K'], bg['rhoi']
    out = np.zeros((D, J.M))
    for s in range(D):
        t = np.zeros(J.M)
        for m in range(D):
            t += J.d(J.mul(rho, K[m, s]), m)
        out[s] = J.mul(rhoi, t)
    return out
for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    rng = np.random.default_rng(21)
    eta = np.diag(np.array(etad, float))
    while True:
        w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
        if abs(np.linalg.det(w0)) > 0.3: break
    Th0 = np.linalg.inv(w0)
    p = rng.normal(size=D); q = Th0 @ p
    rho_bar = 1.0/abs(w0[0, 1]*w0[2, 3] - w0[0, 2]*w0[1, 3] + w0[0, 3]*w0[1, 2])
    ker = np.array([v - (p @ v)/(p @ p)*p for v in np.eye(D)])
    U, S, Vt = np.linalg.svd(ker); kerb = Vt[:3]
    # more modes inside ker(p): random combinations
    modes = [kerb[0], kerb[1]] + [sum(rng.normal()*kerb[i] for i in range(3)) for _ in range(4)]
    print('eta', etad)
    rows = []
    for im, u in enumerate(modes):
        q2 = q @ eta @ q; ql = eta @ q
        Muu = q2*(u @ eta @ u) - (ql @ u)**2
        norm = rho_bar**2*(p @ np.linalg.inv(eta) @ p)*Muu
        acc = {}
        for sg in (+1, -1):
            for phi in phis:
                bg = m12.background(w0, u, p, phi, sg*e0, etad)
                inv = m6.invariants(bg)
                Jv = Jup(bg); G0 = bg['G'][..., 0]
                s = 1.0 if etad[0] > 0 else -1.0
                rho2 = bg['rho'][0]**2
                vals = dict(X=rho2*m5.Xdens(bg), J2=rho2*(Jv[:, 0] @ G0 @ Jv[:, 0]), U2=rho2*s*(inv['th2'] - 2*inv['vth'] + inv['t2V2']), Rg=rho2*inv['R'])
                for k, v in vals.items(): acc[k] = acc.get(k, 0.0) + v/(2*len(phis))
        res = {k: v/(e0**2*norm) for k, v in acc.items()}
        rel = {k: res[k]/res['X'] for k in res}
        target = 0.75 - 6*rel['U2']
        rows.append((rel['J2'], target, rel['U2'], rel['Rg']))
        print(f'  mode {im}: J2/X = {rel["J2"]:+.5f}  U2(s)/X = {rel["U2"]:+.5f}  Rg/X={rel["Rg"]:+.4f}  (3/4 - 6 s U2) = {target:+.5f}  ratio (3/4-6U2)/J2 = {target/rel["J2"]:+.4f}', flush=True)
