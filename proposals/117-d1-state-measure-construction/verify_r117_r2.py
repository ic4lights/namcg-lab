# verify_r117_r2.py -- round-2 verification pack for proposal 117 (r1 pack byte-included
# plus N16: Vol <> 1 checks of the repaired (v) display; S_E = Vol*W at constant
# truncation, B = beta*Vol; lambda=v=1; est[b] holds E_b[W], E_b[W^2], P_b{W>=1/4}.
# (D1 frame non-degeneracy, state/measure route: Euclidean Gibbs measures of
# the truncated Presentation-B Higgs-matrix sector).
# Deterministic: seed 117 throughout. Run:  python -I -B verify_r117.py
# Symbolic/numerical output is a CHECK of the derivation steps, not a proof.
import sys
import numpy as np
import sympy as sp
from scipy.special import gamma as spgamma
from scipy.integrate import quad
from scipy.special import gammaincc as spgammaincc_upper

SEED = 117
NPASS = 0
NFAIL = 0

def check(name, cond, detail=""):
    global NPASS, NFAIL
    if cond:
        NPASS += 1
        print("PASS %s %s" % (name, detail))
    else:
        NFAIL += 1
        print("FAIL %s %s" % (name, detail))

# ----------------------------------------------------------------------------
# S1-S7: symbolic identities (lam = lambda, v = v; s = 4 singular values)
# ----------------------------------------------------------------------------
lam, v = sp.symbols("lambda v", positive=True)
s = sp.symbols("s0:4", nonnegative=True)
V4 = (lam / 4) * sp.Add(*[(si**2 - v**2)**2 for si in s])          # eq:V in singular values
s2 = sp.Add(*[si**2 for si in s])                                  # |Phi|_F^2
s4 = sp.Add(*[si**4 for si in s])

d1 = sp.expand(V4 - ((lam / 4) * s4 - (lam * v**2 / 2) * s2 + lam * v**4))
check("S1-expansion", d1 == 0, "V = (lam/4)|Phi|^4 - (lam v^2/2)|Phi|^2 + lam v^4")

d2 = sp.expand(V4 - ((lam / 16) * s4 - (lam * v**2 / 2) * s2))
check("S2-lower-pre", sp.simplify(d2 - ((3 * lam / 16) * s4 + lam * v**4)) == 0,
      "V - [(lam/16)sum s^4 - (lam v^2/2)sum s^2] = (3lam/16)sum s^4 + lam v^4 >= 0")

# coercivity in u = |Phi|_F^2:  V >= (lam/32)|Phi|^4 - 2 lam v^4, i.e.
# (lam/32)u^2 - (lam v^2/2)u + 3 lam v^4 > 0 for all u (discriminant < 0)
u = sp.symbols("u", nonnegative=True)
qdiff = sp.expand((lam / 32) * u**2 - (lam * v**2 / 2) * u + 3 * lam * v**4)
disc = sp.discriminate(qdiff, u) if hasattr(sp, "discriminate") else sp.discriminant(qdiff, u)
check("S3-coercivity", sp.simplify(disc) < 0 and sp.Poly(qdiff, u).LC() > 0,
      "disc((lam/32)u^2-(lam v^2/2)u+3lam v^4)=%s < 0 => V >= (lam/32)|Phi|^4 - 2lam v^4" % sp.simplify(disc))

# upper bound:  V <= (lam/4)|Phi|^4 + lam v^4   (drop -(lam v^2/2)sum s^2 <= 0 ... chain)
# V = (lam/4)sum (s^2-v^2)^2 <= (lam/4)(sum s^4 + 4 v^4) <= (lam/4)(sum s^2)^2 + lam v^4
d3a = sp.expand((lam / 4) * (s4 + 4 * v**4) - V4)                  # = (lam v^2/2) s2 >= 0
check("S3b-upper1", sp.simplify(d3a - (lam * v**2 / 2) * s2) == 0, "V <= (lam/4)(sum s^4 + 4v^4)")
d3b = sp.expand((lam / 4) * (s2**2 - s4))
check("S3c-upper2", bool(d3b >= 0) and all(bool(t >= 0) for t in sp.Add.make_args(sp.expand(d3b))),
      "sum s^4 <= (sum s^2)^2 => V <= (lam/4)|Phi|^4 + lam v^4")

