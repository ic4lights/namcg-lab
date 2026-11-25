# verify_126_A_nogo.py -- chain 126, Part A: the finite-dimensional unitary obstruction
# for the D1 first-order equivariant class (appH L1616-1621).
#
# Lemma checked here (established; the script verifies its machine-checkable steps):
#   Let rho: so(3,1) -> gl(V), dim V < infinity, be a Lie algebra homomorphism whose
#   image is anti-Hermitian. Then rho = 0. Consequently, if S_cd are N x N
#   anti-Hermitian matrices closing to so(3,1) under bracket and D_a any N x N
#   matrices with [S_cd, D_a] = eta_ad D_c - eta_ac D_d, then D_a = 0: no nonzero
#   finite-N realization of the first class relation exists with the unitary
#   (*-) structure of the class.
# Proof chain:
#   (1) so(3,1) is 6-dim semisimple (Killing nondegenerate; cross-checked exactly
#       against B(X,Y) = 2 tr(XY) in the vector representation) and its Killing
#       form is indefinite (witnesses on rotation and boost).
#   (2) For anti-Hermitian A: tr(ad_A ad_A) = -||ad_A||_HS^2 <= 0, equality iff
#       ad_A = 0; hence any algebra of anti-Hermitian matrices has negative-
#       semidefinite Killing form (compact).
#   (3) A homomorphic image of simple so(3,1) is 0 or isomorphic; isomorphic would
#       make the Killing form both indefinite and definite: contradiction.
#   (4) With ad_S = 0 the relation forces D = 0 (rank check of the label map).
import numpy as np

rng = np.random.default_rng(126)
FAIL = []

