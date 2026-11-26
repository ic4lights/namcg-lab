"""022 script 3: exact quantum Hessian of  S = -1/4 Tr [X^A,X^B]^2 + (m^2/2) Tr X^2  at the compact (Euclidean, so(6)) fuzzy backgrounds
  P4c: 4 matrices X^a = M^{a5}, a=1..4   (compact analogue of T^a = M^{a4}; stationary for m^2 = -3)
  P5c: 5 matrices X^A = M^{A6}, A=1..5   (compact analogue of the SO(4,1)-covariant X^A = M^{A5}; stationary for m^2 = -4)
on the N-th symmetric power of the 4 of su(4)=so(6) (finite matrices; no Poisson limit, no heat kernel).
Hessian:  (H a)^B = ad(X^A)^2 a^B + [a^A,F^{AB}] + [X^A,[a^A,X^B]] + m^2 a^B,  F^{AB}=[X^A,X^B],  on traceless Hermitian a.
Reports: number of negative eigenvalues (excluding the 5 or 4 decoupled identity shifts, which are excluded by tracelessness),
zero eigenvalues versus gauge directions d^2-1, and the smallest positive eigenvalues of the physical sector.
"""
import numpy as np, itertools, sys
import scipy.sparse as sp
import scipy.sparse.linalg as sla

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]], complex); s3 = np.diag([1., -1]).astype(complex); I2 = np.eye(2, dtype=complex)
def kron(*ms):
    out = np.array([[1]], complex)
    for m in ms: out = np.kron(out, m)
    return out
g = [kron(s1, I2, I2), kron(s2, I2, I2), kron(s3, s1, I2), kron(s3, s2, I2), kron(s3, s3, s1), kron(s3, s3, s2)]
chi = np.eye(8, dtype=complex)
for G in g: chi = chi @ G
chi = chi * (1j ** 3 if False else 1)
w, v = np.linalg.eig(chi)
lam = w[0]; sel = np.where(np.abs(w - lam) < 1e-9)[0]
V, _ = np.linalg.qr(v[:, sel])
Sig = np.zeros((6, 6, 4, 4), complex)
for A in range(6):
    for B in range(6):
        Sig[A, B] = V.conj().T @ (-0.25j * (g[A] @ g[B] - g[B] @ g[A])) @ V
# check so(6) relations [M_AB, M_CD] = i(d_BC M_AD - d_AC M_BD - d_BD M_AC + d_AD M_BC)  (up to overall sign conv.)
def comm(a, b): return a @ b - b @ a
d = np.eye(6)
sgn = None
for (A, B, C, D) in [(0, 1, 1, 2), (0, 2, 2, 3), (1, 4, 4, 5)]:
    lhs = comm(Sig[A, B], Sig[C, D])
    rhs = 1j * (d[B, C] * Sig[A, D] - d[A, C] * Sig[B, D] - d[B, D] * Sig[A, C] + d[A, D] * Sig[B, C])
    if sgn is None:
        sgn = 1 if np.allclose(lhs, rhs) else (-1 if np.allclose(lhs, -rhs) else 0)
    assert np.allclose(lhs, sgn * rhs), "so(6) relations fail"
print("so(6) relations hold with sign", sgn)

def sym_power_ops(mats, N):
    states = [t for t in itertools.product(range(N + 1), repeat=4) if sum(t) == N]
    idx = {t: i for i, t in enumerate(states)}
    dim = len(states)
    out = []
    for m in mats:
        rows, cols, vals = [], [], []
        for t in states:
            for i in range(4):
                if t[i] == 0: continue
                for j in range(4):
                    if m[j, i] == 0: continue     # a_j^dag a_i with coefficient m[j,i]: maps |t> -> |t - e_i + e_j>
                    t2 = list(t); amp = np.sqrt(t2[i]); t2[i] -= 1; amp *= np.sqrt(t2[j] + 1); t2[j] += 1
                    rows.append(idx[tuple(t2)]); cols.append(idx[t]); vals.append(m[j, i] * amp)
        out.append(sp.csr_matrix((vals, (rows, cols)), shape=(dim, dim)).toarray())
    return out, dim

