"""Operator-level check of the first-order equivariant class on left-invariant data,
independent of the section-value formulas.  Z = G x SO(3,1) is embedded in G x GL(4)
with matrix coordinates u_a^b; every vector field used is tangent to the SO(3,1) orbits.
  S_cd(u_a^b)  = eta_ad u_c^b - eta_ac u_d^b                 (left action on the first index)
  D_a = u_a^b H_b,  H_b = E_b + (u_c^f Om_bf^g) d/du_c^g      (horizontal lift)
with [E_a, E_b] = C_ab^c E_c abstract left-invariant fields (coefficients depend on u only).
Functions: (i) the relations [S_cd, D_a] = eta_ad D_c - eta_ac D_d and
[D_a, D_b] = -T_ab^c(u) D_c + 1/2 R_ab^{cd}(u) S_cd are solved for T(u), R(u) at a random
Lorentz u and compared with the rotated section values of bg.py; (ii) the vector field
M_b = eta^{ac}[D_c,[D_a,D_b]] is evaluated at random Lorentz u.
"""
import itertools
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
import bg

U = sp.Matrix(4, 4, lambda i, j: sp.Symbol('u%d%d' % (i, j)))
UL = list(U)


def vf_apply(V, f):
    return sum(V['u'][k] * sp.diff(f, UL[k]) for k in range(16))


def comm(V, W, C):
    out = {'E': [0] * 4, 'u': [0] * 16}
    for k in range(4):
        x = vf_apply(V, W['E'][k]) - vf_apply(W, V['E'][k])
        x += sum(V['E'][i] * W['E'][j] * C[i, j, k] for i in range(4) for j in range(4) if C[i, j, k] != 0)
        out['E'][k] = sp.expand(x)
    for k in range(16):
        out['u'][k] = sp.expand(vf_apply(V, W['u'][k]) - vf_apply(W, V['u'][k]))
    return out


def lin(coefs, fields):
    out = {'E': [0] * 4, 'u': [0] * 16}
    for c, F in zip(coefs, fields):
        for k in range(4):
            out['E'][k] += c * F['E'][k]
        for k in range(16):
            out['u'][k] += c * F['u'][k]
    return out


def build(C, W, eta):
    Om = np.einsum('acd,db->abc', W, eta)
    Om = sp.Array(Om.shape and [[[sp.nsimplify(float(x), rational=True) for x in r2] for r2 in r1] for r1 in Om])
    D = []
    for a in range(4):
        F = {'E': [U[a, b] for b in range(4)], 'u': [0] * 16}
        for c in range(4):
            for g in range(4):
                F['u'][4 * c + g] = sp.expand(sum(U[a, b] * U[c, f] * Om[b, f, g]
                                                  for b in range(4) for f in range(4)))
        D.append(F)
    S = {}
    for c, d in itertools.combinations(range(4), 2):
        F = {'E': [0] * 4, 'u': [0] * 16}
        for a in range(4):
            for b in range(4):
                F['u'][4 * a + b] = eta[a, d] * U[c, b] - eta[a, c] * U[d, b]
        S[(c, d)] = F
    return D, S


def numvec(F, sub):
    return np.array([complex(sp.N(x.subs(sub))) if x != 0 else 0 for x in F['E'] + F['u']]).real


def random_lorentz(rng, eta):
    from scipy.linalg import expm
    X = rng.normal(size=(4, 4))
    A = X - eta @ X.T @ eta          # eta-antisymmetric after lowering: (eta A) antisym
    A = 0.4 * A
    L = expm(A)
    assert np.abs(L @ eta @ L.T - eta).max() < 1e-10
    return L


def check(C, W, sig, seed=0, npts=2, matrix_eq=True):
    eta = bg.eta_of(sig)
    Cs = sp.Array([[[sp.nsimplify(float(x), rational=True) for x in r2] for r2 in r1] for r1 in np.asarray(C)])
    D, S = build(C, W, eta)
    pairs = list(S.keys())
    rng = np.random.default_rng(seed)
    _, _, Th, Rh = bg.brackets(C, W, eta)
    out = []
    comms = {(a, b): comm(D[a], D[b], Cs) for a in range(4) for b in range(4) if a < b}
    if matrix_eq:
        etai = np.linalg.inv(eta)
        M = []
        for b in range(4):
            terms = []
            for a in range(4):
                if a == b:
                    continue
                Fab = comms[(a, b)] if a < b else lin([-1], [comms[(b, a)]])
                terms.append(lin([etai[a, a]], [comm(D[a], Fab, Cs)]))
            M.append(lin([1] * len(terms), terms))
    for p in range(npts):
        L = random_lorentz(rng, eta)
        sub = {UL[k]: L.flat[k] for k in range(16)}
        basis = np.array([numvec(F, sub) for F in D] + [numvec(S[k], sub) for k in pairs]).T
        err_rel, err_T, err_R = 0.0, 0.0, 0.0
        Linv = np.linalg.inv(L)
        Tu = np.einsum('aA,bB,ABC,Cc->abc', L, L, Th, Linv)
        Ru = np.einsum('aA,bB,ABCD,Cc,Dd->abcd', L, L, Rh, Linv, Linv)
        for (a, b), F in comms.items():
            v = numvec(F, sub)
            x, *_ = np.linalg.lstsq(basis, v, rcond=None)
            err_rel = max(err_rel, np.abs(basis @ x - v).max())
            err_T = max(err_T, np.abs(-x[:4] - Tu[a, b]).max())
            for n, (c, d) in enumerate(pairs):
                err_R = max(err_R, abs(x[4 + n] - Ru[a, b, c, d]))
        # first relation
        err_S = 0.0
        for (c, d), F in S.items():
            for a in range(4):
                v = numvec(comm(F, D[a], Cs), sub)
                tgt = eta[a, d] * numvec(D[c], sub) - eta[a, c] * numvec(D[d], sub)
                err_S = max(err_S, np.abs(v - tgt).max())
        res = {'span_defect': err_rel, 'T_vs_sectionvalue': err_T, 'R_vs_sectionvalue': err_R,
               'first_relation': err_S}
        if matrix_eq:
            res['matrix_eq_max'] = max(np.abs(numvec(Mb, sub)).max() for Mb in M)
        out.append(res)
    return out
