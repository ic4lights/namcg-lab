"""072-080 r2, d2: pencil identities and typicality for one-cap-per-summand blocks.

For a block with q rank-one edge data (q summands of a direct sum, one cap each, or
q coincident copies), Q = -2i(U R^+ - R U^+) with U (qM x q) orthonormal edge vectors
and R the edge rows.  C0 = U^+ R, Z0 = R^+ R, H = (C0 - C0^+)/(2i),
K = Z0 - C0^+ C0 = R^+(1 - U U^+) R >= 0, T = -2i [[C0^+, Z0], [-1, -C0]].

Checks:
 (a) symbolic (sympy), q = 2, C0 and Z0 generic (Z0 Hermitian):
     det(l - T) = det(l^2 + 4 l H - 4 K);  numerically for q = 3..6 and the nonzero
     spectrum of Q equals the spectrum of T (random R, U);
 (b) block-scalar data H = (+)_f h_f 1_{q_f}, K = (+)_f n_f 1_{q_f}, realised as
     R = U(A + iH) + V K^{1/2} (V isometry into the complement of U, A real symmetric
     block-scalar): spectrum of Q = union over f of q_f copies of
     -2h_f +- 2(h_f^2 + n_f)^{1/2}, for partitions of q <= 5;
 (c) q = 2 diagonal data: quartic is the square of a real monic quadratic iff
     h1 = h2 and n1 = n2 (symbolic: 64d - (4b - a^2)^2 factor); the example
     (h,n) = (3,7), (5,11) has quartic (l-2)^2(l+14)(l+22) exactly;
 (d) moment identity at h_f = 0: sum_j e_j^{2p} with depths (2,1) over the
     multiplicity-1 value equals 1 + 9/17 (p=1) and 1 + 81/145 (p=2) at
     (n1, n2) = (1/4, 2/9) (exact rationals);
 (e) typicality by direct sampling of the edge rows (independent standard complex
     Gaussian momenta give independent isotropic Gaussian edge rows on the block):
     q = 2, block dimension N (M = N/2 per copy), 400 events per point:
       matched scales: medians of D and U2 at N = 50,100,200,400 and log-log slopes;
       column scales (1, 1.6): medians at N = 120, 240, 480;
     D = max_k (e_{kq} - e_{(k-1)q+1}) / max|e|,
     U2 = Tr Q^4 / (2q (Tr Q^2/(2q))^2) - 1;
 (g) matched iid edge rows: median of max|h_f| / min(n_f)^{1/2}, slope ~ -1/2;
 (f) direct sum of two summands with independent Gaussian entries between the
     summands: relative distance of the nonzero spectrum from the union of the two
     diagonal pairs, median over 400 events, at block dimensions 50..800, slope.

Run: python -I proposals/local-gpu/072-080-r2/d2_pencil_typicality.py
Expected: (a)-(d) exact or < 1e-9; (e) matched D slope in [-0.7,-0.3], U2 slope in
[-1.3,-0.7], mismatched D medians > 0.3 with |slope| < 0.1; (f) and (g) slopes in [-0.7,-0.3];
last line 'PASS d2'.
"""
import numpy as np
import sympy as sp
from fractions import Fraction

rng = np.random.default_rng(72081)
ok = True

# (a) symbolic q = 2
l = sp.symbols('l')
c = sp.symbols('c0:8', real=True)
z = sp.symbols('z0:4', real=True)
C0 = sp.Matrix([[c[0] + sp.I * c[1], c[2] + sp.I * c[3]], [c[4] + sp.I * c[5], c[6] + sp.I * c[7]]])
Z0 = sp.Matrix([[z[0], z[2] + sp.I * z[3]], [z[2] - sp.I * z[3], z[1]]])
I2 = sp.eye(2)
T = -2 * sp.I * sp.BlockMatrix([[C0.H, Z0], [-I2, -C0]]).as_explicit()
H = (C0 - C0.H) / (2 * sp.I)
K = Z0 - C0.H * C0
lhs = sp.expand((l * sp.eye(4) - T).det())
rhs = sp.expand((l ** 2 * I2 + 4 * l * H - 4 * K).det())
sym_a = sp.simplify(lhs - rhs) == 0
print('(a) symbolic q=2 det identity:', sym_a)
ok &= sym_a


def pencil(U, R):
    q = U.shape[1]
    C = U.conj().T @ R
    Z = R.conj().T @ R
    return -2j * np.block([[C.conj().T, Z], [-np.eye(q), -C]]), C, Z


