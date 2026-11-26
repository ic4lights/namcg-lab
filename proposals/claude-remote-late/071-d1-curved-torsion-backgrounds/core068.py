"""Linearised first two brackets of the matrix equation in the first-order
equivariant class, about a background with constant frame coefficients.

Conventions (frame indices only; ETA is the contraction, default diag(-1,1,1,1)):
  [e_a, e_b] = C_ab^c e_c
  nabla_a V_b = e_a V_b + Om_{ab}^c V_c,   Om_{ab}^c = w_a^{cd} eta_{db}
  [nabla_a, nabla_b] = -T_ab^c nabla_c + (1/2) R_ab^{cd} S_cd,
  (S_cd V)_e = eta_ed V_c - eta_ec V_d
  T_ab^c = -C_ab^c - Om_ab^c + Om_ba^c
  R_ab^f_c = e_a Om_bc^f - e_b Om_ac^f + Om_ac^d Om_bd^f - Om_bc^d Om_ad^f - C_ab^d Om_dc^f
  B1_b^e   = -nabla^a T_ab^e + T_ab^c T^a_c^e + R_ab^{ae}
  B2_b^{de}=  nabla^a R_ab^{de} - T_ab^c R^a_c^{de}
Fluctuation: delta D_a = -h_a^c D_c + (1/2) w_a^{cd} S_cd.  The amplitudes are
vectors in a mode space of dimension N on which the background frame acts by
matrices Eop[a] with [Eop[a], Eop[b]] = cbar_ab^c Eop[c].  For a character,
N = 1 and Eop[a] = i q_a (requires q_c cbar_ab^c = 0).
Every tensor is a pair (X0, X1): background constant, and first-order part with
one extra trailing mode axis.
"""
import itertools
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
PAIRS = [(c, d) for c in range(4) for d in range(c + 1, 4)]
NF = 40


def set_eta(diag):
    global ETA
    ETA = np.diag(np.asarray(diag, dtype=float))


def unpack(v, N):
    v = np.asarray(v, dtype=complex).reshape(NF, N)
    h = v[:16].reshape(4, 4, N)
    w = np.zeros((4, 4, 4, N), dtype=complex)
    for a in range(4):
        for n, (c, d) in enumerate(PAIRS):
            w[a, c, d] = v[16 + 6 * a + n]
            w[a, d, c] = -v[16 + 6 * a + n]
    return h, w


def pack(B1, B2):
    N = B1.shape[-1]
    out = np.zeros((NF, N), dtype=complex)
    out[:16] = B1.reshape(16, N)
    for b in range(4):
        for n, (d, e) in enumerate(PAIRS):
            out[16 + 6 * b + n] = B2[b, d, e]
    return out.reshape(NF * N)


def mul(spec, A, B):
    ins, out = spec.split('->')
    i1, i2 = ins.split(',')
    return (np.einsum(spec, A[0], B[0]),
            np.einsum(i1 + ',' + i2 + 'n->' + out + 'n', A[0], B[1])
            + np.einsum(i1 + 'n,' + i2 + '->' + out + 'n', A[1], B[0]))


def lin(spec, K, A):
    """Contract the constant array K with both parts of A."""
    ins, out = spec.split('->')
    i1, i2 = ins.split(',')
    return (np.einsum(spec, K, A[0]), np.einsum(i1 + ',' + i2 + 'n->' + out + 'n', K, A[1]))


def tr(A, perm):
    return (A[0].transpose(perm), A[1].transpose(tuple(perm) + (len(perm),)))


def add(*terms):
    return (sum(t[0] for t in terms), sum(t[1] for t in terms))


def scal(s, A):
    return (s * A[0], s * A[1])


def ed(Eop, X):
    """e_a X, new first index a.  The background part is constant."""
    return (np.zeros((4,) + X[0].shape, dtype=complex),
            np.einsum('anm,...m->a...n', Eop, X[1]))


def chars(q):
    return 1j * np.asarray(q, dtype=complex).reshape(4, 1, 1)


def nabla(Eop, Om, X, kinds):
    n = len(kinds)
    out = ed(Eop, X)
    letters = 'bcdefgh'[:n]
    for i, kind in enumerate(kinds):
        src = letters[:i] + 'z' + letters[i + 1:]
        if kind == 'l':      # + Om_{a b_i}^z X_{..z..}
            out = add(out, mul('a' + letters[i] + 'z,' + src + '->a' + letters, Om, X))
        else:                # - Om_{a z}^{b_i} X^{..z..}
            out = add(out, scal(-1.0, mul('az' + letters[i] + ',' + src + '->a' + letters, Om, X)))
    return out


