"""049 r2 s8: first term with the fibre flux on the background. New mathematics of round 2. Prints only.

On the background the flux operator is the action J_ab of so(3,1) on functions (merged: commutes with Box), so
  Z_Sigma = C_tot - C_orb - C_Sigma,   C = (1/2) J_ab J^ab with real (anti-Hermitian) generators on the vector.
Writing so(3,1) over C as su(2)_A + su(2)_B, with labels Lam_A = 2 j_A + 1, Lam_B = 2 j_B + 1:
  per state of an irreducible orbital component, with P(Lam) = exp(-s)[2 cosh(s Lam) + 2 sinh(s Lam)/Lam],
  tr_D e^{-sZ} = P(Lam_A) + P(Lam_B),  tr_V e^{-sZ} = P(Lam_A) P(Lam_B),
  tr_V - 2 tr_D + 4 = (P_A - 2)(P_B - 2).
On a unitary principal-series component Lam_A = m + i r, Lam_B = -m + i r (r real, m integer), so P_B = conj(P_A)
and the first-term integrand is |P_A - 2|^2 >= 0.

(A) Sign and normalisation of Z: singlet value on orbital = vector, the S^2_N spectra, the identity at finite-dimensional
    labels with explicit vector and gamma matrices.
(B) Level J: Plancherel average over (m, r) with weight (r^2 + m^2), H_0 = N^2/th + mu_J, N^2 = r^2 + 1 - m^2 + J(J+1).
    Scaling form W_J = s^2 [ (15/4) th^2 - s th c + s^2 c^2 ], c = J(J+1); identity f(z) = z^2 - z + 15/4.
(C) Direct commuting-N polynomial, without the Casimir identity.
(D) Exact Plancherel integrals against the scaling form; frozen limit.
(E) Level-resolved Y and L' on S^2_N.
"""
import numpy as np
import scipy.linalg as sl
import mpmath as mp
import sympy as sp

np.set_printoptions(precision=6, suppress=True)
eta = np.diag([-1.0, 1.0, 1.0, 1.0])


def vec_gens():
    """(J^{ab})^c_d = eta^{ac} delta^b_d - eta^{bc} delta^a_d, real matrices."""
    G = {}
    for a in range(4):
        for b in range(4):
            M = np.zeros((4, 4), dtype=complex)
            for c in range(4):
                for d in range(4):
                    M[c, d] = eta[a, c] * (b == d) - eta[b, c] * (a == d)
            G[(a, b)] = M
    return G


def gammas():
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    e = np.eye(2, dtype=complex)
    g0 = 1j * np.kron(s1, e)
    g = [g0] + [np.kron(s2, s) for s in (s1, s2, s3)]
    return g, np.kron(s3, e)


def dir_gens(sign=1):
    g, chi = gammas()
    G = {}
    for a in range(4):
        for b in range(4):
            # lower-index gammas are g[a]*eta; generators with the same structure constants as vec_gens up to a tested sign
            G[(a, b)] = sign * 0.25 * (g[a] @ g[b] - g[b] @ g[a])
    return G, chi


