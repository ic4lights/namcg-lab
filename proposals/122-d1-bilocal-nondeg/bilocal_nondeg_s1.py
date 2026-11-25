# -*- coding: ascii -*-
# Item 122, script 1: fiber and operator algebra for the bilocal composite
# M(x,y) = Phi(x) W(x,y) Phi(y)^dagger.
# Tests: R0 sigma_min(AB) >= smin(A)smin(B), equality if a factor is unitary,
# strict otherwise (tooth); R1 factorization T_M = M_Phi T_W M_Phi^dagger at
# the kernel level and two-sided estimate c^2 sW <= smin(T_M) <= C^2 sW with
# teeth; R2 fiber equality smin(A U B^dag)=smin(A)smin(B) for unitary U and
# det multiplicativity; R3 coincidence identity smin(Phi Phi^dag)=smin^2 and
# the threshold chain v^2 - 2 sqrt(eps/lambda) vs the recorded (1-r/v)^4
# form; R5 compression of positive fibers keeps the lower bound, failure for
# general factors (tooth); R6 condition-number transfer.
# Deterministic: fixed seeds, numpy only.
import numpy as np

rng = np.random.default_rng(122)
TOL = 1e-8
fails = []

def chk(name, cond, detail=""):
    tag = "OK" if cond else "FAIL"
    if not cond:
        fails.append(name)
    print("%-40s %s %s" % (name, tag, detail))

def smin(A):
    return np.linalg.svd(A, compute_uv=False)[-1]

def smax(A):
    return np.linalg.svd(A, compute_uv=False)[0]

def rand_u(d):
    Z = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Q, R = np.linalg.qr(Z)
    ph = np.diag(R) / np.abs(np.diag(R))
    return Q * ph[None, :]

def phi_with_svals(sv):
    d = len(sv)
    U = rand_u(d); V = rand_u(d)
    return (U * sv[None, :]) @ V.conj().T

def block_diag(blocks, d):
    n = len(blocks)
    M = np.zeros((n * d, n * d), dtype=complex)
    for i, B in enumerate(blocks):
        M[i*d:(i+1)*d, i*d:(i+1)*d] = B
    return M

print("== R0 ==")
bad_ineq = True; bad_eq = True; strict_seen = False
for trial in range(60):
    d = 2 + trial % 4
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    B = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    if smin(A @ B) < smin(A) * smin(B) - 1e-10:
        bad_ineq = False
    if smin(A @ B) > smin(A) * smin(B) + 1e-10:
        strict_seen = True
    U = rand_u(d)
    if abs(smin(A @ U) - smin(A)) > 1e-9 or abs(smin(U @ A) - smin(A)) > 1e-9:
        bad_eq = False
A2 = np.diag([1.0, 2.0]); B2 = np.diag([2.0, 1.0])
chk("R0 inequality (60 trials)", bad_ineq)
chk("R0 equality with unitary factor", bad_eq)
chk("R0 TOOTH strict w/o unitarity", strict_seen and abs(smin(A2 @ B2) - smin(A2) * smin(B2)) > 0.9,
    "smin(diag(1,2)diag(2,1))=2 vs 1")

print("== R1 ==")
ok_fac = True; ok_low = True; ok_up = True
for trial in range(40):
    Nb = 3 + trial % 4
    d = 4
    sv = np.sort(rng.uniform(0.3, 2.0, size=(Nb, d)), axis=1)
    blocks = [phi_with_svals(sv[i]) for i in range(Nb)]
    Mphi = block_diag(blocks, d)
    T_W = rng.standard_normal((Nb, Nb)) + 1j * rng.standard_normal((Nb, Nb))
    TW_big = np.kron(T_W, np.eye(d))
    T_M = Mphi @ TW_big @ Mphi.conj().T
    for i in range(Nb):
        for j in range(Nb):
            blk = T_M[i*d:(i+1)*d, j*d:(j+1)*d]
            K = (blocks[i] * T_W[i, j]) @ blocks[j].conj().T
            if np.max(np.abs(K - blk)) > 1e-9:
                ok_fac = False
    c = np.min(sv[:, 0]); Cc = np.max(sv[:, d-1])
    sM = smin(T_M); sW = smin(TW_big)
    if not (sM >= c**2 * sW - 1e-8): ok_low = False
    if not (smax(T_M) <= Cc**2 * smax(TW_big) + 1e-8): ok_up = False
