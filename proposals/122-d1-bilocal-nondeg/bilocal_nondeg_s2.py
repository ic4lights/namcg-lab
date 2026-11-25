# -*- coding: ascii -*-
# Item 122, script 2: transport classes and state reading for the bilocal
# composite M = Phi W Phi^dagger.
# T1: finite-N unitary transport (fuzzy Wilson line): sigma_min(T_M) >= c^2,
#     sigma_min(T_U) = 1, condition-number transfer; teeth: c -> 0 and a
#     singular nonunitary transport.
# T2: smooth-kernel compactness: full-space sigma_min collapses with grid
#     refinement while the fixed-band carrier sigma_min is grid-stable
#     (operator lower bound is a carrier property). Exact spectra via the
#     Fourier-diagonalized heat kernel TW = F D F^dag / n, D_k = exp(-s^2 k^2).
# T3: Haar/convexity tooth: E[M] of pointwise nondegenerate M is ~ 0.
# T4: diagonal composite: lambda_min(E[Q]) >= E[lambda_min(Q)] (Loewner) and
#     the Markov+threshold bound max_eps (v^2-2 sqrt(eps/lam))(1-EV/eps);
#     teeth: EV >= lam v^4/4 and double-collapsed bad fiber (E[lmin]=0).
# T5: transport bound sigma_min(Pexp) >= exp(-int sigma_max(omega));
#     anti-Hermitian integrand: sigma_min = 1; scalar gl path: equality.
# Deterministic: fixed seeds; numpy + scipy.linalg.expm.
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(1222)
fails = []

def chk(name, cond, detail=""):
    tag = "OK" if cond else "FAIL"
    if not cond:
        fails.append(name)
    print("%-48s %s %s" % (name, tag, detail))

def smin(A):
    return np.linalg.svd(A, compute_uv=False)[-1]

def smax(A):
    return np.linalg.svd(A, compute_uv=False)[0]

def rand_herm(d):
    H = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    return (H + H.conj().T) / 2

def rand_u(d):
    return expm(1j * rand_herm(d))

def phi_field(Nb, d, vlo, vhi):
    blocks = []
    for _ in range(Nb):
        sv = np.sort(rng.uniform(vlo, vhi, size=d))
        U = rand_u(d); V = rand_u(d)
        blocks.append((U * sv[None, :]) @ V.conj().T)
    M = np.zeros((Nb * d, Nb * d), dtype=complex)
    for i, B in enumerate(blocks):
        M[i*d:(i+1)*d, i*d:(i+1)*d] = B
    return M

print("== T1: unitary fuzzy transport ==")
ok1 = True; oku = True
for N in range(2, 9):
    v, dlt = 1.9, 0.6
    Phi = phi_field(N, 4, v - dlt, v + 0.3)
    U = np.kron(rand_u(N), np.eye(4))
    oku = oku and abs(smin(U) - 1.0) < 1e-9 and abs(smax(U) - 1.0) < 1e-9
    T = Phi @ U @ Phi.conj().T
    if smin(T) < (v - dlt)**2 - 1e-9:
        ok1 = False
    kT = smax(T) / smin(T)
    if kT > ((v + 0.3) / (v - dlt))**2 * (1 + 1e-9):
        ok1 = False
chk("T1 unitary W: smin >= (v-d)^2 and kappa bound", ok1, "N=2..8")
chk("T1 sigma_min(T_U) = 1 exactly", oku)
Phi = phi_field(4, 4, 1e-6, 1.9)
U = np.kron(rand_u(4), np.eye(4))
t = smin(Phi @ U @ Phi.conj().T)
chk("T1 TOOTH c->0 kills the bound (sharp)", t < 1e-2, "smin=%.2e" % t)
G = np.diag([1.0, 1.0, 1.0, 0.0])
Phi2 = phi_field(4, 4, 1.3, 1.9)
t2 = smin(Phi2 @ np.kron(G, np.eye(4)) @ Phi2.conj().T)
chk("T1 TOOTH singular W: smin(T_M)=0, Phi invertible", t2 < 1e-9, "smin=%.1e" % t2)

print("== T2: smooth-kernel compactness vs carrier stability ==")
s2p = 0.15
fulls = []; carrs = []
for n in (32, 64, 128, 256):
    ks = np.fft.fftfreq(n, d=1.0 / n)
    F = np.exp(2j * np.pi * np.outer(np.arange(n), np.arange(n)) / n)
    D = np.exp(-(s2p * ks)**2)
    TW = (F * D[None, :]) @ F.conj().T / n
    fulls.append(smin(TW))
    modes = [k % n for k in (-3, -2, -1, 0, 1, 2, 3)]
    P = F[:, modes] / np.sqrt(n)
    carrs.append(smin(P.conj().T @ TW @ P))
