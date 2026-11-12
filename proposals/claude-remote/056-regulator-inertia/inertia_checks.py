#!/usr/bin/env python3
"""Numerical checks for proposal 056 (regulator inertia of linear contours A = Lambda X).

Conventions: eta = diag(-1,1,...,1); h = Lambda^T eta Lambda; M = Lambda^T P Lambda with P the (real, positive
definite) regulator matrix; Definition (A) has P = I.  'Re h' is the real part of the complex symmetric h.

Checks
 A. Lemma (P = I): if Re M > 0 then Re h has inertia (9 positive, 1 negative), with the quantitative bounds
    lambda_2(Re h) >= lambda_1(Re M)   (Re h >= Re M - 2 a a^T, a = Re row_0(Lambda), Weyl interlacing)
    lambda_1(Re h) <= -v0^*(Re M)v0/|v0|^2 < 0,  v0 = Lambda^{-1} e_0.
    Random and adversarial (optimised) Lambda.
 B. The -C_0 example of the preceding paragraph, Lambda = diag(1, e^{2 pi i/3},...): Re M = diag(1,-1/2,...).
 C. Isotropic regulators (pencil eigenvalues -mu_0, mu x 9, e.g. boosted or time-rescaled): same inertia.
 D. Anisotropic regulators: 3x3 explicit example with Re M > 0 and two negative eigenvalues of Re h; 10x10
    search for Lambda with Re Lambda^T P Lambda > 0 and h in -C_0 (h = -diag(e^{i beta}), beta in K_0, T = I
    without loss of generality since real congruence preserves both conditions).
 E. Momenta with bounded modes on admissible contours (P = I): Re(k^T k) > 0, and an imaginary row 0 (needed
    for bounded modes at imaginary timelike momenta) forces Re h > 0, which A excludes.
 F. N = 2 scaling identities used in the non-integrability argument.
"""
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import expm

rng = np.random.default_rng(56001)
n = 10
eta = np.diag([-1.0] + [1.0] * 9)
out = []
pr = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))


def eigs(S):
    return np.linalg.eigvalsh((S + S.T) / 2)


def inertia(S, tol=1e-12):
    w = eigs(S)
    sc = max(1.0, np.max(np.abs(w)))
    return int(np.sum(w > tol * sc)), int(np.sum(w < -tol * sc)), int(np.sum(np.abs(w) <= tol * sc))


def class_of_phases(d):
    """0 for C_0, 1 for -C_0, None if (P) fails (diagonal h = diag(d))."""
    beta = np.angle(d)
    for c in np.linspace(-np.pi, np.pi, 7201):
        lift = (beta - c + np.pi) % (2 * np.pi) - np.pi
        if np.all(np.abs(lift) < np.pi / 2):
            b = lift + c
            break
    else:
        return None
    s = np.array([b[i] + b[j] for i in range(len(b)) for j in range(i + 1, len(b))])
    for k in range(-3, 4):
        if np.all((s - 2 * k * np.pi > 0) & (s - 2 * k * np.pi < np.pi)):
            return k % 2
    return None


def sample_L(r):
    """Generic complex Lambda = S D R0 (I + t Z): S complex Lorentz, D diagonal phases |phi| < pi/4,
    R0 real, Z complex; callers reject those that violate the regulator condition."""
    A = r.standard_normal((n, n)) + 1j * r.standard_normal((n, n)); A = (A - A.T) / 2
    S = expm(r.choice([0.0, 0.1, 0.3, 0.6]) * eta @ A)
    D = np.diag(np.exp(1j * r.uniform(-0.24, 0.24, n) * np.pi))
    R0 = r.standard_normal((n, n))
    t = r.choice([0.0, 0.1, 0.3, 0.6])
    Z = (r.standard_normal((n, n)) + 1j * r.standard_normal((n, n))) / np.sqrt(n)
    return S @ D @ R0 @ (np.eye(n) + t * Z)


# ---------------- A
pr("A. Lemma for the regulator of Definition (A) (P = I)")
cnt, worst2, worst1 = 0, np.inf, -np.inf
for trial in range(20000):
    L = sample_L(rng)
    M = L.T @ L
    lm = eigs(M.real)[0]
    if lm <= 0:
        continue
    cnt += 1
    h = L.T @ eta @ L
    w = eigs(h.real)
    a = L[0].real
    assert inertia(h.real) == (9, 1, 0)
    worst2 = min(worst2, (w[1] - lm) / np.linalg.norm(M))
    v0 = np.linalg.solve(L, np.eye(n)[0])
    bound = -np.real(v0.conj() @ M.real @ v0) / np.real(v0.conj() @ v0)
    worst1 = max(worst1, (w[0] - bound) / np.linalg.norm(M))
    assert np.allclose(h.real, M.real - 2 * np.outer(a, a) + 2 * np.outer(L[0].imag, L[0].imag))