def hessian(X, m2):
    nA = len(X); dd = X[0].shape[0]
    I = np.eye(dd)
    ad = [np.kron(x, I) - np.kron(I, x.T) for x in X]           # ad(X)(a) = [X,a], row-major vec
    adsq = sum(a @ a for a in ad)
    n2 = dd * dd
    Hm = np.zeros((nA * n2, nA * n2), complex)
    F = [[X[A] @ X[B] - X[B] @ X[A] for B in range(nA)] for A in range(nA)]
    for B in range(nA):
        Hm[B * n2:(B + 1) * n2, B * n2:(B + 1) * n2] += adsq + m2 * np.eye(n2)
        for A in range(nA):
            # [a^A, F^{AB}] = -ad(F^{AB}) a^A
            adF = np.kron(F[A][B], I) - np.kron(I, F[A][B].T)
            Hm[B * n2:(B + 1) * n2, A * n2:(A + 1) * n2] += -adF
            # [X^A,[a^A,X^B]] = -ad(X^A) ad(X^B) a^A
            Hm[B * n2:(B + 1) * n2, A * n2:(A + 1) * n2] += -ad[A] @ ad[B]
    return Hm

def run(name, idxpairs, N):
    mats = [Sig[a, b] for (a, b) in idxpairs]
    X, dd = sym_power_ops(mats, N)
    X = [x * 1.0 for x in X]
    nA = len(X)
    # background check: [X^B,[X^B,X^A]] = lam X^A
    lamA = []
    for A in range(nA):
        acc = sum(comm(X[B], comm(X[B], X[A])) for B in range(nA))
        k = np.vdot(X[A], acc) / np.vdot(X[A], X[A])
        lamA.append(k.real); assert np.allclose(acc, k * X[A], atol=1e-8)
    lam = lamA[0]
    m2 = -lam
    Hm = hessian(X, m2)
    # project out trace parts: a^A = c^A 1
    n2 = dd * dd
    P = np.eye(nA * n2, dtype=complex)
    idv = np.eye(dd).reshape(-1) / np.sqrt(dd)
    for A in range(nA):
        v = np.zeros(nA * n2, complex); v[A * n2:(A + 1) * n2] = idv
        P -= np.outer(v, v.conj())
    # Hermitian check
    herm = np.max(np.abs(Hm - Hm.conj().T))
    # Hessian is real-symmetric on the real space of Hermitian a; complex-linear extension has the same spectrum
    ev = np.linalg.eigvalsh((Hm + Hm.conj().T) / 2)
    # remove the nA identity shifts (eigenvalue m2)
    ev = np.sort(ev)
    ids = np.sum(np.abs(ev - m2) < 1e-8)
    return dict(name=name, N=N, d=dd, lam=lam, m2=m2, herm=herm, ev=ev, ids=ids, nA=nA)

def report(r):
    ev = r['ev']; d = r['d']; nA = r['nA']; tol = 1e-8
    # drop exactly nA identity-direction eigenvalues m2 (they are the decoupled U(1) shifts)
    ev2 = list(ev)
    for _ in range(nA):
        j = int(np.argmin(np.abs(np.array(ev2) - r['m2']))); ev2.pop(j)
    ev2 = np.array(ev2)
    neg = ev2[ev2 < -tol]; zer = ev2[np.abs(ev2) <= tol]; pos = ev2[ev2 > tol]
    print(f"{r['name']} N={r['N']} d={d} m2={r['m2']:+.0f} |herm err {r['herm']:.1e}| negative: {len(neg)} (min {neg.min() if len(neg) else 0:.4f}) "
          f"zero: {len(zer)} (gauge d^2-1 = {d*d-1}) positive: {len(pos)} (smallest {pos.min() if len(pos) else float('nan'):.4f})")
    return neg, zer, pos

if __name__ == "__main__":
    Ns = [int(a) for a in sys.argv[1:]] or [1, 2]
    for N in Ns:
        r4 = run("P4c (4 matrices X^a=M^{a5})", [(a, 4) for a in range(4)], N)
        report(r4)
        r5 = run("P5c (5 matrices X^A=M^{A6})", [(A, 5) for A in range(5)], N)
        report(r5)
