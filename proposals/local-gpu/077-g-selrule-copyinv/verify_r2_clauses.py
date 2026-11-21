"""verify_r2_clauses.py - round-2 evidence-first checks for the insert-r2 wording fixes.

Run from the repository root:
  python -I proposals/077-g-selrule-copyinv/verify_r2_clauses.py > proposals/077-g-selrule-copyinv/verify_r2_clauses.out 2>&1
Exit 0 with 'ALL CHECKS PASS' is the invariant. Checks (no script or out file is
written; this script only reads s2b_qwindow.out):

(A) the corrected 1-based statistic  D1 = max_{k=1,2}(e_{kq}-e_{(k-1)q+1})/max_j|e_j|
    equals the shipped code statistic  Dc = max_{k=0,1}(e[k*q+q-1]-e[k*q])/max|e|
    (s2 stats(), s2b line 211/229, identical form) on random spectra (q=2,3,4) and
    vanishes on tiled spectra, while the round-1 formula read 1-based does NOT vanish
    on a tiled spectrum (documents the off-by-one of finding 1).
(B) U_2 identity: on the identity-lift tiling Q~ = I_2 (x) Q_1 of the rank-one charge
    Q_1 = -2i(|u)(w| - |w)(u|), the code D statistic is 0 (exact tiling) while
    U_2 = mean(e^4)/mean(e^2)^2 - 1 > 0 equals (t_-^2-t_+^2)^2/(t_-^2+t_+^2)^2 and the
    closed form 4 rho^2 (rho^2+n)/(2 rho^2+n)^2, rho=Im(alpha), n=|w_perp|^2;
    U_2 = 0 <=> equal moduli (power mean): spectrum {-s,-s,-s,s} gives U_2 = 0, D > 0;
    the symmetric tiling {-eps,eps} gives U_2 = 0 (finding 2).
(C) the s4b scale mixture: sigma^2 = ln(1.96) gives CV(t)=sqrt(e^{sigma^2}-1) ~ 0.98
    for the variance multiplier t and CV(sqrt(t)) ~ 0.43 for the standard-deviation
    multiplier actually applied in the code (finding 4).
(D) s2b_qwindow.out section (a) grids: q=4,8,16 run through 16q^2, q=32 runs only
    {4q^2, 8q^2} = {4096, 8192} (finding 3).
"""
import numpy as np
rng = np.random.default_rng(7707707707)

FAIL = []


def check(name, cond):
    print('%-58s %s' % (name, 'OK' if cond else 'FAIL'))
    if not cond:
        FAIL.append(name)


def code_D(e, q):
    # shipped statistic: s2 stats() line 78, s2b lines 211/229 (sorted nonzero e)
    e = np.sort(np.asarray(e, float))
    assert len(e) == 2 * q
    return max(float(e[k * q + q - 1] - e[k * q]) for k in range(2)) / np.abs(e).max()


def D1_formula(e, q):
    # round-2 manuscript formula, 1-based indices e_1..e_{2q}
    e = np.sort(np.asarray(e, float))
    num = max(e[k * q - 1] - e[(k - 1) * q] for k in (1, 2))
    return num / np.abs(e).max()


def D_old_1based(e, q):
    # round-1 manuscript formula read 1-based: max_k (e_{(k+1)q-1} - e_{kq}), k=1,2
    # (k=2 term out of range for 2q eigenvalues; take k=1 term only)
    e = np.sort(np.asarray(e, float))
    return (e[(1 + 1) * q - 2] - e[1 * q - 1]) / np.abs(e).max()


def U2_of(e):
    e2 = np.asarray(e, float) ** 2
    return float(np.mean(e2 ** 2)) / float(np.mean(e2)) ** 2 - 1.0


# ---- (A) corrected formula == shipped code statistic
worst = 0.0
for q in (2, 3, 4):
    for _ in range(200):
        e = np.sort(rng.normal(size=2 * q) + 0.3 * rng.normal(size=2 * q))
        if np.abs(e).min() < 0.05:
            continue
        worst = max(worst, abs(code_D(e, q) - D1_formula(e, q)))
check('(A1) |D_code - D_corrected(1-based)| = %g on 600 random spectra' % worst,
      worst == 0.0)

tiled_bad = 0.0
for q in (2, 3, 4, 5):
    for _ in range(50):
        mset = np.sort(rng.uniform(0.5, 3.0, 2)) * rng.choice([-1.0, 1.0], 2)
        e = np.sort(np.tile(mset, q))
        if abs(D1_formula(e, q)) > 0 or abs(code_D(e, q)) > 0:
            tiled_bad += 1
        tiled_bad += 1 if D_old_1based(e, q) < 1e-12 else 0  # old formula must NOT vanish
