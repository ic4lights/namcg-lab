"""Linearisation helpers on left-invariant backgrounds with R != 0 (uses core068.M_op).
Gauge directions with the curvature term:  for xi^c D_c,  h_a^e = nabla_a xi^e + xi^c T_ca^e,
omega_a^{de} = xi^c R_ca^{de};  for 1/2 lam^{cd} S_cd,  h_a^c = -lam^c_a, omega = -nabla lam."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import core068 as K
import bg

SQ3 = np.sqrt(3.0)
Bg = np.zeros((4, 4)); Bg[0, 2] = 1; Bg[2, 0] = -1
N1 = np.zeros((4, 4)); N1[0, 1] = 1; N1[1, 0] = -1; N1[1, 2] = 1; N1[2, 1] = -1
N2 = np.zeros((4, 4)); N2[0, 3] = 1; N2[3, 0] = -1; N2[2, 3] = -1; N2[3, 2] = 1
KL = np.array([1.0, 0, 1.0, 0])


def bg_F(s=1.0, tau=-2 + SQ3):
    m = np.array([0, s * (1 + (tau + 1 / tau) / 2), 0, s * (tau - 1 / tau) / 2])
    W = s * np.einsum('a,cd->acd', KL, Bg) + np.einsum('a,cd->acd', m, N1)
    return np.zeros((4, 4, 4)), W


def bg_H(kappa=1.0, zeta=1.0, x=0.0):
    C = K.lie({(3, 1): {2: kappa}})
    return C, np.einsum('a,cd->acd', KL, zeta * N1 + x * N2)


def gauge_vectors_R(cbar, wbar, Eop, with_R=True):
    Eop = np.asarray(Eop, dtype=complex); N = Eop.shape[-1]
    eta = K.ETA
    Om0 = np.einsum('acd,db->abc', wbar, eta)
    _, _, Tbar, Rbar = bg.brackets(cbar, wbar, eta)
    out = []
    for m in range(N):
        for (c, d) in K.PAIRS:
            lam = np.zeros((4, 4, N), dtype=complex); lam[c, d, m] = 1.0; lam[d, c, m] = -1.0
            h = -np.einsum('cdn,da->acn', lam, eta)
            Dlam = (np.einsum('anm,cdm->acdn', Eop, lam)
                    - np.einsum('azc,zdn->acdn', Om0, lam) - np.einsum('azd,czn->acdn', Om0, lam))
            out.append(K.pack_hw(h, -Dlam))
        for c in range(4):
            xi = np.zeros((4, N), dtype=complex); xi[c, m] = 1.0
            Dxi = np.einsum('anm,em->aen', Eop, xi) - np.einsum('aze,zn->aen', Om0, xi)
            h = Dxi + np.einsum('cn,cae->aen', xi, Tbar)
            w = np.einsum('cn,cade->aden', xi, Rbar) if with_R else np.zeros((4, 4, 4, N), dtype=complex)
            out.append(K.pack_hw(h, w))
    return np.array(out).T


def Qop(cbar, wbar, Eop):
    """Linearised third bracket on order-zero fields A_b (section values):
    F_ab = nabla_a A_b - nabla_b A_a + T_ab^c A_c,  Q_b = nabla^a F_ab - T_ab^c F^a_c."""
    Eop = np.asarray(Eop, dtype=complex); N = Eop.shape[-1]
    eta = K.ETA; etai = np.linalg.inv(eta)
    Om0 = np.einsum('acd,db->abc', wbar, eta)
    _, _, T, _ = bg.brackets(cbar, wbar, eta)
    Q = np.zeros((4 * N, 4 * N), dtype=complex)
    for col in range(4 * N):
        A = np.zeros((4, N), dtype=complex); A.flat[col] = 1.0
        nA = np.einsum('anm,bm->abn', Eop, A) + np.einsum('abz,zn->abn', Om0, A)
        F = nA - nA.transpose(1, 0, 2) + np.einsum('abc,cn->abn', T, A)
        nF = (np.einsum('xnm,abm->xabn', Eop, F) + np.einsum('xaz,zbn->xabn', Om0, F)
              + np.einsum('xbz,azn->xabn', Om0, F))
        Qb = np.einsum('xa,xabn->bn', etai, nF) - np.einsum('abc,ax,xcn->bn', T, etai, F)
        Q[:, col] = Qb.reshape(4 * N)
    return Q