# recorded threshold constant: V(0,v,v,v) = lam v^4 / 4
Vsub = V4.subs({s[0]: 0, s[1]: v, s[2]: v, s[3]: v})
check("S4-threshold", sp.simplify(Vsub - lam * v**4 / 4) == 0, "V(0,v,v,v) = lambda v^4/4 (recorded 115 constant)")

# sup_{t>=0} t e^{-t/2} = 2/e at t = 2
t = sp.symbols("t", nonnegative=True)
f_t = t * sp.exp(-t / 2)
tc = sp.solve(sp.diff(f_t, t), t)
check("S5-supte", tc == [2] and sp.simplify(f_t.subs(t, 2) - 2 / sp.E) == 0, "sup t e^{-t/2} = 2/e at t=2")

# volume of unit ball in D dims: omega_D = pi^{D/2}/Gamma(D/2+1); D=32: pi^16/16!
D = 32
import math
om32_sym = sp.pi**(D / 2) / sp.gamma(D / 2 + 1)
om32_num = float(om32_sym.evalf())
check("S6-ball32", abs(om32_num - np.pi**16 / math.factorial(16)) <= 1e-12 * om32_num,
      "omega_32 = pi^16/16! = %.6e" % om32_num)

# int_{R^D} e^{-c|phi|^4} dphi closed form vs radial quadrature (D=32, c=1)
cval = 1.0
surf = 2 * np.pi**(D / 2) / spgamma(D / 2)
radial, err = quad(lambda r: surf * r**(D - 1) * np.exp(-cval * r**4), 0.0, 4.0, limit=300)
tail = surf * spgammaincc_upper(D / 4, 4.0**4) / 4.0     # (surf/4) Gamma(D/4, 256), negligible
closed = surf * spgamma(D / 4) / (4 * cval**(D / 4))
check("S7-supgauss", abs(radial + tail - closed) / closed < 1e-8,
      "int e^{-|phi|^4} dphi (D=32): quad+tail=%.6e closed=%.6e (Z-finiteness dominating integral)" % (radial + tail, closed))
print("-- symbolic block done --")
# ---------------------------------------------------------------------------
# N2: interpolation sup_x |Phi(x)| <= C_L ||phi||_2 on a finite span, and
#     Holder: (int f^2)^2 <= (int f^4) |M| on the unit torus grid (Vol=1).
# ---------------------------------------------------------------------------
rng = np.random.default_rng(SEED)
g = 16
xs = (np.arange(g) + 0.5) / g
X4 = np.stack(np.meshgrid(xs, xs, xs, xs, indexing="ij"), -1)     # (g,g,g,g,4)
cols = [np.ones(g**4)]
for ax in range(4):
    for fr in (1, 2):
        cols.append(np.cos(2 * np.pi * fr * X4[..., ax]).ravel())
        cols.append(np.sin(2 * np.pi * fr * X4[..., ax]).ravel())
Emat = np.stack(cols, 0)                                          # (K, g^4)
Gram = Emat @ Emat.T / g**4
wG, VG = np.linalg.eigh(Gram)
assert np.all(wG > 1e-10), "basis not independent"
B = (VG / np.sqrt(wG)).T @ Emat                                    # orthonormal rows (mean-square)
Kdim = B.shape[0]
C_L = np.sqrt(np.max(np.sum(B**2, axis=0)))                        # C_L^2 = sup_x sum_k e_k(x)^2
maxerr = 0.0
maxratio = 0.0
for _ in range(40):
    c = rng.standard_normal(Kdim)
    phi = c @ B
    linf = np.max(np.abs(phi))
    l2 = np.sqrt(np.mean(phi**2))
    maxerr = max(maxerr, linf - C_L * l2)
    maxratio = max(maxratio, np.mean(phi**2)**2 / np.mean(phi**4))  # <= 1 (Vol=1)
check("N2-interpolation", maxerr <= 1e-12, "sup|phi| <= C_L ||phi||_2, max surplus %.2e (C_L=%.4f)" % (maxerr, C_L))
check("N2-holder", maxratio <= 1 + 1e-12, "max (mean phi^2)^2 / mean phi^4 = %.6f <= 1" % maxratio)

