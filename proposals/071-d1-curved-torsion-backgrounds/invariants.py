"""Invariants of left-invariant first-order-class backgrounds (C, W): Lie algebra type,
torsion and curvature of the class connection, and the Levi-Civita curvature of the frame."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import bg
E = np.einsum


def lie_info(C, tol=1e-8):
    d = C.shape[0]
    M = C.reshape(d * d, d)
    der = np.linalg.matrix_rank(M, tol)                  # dim [g,g]
    ad = np.transpose(C, (0, 2, 1))                     # ad[a][c,b] = C_ab^c  (ad_a e_b = C_ab^c e_c)
    cent = d - np.linalg.matrix_rank(np.concatenate([a for a in ad], axis=0), tol)
    K = E('acd,bdc->ab', C, C)                          # Killing form C_ac^d C_bd^c
    tr = E('abb->a', C)                                 # trace ad_a
    # lower central series dims
    def span_brackets(V):
        out = E('ia,ab c->ic'.replace(' ', ''), V, np.zeros((d, d, d))) if False else None
        vecs = [E('a,b,abc->c', v, w, C) for v in V for w in np.eye(d)]
        A = np.array(vecs)
        if A.size == 0:
            return np.zeros((0, d))
        u, s, vt = np.linalg.svd(A)
        r = int((s > tol * max(1, s[0] if len(s) else 1)).sum())
        return vt[:r]
    lcs, V = [], np.eye(d)
    for _ in range(5):
        V = span_brackets(V)
        lcs.append(V.shape[0])
    # derived series
    ds, V = [], np.eye(d)
    for _ in range(5):
        vecs = [E('a,b,abc->c', v, w, C) for v in V for w in V]
        A = np.array(vecs) if vecs else np.zeros((0, d))
        if A.size == 0:
            ds.append(0); V = np.zeros((0, d)); continue
        u, s, vt = np.linalg.svd(A)
        r = int((s > tol * max(1, s[0])).sum())
        V = vt[:r]
        ds.append(r)
    return {'dim_derived': der, 'dim_center': cent, 'killing_eigs': np.round(np.linalg.eigvalsh((K + K.T) / 2), 6),
            'trace_ad': np.round(tr, 8), 'lower_central': lcs, 'derived_series': ds}


def lc_connection(C, eta):
    """Levi-Civita Om for the left-invariant orthonormal frame: torsion-free and metric."""
    # Om_ab^c with T = -C - Om + Om^T = 0 and Om_abc (c lowered) antisymmetric in b,c
    Cl = E('abd,dc->abc', C, eta)                       # C_abc lowered last
    # Koszul: Gamma_abc := <nabla_a e_b, e_c> = 1/2 (C_abc - C_bca + C_cab)
    G = 0.5 * (Cl - E('bca->abc', Cl) + E('cab->abc', Cl))
    Gup = E('abd,dc->abc', G, np.linalg.inv(eta))     # Gamma^c_ab
    return -Gup                                         # Om_ab^c = -Gamma^c_ab


def curvature_from_Om(C, Om, eta):
    R = (E('acd,bdf->abcf', Om, Om) - E('bcd,adf->abcf', Om, Om) - E('abd,dcf->abcf', C, Om))
    Rup = E('ce,abcf->abfe', eta, R)
    return Rup


def info(C, W, eta, tol=1e-8):
    etai = np.linalg.inv(eta)
    B1, B2, T, Rup = bg.brackets(C, W, eta)
    Tl = E('abc,cd->abd', T, eta)
    tvec = E('acc->a', T)
    axial = np.array([sum(np.sign(np.linalg.det(np.eye(4)[[a, b, c, d]])) * Tl[a, b, c]
                          for a in range(4) for b in range(4) for c in range(4)
                          if len({a, b, c, d}) == 4) for d in range(4)])
    TT = E('abc,ax,by,cz,xyz->', Tl, etai, etai, eta, T)
    Rl = E('abfe,fg,eh->abgh', Rup, eta, eta)                 # R_ab gh lowered
    RR = E('abcd,ax,by,xycd->', Rl, etai, etai, Rup) if False else E('abcd,ax,by,cz,dw,xyzw->', Rl, etai, etai, etai, etai, Rl)
    Ric = E('abae->be', Rup)
    scal = np.trace(Ric)                       # R_ab^{ab} = Ric_b^b (round 2; round 1 used trace(Ric @ eta), not a scalar)
    # holonomy span: R as map from pairs (a<b) to so(3,1) 6-vectors
    PA = bg.PAIRS
    Rmat = np.array([[Rup[a, b, c, d] for (c, d) in PA] for (a, b) in PA])
    hol = np.linalg.matrix_rank(Rmat, tol)
    OmLC = lc_connection(C, eta)
    RLC = curvature_from_Om(C, OmLC, eta)
    RicLC = E('abae->be', RLC)
    RLCl = E('abfe,fg,eh->abgh', RLC, eta, eta)
    RRLC = E('abcd,ax,by,cz,dw,xyzw->', RLCl, etai, etai, etai, etai, RLCl)
    return {'B1': np.abs(B1).max(), 'B2': np.abs(B2).max(), 'jacobi': bg.jacobi(C),
            '|T|max': np.abs(T).max(), 'T.T': TT, 'trace_vec': tvec, 'axial': axial,
            '|R|max': np.abs(Rup).max(), 'RR': RR, 'Ric': Ric, 'scalar': scal, 'hol_rank': hol,
            'Rmat_sv': np.linalg.svd(Rmat, compute_uv=False),
            'Rmat_eigs': np.linalg.eigvals(Rmat),
            'LC_Ric': RicLC, 'LC_RR': RRLC, 'lie': lie_info(C, tol)}