def brackets(cbar, wbar, Eop, v):
    Eop = np.asarray(Eop, dtype=complex)
    N = Eop.shape[-1]
    h, w = unpack(v, N)
    cbar = np.asarray(cbar, dtype=complex)
    wbar = np.asarray(wbar, dtype=complex)
    Eh = np.einsum('anm,bdm->abdn', Eop, h)          # e_a h_b^d
    C1 = (np.einsum('abf,fdn->abdn', cbar, h) - Eh + Eh.transpose(1, 0, 2, 3)
          - np.einsum('bcn,acd->abdn', h, cbar) + np.einsum('acn,bcd->abdn', h, cbar))
    C = (cbar, C1)
    w1 = w - np.einsum('afn,fcd->acdn', h, wbar)
    Om = (np.einsum('acd,db->abc', wbar, ETA), np.einsum('acdn,db->abcn', w1, ETA))
    T = add(scal(-1.0, C), scal(-1.0, Om), tr(Om, (1, 0, 2)))
    eOm = ed(Eop, Om)                                 # [a,b,c,f] = e_a Om_bc^f
    R = add(eOm, scal(-1.0, tr(eOm, (1, 0, 2, 3))),
            mul('acd,bdf->abcf', Om, Om), scal(-1.0, mul('bcd,adf->abcf', Om, Om)),
            scal(-1.0, mul('abd,dcf->abcf', C, Om)))  # R[a,b,c,f] = R_ab^f_c
    Rup = lin('ce,abcf->abfe', ETA, R)                # R_ab^{fe}
    nT = nabla(Eop, Om, T, 'llu')                     # [x,a,b,e]
    Tup = lin('ax,xcd->acd', ETA, T)                  # T^a_c^e
    B1 = add(scal(-1.0, lin('xa,xabe->be', ETA, nT)),
             mul('abc,ace->be', T, Tup),
             lin('xa,xbae->be', np.eye(4), Rup))
    nR = nabla(Eop, Om, Rup, 'lluu')                  # [x,a,b,d,e]
    Rupup = lin('ax,xcde->acde', ETA, Rup)            # R^a_c^{de}
    B2 = add(lin('xa,xabde->bde', ETA, nR),
             scal(-1.0, mul('abc,acde->bde', T, Rupup)))
    return B1, B2, T, Rup


def background_residual(cbar, wbar):
    B1, B2, T, Rup = brackets(cbar, wbar, chars(np.zeros(4)), np.zeros(NF))
    return float(np.abs(B1[0]).max()), float(np.abs(B2[0]).max()), T[0].real, Rup[0].real


def M_op(cbar, wbar, Eop):
    """Matrix of the linearised brackets on C^40 (x) C^N, index = 40-index * N + mode."""
    N = np.asarray(Eop).shape[-1]
    M = np.zeros((NF * N, NF * N), dtype=complex)
    for n in range(NF * N):
        v = np.zeros(NF * N)
        v[n] = 1.0
        B1, B2, _, _ = brackets(cbar, wbar, Eop, v)
        M[:, n] = pack(B1[1], B2[1])
    return M


def M_of_q(cbar, wbar, q):
    return M_op(cbar, wbar, chars(q))


def M_coeffs(cbar, wbar, dirs=(0, 1, 2, 3)):
    """M(q) = M0 + i sum_mu M1[mu] q_mu - sum_{mu<=nu} M2[mu,nu] q_mu q_nu for
    characters, i.e. the real operator M0 + M1^mu d_mu + M2^{mu nu} d_mu d_nu."""
    z = np.zeros(4)
    M0 = M_of_q(cbar, wbar, z)
    M1, M2 = {}, {}

    def unit(m):
        e = np.zeros(4); e[m] = 1.0; return e
    for m in dirs:
        P, Nn = M_of_q(cbar, wbar, unit(m)), M_of_q(cbar, wbar, -unit(m))
        M1[m] = (P - Nn) / 2j
        M2[(m, m)] = -((P + Nn) / 2 - M0)
    for m, n in itertools.combinations(dirs, 2):
        P = M_of_q(cbar, wbar, unit(m) + unit(n))
        M2[(m, n)] = -(P - M0 - 1j * M1[m] - 1j * M1[n] + M2[(m, m)] + M2[(n, n)])
    for X in [M0] + list(M1.values()) + list(M2.values()):
        assert np.abs(X.imag).max() < 1e-12
    return M0.real, {k: x.real for k, x in M1.items()}, {k: x.real for k, x in M2.items()}


def pack_hw(h, w):
    N = h.shape[-1]
    out = np.zeros((NF, N), dtype=complex)
    out[:16] = h.reshape(16, N)
    for a in range(4):
        for n, (c, d) in enumerate(PAIRS):
            out[16 + 6 * a + n] = w[a, c, d]
    return out.reshape(NF * N)


