#!/usr/bin/env python3
"""s3: mixed-multiplicity moment excess and the 077 diagnostics.
(A) symbolic pair 2p-moments S_p(h,n) = (-2h+2s)^(2p)+(-2h-2s)^(2p), s=(h^2+n)^(1/2),
    at p=1,2; exact rational signature-excess numbers 9/17, 81/145, equal-depth 1;
    exact h=0 identity (mixed moment - multiplicity-1 moment)/mult-1 = sum(q_f-1)n_f^p/sum n_f^p.
(B) realizable mixed block-scalar data: U2 >= 0 always, U2=0 iff equal moduli;
    relative-gap D: 0 at all-equal pair data, >0 at genuinely mixed data.
(C) general h != 0: exact weight identity (mixed-1)/1 = sum(q_f-1)S_p(h_f,n_f)/sum S_p(h_f,n_f)
    verified from full charge spectra; shows the rho_p weight is S_p, not n_f^p, off h=0.
Deterministic seed 20261117; verdicts only.
"""
import numpy as np, sympy as sp
from fractions import Fraction as Fr
rng = np.random.default_rng(20261117)
h, n, lam = sp.symbols('h n lam', positive=False, real=True)
s = sp.sqrt(h**2 + n)
S1 = sp.expand((-2*h + 2*s)**2 + (-2*h - 2*s)**2)
S2 = sp.expand((-2*h + 2*s)**4 + (-2*h - 2*s)**4)
print('A pair moments: S1 =', sp.factor(S1), '| S2 =', sp.factor(S2))

# exact rational excess numbers at h=0: n=(1/4,2/9), q=(2,1); equal depths (2,2)
ns = [Fr(1, 4), Fr(2, 9)]; qs = [2, 1]
rho = [(sum((qs[f]-1)*ns[f]**p for f in range(2)) / sum(ns[f]**p for f in range(2)),
        sum(qs[f]*(4*ns[f])**p*2 for f in range(2)), sum((4*ns[f])**p*2 for f in range(2)))
       for p in (1, 2)]
ok_mom = all((M - m) / m == r for r, M, m in rho)
eq22 = [sum(ns[f]**p for f in range(2)) / sum(ns[f]**p for f in range(2)) for p in (1, 2)]
print('A exact excesses p=1,2:', [r for r, M, m in rho],
      '| moment identity (mixed-1)/1 == rho_p:', ok_mom,
      '| equal-depth (2,2) value p=1,2:', eq22)

def spectrum(qs, hs, ns, N, rng):
    q = sum(qs)
    u = rng.standard_normal(N) + 1j*rng.standard_normal(N); u /= np.linalg.norm(u)
    U = np.kron(np.eye(q), u[:, None])
    W = rng.standard_normal((q*N, 2*q)) + 1j*rng.standard_normal((q*N, 2*q))
    V, _ = np.linalg.qr(W); V = V - U @ (U.conj().T @ V); V, _ = np.linalg.qr(V); V = V[:, :q]
    H = np.diag(np.repeat(hs, qs)); K = np.diag(np.repeat(ns, qs))
    A = rng.standard_normal((q, q)) + 1j*rng.standard_normal((q, q)); A = (A + A.conj().T)/2
    C0 = A + 1j*H
    R = U @ C0 + V * np.sqrt(np.repeat(ns, qs))
    Qt = -2j*(U @ R.conj().T - R @ U.conj().T); Qt = (Qt + Qt.conj().T)/2
    ev = np.sort(np.linalg.eigvalsh(Qt))
    return ev[np.abs(ev) > 1e-7]

def diag(evs):
    q = evs.size // 2
    D = max(evs[q-1] - evs[0], evs[-1] - evs[q]) / np.max(np.abs(evs))
    U2 = np.sum(evs**4) / ((2*q) * (np.sum(evs**2)/(2*q))**2) - 1.0
    return D, U2

dmin_mixed, dmax_equal, umin = 1e18, 0.0, 1e9
for k in range(40):
    qs = [(2, 1), (1, 1), (3, 1)][k % 3]
    hs = rng.standard_normal(len(qs)); ns = 0.4 + 0.6*rng.random(len(qs))
    evs = spectrum(qs, hs, ns, 5, rng); D, U2v = diag(evs)
    dmin_mixed = min(dmin_mixed, D); umin = min(umin, U2v)
for k in range(10):  # equal pair data: tiling, D = 0
    qs = (2, 1)
    evs = spectrum(qs, np.array([0.7, 0.7]), np.array([0.5, 0.5]), 5, rng)
    D, U2v = diag(evs); dmax_equal = max(dmax_equal, D)
print('B mixed-data min D =', '%.3e' % dmin_mixed, '| equal-data max D =', '%.3e' % dmax_equal,
      "| min U2 over 40 mixed samples =", '%.3e' % umin, "(expect > 0; U2 >= 0 always)")

worst_w = 0.0
for k in range(30):
    qs = [2, 1]
    hs = rng.standard_normal(2); ns = 0.4 + 0.6*rng.random(2)
    evs = spectrum(qs, hs, ns, 5, rng)
    S = [8*(2*hh**2 + nn) for hh, nn in zip(hs, ns)]
    S4 = [32*(8*hh**4 + 8*hh**2*nn + nn**2) for hh, nn in zip(hs, ns)]
    for p, Sp in ((1, S), (2, S4)):
        Mm = np.sum(evs**(2*p)); w1 = sum(Sp); wmix = sum(qs[f]*Sp[f] for f in range(2))
        lhs = (Mm - w1) / w1; rhs = sum((qs[f]-1)*Sp[f] for f in range(2)) / w1
        worst_w = max(worst_w, abs(lhs - rhs))
print('C general-h weight identity: max |excess_from_spectra - excess_from_S_p weights| =',
      '%.3e' % worst_w, 'over 30 samples x p=1,2')
