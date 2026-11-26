"""Fast section-value background equations of the first-order equivariant class for
left-invariant data: frame structure constants C[a,b,c] = C_ab^c ([e_a,e_b] = C_ab^c e_c)
and constant connection W[a,c,d] = w_a^{cd} (antisymmetric in c,d).  Conventions as in
proposals/068-d1-torsion-nonzero/core.py (independent re-implementation, constants only):
  Om_ab^c = w_a^{cd} eta_db,  nabla_a V_b = e_a V_b + Om_ab^c V_c
  T_ab^c  = -C_ab^c - Om_ab^c + Om_ba^c
  R_ab^f_c = Om_ac^d Om_bd^f - Om_bc^d Om_ad^f - C_ab^d Om_dc^f
  B1_b^e = -nabla^a T_ab^e + T_ab^c T^a_c^e + R_ab^{ae}
  B2_b^{de} = nabla^a R_ab^{de} - T_ab^c R^a_c^{de}
"""
import numpy as np
E = np.einsum


def eta_of(sig):
    return np.diag(np.asarray(sig, dtype=float))


def geom(C, W, eta):
    Om = E('acd,db->abc', W, eta)
    T = -C - Om + Om.transpose(1, 0, 2)
    R = (E('acd,bdf->abcf', Om, Om) - E('bcd,adf->abcf', Om, Om)
         - E('abd,dcf->abcf', C, Om))                      # R[a,b,c,f] = R_ab^f_c
    Rup = E('ce,abcf->abfe', eta, R)                        # R_ab^{fe}
    return Om, T, Rup


def nab_T(Om, T):   # [x,a,b,e]: nabla_x T_ab^e (constant components)
    return (E('xaz,zbe->xabe', Om, T) + E('xbz,aze->xabe', Om, T)
            - E('xze,abz->xabe', Om, T))


def nab_R(Om, Rup):  # [x,a,b,d,e]: nabla_x R_ab^{de}
    return (E('xaz,zbde->xabde', Om, Rup) + E('xbz,azde->xabde', Om, Rup)
            - E('xzd,abze->xabde', Om, Rup) - E('xze,abdz->xabde', Om, Rup))


def brackets(C, W, eta):
    etai = np.linalg.inv(eta)
    Om, T, Rup = geom(C, W, eta)
    B1 = (-E('xa,xabe->be', etai, nab_T(Om, T)) + E('abc,ax,xce->be', T, etai, T)
          + E('abae->be', Rup))
    B2 = E('xa,xabde->bde', etai, nab_R(Om, Rup)) - E('abc,ax,xcde->bde', T, etai, Rup)
    return B1, B2, T, Rup


def jacobi(C):
    J = (E('abd,dce->abce', C, C) + E('bcd,dae->abce', C, C) + E('cad,dbe->abce', C, C))
    return np.abs(J).max()


PAIRS = [(c, d) for c in range(4) for d in range(c + 1, 4)]


def W_of(p):
    W = np.zeros((4, 4, 4))
    for a in range(4):
        for n, (c, d) in enumerate(PAIRS):
            W[a, c, d] = p[6 * a + n]
            W[a, d, c] = -p[6 * a + n]
    return W
