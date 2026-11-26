#!/usr/bin/env python3
"""s1: exact mixed-multiplicity spectrum of block-equalized coincident copies.
(A) symbolic: det(lam^2 I + 4 lam H - 4 K) == prod_f (lam^2+4 lam h_f - 4 n_f)^q_f
    at block-scalar (H,K), and the same for the pencil det(lam I - T) (078 identity).
(B) numeric: explicit realizable edge-row blocks R, U = 1_q (x) u; full charge
    Q~ = -2i(UR^+ - RU^+) (qN x qN, rank 2q), nonzero spectra vs the pair formula,
    per-factor involution lam -> -4 n_f / lam. Deterministic seed; verdicts only.
"""
import numpy as np, sympy as sp
rng = np.random.default_rng(20261117)
lam = sp.symbols('lam')

def pencil_det(C0, Z0, q):
    I = sp.eye(q)
    T = -2*sp.I*sp.Matrix(sp.BlockMatrix([[C0.adjoint(), Z0], [-I, -C0]]))
    return sp.expand((lam*sp.eye(2*q) - T).det())

def blk(hs, ns, qs):
    H = sp.diag(*sum([[hs[f]]*qs[f] for f in range(len(qs))], []))
    K = sp.diag(*sum([[ns[f]]*qs[f] for f in range(len(qs))], []))
    return H, K

# ---- (A) symbolic: q=2 partitions (1,1),(2); q=3 partition (2,1) ----
sym_ok = []
for qs, tag in [((1,1),'q2_1_1'), ((2,),'q2_2'), ((2,1),'q3_2_1')]:
    q = sum(qs)
    hs = [sp.symbols('h%d'%f, real=True) for f in range(len(qs))]
    ns = [sp.symbols('n%d'%f, real=True) for f in range(len(qs))]
    A = sp.Matrix([[sp.symbols('ar%d%d'%(min(r,c),max(r,c)), real=True)
                    for c in range(q)] for r in range(q)])
    H, K = blk(hs, ns, qs)
    C0 = A + sp.I*H
    Z0 = K + C0.adjoint()*C0
    prod = sp.expand(sp.prod([(lam**2 + 4*lam*hs[f] - 4*ns[f])**qs[f] for f in range(len(qs))]))
    e_quad = sp.expand((lam**2*sp.eye(q) + 4*lam*H - 4*K).det())
    e_pen = pencil_det(C0, Z0, q)
    sym_ok.append((tag, sp.expand(e_quad - prod) == 0, sp.expand(e_pen - prod) == 0))
print('A symbolic block-scalar factorizations (tag, quad==prod, pencil==prod):')
for r in sym_ok: print('  ', r)

# ---- (B) numeric: explicit realizable data R, U=1_q (x) u; full charge spectra ----
def realizable(qs, N, rng):
    q = sum(qs)
    u = rng.standard_normal(N) + 1j*rng.standard_normal(N); u /= np.linalg.norm(u)
    U = np.kron(np.eye(q), u[:, None])                       # qN x q isometry
    W = rng.standard_normal((q*N, 2*q)) + 1j*rng.standard_normal((q*N, 2*q))
    Qh, _ = np.linalg.qr(W)
    V = Qh[:, :q]
    V = V - U @ (U.conj().T @ V)                             # orthogonalise vs col(U)
    Vt, _ = np.linalg.qr(V)
    V = Vt[:, :q]                                            # qN x q isometry, U^+ V = 0
    hs = rng.standard_normal(len(qs)); ns = 0.5 + rng.random(len(qs))
    H = np.diag(np.repeat(hs, qs)); K = np.diag(np.repeat(ns, qs))
    A = rng.standard_normal((q, q)) + 1j*rng.standard_normal((q, q)); A = (A + A.conj().T)/2
    C0 = A + 1j*H                                            # Im C0 = H block-scalar
    R = U @ C0 + V * np.sqrt(np.repeat(ns, qs))                    # R^+(I-UU^+)R = K, U^+R = C0
    return U, R, hs, ns, q

worst = 0.0; worst_inv = 0.0; cases = 0; rank_ok = True
for qs in [(1,1),(2,),(2,1),(3,),(2,2),(3,1),(4,1),(3,2)]:
    q = sum(qs)
    for N in [2, 3, 5, 8]:
        for rep in range(3):
            U, R, hs, ns, q = realizable(qs, N, rng)
            Qt = -2j*(U @ R.conj().T - R @ U.conj().T); Qt = (Qt + Qt.conj().T)/2
            ev = np.linalg.eigvalsh(Qt)
            nz = ev[np.abs(ev) > 1e-7]
            if nz.size != 2*q: rank_ok = False
            pairs = np.sort(np.concatenate([np.array([-2*h+2*np.sqrt(h*h+n), -2*h-2*np.sqrt(h*h+n)])
                                            for h, n in zip(np.repeat(hs, qs), np.repeat(ns, qs))]))
            worst = max(worst, np.max(np.abs(np.sort(nz) - pairs)))
            inv = []
            for h, n in zip(np.repeat(hs, qs), np.repeat(ns, qs)):
                inv += [-4*n/(-2*h+2*np.sqrt(h*h+n)), -4*n/(-2*h-2*np.sqrt(h*h+n))]
            worst_inv = max(worst_inv, np.max(np.abs(np.sort(np.array(inv)) - np.sort(nz))))
            cases += 1
print('B cases=%d worst-spectrum-dev=%.3e worst-involution-dev=%.3e rank2q_ok=%s'
      % (cases, worst, worst_inv, rank_ok))
