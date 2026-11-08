"""
062 / s1: enveloping-algebra identities used for the so(4,1) (W timelike) member, checked on explicit
finite-dimensional (hence non-unitary) representations of the Lorentzian real form so(4,1), obtained from
compact so(5) representations by the Weyl trick L_{0B} = i M_{0B}.

Checks (adjoint action on End(V), V = Sym^n of the 4-dim spinor of so(5), n = 1, 2):
 (a) L_AB obey [L_AB, L_CD] = i(eta_BC L_AD - eta_AC L_BD - eta_BD L_AC + eta_AD L_BC), eta = diag(-1,1,1,1,1)
     (the convention of Manta-Steinacker 2502.02498, Eq. (1)); T^a = L^{a4}, a = 0..3.
 (b) Clifford: {g^a, g^b} = 2 eta^{ab} on C^4; spin generators S_ab obey the same algebra as ad L_ab.
 (c) D = g^a ad(T_a):  D^2 = C5 - C4tot + 3/2   (Casimirs formed with eta).
 (d) on each chirality block: X := (C4tot - C4 - 3/2)/2 satisfies X^2 + X = J_L^2, with
     4 J_L^2 = C4 + 2 i s P, P = J.K, s = +1 or -1 by chirality (determined here), and C4 = 2(J_L^2 + J_R^2).
 (e) D^2 = C5 - C4 - 2X on each chirality block; kernel dimension of D in these non-unitary finite-dim
     representations (it is non-zero: the j_L of finite-dimensional so(3,1) components are real).
"""
import numpy as np, itertools
np.set_printoptions(precision=3, suppress=True)

# Euclidean Cl(5) on C^4: Hermitian g_E[0..4]
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex); I2 = np.eye(2)
gE = [np.kron(s1, s1), np.kron(s1, s2), np.kron(s1, s3), np.kron(s2, I2), np.kron(s3, I2)]
for A in range(5):
    for B in range(5):
        assert np.allclose(gE[A] @ gE[B] + gE[B] @ gE[A], 2 * (A == B) * np.eye(4))
# compact so(5) Hermitian generators on the spinor: M_AB = -(i/4)[g_A, g_B]
M4 = {(A, B): -0.25j * (gE[A] @ gE[B] - gE[B] @ gE[A]) for A in range(5) for B in range(5)}

import math
def sym_power2(n):
    d = 4 ** n
    P = np.zeros((d, d))
    for perm in itertools.permutations(range(n)):
        for idx in itertools.product(range(4), repeat=n):
            src = np.ravel_multi_index(idx, [4] * n)
            dst = np.ravel_multi_index(tuple(idx[p] for p in perm), [4] * n)
            P[dst, src] += 1
    P /= math.factorial(n)
    w, v = np.linalg.eigh(P)
    B = v[:, w > 0.5]
    def rep(X):
        tot = np.zeros((d, d), complex)
        for k in range(n):
            ops = [np.eye(4)] * n; ops[k] = X
            t = ops[0]
            for o in ops[1:]:
                t = np.kron(t, o)
            tot += t
        return B.conj().T @ tot @ B
    return rep, B.shape[1]

eta5 = np.diag([-1., 1, 1, 1, 1])
eta4 = np.diag([-1., 1, 1, 1])
# Lorentzian Clifford on C^4 with {g^a, g^b} = 2 eta^{ab}: g^0 = i gE0, g^i = gE_i
gU = [1j * gE[0], gE[1], gE[2], gE[3]]
for a in range(4):
    for b in range(4):
        assert np.allclose(gU[a] @ gU[b] + gU[b] @ gU[a], 2 * eta4[a, b] * np.eye(4))
gL = [sum(eta4[a, b] * gU[b] for b in range(4)) for a in range(4)]  # lower index
chir = gU[0] @ gU[1] @ gU[2] @ gU[3]
# normalise chirality to square to +1
c2 = chir @ chir
chir = chir * (1j if np.allclose(c2, -np.eye(4)) else 1)
assert np.allclose(chir @ chir, np.eye(4))
for a in range(4):
    assert np.allclose(chir @ gU[a] + gU[a] @ chir, 0)

def comm(X, Y): return X @ Y - Y @ X

out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

