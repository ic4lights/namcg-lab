"""
Proposal 059, check 2 (numeric, numpy float64).

Fuzzy-sphere (Berezin-Toeplitz-type) finite-N matrix realization of the
derivation part of the first-order equivariant class and of the ghost
operator [X^a,[X_a,.]] of Appendix H (sec:status-D).

Data: spin j = (N-1)/2, N odd; J_i the spin-j matrices,
    [J_i,J_j] = i eps_ijk J_k exactly;
    X_i = J_i / sqrt(j(j+1))            (radius-1 fuzzy sphere),
    [X_i,X_j] = i hbar_eff eps_ijk X_k,   hbar_eff = 1/sqrt(j(j+1));
    derivations  L_a := (1/hbar_eff) ad_{X_a} = (1/hbar_eff)[X_a, .].

Checks:
 (1) L_a obey the Leibniz rule EXACTLY (inner derivations) and close the
     so(3) bracket exactly as superoperators, [L_i,L_j] = i eps_ijk L_k
     (machine precision): finite-N realization of the rotation-algebra
     action part of the class relations with NO error.
 (2) They act on the matrix coordinates exactly: L_i(X_j) = i eps_ijk X_k.
 (3) Moyal-vs-Poisson error for polynomial symbols is O(hbar_eff)
     (log-log slope ~ 1 over the N-range): the O(hbar_eff) error of the
     class relations when coefficient functions are moved through the
     noncommutative product at finite N.
 (4) The classical frame redundancy sum_i x_i rho_i = 0 is violated only
     at O(hbar_eff) (log-log slope ~ 1).
 (5) The ghost operator G = sum_i ad_{X_i}^2 (Euclidean contraction) on
     End(C^N) has spectrum EXACTLY { +l(l+1) hbar_eff^2, multiplicity
     2l+1, l = 0..N-1 }: G/hbar_eff^2 reproduces the Laplace-Beltrami
     spectrum +l(l+1) of the unit S^2 with no relative error at fixed l;
     the matrix truncation only removes the l > N-1 modes (full eigvalsh
     multiset comparison).

Run:  python -I d1_finiteN_class.py   (stdout; saved next to it)
"""
import numpy as np

def spin_matrices(j):
    m = np.arange(j, -j - 1.0, -1.0)
    Jz = np.diag(m)
    Jp = np.zeros((len(m), len(m)))
    for i in range(len(m) - 1):
        Jp[i, i + 1] = np.sqrt(j * (j + 1) - m[i + 1] * (m[i + 1] + 1))
    Jx = (Jp + Jp.conj().T) / 2.0
    Jy = (Jp - Jp.conj().T) / 2.0j
    return [np.array(Jx), np.array(Jy), np.array(Jz)]

def super_ad(A):
    # row-major vectorization (numpy reshape order):
    # vec(A f) = (A kron I) vec(f),  vec(f A) = (I kron A^T) vec(f)
    N = A.shape[0]
    I = np.eye(N)
    return np.kron(A, I) - np.kron(I, A.T)

def epsv(a, b, c):
    return np.linalg.det(np.eye(3)[[a, b, c]])

res = []
def rep(ok, name, extra=""):
    res.append(ok); print(f"{'PASS' if ok else 'FAIL'}  {name}  {extra}")

