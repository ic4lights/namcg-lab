# verify_r115.py -- checks for proposal 115-d1-frame-nondeg-defect-threshold
# Run:  python -I verify_r115.py     (deterministic, seed 115; numpy + sympy only)
#
# Objects (chapters/ch03-matrix-action.tex):
#   eq:V  V(Phi) = (lambda/4) Tr (Phi^dagger Phi - v^2 I)^2 ,  Phi a complex 4x4.
#   eq:vacuum-manifold  Phi^dagger Phi = v^2 I.
# Checks:
#  A1 vacuum manifold v*U(4): V = 0 and |det Phi| = v^4 (with U(1) phase).
#  A2 Phi^dagger Phi = v^2 I forces Phi Phi^dagger = v^2 I (invertibility).
#  B1 symbolic: inf of 4V/lambda over singular values with sigma_min = 0 is
#     v^4, attained at (0,v,v,v):  f - v^4 = sum_{i>=2} (sigma_i^2 - v^2)^2.
#  B2 numerical: min of V over rank-3 matrices (det Phi = 0) is lambda v^4/4.
#  B3 contrapositive + quantitative bound: V <= eps < lambda v^4/4 forces every
#     sigma_i^2 >= v^2 - sqrt(4 eps/lambda), |det Phi| >= (v^2 - sqrt(4 eps/lambda))^2,
#     |det e| = |det Phi|/v^4 >= (1 - sqrt(4 eps/lambda)/v^2)^2 (Repair II e = Phi/v).
#  C1 symbolic boost: V(v*Omega(t)) = 2 lambda v^4 cosh(2t) sinh^2(t); det(Om^T Om)=1.
#  C2 quadratic limit matches recorded V^(2)(d = v B) = 2 lambda v^4 (appH L2158).
#  C3 random Lorentz orbit: V(v Om) = (lambda v^4/4)||Om^T Om - I||_F^2 >= 0,
#     = 0 on SO(3), > 0 iff a boost is present; Omega^T eta Omega = eta.
#  C4 SO(3) subgroup: V(v Omega) = 0 exactly (three flat directions).
import numpy as np
import sympy as sp

rng = np.random.default_rng(115)
v = 1.37
lam = 0.83
I4 = np.eye(4, dtype=complex)
eta = np.diag([-1.0, 1.0, 1.0, 1.0])

def cV(Phi):
    D = Phi.conj().T @ Phi - (v * v) * I4
    return 0.25 * lam * float(np.real(np.trace(D @ D)))

def randU(n=4):
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    Q, R = np.linalg.qr(A)
    return Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))

def expm(M):
    s = 8
    A = M / (2.0 ** s)
    E = np.eye(len(M), dtype=complex)
    T = np.eye(len(M), dtype=complex)
    for k in range(1, 26):
        T = T @ A / k
        E = E + T
    for _ in range(s):
        E = E @ E
    return E

ok = []
def chk(name, cond, info=""):
    ok.append(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + info if info else ""))

# ---------- A: vacuum manifold ----------
worstV = 0.0; worstD = 0.0
for _ in range(200):
    th = rng.uniform(0, 2 * np.pi)
    Phi = v * np.exp(1j * th) * randU()
    worstV = max(worstV, cV(Phi))
    worstD = max(worstD, abs(abs(np.linalg.det(Phi)) - v ** 4))
chk("A1 V=0 and |det Phi|=v^4 on v*U(4)*phase", worstV < 1e-12 and worstD < 1e-10,
    f"maxV={worstV:.3e} max|det|dev={worstD:.3e}")
worstA2 = 0.0
for _ in range(50):
    U = randU(); P = v * U
    worstA2 = max(worstA2, np.max(np.abs(P @ P.conj().T - (v * v) * I4)))
chk("A2 Phi^dag Phi=v^2 I => Phi Phi^dag=v^2 I", worstA2 < 1e-10, f"max={worstA2:.3e}")

# ---------- B: defect threshold ----------
s2, s3, s4, vv = sp.symbols("s2 s3 s4 v", positive=True)
f = (0 - vv ** 2) ** 2 + (s2 ** 2 - vv ** 2) ** 2 + (s3 ** 2 - vv ** 2) ** 2 + (s4 ** 2 - vv ** 2) ** 2
resid = sp.simplify(f - (vv ** 4 + (s2 ** 2 - vv ** 2) ** 2 + (s3 ** 2 - vv ** 2) ** 2 + (s4 ** 2 - vv ** 2) ** 2))
chk("B1 symbolic: 4V/lambda|(s1=0) - v^4 = sum (s_i^2-v^2)^2 (squares >= 0)",
    resid == 0 and f.subs({s2: vv, s3: vv, s4: vv}) == vv ** 4)
th4 = lam * v ** 4 / 4.0
best = np.inf
for _ in range(40000):
    u = rng.uniform(0.0, 2.0 * v, 3)
    Phi = randU() @ np.diag(np.array([0.0, u[0], u[1], u[2]])) @ randU().conj().T
    best = min(best, cV(Phi))
chk("B2 min V over det Phi=0 >= lambda v^4/4 (= %g), sampled min close" % th4,
    best >= th4 - 1e-12 and best < th4 * 1.02, f"min={best:.6f} th={th4:.6f}")
