"""049 s2: exact scaling of the one-loop functional on a product background. Prints only.

Product: X^a = sqrt(lam) A^a (x) 1, a = 0..3 (Euclidean section), X^i = chi 1 (x) B^i, i = 1..6, with random Hermitian
A^a (d1 x d1) and B^i (d2 x d2).  Operators on Mat(d1 d2):
  vector  H0 delta_AB + 2 ad([X^A,X^B])  (ten components), weight +1
  ghost   H0, weight -2
  spinor  (Gamma_A ad X^A)^2 on the positive chirality of SO(10), sixteen components, weight -1/2.

Checks:
 (A) the operators are exactly lam H_M + chi^2 H_K, so that for str 1 = 0
     Gamma_1 = (1/2) sum c_i ln w_i  (with c_i the weights over non-zero eigenvalues) depends on lam, chi only via chi^2/lam;
 (B) the small-s expansion: str H^k = 0, k = 0..3;
 (C) the mode counting that makes Gamma_1 well defined: sum of weights of zero eigenvalues is reported.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from klib import adc, comm

rng = np.random.default_rng(4902)


def herm(d):
    r = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    r = (r + r.conj().T) / 2
    return r - np.trace(r) / d * np.eye(d)


def gamma10():
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    e = np.eye(2, dtype=complex)
    out = []
    for k in range(5):
        for s in (s1, s2):
            m = np.array([[1]], dtype=complex)
            for j in range(5):
                m = np.kron(m, s3 if j < k else (s if j == k else e))
            out.append(m)
    chir = np.array([[1]], dtype=complex)
    for j in range(5):
        chir = np.kron(chir, s3)
    return out, chir


GAM, CHIR = gamma10()
sel = np.where(np.real(np.diag(CHIR)) > 0)[0]
PLUS = np.eye(32, dtype=complex)[:, sel]
sig = [PLUS.conj().T @ g @ (np.eye(32, dtype=complex)[:, np.where(np.real(np.diag(CHIR)) < 0)[0]]) for g in GAM]


def spectra10(X):
    d = X[0].shape[0]
    ads = [adc(x) for x in X]
    H0 = sum(a @ a for a in ads)
    D2 = d * d
    HV = np.zeros((10 * D2, 10 * D2), dtype=complex)
    for i in range(10):
        for j in range(10):
            blk = 2 * adc(comm(X[i], X[j]))
            if i == j:
                blk = blk + H0
            HV[i * D2:(i + 1) * D2, j * D2:(j + 1) * D2] = blk
    # D maps positive to negative chirality; D^dagger D is the operator on the positive chirality
    D = sum(np.kron(s, a) for s, a in zip(sig, ads))
    HD = D @ D.conj().T
    w0 = np.linalg.eigvalsh((H0 + H0.conj().T) / 2)
    wV = np.linalg.eigvalsh((HV + HV.conj().T) / 2)
    wD = np.linalg.eigvalsh((HD + HD.conj().T) / 2)
    return w0, wV, wD


def gamma1(w0, wV, wD, tol=1e-9):
    """(1/2) sum c ln w on non-zero eigenvalues; returns value and weight of zero eigenvalues."""
    vals = 0.0
    zero = 0.0
    for w, c in ((wV, 1.0), (w0, -2.0), (wD, -0.5)):
        nz = np.abs(w) > tol
        vals += 0.5 * c * np.sum(np.log(np.abs(w[nz])))
        zero += c * np.sum(~nz)
    return vals, zero, min(wV.min(), wD.min())


d1, d2 = 2, 2
A = [herm(d1) for _ in range(4)]
B = [herm(d2) for _ in range(6)]


def X_of(lam, chi):
    return [np.sqrt(lam) * np.kron(a, np.eye(d2)) for a in A] + [chi * np.kron(np.eye(d1), b) for b in B]


print("(A) dependence on chi^2/lam (expected equal within each group of rows)")
print("    %8s %8s %12s %22s %12s" % ("lam", "chi", "chi^2/lam", "Gamma_1", "zero weight"))
for lam, chi in ((1.0, 1.0), (2.0, np.sqrt(2.0)), (0.3, np.sqrt(0.3)), (7.0, np.sqrt(7.0)),
                 (1.0, 2.0), (4.0, 4.0), (0.25, 1.0), (1.0, 0.5), (16.0, 2.0)):
    w0, wV, wD = spectra10(X_of(lam, chi))
    g, z, mn = gamma1(w0, wV, wD)
    print("    %8.3f %8.4f %12.5f %22.12f %12.1f" % (lam, chi, chi ** 2 / lam, g, z))

print("(B) str H^k at lam = 2, chi = 1.3")
w0, wV, wD = spectra10(X_of(2.0, 1.3))
for k in range(0, 5):
    print("    k=%d  str H^k = % .4e" % (k, (wV ** k).sum() - 2 * (w0 ** k).sum() - 0.5 * (wD ** k).sum()))
print("    smallest vector eigenvalue %.4f (a negative mode leaves the proper-time form undefined; ln|w| printed above)" % wV.min())

print("(C) the operator split: || H(lam,chi) - lam H(1,0) - chi^2 H(0,1) ||")
ads = lambda X: sum(adc(x) @ adc(x) for x in X)
print("    H0 residual %.2e" % np.abs(ads(X_of(2.0, 1.3)) - 2.0 * ads(X_of(1.0, 0.0)) - 1.69 * ads(X_of(0.0, 1.0))).max())