def nzQ(U, R):
    Q = -2j * (U @ R.conj().T - R @ U.conj().T)
    ev = np.linalg.eigvalsh(Q)
    return np.sort(ev[np.abs(ev) > 1e-9 * np.abs(ev).max()])


worst = 0.0
for q in range(3, 7):
    for _ in range(5):
        D = q * 4 + 3
        U, _r = np.linalg.qr(rng.normal(size=(D, q)) + 1j * rng.normal(size=(D, q)))
        R = rng.normal(size=(D, q)) + 1j * rng.normal(size=(D, q))
        Tm, C, Z = pencil(U, R)
        Hm = (C - C.conj().T) / 2j
        Km = Z - C.conj().T @ C
        lam = np.linalg.eigvals(Tm)
        for x in lam:
            v = abs(np.linalg.det(x * x * np.eye(q) + 4 * x * Hm - 4 * Km))
            worst = max(worst, v / max(1.0, abs(x)) ** (2 * q))
        e1 = np.sort(lam.real)
        worst = max(worst, np.abs(np.sort(e1) - nzQ(U, R)).max() / np.abs(e1).max(), np.abs(lam.imag).max() / np.abs(e1).max())
print('(a) numerical q=3..6: max residual %.2e' % worst)
ok &= worst < 1e-9

# (b) block-scalar realisation
worst = 0.0
for parts in [(1, 1), (2,), (2, 1), (1, 1, 1), (3, 2), (2, 2, 1), (1, 4)]:
    q = sum(parts)
    D = 3 * q + 2
    Q_, _r = np.linalg.qr(rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D)))
    U, V = Q_[:, :q], Q_[:, q:2 * q]
    hs = rng.normal(size=len(parts))
    ns = rng.random(size=len(parts)) + 0.2
    hd = np.concatenate([[h] * k for h, k in zip(hs, parts)])
    nd = np.concatenate([[n] * k for n, k in zip(ns, parts)])
    A = np.diag(np.concatenate([[a] * k for a, k in zip(rng.normal(size=len(parts)), parts)]))
    R = U @ (A + 1j * np.diag(hd)) + V @ np.diag(np.sqrt(nd))
    # C0 = A + iH has Im part H? H = (C0 - C0^+)/(2i) = diag(hd)
    pred = np.sort(np.concatenate([[-2 * h + 2 * np.sqrt(h * h + n), -2 * h - 2 * np.sqrt(h * h + n)] * k
                                   for h, n, k in zip(hs, ns, parts)]))
    pred2 = np.sort(-pred)
    got = nzQ(U, R)
    worst = max(worst, min(np.abs(got - pred).max(), np.abs(got - pred2).max()) / np.abs(pred).max())
print('(b) block-scalar spectrum: max deviation %.2e' % worst)
ok &= worst < 1e-9

# (c) q = 2 criterion
h1, h2, n1, n2 = sp.symbols('h1 h2 n1 n2', real=True)
quart = sp.expand((l ** 2 + 4 * h1 * l - 4 * n1) * (l ** 2 + 4 * h2 * l - 4 * n2))
P = sp.Poly(quart, l)
_, a, b, cc, d = P.all_coeffs()
c1 = sp.factor(8 * cc - a * (4 * b - a ** 2))
c2 = sp.factor(64 * d - (4 * b - a ** 2) ** 2)
print('(c) 8c - a(4b-a^2) =', c1)
print('(c) 64d - (4b-a^2)^2 =', c2)
c2_ok = sp.expand(c2 - (1024 * n1 * n2 - 256 * ((h1 - h2) ** 2 + n1 + n2) ** 2)) == 0
ex = sp.factor(quart.subs({h1: 3, n1: 7, h2: 5, n2: 11}))
print('(c) example (3,7),(5,11):', ex)
ex_ok = sp.expand(ex - (l - 2) ** 2 * (l + 14) * (l + 22)) == 0
print('(c) checks:', c2_ok, ex_ok)
ok &= c2_ok and ex_ok

# (d) moment identity (pair at h = 0: eigenvalues +-2 n^{1/2}, e^{2p} = (4n)^p each, 2 per pair)
for p, target in [(1, Fraction(9, 17)), (2, Fraction(81, 145))]:
    nn = [Fraction(1, 4), Fraction(2, 9)]
    qs = [2, 1]
    mixed = sum(qf * 2 * (4 * nf) ** p for qf, nf in zip(qs, nn))
    single = sum(2 * (4 * nf) ** p for nf in nn)
    r = mixed / single - 1
    print('(d) p=%d excess = %s' % (p, r))
    ok &= r == target