Ns = [5, 7, 9, 11, 13, 15, 17, 19, 21, 25, 31]
pts3, pts4 = [], []
for N in Ns:
    j = (N - 1) / 2.0
    J = spin_matrices(j)
    Jeff = np.sqrt(j * (j + 1))
    h = 1.0 / Jeff
    X = [Ji / Jeff for Ji in J]
    rng = np.random.default_rng(12345 + N)
    r1 = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    r2 = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    L = [super_ad(Xi) / h for Xi in X]

    def Lm(a, M):
        return (L[a] @ M.reshape(N * N)).reshape(N, N)
    leb = max(np.linalg.norm(Lm(a, r1 @ r2) - Lm(a, r1) @ r2 - r1 @ Lm(a, r2))
              for a in range(3))
    clo = 0.0
    for a in range(3):
        for b in range(3):
            s = np.zeros((N * N, N * N), complex)
            for c in range(3):
                s += 1j * epsv(a, b, c) * L[c]
            clo = max(clo, np.linalg.norm(L[a] @ L[b] - L[b] @ L[a] - s))
    rep(leb < 1e-10, f"N={N}: Leibniz rule exact (err {leb:.2e})")
    rep(clo < 1e-10, f"N={N}: [L_i,L_j] = i eps_ijk L_k exact (err {clo:.2e})")

    act = 0.0
    for a in range(3):
        for b in range(3):
            lhs = (X[a] @ X[b] - X[b] @ X[a]) / h
            rhs = np.zeros((N, N), complex)
            for c in range(3):
                rhs += 1j * epsv(a, b, c) * X[c]
            act = max(act, np.linalg.norm(lhs - rhs))
    rep(act < 1e-10, f"N={N}: L_i(X_j) = i eps_ijk X_k exact (err {act:.2e})")

    # (3) P = x1^2 x2, Q = x3 ; {x_i,x_j} = eps_ijk x_k
    #  {x1^2 x2, x3} = x1^2 {x2,x3} + {x1^2,x3} x2 = x1^3 + 2 x1 (-x2) x2 = x1^3 - 2 x1 x2^2
    P = X[0] @ X[0] @ X[1]
    Q = X[2]
    sym_x1x2sq = sum(P0 @ P1 @ P2 for P0, P1, P2 in
                     [(X[0], X[1], X[1]), (X[1], X[0], X[1]), (X[1], X[1], X[0])]) / 3.0
    cl = X[0] @ X[0] @ X[0] - 2.0 * sym_x1x2sq
    moy = (P @ Q - Q @ P) / (1j * h)
    E3 = np.linalg.norm(moy - cl) / np.linalg.norm(moy)
    pts3.append((np.log(N), np.log(E3)))

    # (4) redundancy operator R = sum_i (left-mult X_i) o L_i, on coordinate sector
    R = sum(np.kron(X[i], np.eye(N)) @ L[i] for i in range(3))
    rel = max(np.linalg.norm(R @ Xc.reshape(N * N)) for Xc in X) / max(np.linalg.norm(Xc) for Xc in X)
    pts4.append((np.log(N), np.log(rel)))
    print(f"info  N={N}: Moyal-vs-Poisson rel err {E3:.3e}; redundancy violation {rel:.3e}")

    # (5) ghost spectrum
    G = sum(super_ad(Xi) @ super_ad(Xi) for Xi in X)
    G = (G + G.conj().T) / 2
    ev = np.sort(np.linalg.eigvalsh(G)) / h**2
    exp = np.sort(np.concatenate([np.full(2 * l + 1, float(l * (l + 1)))
                                  for l in range(2 * int(round(j)) + 1)]))
    d = np.max(np.abs(ev - exp))
    rep(d < 1e-8, f"N={N}: ghost spectrum G/hbar^2 = +l(l+1) exactly (LB spectrum of S^2), l <= N-1 (max dev {d:.2e})")

def slope(pts):
    x = np.array([p[0] for p in pts]); y = np.array([p[1] for p in pts])
    return np.polyfit(x, y, 1)[0]

s3, s4 = slope(pts3), slope(pts4)
print()
rep(abs(s3 + 1.0) < 0.15, "check (3): log-log slope of Moyal-vs-Poisson error vs N is -1 (error ~ hbar_eff ~ 1/N)", f"slope = {s3:.3f}")
rep(abs(s4 + 1.0) < 0.15, "check (4): log-log slope of redundancy violation vs N is -1 (violation ~ hbar_eff)", f"slope = {s4:.3f}")
print()
print("ALL PASS" if all(res) else "SOME FAIL")
