"""051 s6 (round 2): checks for findings F1, F4, F5, F10, F11.  Numerical checks, seeded; the reasoning is in proposal-r2.md.

 A (F1, R14, R15) The 2 x 2 matrix on the probes of s3 is a compression of the multiplication operator Q2(p,t), not its
   restriction to an invariant space.  With Gauss-Hermite quadrature (exact in p, spectrally accurate in t):
   the entries H_ij; the defect ||Q2 O_i||^2 - sum_j H_ij^2, zero if and only if the span is invariant;
   the leading ratio ||Q2 O_i||^2 / H12^2, derived by hand to be 3; the 3 x 3 Hankel determinant of the spectral moments,
   zero for any measure of at most two atoms.
 B (F1) Seeded Monte Carlo of the spectral measure of each probe under the full operator: non-negative weights; quantiles
   against the compressed eigenvalues; largest bin mass per unit width as bins shrink (bounded means no atom seen);
   eps Im G(lambda + i eps) at the compressed eigenvalue against the same for the compressed resolvent (residue);
   density near s = 0 against the leading formula sqrt2/(pi sigma sqrt(vGv)), derived in proposal-r2.md; here vGv = 4.
 C (R7) On a finite model of (p,u) with translation charge k: eta^{ab} Tr(A_a^dagger A_b) = sum |O|^2,
   eta^{ab} Tr(A_a A_b) = 0 for k != 0, and the Hermitian part has half the value.  Control at k = 0, where this fails.
 D (R8, R9, R10) G = int w p p on weights on a hyperplane through the origin, on an affine hyperplane off the origin, on a null
   hyperplane q.p = 0 and generic; the values for h_i^0, for h_i^mu along q, and for the fibre probes of J_lambda.
 E (R1) gauge directions have value Q.Q |Lambda|^2 of either sign and solve E A = 0.
 F (R12, R13) k.lambda = 0 gives v = 0 and the first probe vanishes; right translation of u alone gives the multiplier
   (k + (1 - Lam)p)^2, while exp(t J) gives k^2 = 0.
"""
import numpy as np

etan = np.array([-1.0, 1, 1, 1])
eta = np.diag(etan)
k0 = np.array([-1.0, 1, 0, 0])


def boost(t, a=0, b=2):
    """arrays of t -> array (...,4,4)"""
    t = np.asarray(t, dtype=float)
    L = np.zeros(t.shape + (4, 4))
    L[..., range(4), range(4)] = 1
    L[..., a, a] = np.cosh(t)
    L[..., b, b] = np.cosh(t)
    L[..., a, b] = np.sinh(t)
    L[..., b, a] = np.sinh(t)
    return L


def rot(t, a=1, b=2):
    t = np.asarray(t, dtype=float)
    L = np.zeros(t.shape + (4, 4))
    L[..., range(4), range(4)] = 1
    L[..., a, a] = np.cos(t)
    L[..., b, b] = np.cos(t)
    L[..., a, b] = -np.sin(t)
    L[..., b, a] = np.sin(t)
    return L


def Q2(p, Lam, k=k0):
    """p (n,4), Lam (n,4,4): (k + (1 - Lam)p)^2"""
    vec = k + p - np.einsum('...ij,...j->...i', Lam, p)
    return (vec ** 2 * etan).sum(axis=-1)


CASES = [('boost(0,2)', boost, np.array([0.0, 0, -2, 0])), ('rotation(1,2)', rot, np.array([0.0, 0, 2, 0]))]