dec = all(fulls[i + 1] < fulls[i] * 1e-3 or fulls[i + 1] < 1e-16 for i in range(len(fulls) - 1)) and fulls[0] > 1e-4 and fulls[-1] < 1e-16
chk("T2 TOOTH full smin -> 0 (superexponential)", dec,
    " ".join("%.1e" % x for x in fulls))
chk("T2 carrier (|k|<=3) smin grid-stable", abs(carrs[-1] - carrs[1]) < 1e-6,
    "carrier=%.6f (exact e^{-.2*9}=%.6f)" % (carrs[-1], np.exp(-s2p**2 * 9)))

print("== T3: Haar/convexity tooth ==")
d = 4; v = 1.0
Msum = np.zeros((d, d), dtype=complex)
K = 4000
for _ in range(K):
    Msum += (v * rand_u(d)) @ rand_u(d) @ (v * rand_u(d)).conj().T
EM = Msum / K
chk("T3 TOOTH Haar-mean composite ~ 0", smin(EM) < 0.05 and np.linalg.norm(EM) < 0.25,
    "|EM|=%.3f smin=%.3f" % (np.linalg.norm(EM), smin(EM)))

print("== T4: Loewner + Markov moment bound (MC) ==")
v, lam, p, K = 1.5, 2.0, 0.7, 1500
rows = []
for rep in range(3):
    EQ = np.zeros((4, 4), dtype=complex)
    EV = 0.0; Elam = 0.0
    for _ in range(K):
        if rng.random() < p:
            sv = np.array([v, v, v, v])
        else:
            sv = np.array([0.0, v, v, v])
        Phi = rand_u(4) @ np.diag(sv)
        EQ += (Phi @ Phi.conj().T) / K
        EV += (lam / 4 * np.sum((sv**2 - v**2)**2)) / K
        Elam += sv[0]**2 / K
    rows.append((np.linalg.eigvalsh(EQ)[0], Elam, EV))
okA = all(r[0] >= r[1] - 1e-9 for r in rows)
chk("T4 lambda_min(E[Q]) >= E[lambda_min(Q)]", okA, "p=%.1f, 3 reps" % p)
EVm = np.mean([r[2] for r in rows]); Elamm = np.mean([r[1] for r in rows])
eps = np.linspace(EVm * (1 + 1e-9) + 1e-12, lam * v**4 / 4 * (1 - 1e-9), 4000)
best = np.max((v**2 - 2 * np.sqrt(eps / lam)) * (1 - EVm / eps))
chk("T4 bound positive and <= E[lambda_min]", best > 0 and best <= Elamm + 1e-9,
    "best=%.3f Elam=%.3f EV=%.3f" % (best, Elamm, EVm))
EV2 = (1 - 0.5) * lam / 4 * 2 * v**4
best2 = np.max((v**2 - 2 * np.sqrt(eps / lam)) * (1 - EV2 / eps))
Elam2 = 0.0
chk("T4 TOOTH EV > lam v^4/4 or double collapse: no bound", best2 <= 1e-12,
    "EV2=%.2f best=%.1e" % (EV2, best2))

print("== T5: bounded-connection transport bound ==")
d = 4
ok5 = True; anti = True
for trial in range(30):
    nst = 150
    wsum = 0.0; U = np.eye(d, dtype=complex)
    for k in range(nst):
        Hc = rand_herm(d)
        sl = 1j * Hc / nst
        U = expm(sl) @ U
        wsum += smax(sl)
    if smin(U) < np.exp(-wsum) - 1e-9:
        ok5 = False
    if abs(smin(U) - 1.0) > 1e-9:
        anti = False
chk("T5 sigma_min(Pexp) >= exp(-int smax(omega))", ok5, "30 unitary trials")
chk("T5 anti-Hermitian integrand: sigma_min = 1", anti)
U = np.eye(d, dtype=complex)
for k in range(200):
    U = expm(-0.3 / 200 * np.eye(d, dtype=complex)) @ U
chk("T5 sharp: scalar gl path reaches the bound", abs(smin(U) - np.exp(-0.3)) < 1e-9)

print("== S2 SUMMARY ==")
print("FAILURES: %d %s" % (len(fails), fails if fails else "(none)"))