def su2(j):
    d = int(round(2 * j + 1))
    m = np.array([j - k for k in range(d)])
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((d, d), dtype=complex)
    for k in range(d - 1):
        Jp[k, k + 1] = np.sqrt(j * (j + 1) - m[k + 1] * (m[k + 1] + 1))
    return (Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, Jz


def low(a, b):
    return eta[a, a] * eta[b, b]


def casimir(G):
    d = G[(0, 0)].shape[0]
    C = np.zeros((d, d), dtype=complex)
    for a in range(4):
        for b in range(4):
            C = C + 0.5 * low(a, b) * G[(a, b)] @ G[(a, b)]
    return C


def struct_test(G, V):
    """Same commutators as the vector: [G^{01},G^{12}] etc. expressed by the structure constants read from V."""
    keys = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    basis = np.array([V[k].flatten() for k in keys]).T
    res = 0.0
    for k1 in keys:
        for k2 in keys:
            cv = V[k1] @ V[k2] - V[k2] @ V[k1]
            co = np.linalg.lstsq(basis, cv.flatten(), rcond=None)[0]
            cg = G[k1] @ G[k2] - G[k2] @ G[k1]
            pred = sum(c * G[k] for c, k in zip(co, keys))
            res = max(res, np.abs(cg - pred).max())
    return res


def orbital(jA, jB, V):
    """Build J^{ab} on (jA, jB) with the commutators of V; the choice of K sign is tested."""
    A = su2(jA)
    B = su2(jB)
    dA, dB = A[0].shape[0], B[0].shape[0]
    Ia, Ib = np.eye(dA), np.eye(dB)
    Aa = [np.kron(x, Ib) for x in A]
    Bb = [np.kron(Ia, x) for x in B]
    L = [x + y for x, y in zip(Aa, Bb)]
    K = [x - y for x, y in zip(Aa, Bb)]
    for sl_ in (1, -1):
        for sk in (1, -1):
            G = {}
            G[(0, 0)] = np.zeros_like(L[0])
            for i in range(3):
                G[(i + 1, i + 1)] = np.zeros_like(L[0])
                G[(0, i + 1)] = sk * K[i]
                G[(i + 1, 0)] = -sk * K[i]
            for (i, j, k) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
                G[(i + 1, j + 1)] = sl_ * 1j * L[k]
                G[(j + 1, i + 1)] = -sl_ * 1j * L[k]
            if struct_test(G, V) < 1e-10:
                return G
    raise RuntimeError("no sign choice reproduces the structure constants")


def Zop(G, S):
    """Z = C_tot - C_orb - C_S with total generators G x 1 + 1 x S; equals sum_{ab} low(a,b) G^{ab} x S^{ab}."""
    d1 = G[(0, 0)].shape[0]
    d2 = S[(0, 0)].shape[0]
    Z = np.zeros((d1 * d2, d1 * d2), dtype=complex)
    for a in range(4):
        for b in range(4):
            Z = Z + low(a, b) * np.kron(G[(a, b)], S[(a, b)])
    return Z


def P(Lam, s):
    return np.exp(-s) * (2 * np.cosh(s * Lam) + 2 * np.sinh(s * Lam) / Lam)


print("(A) sign and normalisation")
V = vec_gens()
D, chi5 = dir_gens(1)
print("    Dirac generators reproduce the vector commutators, residual:", struct_test(D, V), "(sign +1)")
print("    C on vector:", np.round(casimir(V)[0, 0].real, 12), " C on Dirac:", np.round(casimir(D)[0, 0].real, 12))
Z1 = Zop(V, V)
w1 = np.linalg.eigvals(Z1)
print("    orbital = vector, spin = vector: eigenvalues of Z:", sorted(set(np.round(w1.real, 8))), " singlet (9 = 3 H_0 on T_a, H_0 T_a = 3 T_a, requires Z = +6)")
print("    H_V T_a = H_0 T_a + 2[[T_a,T_b],T^b] = 3 H_0 T_a is an identity of the double commutator; on S^2_N, 3*2 = 6 is the closed value at l=1, j=0.")
print("    so(3) analogue: real generators, Z = C_tot - C_orb - C_S with C = (1/2) J_ij J_ij, against the closed vector spectrum of S^2_N")
for l in (1, 2, 3):
    Lx = su2(l)
    Jo = {(0, 1): 1j * Lx[2], (1, 2): 1j * Lx[0], (2, 0): 1j * Lx[1]}
    # real generators in the vector
    Sv = {(0, 1): np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]], dtype=complex), (1, 2): np.array([[0, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=complex), (2, 0): np.array([[0, 0, -1], [0, 0, 0], [1, 0, 0]], dtype=complex)}
    cJ = Jo[(0, 1)] @ Jo[(1, 2)] - Jo[(1, 2)] @ Jo[(0, 1)]
    cS = Sv[(0, 1)] @ Sv[(1, 2)] - Sv[(1, 2)] @ Sv[(0, 1)]
    ratio = [np.trace(cJ.conj().T @ Jo[(2, 0)]) / np.trace(Jo[(2, 0)].conj().T @ Jo[(2, 0)]), np.trace(cS.conj().T @ Sv[(2, 0)]) / np.trace(Sv[(2, 0)].conj().T @ Sv[(2, 0)])]
    print("      commutators [J01,J12] = k J20, k on orbital and on vector:", np.round(ratio, 10))
    best = None
    for sg in (1, -1):
        Zs = sum(2 * np.kron(sg * Jo[k], Sv[k]) for k in Jo)
        ev = np.round(np.sort((np.linalg.eigvals(Zs) + l * (l + 1)).real), 6)
        tgt = np.sort([l * (l - 1)] * (2 * l + 3) + [l * (l + 1) + 2] * (2 * l + 1) + [(l + 1) * (l + 2)] * (2 * l - 1))
        if np.allclose(ev, tgt):
            best = sg
    print("      l=%d closed spectrum reproduced for the commutator-consistent sign: %s" % (l, best))
print("    identity at finite-dimensional labels (explicit vector and gamma matrices; per state)")
g, chi = gammas()
for (jA, jB) in ((0.5, 0.5), (1, 0), (1, 1), (1.5, 0.5), (2, 1), (2.5, 1.5)):
    G = orbital(jA, jB, V)
    dim = G[(0, 0)].shape[0]
    ZV = Zop(G, V)
    ZD = Zop(G, D)
    res = []
    for s in (0.05, 0.3, 1.1):
        tV = np.trace(sl.expm(-s * ZV)) / dim
        tD = np.trace(sl.expm(-s * ZD)) / dim
        PA, PB = P(2 * jA + 1, s), P(2 * jB + 1, s)
        res.append(max(abs(tD - (PA + PB)), abs(tV - PA * PB), abs(tV - 2 * tD + 4 - (PA - 2) * (PB - 2))))
    print("      (jA,jB)=(%.1f,%.1f) dim %d max residual %.2e" % (jA, jB, dim, max(res)))

print("(B) scaling form")
t, u, z = sp.symbols("t u z", positive=True)
print("    moments with (r^2+m^2)^3 e^{-t r^2} over int r^2 e^{-t r^2}: 15/(4t^2) + (9/2) m^2/t + 3 m^4 + 2 t m^6")
r = sp.Symbol("r", positive=True)
mm = sp.Symbol("m", positive=True)
I1 = sp.integrate(r ** 2 * sp.exp(-t * r ** 2), (r, 0, sp.oo))
print("      check:", sp.simplify(sp.integrate((r ** 2 + mm ** 2) ** 3 * sp.exp(-t * r ** 2), (r, 0, sp.oo)) / I1 - (sp.Rational(15, 4) / t ** 2 + sp.Rational(9, 2) * mm ** 2 / t + 3 * mm ** 4 + 2 * t * mm ** 6)))
mp.mp.dps = 40
for zz in (mp.mpf("0.1"), mp.mpf(1), mp.mpf(7), mp.mpf(40)):
    val = mp.exp(-zz) * mp.quad(lambda v: mp.exp(zz * v * v) * (mp.mpf(15) / 4 + mp.mpf(9) / 2 * zz * v ** 2 + 3 * zz ** 2 * v ** 4 + 2 * zz ** 3 * v ** 6), [0, 0.5, 0.9, 1])
    print("    f(%s) by quadrature %s ; z^2 - z + 15/4 = %s" % (mp.nstr(zz, 4), mp.nstr(val, 20), mp.nstr(zz ** 2 - zz + mp.mpf(15) / 4, 20)))
print("    by parts: with M_k = int_0^1 u^{2k} e^{z u^2} du, (2k+1) M_k + 2 z M_{k+1} = e^z, hence the identity for every z.")
print("    normalisation: (1/(2J+1)) Sum_m e^{t(m^2-1-c)} (r^2+m^2 moment) against e^{-t} at small t (a_1 = R/6 on the slice, independent of J)")
for J in (0, 1, 2, 5):
    c_ = J * (J + 1)
    for t_ in (1e-3,):
        v = np.mean([np.exp(t_ * (m * m - 1 - c_)) * (1 + 2 * t_ * m * m) for m in range(-J, J + 1)])
        print("      J=%d t=%.0e value %.9f e^{-t} %.9f" % (J, t_, v, np.exp(-t_)))

print("(C) commuting N: (1/24)(tr_V Z^4 - 2 tr_D Z^4)/(2J+1), N = (0,0,n), spin J matrices; expected top terms n^4 - (2/3) c n^2 + c^2")
n = sp.Symbol("n", real=True)
Vs = {k: sp.Matrix(np.round(v.real, 0).astype(int).tolist()) for k, v in V.items()}


def dsym():
    return {k: sp.Matrix(4, 4, lambda i, j: sp.nsimplify(complex(v[i, j]).real) + sp.I * sp.nsimplify(complex(v[i, j]).imag)) for k, v in D.items()}


Ds = dsym()
for J in (1, 2, 3):
    d = 2 * J + 1
    mv = [J - k for k in range(d)]
    Sz = sp.diag(*mv)
    Sp = sp.zeros(d, d)
    for k in range(d - 1):
        Sp[k, k + 1] = sp.sqrt(J * (J + 1) - mv[k + 1] * (mv[k + 1] + 1))
    Sx = (Sp + Sp.H) / 2
    Sy = (Sp - Sp.H) / (2 * sp.I)
    # rotations J^{ij} = i eps_ijk S_k up to the sign fixed in orbital(); boosts J^{0i} = i N_i with the commuting symbol N
    def Zs(Sg):
        Z = sp.zeros(d * Sg[(0, 1)].shape[0], d * Sg[(0, 1)].shape[0])
        pairs = {(1, 2): sp.I * Sz, (2, 3): sp.I * Sx, (3, 1): sp.I * Sy}
        for (a, b), Op in pairs.items():
            Z = Z + 2 * sp.kronecker_product(Op, Sg[(a, b)])
        Z = Z + 2 * low(0, 3) * sp.kronecker_product(sp.I * n * sp.eye(d), Sg[(0, 3)])
        return Z
    ZV = Zs(Vs)
    ZD = Zs(Ds)
    a4 = sp.expand(((ZV ** 2) ** 2).trace())
    b4 = sp.expand(((ZD ** 2) ** 2).trace())
    pol = sp.expand(sp.simplify((a4 - 2 * b4) / (24 * d)))
    print("    J=%d c=%d: %s  ; expected top: n^4 + %s n^2 + %s" % (J, J * (J + 1), pol, sp.Rational(-2, 3) * J * (J + 1), (J * (J + 1)) ** 2))

print("(D) exact Plancherel average W_J(s) against the scaling form; integrand |P-2|^2 >= 0 identically")
xg, wg = np.polynomial.legendre.leggauss(1200)


def W_exact(s, J, th):
    t_ = s / th
    c_ = J * (J + 1)
    rmax = 9.0 / np.sqrt(t_) + 5
    rr = 0.5 * rmax * (xg + 1)
    wr = 0.5 * rmax * wg
    I1_ = np.sqrt(np.pi) / (4 * t_ ** 1.5)
    tot = 0.0
    nrm = 0.0
    for m in range(-J, J + 1):
        Lam = m + 1j * rr
        val = P(Lam, s) - 2
        wgt = (rr ** 2 + m * m) * np.exp(-t_ * rr ** 2)
        tot += np.exp(t_ * (m * m - 1 - c_)) * np.sum(wr * wgt * np.abs(val) ** 2) / I1_
        nrm += np.exp(t_ * (m * m - 1 - c_)) * np.sum(wr * wgt) / I1_
    return tot / (2 * J + 1), nrm / (2 * J + 1)


def W_scal(s, J, th):
    c_ = J * (J + 1)
    return s ** 2 * (15.0 / 4 * th ** 2 - s * th * c_ + s ** 2 * c_ ** 2)


print("    frozen limit: th large, xi fixed, J=0, against w(xi)")
def wf(x):
    return 6 + 2 * (1 - 4 * x) * np.exp(-2 * x) - 8 * (1 - x) * np.exp(-x / 2)
for xi_ in (0.2, 1.0, 3.0):
    th = 2e4
    s = 2 * xi_ / th
    print("      xi=%.1f W_exact %.8f w(xi) %.8f" % (xi_, W_exact(s, 0, th)[0], wf(xi_)))
print("    s, J, th | W_exact | W_scal | ratio")
for th in (1.0, 2.0, 5.0):
    for J in (0, 1, 3, 10, 30):
        for s in (1e-3, 1e-2):
            we = W_exact(s, J, th)[0]
            ws = W_scal(s, J, th)
            print("      %.0e %3d %3.0f | %.6e | %.6e | %.6f" % (s, J, th, we, ws, we / ws))
print("    Y_{A,J} = 2a int ds s^-2 e^{-s(a+mu)} W_J(s): exact against the scaling closed form, th=1, 2")
sg, swg = np.polynomial.legendre.leggauss(240)


def Y_exact(a, J, th):
    mu = J * (J + 2)
    D_ = a + mu
    edges = np.linspace(np.log(1e-5 / D_), np.log(45.0 / D_), 41)
    tot = 0.0
    for i in range(40):
        h = 0.5 * (edges[i + 1] - edges[i])
        m_ = 0.5 * (edges[i + 1] + edges[i])
        for x_, w_ in zip(sg[::6], swg[::6] * 6):
            s = np.exp(m_ + h * x_)
            tot += w_ * h * s * np.exp(-s * D_) * s ** -2 * W_exact(s, J, th)[0]
    return 2 * a * tot


def Y_scal(a, J, th):
    mu = J * (J + 2)
    c_ = J * (J + 1)
    D_ = a + mu
    return 2 * a * (15.0 / 4 * th ** 2 / D_ - th * c_ / D_ ** 2 + 2 * c_ ** 2 / D_ ** 3)


for th in (1.0, 2.0):
    for a, J in ((200.0, 0), (200.0, 3), (200.0, 10), (20.0, 10), (2000.0, 30)):
        ye = Y_exact(a, J, th)
        ys = Y_scal(a, J, th)
        print("      a=%6.0f J=%2d th=%.0f exact %.6f scaling %.6f ratio %.5f" % (a, J, th, ye, ys, ye / ys))

print("(E) level-resolved first term and L' on S^2_N. Units sqrt|g|/32 pi^2 times F; hypotheses of the frozen symbol, cross term dropped")
mp.mp.dps = 40


def s2data(l):
    L = mp.mpf(l)
    tc = [(4 * (2 * L + 2), L * L), (4 * 2 * L, (L + 1) ** 2), (-8 * (2 * L + 1), L * (L + 1))]
    if l == 0:
        vc = [(mp.mpf(3), mp.mpf(0)), (mp.mpf(-3), mp.mpf(0))]
    else:
        vc = [(2 * L + 3, L * (L - 1)), (2 * L + 1, L * (L + 1) + 2), (2 * L - 1, (L + 1) * (L + 2)), (-3 * (2 * L + 1), L * (L + 1))]
    return tc, vc


def Jm(b, th):
    return 4 * (b + th / 4) * mp.log(b + th / 4) - 4 * b * mp.log(b) + 2 * th * mp.log(b + th / 4)


def Lev(N, n_, x, th):
    x = mp.mpf(x)
    th = mp.mpf(th)
    chi2 = x * th
    F = mp.mpf((n_ + 1) ** 2)
    Yt = Ms = Q4 = Mfl = mp.mpf(0)
    for J in range(n_ + 1):
        wJ = (2 * J + 1) / F
        mu = mp.mpf(J * (J + 2))
        c_ = mp.mpf(J * (J + 1))
        for l in range(N):
            tc, vc = s2data(l)
            a = l * (l + 1) * chi2
            if a > 0:
                D_ = a + mu
                Yt += wJ * (2 * l + 1) * 2 * a * (mp.mpf(15) / 4 * th ** 2 / D_ - th * c_ / D_ ** 2 + 2 * c_ ** 2 / D_ ** 3)
            for co, b0 in tc:
                b = b0 * chi2
                if b > 0:
                    Ms += wJ * (-co * b / 2) * Jm(b + mu, th) if mu > 0 else wJ * (-co * b / 2) * Jm(b, th)
                    Mfl += wJ * (-co * b * c_ / (b + mu))
            for co, b0 in vc:
                b = b0 * chi2
                if b > 0:
                    Q4 += wJ * 2 * co * b * (b + mu) * mp.log(b + mu)
            for co, b0 in tc:
                b = b0 * chi2
                if b > 0:
                    Q4 += -wJ * 2 * co * b * (b + mu) * mp.log(b + mu)
    return Yt, Ms, Mfl, Q4


print("    N n x th | Y/(7.5 th^2 (N^2-1)) | estimate 1-delta | fibre-flux mixed / Y | L'/(N^2 th^2) | law | n/(chi N)")
for N, n_ in ((64, 2), (64, 5), (256, 2), (256, 5), (256, 10), (256, 40), (1024, 10)):
    for x, th in (("0.1", 1), ("0.3", 1), ("0.3", 2), ("0.81", 1), ("2.5", 1)):
        Yt, Ms, Mfl, Q4 = Lev(N, n_, x, th)
        xm = mp.mpf(x)
        tm = mp.mpf(th)
        chi2 = xm * tm
        s1 = sum((2 * l + 1) / (l * (l + 1) * chi2) for l in range(1, N)) / (N ** 2 - 1)
        F = (n_ + 1) ** 2
        av = sum((2 * J + 1) * (J * (J + 2) + mp.mpf(4) / 15 * J * (J + 1) / tm) for J in range(n_ + 1)) / F
        Lp = Yt + Ms + Mfl + Q4
        print("    %5d %3d %5s %d | %s | %s | %s | %s | %s | %s" % (N, n_, x, th, mp.nstr(Yt / (mp.mpf(15) / 2 * tm ** 2 * (N ** 2 - 1)), 7), mp.nstr(1 - s1 * av, 7), mp.nstr(Mfl / Yt, 3), mp.nstr(Lp / (N ** 2 * tm ** 2), 7), mp.nstr(-4 * xm ** 2 - 6 * xm + mp.mpf(15) / 2, 6), mp.nstr(n_ / (mp.sqrt(chi2) * N), 3)))