tooth_ok = False
Nb, d = 4, 4
# Tooth 1: rank-deficient transport W (sW=0) forces sM=0 even for invertible
# Phi: Phi-data alone cannot supply a positive kernel lower bound.
sv = np.full((Nb, d), 1.0)
blocks = [phi_with_svals(sv[i]) for i in range(Nb)]
Mphi = block_diag(blocks, d)
P = rand_u(Nb) @ np.diag([1.0, 1.0, 1.0, 0.0]) @ rand_u(Nb).conj().T
TW_big = np.kron(P, np.eye(d))
sM = smin(Mphi @ TW_big @ Mphi.conj().T)
c_min = np.min(sv[:, 0])
tooth1 = (smin(TW_big) < 1e-12) and (sM < 1e-10) and (c_min > 0.5)
# Tooth 2: a near-degenerate fiber kills the lower bound even for a well-
# conditioned W (sharpness: the bound tracks c^2, not C^2)
sv2 = np.full((Nb, d), 1.0); sv2[1, 0] = 1e-5
blocks2 = [phi_with_svals(sv2[i]) for i in range(Nb)]
Mphi2 = block_diag(blocks2, d)
Wg = rng.standard_normal((Nb, Nb)) + 1j * rng.standard_normal((Nb, Nb))
TWg = np.kron(Wg, np.eye(d))
sM2 = smin(Mphi2 @ TWg @ Mphi2.conj().T)
tooth2 = sM2 < 1e-3 * smin(TWg)  # c^2 = 1e-10 case vs c^2 = 1
chk("R1 kernel factorization exact (40)", ok_fac)
chk("R1 lower estimate c^2 sW <= sM (40)", ok_low)
chk("R1 upper estimate smax(T_M) <= C^2 smax(W) (40)", ok_up)
chk("R1 TOOTH sW=0 forces sM=0 (Phi invertible)", tooth1)
chk("R1 TOOTH near-deg fiber tracks c^2", tooth2)

print("== R2 ==")
ok2 = True; okdet = True
for trial in range(60):
    d = 4
    a = rng.uniform(0.4, 2.0); b = rng.uniform(0.4, 2.0)
    sa = np.sort(rng.uniform(a, a + 1.0, size=d)); sb = np.sort(rng.uniform(b, b + 1.0, size=d))
    sa[0] = a; sb[0] = b
    A = phi_with_svals(sa); B = phi_with_svals(sb); U = rand_u(d)
    M = A @ U @ B.conj().T
    if smin(M) < sa[0] * sb[0] - 1e-8: ok2 = False
    if abs(abs(np.linalg.det(M)) - abs(np.linalg.det(A) * np.linalg.det(B))) > 1e-6: okdet = False
ok_rad = True
for trial in range(30):
    rho = rng.uniform(0.5, 1.5); sig = rng.uniform(0.5, 1.5)
    A = rho * rand_u(4); B = sig * rand_u(4); U = rand_u(4)
    if abs(smin(A @ U @ B.conj().T) - rho * sig) > 1e-9: ok_rad = False
strict2 = False
for trial in range(60):
    sa2 = np.sort(rng.uniform(0.4, 2.0, size=4)); sb2 = np.sort(rng.uniform(0.4, 2.0, size=4))
    if sa2[-1] > 1.5 * sa2[0] and sb2[-1] > 1.5 * sb2[0]:
        M2 = phi_with_svals(sa2) @ rand_u(4) @ phi_with_svals(sb2).conj().T
        if smin(M2) > sa2[0] * sb2[0] * 1.05:
            strict2 = True