pr(f"  random Lambda with Re M > 0: {cnt}; inertia of Re h always (9,1,0)")
pr(f"  min over samples of [lambda_2(Re h) - lambda_1(Re M)]/|M| = {worst2:.3e} (must be >= 0)")
pr(f"  max over samples of [lambda_1(Re h) - (-v0*ReM v0/|v0|^2)]/|M| = {worst1:.3e} (must be <= 0)")


def unpackL(x):
    return (x[:n * n] + 1j * x[n * n:]).reshape(n, n)


def adv_obj(x):
    L = unpackL(x)
    L = L / np.linalg.norm(L)
    M = L.T @ L
    h = L.T @ eta @ L
    lm = eigs(M.real)[0]
    w2 = eigs(h.real)[1]
    return w2 + 50 * max(0.0, 1e-3 - lm)   # push the second eigenvalue of Re h down while Re M > 0


best = np.inf
for trial in range(12):
    x0 = np.concatenate([rng.standard_normal(n * n), rng.uniform(0, 1.5) * rng.standard_normal(n * n)])
    res = minimize(adv_obj, x0, method='Nelder-Mead', options={'maxiter': 6000, 'xatol': 1e-9, 'fatol': 1e-12})
    res = minimize(adv_obj, res.x, method='Powell', options={'maxiter': 20000})
    L = unpackL(res.x); L = L / np.linalg.norm(L)
    M = L.T @ L; h = L.T @ eta @ L
    lm = eigs(M.real)[0]
    if lm > 0:
        best = min(best, eigs(h.real)[1] - lm)
pr(f"  adversarial search (12 starts): min [lambda_2(Re h) - lambda_1(Re M)] among admissible end points = {best:.3e}"
   " (must be >= 0)")

# ---------------- B
pr("B. The -C_0 example A_0 = X_0, A_i = e^{2 pi i/3} X_i")
L = np.diag([1.0] + [np.exp(2j * np.pi / 3)] * 9)
M = L.T @ L; h = L.T @ eta @ L
pr("  eigenvalues of Re M:", np.round(eigs(M.real), 6)[[0, -1]], " class of h:",
   {0: "C_0", 1: "-C_0", None: "outside C"}[class_of_phases(np.diag(h))], " inertia Re h:", inertia(h.real))

# ---------------- C
pr("C. Isotropic regulators: P = c L_b^T diag(mu0, mu,...,mu) L_b with L_b a real boost")
cntC = 0
for trial in range(4000):
    th = rng.uniform(-2, 2)
    Lb = np.eye(n); Lb[0, 0] = Lb[1, 1] = np.cosh(th); Lb[0, 1] = Lb[1, 0] = np.sinh(th)
    P = Lb.T @ np.diag([rng.uniform(0.2, 5)] + [1.0] * 9) @ Lb
    P = P * rng.uniform(0.3, 3)
    Pi = np.linalg.cholesky(P)                      # P = Pi Pi^T; Lambda = Pi^{-T} L' with L' sampled
    L = np.linalg.solve(Pi.T, sample_L(rng))
    M = L.T @ P @ L
    if eigs(M.real)[0] <= 0:
        continue
    cntC += 1
    assert inertia((L.T @ eta @ L).real) == (9, 1, 0)
pr(f"  admissible samples {cntC}; inertia of Re h always (9,1,0)")

# ---------------- D
pr("D. Anisotropic regulators")
mu = 4.0; al, be, ga = 1.0, 0.8, 1.0      # alpha^2 > beta^2, alpha^2 < mu beta^2
E3 = np.diag([-1.0, 1.0, mu])
L3 = np.array([[0, 0, ga], [al, 0, 0], [1j * be, 1, 0]])
M3 = L3.T @ L3; h3 = L3.T @ E3 @ L3
pr("  3x3, E = diag(-1,1,4) (P = I in these coordinates): eig Re M =", np.round(eigs(M3.real), 4),
   " eig Re h =", np.round(eigs(h3.real), 4))


