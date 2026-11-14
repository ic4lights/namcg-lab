"""
067 e2: what the trace norm T = Tr E^{1/2} of the edge map measures (e1 gives E diagonal on toric blocks).

(A) Pointwise identity (any 4-dim leaf, any embedding with positive contraction, any covector n = df):
      K^{mu nu} n_mu n_nu = sum_I {f, x^I}^2,      K = theta g theta^T,  g = dx^T dx,  rho = 1/|Pf theta|,
      rho sqrt(K^{00}) = (sqrt g / rho) sqrt(det_3 K^{-1}|_{ij}) = sqrt(det_3 gt_{ij}),  gt = (sqrt g/rho)^{2/3} K^{-1},
    in coordinates with f = y^0.  So  P_K := (2 pi)^{-2} int rho d^4y delta(f) sqrt(K(df,df))  is (2 pi)^{-2} times the
    3-volume of the level set in the tensor gt.
(B) Block cap x whole second sphere on X = (A1 J (x) 1, 1 (x) A2 J): edge map of rank N, T = N s1, independent of A2
    (finite N, from the formula proved in the proposal and checked against the operator in e1), and
      sqrt2 T / P_K = rms_phi |A1 e_phi| / mean_phi |A1 e_phi| >= 1, equality iff sigma_1 = sigma_2,
    with P_K evaluated with R^2 sin^2(theta) -> M1 (N - M1) as in 065.
    Scaling exponents of T and of the edge 3-volume in g, K^{-1}, gt under A1 -> lam A1 and A2 -> lam A2.
(C) Oblique half-plane blocks a i1 + b i2 < c on the round product: T (lattice formula) against the crystalline
    density  tau(n) = (n_max - n_min) sqrt(e_dir(max)) + n_min sqrt(e1 + e2)  and against sqrt(n1^2 e1 + n2^2 e2)
    (= density of P_K / sqrt2 on the round product), per unit Euclidean length of the boundary in the (i1, i2) plane,
    n the unit normal, e_f = k_f i_f (N - i_f).
Output to stdout only.
"""
import numpy as np

rng = np.random.default_rng(67002)

# ---------------------------------------------------------------- (A)
worst = 0.0
for t in range(200):
    B = rng.normal(size=(4, 4)); th = B - B.T                      # theta^{alpha beta}
    dx = rng.normal(size=(6, 4))                                   # d_alpha x^I
    g = dx.T @ dx
    K = th.T @ g @ th                                              # K^{mu nu} = theta^{alpha mu} g_{alpha beta} theta^{beta nu}
    rho = 1.0 / np.sqrt(abs(np.linalg.det(th)))                    # 1/|Pf theta|
    n = np.array([1.0, 0, 0, 0])                                   # f = y^0
    pb = dx @ (th @ n)                                             # {x^I, f} = theta^{alpha beta} d_alpha x^I d_beta f
    lhs1 = n @ K @ n; rhs1 = (pb ** 2).sum()
    Kinv = np.linalg.inv(K)
    sg = np.sqrt(np.linalg.det(g))
    d3 = np.linalg.det(Kinv[1:, 1:])
    a = rho * np.sqrt(K[0, 0]); b = (sg / rho) * np.sqrt(d3)
    gt = (sg / rho) ** (2.0 / 3.0) * Kinv
    c = np.sqrt(np.linalg.det(gt[1:, 1:]))
    worst = max(worst, abs(lhs1 / rhs1 - 1), abs(a / b - 1), abs(a / c - 1))
print('(A) pointwise identities, 200 random (theta, dx): max relative deviation %.2e' % worst)
assert worst < 1e-8

# ---------------------------------------------------------------- (B)
def k_of(A):                                                       # (sigma_1^2 + sigma_2^2)/4 on the (1,2) plane
    return 0.25 * (A[:, 0] ** 2 + A[:, 1] ** 2).sum()

def T_fibre(N, M1, A1):                                            # cap (i1 < M1) x whole second sphere
    return N * np.sqrt(k_of(A1) * M1 * (N - M1))

def speed_stats(A, nphi=20000):
    ph = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    e = np.stack([-np.sin(ph), np.cos(ph), 0 * ph])
    sp = np.linalg.norm(A @ e, axis=0)
    return sp.mean(), np.sqrt((sp ** 2).mean())

def PK_fibre(N, M1, A1):                                           # (2pi)^-2 int dphi1 dI2 dphi2 |d_phi1 x|
    mean, rms = speed_stats(A1)
    return N * np.sqrt(M1 * (N - M1)) * mean

