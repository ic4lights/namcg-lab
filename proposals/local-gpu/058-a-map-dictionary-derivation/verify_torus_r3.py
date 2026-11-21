import numpy as np

# Script 6 (round 3): torus statements as worded in the r3 insertion.
#  (1) Remainder bound with the clock matrix rebuilt for each theta = 2 pi p/N
#      (script 2 varied theta only in the Weyl phase and kept U at p=1, so its
#      scaling table does not realise U V = e^{i theta} V U for p>1).
#  (2) Pairing: Tr W_v W_w = N delta_{v+w,0} for |m|,|n| <= M, 2M < N; without a
#      mode limit there are aliasing terms v+w = 0 mod N, v+w != 0, with
#      |Tr W_v W_w| = N.
#  (3) The bound uses |2 sin(x/2) - x| <= |x|^3/24.

rng = np.random.default_rng(11)
N = 60
V = np.roll(np.eye(N, dtype=complex), 1, axis=0)


def mats(p):
    th = 2 * np.pi * p / N
    U = np.diag(np.exp(1j * th * np.arange(N)))
    assert np.allclose(U @ V, np.exp(1j * th) * V @ U)

    def W(m, n):
        return np.exp(-1j * (th / 2) * m * n) * (np.linalg.matrix_power(U, m) @ np.linalg.matrix_power(V, n))
    return th, W


M = 5
assert 2 * M < N
modes = [(m, n) for m in range(-M, M + 1) for n in range(-M, M + 1)]
ok1 = True
print("(1) remainder bound, theta = 2 pi p / N, U rebuilt for each p:")
for p in (1, 2, 3, 4):
    th, W = mats(p)
    err = 0.0
    for _ in range(40):
        m, n, mp, nq = rng.integers(-M, M + 1, size=4)
        s = m * nq - n * mp
        lhs = W(m, n) @ W(mp, nq) - W(mp, nq) @ W(m, n)
        err = max(err, np.linalg.norm(lhs - 2j * np.sin(th * s / 2) * W(m + mp, n + nq), 2))
    F = {v: rng.normal() for v in modes}
    G = {v: rng.normal() for v in modes}
    Wf = sum(c * W(*v) for v, c in F.items())
    Wg = sum(c * W(*v) for v, c in G.items())
    P = np.zeros((N, N), dtype=complex)
    bnd = 0.0
    for v, c in F.items():
        for u, d in G.items():
            s = v[0] * u[1] - v[1] * u[0]
            P += c * d * th * s * W(v[0] + u[0], v[1] + u[1])
            bnd += abs(c) * abs(d) * (th * abs(s)) ** 3 / 24
    R = (Wf @ Wg - Wg @ Wf) / 1j - P
    nR = np.linalg.norm(R, 2)
    ok = err < 1e-9 and nR <= bnd
    ok1 = ok1 and ok
    print("  p=%d theta=%.5f product-law err=%.1e ||R||=%.4e bound=%.4e ok=%s" % (p, th, err, nR, bnd, ok))

th, W = mats(1)
ok2a = all(abs(np.trace(W(*v) @ W(*u)) - (N if (v[0] + u[0], v[1] + u[1]) == (0, 0) else 0)) < 1e-8
           for v in modes for u in modes)
print("\n(2a) Tr W_v W_w = N delta_{v+w,0} for all modes with |m|,|n|<=M, 2M<N:", ok2a)
alias = abs(np.trace(W(N // 2, 0) @ W(N // 2, 0)))
alias2 = abs(np.trace(W(3, N - 2) @ W(-3, 2)))
print("(2b) without a mode limit: |Tr W_(N/2,0) W_(N/2,0)| =", round(alias, 8),
      "; |Tr W_(3,N-2) W_(-3,2)| =", round(alias2, 8), "(aliasing, both = N)")
ok2b = abs(alias - N) < 1e-8 and abs(alias2 - N) < 1e-8

x = np.linspace(-20, 20, 200001)
ok3 = np.all(np.abs(2 * np.sin(x / 2) - x) <= np.abs(x) ** 3 / 24 + 1e-12)
print("(3) |2 sin(x/2) - x| <= |x|^3/24 on [-20,20]:", bool(ok3))
print("\nALL CHECKS:", bool(ok1 and ok2a and ok2b and ok3))