eps = 0.3 * th4
sq = v * v - np.sqrt(4.0 * eps / lam)
bad = 0; nused = 0; worstm = np.inf
for _ in range(200000):
    t = rng.uniform(0, 0.6)
    Phi = v * randU() @ (I4 + t * (rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))))
    V = cV(Phi)
    if V <= eps:
        nused += 1
        sg = np.linalg.svd(Phi, compute_uv=False) ** 2
        dete = abs(np.linalg.det(Phi)) / v ** 4
        worstm = min(worstm, dete - sq * sq / v ** 4)
        if np.any(sg < sq - 1e-12) or dete < (sq / (v * v)) ** 2 - 1e-12:
            bad += 1
chk("B3 V<=eps => sigma_i^2>=v^2-sqrt(4eps/lam) and |det e|>=(1-sqrt(4eps/lam)/v^2)^2",
    bad == 0 and nused > 100, f"n={nused} viol={bad} worst det e margin={worstm:.3e}")

# ---------- C: internal SO(3,1) orbit ----------
t, lams, vs = sp.symbols("t lambda v", positive=True)
Om = sp.Matrix([[sp.cosh(t), sp.sinh(t), 0, 0],
                [sp.sinh(t), sp.cosh(t), 0, 0],
                [0, 0, 1, 0], [0, 0, 0, 1]])
M2 = Om.T @ Om - sp.eye(4)
Vor = sp.simplify((lams * vs ** 4 / 4) * (M2 * M2).trace())
chk("C1 symbolic: V(v Om(t)) = 2 lambda v^4 cosh(2t) sinh^2(t); det(Om^T Om)=1",
    sp.simplify(Vor - 2 * lams * vs ** 4 * sp.cosh(2 * t) * sp.sinh(t) ** 2) == 0
    and sp.simplify((Om.T @ Om).det() - 1) == 0)
series = sp.series(Vor.subs({lams: 1.0, vs: 1.0}), t, 0, 4).removeO()
chk("C2 quadratic term 2 t^2 matches recorded V^(2)(d=vB)=2 lambda v^4",
    sp.simplify(series - 2 * t ** 2) == 0)
K0 = np.zeros((4, 4)); K0[0, 1] = K0[1, 0] = 1.0
K1 = np.zeros((4, 4)); K1[0, 2] = K1[2, 0] = 1.0
K2 = np.zeros((4, 4)); K2[0, 3] = K2[3, 0] = 1.0
J0 = np.zeros((4, 4)); J0[1, 2] = -1.0; J0[2, 1] = 1.0
J1 = np.zeros((4, 4)); J1[1, 3] = -1.0; J1[3, 1] = 1.0
J2 = np.zeros((4, 4)); J2[2, 3] = -1.0; J2[3, 2] = 1.0
worstId = 0.0; worstEta = 0.0; worstNeg = 0.0; worstZero = 0.0; nboost0 = 0
for _ in range(3000):
    a = rng.standard_normal(3) * rng.choice([0.0, 1.0])
    th = rng.standard_normal(3)
    Om = expm(sum(a[i] * [K0, K1, K2][i] for i in range(3))
              + sum(th[i] * [J0, J1, J2][i] for i in range(3)))
    Mx = Om.T @ Om - np.eye(4)
    Vor_n = 0.25 * lam * v ** 4 * float(np.real(np.sum(Mx * Mx)))
    Dn = 0.25 * lam * float(np.real(np.trace(
        (v * v * (Om.conj().T @ Om) - v * v * np.eye(4))
        @ (v * v * (Om.conj().T @ Om) - v * v * np.eye(4)))))
    worstId = max(worstId, abs(Vor_n - Dn))
    worstEta = max(worstEta, np.max(np.abs(Om.T @ eta @ Om - eta)))
    worstNeg = min(worstNeg, Vor_n)
    if np.allclose(a, 0.0):
        nboost0 += 1
        worstZero = max(worstZero, Vor_n)
    else:
        if Vor_n <= 1e-9:
            worstNeg = -1.0
chk("C3 V(v Om)=(lambda v^4/4)||Om^T Om-I||^2 >=0, zero iff pure rotation, Om^T eta Om=eta",
    worstId < 1e-9 and worstEta < 1e-9 and worstNeg > -1e-12 and nboost0 > 100,
    f"idmax={worstId:.2e} etapremax={worstEta:.2e} minV={worstZero:.2e} pureRotMaxV={worstZero:.2e}")
worstRot = 0.0
for _ in range(500):
    th = rng.standard_normal(3)
    Omr = expm(sum(th[i] * [J0, J1, J2][i] for i in range(3)))
    worstRot = max(worstRot, cV(v * Omr.astype(complex)))
chk("C4 SO(3) subgroup: V(v Om)=0 exactly (3 flat directions)", worstRot < 1e-12,
    f"max={worstRot:.3e}")

print("threshold lambda v^4/4 = %.10g ; sqrt(4 eps/lam) = %.10g" % (th4, np.sqrt(4 * eps / lam)))
print("ALL CHECKS PASSED (seed 115)" if all(ok) else "SOME CHECKS FAILED")
raise SystemExit(0 if all(ok) else 1)
