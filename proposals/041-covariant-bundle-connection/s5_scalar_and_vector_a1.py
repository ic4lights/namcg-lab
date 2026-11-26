"""s5: validation of the Gilkey routine on the scalar operator O_s (expect sqrt|G| a_1 = rho R[g_rho]/6 pointwise, manuscript) and on the vector
operator O_v in the a-variables (expect sqrt|G| a_1 = (4/6) rho R[g_rho] + rho^2 X, manuscript), with X = eta^{rl} eta_{ma} eta_{nb} d_r Th^{mn} d_l Th^{ab}."""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
from geom import *

def rho_Rgrho(bg):
    # g_rho,mu nu = G_{mu nu}/rho   (g_rho^{mu nu} = rho K^{mu nu})
    G, rho, rhoi = bg['G'], bg['rho'], bg['rhoi']
    g = np.stack([[J.mul(G[m, n], rhoi) for n in range(D)] for m in range(D)])
    return rho[0]*ricci_scalar_at0(g)

def Xdens(bg):
    Th, eta = bg['Th'], bg['eta']
    dT = np.stack([J.d(Th, k) for k in range(D)], axis=-2)      # dT[m,n,k,M]
    x = 0.0
    for r in range(D):
        for m in range(D):
            for n in range(D):
                for a in range(D):
                    for b in range(D):
                        x += eta[r, r]*eta[m, a]*eta[n, b]*dT[m, n, r, 0]*dT[a, b, r, 0]
    return x

if __name__ == '__main__':
    for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        for seed in (1, 2, 3):
            bg = s3.setup(seed, etad)
            G, rho, K, rhoi = bg['G'], bg['rho'], bg['K'], bg['rhoi']
            sq = np.sqrt(abs(np.linalg.det(G[..., 0])))
            # scalar operator
            def Os(A):
                out = np.zeros_like(A)
                s = np.zeros(J.M)
                for mm in range(D):
                    for n in range(D):
                        s += J.d(J.mul(J.mul(rho, K[mm, n]), J.d(A[0], n)), mm)
                out[0] = -J.mul(rhoi, s)
                return out
            a, b = apply_to_jets(Os, 1)
            a1s, _ = gilkey_a1(a, b, G, 1)
            # vector operator in a-variables
            a4, b4 = apply_to_jets(lambda A: s3.Ov_apply(bg, A), 4)
            a1v, _ = gilkey_a1(a4, b4, G, 4)
            RR = rho_Rgrho(bg); X = Xdens(bg)
            print(f'eta={etad} seed={seed}: scalar  sqrtG*a1 = {sq*a1s:+.8f}  rho R[g_rho]/6 = {RR/6:+.8f}')
            print(f'                      vector  sqrtG*a1 = {sq*a1v:+.8f}  4/6 rho R[g_rho] + rho^2 X = {4*RR/6 + rho[0]**2*X:+.8f}   (rho^2 X = {rho[0]**2*X:+.5f})')