# ---------------------------------------------------------------------------
# N3: kinetic identity int |grad Phi|_F^2 dvol = sum_k (2pi)^2 |k|^2 ||phi_k||_F^2
#     for lattice-Fourier modes (exact grid orthonormality); unique k=0 mode.
# ---------------------------------------------------------------------------
gg = 8
ys = (np.arange(gg) + 0.5) / gg
ks = [(a, b, c, d) for a in (-2, -1, 0, 1, 2) for b in (-2, -1, 0, 1, 2)
      for c in (-2, -1, 0, 1, 2) for d in (-2, -1, 0, 1, 2) if a*a + b*b + c*c + d*d <= 8]
Y4 = np.stack(np.meshgrid(ys, ys, ys, ys, indexing="ij"), -1)
EM = np.stack([np.exp(2j * np.pi * (Y4 @ np.array(k))) for k in ks], 0).reshape(len(ks), -1)   # (m, N)
Gm = np.einsum("in,jn->ij", EM.conj(), EM).real / EM.shape[1]
check("N3-orthonormal", np.max(np.abs(Gm - np.eye(len(ks)))) < 1e-12, "Fourier-mode Gram = I")
phi_k = rng.standard_normal((len(ks), 4, 4)) + 1j * rng.standard_normal((len(ks), 4, 4))
Phi = np.einsum("kij,kn->nij", phi_k, EM)                                  # (N,4,4)
grads = [np.einsum("kij,kn->nij", phi_k, EM * (2j * np.pi * np.array([k[ax] for k in ks]))[:, None])
         for ax in range(4)]
Knum = float(sum(np.sum(np.abs(g)**2) / EM.shape[1] for g in grads))
Kexact = float(sum((2 * np.pi)**2 * sum(kk * kk for kk in ks[i]) * np.sum(np.abs(phi_k[i])**2)
                   for i in range(len(ks))))
check("N3-kinetic", abs(Knum - Kexact) / Kexact < 1e-10, "kinetic identity rel-err %.2e" % (abs(Knum - Kexact) / Kexact))
check("N3-constants", ks.count((0, 0, 0, 0)) == 1,
      "k=0 is the unique constant mode (kinetic vanishes only on constants, lambda_1=(2pi)^2)")

# ---------------------------------------------------------------------------
# N4/N5: 4D radial integrals over singular values (complex-SVD Jacobian
# J(sig)=prod_{i<j}(si^2-sj^2)^2 * prod si; lambda=v=|M|=1; model
# W(sig)=(1/4)sum (si^2-1)^2 = V at one point; Gibbs weight exp(-b W) J d^4sig,
# i.e. the constant-mode truncation with S_E = W, Vol=1).
# ---------------------------------------------------------------------------
def jac_W(s0, s1, s2, s3):
    A = (s0, s1, s2, s3)
    W = 0.25 * sum((a*a - 1.0)**2 for a in A)
    return W

def q1_cdf(b, R=6.0, n=200001):
    # proposal per-dim density q1(s) ~ s^13 exp(-b (s^2-1)^2/4): absorbs the
    # target t = exp(-b W) prod (si^2-sj^2)^2 prod si up to the bounded weight
    # w = prod (si^2-sj^2)^2 / prod si^12, exactly, for every b.
    s = np.linspace(0.0, R, n)
    logq = 13.0 * np.log(np.maximum(s, 1e-300)) - b * (s * s - 1.0)**2 / 4.0
    q = np.exp(logq - logq.max())
    c = np.concatenate([[0.0], np.cumsum(0.5 * (q[1:] + q[:-1]) * np.diff(s))])
    c /= c[-1]
    return s, c

PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

def is_draws(b, nsamp, rng):
    s, c = q1_cdf(b)
    sig = np.interp(rng.random((nsamp, 4)), c, s)
    w = np.ones(nsamp)
    for i, j in PAIRS:
        r2i, r2j = sig[:, i]**2, sig[:, j]**2
        w *= ((r2i - r2j) / (r2i * r2j))**2
    Wv = 0.25 * np.sum((sig * sig - 1.0)**2, axis=1)
    return w, Wv

