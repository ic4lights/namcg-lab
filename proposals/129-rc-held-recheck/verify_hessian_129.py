# verify_hessian_129.py -- item 129, held block 48 paragraph 1 (F-area cubic branch).
# Run:  python -I proposals/129-rc-held-recheck/verify_hessian_129.py
# Expected invariant output: last line  HESSIAN_129 PASS  with all residuals < 1e-8.
#
# Model of the held claim:
#   S(X) = -(1/4) tr [X^i,X^j][X^i,X^j] + (i c/3) eps_ijk tr X^i X^j X^k,  X = chi J,
#   J^i Hermitian spin-(N-1)/2 generators, [J^i,J^j] = i eps^{ijk} J^k.
#   V(chi) = a4 chi^4 + a3 c chi^3 =: abar (chi^4 - (2/3) c3 chi^3)
#     => c3/chi = -(3/2) (a3 c)/(a4 chi),   kappa3 = 2 - c3/chi.
# Tests:
#  (1) GAUGE-FREE SHIFT IDENTITY: the difference of the (unfixed) quadratic operators
#      2(G(c) - G(0)) = (c3/chi) chi^2 * SO,  SO_{ij} = -eps_{kij} i ad_{J^k}  (real on the
#      Hermitian basis), i.e. the cubic term changes only the spin-orbit coefficient,
#      2 S.L -> kappa3 S.L.  Residual < 1e-8 for N=2..5, several c.
#  (2) SO spectrum on the su(N) content = { l^(2l+3), (-1)^(2l+1), (-(l+1))^(2l-1) },
#      l=1..N-1, plus 3 trace zero modes (quantum S.L eigenvalues).
#  (3) Branch bookkeeping (integer arithmetic): branches of chi^2(L^2 - kappa3 SO) over
#      l=1..N-1; no negative mode iff -1 <= kappa3 <= 2; kappa3=-2 has mode -2 chi^2;
#      kappa3=2 gives l(l-1), l(l+1)+2, (l+1)(l+2)  (the appH L3194 anchor spectrum).
#  (4) Multiplicities sum to 3(N^2-1).
# NOTE: the full gauge-fixed identity H = chi^2(L^2 - kappa3 SO) additionally needs the c=0
# anchor, which is OUR integrated statement at appH L3194 (flux operator, Lambda^i = J^i);
# a flux-free numeric Hessian has a different kernel structure and is NOT a valid test of it.
import numpy as np

EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
       (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}