def build(x, mus):
    """Lambda = S Lambda_0 with S^T E S = E, Lambda_0^T E Lambda_0 = -diag(d); returns Lambda, h, M (P = I)."""
    E = np.diag(np.concatenate([[-1.0], mus]))
    A = (x[:n * n] + 1j * x[n * n:2 * n * n]).reshape(n, n); A = (A - A.T) / 2
    S = expm(np.linalg.solve(E, A))
    beta = x[2 * n * n:2 * n * n + n]
    d = np.exp(1j * beta)
    sqE = np.sqrt(E.diagonal().astype(complex))
    L0 = np.diag(np.sqrt(-d) / sqE)
    Lm = S @ L0
    return Lm, Lm.T @ E @ Lm, Lm.T @ Lm, d


def K0_pen(beta):
    s = beta[:, None] + beta[None, :]
    off = ~np.eye(n, dtype=bool)
    return np.sum(np.maximum(0, 0.05 - s[off]) + np.maximum(0, s[off] - (np.pi - 0.05)))


def objD(x, mus):
    Lm, h, M, d = build(x, mus)
    nr = np.linalg.norm(M)
    return -eigs(M.real)[0] / nr + 10 * K0_pen(x[2 * n * n:])


for label, mus in (("isotropic mu = 1 (Definition (A))", np.ones(9)),
                   ("anisotropic mu = 1,...,1,25", np.array([1.0] * 8 + [25.0])),
                   ("anisotropic mu = 25^(j/8), j=0..8", 25.0 ** (np.arange(9) / 8))):
    bestv, bestx = -np.inf, None
    for trial in range(6):
        x0 = np.concatenate([0.7 * rng.standard_normal(2 * n * n), np.full(n, np.pi / 4) + 0.1 * rng.standard_normal(n)])
        res = minimize(objD, x0, args=(mus,), method='L-BFGS-B', options={'maxiter': 3000})
        v = -res.fun
        if v > bestv:
            bestv, bestx = v, res.x
    Lm, h, M, d = build(bestx, mus)
    cls = class_of_phases(-d)  # h = -diag(d) up to the complex Lorentz S (which does not change h)
    hd = -np.diag(d)
    pr(f"  {label}: best lambda_min(Re M)/|M| = {eigs(M.real)[0]/np.linalg.norm(M):+.4e}; h = -diag(d) exact to"
       f" {np.max(np.abs(h - hd)):.1e}; class of h = {({0:'C_0',1:'-C_0',None:'outside C'})[class_of_phases(np.diag(hd))]};"
       f" inertia Re h {inertia(h.real)}")
    if eigs(M.real)[0] > 0 and not label.startswith("isotropic"):
        np.save(__file__.replace('inertia_checks.py', 'anisotropic_example_%d.npy' % int(mus[0] == mus[1])),
                np.concatenate([bestx, mus]))

# 10x10 version in the original coordinates: P = diag(1,1,1/4,1,...,1), Lambda = P^{-1/2} blockdiag(L3, I_7)
P10 = np.diag([1.0, 1.0, 0.25] + [1.0] * 7)
L10 = np.diag(np.diag(P10) ** -0.5) @ np.block([[L3, np.zeros((3, 7))], [np.zeros((7, 3)), np.eye(7)]])
pr("  10x10, P = diag(1,1,1/4,1,...,1): eig Re(Lambda^T P Lambda) min =", np.round(eigs((L10.T @ P10 @ L10).real)[0], 4),
   "; inertia of Re(Lambda^T eta Lambda) =", inertia((L10.T @ eta @ L10).real))

# ---------------- G
pr("G. Mass term: combined quadratic matrix P_eff = eps I + i g eta (g = gamma/(2 g_YM^2))")
cntG, okG = 0, 0
for trial in range(20000):
    eps = rng.uniform(0.0, 1.0); gg = -rng.uniform(0.0, 3.0)
    if eps == 0 and gg == 0:
        continue
    Peff = eps * np.eye(n) + 1j * gg * eta
    L = sample_L(rng)
    # random complex phase rotations so that admissible samples with Im h of both signs occur
    L = np.diag(np.exp(1j * rng.uniform(-0.6, 0.6, n))) @ L
    Me = L.T @ Peff @ L
    if eigs(Me.real)[0] <= 0:
        continue
    cntG += 1
    h = L.T @ eta @ L
    a = L[0].real
    lhs = ((eps + 1j * gg) * h).real
    assert np.allclose((eps + 1j * gg) * h, Me - 2 * eps * np.outer(L[0], L[0]))
    if inertia(lhs)[1] <= 1:
        okG += 1
pr(f"  gamma <= 0: admissible samples {cntG}; identity (eps+ig)h = M_eff - 2 eps l l^T exact;"
   f" Re((eps+ig)h) has <= 1 negative eigenvalue in {okG}/{cntG}")