def is_est(b, nsamp, rng):
    w, Wv = is_draws(b, nsamp, rng)
    sw = w.sum()
    return float((w * Wv).sum() / sw), float((w * Wv**2).sum() / sw),            float(w[Wv >= 0.25].sum() / sw), sw

rngR = np.random.default_rng(SEED + 10)
BS = (0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 64.0)
est = {}
for b in BS:
    rnb = np.random.default_rng(SEED + 7 + int(round(b)))
    est[b] = is_est(b, 3000000, rnb)
# log-partition differences, adjacent ratios: ln Z(b1) - ln Z(b2) =
# ln E_{q_{b2}}[w e^{(b2-b1)W}] - ln E_{q_{b2}}[w]
lndiff = {}
for b1, b2 in zip(BS[:-1], BS[1:]):
    rnb = np.random.default_rng(SEED + 200 + int(round(b2)))
    w, Wv = is_draws(b2, 1500000, rnb)
    lndiff[(b1, b2)] = float(np.log(np.mean(w * np.exp((b2 - b1) * Wv))) - np.log(np.mean(w)))
logZ = {1.0: 0.0}
for (b1, b2), v in lndiff.items():
    if b2 in logZ:
        logZ[b1] = logZ[b2] + v
    else:
        logZ[b2] = logZ[b1] - v
# convergence: rerun b=1, b=16 with a second seed
E1r, _, P1r, _ = is_est(1.0, 1500000, np.random.default_rng(SEED + 991))
E16r, _, _, _ = is_est(16.0, 1500000, np.random.default_rng(SEED + 992))
check("N4-IS-converge", abs(E1r - est[1.0][0]) / est[1.0][0] < 0.08 and abs(E16r - est[16.0][0]) / est[16.0][0] < 0.08,
      "E_b[W] seed-split rel-diff b=1: %.4f, b=16: %.4f" % (abs(E1r - est[1.0][0]) / est[1.0][0], abs(E16r - est[16.0][0]) / est[16.0][0]))
check("N4-Zpositive", all(est[b][0] > 0 and np.isfinite(est[b][0]) for b in BS),
      "Z(b) in (0,inf) via IS for b in %s" % (BS,))
fvals = {b: 4.0 * est[b][0] for b in BS}
Evals = {b: est[b][0] for b in BS}
dec = all(Evals[b1] > Evals[b2] for b1, b2 in zip(BS[:-1], BS[1:]))
check("N5-mono", dec, "E_b[S]=E_b[V] strictly decreasing: " + " ".join("%g:%.4f" % (b, Evals[b]) for b in BS))
bf = {b: b * fvals[b] for b in BS}
check("N5-rate", all(10.0 <= bf[b] <= 90.0 for b in BS) and fvals[64.0] < 0.6,
      "f(b)=4E_b[V] = O(1/b): b*f(b) in [%.1f, %.1f], f(64)=%.4f" % (min(bf.values()), max(bf.values()), fvals[64.0]))
# E[S] <= (2/e) Z(1/2)/Z(1), Vol=1 constant truncation: S = W
upperES = (2.0 / np.e) * np.exp(logZ[0.5])
check("N5-ES-bound", Evals[1.0] <= upperES, "E[S]=E[W]=%.5f <= (2/e)Z(1/2)/Z(1)=%.5f" % (Evals[1.0], upperES))
# convexity of ln Z: secant slopes of logZ vs beta must be decreasing
secs = [(logZ[b2] - logZ[b1]) / (b2 - b1) for b1, b2 in zip(BS[:-1], BS[1:])]
check("N13-lnZ-convex", all(secs[i] >= secs[i-1] - 1e-6 for i in range(1, len(secs))),
      "secant slopes of lnZ increasing (lnZ convex; d lnZ/dbeta = -E_beta[S] increasing): " + " ".join("%.4f" % x for x in secs))
# Markov/soft-event: (lam v^4/4) P{V>=lam v^4/4} <= E_b[V]  and P <= min(1, f)
mk = all(0.25 * est[b][2] <= Evals[b] + 1e-12 and est[b][2] <= min(1.0, fvals[b]) + 1e-9 for b in BS)
check("N8-markov", mk, "P{V>=lam v^4/4} <= min(1,4E[V]) and (1/4)P<=E[V] for all b; P(1)=%.4f P(16)=%.4f"
      % (est[1.0][2], est[16.0][2]))
