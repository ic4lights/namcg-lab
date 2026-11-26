"""laplace_model_r2.py -- verification of the corrected commuting-ray Laplace
model used in proposal 054 round 2 (gatekeeper findings F1 and F3).

Checks:
(1) exact Gaussian Fourier integral: for real c>0, eps>0 and complex kappa,
    int_R exp(+/- i*kappa*rho/2 - c*eps*rho^2/2) drho
        = sqrt(2*pi/(c*eps)) * exp(-kappa^2/(8*c*eps));
    real-kappa case symbolically (sympy), complex-kappa case numerically (mpmath).
(2) branch sum: I_+ = I_- exactly (rho -> -rho maps the even Gaussian weight onto
    itself and flips the phase), so I_+ + I_- = 2*sqrt(2*pi/(c*eps))*exp(-kappa^2/(8*c*eps));
    for kappa = a + i b the log-modulus grows like (b^2 - a^2)/(8*c*eps), so growth
    as eps -> 0+ happens iff b^2 > a^2, i.e. |Im kappa| > |Re kappa|.
(3) failure set of the ray condition: for k = u + i v (u, v real) and real unit
    rho_hat, |Im(k.rho_hat)| > |Re(k.rho_hat)| iff (v.rho_hat)^2 > (u.rho_hat)^2;
    max over unit rho_hat of the difference is lambda_max(v v^T - u u^T), and
    lambda_max <= 0 iff v = c u with |c| <= 1 (rank-one PSD argument), so exactly
    the family k = u + i c u, |c| <= 1, has NO commuting ray with |Im| > |Re|.
(4) anti-Wick-slice tangents at u = 0: slice points have k^0 = r^0 exp(+3 pi i/8),
    k^i = r^i exp(-pi i/8).  A pure-time slice point gives v = tan(3 pi/8) u with
    tan(3 pi/8) > 1 (some ray has |Im| > |Re|); a pure-space slice point gives
    |c| = tan(pi/8) < 1 (no ray has |Im| > |Re|).  Generic mixed slice points have
    v not parallel to u, hence lambda_max > 0.
(5) F3 inequality: 2*sinh(|y|/2) <= |2*cos((x + i y)/2)| for all real x, y, from
    |2 cos(z/2)|^2 = 4(cos^2(x/2) + sinh^2(y/2)); the superseded bound exp(b*rho)/4
    is violated, e.g. at b = 0.7, rho = 40, Re omega = pi (factor-2 exponent error).
All outputs are symbolic/numerical checks, not proofs.
"""
import numpy as np
import sympy as sp
import mpmath as mp

ok = True


def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        ok = False


# ---------- (1) exact Gaussian Fourier integral ----------
rho = sp.symbols("rho", real=True)
kap = sp.symbols("kappa", real=True)
cc, ee = sp.symbols("c eps", positive=True)
I_real = sp.integrate(sp.exp(sp.I * kap * rho / 2 - cc * ee * rho ** 2 / 2),
                      (rho, -sp.oo, sp.oo))
target = sp.sqrt(2 * sp.pi / (cc * ee)) * sp.exp(-kap ** 2 / (8 * cc * ee))
chk("(1a) sympy real-kappa gaussian equals sqrt(2pi/(c eps)) exp(-kappa^2/(8 c eps))",
    sp.simplify(I_real - target) == 0)

mp.mp.dps = 80


def gauss_num(kap_c, ccv, eev, sign=1):
    f = lambda t: mp.exp(sign * 1j * kap_c * t / 2 - ccv * eev * t * t / 2)
    return mp.quad(f, [-mp.inf, mp.inf])


worst = mp.mpf(0)
samples = [(0.3, 1.7, 2.0, mp.mpf("0.05")), (-1.2, -0.4, 1.0, mp.mpf("0.02")),
           (0.9, 0.9, 1.5, mp.mpf("0.01")), (2.0, 0.0, 1.0, mp.mpf("0.1"))]
for (aa, bb, ccv, eev) in samples:
    kc = aa + 1j * bb
    ana = mp.sqrt(2 * mp.pi / (ccv * eev)) * mp.exp(-kc ** 2 / (8 * ccv * eev))
    for sgn in (1, -1):
        rel = abs(gauss_num(kc, ccv, eev, sgn) - ana) / abs(ana)
        worst = max(worst, rel)
chk("(1b) complex-kappa numeric quad matches analytic form (rel err < 1e-8)",
    worst < 1e-8)
print("    max rel err over samples = %s" % mp.nstr(worst, 3))

# ---------- (2) branch sum and growth criterion ----------
relmax = mp.mpf(0)
for (aa, bb) in [(0.6, 1.4), (1.4, 0.6), (0.0, 1.0), (1.0, 0.0)]:
    kc = aa + 1j * bb
    seq = [mp.mpf("0.05"), mp.mpf("0.01"), mp.mpf("0.002")]
    mags = []
    for eev in seq:
        ip = gauss_num(kc, 2.0, eev, 1)
        im = gauss_num(kc, 2.0, eev, -1)
        mags.append(abs(ip + im))
        pred = 2 * mp.sqrt(2 * mp.pi / (2.0 * eev)) * mp.exp((bb ** 2 - aa ** 2) / (8 * 2.0 * eev))
        relmax = max(relmax, abs(mags[-1] / pred - 1))
    growth = (bb ** 2 > aa ** 2)
    mono = (mags[0] < mags[1] < mags[2]) if growth else (mags[0] > mags[1] > mags[2])
    chk("(2) branch-sum modulus = 2 sqrt(2pi/(c eps)) e^{(b^2-a^2)/(8c eps)} and "
        "eps->0 growth iff b^2>a^2 : a=%.1f b=%.1f" % (aa, bb), mono)
