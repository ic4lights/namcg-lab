#!/usr/bin/env python3
"""Numerical checks of the algebraic lemma on linear contours A = Lambda X (proposal 055).

h = Lambda^T eta^{-1} Lambda (complex symmetric n x n).  Condition (P):
    Im[h(a,a)h(b,b) - h(a,b)^2] > 0 for all linearly independent real a, b.
Lemma (n >= 3): (P) <=> h = T^T diag(d) T with T real invertible and phases beta of d such that, after a
common shift by k*pi, all pairwise sums beta_mu + beta_nu lie in (0, pi)  (class C_0 for k even, C_1 = -C_0 for
k odd).  For h in C_0 and real q != 0, arg(q^T h^{-1} q) lies in (-pi, pi/2).

Checks:
 A. random h in C_0 / C_1 built from the normal form: (P) by direct minimisation; theta in (0,pi/2) resp.
    (pi,3pi/2) with Re(e^{-i theta} h) > 0; args of q^T h^{-1} q for random real q.
 B. random general complex symmetric h near the Euclidean point and near eta^{-1}: decide (P) by direct
    minimisation and independently by the lemma's normal form; the two decisions must agree; for every h with
    (P), the class is determined and the cone of q^T h^{-1} q lies in the predicted sector.
 C. adversarial search: maximise the arg of q^T h^{-1} q over h satisfying (P) (penalty) and real q, starting
    from the per-index contours R_u; the supremum must not exceed pi in modulus... reported as the largest
    |arg + pi/4| - 3pi/4 found (must stay < 0 for C_0 starts).
 D. n = 2 counterexample: (P) holds but q^T h^{-1} q is negative real (shows n >= 3 is needed).
 E. per-index contours R_u: membership in C_0 exactly for 0 < u < 2.
 F. perturbations of eta^{-1} that satisfy (P) are all in C_0 (Re h keeps inertia (9,1)).
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20261107)
n = 10
eta = np.diag([-1.0] + [1.0] * 9)


def imdet_ratio(h, a, b):
    haa = a @ h @ a; hbb = b @ h @ b; hab = a @ h @ b
    w2 = (a @ a) * (b @ b) - (a @ b) ** 2
    return np.imag(haa * hbb - hab ** 2) / w2


def P_min(h, starts=40, seed=0):
    """min over 2-planes of Im det_h / |a^b|^2 by BFGS from random starts."""
    r = np.random.default_rng(seed)
    m = h.shape[0]
    best = np.inf
    f = lambda x: imdet_ratio(h, x[:m], x[m:])
    for _ in range(starts):
        x0 = r.standard_normal(2 * m)
        res = minimize(f, x0, method='BFGS', options={'gtol': 1e-10, 'maxiter': 2000})
        best = min(best, res.fun)
    # also all coordinate planes and planes spanned by eigenvectors of Re h, Im h
    for i in range(m):
        for j in range(i + 1, m):
            e = np.eye(m)
            best = min(best, imdet_ratio(h, e[i], e[j]))
    return best


def theta_set(h, ngrid=7200):
    """theta in [0,2pi) with Re(e^{-i theta}h) positive definite; returns (thetas, minimal eigenvalues)."""
    R, S = h.real, h.imag
    th = np.linspace(0, 2 * np.pi, ngrid, endpoint=False)
    mins = np.array([np.linalg.eigvalsh(np.cos(t) * R + np.sin(t) * S)[0] for t in th])
    return th[mins > 0], th, mins


def normal_form(h, theta):
    """h = T^T diag(d) T with T real, from P = Re(e^{-i theta}h) > 0."""
    P = (np.exp(-1j * theta) * h).real
    Q = (np.exp(-1j * theta) * h).imag
    w, V = np.linalg.eigh(P)
    Pm = V @ np.diag(w ** -0.5) @ V.T
    lam, U = np.linalg.eigh(Pm @ Q @ Pm)
    d = np.exp(1j * theta) * (1 + 1j * lam)
    T = U.T @ np.linalg.inv(Pm)
    return d, T


def class_of_phases(d):
    """Return k (0 or 1) such that after lifting into a semicircle and shifting by k*pi all pair sums are in
    (0,pi); None if (P) fails."""
    beta = np.angle(d)
    m = len(beta)
    # find a lift in an open semicircle: centre = argument of a direction with all |beta - c| < pi/2
    for c in np.linspace(-np.pi, np.pi, 3601):
        lift = (beta - c + np.pi) % (2 * np.pi) - np.pi
        if np.all(np.abs(lift) < np.pi / 2):
            b = lift + c
            break
    else:
        return None
    s = np.array([b[i] + b[j] for i in range(m) for j in range(i + 1, m)])
    for k in range(-3, 4):
        if np.all((s - 2 * k * np.pi > 0) & (s - 2 * k * np.pi < np.pi)):
            return k % 2
    return None


def random_K0(m, r):
    while True:
        b = r.uniform(-np.pi / 2, np.pi, m)
        s = b[:, None] + b[None, :]
        off = ~np.eye(m, dtype=bool)
        if np.all((s[off] > 0) & (s[off] < np.pi)):
            return b


def cone_args(h, nq=4000, r=rng):
    hinv = np.linalg.inv(h)
    q = r.standard_normal((nq, h.shape[0]))
    z = np.einsum('ij,jk,ik->i', q, hinv, q)
    return np.angle(z)


out = []
pr = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))

# ---------- A
pr("A. normal-form samples (n=10)")
worstP, worstarg0, worstarg1 = np.inf, -np.inf, -np.inf
for trial in range(30):
    b = random_K0(n, rng)
    T = rng.standard_normal((n, n))
    d = rng.uniform(0.3, 3.0, n) * np.exp(1j * b)
    h0 = T.T @ np.diag(d) @ T
    for k, h in ((0, h0), (1, -h0)):
        pm = P_min(h, starts=6, seed=trial)
        worstP = min(worstP, pm / np.linalg.norm(h) ** 2)
        ths, _, _ = theta_set(h, 1440)
        assert len(ths) > 0
        mid = np.angle(np.mean(np.exp(1j * ths))) % (2 * np.pi)
        if k == 0:
            assert 0 < mid < np.pi / 2, mid
            a = cone_args(h)
            worstarg0 = max(worstarg0, np.max(a), -np.min(a) - np.pi)  # need a < pi/2 and a > -pi
            assert np.all(a < np.pi / 2) and np.all(a > -np.pi)
        else:
            assert np.pi < mid < 3 * np.pi / 2, mid
            a = (cone_args(h)) % (2 * np.pi)  # predicted in (0, 3pi/2)
            assert np.all((a > 0) & (a < 3 * np.pi / 2))
pr("  (P) min ratio over samples (scaled, must be > 0):", f"{worstP:.3e}")
pr("  C_0: midpoint of the theta arc in (0,pi/2); C_1: in (pi,3pi/2); cone args inside predicted sectors: OK")

# ---------- B
pr("B. general complex symmetric h near the Euclidean point and near eta^{-1}: (P) by minimisation vs normal form")
agree, nP, n0, n1 = 0, 0, 0, 0
tot = 0
for trial in range(200):
    base = np.exp(1j * np.pi / 4) * np.eye(n) if trial % 2 == 0 else eta.astype(complex)
    E = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    E = (E + E.T) / 2
    scale = rng.choice([0.05, 0.15, 0.3, 0.6])
    h = base + scale * E
    pm = P_min(h, starts=8, seed=1000 + trial)
    passP = pm > 1e-9
    ths, th, mins = theta_set(h, 2880)
    lemmaP = False
    cls = None
    if len(ths) > 0:
        d, T = normal_form(h, ths[len(ths) // 2])
        assert np.allclose(T.T @ np.diag(d) @ T, h, atol=1e-8)
        cls = class_of_phases(d)
        lemmaP = cls is not None
    tot += 1
    if passP == lemmaP:
        agree += 1
    else:
        pr("   disagreement at trial", trial, "Pmin", pm, "theta-set size", len(ths), "class", cls)
    if passP:
        nP += 1
        if cls == 0:
            n0 += 1
            a = cone_args(h)
            assert np.all(a < np.pi / 2) and np.all(a > -np.pi)
        elif cls == 1:
            n1 += 1
pr(f"  trials {tot}; decisions agree {agree}; (P) holds in {nP} (class C_0: {n0}, C_1: {n1})")

# ---------- C
pr("C. adversarial: push arg(q^T h^{-1} q) out of the sector, starting in C_0, (P) enforced by penalty;")
pr("   h normalised to Frobenius norm sqrt(n); final candidates re-tested by minimisation (ratio > 1e-6, cond < 1e6)")
def unpack(x):
    hr = x[:n * n].reshape(n, n); hi = x[n * n:2 * n * n].reshape(n, n)
    h = (hr + hr.T) / 2 + 1j * (hi + hi.T) / 2
    h = h * np.sqrt(n) / np.linalg.norm(h)
    q = x[2 * n * n:]
    return h, q
best_excess = -np.inf
counted = 0
for trial in range(8):
    u = rng.uniform(0.05, 1.95)
    h0 = np.diag([np.exp(1j * (np.pi - 3 * np.pi * u / 4))] + [np.exp(1j * np.pi * u / 4)] * 9)
    q0 = rng.standard_normal(n)
    x0 = np.concatenate([h0.real.ravel(), h0.imag.ravel(), q0])
    pts = [rng.standard_normal((2, n)) for _ in range(150)]
    E = np.eye(n)
    def obj(x):
        h, q = unpack(x)
        if np.linalg.cond(h) > 1e6:
            return 10.0
        z = q @ np.linalg.solve(h, q)
        a = np.angle(z * np.exp(1j * np.pi / 4))
        pen = 0.0
        for (aa, bb) in pts:
            pen += max(0.0, 1e-3 - imdet_ratio(h, aa, bb)) ** 2
        for i in range(n):
            for j in range(i + 1, n):
                pen += max(0.0, 1e-3 - imdet_ratio(h, E[i], E[j])) ** 2
        return -abs(a) + 1e4 * pen
    res = minimize(obj, x0, method='Powell', options={'maxiter': 6000, 'xtol': 1e-6, 'ftol': 1e-10})
    h, q = unpack(res.x)
    pm = P_min(h, starts=20, seed=trial)
    z = q @ np.linalg.solve(h, q)
    a = np.angle(z * np.exp(1j * np.pi / 4))
    excess = abs(a) - 3 * np.pi / 4
    cond = np.linalg.cond(h)
    if pm > 1e-6 and cond < 1e6:
        counted += 1
        ths, _, _ = theta_set(h, 7200)
        cls = class_of_phases(normal_form(h, ths[len(ths) // 2])[0]) if len(ths) else None
        best_excess = max(best_excess, excess)
        pr(f"   start u={u:.3f}: Pmin ratio={pm:.2e}, cond={cond:.1e}, class {cls}, |arg(z e^(i pi/4))| - 3pi/4 = {excess:.3e}")
    else:
        pr(f"   start u={u:.3f}: final point fails the re-test (Pmin ratio={pm:.2e}, cond={cond:.1e}); not counted")
pr(f"  counted {counted}; largest excess with (P) holding (lemma predicts < 0):", f"{best_excess:.3e}")

# ---------- D
pr("D. n = 2: (P) does not exclude the forbidden quadrant")
h2 = np.diag([np.exp(1j * (np.pi / 4 + 0.9 * np.pi)), np.exp(1j * (np.pi / 4 - 0.85 * np.pi))])
pm2 = P_min(h2, starts=20)
z2 = np.array([1.0, 1.0]) @ np.linalg.inv(h2) @ np.array([1.0, 1.0])
pr(f"  Im det h = {np.imag(np.linalg.det(h2)):.4f} > 0 (P min {pm2:.4f}); q=(1,1): q^T h^-1 q = {z2:.4f}, arg/pi = {np.angle(z2)/np.pi:.4f}")

# ---------- E
pr("E. R_u: h = diag(-e^{-3 pi i u/4}, e^{pi i u/4} x9)")
for u in [0.0, 0.01, 0.5, 1.0, 1.5, 1.99, 2.0, 2.01, 2.5]:
    d = np.array([-np.exp(-3j * np.pi * u / 4)] + [np.exp(1j * np.pi * u / 4)] * 9)
    m = min(np.imag(d[i] * d[j]) for i in range(n) for j in range(i + 1, n))
    pr(f"  u={u:5.2f}: min_{{mu<nu}} Im(d_mu d_nu) = {m:+.4f}   class {class_of_phases(d) if m > 0 else None}")

# ---------- F
pr("F. perturbations of R_u, u in (0.02,0.3) (near eta^{-1}), satisfying (P)")
cnt, c0 = 0, 0
for trial in range(400):
    E = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n)); E = (E + E.T) / 2
    u = rng.uniform(0.02, 0.3)
    hu = np.diag([-np.exp(-3j * np.pi * u / 4)] + [np.exp(1j * np.pi * u / 4)] * 9)
    h = hu + rng.choice([0.01, 0.03, 0.1]) * u * E
    ths, _, _ = theta_set(h, 2880)
    if len(ths) == 0:
        continue
    d, T = normal_form(h, ths[len(ths) // 2])
    cls = class_of_phases(d)
    if cls is None:
        continue
    cnt += 1
    if cls == 0:
        c0 += 1
    inert = np.sum(np.linalg.eigvalsh(h.real) < 0)
    assert inert == 1
pr(f"  perturbations in C: {cnt}; of these in C_0: {c0}; Re h has exactly one negative eigenvalue in all")

open(__file__.replace('.py', '.txt'), 'w').write('\n'.join(out) + '\n')