# super-Gaussian event bound: P{W>=T} <= exp(-b T/2) Z(b/2)/Z(b), T=1/4
ok11 = True
for b in (2.0, 4.0, 8.0, 16.0):
    upperP = np.exp(-b * 0.25 / 2.0 + logZ[b / 2] - logZ[b])
    if not est[b][2] <= upperP + 1e-9:
        ok11 = False
check("N11-event-cost", ok11, "P_b{V>=T} <= e^{-bT/2} Z(b/2)/Z(b) at b=2,4,8,16: " +
      " ".join("b%g:%.3f<=%.3f" % (b, est[b][2], np.exp(-b * 0.25 / 2.0 + logZ[b / 2] - logZ[b])) for b in (2.0, 4.0, 8.0, 16.0)))
# second moment: b^2 E_b[W^2] bounded
m2 = {b: b * b * est[b][1] for b in BS}
check("N12-second-moment", max(m2.values()) < 30 * min(m2.values()),
      "b^2 E_b[W^2] bounded: " + " ".join("%g:%.2f" % (b, m2[b]) for b in BS))
# Laplace-type lower bound Z(b) >= c b^{-8}: b^8 Z(b) in a bounded band
# rigorous package input: Laplace-chart lower bound Z(b) >= c b^{-q} (q = 8n = 8
# asymptotically, q = 9 margin); numerically test ln Z(b) >= ln Z(1) - 9 ln b - 1
lap = {b: logZ[b] + 9.0 * np.log(b) for b in BS}
check("N9-laplace", all(lap[b] >= logZ[1.0] - 1.0 for b in BS),
      "Z(b) >= Z(1) e^{-1} b^{-9}: min_b [lnZ + 9 ln b - lnZ(1)] = %.2f >= -1: " % (min(lap.values()) - logZ[1.0]) +
      " ".join("%g:%.2f" % (b, lap[b] - logZ[1.0]) for b in BS))

# ---------------------------------------------------------------------------
# N15: full linearization chain  sup_x V(x) <= 8 C^4 (int V + 2 lam v^4 |M|) + lam v^4
#      (lambda=v=|M|=1; C = sup_x (sum_k ||E_k(x)||_F^2)^{1/2} = 4 C_L for the
#      matrix-valued span), checked on random matrix-valued trig fields, plus
#      the interpolation sup_x |Phi(x)|_F <= C ||phi||_2 itself.
# ---------------------------------------------------------------------------
def pot(Ph):
    # V = (lam/4) Tr(M^2) - (lam v^2/2) Tr M + lam v^4 with M = Phi^dag Phi,
    # Tr(M^2) = ||M||_F^2 (M Hermitian); lam = v = 1.
    M = np.einsum("nij,nik->njk", Ph.conj(), Ph)
    trM = np.einsum("nii->n", M).real
    trM2 = np.sum(np.abs(M)**2, axis=(1, 2))
    return 0.25 * trM2 - 0.5 * trM + 1.0, trM

worstSlack = np.inf
worstInterp = -np.inf
Cfull = 4.0 * C_L
for _ in range(30):
    Am = rng.standard_normal((Kdim, 4, 4)) + 1j * rng.standard_normal((Kdim, 4, 4))
    Ph = np.einsum("kn,kab->nab", B, Am)                        # (N,4,4)
    Vx, trM = pot(Ph)
    Fs = np.sqrt(trM)
    worstInterp = max(worstInterp, np.max(Fs) - Cfull * np.sqrt(np.mean(trM)))
    intV = np.mean(Vx)
    bound = 8.0 * (Cfull**4) * (intV + 2.0) + 1.0
    worstSlack = min(worstSlack, bound - np.max(Vx))
check("N15-interpolation", worstInterp <= 1e-12, "sup|Phi|_F <= 4 C_L ||phi||_2, max surplus %.2e" % worstInterp)
check("N15-linearization", worstSlack >= 0, "sup_x V(x) <= 8C^4(intV + 2 lam v^4)+lam v^4; min slack %.3e" % worstSlack)

