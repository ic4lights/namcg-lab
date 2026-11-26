# s3_generalD_checks.py -- proposal 103, general-D checks.
#  (A) symbolic re-derivation of the 089 closed-form product pushforward from the ray formula
#      f(p) = int_0^oo tau^{D-1} g(tau p) dtau at diagonal covariance, D=2 and D=3;
#  (B) D=3 equicorrelated slots Sigma = [[1,t,t],[t,1,t],[t,t,1]]: exact Wick moment
#      E[E1 E2 E3] = 1 + 3 t^2 + 2 t^3 (permanent/contingency form) vs Monte Carlo;
#  (C) D=3 profile statistics under equicorrelated slots, t in {0, 1/2}: MC estimates of
#      E[s2], E[s2^2], E[rho_2]=1+E[s2] against the flat-Dirichlet closed values of the
#      flat-Dirichlet statistics paragraph (t=0 check: 1/2, 4/15, 3/2) and the direction of
#      the shift for t=1/2 (attraction toward the uniformity locus).
# Run from repo root: python -I proposals/103-g-moments-nonproduct-measures/s3_generalD_checks.py
import numpy as np
import sympy as sp

print("=== (A) ray formula recovers the 089 closed form at diagonal Sigma ===")
p1, p2, p3, tau, s1, s2, s3v = sp.symbols("p1 p2 p3 tau s1 s2 s3", positive=True)
for D, ps, ss in [(2, (p1, p2), (s1, s2)), (3, (p1, p2, p3), (s1, s2, s3v))]:
    g = sp.prod(sp.exp(-tau * pv / sv) / sv for pv, sv in zip(ps, ss))
    ray = sp.integrate(tau ** (D - 1) * g, (tau, 0, sp.oo))
    ray = sp.simplify(ray)
    G = sp.prod(ss)
    Lam = sum(pv / sv for pv, sv in zip(ps, ss))
    target = sp.factorial(D - 1) / (G * Lam**D)
    print("D=%d: ray integral = %s" % (D, ray))
    print("D=%d: matches (D-1)!/(G (sum p_i/g_i)^D):" % D, sp.simplify(ray - target) == 0)

print()
print("=== (B) exact D=3 equicorrelated Wick moment ===")
import itertools

def tables(rs, cs):
    if not rs:
        yield []
        return
    for row in itertools.product(range(rs[0] + 1), repeat=len(cs)):
        if sum(row) != rs[0] or any(row[j] > cs[j] for j in range(len(cs))):
            continue
        for rest in tables(rs[1:], [cs[j] - row[j] for j in range(len(cs))]):
            yield [list(row)] + rest

t = sp.symbols("t", positive=True)
Sig3 = sp.Matrix([[1, t, t], [t, 1, t], [t, t, 1]])
tot = sp.Integer(0)
for M in tables([1, 1, 1], [1, 1, 1]):
    term = sp.Integer(1)
    for i in range(3):
        for j in range(3):
            if M[i][j]:
                term *= Sig3[i, j]
    tot += term
closed = sp.expand(tot)
print("E[E1 E2 E3] exact =", closed, " (closed form 1+3t^2+2t^3 match:", sp.simplify(closed - (1 + 3 * t**2 + 2 * t**3)) == 0, ")")

rng = np.random.default_rng(1033)
n = 4_000_000

def sample_D(Sig_np, n, rng):
    L = np.linalg.cholesky(Sig_np)
    z = (rng.standard_normal((n, Sig_np.shape[0])) + 1j * rng.standard_normal((n, Sig_np.shape[0]))) / np.sqrt(2)
    W = z @ L.T
    return np.abs(W) ** 2

tv = 0.5
S3 = np.array([[1.0, tv, tv], [tv, 1.0, tv], [tv, tv, 1.0]])
E = sample_D(S3, n, rng)
mc = np.mean(E[:, 0] * E[:, 1] * E[:, 2])
ex = 1 + 3 * tv**2 + 2 * tv**3
print("t=0.5: exact %.6f MC %.6f reldev %.2e" % (ex, mc, abs(ex - mc) / ex))

print()
print("=== (C) D=3 profile statistics: equicorrelated vs flat Dirichlet ===")
for tv in [0.0, 0.5]:
    S = np.array([[1.0, tv, tv], [tv, 1.0, tv], [tv, tv, 1.0]])
    E = sample_D(S, n, rng)
    p = E / E.sum(1, keepdims=True)
    s2 = (p**2).sum(1)
    s2sq = np.mean(s2**2)
    print("t=%.1f: MC E[s2]=%.5f  E[rho_2]=1+E[s2]=%.5f  E[s2^2]=%.5f"
          % (tv, np.mean(s2), 1 + np.mean(s2), s2sq))
print("flat-Dirichlet closed values at D=3 (t=0 check, flat-Dirichlet statistics paragraph):"
      " E[s2]=2/(D+1)=%.5f, E[s2^2]=4(D+5)/((D+1)(D+2)(D+3))=%.5f, E[rho_2]=(D+3)/(D+1)=%.5f"
      % (2 / 4, 4 * 8 / (4 * 5 * 6), 6 / 4))
print("S3 DONE")