check('(A2) corrected & code D = 0 on 200 tiled spectra; old-1-based never vanishes',
      tiled_bad == 0)

# ---- (B) U_2 identity on the named identity-lift tiling
worst_f = 0.0
worst_cf = 0.0
for _ in range(50):
    rho = rng.uniform(0.1, 2.0) * rng.choice([-1.0, 1.0])
    re = rng.uniform(-2.0, 2.0)
    b = rng.uniform(0.3, 3.0)
    u = np.array([1.0, 0.0, 0.0]) + 0j
    w = np.array([re + 1j * rho, b, 0.0]) + 0j
    Q1 = -2j * (np.outer(u, w.conj()) - np.outer(w, u.conj()))
    Qt = np.kron(np.eye(2), Q1)
    ev = np.linalg.eigvalsh(Qt)
    thr = 1e-9 * max(1.0, np.abs(ev).max())
    e = np.sort(ev[np.abs(ev) > thr].real)
    assert len(e) == 4
    assert e[1] - e[0] < 1e-10 and e[3] - e[2] < 1e-10  # exact double degeneracy
    d = code_D(e, 2)
    u2 = U2_of(e)
    tsm, tsp = ((e[0] + e[1]) / 2) ** 2, ((e[2] + e[3]) / 2) ** 2
    closed = (tsm - tsp) ** 2 / (tsm + tsp) ** 2
    cf = 4 * rho ** 2 * (rho ** 2 + b ** 2) / (2 * rho ** 2 + b ** 2) ** 2
    worst_f = max(worst_f, abs(d), abs(u2 - closed), u2 <= 0.0)
    worst_cf = max(worst_cf, abs(closed - cf))
check('(B1) identity-lift tiling: D_code = 0 and U_2 > 0 = (t_-^2-t_+^2)^2/(t_-^2+t_+^2)^2',
      worst_f < 1e-10)
check('(B2) closed form == 4 rho^2 (rho^2+n)/(2 rho^2+n)^2 (max dev %g)' % worst_cf,
      worst_cf < 1e-12)
u2_untiled = U2_of([-1.0, -1.0, -1.0, 1.0])
d_untiled = code_D([-1.0, -1.0, -1.0, 1.0], 2)
check('(B3) {-s,-s,-s,s}: U_2 = 0 (%g) but D = %.4g > 0 (not tiled)' % (u2_untiled, d_untiled),
      u2_untiled == 0.0 and d_untiled > 0)
check('(B4) symmetric tiling {-eps,eps}: U_2 = 0', U2_of([-0.7, -0.7, 0.7, 0.7]) == 0.0)

# ---- (C) lognormal mixture CVs
s_sig2 = np.log(1.4 ** 2)
t = np.exp(rng.normal(-s_sig2 / 2, np.sqrt(s_sig2), 2_000_000))
cv_t = t.std() / t.mean()
cv_sqrtt = np.sqrt(t).std() / np.sqrt(t).mean()
print('(C) empirical CV(t) = %.4f, CV(sqrt t) = %.4f; analytic sqrt(e^s2-1) = %.4f, '
      'sqrt(e^{s2/4}-1) = %.4f' % (cv_t, cv_sqrtt,
                                   np.sqrt(np.exp(s_sig2) - 1), np.sqrt(np.exp(s_sig2 / 4) - 1)))
check('(C1) CV of variance multiplier ~ 0.98 (not 0.4): %.4f' % cv_t, abs(cv_t - 0.98) < 0.01)
check('(C2) CV of std multiplier ~ 0.43: %.4f' % cv_sqrtt, abs(cv_sqrtt - 0.428) < 0.01)

# ---- (D) s2b grid extents from the shipped out
txt = open('proposals/077-g-selrule-copyinv/s2b_qwindow.out').read()
grids = {}
for line in txt.splitlines():
    if line.startswith('(a) q='):
        q = int(line.split('q=')[1].split(':')[0])
        pts = [int(s.strip().strip(chr(39)).split(':')[0]) for s in
               line.split('N,D median: [')[1].split(']')[0].split(',')]
        grids[q] = pts
ok = all(grids[q] == [4 * q * q, 8 * q * q, 16 * q * q] for q in (4, 8, 16))
ok = ok and grids[32] == [4 * 32 ** 2, 8 * 32 ** 2] == [4096, 8192]
print('(D) s2b (a) grids: %s' % grids)
check('(D1) q=4,8,16 through 16q^2; q=32 only {4096, 8192} = {4q^2, 8q^2}', ok)

print()
if FAIL:
    print('CHECKS FAILED: %s' % FAIL)
    raise SystemExit(1)
print('ALL CHECKS PASS')