def chk(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAIL.append(name)

eta = np.diag([-1.0, 1.0, 1.0, 1.0])

# --- so(3,1) generators in the vector representation:
# (J_ij)^mu_nu = delta^mu_i eta_jn - delta^mu_j eta_in, i<j.
keys = [(i, j) for i in range(4) for j in range(i + 1, 4)]
gens = {}
for (i, j) in keys:
    M = np.zeros((4, 4))
    for mu in range(4):
        for n in range(4):
            M[mu, n] = ((1.0 if mu == i else 0.0) * eta[j, n]
                        - (1.0 if mu == j else 0.0) * eta[i, n])
    gens[(i, j)] = M

chk("A0 six independent generators (rank 6)",
    np.linalg.matrix_rank(np.stack([g.ravel() for g in gens.values()])) == 6)
chk("A0b eta-antisymmetry of all generators",
    all(np.allclose(gens[k].T @ eta + eta @ gens[k], 0, atol=1e-12) for k in keys))

# --- structure constants of the span: [e_p, e_q] = sum_r c[p,q,r] e_r.
basis = np.stack([gens[k].ravel() for k in keys])          # 6 x 16
c = np.zeros((6, 6, 6))
for p, k1 in enumerate(keys):
    for q, k2 in enumerate(keys):
        C = gens[k1] @ gens[k2] - gens[k2] @ gens[k1]
        x, *_ = np.linalg.lstsq(basis.T, C.ravel(), rcond=None)
        c[p, q, :] = x
res = max(np.linalg.norm(basis.T @ c[p, q] - (gens[keys[p]] @ gens[keys[q]]
            - gens[keys[q]] @ gens[keys[p]]).ravel())
          for p in range(6) for q in range(6))
chk("A1 exact closure of span under bracket (residual < 1e-9)", res < 1e-9)

# --- Killing form B[p,q] = tr(ad_{e_p} ad_{e_q}), explicit loops.
def AD(m):
    Mm = np.zeros((6, 6))
    for r in range(6):
        for t in range(6):
            Mm[t, r] = c[m, r, t]   # (ad e_m) e_r = sum_t c[m,r,t] e_t
    return Mm
ADs = [AD(m) for m in range(6)]
Bk = np.zeros((6, 6))
for p in range(6):
    for q in range(6):
        Bk[p, q] = np.trace(ADs[p] @ ADs[q])
chk("A2a Killing symmetric", np.allclose(Bk, Bk.T, atol=1e-10))
cross = max(abs(Bk[p, q] - 2.0 * np.trace(gens[keys[p]] @ gens[keys[q]]))
            for p in range(6) for q in range(6))
chk("A2b exact cross-check B(X,Y) = 2 tr(XY) vector rep (so(p,q) identity)", cross < 1e-9)
chk("A2 nondegenerate Killing form (semisimple)", abs(np.linalg.det(Bk)) > 1e-6)
w = np.linalg.eigvalsh(0.5 * (Bk + Bk.T))
chk("A3 Killing form INDEFINITE (noncompact)", (w.min() < -1e-9) and (w.max() > 1e-9))
i12 = keys.index((1, 2)); i01 = keys.index((0, 1))
chk("A3a B(J12,J12) < 0 (compact direction)", Bk[i12, i12] < 0)
chk("A3b B(K1,K1) > 0 (boost direction)", Bk[i01, i01] > 0)
print("   B(J12,J12) = %.6f  B(K1,K1) = %.6f  eigs = %s  det = %.3f"
      % (Bk[i12, i12], Bk[i01, i01], np.round(w, 4), np.linalg.det(Bk)))

# --- (2) tr(ad_A^2) = -||ad_A||_HS^2 for anti-Hermitian A.
def admat(Ain):
    M = np.zeros((16, 16), dtype=complex)
    E = np.zeros((4, 4), dtype=complex)
    for a in range(16):
        E[:] = 0.0
        E.reshape(16)[a] = 1.0
        M[:, a] = (Ain @ E - E @ Ain).reshape(16)
    return M
ok = True
for trial in range(8):
    A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    M = admat(A - A.conj().T)
    ok = ok and abs(np.trace(M @ M) + np.sum(np.abs(M) ** 2)) < 1e-9
chk("A4 tr(ad_A^2) = -||ad_A||_HS^2 (anti-Hermitian, 4x4, 8 seeds)", ok)

# --- derived algebra full (no abelian quotient of the tested generators).
chk("A5 derived algebra = full",
    np.linalg.matrix_rank(np.stack([c[p, q, :] for p in range(6) for q in range(6)])) == 6)

# --- (4) if ad_S = 0, the relation is eta_{aj} D_i - eta_{ai} D_j = 0 (all i<j, all a),
#     label-wise; the label map D -> residuals has full column rank 4.
A = np.zeros((24, 4)); r = 0
for (i, j) in keys:
    for a in range(4):
        A[r, i] += eta[a, j]
        A[r, j] -= eta[a, i]
        r += 1
chk("A6 ad_S=0 forces D=0 (label map rank 4)", np.linalg.matrix_rank(A) == 4)

# --- CONTROL: the A3 test must discriminate. so(4) (antisymmetric real generators,
# compact real form) has negative-definite Killing form: the indefinite test must
# report DEFINITE (max eig < 0). If the test were vacuous this control stays dead.
gens4 = {}
for idx, (i, j) in enumerate(keys):
    M = np.zeros((4, 4)); M[i, j] = 1.0; M[j, i] = -1.0
    gens4[idx] = M
c4 = np.zeros((6, 6, 6))
for p in range(6):
    for q in range(6):
        C = gens4[p] @ gens4[q] - gens4[q] @ gens4[p]
        for rr in range(6):
            c4[p, q, rr] = -0.5 * np.trace(C @ gens4[rr])   # tr(G_a G_b) = -2 delta_ab
ADs4 = []
for m in range(6):
    Mm = np.zeros((6, 6))
    for r in range(6):
        for t in range(6):
            Mm[t, r] = c4[m, r, t]
    ADs4.append(Mm)
Bk4 = np.zeros((6, 6))
for p in range(6):
    for q in range(6):
        Bk4[p, q] = np.trace(ADs4[p] @ ADs4[q])
cross4 = max(abs(Bk4[p, q] - 2.0 * np.trace(gens4[p] @ gens4[q]))
             for p in range(6) for q in range(6))
chk("A7 so(4) Killing cross-check B = 2 tr(XY) (validates control's constants)",
    cross4 < 1e-9)
w4 = np.linalg.eigvalsh(0.5 * (Bk4 + Bk4.T))
fired = w4.max() < -1e-9
print(("CONTROL-FIRED " if fired else "CONTROL-DEAD ") +
      "so(4) Killing IS negative definite (eigs %s): A3 discriminates compact vs Lorentzian"
      % np.round(w4, 3))
if not fired:
    FAIL.append("CONTROL A3")

# --- CONTROL 2: the A4 identity must fail for a non-anti-Hermitian matrix.
A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
M = admat(A)
dev = abs(np.trace(M @ M) + np.sum(np.abs(M) ** 2))
fired2 = dev > 1.0
print(("CONTROL-FIRED " if fired2 else "CONTROL-DEAD ") +
      "generic (non-anti-Hermitian) matrix violates A4 identity, dev = %.3f" % dev)
if not fired2:
    FAIL.append("CONTROL A4")

print("SUMMARY_A:", "ALL-PASS" if not FAIL else "FAILURES " + repr(FAIL))
