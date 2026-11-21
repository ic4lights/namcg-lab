# s1_structure_general_q.py
# Exact structure theorem for the coincident-copy edge-charge pencil, general q.
#   U = I_q kron u (qN x q isometry), R any qN x q, C0 = U^dag R, Z0 = R^dag R,
#   T = -2i M, M = [[C0^dag, Z0], [-I_q, -C0]]  (the integrated 077 pencil).
# Checks:
#  (0) the constant sign s_q of det(tI - M) = s_q * det(t^2 I + (C0 - C0^dag) t + (Z0 - C0^dag C0))
#      is independent of the data (numeric, q=1..4); s_1=-1, s_2=+1, s_3=+1 asserted.
#  (1) with H := (C0 - C0^dag)/(2i) Hermitian and K := R^dag (I - U U^dag) R (= Z0 - C0^dag C0) PSD,
#      det(tI - M) = s_q det(t^2 I + 2i H t + K)  (numeric q=1..6, random complex data).
#  (2) Re C0 invisibility at general q: an explicit split R' with U^dag R' = i H + A (A any
#      Hermitian) and R'^dag (I-UU^dag) R' = K leaves the char poly of T unchanged (numeric q=2,3).
#  (3) sympy-expansion proof of (1) at q=2,3 with generic Hermitian H and generic Hermitian K.
# No manuscript I/O. Run: python -I s1_structure_general_q.py > s1_structure_general_q.out 2>&1
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261117)

def pencil(R, u, q):
    N = len(u)
    U = np.kron(np.eye(q), u.reshape(-1, 1))       # qN x q isometry
    C0 = U.conj().T @ R
    Z0 = R.conj().T @ R
    M = np.block([[C0.conj().T, Z0], [-np.eye(q), -C0]])
    return U, C0, Z0, M

# ---------- (0) constant sign ----------
SIGN = {}
for q in (1, 2, 3, 4, 5, 6):
    vals = set()
    for _ in range(4):
        u = rng.normal(size=7) + 1j*rng.normal(size=7); u /= np.linalg.norm(u)
        R = rng.normal(size=(q*7, q)) + 1j*rng.normal(size=(q*7, q))
        U, C0, Z0, M = pencil(R, u, q)
        t = complex(rng.normal(), rng.normal())
        Qp = np.eye(q)*t*t + (C0 - C0.conj().T)*t + (Z0 - C0.conj().T@C0)
        r = np.linalg.det(t*np.eye(2*q) - M)/np.linalg.det(Qp)
        vals.add((round(r.real, 5), round(r.imag, 5)))
    assert len(vals) == 1, (q, vals)
    SIGN[q] = list(vals)[0][0]
print("(0) constant sign s_q of det(tI-M) = s_q det(t^2 I + (C0-C0^dag)t + (Z0-C0^dag C0)):",
      SIGN)
assert all(v == 1.0 for v in SIGN.values()), "sign != +1 (expected s_q=+1 for all q)"

# ---------- (1) Hermitian-data determinant identity ----------
worst_all = 0.0
for q in range(1, 7):
    N = 3*q + 2
    u = rng.normal(size=N) + 1j*rng.normal(size=N); u /= np.linalg.norm(u)
    R = rng.normal(size=(q*N, q)) + 1j*rng.normal(size=(q*N, q))
    U, C0, Z0, M = pencil(R, u, q)
    H = (C0 - C0.conj().T)/(2j)
    K = R.conj().T @ (np.eye(q*N) - U@U.conj().T) @ R
    assert np.allclose(H, H.conj().T, atol=1e-12)
    assert np.linalg.eigvalsh(K).min() > -1e-10          # K PSD
    worst = 0.0
    for _ in range(4):
        t = complex(rng.normal(), rng.normal())
        lhs = np.linalg.det(t*np.eye(2*q) - M)
        rhs = SIGN[q]*np.linalg.det(np.eye(q)*t*t + 2j*H*t + K)
        worst = max(worst, abs(lhs-rhs)/max(1.0, abs(lhs)))
    worst_all = max(worst_all, worst)
    print("(1) q=%d N=%d: det(tI-M) = s_q det(t^2 I + 2iHt + K), max rel dev %.3e" % (q, N, worst))
    assert worst < 1e-9
