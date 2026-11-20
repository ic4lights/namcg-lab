# verify_098.py - checks for the scalar P_2 fibre-interval non-bridge (item 098). Seed fixed. No writes.
# Run from repo root: python -I proposals/098-g-scalar-p2-nonbridge-d3/verify_098.py
import numpy as np
rng = np.random.default_rng(20261119)
ok = 0
def chk(tag, cond, info=""):
    global ok
    print(("PASS " if cond else "FAIL ") + tag + (" " + info if info else ""))
    if not cond:
        ok += 1

def gram(A):  # batched A^dagger A, A shape (n, M, D) -> (n, D, D)
    return np.einsum('nik,nil->nkl', A.conj(), A)

def haarU(n, D):  # n Haar-distributed D x D unitaries via phase-corrected QR
    Z = rng.standard_normal((n, D, D)) + 1j * rng.standard_normal((n, D, D))
    Q, R = np.linalg.qr(Z)
    d = np.diagonal(R, axis1=1, axis2=2)
    Q = Q * (d / np.abs(d))[:, None, :]
    return Q

def P2(G):
    t = np.real(np.trace(G, axis1=-2, axis2=-1))
    dg = np.real(np.diagonal(G, axis1=-2, axis2=-1))
    return (dg * dg).sum(-1) / t**2

def evals(G):
    return np.linalg.eigvalsh(G)[..., ::-1]  # descending

# V0 algebraic identity: tau^2*P2 = sum(lambda^2) - sum_{j!=k}|G_jk|^2
A = (rng.standard_normal((400, 5, 4)) + 1j * rng.standard_normal((400, 5, 4))) / np.sqrt(2)
G = gram(A); t = np.real(np.trace(G, axis1=-2, axis2=-1))
lam = evals(G)
off = (np.abs(G)**2).sum((-2, -1)) - (np.abs(np.diagonal(G, axis1=-2, axis2=-1))**2).sum(-1)
err0 = np.max(np.abs((P2(G) * t**2) - (lam**2).sum(-1) + off))
chk("V0 identity", err0 < 1e-9, "maxerr %.2e" % err0)
# V0b Cauchy bracket: 1/D <= P2 <= sum p^2
sps = (lam / t[..., None])**2
chk("V0b bracket", np.all(P2(G) >= 1/4 - 1e-12) and np.all(P2(G) <= sps.sum(-1) + 1e-12))
# V1 endpoint attainment on one orbit: lam=(3,1,0.2), D=3
lam0 = np.diag([3.0, 1.0, 0.2]); tau0 = 4.2
U = haarU(6000, 3)
Gor = np.einsum('nji,jk,nkl->nil', U.conj(), lam0, U)
p2v = P2(Gor)
chk("V1 diag endpoint", abs(P2(lam0[None]) [0] - (3**2+1+0.04)/tau0**2) < 1e-12,
    "%.10f" % P2(lam0[None])[0])
F = np.array([[np.exp(2j*np.pi*j*k/3) for k in range(3)] for j in range(3)]) / np.sqrt(3)
chk("V1 fourier moduli", np.max(np.abs(np.abs(F)**2 - 1/3)) < 1e-14)
Gf = F.conj().T @ lam0 @ F
chk("V1 uniform endpoint", abs(P2(Gf[None])[0] - 1/3) < 1e-12, "%.12f" % P2(Gf[None])[0])
chk("V1 orbit fills interval", abs(p2v.min() - 1/3) < 0.02 and abs(p2v.max() - (9+1+0.04)/17.64) < 0.02,
    "min %.5f max %.5f" % (p2v.min(), p2v.max()))
# V1b no atom: 40 equal bins on [1/3, sum p^2], max/mean < 4
hist, _ = np.histogram(p2v, bins=40, range=(1/3, (9+1+0.04)/17.64))
chk("V1b flat-ish density", hist.max() / hist.mean() < 4.0, "max/mean %.2f" % (hist.max()/hist.mean()))

# V2 derivative identity: d/dtheta P2-orbit at theta=0 equals 4 Re G012 (G011-G022)/(4 tau^2)... exact form:
# f(theta) = sum_j [R^dag G0 R]_jj^2 ; f'(0) = 4 Re(G0_12)(G0_11 - G0_22)
for trial in range(4):
    Uu = haarU(1, 3)[0]
    G0 = Uu.conj().T @ lam0 @ Uu
    th = 1e-5
    R = np.eye(3, dtype=complex); c, s = np.cos(th), np.sin(th)
    R[:2, :2] = [[c, -s], [s, c]]
    f = lambda RR: (np.real(np.diagonal(RR.conj().T @ G0 @ RR))**2).sum()
    fd = (f(R) - f(R.conj().T)) / (2 * th)
    an = 4 * np.real(G0[0, 1]) * (np.real(G0[0, 0]) - np.real(G0[1, 1]))
    chk("V2 derivative trial %d" % trial, abs(fd - an) < 1e-6, "fd %.8f an %.8f" % (fd, an))