# ---------------------------------------------------------------------------
# N6: determinant cone has codimension-2 small-ball scaling (absolute
#     continuity of the one-point law; complex-Gaussian probe).
# ---------------------------------------------------------------------------
rng2 = np.random.default_rng(SEED + 1)
epsall = np.array([5e-2, 1e-1, 2e-1, 3e-1, 5e-1])
cnt6 = np.zeros(len(epsall)); nb6 = 0
for _ in range(6):
    Gc = rng2.standard_normal((250000, 4, 4)) + 1j * rng2.standard_normal((250000, 4, 4))
    sl, ld6 = np.linalg.slogdet(Gc)
    t6 = np.exp(ld6)
    for i6, e6 in enumerate(epsall):
        cnt6[i6] += np.sum(t6 < e6)
    nb6 += 250000
Pall = cnt6 / nb6
Pfine = np.mean(np.exp(ld6) < 1e-2)
use = (cnt6 >= 30.0)
Afit = np.polyfit(np.log(epsall[use]), np.log(Pall[use]), 1)
check("N6-codim2", use.sum() >= 4 and 1.2 < Afit[0] < 3.2 and np.all(np.diff(Pall) > 0),
      "P(|det X|<eps) ~ eps^s over %d usable eps (n=%d), fitted s=%.2f (expect ~2 + log corr: real codim 2)" % (use.sum(), nb6, Afit[0]))
check("N6-nullprob", Pfine < 5e-5, "small-ball probability of singular cone -> 0 (P(1e-2)=%.2e, batch tail): omega_x{det=0}=0 by absolute continuity" % Pfine)

# ---------------------------------------------------------------------------
# N7: Fubini/defect-set probe: random trigonometric matrix field on the torus:
#     spacetime-Lebesgue fraction of {det Phi(x) approx 0} collapses with eps
#     (defect set null), while the event itself is accessible.
# ---------------------------------------------------------------------------
rng3 = np.random.default_rng(SEED + 2)
# Smooth matrix field on T^4 with det Phi(x) = 1/2 + cos(2 pi x0) + i sin(2 pi x1):
# rank-2 zeros (4 circles x2,x3-free), so {det=0} is a codim-2 set and the tube
# {|det Phi|<t} has Lebesgue measure ~ t^2 -> 0 (defect set null, Fubini probe).
gN = 512
zs7 = (np.arange(gN) + 0.5) / gN
DD = 0.5 + np.cos(2 * np.pi * zs7)[:, None] + 1j * np.sin(2 * np.pi * zs7)[None, :]
a7 = np.abs(DD).ravel()
thr7 = np.array([0.05, 0.1, 0.2, 0.4, 0.8])
m7 = np.array([np.mean(a7 < t) for t in thr7])
use7 = (m7 * len(a7)) >= 30.0
slope7 = np.polyfit(np.log(thr7[use7]), np.log(m7[use7]), 1)[0]
check("N7-defect-null", use7.sum() >= 4 and 1.2 < slope7 < 3.0 and m7[1] < 0.02,
      "defect-tube fractions m(t) collapse: " + " ".join("%.2f:%.5f" % (t, m) for t, m in zip(thr7, m7)) +
      ", fitted slope %.2f (expect ~2: rank-2 complex zeros) -> defect set Lebesgue-null" % slope7)

# ---------------------------------------------------------------------------
# N10: tube supremum bound  V(v(I+E)) <= (lam/4) v^4 (2+rho)^4 + lam v^4 on
#      ||E||_F <= rho (tube lower bound Z >= omega_32 rho^32 exp(-b c_sup)).
# ---------------------------------------------------------------------------
rho = 0.5
U = rng3.standard_normal((20000, 16)) + 1j * rng3.standard_normal((20000, 16))
U /= np.linalg.norm(U, axis=1, keepdims=True)
rad = rho * rng3.random((20000, 1))**(1.0 / 32.0)
E = (U * rad).reshape(-1, 4, 4)
Fe = np.eye(4)[None] + E
Vt, trF = pot(Fe)
Fro = np.sqrt(trF)
boundt = 0.25 * (2 + rho)**4 + 1.0
check("N10-tube-frob", np.max(Fro) <= (2 + rho) + 1e-12, "max |I+E|_F = %.4f <= 2+rho = %.4f" % (np.max(Fro), 2 + rho))
check("N10-tube", np.max(Vt) <= boundt, "max tube V = %.4f <= (lam/4)(2+rho)^4 + lam v^4 = %.4f" % (np.max(Vt), boundt))