print('=== A compression against the full multiplication operator, Gaussian w, P = 1')
for name, Lf, v in CASES:
    # v is confirmed from a finite difference of Q2 at t = 0
    test_p = np.array([[0.3, -0.7, 1.1, 0.4]])
    h = 1e-6
    dQ = (Q2(test_p, Lf(np.array([h]))) - Q2(test_p, Lf(np.array([-h])))) / (2 * h)
    assert abs(dQ[0] - test_p[0] @ v) < 1e-6, (dQ, test_p[0] @ v)
    a = float(v @ v)
    xp, wp = np.polynomial.hermite.hermgauss(10)
    xp = np.sqrt(2) * xp
    wp = wp / np.sqrt(np.pi)
    g = np.stack(np.meshgrid(xp, xp, xp, xp, indexing='ij'), axis=-1).reshape(-1, 4)
    gw = np.prod(np.stack(np.meshgrid(wp, wp, wp, wp, indexing='ij'), axis=-1).reshape(-1, 4), axis=1)
    xt, wt = np.polynomial.hermite.hermgauss(40)
    wt = wt / np.sqrt(np.pi)
    print('---', name, 'v =', v.tolist(), ' a = vGv =', a)
    for sig in (0.1, 0.05, 0.01):
        m1 = np.zeros(5)
        m2 = np.zeros(5)
        H12 = 0.0
        for x_, w_ in zip(xt, wt):
            t = sig * x_
            Lam = Lf(np.full(len(g), t))
            q = Q2(g, Lam)
            vp = g @ v
            W1 = vp ** 2 / a
            W2 = 2 * t ** 2 / sig ** 2
            W12 = vp / np.sqrt(a) * (-np.sqrt(2) * t / sig)
            for j in range(5):
                m1[j] += w_ * (gw * W1 * q ** j).sum()
                m2[j] += w_ * (gw * W2 * q ** j).sum()
            H12 += w_ * (gw * W12 * q).sum()
        H = np.array([[m1[1], H12], [H12, m2[1]]])
        ev, U = np.linalg.eigh(H)
        d1 = m1[2] - (H[0, 0] ** 2 + H12 ** 2)
        d2 = m2[2] - (H[1, 1] ** 2 + H12 ** 2)
        # Hankel, full measure against compression, normalised by the cube of the variance
        def hank(m):
            return np.linalg.det(np.array([[m[0], m[1], m[2]], [m[1], m[2], m[3]], [m[2], m[3], m[4]]]))
        var1 = m1[2] - m1[1] ** 2
        mc = [(np.linalg.matrix_power(H, j))[0, 0] for j in range(5)]
        varc = mc[2] - mc[1] ** 2
        print(' sigma=%.2f norms %.10f %.10f | H11=%.3e H22=%.3e H12=%.6e | eigenvalues %.6f %.6f' %
              (sig, m1[0], m2[0], H[0, 0], H[1, 1], H12, ev[0], ev[1]))
        print('   defect ||Q O1||^2-|H e1|^2=%.4e, ||Q O2||^2-|H e2|^2=%.4e; ratio ||Q O1||^2/H12^2=%.5f, ||Q O2||^2/H12^2=%.5f' %
              (d1, d2, m1[2] / H12 ** 2, m2[2] / H12 ** 2))
        print('   Hankel3/var^3: full measure of O1 %.4f; compression %.2e' % (hank(m1) / var1 ** 3, hank(mc) / varc ** 3))
        assert d1 > 0.5 * H12 ** 2 and d2 > 0.5 * H12 ** 2
        assert abs(hank(mc) / varc ** 3) < 1e-6 and hank(m1) / var1 ** 3 > 1
    assert abs(m1[2] / H12 ** 2 - 3) < 0.01 and abs(m2[2] / H12 ** 2 - 3) < 0.01

print('=== B spectral measure of the probes under the full operator, Monte Carlo, sigma = 0.05, P = 1, N = 4000000')
rng = np.random.default_rng(5102)
N = 4000000
sig = 0.05
for name, Lf, v in CASES:
    p = rng.normal(0, 1, size=(N, 4))
    t = rng.normal(0, sig / np.sqrt(2), size=N)
    Lam = Lf(t)
    q = Q2(p, Lam)
    vp = p @ v
    a = float(v @ v)
    W = {'O1': vp ** 2 / a, 'O2': 2 * t ** 2 / sig ** 2}
    # compression from the same sample, so sampling error does not enter the comparison
    H = np.array([[(W['O1'] * q).mean(), (vp / np.sqrt(a) * (-np.sqrt(2) * t / sig) * q).mean()], [0, (W['O2'] * q).mean()]])
    H[1, 0] = H[0, 1]
    ev, U = np.linalg.eigh(H)
    print('---', name, ' compressed eigenvalues %.5f %.5f, predicted +-%.5f' % (ev[0], ev[1], sig / np.sqrt(2) * np.sqrt(a)))
    pred0 = 1 / (np.sqrt(2) * np.pi * sig)
    for lab, i in (('O1', 0), ('O2', 1)):
        wt_ = W[lab]
        assert (wt_ >= 0).all()
        order = np.argsort(q)
        qs, ws = q[order], wt_[order]
        cw = np.cumsum(ws) / ws.sum()
        qq = [qs[np.searchsorted(cw, x)] for x in (0.05, 0.25, 0.5, 0.75, 0.95)]
        beyond = ws[np.abs(qs) > np.abs(ev).max()].sum() / ws.sum()
        print('  %s: non-negative weights, total %.5f; quantiles 5,25,50,75,95%% = %s; mass beyond the larger compressed |eigenvalue| %.3f' %
              (lab, wt_.mean(), ' '.join('%.4f' % x for x in qq), beyond))
        rows = []
        for width in (0.02, 0.01, 0.005, 0.0025):
            edges = np.arange(-1.0, 1.0 + width, width)
            mass, _ = np.histogram(q, bins=edges, weights=wt_ / wt_.sum())
            rows.append('%.4f:%.2f' % (width, mass.max() / width))
        print('     largest bin mass / width, by width (bounded: no atom seen) ', ' '.join(rows))
        win = 0.01
        dens = ws[np.abs(qs) < win].sum() / ws.sum() / (2 * win)
        print('     density near 0, window +-%.2f: %.3f; leading formula 1/(sqrt2 pi sigma) = %.3f' % (win, dens, pred0))
        lam = ev[1]
        resid = U[i, :] ** 2
        cols = []
        for e_ in (0.02, 0.005, 0.00125):
            full = e_ * (wt_ / wt_.sum() * e_ / ((lam - q) ** 2 + e_ ** 2)).sum()
            comp = e_ * (resid * e_ / ((lam - ev) ** 2 + e_ ** 2)).sum()
            cols.append('eps=%.5f: full %.4f, compression %.4f' % (e_, full, comp))
        print('     eps Im G at the upper compressed eigenvalue;', '; '.join(cols))
        assert full < 0.05 and comp > 0.3

