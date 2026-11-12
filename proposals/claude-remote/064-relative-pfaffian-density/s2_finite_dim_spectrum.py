"""
064 / s2: the fibre formula of s1 tested on explicit finite-dimensional representations, and the compact
relative Pfaffian.

Representations: V_n = Sym^n of the 4-dim spinor of so(5), n = 1, 2, with the Lorentzian real form so(4,1)
obtained by the Weyl trick (as in 062/s1). Adjoint action on End(V_n), Dirac spinor C^4 of so(3,1).

 (a) the spectrum (with multiplicities) of the chiral block of D^2 on C^2 (x) End(V_n) equals the multiset
     predicted by s1: for each so(5) component (m1,m2) of End(V_n) and each Gelfand-Tsetlin so(4) component
     (k1,k2), eigenvalue A+1-z with multiplicity (z+1)(2j_R+1) and A+1+z with multiplicity (z-1)(2j_R+1),
     z = 2 j_L + 1 = k1+k2+1, 2 j_R + 1 = k1-k2+1, A = C5 - C4. So the spinor weights (z+-1)/z are the
     multiplicities per unit orbital dimension in the compact case.
 (b) compact relative Pfaffian on the traceless matrices,
        log Pf_rel(eps) = (1/4) [ Tr_16 log(D^2 - i eps) - 16 Tr log(Box - i eps) ],  16 = 4 copies of C^4,
     behaves as (K/4) log eps with K = dim ker on the 16 components (80 for n = 1, 304 for n = 2), so
     Pf_rel(eps) -> 0 as eps -> 0; Box = C5 - C4 has no kernel on the traceless matrices.
"""
import numpy as np, itertools, math

out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex); I2 = np.eye(2)
gE = [np.kron(s1, s1), np.kron(s1, s2), np.kron(s1, s3), np.kron(s2, I2), np.kron(s3, I2)]
M4 = {(A, B): -0.25j * (gE[A] @ gE[B] - gE[B] @ gE[A]) for A in range(5) for B in range(5)}

def sym_power2(n):
    d = 4 ** n
    P = np.zeros((d, d))
    for perm in itertools.permutations(range(n)):
        for idx in itertools.product(range(4), repeat=n):
            src = np.ravel_multi_index(idx, [4] * n)
            dst = np.ravel_multi_index(tuple(idx[q] for q in perm), [4] * n)
            P[dst, src] += 1
    P /= math.factorial(n)
    w, v = np.linalg.eigh(P)
    B = v[:, w > 0.5]
    def rep(X):
        tot = np.zeros((d, d), complex)
        for kk in range(n):
            ops = [np.eye(4)] * n; ops[kk] = X
            t = ops[0]
            for o in ops[1:]:
                t = np.kron(t, o)
            tot += t
        return B.conj().T @ tot @ B
    return rep, B.shape[1]

eta5 = np.diag([-1., 1, 1, 1, 1]); eta4 = np.diag([-1., 1, 1, 1])
gU = [1j * gE[0], gE[1], gE[2], gE[3]]
chir = gU[0] @ gU[1] @ gU[2] @ gU[3]
chir = chir * (1j if np.allclose(chir @ chir, -np.eye(4)) else 1)
assert np.allclose(chir @ chir, np.eye(4))

def predicted_chiral_spectrum(n):
    ev = []
    for m1 in range(0, n + 1):
        for m2 in range(0, m1 + 1):
            C5 = m1 * (m1 + 3) + m2 * (m2 + 1)
            for k1 in range(m2, m1 + 1):
                for k2 in range(-m2, m2 + 1):
                    C4 = k1 * k1 + 2 * k1 + k2 * k2
                    Aval = C5 - C4; zz = k1 + k2 + 1; dR = k1 - k2 + 1
                    ev += [Aval + 1 - zz] * ((zz + 1) * dR) + [Aval + 1 + zz] * ((zz - 1) * dR)
    return np.sort(np.array(ev, float))

