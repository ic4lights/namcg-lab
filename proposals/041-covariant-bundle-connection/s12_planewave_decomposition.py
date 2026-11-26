"""s12: decomposition of the plane-wave quadratic forms (about constant omega_bar) of the vector-sector a_1 into covariant pieces.

Background: omega = omega_bar + eps*d(A), A_nu = u^mu omega_bar_{mu nu} cos(p.x + phi)  (Moser form of the matrix fluctuation a^mu = u^mu cos(p.x+phi)).
For each mode u and each phase phi, eps = +-e0 (symmetrised), jets at x = 0 (3-jets), density D = sqrt|G| * (scalar) is averaged over phi (6 phases).
The second-order coefficient is  <D>^{(2)} = (<D(+e0)> + <D(-e0)>)/(2 e0^2)  (first order averages to zero).
Quantities (all densities sqrt|G| = rho^2 times scalars):
   a1V  : a_1 of the matrix vector operator O_v (a variables)                     [manuscript: (4/6) rho R[g_rho] + rho^2 X]
   a1M  : a_1 of the covariant Maxwell(G, rho) + axion operator                   [analytic: -R/3 + box ln rho - V^2 + 6 s |d th - th V|^2]
   Rg   : rho^2 R_G,   U2 : rho^2 |d th~ - th~ V|^2_G,  RR : rho R[g_rho],  X : rho^2 X
Normalisation: ratio to  eps^2 rhobar^2 p_eta^2 M(u,u), M = q^2 eta - q q, q = Thetabar p;  the manuscript values are  X -> 1,  rho R[g_rho] -> -1/4 (delta rho = 0 modes).
"""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
    import s6b_covariant_a1_fit as m6
    import s5_scalar_and_vector_a1 as m5
from geom import *


def cos_jet(p, phi):
    lin = np.zeros(J.M)
    for k in range(D):
        mon = tuple(1 if j == k else 0 for j in range(D)); lin[J.idx[mon]] = p[k]
    l2 = J.mul(lin, lin); l3 = J.mul(l2, lin)
    c = np.zeros(J.M); c[0] = np.cos(phi)
    return c - np.sin(phi)*lin - np.cos(phi)*l2/2.0 + np.sin(phi)*l3/6.0


def bg_from_omega(om, etad):
    Th = J.inv_series(om)
    eta = np.diag(np.array(etad, float))
    etaJ = np.zeros((D, D, J.M)); etaJ[:, :, 0] = eta
    Pf = J.mul(om[0, 1], om[2, 3]) - J.mul(om[0, 2], om[1, 3]) + J.mul(om[0, 3], om[1, 2])
    sg = np.sign(Pf[0]); rho = sg*Pf; rhoi = s3.scal_inv(rho)
    K = J.matmul(J.matmul(np.transpose(Th, (1, 0, 2)), etaJ), Th)
    G = J.inv_series(K)
    return dict(eta=eta, etaJ=etaJ, om=om, Th=Th, rho=rho, rhoi=rhoi, K=K, G=G, sg=sg, Pf=Pf)


def background(w0, u, p, phi, eps, etad):
    A_c = u @ w0                          # A_nu = u^mu w0_{mu nu}
    cj = cos_jet(p, phi)
    A = np.array([eps*A_c[n]*cj for n in range(D)])
    om = np.zeros((D, D, J.M)); om[:, :, 0] = w0
    for m in range(D):
        for n in range(D):
            om[m, n] += J.d(A[n], m) - J.d(A[m], n)
    return bg_from_omega(om, etad)


def pieces(bg, with_V=True, with_M=True):
    inv = m6.invariants(bg)
    s = 1.0 if bg['eta'][0, 0] > 0 else -1.0
    rho0 = bg['rho'][0]
    D2 = rho0**2
    U2 = inv['th2'] - 2*inv['vth'] + inv['t2V2']
    out = dict(Rg=D2*inv['R'], U2=D2*s*U2, RR=rho0*m5.rho_Rgrho(bg)/rho0*1.0, X=D2*m5.Xdens(bg), V2=D2*inv['V2'])
    out['RR'] = m5.rho_Rgrho(bg)           # rho R[g_rho]
    if with_V: out['a1V'] = D2*m6.a1_V(bg)
    if with_M: out['a1M'] = D2*m6.a1_M(bg)
    return out


if __name__ == '__main__':
    e0 = 2e-3
    phis = np.arange(6)*2*np.pi/6 + 0.3
    for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        rng = np.random.default_rng(21)
        eta = np.diag(np.array(etad, float))
        while True:
            w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
            if abs(np.linalg.det(w0)) > 0.3: break
        Th0 = np.linalg.inv(w0)
        p = rng.normal(size=D)
        q = Th0 @ p                       # q^mu = Theta^{mu rho} p_rho  (gauge direction u ~ q)
        rho_bar = 1.0/abs(w0[0, 1]*w0[2, 3] - w0[0, 2]*w0[1, 3] + w0[0, 3]*w0[1, 2])
        # modes: u with p.u = 0 (two classes mod q) and a generic u
        basis = np.eye(D)
        # u in ker(p): Gram-Schmidt style
        ker = []
        for v in basis:
            w_ = v - (p @ v)/(p @ p)*p
            ker.append(w_)
        ker = np.array(ker)
        U, S, Vt = np.linalg.svd(ker)
        kerb = Vt[:3]                     # 3-dim ker(p) (contains q since p.q = 0)
        # remove component along q (mod q): pick two vectors independent of q
        modes = []
        for v in kerb:
            if len(modes) == 2: break
            modes.append(v)
        modes.append(rng.normal(size=D))  # generic: delta rho != 0
        print(f'eta={etad}: p_eta^2={p@np.linalg.inv(eta)@p:+.3f}, rho_bar={rho_bar:.3f}, p.q={p@q:.1e}')
        for im, u in enumerate(modes):
            ql = eta @ q
            q2 = q @ eta @ q
            Muu = q2*(u @ eta @ u) - (ql @ u)**2
            norm = rho_bar**2*(p @ np.linalg.inv(eta) @ p)*Muu
            acc = {}
            for sg in (+1, -1):
                for phi in phis:
                    bg = background(w0, u, p, phi, sg*e0, etad)
                    pc = pieces(bg)
                    for k, v in pc.items():
                        acc[k] = acc.get(k, 0.0) + v/(2*len(phis))
            # second order coefficient
            res = {k: v/(e0**2*norm) for k, v in acc.items()}
            ratio_X = res['X']
            print(f'  mode {im} (p.u={p@u:+.3f}): ' + ', '.join(f'{k}={res[k]:+.4f}' for k in ['X', 'RR', 'Rg', 'U2', 'V2', 'a1V', 'a1M']), flush=True)
            print(f'      relative to X: ' + ', '.join(f'{k}={res[k]/ratio_X:+.4f}' for k in ['X', 'RR', 'Rg', 'U2', 'V2', 'a1V', 'a1M']), flush=True)