for n in (1, 2):
    rep, dV = sym_power2(n)
    Mv = {k: rep(v) for k, v in M4.items()}
    # Lorentzian real form (Weyl trick): L_{0B} = i M_{0B}, L_{AB} = M_{AB} for A,B >= 1
    L = {}
    for (A, B), X in Mv.items():
        L[(A, B)] = (1j * X) if ((A == 0) != (B == 0)) else X
    # (a) commutation relations
    err = 0; err_alt = 0
    for (A, B), (C, Dd) in itertools.product(L.keys(), repeat=2):
        lhs = comm(L[(A, B)], L[(C, Dd)])
        rhs = 1j * (eta5[B, C] * L[(A, Dd)] - eta5[A, C] * L[(B, Dd)] - eta5[B, Dd] * L[(A, C)] + eta5[A, Dd] * L[(B, C)])
        err = max(err, np.abs(lhs - rhs).max())
        err_alt = max(err_alt, np.abs(lhs + rhs).max())
    log(f'n={n}: dim V={dV}; so(4,1) relations (MS Eq.(1) sign) residual {err:.1e}; opposite sign residual {err_alt:.1e}')
    sgn = 1 if err < 1e-10 else -1
    assert min(err, err_alt) < 1e-10
    # adjoint action on End(V) (row-major vec: vec(XY - YX) = (X (x) I - I (x) X^T) vec(Y))
    Iv = np.eye(dV)
    ad = {k: np.kron(X, Iv) - np.kron(Iv, X.T) for k, X in L.items()}
    dE = dV * dV
    def up(A, B):  # L^{AB}
        return eta5[A, A] * eta5[B, B] * ad[(A, B)]
    C5 = 0.5 * sum(eta5[A, A] * eta5[B, B] * ad[(A, B)] @ ad[(A, B)] for A in range(5) for B in range(5))
    C4 = 0.5 * sum(eta5[A, A] * eta5[B, B] * ad[(A, B)] @ ad[(A, B)] for A in range(4) for B in range(4))
    T_low = [ad[(a, 4)] for a in range(4)]  # T_a = L_{a4}
    # (b) spin generators with the same algebra: try S_ab = +-(i/4)[g_a, g_b]
    best = None
    for ss in (1, -1):
        S = {(a, b): ss * 0.25j * comm(gL[a], gL[b]) for a in range(4) for b in range(4)}
        e = 0
        for (A, B), (C, Dd) in itertools.product(S.keys(), repeat=2):
            lhs = comm(S[(A, B)], S[(C, Dd)])
            rhs = sgn * 1j * (eta4[B, C] * S[(A, Dd)] - eta4[A, C] * S[(B, Dd)] - eta4[B, Dd] * S[(A, C)] + eta4[A, Dd] * S[(B, C)])
            e = max(e, np.abs(lhs - rhs).max())
        if e < 1e-10:
            best = (ss, S)
    assert best is not None
    ss, S = best
    log(f'   spin generators S_ab = {ss:+d}(i/4)[g_a,g_b] obey the same relations as ad L_ab')
    I4 = np.eye(4); IE = np.eye(dE)
    Lt = {(a, b): np.kron(I4, ad[(a, b)]) + np.kron(S[(a, b)], IE) for a in range(4) for b in range(4)}
    C4tot = 0.5 * sum(eta4[a, a] * eta4[b, b] * Lt[(a, b)] @ Lt[(a, b)] for a in range(4) for b in range(4))
    C5b = np.kron(I4, C5); C4b = np.kron(I4, C4)
    D = sum(np.kron(gU[a], T_low[a]) for a in range(4))
    r_c = np.abs(D @ D - (C5b - C4tot + 1.5 * np.eye(4 * dE))).max()
    r_alt = np.abs(D @ D - (C5b - C4tot - 1.5 * np.eye(4 * dE))).max()
    log(f'   (c) |D^2 - (C5 - C4tot + 3/2)| = {r_c:.1e}   (control with -3/2: {r_alt:.1e})')
    # chirality blocks
    w, v = np.linalg.eigh((chir + chir.conj().T) / 2)
    for chi in (+1, -1):
        Pb = v[:, np.isclose(w, chi)]  # 4x2
        Pr = np.kron(Pb, IE)
        def blk(O): return Pr.conj().T @ O @ Pr
        X = 0.5 * (blk(C4tot) - blk(C4b) - 1.5 * np.eye(2 * dE))
        # J, K from ad L
        J = [0.5 * sum((1 if (i, j, k) in [(1, 2, 3), (2, 3, 1), (3, 1, 2)] else -1 if (i, j, k) in [(2, 1, 3), (3, 2, 1), (1, 3, 2)] else 0) * ad[(i, j)] for i in range(1, 4) for j in range(1, 4)) for k in range(1, 4)]
        K = [ad[(0, i)] for i in range(1, 4)]
        P = sum(J[k] @ K[k] for k in range(3))
        assert np.abs(sum(J[k] @ J[k] for k in range(3)) - sum(K[k] @ K[k] for k in range(3)) - C4).max() < 1e-9
        res = {}
        for s in (+1, -1):
            JL2 = 0.25 * (C4 + 2j * s * P)
            res[s] = np.abs(X @ X + X - np.kron(np.eye(2), JL2)).max()
        s_ok = min(res, key=res.get)
        JL2 = 0.25 * (C4 + 2j * s_ok * P); JR2 = 0.25 * (C4 - 2j * s_ok * P)
        r_sum = np.abs(C4 - 2 * (JL2 + JR2)).max()
        r_e = np.abs(blk(D @ D) - (blk(C5b) - blk(C4b) - 2 * X)).max()
        # kernel of the chiral piece of D: D maps chirality chi to -chi
        Pm = np.kron(v[:, np.isclose(w, -chi)], IE)
        Wop = Pm.conj().T @ D @ Pr
        sv = np.linalg.svd(Wop, compute_uv=False)
        ker = int(np.sum(sv < 1e-8 * max(1, sv.max())))
        log(f'   chirality {chi:+d}: |X^2+X-J_L^2| with s=+1: {res[1]:.1e}, s=-1: {res[-1]:.1e}  -> s={s_ok:+d};'
            f' |C4-2(J_L^2+J_R^2)| {r_sum:.1e}; (e) |D^2-(C5-C4-2X)| {r_e:.1e}; dim ker(W) = {ker}')
        assert res[s_ok] < 1e-9 and r_sum < 1e-9 and r_e < 1e-9
log('All identities hold to machine precision on these finite-dimensional representations of the Lorentzian real form.')
log('The kernels found are those of non-unitary finite-dimensional representations, where j_L is real; they are not a statement about unitary representations.')
open(__file__.replace('.py', '.out.txt'), 'w').write('\n'.join(out) + '\n')