print('=== C pairing and Hermitian part on a finite model with translation charge k')


def random_lorentz(r):
    return boost(r.normal(), 0, r.integers(1, 4)) @ rot(r.normal(), 1, 2) @ rot(r.normal(), 2, 3)


def finite_model(k, L=7, nu=5, seed=7):
    r = np.random.default_rng(seed)
    us = [random_lorentz(r) for _ in range(nu)]
    for u in us:
        assert np.allclose(u @ eta @ u.T, eta)
    eps_ = np.array([0.3, 0.2, -0.4, 0.0])
    eps_ = eps_ / np.sqrt(abs(eps_ @ eta @ eps_))
    assert abs(eps_ @ eta @ eps_ - 1) < 1e-12 or abs(eps_ @ eta @ eps_ + 1) < 1e-12
    if eps_ @ eta @ eps_ < 0:
        raise SystemExit('choose a spacelike epsilon')
    D = L * nu
    idx = lambda ip, iu: ip * nu + iu
    O = np.zeros((D, D), dtype=complex)
    for ip in range(L):
        for iu in range(nu):
            for ju in range(nu):
                O[idx(ip, iu), idx((ip - k) % L, ju)] = r.normal() + 1j * r.normal()
    A = np.zeros((4, D, D), dtype=complex)
    for ip in range(L):
        for iu in range(nu):
            for a_ in range(4):
                A[a_, idx(ip, iu), :] = (us[iu][a_] @ eps_) * O[idx(ip, iu), :]
    herm = 0.5 * (A + np.conj(np.transpose(A, (0, 2, 1))))
    pair = sum(etan[a_] * np.trace(np.conj(A[a_]).T @ A[a_]) for a_ in range(4))
    cross = sum(etan[a_] * np.trace(A[a_] @ A[a_]) for a_ in range(4))
    hval = sum(etan[a_] * np.trace(herm[a_] @ herm[a_]) for a_ in range(4))
    return (np.abs(O) ** 2).sum(), pair, cross, hval


for k in (1, 3, 0):
    o2, pair, cross, hval = finite_model(k)
    print('  k=%d: sum|O|^2=%.8f; eta Tr(A^dag A)=%.8f%+.1ei; |eta Tr(A A)|=%.3e; eta Tr(H H)=%.8f; ratio %.8f' %
          (k, o2, pair.real, pair.imag, abs(cross), hval.real, hval.real / o2))
    assert abs(pair - o2) < 1e-9
    if k != 0:
        assert abs(cross) < 1e-9 and abs(hval.real / o2 - 0.5) < 1e-12
    else:
        assert abs(cross) > 1e-3 and abs(hval.real / o2 - 0.5) > 1e-3
print('  control k=0: the cross term does not vanish and the half-value fails, so the charge condition is needed')