chk("(2c) branch-sum modulus formula rel err < 1e-8 over cases", relmax < 1e-8)
print("    max rel err = %s" % mp.nstr(relmax, 3))

# ---------- (3) failure set of the ray condition ----------
rng = np.random.default_rng(7)


def lmax(u, v):
    return np.linalg.eigvalsh(np.outer(v, v) - np.outer(u, u))[-1]


bad = 0
for _ in range(500):  # generic (independent) pairs must admit a growth ray
    u = rng.normal(size=10)
    v = rng.normal(size=10)
    if lmax(u, v) <= 1e-9:
        bad += 1
chk("(3a) generic non-parallel (u,v) in R^10 admit a ray with (v.r)^2>(u.r)^2 (500 draws)",
    bad == 0)
bad = 0
for _ in range(500):
    u = rng.normal(size=10)
    ccv = rng.uniform(-1, 1)
    v = ccv * u
    if lmax(u, v) > 1e-9:
        bad += 1
chk("(3b) k = u + i c u with |c| <= 1 has NO growth ray (500 draws, lambda_max <= 0)",
    bad == 0)
bad = 0
for _ in range(500):
    u = rng.normal(size=10)
    ccv = rng.uniform(1.05, 3.0)
    v = ccv * u
    if lmax(u, v) <= 1e-9:
        bad += 1
chk("(3c) k = u + i c u with |c| > 1 admits growth rays (500 draws, lambda_max > 0)",
    bad == 0)
u = rng.normal(size=10)
lam1 = lmax(u, u)
lam_m1 = lmax(u, -u)
lam0 = lmax(u, 0.5 * u)
chk("(3d) |c|<=1 families give lambda_max = 0 (top eigenvalue sits at 0 on the "
    "orthogonal nullspace; no strict growth ray)",
    abs(lam1) < 1e-9 and abs(lam_m1) < 1e-9 and abs(lam0) < 1e-9)

# ---------- (4) anti-Wick slice tangents at u = 0 ----------
t_s = np.tan(np.pi / 8)
t_t = np.tan(3 * np.pi / 8)
chk("(4a) tan(pi/8) < 1 < tan(3pi/8)", t_s < 1 < t_t)
e0 = np.zeros(4)
e0[0] = 1.0
ei = np.zeros(4)
ei[1] = 1.0
uT = np.cos(3 * np.pi / 8) * e0
vT = np.sin(3 * np.pi / 8) * e0
uS = np.cos(np.pi / 8) * ei
vS = -np.sin(np.pi / 8) * ei
chk("(4b) pure-time slice point (k0 = r e^{3 pi i/8}): growth ray exists",
    lmax(uT, vT) > 0)
chk("(4c) pure-space slice point (ki = r e^{-pi i/8}): no strict growth ray "
    "(lambda_max = 0 = -cos(pi/4) < 0 on the e_i plane, 0 on the orthogonal 8-space)",
    lmax(uS, vS) <= 1e-12)
r0, ri = rng.uniform(0.2, 2.0), rng.uniform(0.2, 2.0)
uMix = r0 * np.cos(3 * np.pi / 8) * e0 + ri * np.cos(np.pi / 8) * ei
vMix = r0 * np.sin(3 * np.pi / 8) * e0 - ri * np.sin(np.pi / 8) * ei
bad = 0
for _ in range(200):
    r0, ri = rng.uniform(0.05, 3.0), rng.uniform(0.05, 3.0)
    uM = r0 * np.cos(3 * np.pi / 8) * e0 + ri * np.cos(np.pi / 8) * ei
    vM = r0 * np.sin(3 * np.pi / 8) * e0 - ri * np.sin(np.pi / 8) * ei
    if lmax(uM, vM) <= 1e-12:
        bad += 1
chk("(4d) generic mixed slice point: v not parallel u, growth ray exists (200 draws)",
    bad == 0)

# ---------- (5) F3 inequality and superseded bound ----------
xs = rng.uniform(-40, 40, 20000)
ys = rng.uniform(-40, 40, 20000)
lhs = 2 * np.sinh(np.abs(ys) / 2)
rhs = np.abs(2 * np.cos((xs + 1j * ys) / 2))
chk("(5a) 2 sinh(|y|/2) <= |2 cos((x+iy)/2)| on 20000-point grid (relative tol)",
    np.all(lhs <= rhs + 1e-9 * np.maximum(1.0, rhs)))
A2 = np.abs(2 * np.cos((xs + 1j * ys) / 2)) ** 2
B2 = 4 * (np.cos(xs / 2) ** 2 + np.sinh(ys / 2) ** 2)
chk("(5b) |2 cos(z/2)|^2 = 4(cos^2(x/2) + sinh^2(y/2)) on same grid (relative tol)",
    np.all(np.abs(A2 - B2) <= 1e-9 * np.maximum(1.0, np.abs(B2))))
bbv, rrv = 0.7, 40.0
exact_worst = abs(2 * np.cos((np.pi + 1j * bbv * rrv) / 2))  # = 2 sinh(b rho / 2)
new_bound = 2 * np.sinh(bbv * rrv / 2)
old_bound = np.exp(bbv * rrv) / 4
chk("(5c) superseded bound e^{b rho}/4 violated at b=0.7 rho=40 x=pi "
    "(exact 2 sinh(14)=%.4e < e^{28}/4=%.4e)" % (exact_worst, old_bound),
    exact_worst < old_bound and abs(exact_worst - new_bound) < 1e-9 * new_bound)

print("OVERALL:", "ALL CHECKS PASS" if ok else "FAILURES PRESENT")
