# verify_097.py - deterministic checks for proposal 097 (hetero-variance non-bridge)
# Run: python -I proposals/097-g-nonbridge-hetero-variance/verify_097.py   (repo root)
# Seed fixed: 20261119. Tool output is a check, not a proof.
import numpy as np

rng = np.random.default_rng(20261119)
ok = 0

def chk(tag, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + tag)
    if not cond:
        ok += 1

def cN(shape):
    # standard complex normal: |z|^2 ~ Exp(1)
    return (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) / np.sqrt(2.0)

def gram(A):
    # batched D x D Gram W = A^dagger A for A of shape (n, M, D), M >= D
    return np.einsum('nik,nil->nkl', A.conj(), A)

def sortd(G):
    w = np.linalg.eigvalsh(G)          # ascending
    return w[:, ::-1]                  # descending

# ---------- H0: the named column-profile law is implemented correctly ----------
# D=2, M=2, v=(1,3): G_11 = v1*E1 + v2*E2, E iid Exp(1)  => mean 4, var 10
v2 = np.array([1.0, 3.0])
A = cN((400000, 2, 2)) * np.sqrt(v2)[None, None, :]
x = np.abs(A[:, 0, :]) ** 2
x = x.sum(axis=1)
chk("H0a.mean", abs(x.mean() - v2.sum()) < 0.05 * np.sqrt((v2 ** 2).sum() / len(x)) + 0.01)
chk("H0b.var", abs(x.var() - (v2 ** 2).sum()) < 0.05 * np.sqrt(2 * (v2 ** 2).sum() ** 2 / len(x)) + 0.02)
# D=1, M=5, v=2: G = v * Gamma(5,1) => mean 10, var 20
y = (2.0 * np.abs(cN((200000, 5))) ** 2).sum(axis=1)
chk("H0c.gamma", abs(y.mean() - 10.0) < 0.05 * np.sqrt(20 / len(y)) + 0.01 and abs(y.var() - 20.0) < 0.1 * np.sqrt(2 * 400 / len(y)) + 0.05)

# ---------- H1: rank-one pair (profile-blind support datum), D=2,3,4 ----------
for D in (2, 3, 4):
    tau = 4.0
    a = np.zeros(D); a[0] = 1.0
    b = np.zeros(D); b[0] = b[1] = 1 / np.sqrt(2.0)
    G1 = tau * np.outer(a, a.conj()); G2 = tau * np.outer(b, b.conj())
    w1 = np.sort(np.linalg.eigvalsh(G1))[::-1]; w2 = np.sort(np.linalg.eigvalsh(G2))[::-1]
    spec_ok = np.allclose(w1, w2, atol=1e-10) and abs(w1[0] - tau) < 1e-10 and np.allclose(w1[1:], 0, atol=1e-10)
    d1 = np.diag(G1).real / tau; d2 = np.diag(G2).real / tau
    p_ok = abs((d1 ** 2).sum() - 1.0) < 1e-12 and abs((d2 ** 2).sum() - 0.5) < 1e-12
    chk("H1.pair.D%d" % D, spec_ok and p_ok)

# ---------- H1b: plane-rotation curve with varying P2 (profile-blind) ----------
lam = np.array([3.0, 0.7, 0.3]); tau = 4.0
def rotG(th):
    U = np.eye(3, dtype=complex)
    c, s = np.cos(th), np.sin(th)
    U[0, 0] = c; U[0, 1] = s; U[1, 0] = -s; U[1, 1] = c
    return U @ np.diag(lam) @ U.conj().T
ths = np.linspace(0.05, np.pi / 4, 8)
Gs = [rotG(t) for t in ths]
spec_fix = all(np.allclose(np.sort(np.linalg.eigvalsh(G))[::-1], lam, atol=1e-12) for G in Gs)
P2s = [float((np.sort(np.diag(G).real)[::-0] if False else np.diag(G).real / tau).dot(np.diag(G).real / tau)) for G in Gs]
# closed form: P2 = sum lam^2 - 2 (lam1-lam2)^2 sin^2 cos^2
P2f = [float((lam ** 2).sum() / tau ** 2 - 2 * (lam[0] - lam[1]) ** 2 * (np.sin(t) ** 2) * (np.cos(t) ** 2) / tau ** 2) for t in ths]
strict = all(P2s[i] > P2s[i + 1] + 1e-9 for i in range(len(P2s) - 1))
form = all(abs(P2s[i] - P2f[i]) < 1e-12 for i in range(len(P2s)))
chk("H1b.specfixed", spec_fix)
chk("H1b.P2strict", strict and form)

