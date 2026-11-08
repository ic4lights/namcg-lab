#!/usr/bin/env python3
"""Checks for proposal 057 (plane-class invariant for the regulated Lorentzian integral with mass gamma > 0).

Conventions as in 055/056: eta = diag(-1,1,...,1), A = Lambda X, h = Lambda^T eta Lambda, ell = Lambda^T e_0,
gamma' = gamma/(2 g^2), M_g = eps Lambda^T Lambda + i gamma' h (matrix of the quadratic exponent on the contour),
phi = arg(eps + i gamma') in (0, pi/2), h' = e^{i phi} h, R' = Re h'.
For a real 2-plane P with R'|_P > 0: Theta(P) = arg det(h'|_P) on the branch theta_1+theta_2 in (-pi, pi),
theta_j = arctan(sigma_j), sigma_j eigenvalues of r^{-1/2} s r^{-1/2}, r = R'|_P, s = Im h'|_P.
D (Re iS_b <= 0 at N=2): Im det(h|_P) >= 0 for all real planes; then Theta in U=[2phi,pi) or L=(-pi,2phi-pi].

Checks
 A. Identity (eps+i gamma')h = M_g - 2 eps ell ell^T and R' > 0 on Z = {x real: Re ell.x = Im ell.x = 0}.
 B. Theta at eta (= 2 phi, class U) and at h_* = -e^{i pi/4} 1 (= 2 phi - 3 pi/2, class L).
 C. Admissibility of Lambda_* = diag(e^{i pi/8}, e^{-3 pi i/8} x 9) iff gamma' > eps.
 D. Random D-members: all sampled R'-positive planes have one class (connectedness of the positive planes).
 E. Random -C_0 members h = -T^T diag(d) T with n_-(R') <= 1: an R'-positive coordinate plane of class L exists
    (lemma), and every sampled R'-positive plane is L.
 F. Random walks from R_u (u = 0.3 eps/gamma', joined to Lambda = 1 along R_u) inside {Re M_g > 0, h in D}: class stays U (illustration of the theorem).
 G. Isotropic P = diag(p0, p, ..., p): (eps p + i gamma') h = eps Lambda^T P Lambda + i gamma' h - eps(p0+p) ell ell^T.
 H. eps -> 0 on R_u: admissible u closes like eps/gamma'; the limit contour is the Hermitian one.
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(57001)
n = 10
eta = np.diag([-1.0] + [1.0] * 9)
out = []


def pr(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)


def Mg(L, eps, gp):
    return eps * L.T @ L + 1j * gp * (L.T @ eta @ L)


def is_pd(S, tol=1e-12):
    return np.min(np.linalg.eigvalsh((S + S.T).real / 2)) > tol


def theta_plane(hp, a, b):
    B = np.stack([a, b], axis=1)
    H = B.T @ hp @ B
    r, s = H.real, H.imag
    w, V = np.linalg.eigh((r + r.T) / 2)
    if np.min(w) <= 1e-12:
        return None
    ri = V @ np.diag(w ** -0.5) @ V.T
    sig = np.linalg.eigvalsh(ri @ ((s + s.T) / 2) @ ri)
    return float(np.sum(np.arctan(sig)))


def cls(Theta, phi, tol=1e-9):
    if Theta is None:
        return None
    if Theta >= 2 * phi - tol:
        return 'U'
    if Theta <= 2 * phi - np.pi + tol:
        return 'L'
    return 'gap'


def Dmin(h, starts=12, iters=400):
    """min over orthonormal real a,b of Im det(h|span(a,b)); >= -tol means h in D (numerically)."""
    nn = h.shape[0]

    def f(v):
        a, b = v[:nn], v[nn:]
        a = a / np.linalg.norm(a)
        b = b - (a @ b) * a
        b = b / np.linalg.norm(b)
        return float(np.imag((a @ h @ a) * (b @ h @ b) - (a @ h @ b) ** 2))
    best = np.inf
    for _ in range(starts):
        r = minimize(f, rng.normal(size=2 * nn), method='BFGS', options={'maxiter': iters})
        best = min(best, r.fun)
    return best


def rand_planes(k, nn=n):
    for _ in range(k):
        Q, _ = np.linalg.qr(rng.normal(size=(nn, 2)))
        yield Q[:, 0], Q[:, 1]


# A
pr('== A: identity and Z-positivity ==')
worst_id, worst_Z = 0.0, np.inf
cntA = 0
for t in range(4000):
    L = np.eye(n) + 0.6 * (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) * rng.uniform(0, 1)
    eps, gp = rng.uniform(0.01, 1), rng.uniform(0.01, 3)
    M = Mg(L, eps, gp)
    if not is_pd(M.real):
        continue
    cntA += 1
    h = L.T @ eta @ L
    ell = L.T[:, 0]
    worst_id = max(worst_id, np.max(np.abs((eps + 1j * gp) * h - M + 2 * eps * np.outer(ell, ell))))
    phi = np.angle(eps + 1j * gp)
    Rp = (np.exp(1j * phi) * h).real
    C = np.stack([ell.real, ell.imag])
    _, _, Vt = np.linalg.svd(C)
    Zb = Vt[2:].T
    worst_Z = min(worst_Z, np.min(np.linalg.eigvalsh(Zb.T @ Rp @ Zb)))
    npos = np.sum(np.linalg.eigvalsh(Rp) > 0)
    assert npos >= 8
pr('admissible samples', cntA, 'max |identity residual|', f'{worst_id:.2e}', "min eig R'|_Z", f'{worst_Z:.3e}', "(>0); n_+(R') >= 8 in all")

# B
pr('== B: Theta at eta and h_* ==')
for phv in [0.3, 0.7, 1.0, 1.4]:
    hs = -np.exp(1j * np.pi / 4) * np.eye(n)
    hpe = np.exp(1j * phv) * eta.astype(complex)
    te = [theta_plane(hpe, a, b) for a, b in rand_planes(400)]
    te = [x for x in te if x is not None]
    pr(f'phi={phv}: eta: {len(te)} positive planes of 400, Theta range [{min(te):.9f},{max(te):.9f}] vs 2phi={2 * phv:.9f}; classes', sorted(set(cls(x, phv) for x in te)))
    hp = np.exp(1j * phv) * hs
    if np.min(np.linalg.eigvalsh(hp.real)) <= 0:
        pr(f"   h_*: R' not positive (phi <= pi/4, Lambda_* not admissible)")
        continue
    ths = [theta_plane(hp, a, b) for a, b in rand_planes(50)]
    pr(f'   h_*: Theta range [{min(ths):.9f},{max(ths):.9f}] vs 2phi-3pi/2={2 * phv - 1.5 * np.pi:.9f}, 2phi-pi={2 * phv - np.pi:.9f}; class', cls(ths[0], phv))

# C
pr('== C: admissibility of Lambda_* ==')
Ls = np.diag([np.exp(1j * np.pi / 8)] + [np.exp(-3j * np.pi / 8)] * 9)
for eps, gp in [(0.1, 0.2), (0.2, 0.1), (0.1, 0.1001), (0.1, 0.0999), (0.01, 1.0)]:
    M = Mg(Ls, eps, gp)
    pr(f"eps={eps}, gamma'={gp}: min eig Re M_g = {np.min(np.linalg.eigvalsh(M.real)):+.6f}; (gamma'-eps)/sqrt2 = {(gp - eps) / np.sqrt(2):+.6f}")
hs = Ls.T @ eta @ Ls
pr('h(Lambda_*) = -e^{i pi/4} 1 :', np.allclose(hs, -np.exp(1j * np.pi / 4) * np.eye(n)))

# D
pr('== D: one class on the positive planes of D-members ==')
cntD = 0
tried = 0
for t in range(80):
    tried += 1
    beta = rng.uniform(0, 0.3, size=n)
    d = np.exp(1j * beta)
    d[0] = -np.exp(1j * rng.uniform(-0.5, 0.0))
    T = np.eye(n) + 0.3 * rng.normal(size=(n, n))
    h = T.T @ np.diag(d) @ T
    if Dmin(h, starts=4) < -1e-9:
        continue
    for phv in [0.5, 1.2]:
        hp = np.exp(1j * phv) * h
        cl = set()
        for a, b in rand_planes(300):
            c = cls(theta_plane(hp, a, b), phv)
            if c is not None:
                cl.add(c)
        assert 'gap' not in cl and len(cl) <= 1, cl
    cntD += 1
pr('D-members tested', cntD, 'of', tried, "candidates: every sampled R'-positive plane in a single class, no gap values")

# E
pr('== E: -C_0 members with n_-(R\') <= 1 have class L ==')
cntE = 0
iu = np.triu_indices(n, 1)
for t in range(20000):
    beta = rng.uniform(0, np.pi / 2, size=n)
    if rng.uniform() < 0.5:
        beta[0] = rng.uniform(-np.pi / 2, 0)
    if rng.uniform() < 0.5:
        beta[1] = rng.uniform(np.pi / 2, np.pi)
    s = beta[:, None] + beta[None, :]
    if not np.all((s[iu] > 0) & (s[iu] < np.pi)):
        continue
    d = np.exp(1j * beta) * rng.uniform(0.5, 2, size=n)
    phv = rng.uniform(0.01, np.pi / 2 - 0.01)
    alpha = np.angle(-np.exp(1j * phv) * d)
    pos = np.cos(alpha) > 0
    if np.sum(np.cos(alpha) < 0) > 1:
        continue
    cntE += 1
    good = [mu for mu in range(n) if pos[mu] and 0 < beta[mu] < np.pi / 2]
    assert len(good) >= 2, (beta, alpha)
    mu, nu = good[0], good[1]
    assert alpha[mu] + alpha[nu] <= 2 * phv - np.pi + 1e-12
    if cntE <= 300:
        T = np.eye(n) + 0.4 * rng.normal(size=(n, n))
        h = -T.T @ np.diag(d) @ T
        hp = np.exp(1j * phv) * h
        cl = set()
        for a, b in rand_planes(200):
            c = cls(theta_plane(hp, a, b), phv)
            if c is not None:
                cl.add(c)
        assert cl <= {'L'}, cl
pr('admissible -C_0 samples', cntE, ": each has an R'-positive coordinate pair with beta in (0,pi/2) and Theta <= 2phi-pi; first 300 (with a real congruence T): all sampled positive planes L")


# F
pr("== F: random walks from R_u, u = 0.3 eps/gamma' (joined to Lambda = 1 inside the class) ==")
def walk(eps, gp, steps, bias, seed, step=0.004):
    r = np.random.default_rng(seed)
    phv = np.angle(eps + 1j * gp)
    u0 = 0.3 * eps / gp
    L = np.diag([np.exp(-3j * np.pi * u0 / 8)] + [np.exp(1j * np.pi * u0 / 8)] * 9)
    acc = 0
    classes = set()
    for k in range(steps):
        Z = r.normal(size=(n, n)) + 1j * r.normal(size=(n, n))
        Ln = L + step * Z / np.linalg.norm(Z) * np.sqrt(n) + bias * (Ls - L) / max(1, np.linalg.norm(Ls - L))
        M = Mg(Ln, eps, gp)
        if not is_pd(M.real):
            continue
        h = Ln.T @ eta @ Ln
        if Dmin(h, starts=3, iters=200) < -1e-10:
            continue
        L = Ln
        acc += 1
        hp = np.exp(1j * phv) * h
        for a, b in rand_planes(40):
            c = cls(theta_plane(hp, a, b), phv)
            if c is not None:
                classes.add(c)
    return L, acc, classes


for eps, gp, bias, seed in [(0.1, 0.5, 0.0, 1), (0.1, 0.5, 0.02, 2), (0.05, 1.0, 0.02, 3)]:
    L, acc, classes = walk(eps, gp, 150, bias, seed)
    h = L.T @ eta @ L
    dist = np.linalg.norm(h + np.exp(1j * np.pi / 4) * np.eye(n))
    pr(f"eps={eps}, gamma'={gp}, bias={bias}: accepted {acc}/150, classes seen {sorted(classes)}, |h - h_*| at end {dist:.3f} (|eta - h_*| = {np.linalg.norm(eta + np.exp(1j * np.pi / 4) * np.eye(n)):.3f})")

# G
pr('== G: isotropic P identity ==')
worst = 0
for t in range(200):
    p0, p = rng.uniform(0.2, 3, size=2)
    P = np.diag([p0] + [p] * 9)
    L = np.eye(n) + 0.5 * (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
    eps, gp = rng.uniform(0.01, 1, size=2)
    h = L.T @ eta @ L
    ell = L.T[:, 0]
    lhs = (eps * p + 1j * gp) * h
    rhs = eps * L.T @ P @ L + 1j * gp * h - eps * (p0 + p) * np.outer(ell, ell)
    worst = max(worst, np.max(np.abs(lhs - rhs)))
pr('max residual', f'{worst:.2e}')

# H
pr('== H: eps -> 0 on R_u at fixed gamma\' ==')
gp = 1.0
for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
    us = np.linspace(0, 0.66, 660001)
    ok = (eps * np.cos(3 * np.pi * us / 4) - gp * np.sin(3 * np.pi * us / 4) > 0) & (eps * np.cos(np.pi * us / 4) - gp * np.sin(np.pi * us / 4) > 0)
    umax = us[ok].max()
    pr(f"eps={eps}: largest admissible u on R_u = {umax:.7f}, u*gamma'/eps = {umax * gp / eps:.4f} (limit 4/(3 pi) = {4 / (3 * np.pi):.4f})")
pr('limit contour as eps -> 0: u -> 0, h_0 = eta, Im h_0 = 0, Re iS_b = 0 on all real X')

with open(__file__.replace('.py', '.txt'), 'w') as f:
    f.write('\n'.join(out) + '\n')
