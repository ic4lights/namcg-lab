"""Leading-symbol tools for a set of matrices X^I = M^{C_I D_I} on the CP^{1,2} orbit (tangent vectors are 15-vectors of delta M^{AB}, A<B)."""
import numpy as np, itertools
from cp12_realisation import *

s = -1.0
pairs = [(A, B) for A in range(6) for B in range(A + 1, 6)]
pidx = {p: i for i, p in enumerate(pairs)}


def vec(M0, C, D):
    """Hamiltonian field of M^{CD}: components {M^{CD}, M^{AB}} on the 15 coordinates."""
    return np.array([s * lie(C, D, A, B, M0) for (A, B) in pairs])


def lin_coeffs(C, D, E, F):
    """{M^{CD}, M^{EF}} = s * sum_P L_P M^P ; return L (15,)."""
    L = np.zeros(15)
    for k, (A, B) in enumerate(pairs):
        Mu = np.zeros((6, 6)); Mu[A, B] = 1; Mu[B, A] = -1
        L[k] = s * lie(C, D, E, F, Mu)
    return L


def ham_of_lin(M0, L):
    return sum(L[k] * vec(M0, A, B) for k, (A, B) in enumerate(pairs))


def hodge_split(F):
    eps = np.zeros((4, 4, 4, 4))
    for p in itertools.permutations(range(4)):
        eps[p] = np.linalg.det(np.eye(4)[list(p)])
    dual = 0.5 * np.einsum('abcd,cd->ab', eps, F)
    return 0.5 * (F + dual), 0.5 * (F - dual)


def amp(Fh):
    return np.sqrt(0.25 * np.sum(Fh ** 2))


def planes(F):
    Fp, Fm = hodge_split(F)
    p, r = amp(Fp), amp(Fm)
    return p + r, abs(p - r), p, r


def symbol(M0, fields, etas, tol=1e-9):
    """fields: list of (C,D); etas: contraction weights eta_I. Returns dict with rank, h, S-tensor F_{ij,k}, centre rank."""
    Dv = np.array([vec(M0, C, D) for (C, D) in fields])        # (nI,15)
    u, sv, vh = np.linalg.svd(Dv)
    rk = int(np.sum(sv > tol * sv[0]))
    E = vh[:rk]                                                  # orthonormal basis of H in R^15
    c = Dv @ E.T                                                 # (nI,rk)
    h = c.T @ np.diag(etas) @ c
    nI = len(fields)
    # brackets [D^I,D^J] = ham({X^I,X^J})
    brs = {}
    for I, J in itertools.combinations(range(nI), 2):
        L = lin_coeffs(*fields[I], *fields[J])
        brs[(I, J)] = ham_of_lin(M0, L)
    # centre: complement of H spanned by all brackets mod H (and generally of the full tangent space)
    allb = np.array(list(brs.values()))
    proj = allb - (allb @ E.T) @ E
    uu, ss, vv = np.linalg.svd(proj)
    zr = int(np.sum(ss > tol * max(ss[0], 1e-30)))
    Z = vv[:zr]
    S = np.zeros((nI, nI, zr))
    for (I, J), v in brs.items():
        cz = Z @ v
        S[I, J] = cz; S[J, I] = -cz
    cp = np.linalg.pinv(c)                                       # (rk,nI)
    Fij = np.einsum('iI,IJk,jJ->ijk', cp, S, cp)
    recon = np.einsum('Ii,ijk,Jj->IJk', c, Fij, c)
    res = np.max(np.abs(recon - S))
    return dict(rank=rk, c=c, h=h, F=Fij, zrank=zr, resid=res, sv=sv, Z=Z, E=E)


def sqrtm_sym(Q):
    w, v = np.linalg.eigh(Q)
    return (v * np.sqrt(np.abs(w))) @ v.T