# (e) typicality
def stats(N, scales, q=2, events=400):
    Ds, Us = [], []
    for _ in range(events):
        R = (rng.normal(size=(N, q)) + 1j * rng.normal(size=(N, q))) * np.array(scales)
        U = np.zeros((N, q), complex)
        for b in range(q):
            U[b * (N // q), b] = 1.0
        Tm, _c, _z = pencil(U, R)
        e = np.sort(np.linalg.eigvals(Tm).real)
        Dv = max(e[k * q - 1] - e[(k - 1) * q] for k in (1, 2)) / np.abs(e).max()
        U2 = (e ** 4).sum() / (2 * q * ((e ** 2).sum() / (2 * q)) ** 2) - 1
        Ds.append(Dv)
        Us.append(U2)
    return np.median(Ds), np.median(Us)


Ns = [50, 100, 200, 400]
mD, mU = [], []
for N in Ns:
    d_, u_ = stats(N, [1.0, 1.0])
    mD.append(d_)
    mU.append(u_)
    print('(e) matched  N=%4d  D=%.4f  U2=%.4f' % (N, d_, u_))
sD = np.polyfit(np.log(Ns), np.log(mD), 1)[0]
sU = np.polyfit(np.log(Ns), np.log(mU), 1)[0]
print('(e) matched slopes: D %.3f  U2 %.3f' % (sD, sU))
Nm = [120, 240, 480]
xD = []
for N in Nm:
    d_, u_ = stats(N, [1.0, 1.6])
    xD.append(d_)
    print('(e) scales (1,1.6)  N=%4d  D=%.4f  U2=%.4f' % (N, d_, u_))
sX = np.polyfit(np.log(Nm), np.log(xD), 1)[0]
print('(e) mismatched D slope %.3f' % sX)
ok &= (-0.7 <= sD <= -0.3) and (-1.3 <= sU <= -0.7) and min(xD) > 0.3 and abs(sX) < 0.1

# (f) direct sum with entries between summands
Nf = [50, 100, 200, 400, 800]
med = []
for N in Nf:
    devs = []
    for _ in range(400):
        R = rng.normal(size=(N, 2)) + 1j * rng.normal(size=(N, 2))
        U = np.zeros((N, 2), complex)
        U[0, 0] = 1.0
        U[N // 2, 1] = 1.0
        Tm, C, Z = pencil(U, R)
        e = np.sort(np.linalg.eigvals(Tm).real)
        Hm = (C - C.conj().T) / 2j
        Km = Z - C.conj().T @ C
        un = []
        for f in range(2):
            h, n = Hm[f, f].real, Km[f, f].real
            un += [-2 * h + 2 * np.sqrt(h * h + n), -2 * h - 2 * np.sqrt(h * h + n)]
        devs.append(np.abs(e - np.sort(un)).max() / np.abs(e).max())
    med.append(np.median(devs))
    print('(f) block dim %4d  median relative distance from the union of diagonal pairs %.4f' % (N, med[-1]))
sF = np.polyfit(np.log(Nf), np.log(med), 1)[0]
print('(f) slope %.3f' % sF)
ok &= -0.7 <= sF <= -0.3

# (g) imaginary parts against norms for matched iid edge rows (q = 2)
Ng = [50, 100, 200, 400]
mr = []
for N in Ng:
    rs = []
    for _ in range(400):
        R = rng.normal(size=(N, 2)) + 1j * rng.normal(size=(N, 2))
        U = np.zeros((N, 2), complex)
        U[0, 0] = 1.0
        U[N // 2, 1] = 1.0
        C = U.conj().T @ R
        Hm = (C - C.conj().T) / 2j
        Km = R.conj().T @ R - C.conj().T @ C
        rs.append(np.abs(np.linalg.eigvalsh(Hm)).max() / np.sqrt(np.linalg.eigvalsh(Km).min()))
    mr.append(np.median(rs))
    print('(g) N=%4d median max|h|/min(n)^(1/2) = %.4f' % (N, mr[-1]))
sG = np.polyfit(np.log(Ng), np.log(mr), 1)[0]
print('(g) slope %.3f' % sG)
ok &= -0.7 <= sG <= -0.3

print('all checks inside thresholds:', ok)
assert ok
print('PASS d2')