for n in (1, 2):
    rep, dV = sym_power2(n)
    Mv = {kk: rep(v) for kk, v in M4.items()}
    L = {(A, B): (1j * X if ((A == 0) != (B == 0)) else X) for (A, B), X in Mv.items()}
    Iv = np.eye(dV)
    ad = {kk: np.kron(X, Iv) - np.kron(Iv, X.T) for kk, X in L.items()}
    dE = dV * dV
    C5 = 0.5 * sum(eta5[A, A] * eta5[B, B] * ad[(A, B)] @ ad[(A, B)] for A in range(5) for B in range(5))
    C4 = 0.5 * sum(eta5[A, A] * eta5[B, B] * ad[(A, B)] @ ad[(A, B)] for A in range(4) for B in range(4))
    T_low = [ad[(a, 4)] for a in range(4)]
    D = sum(np.kron(gU[a], T_low[a]) for a in range(4))
    Box = sum(eta4[a, a] * T_low[a] @ T_low[a] for a in range(4))
    assert np.abs(Box - (C5 - C4)).max() < 1e-9
    w, v = np.linalg.eigh((chir + chir.conj().T) / 2)
    IE = np.eye(dE)
    pred = predicted_chiral_spectrum(n)
    for chi in (+1, -1):
        Pr = np.kron(v[:, np.isclose(w, chi)], IE)
        blk = Pr.conj().T @ (D @ D) @ Pr
        evs = np.sort(np.linalg.eigvals(blk).real)
        imax = np.abs(np.linalg.eigvals(blk).imag).max()
        dev = np.abs(evs - pred).max() if len(evs) == len(pred) else np.inf
        log(f'n={n} chirality {chi:+d}: size {blk.shape[0]}, predicted {len(pred)}; max |eigenvalue - prediction| = {dev:.1e}; max |Im| = {imax:.1e}')
        assert dev < 1e-8
    # (b) relative Pfaffian on traceless matrices
    tr = np.eye(dV).reshape(-1) / np.sqrt(dV)          # unit trace mode (row-major vec of identity)
    Q, _ = np.linalg.qr(np.column_stack([tr, np.random.default_rng(1).standard_normal((dE, dE - 1))]))
    B0 = Q[:, 1:]                                       # orthonormal basis of the traceless matrices
    BoxT = B0.conj().T @ Box @ B0
    Pt = np.kron(np.eye(4), B0)
    D2T = Pt.conj().T @ (D @ D) @ Pt
    eD = np.linalg.eigvalsh((D2T + D2T.conj().T) / 2); eB = np.linalg.eigvalsh((BoxT + BoxT.conj().T) / 2)
    Kc4 = int(np.sum(np.abs(eD) < 1e-9)); KB = int(np.sum(np.abs(eB) < 1e-9))
    log(f'   traceless: kernel of D^2 on C^4 (x) End_0 = {Kc4}, so K on the 16 components = {4 * Kc4}; kernel of Box on End_0 = {KB}; min Box eigenvalue = {eB.min():.4f}')
    def logPf(eps):
        return 0.25 * (4 * np.sum(np.log(eD - 1j * eps)) - 16 * np.sum(np.log(eB - 1j * eps)))
    prev = None
    for eps in (1e-2, 1e-4, 1e-6, 1e-8):
        lp = logPf(eps)
        slope = None if prev is None else (lp.real - prev[1].real) / (np.log(eps) - np.log(prev[0]))
        log(f'   eps = {eps:.0e}: log|Pf_rel| = {lp.real:.4f}' + ('' if slope is None else f', d log|Pf_rel| / d log eps = {slope:.4f}'))
        prev = (eps, lp)
    assert abs(slope - Kc4) < 1e-3   # (1/4) * 4 * Kc4 = K/4
    log(f'   slope = K/4 = {Kc4}: Pf_rel(eps) ~ eps^(K/4) -> 0')
log('All checks passed.')
open(__file__.replace('.py', '.out.txt'), 'w').write('\n'.join(out) + '\n')