# V3 hetero band conditioning, D=3: M=3, D=3, profile g=(1,2,5), sigma=1 (097 model)
M, DD = 3, 3
gpr = np.array([1.0, 2.0, 5.0])
N = 600000
A = (rng.standard_normal((N, M, DD)) + 1j * rng.standard_normal((N, M, DD))) / np.sqrt(2) * np.sqrt(gpr)
G = gram(A)
t = np.real(np.trace(G, axis1=-2, axis2=-1))
p = evals(G) / t[..., None]
band = (np.abs(p[:, 0] - 0.62) < 0.025) & (np.abs(p[:, 1] - 0.25) < 0.025)
nb = band.sum()
p2b = P2(G)[band]; ps2 = (p**2).sum(-1)[band]
chk("V3 band count", nb > 1500, "n=%d" % nb)
chk("V3 interval support", np.all(p2b >= 1/3 - 1e-9) and np.all(p2b <= ps2 + 1e-9))
hist3, _ = np.histogram(p2b, bins=30, range=(p2b.min(), p2b.max()))
chk("V3 no atom", hist3.max() / hist3.mean() < 6.0, "max/mean %.2f" % (hist3.max()/hist3.mean()))
# mass-per-width at the median halves scales: bounded above and below => no atom
am = np.median(p2b)
def mpw(h):
    return np.mean((p2b > am - h) & (p2b <= am + h)) / (2 * h)
w1, w2, w3 = mpw(0.02), mpw(0.005), mpw(0.00125)
chk("V3 mass-per-width bounded", 0.4 < w2 / w1 < 2.5 and 0.4 < w3 / w2 < 2.5,
    "w %.1f %.1f %.1f" % (w1, w2, w3))

# V4 D=2 hetero batched: P2 conditional on spectrum = pushforward of exp(-beta G11) via P2=2x^2-2x+1
M2, D2 = 4, 2
gpr2 = np.array([1.0, 2.0]); beta = 1 / 1.0 - 1 / 2.0  # sigma=1
acc = []
accx = []
for rep in range(20):
    A = (rng.standard_normal((375000, M2, D2)) + 1j * rng.standard_normal((375000, M2, D2))) / np.sqrt(2) * np.sqrt(gpr2)
    G = gram(A)
    t = np.real(np.trace(G, axis1=-2, axis2=-1))
    p = evals(G) / t[..., None]
    band2 = (np.abs(t - 4.0) < 0.3) & (np.abs(p[:, 0] - 0.65) < 0.012)
    x = np.real(G[:, 0, 0]) / t
    acc.append(2 * x[band2]**2 - 2 * x[band2] + 1)
    accx.append(x[band2])
p2b2 = np.concatenate(acc); nb2 = len(p2b2)
emp = p2b2.mean(); se = p2b2.std() / np.sqrt(nb2)
# quadrature prediction at band-center spectrum tau=4, lam=(2.6,1.4): x in [0.35,0.65]
xs = np.linspace(0.35, 0.65, 20001)
w = np.exp(-beta * (xs * 4.0))
pred = np.trapezoid(w * (2 * xs**2 - 2 * xs + 1), xs) / np.trapezoid(w, xs)
z = (emp - pred) / se
chk("V4 tilt scalar pred", nb2 > 1500 and abs(z) < 5.0, "n=%d emp %.5f pred %.5f z %.1f" % (nb2, emp, pred, z))
# V4b no atom and full support: 10 equal-width bins on the fibre interval image, each >= 5 counts
lo, hi = 0.5, 2 * 0.35**2 - 2 * 0.35 + 1
h2, _ = np.histogram(p2b2, bins=10, range=(lo, hi))
chk("V4b bins nonzero", h2.min() >= 5, "min count %d" % h2.min())
# V5 pair pin at D=2: given (tau, P2), the diagonal multiset is the two quadratic roots
x1 = np.concatenate(accx)[:2000]
tau1 = t[band2][:2000]
P2v = 2*x1**2 - 2*x1 + 1  # equals (d1^2+d2^2), d1+d2=1
disc = np.sqrt(np.maximum(2*P2v - 1, 0))
r1, r2 = (1 + disc)/2, (1 - disc)/2
dtrue = np.sort(np.stack([x1, 1-x1], -1))[:, ::-1]
rec = np.sort(np.stack([r1, r2], -1), -1)[:, ::-1]
chk("V5 pair pin", np.max(np.abs(dtrue - rec)) < 1e-12, "maxerr %.2e" % np.max(np.abs(dtrue-rec)))
# V6 two-angle patch: rank-2 diagonal map, and one P2 level set traced as a curve of distinct diagonals
def dpatch(lamv, c1, s1, c2, s2):
    l1, l2, l3 = lamv[:3]
    a = l1 * s1 * s1 + l2 * c1 * c1
    return (l1 * c1 * c1 + l2 * s1 * s1, a * c2 * c2 + l3 * s2 * s2, a * s2 * s2 + l3 * c2 * c2)

