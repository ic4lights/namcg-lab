"""077: pin the z<->R copy-block convention and the s5(a) Qs form empirically.

Part 1 (physics): q=2, N=20, one coincident edge-charge draw. Build w_{ba} =
sum_f conj(c_f) Th Pi^f_{ba} v from the SAME Pis that enter edge_charge, then
test which R convention satisfies Ql == -2i(U R^+ - R U^+) exactly:
  conv A: R block(x,y) = w_{yx} (copy-transpose)
  conv B: R block(x,y) = w_{xy} (as coded in s2b Tmat_from_z).
Part 2 (s5(a) corrected): R with block-equal COLUMNS (R_{xy} = z_y),
Qs := -2i(U R^+ - R U^+) built directly; compare spectrum(T) (eigvals) with
nonzero spectrum(Qs), and show the OLD s5 block formula is non-Hermitian.
Run: python -I proposals/077-g-selrule-copyinv/debug_conventions.py
"""
import numpy as np

rng = np.random.default_rng(7)


def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    return [(jp + jp.conj().T) / 2, (jp - jp.conj().T) / 2j, j3]


def cap_data(J, n, M):
    nj = n[0] * J[0] + n[1] * J[1] + n[2] * J[2]
    ev, evec = np.linalg.eigh(nj)
    order = np.argsort(-np.real(ev))
    u = evec[:, order[M - 1]]
    v = evec[:, order[M]]
    Th = evec[:, order[:M]] @ evec[:, order[:M]].conj().T
    return Th, u, v


def herg(m):
    g = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    return g + g.conj().T


def edge_charge(Xs, Th, Pis):
    Tb = np.eye(len(Th), dtype=complex) - Th
    A = sum((Th @ x @ Tb) @ (Tb @ pi @ Th) for x, pi in zip(Xs, Pis))
    return -2j * (A - A.conj().T)


# ---------- Part 1
q, N = 2, 20
M = N // 2
J = su2(N)
n = rng.normal(size=3); n /= np.linalg.norm(n)
Th, u, v = cap_data(J, n, M)
A3 = rng.normal(size=(3, 3))
X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
ca = [np.vdot(u, x @ v) for x in X]
Pis = [herg(q * N) for _ in range(3)]
Iq = np.eye(q)
Ql = edge_charge([np.kron(Iq, x) for x in X], np.kron(Iq, Th), Pis)
w = {(b, a): sum(np.conj(ca[f]) * (Th @ Pis[f][b * N:(b + 1) * N,
                                                  a * N:(a + 1) * N] @ v)
                 for f in range(3))
     for b in range(q) for a in range(q)}
U = np.kron(np.eye(q), u[:, None])
for tag, f in [("A: R_{xy}=w_{yx}", lambda x, y: w[(y, x)]),
               ("B: R_{xy}=w_{xy}", lambda x, y: w[(x, y)])]:
    R = np.zeros((q * N, q), complex)
    for x in range(q):
        for y in range(q):
            R[x * N:(x + 1) * N, y] = f(x, y)
    Qf = -2j * (U @ R.conj().T - R @ U.conj().T)
    print("conv %s : max|Ql - Qfact| = %.2e" % (tag, np.abs(Ql - Qf).max()))

# ---------- Part 2
q2, N2 = 2, 3
Zc = rng.normal(size=(N2, q2)) + 1j * rng.normal(size=(N2, q2))
U2 = np.kron(np.eye(q2), np.eye(N2)[:, 0:1])
R2 = np.zeros((q2 * N2, q2), complex)
for x in range(q2):
    for y in range(q2):
        R2[x * N2:(x + 1) * N2, y] = Zc[:, y]          # block-equal columns
Qs = -2j * (U2 @ R2.conj().T - R2 @ U2.conj().T)
C0 = U2.conj().T @ R2
Z0 = R2.conj().T @ R2
T = -2j * np.block([[C0.conj().T, Z0], [-np.eye(q2), -C0]])
evT = np.linalg.eigvals(T)
e1 = np.sort(np.linalg.eigvalsh(Qs))
thr = 1e-9 * max(1.0, np.abs(e1).max())
nz = e1[np.abs(e1) > thr]
print("Part2: max|imag eigvals(T)| %.2e ; dev nz(Qs) vs sorted Re(T): %.2e"
      % (np.abs(evT.imag).max(), max(abs(np.sort(evT.real) - nz))))
# old s5 (a) block formula for the record: block(b,a) uses z_col in BOTH terms
Qo = np.zeros((q2 * N2, q2 * N2), complex)
for ra in range(q2):
    for cb in range(q2):
        zb = Zc[:, cb]
        blk = np.zeros((N2, N2), complex)
        blk[0, :] += -2j * np.conj(zb)
        blk[:, 0] += -2j * (-zb * 1.0) + 2j * np.conj(zb[0]) * np.eye(N2)[0, :]
        for i in range(N2):
            for j in range(N2):
                blk[i, j] = -2j * ((1 if i == 0 else 0) * np.conj(zb[j])
                                   - zb[i] * (1 if j == 0 else 0))
        Qo[ra * N2:(ra + 1) * N2, cb * N2:(cb + 1) * N2] = blk
print("Part2: old-s5-Qs non-Hermiticity max|Q-Q^H| = %.2e ; its max|Q-Qs_new| = %.2e"
      % (np.abs(Qo - Qo.conj().T).max(), np.abs(Qo - Qs).max()))
print("DONE")