def edge_volumes(N, M1, A1, A2, n2=24, nphi=96):
    """3-volume of the edge {I1 = M1} in g, K^{-1} and gt, by quadrature in action-angle coordinates
    (I, phi) per sphere, omega = dI ^ dphi, x = R A n(theta, phi), cos(theta) = 1 - 2 I / N, R = N/2."""
    R = N / 2.0
    def jac(A, I, ph):
        ct = 1 - 2 * I / N; st = np.sqrt(max(1 - ct * ct, 0.0))
        dth_dI = (2.0 / N) / st
        dn_dth = np.array([ct * np.cos(ph), ct * np.sin(ph), -st])
        dn_dph = np.array([-st * np.sin(ph), st * np.cos(ph), 0.0])
        return R * np.stack([A @ dn_dth * dth_dI, A @ dn_dph], axis=1)   # 3 x 2, columns d_I, d_phi
    th2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
    theta = np.zeros((4, 4)); theta[:2, :2] = th2; theta[2:, 2:] = th2
    Vg = VK = Vt = PK = 0.0
    # Gauss-Legendre in I2 on (0, N), midpoint in the angles
    xs, ws = np.polynomial.legendre.leggauss(n2); I2s = 0.5 * N * (xs + 1); w2 = 0.5 * N * ws
    phs = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi; wph = 2 * np.pi / nphi
    for p1 in phs:
        J1 = jac(A1, float(M1), p1)
        for I2, wI in zip(I2s, w2):
            J2 = jac(A2, I2, 0.3)                                  # integrand below is averaged over phi2 explicitly
            for p2 in phs[:: max(1, nphi // 12)]:
                J2 = jac(A2, I2, p2)
                dx = np.zeros((6, 4)); dx[:3, :2] = J1; dx[3:, 2:] = J2
                g = dx.T @ dx; K = theta.T @ g @ theta; Kinv = np.linalg.inv(K)
                sg = np.sqrt(np.linalg.det(g)); idx = [1, 2, 3]
                w = wph * wI * (2 * np.pi / len(phs[:: max(1, nphi // 12)]))
                Vg += w * np.sqrt(np.linalg.det(g[np.ix_(idx, idx)]))
                VK += w * np.sqrt(np.linalg.det(Kinv[np.ix_(idx, idx)]))
                Vt += w * sg * np.sqrt(np.linalg.det(Kinv[np.ix_(idx, idx)]))      # rho = 1
                PK += w * np.sqrt(K[0, 0]) / (2 * np.pi) ** 2
    return Vg, VK, Vt, PK

N, M1 = 40, 13
A1 = rng.normal(size=(3, 3)); A2 = rng.normal(size=(3, 3))
print('(B) cap x whole second sphere, N=%d M1=%d, generic A1, A2' % (N, M1))
T0 = T_fibre(N, M1, A1)
mean, rms = speed_stats(A1)
print('    T = N s1 = %.6f ; P_K (closed form) = %.6f ; sqrt2 T / P_K = %.6f ; rms/mean speed = %.6f'
      % (T0, PK_fibre(N, M1, A1), np.sqrt(2) * T0 / PK_fibre(N, M1, A1), rms / mean))
assert abs(np.sqrt(2) * T0 / PK_fibre(N, M1, A1) - rms / mean) < 1e-9 and rms / mean > 1
Vg, VK, Vt, PK = edge_volumes(N, M1, A1, A2)
print('    quadrature: P_K = %.6f (closed form %.6f) ; (2pi)^-2 Vol_3[gt] = %.6f' % (PK, PK_fibre(N, M1, A1), Vt / (2 * np.pi) ** 2))
assert abs(PK / PK_fibre(N, M1, A1) - 1) < 1e-6 and abs(Vt / (2 * np.pi) ** 2 / PK - 1) < 1e-9
Ar = 1.3 * np.eye(3)
print('    round A1 = 1.3*1: sqrt2 T / P_K = %.12f' % (np.sqrt(2) * T_fibre(N, M1, Ar) / PK_fibre(N, M1, Ar)))
assert abs(np.sqrt(2) * T_fibre(N, M1, Ar) / PK_fibre(N, M1, Ar) - 1) < 1e-9

lam = 1.7
def expo(v1, v0): return np.log(v1 / v0) / np.log(lam)
V0 = edge_volumes(N, M1, A1, A2, n2=12, nphi=48)
V1 = edge_volumes(N, M1, lam * A1, A2, n2=12, nphi=48)
V2 = edge_volumes(N, M1, A1, lam * A2, n2=12, nphi=48)
rows = [('T (lattice, exact)', expo(T_fibre(N, M1, lam * A1), T0), 0.0),
        ('Vol_3 induced g', expo(V1[0], V0[0]), expo(V2[0], V0[0])),
        ('Vol_3 K^{-1}', expo(V1[1], V0[1]), expo(V2[1], V0[1])),
        ('Vol_3 gt = (sqrt g/rho)^{2/3} K^{-1}', expo(V1[2], V0[2]), expo(V2[2], V0[2])),
        ('P_K', expo(V1[3], V0[3]), expo(V2[3], V0[3]))]
print('    scaling exponents under (A1 -> lam A1, A2 -> lam A2):')
for name, e1, e2 in rows:
    print('      %-38s (%+.4f, %+.4f)' % (name, e1, e2))
exp_expected = [(1, 0), (1, 2), (-1, -2), (1, 0), (1, 0)]
for (name, e1, e2), (x1, x2) in zip(rows, exp_expected):
    assert abs(e1 - x1) < 1e-6 and abs(e2 - x2) < 1e-6, name

# ---------------------------------------------------------------- (C)
def T_lattice(N, Om, k1, k2):
    i = np.arange(N)
    up = (i + 1) * (N - i - 1)            # link i -> i+1
    dn = i * (N - i)                      # link i -> i-1
    out_up1 = np.ones_like(Om); out_up1[:-1, :] = ~Om[1:, :]; out_up1[-1, :] = False
    out_dn1 = np.ones_like(Om); out_dn1[1:, :] = ~Om[:-1, :]; out_dn1[0, :] = False
    out_up2 = np.ones_like(Om); out_up2[:, :-1] = ~Om[:, 1:]; out_up2[:, -1] = False
    out_dn2 = np.ones_like(Om); out_dn2[:, 1:] = ~Om[:, :-1]; out_dn2[:, 0] = False
    E = k1 * (up[:, None] * out_up1 + dn[:, None] * out_dn1) + k2 * (up[None, :] * out_up2 + dn[None, :] * out_dn2)
    E = np.where(Om, E, 0.0)
    return np.sqrt(E).sum(), E.sum(), int((E > 0).sum())

def line_integrals(N, a, b, c, k1, k2, npt=400001):
    """boundary a x1 + b x2 = c inside the square (0,N)^2; densities per unit Euclidean length."""
    nrm = np.hypot(a, b); n1, n2 = a / nrm, b / nrm
    # parametrise by x2 where 0 < x1 = (c - b x2)/a < N
    lo = max(0.0, (c - a * N) / b); hi = min(float(N), c / b)
    x2 = np.linspace(lo, hi, npt); x1 = (c - b * x2) / a
    e1 = k1 * x1 * (N - x1); e2 = k2 * x2 * (N - x2)
    dl = (hi - lo) / (npt - 1) * nrm / a                            # Euclidean length element
    if n1 >= n2: tau = (n1 - n2) * np.sqrt(e1) + n2 * np.sqrt(e1 + e2)
    else:        tau = (n2 - n1) * np.sqrt(e2) + n1 * np.sqrt(e1 + e2)
    riem = np.sqrt(n1 ** 2 * e1 + n2 ** 2 * e2)
    s2 = n1 * e1 + n2 * e2
    tr = lambda y: (y[1:] + y[:-1]).sum() * 0.5 * dl
    return tr(tau), tr(riem), tr(s2), max(n1, n2) * (hi - lo) * nrm / a

print('(C) half-plane blocks a i1 + b i2 < c on the round product (k1 = nu1^2/2, k2 = nu2^2/2)')
k1, k2 = 0.5 * 1.0 ** 2, 0.5 * 1.6 ** 2
for (a, b) in ((1.0, 0.0), (1.0, 1.0), (1.0, np.sqrt(2) - 1), (1.0, 1 / np.sqrt(3)), (np.sqrt(5) - 2, 1.0)):
    for N in (200, 800, 3200):
        ii1, ii2 = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
        c = 0.5 * (a + b) * N + 0.123
        Om = a * (ii1 + 0.5) + b * (ii2 + 0.5) < c
        T, s2, r = T_lattice(N, Om, k1, k2)
        if b == 0.0:
            M1 = int(Om[:, 0].sum()); Tc = N * np.sqrt(k1 * M1 * (N - M1)); Tr = Tc; s2c = N * k1 * M1 * (N - M1); rc = N
        else:
            Tc, Tr, s2c, rc = line_integrals(N, a, b, c, k1, k2)
        print('    b/a=%.4f N=%4d  T/T_cryst=%.5f  T/(P_K/sqrt2)=%.5f  s^2/int(n1 e1+n2 e2)=%.5f  rank/(max(n1,n2) L)=%.5f'
              % (b / a, N, T / Tc, T / Tr, s2 / s2c, r / rc))
        if N == 3200:
            assert abs(T / Tc - 1) < 2e-3 and abs(s2 / s2c - 1) < 2e-3 and abs(r / rc - 1) < 2e-3
            if b == 0.0 or a == b: assert abs(T / Tr - 1) < 2e-3
            else: assert T / Tr > 1.01
print('PASS e2')