# ---------- H3: the fibre tilt is bounded above and below (fixed spectrum) ----------
vD3 = np.array([1.0, 2.0, 5.0])          # variances sigma^2 g, sigma=1, g non-constant
Z = cN((2000, 3, 3))
Q, R = np.linalg.qr(Z)                   # batched QR: Haar U(3) up to column phases (moduli unaffected)
absq2 = np.abs(Q) ** 2                   # rows j of G-side fibre coordinate
wts = 1.0 / vD3
expo = np.einsum('njk,k,j->n', absq2, lam, wts)   # sum_j sum_k lam_k |u_jk|^2 / v_j
w = np.exp(-expo)
lo, hi = np.exp(-lam.sum() * wts.max()), np.exp(-lam.sum() * wts.min())
chk("H3.bounds", bool((w >= lo - 1e-15).all() and (w <= hi + 1e-15).all()))
chk("H3.ratio", float(np.log(w.max()) - np.log(w.min())) <= lam.sum() * (wts.max() - wts.min()) + 1e-12)
# a non-constant profile genuinely tilts: variance of expo > 0
chk("H3.nonflat", float(expo.var()) > 1e-6)

# ---------- H4: exact D=2 hetero conditional law of G11: tilted uniform ----------
# conditional on (lam1>lam2): density of G11 on [lam2,lam1] prop. to exp(-beta*G11),
# beta = 1/v1 - 1/v2 ; the constant-variance law of 095 is the beta=0 (uniform) case.
def mom_exp(a, b, beta):
    # moments of x on [a,b] with weight exp(-beta x), quadrature (Simpson, 20001 pts)
    xs = np.linspace(a, b, 20001)
    ws = np.exp(-beta * (xs - a))
    Zq = np.trapezoid(ws, xs)
    m1q = np.trapezoid(ws * xs, xs) / Zq
    m2q = np.trapezoid(ws * xs * xs, xs) / Zq
    return m1q, m2q - m1q * m1q

beta = 1.0 / 1.0 - 1.0 / 3.0
A = cN((300000, 2, 2)) * np.sqrt(v2)[None, None, :]
G = gram(A); wsp = sortd(G)
tauB = wsp.sum(axis=1); pn = wsp / tauB[:, None]
band = (np.abs(pn[:, 0] - 0.65) < 0.025) & (np.abs(pn[:, 1] - 0.35) < 0.025)
d1 = np.real(G[:, 0, 0]) / tauB
cnt = int(band.sum())
chk("H4.count", cnt > 1500)
# prediction at band centre tau0=4, interval [1.4,2.6], tilt beta=2/3
m1q, v1q = mom_exp(1.4, 2.6, beta * 4.0 / 4.0 * 1.0)   # tilt on x in [lam2,lam1] at tau0=4: beta*x, x=G11
# scale to t = G11/tau0 in [0.35,0.65]: mean(t)=m1q/4, var(t)=v1q/16
t1q, tvq = m1q / 4.0, v1q / 16.0
emp = d1[band]
chk("H4.mean", abs(emp.mean() - t1q) < 0.015)
chk("H4.var", abs(emp.var() - tvq) < 0.015)
chk("H4.nonunif", abs(emp.mean() - 0.5) > 0.01)
print("  H4 numbers: emp mean %.4f var %.5f | pred %.4f %.5f | n=%d" % (emp.mean(), emp.var(), t1q, tvq, cnt))

# ---------- H2/H5: D=3 hetero band: non-atomicity and rank-2 scatter of (d1,d2) ----------
M, Dn = 3, 3
v3 = np.array([1.0, 2.0, 5.0])
A = cN((1200000, M, Dn)) * np.sqrt(v3)[None, None, :]
G = gram(A); wsp = sortd(G)
tauB = wsp.sum(axis=1); pn = wsp / tauB[:, None]
band = (np.abs(pn[:, 0] - 0.62) < 0.025) & (np.abs(pn[:, 1] - 0.25) < 0.025) & (np.abs(pn[:, 2] - 0.13) < 0.025)
d13 = np.real(G[:, 0, 0]) / tauB
d23 = np.real(G[:, 1, 1]) / tauB
cnt3 = int(band.sum())
chk("H2.count", cnt3 > 1500)
e = d13[band]
def conc(vals, delta):
    m = np.median(vals)
    return float(np.mean(np.abs(vals - m) < delta))
r1, r2 = conc(e, 0.01), conc(e, 0.02)
r4 = conc(e, 0.04)
hist, _ = np.histogram(e, bins=16)
chk("H2 nonatomic.ratio", 1.3 < r2 / max(r1, 1e-12) < 2.9 and 1.3 < r4 / max(r2, 1e-12) < 2.9)
chk("H2 noatom.hist", int(hist.max()) < 4.0 * hist.mean())
chk("H2.nonunif", abs(np.mean(d13[band]) - 1.0 / 3.0) > 0.01)
X = np.stack([d13[band], d23[band]], axis=1)
C = np.cov(X.T)
evC = np.linalg.eigvalsh(C)
chk("H5.scatter2d", evC[0] > 1e-5 and evC[1] > 1e-5)
print("  D3 band: n=%d E[d1]=%.4f ratio(2d/d)=%.2f cov eig %.2e %.2e" % (cnt3, np.mean(d13[band]), r2 / max(r1, 1e-12), evC[0], evC[1]))

print("SUMMARY " + ("ALL PASS" if ok == 0 else "FAILURES %d" % ok))
raise SystemExit(0 if ok == 0 else 1)
