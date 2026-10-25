"""
s1_factorisation.py  (proposal 044)

Exact factorisation of the weighted one-loop heat trace of the maximally supersymmetric content
(10-component vector, weight +1; 16-component Weyl spinor, weight -1/2; ghosts, weight -2) on a
product background M x K, Euclidean so(10).

Model (finite-dimensional, so that every trace is exact):
  Hilbert space  H = H_M (x) H_K,  dim H_M = nM, dim H_K = nK.
  Common scalar operator  H0 = hM (x) 1 + 1 (x) hK.
  Vector:   H_V = H0 (x) 1_10 + sum_{a<b in M} lam f_ab (x) 1 (x) Sig_V^{ab} + sum_{i<j in K} mu 1 (x) k_ij (x) Sig_V^{ij}
  Spinor:   H_S = same with Sig_S^{IJ} = (i/4)[Gam^I, Gam^J] restricted to the 16 (Weyl) of so(10).
  No mixed flux (f_{ai} = 0); the f_ab act on H_M only, the k_ij on H_K only; f, k, hM, hK are random
  Hermitian matrices and do NOT commute with each other (generic Duhamel ordering).
  str(s) := Tr e^{-s H_V} - (1/2) Tr e^{-s H_S} - 2 Tr e^{-s H0}.

Checks:
 (A) the factorisation identity, for the splits d_M = 4 (so(4) x so(6), 16 = (2+,4+) + (2-,4-) or the
     other pairing) and d_M = 7 (so(7) x so(3), 16 = (8,2)), computed from independent M- and K-traces:
       d_M=4:  str = V^M s0^K + s0^M V^K - 2 s0^M s0^K - 1/2 (S+^M S+^K + S-^M S-^K)
       d_M=7:  str = V^M s0^K + s0^M V^K - 2 s0^M s0^K - 1/2 S8^M S2^K
 (B) Taylor coefficients c_{mn} of str in (lam, mu) (2D Fourier on circles; str is entire):
       c_{m0} = c_{0n} = 0 for m,n <= 3;  c_{1n} = c_{m1} = 0;  c_{22} = -(1/8) v2^M v2^K,
     with v2 the lam^2 (mu^2) coefficient of the index part V - d s0 of the vector trace;
     index relations used in the proposal (Dynkin-index equalities and conjugate-representation signs).
"""
import numpy as np
from scipy.linalg import expm
from itertools import combinations
rng = np.random.default_rng(20261025)

X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)

def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms: out = np.kron(out, m)
    return out

def gammas(n):
    """Hermitian Euclidean gamma matrices for so(2m), n = 2m, size 2^m (Jordan-Wigner)."""
    m = n // 2; gs = []
    for k in range(m):
        pre = [Z] * k; post = [I2] * (m - k - 1)
        gs.append(kron(*(pre + [X] + post))); gs.append(kron(*(pre + [Y] + post)))
    return gs

def chirality(gs):
    P = np.eye(gs[0].shape[0], dtype=complex)
    for g in gs: P = P @ g
    for c in (1, 1j, -1, -1j):
        C = c * P
        if np.allclose(C, C.conj().T) and np.allclose(C @ C, np.eye(C.shape[0])): return C
    raise RuntimeError

def spin_gens(gs, basis=None):
    """Sig^{IJ} = (i/4)[g_I, g_J] (Hermitian), optionally restricted to the columns of basis."""
    S = {}
    for I, J in combinations(range(len(gs)), 2):
        M = 0.25j * (gs[I] @ gs[J] - gs[J] @ gs[I])
        if basis is not None: M = basis.conj().T @ M @ basis
        S[(I, J)] = M
    return S

def vec_gens(n):
    S = {}
    for I, J in combinations(range(n), 2):
        M = np.zeros((n, n), complex); M[I, J] = 1j; M[J, I] = -1j
        S[(I, J)] = M
    return S

def eig_basis(C, val):
    w, v = np.linalg.eigh(C); return v[:, np.isclose(w, val)]