chk("R2 smin(AUB^dag) >= smin(A)smin(B) (60)", ok2)
chk("R2 equality on radial shells rho*U (30)", ok_rad)
chk("R2 TOOTH strict for non-radial fibers", strict2)
chk("R2 det multiplicativity (60)", okdet)

print("== R3 ==")
v, lam = 1.7, 2.3
ok3 = True; okth = True; okdetb = True
for trial in range(80):
    eps = lam * v**4 / 4 * rng.uniform(0.0, 0.999)
    vlo2 = max(v**2 - 2 * np.sqrt(eps / lam), 0.0)
    sv = np.sort(np.sqrt(np.full(4, vlo2)) + np.abs(rng.standard_normal(4)) * 0.05)
    Phi = phi_with_svals(sv)
    Q = Phi @ Phi.conj().T
    if abs(smin(Q) - sv[0]**2) > 1e-10 * max(1.0, sv[0]**2): ok3 = False
    if smin(Q) < vlo2 - 1e-12: okth = False
    re = v - np.sqrt(max(v**2 - 2 * np.sqrt(eps / lam), 0.0))
    if abs((1 - re / v)**4 - (vlo2 / v**2)**2) > 1e-12: okth = False
    # det lower bound: prod sigma_i^2 >= vlo2^4 = ((vlo2/v^2) v^2)^4 / ...
    if np.prod(sv**2) < vlo2**4 * (1 - 1e-12): okdetb = False
chk("R3 smin(Phi Phi^dag)=smin(Phi)^2 (80)", ok3)
chk("R3 threshold chain vs recorded form", okth)
chk("R3 det bound prod sv^2 >= vlo2^4", okdetb)
svd = np.array([1e-7, v, v, v]); Vd = lam / 4 * np.sum((svd**2 - v**2)**2)
chk("R3 TOOTH sv=(0,v,v,v) at threshold", Vd <= lam * v**4 / 4 * 1.0001 and smin(np.diag(svd)) < 1e-6)

print("== R5 ==")
d = 6
okp = True
for trial in range(30):
    X = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    H = X @ X.conj().T + 0.4 * np.eye(d)
    r = 2 + trial % 4
    Qm = rand_u(d)
    P = Qm @ np.diag([1.0]*r + [0.0]*(d-r)) @ Qm.conj().T
    w = np.sort(np.abs(np.linalg.eigvalsh(P @ H @ P)))
    if w[d - r] < 0.4 - 1e-10: okp = False
chk("R5 compression of H>=s keeps s (30)", okp)
found = False
for trial in range(300):
    X = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    s = smin(X)
    P = np.zeros((d, d), dtype=complex); P[0, 0] = 1
    if abs((P @ X @ P)[0, 0]) < 0.5 * s:
        found = True
chk("R5 TOOTH non-positive compresses below s", found)

print("== R6 ==")
ok6 = True
for trial in range(30):
    Nb, df = 4, 4
    svl, svu = 0.6, 2.5
    sv = np.sort(rng.uniform(svl, svu, size=(Nb, df)), axis=1)
    blocks = [phi_with_svals(sv[i]) for i in range(Nb)]
    Mphi = block_diag(blocks, df)
    Wb = rng.standard_normal((Nb, Nb)) + 1j * rng.standard_normal((Nb, Nb))
    TW = np.kron(Wb, np.eye(df))
    T = Mphi @ TW @ Mphi.conj().T
    if smax(T) / smin(T) > (smax(TW) / smin(TW)) * (svu / svl)**2 + 1e-8:
        ok6 = False
chk("R6 kappa transfer (30)", ok6)

print("== S1 SUMMARY ==")
print("FAILURES: %d %s" % (len(fails), fails if fails else "(none)"))
