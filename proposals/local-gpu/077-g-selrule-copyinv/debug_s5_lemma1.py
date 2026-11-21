"""Debug s5 Lemma 1(a): numeric twin of the sympy construction, q=2, N=3.

Builds Qs, C0, Z0, T exactly as s5 does (no-conjugate C0) with random complex
numbers and tests, in order:
  T1: Qs == -2i(U R^+ - R U^+)            (block-equal specialization)
  T2: nonzero spectrum(Qs) vs eigvals(T)  (similarity lemma, both C0 versions)
  T3: top-2q+1 charpoly coefficients (numpy poly of eigs), both C0 conventions
Prints max abs deviations. Run: python -I
proposals/077-g-selrule-copyinv/debug_s5_lemma1.py
"""
import numpy as np

rng = np.random.default_rng(1)
q, N = 2, 3
n = q * N

Zcols = rng.normal(size=(N, q)) + 1j * rng.normal(size=(N, q))  # column a: z_a

U = np.zeros((n, q), complex)
for a in range(q):
    U[a * N, a] = 1.0                       # u = e_0 per copy-block
R = np.zeros((n, q), complex)
for b in range(n):
    for a in range(q):
        R[b, a] = Zcols[b % N, a]           # block-equal rows

# Qs as s5 builds it: block(row ra, col cb) = -2i(|u)(z_cb| - |z_cb)(u|)
Qs = np.zeros((n, n), complex)
for ra in range(q):
    for cb in range(q):
        zb = Zcols[:, cb]
        blk = np.zeros((N, N), complex)
        for i in range(N):
            for j in range(N):
                ui = 1.0 if i == 0 else 0.0
                uj = 1.0 if j == 0 else 0.0
                blk[i, j] = -2j * (ui * np.conj(zb[j]) - zb[i] * uj)
        Qs[ra * N:(ra + 1) * N, cb * N:(cb + 1) * N] = blk

Qrange = -2j * (U @ R.conj().T - R @ U.conj().T)
print("T1  max|Qs - (-2i(U R^+ - R U^+))| :", np.abs(Qs - Qrange).max())

for tag, C0 in [("C0=U^+R (no conj)", U.conj().T @ R),
                ("C0=conj(U^+R)", (U.conj().T @ R).conj())]:
    Z0 = R.conj().T @ R
    T = -2j * np.block([[C0.conj().T, Z0], [-np.eye(q), -C0]])
    ev = np.linalg.eigvals(T)
    e1 = np.sort(np.linalg.eigvalsh(Qs))
    thr = 1e-9 * max(1.0, np.abs(e1).max())
    nz1 = e1[np.abs(e1) > thr]
    print(tag, "| eigvals(T) :", np.sort(np.round(ev.real, 6)),
          " max|imag| :", np.abs(ev.imag).max())
    print("    nz spectrum Qs :", np.sort(np.round(nz1, 6)),
          " dev vs sorted T :",
          max(abs(np.sort(ev.real) - np.sort(nz1))) if len(ev) == len(nz1) else "count mismatch")
    # top coefficients: charpoly via numpy eigenvalues
    pQ = np.poly(np.linalg.eigvals(Qs))          # monic, lam^6..lam^0
    pT = np.poly(ev)                              # lam^4..lam^0
    d = [np.abs(pQ[N * q - k] - pT[2 * q - k]) for k in range(2 * q + 1)]
    print("    top-2q+1 charpoly coeff dev :", ["%.2e" % x for x in d])
print("DONE")