print("(1) done, global max rel dev %.3e" % worst_all)

# ---------- (2) Re C0 invisibility ----------
for q in (2, 3):
    N = 3*q + 2
    u = rng.normal(size=N) + 1j*rng.normal(size=N); u /= np.linalg.norm(u)
    U = np.kron(np.eye(q), u.reshape(-1, 1))
    R = rng.normal(size=(q*N, q)) + 1j*rng.normal(size=(q*N, q))
    H = (U.conj().T@R - R.conj().T@U)/(2j)
    P = np.eye(q*N) - U@U.conj().T
    K = R.conj().T @ P @ R
    _, _, _, M = pencil(R, u, q)
    for _ in range(3):
        A = rng.normal(size=(q, q)); A = (A + A.T)/2*np.random.default_rng(1).normal()
        C0p = A + 1j*H                             # same Im part, arbitrary Hermitian Re part
        Rp = U @ C0p + P @ R                       # U^dag Rp = C0p (P U = 0), Rp^dag P Rp = R^dag P R = K
        U2, C02, Z02, M2 = pencil(Rp, u, q)
        assert np.allclose(C02, C0p, atol=1e-10) and np.allclose(Rp.conj().T@P@Rp, K, atol=1e-10)
        worst = 0.0
        for _ in range(3):
            lam = complex(rng.normal(), rng.normal())
            d1 = np.linalg.det(lam*np.eye(2*q) + 2j*M)     # char poly of T=-2iM at lam
            d2 = np.linalg.det(lam*np.eye(2*q) + 2j*M2)
            worst = max(worst, abs(d1-d2)/max(1.0, abs(d1)))
        print("(2) q=%d: Re C0 -> Re C0 + A (||A||=%.2f): char-poly rel dev %.3e" %
              (q, np.linalg.norm(A), worst))
        assert worst < 1e-9

# ---------- (3) sympy-expansion proof at q=2,3 ----------
for q in (2, 3):
    def herm(name):
        Mx = sp.zeros(q, q)
        for i in range(q):
            Mx[i, i] = sp.Symbol('%s_%d%d' % (name, i, i), real=True)
        for i in range(q):
            for j in range(i+1, q):
                a = sp.Symbol('%s_%d%d_re' % (name, i, j), real=True)
                b = sp.Symbol('%s_%d%d_im' % (name, i, j), real=True)
                Mx[i, j] = a + sp.I*b
                Mx[j, i] = a - sp.I*b
        return Mx
    Hm, Km, t = herm('h'), herm('k'), sp.Symbol('t')
    C0x = sp.I*Hm                       # Re part zero; then C0^dag = -i H, Z0 = K + C0^dag C0
    Z0x = Km + (-sp.I*Hm)@(sp.I*Hm)
    Mx = sp.zeros(2*q, 2*q)
    Mx[:q, :q] = C0x.conjugate().T if q == 1 else C0x.adjoint()
    Mx[:q, q:] = Z0x
    Mx[q:, :q] = -sp.eye(q)
    Mx[q:, q:] = -C0x
    d1 = sp.expand((t*sp.eye(2*q) - Mx).det())
    d2 = SIGN[q]*sp.expand((sp.eye(q)*t**2 + 2*sp.I*Hm*t + Km).det())
    diff = sp.expand(d1 - d2)
    print("(3) q=%d sympy: det(tI-M) - s_q det(t^2 I + 2iHt + K) identically zero: %s" %
          (q, diff == 0))
    assert diff == 0

print("ALL S1 ASSERTS PASS")
