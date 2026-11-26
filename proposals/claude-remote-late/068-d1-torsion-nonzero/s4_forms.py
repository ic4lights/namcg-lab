"""S4. Constant bilinear forms on the section fields (h, w) for which the linearised
operator M(d) = M0 + M1^mu d_mu + M2^{mu nu} d_mu d_nu is formally symmetric
(adversary test F4):  B(phi, psi) = int phi^T G psi,  B(phi, M psi) = B(M phi, psi)
  <=>  G M0 = M0^T G,  G M1^mu = -(M1^mu)^T G,  G M2^{mu nu} = (M2^{mu nu})^T G.
Run from this folder: python s4_forms.py > s4_forms_output.txt"""
import numpy as np
from core import *


def forms(c, w):
    M0, M1, M2 = M_coeffs(c, w)
    I = np.eye(NF)
    L = lambda X: np.kron(I, X.T)        # vec(G) -> vec(G X)
    Rr = lambda X: np.kron(X.T, I)       # vec(G) -> vec(X^T G)
    rows = [L(M0) - Rr(M0)] + [L(M1[m]) + Rr(M1[m]) for m in M1] + [L(M2[k]) - Rr(M2[k]) for k in M2]
    A = np.vstack(rows)
    ev, V = np.linalg.eigh(A.T @ A)
    k = int((ev < 1e-9 * ev[-1]).sum())
    return V[:, :k].T.reshape(k, NF, NF), ev[k:k + 2]


def label_part(G):
    """If G = eta_ab (x) g on w_a^{lam}, return g (6x6) and the factorisation defect."""
    W = G[16:, 16:].reshape(4, 6, 4, 6)
    g = sum(ETA[a, a] * W[a, :, a, :] for a in range(4)) / 4
    return g, np.abs(W - np.einsum('ab,lm->albm', ETA, g)).max()


def ad_J12():
    """Adjoint action of the rotation generator J_12 on so(3,1) in the basis PAIRS."""
    J = np.zeros((4, 4)); J[1, 2] = 1; J[2, 1] = -1
    Jm = J @ ETA                                   # mixed J^c_d
    out = np.zeros((6, 6))
    for n, (c, d) in enumerate(PAIRS):
        lam = np.zeros((4, 4)); lam[c, d] = 1; lam[d, c] = -1
        com = Jm @ lam + lam @ Jm.T                # (J lam)^{cd}: rotate both upper indices
        for m, (e, f) in enumerate(PAIRS):
            out[m, n] = com[e, f]
    return out


for name, bg in [('flat', flat()), ('null rotation, constant-connection gauge', null_rotation_g2())]:
    Gs, gap = forms(*bg)
    k = len(Gs)
    sym = np.array([(G + G.T) / 2 for G in Gs]); asym = np.array([(G - G.T) / 2 for G in Gs])
    rs = np.linalg.matrix_rank(sym.reshape(k, -1), tol=1e-7); ra = np.linalg.matrix_rank(asym.reshape(k, -1), tol=1e-7)
    hh = max(np.abs(G[:16, :16]).max() for G in Gs)
    hw = max(max(np.abs(G[:16, 16:]).max(), np.abs(G[16:, :16]).max()) for G in Gs)
    g = np.random.default_rng(0)
    Gc = sum(g.normal() * G for G in Gs)
    print('==', name)
    print('  dimension of the solution space %d (symmetric %d, antisymmetric %d); next eigenvalues of the constraint %s' % (k, rs, ra, np.round(gap, 3)))
    print('  max |G| on the frame-frame block %.1e, on the frame-connection blocks %.1e; rank of a generic member %d of 40' % (hh, hw, np.linalg.matrix_rank(Gc, tol=1e-7)))
    defect = max(label_part(G)[1] for G in Gs)
    print('  defect of the factorisation G_ww = eta_ab (x) g: %.1e' % defect)
    gl = np.array([label_part(G)[0] for G in Gs])
    A = ad_J12()
    inv = max(np.abs(A.T @ x + x @ A).max() for x in gl)
    print('  max defect of ad(J_12)-invariance of g over the family: %.1e' % inv)
    # membership: Killing form and the positive form delta on components
    kill = np.diag([ETA[c, c] * ETA[d, d] for (c, d) in PAIRS]).astype(float)
    pos = np.eye(6)
    span = gl.reshape(k, 36)
    for nm, target in [('Killing form (1/2) lam_cd mu^cd', kill), ('positive form sum_{c<d} lam^cd mu^cd', pos)]:
        res = np.linalg.lstsq(span.T, target.reshape(36), rcond=None)
        err = np.abs(span.T @ res[0] - target.reshape(36)).max()
        print('  %s in the family: %s (residual %.1e); signature of it: %s' % (nm, err < 1e-8, err, np.sign(np.linalg.eigvalsh(target)).astype(int)))