def v6_grads(lamv, th, ph, tau):
    c1, s1, c2, s2 = np.cos(th), np.sin(th), np.cos(ph), np.sin(ph)
    h = 1e-6
    ch, sh = np.cos(h), np.sin(h)
    d0 = dpatch(lamv, c1, s1, c2, s2)
    da = dpatch(lamv, c1 * ch - s1 * sh, s1 * ch + c1 * sh, c2, s2)
    db = dpatch(lamv, c1, s1, c2 * ch - s2 * sh, s2 * ch + c2 * sh)
    q0 = sum(d * d for d in d0)
    g0 = (sum(d * d for d in da) - q0) / h / tau**2
    g1 = (sum(d * d for d in db) - q0) / h / tau**2
    j00 = (da[0] - d0[0]) / h
    j01 = (da[1] - d0[1]) / h
    j10 = (db[0] - d0[0]) / h
    j11 = (db[1] - d0[1]) / h
    return q0 / tau**2, g0, g1, j00 * j11 - j01 * j10

def v6_case(lamv, tag, nd):
    th = np.linspace(0, 2 * np.pi, 900, endpoint=False)
    C1, C2 = np.meshgrid(np.cos(th), np.cos(th))
    S1, S2 = np.meshgrid(np.sin(th), np.sin(th))
    tau = float(sum(lamv))
    p2, g0, g1, detJ = v6_grads(lamv, C1, C2, tau)
    gmag = np.sqrt(g0 * g0 + g1 * g1)
    reg = (np.abs(detJ) > 1e-5) & (gmag > 1e-5)
    chk(tag + " rank2 region", reg.mean() > 0.15, "frac %.3f" % reg.mean())
    ipk = np.unravel_index(np.argmax(np.where(reg, np.minimum(np.abs(detJ), gmag), -1.0)), detJ.shape)
    t0, f0 = th[ipk[0]], th[ipk[1]]
    lev = p2[ipk]
    chk(tag + " interior level", p2.min() + 1e-6 < lev < p2.max() - 1e-6,
        "lev %.5f in [%.5f, %.5f]" % (lev, p2.min(), p2.max()))
    t, f = t0, f0
    steps, cols = [], []
    for k in range(400):
        p2k, g0k, g1k, _ = v6_grads(lamv, t, f, tau)
        nrm = np.hypot(g0k, g1k)
        tx, ty = g1k / nrm, -g0k / nrm
        t = t + 0.02 * tx
        f = f + 0.02 * ty
        for _ in range(3):
            p2c, g0c, g1c, _ = v6_grads(lamv, t, f, tau)
            g = g0c * g0c + g1c * g1c
            if g < 1e-12:
                break
            t = t - (p2c - lev) * g0c / g
            f = f - (p2c - lev) * g1c / g
        d = dpatch(lamv, np.cos(t), np.sin(t), np.cos(f), np.sin(f))
        row = list(d) + ([lamv[3]] if nd == 4 else [])
        cols.append(np.sort(row))
        steps.append((t, f))
    arr = np.stack(cols)
    dev = max(abs(v6_grads(lamv, t, f, tau)[0] - lev) for t, f in steps)
    for dl in (0.02, 0.008):
        keys = np.unique(np.round(arr / dl).astype(np.int64), axis=0)
        if dl == 0.02:
            n1 = len(keys)
        else:
            chk(tag + " level clusters", len(keys) >= 30 and len(keys) >= 1.5 * n1 and dev < 1e-6,
                "n 0.020 -> %d, n 0.008 -> %d, leveldev %.1e" % (n1, len(keys), dev))

v6_case((3.0, 1.0, 0.2), "V6 D3", 3)
v6_case((3.0, 1.0, 0.2, 0.7), "V6 D4", 4)
print("SUMMARY " + ("ALL PASS" if ok == 0 else "FAILURES %d" % ok))
raise SystemExit(0 if ok == 0 else 1)