def rand_herm(n, scale=1.0):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return scale * (A + A.conj().T) / 2

def rand_pos(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return A @ A.conj().T / n + 0.5 * np.eye(n)

def tr_exp(H, s): return np.trace(expm(-s * H))

# so(10) data
G10 = gammas(10); C11 = chirality(G10); B16 = eig_basis(C11, 1.0); assert B16.shape[1] == 16
SV10 = vec_gens(10); SS16 = spin_gens(G10, B16)
# normalisation check: tr_10(Sig Sig) = 2, tr_16(Sig Sig) = 4, so str(Sig Sig) = 2 - 4/2 = 0
assert np.isclose(np.trace(SV10[(0, 1)] @ SV10[(0, 1)]).real, 2) and np.isclose(np.trace(SS16[(0, 1)] @ SS16[(0, 1)]).real, 4)

def full_str(s, hM, hK, f, k, dM, lam, mu):
    nM, nK = hM.shape[0], hK.shape[0]
    IM, IK = np.eye(nM), np.eye(nK)
    H0 = np.kron(hM, IK) + np.kron(IM, hK)
    def op(gens, dim):
        H = np.kron(H0, np.eye(dim))
        for (I, J), F in f.items(): H = H + lam * np.kron(np.kron(F, IK), gens[(I, J)])
        for (I, J), F in k.items(): H = H + mu * np.kron(np.kron(IM, F), gens[(I + dM, J + dM)])
        return H
    return tr_exp(op(SV10, 10), s) - 0.5 * tr_exp(op(SS16, 16), s) - 2 * tr_exp(H0, s)

def block_tr(s, h, fl, gens, dim, scale, basis=None):
    n = h.shape[0]; H = np.kron(h, np.eye(dim))
    for key, F in fl.items():
        g = gens[key] if basis is None else basis.conj().T @ gens[key] @ basis
        H = H + scale * np.kron(F, g)
    return tr_exp(H, s)

def setup(dM, nM=3, nK=2):
    dK = 10 - dM
    hM, hK = rand_pos(nM), rand_pos(nK)
    f = {key: rand_herm(nM, 0.7) for key in combinations(range(dM), 2)}
    k = {key: rand_herm(nK, 0.7) for key in combinations(range(dK), 2)}
    return hM, hK, f, k

def mk_spinor_blocks(dM):
    dK = 10 - dM
    if dM == 4:
        gM = gammas(4); gK = gammas(6)
        cM, cK = chirality(gM), chirality(gK)
        SM = spin_gens(gM); SK = spin_gens(gK)
        return dict(M={'+': (SM, eig_basis(cM, 1)), '-': (SM, eig_basis(cM, -1))},
                    K={'+': (SK, eig_basis(cK, 1)), '-': (SK, eig_basis(cK, -1))})
    if dM == 7:
        g6 = gammas(6); g7 = g6 + [chirality(g6)]
        SM = spin_gens(g7)
        gK = [X, Y, Z]; SK = spin_gens(gK)
        return dict(M={'8': (SM, None)}, K={'2': (SK, None)})
    raise ValueError

def pieces(s, hM, hK, f, k, dM, lam, mu, blocks):
    dK = 10 - dM
    s0M, s0K = tr_exp(hM, s), tr_exp(hK, s)
    VM = block_tr(s, hM, f, vec_gens(dM), dM, lam)
    VK = block_tr(s, hK, k, vec_gens(dK), dK, mu)
    SMb = {c: block_tr(s, hM, f, SG, (B.shape[1] if B is not None else SG[(0, 1)].shape[0]), lam, B) for c, (SG, B) in blocks['M'].items()}
    SKb = {c: block_tr(s, hK, k, SG, (B.shape[1] if B is not None else SG[(0, 1)].shape[0]), mu, B) for c, (SG, B) in blocks['K'].items()}
    return s0M, s0K, VM, VK, SMb, SKb

out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

P("=== (A) factorisation identity ===")
for dM in (4, 7):
    blocks = mk_spinor_blocks(dM)
    for trial in range(3):
        hM, hK, f, k = setup(dM)
        s, lam, mu = 0.6, 1.0, 1.0
        lhs = full_str(s, hM, hK, f, k, dM, lam, mu)
        s0M, s0K, VM, VK, SMb, SKb = pieces(s, hM, hK, f, k, dM, lam, mu, blocks)
        base = VM * s0K + s0M * VK - 2 * s0M * s0K
        if dM == 4:
            r1 = base - 0.5 * (SMb['+'] * SKb['+'] + SMb['-'] * SKb['-'])
            r2 = base - 0.5 * (SMb['+'] * SKb['-'] + SMb['-'] * SKb['+'])
            P(f"dM=4 trial {trial}: str = {lhs.real:+.12e}{lhs.imag:+.1e}i | rel.res pairing(++,--) = {abs(lhs-r1)/abs(lhs):.2e} | pairing(+-,-+) = {abs(lhs-r2)/abs(lhs):.2e}")
        else:
            r1 = base - 0.5 * SMb['8'] * SKb['2']
            P(f"dM=7 trial {trial}: str = {lhs.real:+.12e}{lhs.imag:+.1e}i | rel.res (8,2) = {abs(lhs-r1)/abs(lhs):.2e}")

def taylor2(fun, N=20, r=1.0):
    th = 2 * np.pi * np.arange(N) / N
    vals = np.array([[fun(r * np.exp(1j * a), r * np.exp(1j * b)) for b in th] for a in th])
    C = np.fft.fft2(vals) / N**2
    return lambda m, n: C[m % N, n % N] / r**(m + n)

def taylor1(fun, N=20, r=1.0):
    th = 2 * np.pi * np.arange(N) / N
    vals = np.array([fun(r * np.exp(1j * a)) for a in th]); C = np.fft.fft(vals) / N
    return lambda m: C[m % N] / r**m

P("")
P("=== (B) Taylor coefficients c_{mn} of str in (lam, mu), s = 0.6 ===")
for dM in (4, 7):
    dK = 10 - dM
    blocks = mk_spinor_blocks(dM)
    hM, hK, f, k = setup(dM)
    s = 0.6
    c = taylor2(lambda l, m: full_str(s, hM, hK, f, k, dM, l, m))
    scale = abs(c(4, 0)) + abs(c(0, 4)) + abs(c(2, 2))
    P(f"-- dM = {dM}: scale |c40|+|c04|+|c22| = {scale:.3e}")
    for (m, n) in [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, 2), (0, 3), (1, 1), (2, 1), (1, 2), (3, 1), (1, 3)]:
        P(f"   c_{m}{n}/scale = {abs(c(m, n))/scale:.2e}   (expected 0)")
    P(f"   c_40 = {c(4,0).real:+.6e}, c_04 = {c(0,4).real:+.6e}  (nonzero: first M-only / K-only order)")
    s0M, s0K = tr_exp(hM, s), tr_exp(hK, s)
    vM = taylor1(lambda l: block_tr(s, hM, f, vec_gens(dM), dM, l) - dM * s0M)
    vK = taylor1(lambda m: block_tr(s, hK, k, vec_gens(dK), dK, m) - dK * s0K)
    pred22 = -(1 / 8) * vM(2) * vK(2)
    P(f"   c_22 = {c(2,2).real:+.10e} ; -(1/8) v2M v2K = {pred22.real:+.10e} ; rel.diff = {abs(c(2,2)-pred22)/abs(pred22):.2e}")
    P(f"   v1M = {abs(vM(1)):.1e}, v3M = {abs(vM(3)):.1e}, v1K = {abs(vK(1)):.1e}, v3K = {abs(vK(3)):.1e}  (vector-index odd orders; nonzero allowed for non-commuting fluxes, structure-constant part)")
    # spinor index parts
    sp = {}
    for side, h, fl, sc in (('M', hM, f, None), ('K', hK, k, None)):
        for cname, (SG, B) in blocks[side].items():
            dim = B.shape[1] if B is not None else SG[(0, 1)].shape[0]
            s0 = s0M if side == 'M' else s0K
            if side == 'M':
                sp[(side, cname)] = taylor1(lambda l, SG=SG, B=B, dim=dim: block_tr(s, hM, f, SG, dim, l, B) - dim * s0M)
            else:
                sp[(side, cname)] = taylor1(lambda m, SG=SG, B=B, dim=dim: block_tr(s, hK, k, SG, dim, m, B) - dim * s0K)
    if dM == 4:
        sgp, sgm = sp[('M', '+')], sp[('M', '-')]; tp, tm = sp[('K', '+')], sp[('K', '-')]
        P(f"   so(4): v2M = {vM(2).real:+.8e} ; 2(sig2+ + sig2-) = {2*(sgp(2)+sgm(2)).real:+.8e}   [Dirac index = half vector index at 2nd order]")
        P(f"          sig2+ = {sgp(2).real:+.6e}, sig2- = {sgm(2).real:+.6e}  (differ: self-dual / anti-self-dual parts)")
        P(f"   so(6): v2K = {vK(2).real:+.8e} ; tau2+ + tau2- = {(tp(2)+tm(2)).real:+.8e} ; tau2+ - tau2- = {abs(tp(2)-tm(2)):.1e} (expected 0, conjugate reps)")
        P(f"          tau3+ = {tp(3).real:+.6e}{tp(3).imag:+.1e}i, tau3- = {tm(3).real:+.6e}{tm(3).imag:+.1e}i, sum = {(tp(3)+tm(3)).real:+.6e} vs v3K = {vK(3).real:+.6e} (equal: structure-constant part; the d-symbol part flips sign between 4 and 4bar)")
        pred23 = -0.5 * (sgp(2) * tp(3) + sgm(2) * tm(3))
        P(f"   c_23 = {c(2,3).real:+.6e}{c(2,3).imag:+.1e}i ; -(1/2)(sig2+ tau3+ + sig2- tau3-) = {pred23.real:+.6e}{pred23.imag:+.1e}i  (parity-odd mixed term; with tau3-=-tau3+ it is -(1/2)(sig2+-sig2-)tau3+)")
        pred22b = -0.5 * (sgp(2) * tp(2) + sgm(2) * tm(2))
        P(f"   c_22 via spinor blocks: {pred22b.real:+.10e}  (= -(1/4) v2K (sig2+ + sig2-))")
    else:
        s8, t2 = sp[('M', '8')], sp[('K', '2')]
        P(f"   so(7): v2M = {vM(2).real:+.8e} ; sig2(8) = {s8(2).real:+.8e}   [T(8) = T(7)]")
        P(f"   so(3): v2K = {vK(2).real:+.8e} ; 4 tau2(2) = {4*t2(2).real:+.8e}   [T(3) = 4 T(2)]")
        P(f"   c_22 via spinor blocks: {(-0.5*s8(2)*t2(2)).real:+.10e}")


P("")
P("=== (C) positivity of the spinor index part tau^K(s) = Tr tr e^{-s(h+Sig.k)} - dim * Tr e^{-s h} (Peierls-Bogoliubov) ===")
for dM in (4, 7):
    blocks = mk_spinor_blocks(dM)
    mins = []
    for trial in range(20):
        hM, hK, f, k = setup(dM)
        for s in (0.05, 0.3, 1.0, 3.0):
            s0K = tr_exp(hK, s)
            tot = 0
            for cname, (SG, B) in blocks['K'].items():
                dim = B.shape[1] if B is not None else SG[(0, 1)].shape[0]
                tot += (block_tr(s, hK, k, SG, dim, 1.0, B) - dim * s0K).real
            mins.append(tot / s0K.real)
    P(f"dM = {dM}: min over 20 random K data and s in (0.05,0.3,1,3) of tau^K/s0^K = {min(mins):.3e} (>= 0 expected)")
P("")
P("ALL CHECKS PRINTED; compare residuals with 0 (machine precision ~1e-12 relative for (A), ~1e-10 for (B)).")
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