def spin_mats(N):
    j = (N - 1) / 2.0
    Jz = np.diag([j - m for m in range(N)]).astype(complex)
    Jp = np.zeros((N, N), dtype=complex)
    for m in range(N - 1):
        mm = j - m
        Jp[m, m + 1] = np.sqrt(j * (j + 1) - mm * (mm - 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, Jz]

def onb(N):
    B = []
    for a in range(N):
        E = np.zeros((N, N), dtype=complex); E[a, a] = 1.0; B.append(E)
    for a in range(N):
        for b in range(a + 1, N):
            E = np.zeros((N, N), dtype=complex); E[a, b] = E[b, a] = 1 / np.sqrt(2); B.append(E)
            E = np.zeros((N, N), dtype=complex); E[a, b] = 1j / np.sqrt(2); E[b, a] = -1j / np.sqrt(2); B.append(E)
    return B

def S_action(X, c):
    t = 0j
    for i in range(3):
        for j in range(3):
            C = X[i] @ X[j] - X[j] @ X[i]
            t -= 0.25 * np.trace(C @ C)
    for (i, j, k), s in EPS.items():
        t += 1j * c * s * np.trace(X[i] @ X[j] @ X[k]) / 3.0
    return float(np.real(t))

def quad_part(X0, A, c):
    # exact quadratic part of t -> S(X0 + tA) (even-part extraction, exact for quartic polynomials)
    E = lambda t: (S_action([X0[i] + t * A[i] for i in range(3)], c)
                   + S_action([X0[i] - t * A[i] for i in range(3)], c))
    return (16 * E(1.0) - E(2.0) - 15 * E(0.0)) / 24.0

def build(chi, c, N):
    J = spin_mats(N)
    X0 = [chi * J[i] for i in range(3)]
    B = onb(N); nb = len(B); n = 3 * nb
    def Q(A):
        return quad_part(X0, A, c)
    def bvec(p):
        i, m = divmod(p, nb)
        A = [np.zeros((N, N), dtype=complex) for _ in range(3)]; A[i] = B[m]
        return A
    G = np.zeros((n, n))
    for p in range(n):
        for q in range(p, n):
            Ap, Aq = bvec(p), bvec(q)
            v = (Q([Ap[i] + Aq[i] for i in range(3)]) - Q(Ap) - Q(Aq)) / 2.0
            G[p, q] = G[q, p] = v
    a4 = S_action([J[i] for i in range(3)], 0.0)
    a3 = S_action([J[i] for i in range(3)], 1.0) - a4
    return G, J, B, a4, a3

def so_matrix(J, N, B):
    """SO: (SO A)^i = -eps_{kij} i [J^k, A^j]  (real symmetric on the Hermitian basis)."""
    nb = len(B); n = 3 * nb
    M = np.zeros((n, n))
    def apply(A):
        Y = [np.zeros((N, N), dtype=complex) for _ in range(3)]
        for i in range(3):
            t = np.zeros((N, N), dtype=complex)
            for k in range(3):
                for j in range(3):
                    s = EPS.get((k, i, j), 0)
                    if s:
                        t += s * 1j * (J[k] @ A[j] - A[j] @ J[k])
            Y[i] = -t
        return Y
    for p in range(n):
        i1, m1 = divmod(p, nb)
        A = [np.zeros((N, N), dtype=complex) for _ in range(3)]; A[i1] = B[m1]
        Y = apply(A)
        for q in range(n):
            i2, m2 = divmod(q, nb)
            M[q, p] = M[p, q] = float(np.real(np.trace(Y[i2] @ B[m2])))
    return M

def main():
    # ---- convention: a3/a4 of the CS term against the quartic
    G0, J, B, a4, a3 = build(1.0, 0.0, 3)
    print(f"convention: a3/a4 = {a3/a4:+.6f} (expect -2/3), kappa3(c=+1,chi=1) = {2+1.5*a3/a4:+.6f} (expect +1)")

    # ---- (1) gauge-free shift identity
    worst = 0.0
    for (N, chi, c) in [(2, 1.0, 1.0), (3, 1.0, 1.0), (3, 1.0, -2.0), (4, 1.0, 2.0/3.0),
                        (4, 2.0, 2.0), (5, 1.0, -0.5), (5, 1.0, 1.5)]:
        Gc, J, B, a4, a3 = build(chi, c, N)
        G0, _, _, _, _ = build(chi, 0.0, N)
        c3 = -1.5 * a3 * c / a4           # V = a4 chi^4 + a3 c chi^3 = a4(chi^4 - (2/3)c3 chi^3)
        SO = so_matrix(J, N, B)
        D = 2.0 * (Gc - G0)
        r = float(np.max(np.abs(D - (c3 / chi) * chi * chi * SO)))
        worst = max(worst, r)
        print(f"N={N} chi={chi} c={c:+.3f}: c3/chi={c3/chi:+.6f} shift-residual={r:.3e}")
    assert worst < 1e-8, worst

    # ---- (2) SO spectrum multiset
    for N in [2, 3, 4]:
        _, J, B, _, _ = build(1.0, 0.0, N)
        SO = so_matrix(J, N, B)
        ev = np.sort(np.linalg.eigvalsh(SO))
        want = [0.0, 0.0, 0.0]
        for l in range(1, N):
            want += [float(l)] * (2 * l + 3) + [-1.0] * (2 * l + 1) + [-(l + 1.0)] * (2 * l - 1)
        assert len(ev) == len(want)
        r = float(np.max(np.abs(ev - np.sort(np.array(want)))))
        assert r < 1e-8, (N, r)
        print(f"N={N}: SO spectrum = {{l, -1, -(l+1)}} over l=1..{N-1} + 3 trace zeros (res {r:.1e})")

    # ---- (3) branch bookkeeping and no-negative-mode window (exact integer/rational arithmetic)
    def branches(k3):
        out = []
        for l in range(1, 12):
            out += [(l * (l + 1) - k3 * l, 2 * l + 3), (l * (l + 1) + k3, 2 * l + 1),
                    (l * (l + 1) + k3 * (l + 1), 2 * l - 1)]
        return out
    def min_branch(k3):
        return min(v for v, m in branches(k3))
    from fractions import Fraction
    for k3 in [-1.25, -1.0, -0.5, 0.0, 1.0, 2.0, 2.25, -1.0000001, 2.0000001]:
        ok = min_branch(k3) >= -1e-12
        want = (-1.0 - 1e-12) <= k3 <= (2.0 + 1e-12)
        assert ok == want, (k3, min_branch(k3), ok, want)
    print("no-negative-mode iff -1 <= kappa3 <= 2: OK (binding modes j=l-1 at l=1 for -1, j=l+1 at l=1 for 2)")
    assert min_branch(-2.0) == -2.0
    print(f"kappa3=-2: minimum branch = {min_branch(-2.0):+.3f} chi^2  (l=1, j=l-1=0 mode)")
    # kappa3=2 anchor = appH L3194 c3=0 spectrum values
    for l in range(1, 12):
        vals = {l * (l + 1) - 2 * l, l * (l + 1) + 2, l * (l + 1) + 2 * (l + 1)}
        assert vals == {l * (l - 1), l * (l + 1) + 2, (l + 1) * (l + 2)}
    print("kappa3=2 branch values = l(l-1), l(l+1)+2, (l+1)(l+2): matches appH L3194 anchor")

    # ---- (4) multiplicities
    for N in range(2, 8):
        s = (2 * 1 + 3) * 0
        s = sum((2 * l + 3) + (2 * l + 1) + (2 * l - 1) for l in range(1, N))
        assert s == 3 * (N * N - 1), (N, s)
    print("multiplicity sum = 3(N^2-1): OK for N=2..7 (adjoint content only, no l=0)")

    print("HESSIAN_129 PASS")

main()