print('=== D the matrix G on hyperplanes; R8, R9, R10')
q_up = np.array([1.0, 1, 0, 0])
r = np.random.default_rng(9)
base = r.normal(size=(4000, 4))
sets = {
    'generic': base,
    'through the origin, p_0=0': base * np.array([0.0, 1, 1, 1]),
    'affine off the origin, p_0=1': base * np.array([0.0, 1, 1, 1]) + np.array([1.0, 0, 0, 0]),
    'through the origin, q.p=0, q null': np.stack([-base[:, 1], base[:, 1], base[:, 2], base[:, 3]], axis=1),
}
for nm, s in sets.items():
    w = np.full(len(s), 1 / len(s))
    G = (s * w[:, None]).T @ s
    ev = np.linalg.eigvalsh(G)
    # fibre probes of J_lambda: value int psi^2 int w, on a grid in t
    tg = np.linspace(-1, 1, 4001)
    dt = tg[1] - tg[0]
    sg = 0.05
    phi = (np.exp(-tg ** 2 / sg ** 2) / (sg * np.sqrt(np.pi))) ** 0.5
    psi = np.sqrt(2) * sg * np.gradient(phi, tg)
    val_J = (psi ** 2).sum() * dt * w.sum()
    print('  %-36s eig G min %.5f max %.3f; G_00=%.5f, G_11=%.3f; h_i^0 value G_00; h along q: qGq=%.5f; fibre probe of J_lambda: %.5f' %
          (nm, ev[0], ev[-1], G[0, 0], G[1, 1], q_up @ G @ q_up, val_J))
    assert ev[0] > -1e-12 and val_J > 0.99
    c = (G[1, 1] + G[0, 0]) / 2
    assert not np.allclose(G, c * eta)
print('  so: on p_0=0 the value of h_i^0 is 0 (rejects "positive on every truncation"); on q.p=0 the direction q has value 0;')
print('  on an affine hyperplane G stays positive definite (rejects "unless w lies on a hyperplane"); the fibre probe is unaffected.')

print('=== E gauge directions on shell')
rq = np.random.default_rng(11)
seen = set()
for _ in range(2000):
    Q = rq.normal(size=4) * np.array([1.3, 1, 1, 1])
    L_ = rq.normal() + 1j * rq.normal()
    A = Q * L_
    QQ = Q @ eta @ Q
    Ea = QQ * A - Q * (Q @ eta @ A)
    form = (np.conj(A) @ eta @ A).real
    assert np.allclose(Ea, 0)
    assert abs(form - QQ * abs(L_) ** 2) < 1e-10
    seen.add(np.sign(QQ))
print('  E A = 0 and form = Q.Q |Lambda|^2 on 2000 samples; signs of Q.Q seen:', sorted(seen))
assert seen == {-1.0, 1.0}

print('=== F k.lambda != 0, and right translation of u alone against exp(t J)')
rr = np.random.default_rng(13)
ps_ = rr.normal(size=(200, 4))
dq = (Q2(ps_, rot(np.full(200, 1e-6), 2, 3)) - Q2(ps_, rot(np.full(200, -1e-6), 2, 3))) / 2e-6
print('  rotation (2,3) with k=(-1,1,0,0), so k.lambda=0: max |d Q2/dt at 0| over 200 p = %.2e, so v=0 and the first probe vanishes' % np.abs(dq).max())
assert np.abs(dq).max() < 1e-6
for t_ in (0.3, -0.8):
    Lam = boost(t_)
    Li = np.linalg.inv(Lam)
    u = random_lorentz(rr)
    pp = rr.normal(size=4)
    # kernel of e^{ik.y} R_Lam from m'=(p',u') to m=(p'+k, u' Lam^{-1}): X_a(m) - X_a(m'), X_a = -u_a^b p_b, with u' = u Lam
    up = u @ Lam
    Q_R = -u @ (pp + k0) + up @ pp
    expected = (k0 + (np.eye(4) - Lam) @ pp)
    # exp(t J): the same right translation combined with p -> Lam p on the source, so that u p is preserved on the label
    Q_J = -u @ (Lam @ pp + k0) + up @ pp
    print('  t=%+.1f: right translation alone Q.Q=%.6f, (k+(1-Lam)p)^2=%.6f; with exp(tJ) Q.Q=%.2e' %
          (t_, Q_R @ eta @ Q_R, expected @ eta @ expected, Q_J @ eta @ Q_J))
    assert abs(Q_R @ eta @ Q_R - expected @ eta @ expected) < 1e-9
    assert abs(Q_J @ eta @ Q_J) < 1e-9
print('ALL ASSERTIONS PASSED')
