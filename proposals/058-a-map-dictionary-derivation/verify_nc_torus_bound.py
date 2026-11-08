import numpy as np

# Script 2: finite-N ('t Hooft / noncommutative torus) Weyl data with an
# EXACT per-order-in-Theta operator-norm bound. No unbounded operators, no
# cutoff removal subtleties: everything is a bounded N x N matrix, so the
# operator-norm statement is honest.
#
# Data: H_N = C^N, N even, p odd, theta = 2*pi*p/N. U = clock, V = shift:
#   U V = e^{i theta} V U.
# Symmetric (Weyl-ordered) symbol map on modes v=(m,n), |m|,|n| <= M:
#   W_hat(e_v) := e^{-i (theta/2) m n} U^m V^n  (unitary).
# Product law (verified numerically here, exact by construction):
#   [W_hat(e_v), W_hat(e_w)] = 2 i sin( (theta/2) sigma(v,w) ) W_hat(e_{v+w}),
#   sigma(v,w) = m n' - n m'.
# Classical limit: define Poisson bracket {e_v,e_w} = Theta12 * sigma(v,w) e_{v+w}
# with Theta12 := theta. Then the remainder of
#   (1/i)[W_hat(f), W_hat(g)] - W_hat({f,g})
# has, for modes with 2M < N (no wraparound), the EXACT operator-norm bound
#   ||R|| <= sum_{v,w} |fhat_v||ghat_w| * (theta |sigma|)^3 / 24,
# because |2 sin(x) - 2x| <= |x|^3/3 with x = (theta/2) sigma.
# Also verified: exact pairing Tr W_hat(f) W_hat(g) = N * sum_v fhat_v ghat_{-v}
# = N * (torus average of f g): the matrix pairing equals the continuum pairing
# with NO Theta-order corrections (rho = 1/|Pf theta| normalisation matches
# def:matrix-coords-ext).

N = 60
p = 1
theta = 2 * np.pi * p / N

w = np.exp(2j * np.pi / N)
U = np.diag(w ** np.arange(N))
V = np.roll(np.eye(N, dtype=complex), 1, axis=0)  # V e_j = e_{j+1}
assert np.allclose(U @ V, np.exp(1j * theta) * V @ U)

M = 5
assert 2 * M < N

def What(m, n):
    return np.exp(-1j * (theta / 2) * m * n) * (np.linalg.matrix_power(U, m) @ np.linalg.matrix_power(V, n))

# --- exact product law ---
maxerr = 0.0
rng = np.random.default_rng(7)
for _ in range(60):
    m, n, mp, np_ = rng.integers(-M, M + 1, size=4)
    sig = m * np_ - n * mp
    lhs = What(m, n) @ What(mp, np_) - What(mp, np_) @ What(m, n)
    rhs = 2j * np.sin(theta * sig / 2) * What(m + mp, n + np_)
    maxerr = max(maxerr, np.linalg.norm(lhs - rhs, 2))
print("product-law max operator-norm error (machine level):", maxerr)

# --- remainder bound and Theta^3 scaling ---
modes = [(m, n) for m in range(-M, M + 1) for n in range(-M, M + 1)]
def rand_symbol(scale=1.0):
    fh = {v: rng.normal() * scale for v in modes}
    return fh

def W_of(fh):
    A = np.zeros((N, N), dtype=complex)
    for (m, n), c in fh.items():
        A += c * What(m, n)
    return A

def poisson_symbol(fh, gh):  # coefficients of {f,g}, Theta12 = theta
    out = {}
    for v, c in fh.items():
        for u, d in gh.items():
            sig = v[0] * u[1] - v[1] * u[0]
            s = (v[0] + u[0], v[1] + u[1])
            if abs(s[0]) < N // 2 and abs(s[1]) < N // 2:
                out[s] = out.get(s, 0.0) + c * d * theta * sig
    return out

def sigma_bound(fh, gh, th):
    tot = 0.0
    for v, c in fh.items():
        for u, d in gh.items():
            sig = abs(v[0] * u[1] - v[1] * u[0])
            tot += abs(c) * abs(d) * (th * sig) ** 3 / 24.0
    return tot

print("\nscaling of ||R||_op vs theta (mode structure fixed):")
for pp in [1, 2, 3, 4]:
    th = 2 * np.pi * pp / N
    # recompute with this theta
    def What2(m, n, th=th):
        return np.exp(-1j * (th / 2) * m * n) * (np.linalg.matrix_power(U, m) @ np.linalg.matrix_power(V, n))
    F = {v: rng.normal() for v in modes}
    G = {v: rng.normal() for v in modes}
    Wf = sum(c * What2(*v) for v, c in F.items())
    Wg = sum(c * What2(*v) for v, c in G.items())
    Pois = 0
    for v, c in F.items():
        for u, d in G.items():
            sig = v[0] * u[1] - v[1] * u[0]
            s = (v[0] + u[0], v[1] + u[1])
            if abs(s[0]) < N // 2 and abs(s[1]) < N // 2:
                Pois += c * d * th * sig * What2(*s)
    R = (Wf @ Wg - Wg @ Wf) / 1j - Pois
    nR = np.linalg.norm(R, 2)
    bnd = sigma_bound(F, G, th)
    print(f"  theta={th:.5f}  ||R||={nR:.6e}  bound=(th^3/24)*sum={bnd:.6e}  ratio ||R||/th^3={nR/th**3:.4e}  bound ok: {nR <= bnd + 1e-12}")

# --- exact pairing identity ---
F = {v: rng.normal() + 1j * rng.normal() for v in modes}
G = {v: rng.normal() + 1j * rng.normal() for v in modes}
Wf = sum(c * What(*v) for v, c in F.items())
Wg = sum(c * What(*v) for v, c in G.items())
lhs = np.trace(Wf @ Wg)
rhs = N * sum(F[(m, n)] * G[(-m, -n)] for (m, n) in modes)
print("\nexact pairing Tr W(f)W(g) = N*sum fhat_v ghat_-v:")
print("  Tr =", lhs, "\n  RHS=", rhs, "\n  |diff| =", abs(lhs - rhs))

# continuum pairing of fg: N * mean(f g) with modes on 2pi torus:
# mean(f g) = sum_v fhat_v ghat_-v ; matches rho = 1/|Pf theta| scaling note.
print("\npairing exact (no Theta-order corrections):", abs(lhs - rhs) < 1e-10)

# Hermiticity: if f real symbol (ghat_-v = conj fhat_v), W_hat(f) Hermitian
Hf = {v: F[v] for v in modes}
# make a real symbol
R_ = {v: 0.0 for v in modes}
for (m, n) in modes:
    if (m, n) == (0, 0):
        R_[(0, 0)] = rng.normal()
    elif (m, n) > (0, 0) or ((m, n)[0] > 0):
        c = rng.normal() + 1j * rng.normal()
        R_[(m, n)] = c
        R_[(-m, -n)] = np.conj(c)
Wrealsym = sum(c * What(*v) for v, c in R_.items())
print("real symbol -> Hermitian operator:", np.allclose(Wrealsym, Wrealsym.conj().T))