def gauge_vectors(cbar, wbar, Eop):
    """Gauge directions (h, w), 10 N columns: local rotations and diffeomorphisms.
    [1/2 lam^{cd} S_cd, D_a] = lam^c_a D_c - 1/2 (D_a lam^{cd}) S_cd
    [xi^c D_c, D_a] = -(D_a xi^c) D_c + xi^c [D_c, D_a]   (Rbar = 0)."""
    Eop = np.asarray(Eop, dtype=complex)
    N = Eop.shape[-1]
    cbar = np.asarray(cbar, dtype=complex); wbar = np.asarray(wbar, dtype=complex)
    Om0 = np.einsum('acd,db->abc', wbar, ETA)
    Tbar = -cbar - Om0 + Om0.transpose(1, 0, 2)
    out = []
    for m in range(N):
        for (c, d) in PAIRS:
            lam = np.zeros((4, 4, N), dtype=complex); lam[c, d, m] = 1.0; lam[d, c, m] = -1.0
            h = -np.einsum('cdn,da->acn', lam, ETA)           # h_a^c = -lam^c_a
            Dlam = (np.einsum('anm,cdm->acdn', Eop, lam)
                    - np.einsum('azc,zdn->acdn', Om0, lam) - np.einsum('azd,czn->acdn', Om0, lam))
            out.append(pack_hw(h, -Dlam))
        for c in range(4):
            xi = np.zeros((4, N), dtype=complex); xi[c, m] = 1.0
            Dxi = np.einsum('anm,em->aen', Eop, xi) - np.einsum('aze,zn->aen', Om0, xi)
            h = Dxi + np.einsum('cn,cae->aen', xi, Tbar)
            out.append(pack_hw(h, np.zeros((4, 4, 4, N), dtype=complex)))
    return np.array(out).T


def lie(brs):
    c = np.zeros((4, 4, 4))
    for (a, b), val in brs.items():
        for d, x in val.items():
            c[a, b, d] += x
            c[b, a, d] -= x
    return c


def jacobi(c):
    J = (np.einsum('abd,dce->abce', c, c) + np.einsum('bcd,dae->abce', c, c)
         + np.einsum('cad,dbe->abce', c, c))
    return float(np.abs(J).max())


def rank(M, tol=1e-8):
    s = np.linalg.svd(M, compute_uv=False)
    return int((s > tol * max(1.0, s[0])).sum())


# Backgrounds ---------------------------------------------------------------
def flat():
    return np.zeros((4, 4, 4)), np.zeros((4, 4, 4))


def null_rotation_g1():
    """E_0 - E_3 central, [E_0+E_3, E_1] = E_2, [E_0+E_3, E_2] = -E_1; wbar = 0."""
    c = lie({(0, 1): {2: 0.5}, (3, 1): {2: 0.5}, (0, 2): {1: -0.5}, (3, 2): {1: -0.5}})
    return c, np.zeros((4, 4, 4))


def null_rotation_g2(kappa=1.0):
    """Flat frame, constant connection w_a^{12} = kappa k_a, k_a = (1,0,0,1)."""
    w = np.zeros((4, 4, 4))
    k = np.array([1.0, 0.0, 0.0, 1.0])
    for a in range(4):
        w[a, 1, 2] = kappa * k[a]; w[a, 2, 1] = -kappa * k[a]
    return np.zeros((4, 4, 4)), w


def heisenberg(kappa=1.0):
    """[E_3, E_1] = kappa E_2, E_0 and E_2 central; wbar = 0."""
    return lie({(3, 1): {2: kappa}}), np.zeros((4, 4, 4))


def second_algebra():
    """[E_0,E_2]=E_2, [E_0,E_3]=E_3, [E_1,E_2]=E_2, [E_1,E_3]=-E_3 (non-unimodular)."""
    return lie({(0, 2): {2: 1.0}, (0, 3): {3: 1.0}, (1, 2): {2: 1.0}, (1, 3): {3: -1.0}}), np.zeros((4, 4, 4))


def heisenberg_modes(p, q0, N, kappa=1.0):
    """Schroedinger representation of the Heisenberg background on N oscillator
    levels: E_2 = i p, E_0 = i q0, E_1 = sqrt(kappa p/2)(a - a^dag),
    E_3 = -i sqrt(kappa p/2)(a + a^dag), p > 0, so that [E_3, E_1] = kappa E_2.
    Exact except in the top level."""
    a = np.diag(np.sqrt(np.arange(1, N)), 1).astype(complex)
    ad = a.conj().T
    I = np.eye(N, dtype=complex)
    s = np.sqrt(kappa * p / 2.0)
    return np.array([1j * q0 * I, s * (a - ad), 1j * p * I, -1j * s * (a + ad)])