phi = -np.pi / 2 + np.pi / 2 * np.linspace(0, 1, 7)
worst = 10
for trial in range(300):
    while True:
        b = rng.uniform(-np.pi / 2, np.pi, n)
        sm = b[:, None] + b[None, :]
        if np.all((sm[~np.eye(n, dtype=bool)] > 0) & (sm[~np.eye(n, dtype=bool)] < np.pi)):
            break
    T = rng.standard_normal((n, n))
    h = -T.T @ np.diag(rng.uniform(0.3, 3, n) * np.exp(1j * b)) @ T
    for ph in phi:
        worst = min(worst, inertia((np.exp(1j * ph) * h).real)[1])
pr(f"  random h in -C_0 (300), phi in [-pi/2, 0]: min number of negative eigenvalues of Re(e^(i phi) h) = {worst}"
   " (claim >= 8)")
Lg = np.diag([np.exp(1j * np.pi / 8)] + [np.exp(-3j * np.pi / 8)] * 9)
hg = Lg.T @ eta @ Lg
for eps, gg in ((0.1, 0.2), (0.1, 0.05), (0.0, 0.3)):
    Me = Lg.T @ (eps * np.eye(n) + 1j * gg * eta) @ Lg
    pr(f"  gamma > 0 example A_0 = e^(i pi/8) X_0, A_i = e^(-3 pi i/8) X_i: h = -e^(i pi/4) I to"
       f" {np.max(np.abs(hg + np.exp(1j*np.pi/4)*np.eye(n))):.1e}; class {({0:'C_0',1:'-C_0',None:'outside C'})[class_of_phases(np.diag(hg))]};"
       f" eps={eps}, g={gg}: min eig Re M_eff = {eigs(Me.real)[0]:+.4f} (positive iff g > eps)")
# Euclidean damping on that contour: h^2 = i, so i S_b = i * i * S_E = -S_E
pr(f"  h_00 h_11 = {hg[0,0]*hg[1,1]:.3f}, h_11 h_22 = {hg[1,1]*hg[2,2]:.3f} (both i: Re iS_b = -S_E)")

# ---------------- E
pr("E. Momenta with bounded modes on admissible contours (P = I)")
cntE, worstE = 0, np.inf
for trial in range(20000):
    L = sample_L(rng)
    M = L.T @ L
    if eigs(M.real)[0] <= 0:
        continue
    q = rng.standard_normal(n)
    k = np.linalg.solve(L.T, q)
    cntE += 1
    worstE = min(worstE, np.real(k @ k) / (q @ q) * np.linalg.norm(M))
pr(f"  samples {cntE}: min Re(k^T k) * |M| / |q|^2 = {worstE:.3e} (must be > 0)")
def neg_lmin_imag_row0(x):
    L = (x[:n * n] + 1j * x[n * n:]).reshape(n, n)
    L[0] = 1j * L[0].imag
    M = L.T @ L
    return -eigs(M.real)[0] / np.linalg.norm(M)


bestI = -np.inf
for trial in range(8):
    L0 = sample_L(rng); L0[0] = 1j * rng.standard_normal(n)
    res = minimize(neg_lmin_imag_row0, np.concatenate([L0.real.ravel(), L0.imag.ravel()]), method='L-BFGS-B',
                   options={'maxiter': 3000})
    bestI = max(bestI, -res.fun)
L = sample_L(rng); L[0] = 1j * L[0].imag
assert np.allclose((L.T @ eta @ L).real, (L.T @ L).real + 2 * np.outer(L[0].imag, L[0].imag))
pr(f"  imaginary row 0: Re h = Re M + 2 b b^T (exact); max over 8 optimised starts of lambda_min(Re M)/|M| ="
   f" {bestI:+.3e} (must be <= 0)")

# ---------------- F
pr("F. N = 2 scaling used in the non-integrability argument")
h = np.diag(np.exp(1j * rng.uniform(-1, 1, n)))
Z = rng.standard_normal((n, 3))
for R, s in ((10.0, 0.1), (100.0, 0.01), (3.0, 0.5)):
    X = Z @ np.diag([R, s, s])
    G = X.T @ h @ X
    lhs = np.linalg.det(G); rhs = R ** 2 * s ** 4 * np.linalg.det(Z.T @ h @ Z)
    s2 = (np.trace(G) ** 2 - np.trace(G @ G)) / 2
    pr(f"  R={R}, s={s}: det G / (R^2 s^4 det Z^T h Z) = {lhs/rhs:.12f};  |sigma_2(G)| = {abs(s2):.4f}"
       f" (bounded when s = 1/R)")

open(__file__.replace('.py', '.txt'), 'w').write('\n'.join(out) + '\n')