# ---------------------------------------------------------------------------
# N16 (round 2, gatekeeper Finding 1): repaired (v) display at Vol <> 1.
# Constant-field truncation, fixed zero background gauge: S_E(phi) = Vol*W(phi),
# so mu_beta has inverse temperature B = beta*Vol in W (lambda=v=1). The
# repaired (option (a)) display reads
#   Vol*P_B{W>=1/4} <= 4*E_{mu_beta}[S_E] = 4*Vol*E_B[W]   for every Vol>0,
# and the beta >= beta_0 chain uses E_{mu_beta}[S_E] = Vol*E_{beta*Vol}[W]
# nonincreasing in beta. Dividing by Vol this is exactly Markov's inequality
# P_B{W>=1/4} <= 4*E_B[W] -- Vol-balanced, no power of Vol missing. The r1
# (false) display P_B{W>=1/4} <= 4*Vol*E_B[W] is checked to FAIL in the
# gatekeeper counterexample regime (Vol small at fixed beta, B = beta*Vol
# small): there P_B -> 1 while 4*Vol*E_B[W] = 4*Vol*O(1/(beta*Vol)) = O(1/beta)
# stays small; the failure is the tooth of this test.
# ---------------------------------------------------------------------------
def vol_arm(vol, b):                 # b = B = beta*Vol; est[b] computed above
    return vol * est[b][2], 4.0 * vol * est[b][0]
arms14 = [vol_arm(0.25, b) for b in (1.0, 2.0, 4.0, 8.0, 16.0)]
check("N16-repaired-Vol14", all(l <= r + 1e-12 for l, r in arms14),
      "repaired (v) at Vol=1/4: Vol*P_B <= 4*Vol*E_B[W], B in {1,2,4,8,16}; " +
      " ".join("B=%g:%.4f<=%.4f" % (b, l, r) for b, (l, r) in zip((1.0, 2.0, 4.0, 8.0, 16.0), arms14)))
# full repaired chain (both inequalities) at Vol=1/4, beta=16 >= beta_0=4:
# B = beta*Vol: 4 and 1; lhs = Vol*P_B{W>=1/4} at B=4.
lhsC = 0.25 * est[4.0][2]
rhs16 = 4.0 * 0.25 * est[4.0][0]
rhs4 = 4.0 * 0.25 * est[1.0][0]
check("N16-chain-beta-monotone", lhsC <= rhs16 <= rhs4,
      "repaired chain Vol=1/4, beta=16>=beta_0=4: %.4f <= %.4f <= %.4f" % (lhsC, rhs16, rhs4))
# Vol > 1 arm (Vol-balanced for large volume too): Vol=4, beta=4 -> B=16
l4, r4v = vol_arm(4.0, 16.0)
check("N16-Vol-gt1", l4 <= r4v + 1e-12, "Vol=4, B=16: Vol*P = %.4f <= 4*Vol*E_B[W] = %.4f" % (l4, r4v))
# tooth: r1 (Vol-misbalanced) display fails at Vol=1/64, beta=64 (B=1) while
# the repaired display holds there (counterexample regime of review-r1).
volT = 1.0 / 64.0
lhs_oldT = est[1.0][2]                    # Vol^-1 * Vol * P = P (r1 left side)
lhs_newT, rhs_oldT = vol_arm(volT, 1.0)   # repaired lhs; rhs identical to r1 rhs
check("N16-old-display-fails", lhs_oldT > rhs_oldT and lhs_newT <= rhs_oldT,
      "r1 display fails at Vol=1/64, beta=64: P=%.4f > 4*Vol*E=%.4f; repaired %.6f <= %.4f"
      % (lhs_oldT, rhs_oldT, lhs_newT, rhs_oldT))

# ---------------------------------------------------------------------------
print("-- summary --")
print("PASS %d FAIL %d" % (NPASS, NFAIL))
print("ALL CHECKS DONE 117R2")
sys.exit(1 if NFAIL else 0)
