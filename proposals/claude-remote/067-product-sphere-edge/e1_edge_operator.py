"""
067 e1: exact edge operator of a lattice block on the product fuzzy factor S^2_N x S^2_N.

Configuration: six Hermitian N^2 x N^2 matrices X^I = (A1^a_b J^b (x) 1, 1 (x) A2^a_b J^b), A1, A2 real invertible
3x3, J^b the N-dim irrep of su(2), positive contraction delta_IJ.  Basis |i1,i2), J^3 = j - i.
Theta = projector on a lattice set Omega of joint J^3 (x) 1, 1 (x) J^3 eigenvectors (every block defined by the
ordered eigenbasis of a reference matrix a J^3(x)1 + b 1(x)J^3 is of this form).

Claim (exact, finite N).  If no section of Omega along either lattice direction has a gap of exactly one site
(pattern in/out/in), then E := sum_I Theta X^I Thetabar X^I Theta is diagonal in |i1,i2), with eigenvalue at a site
of Omega
   E = k1 [ i1(N-i1) [ (i1-1,i2) not in Omega ] + (i1+1)(N-i1-1) [ (i1+1,i2) not in Omega ] ] + (same for factor 2),
   k_f = (1/4) sum_a ( (A_f)^a_1^2 + (A_f)^a_2^2 )  ( = (sigma_1^2+sigma_2^2)/4 of 065 for n = e_3 ).
Hence  s^2 = Tr E = (1/2) Tr(Theta Box Theta),  T := Tr E^{1/2} (trace norm of the edge map),
rank of the edge map = number of edge sites.  For a product block P (x) Q (ranks M1, M2):
   s^2 = M2 s1^2 + M1 s2^2,   T = (M2-1) s1 + (M1-1) s2 + sqrt(s1^2+s2^2),   rank = M1 + M2 - 1,
with s_f^2 = k_f M_f (N - M_f) the single-factor edge datum of 065.
If a single-site gap exists and A_f is not conformal on the (1,2) plane, E has off-diagonal entries (checked).
Output to stdout only.
"""
import numpy as np

rng = np.random.default_rng(67001)

def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]

def config(N, A1, A2):
    J = su2(N); I = np.eye(N)
    X = [np.kron(sum(A1[a, b] * J[b] for b in range(3)), I) for a in range(3)]
    X += [np.kron(I, sum(A2[a, b] * J[b] for b in range(3))) for a in range(3)]
    return X

def formula(N, Om, A1, A2):
    k1 = 0.25 * (A1[:, 0] ** 2 + A1[:, 1] ** 2).sum()
    k2 = 0.25 * (A2[:, 0] ** 2 + A2[:, 1] ** 2).sum()
    E = np.zeros((N, N))
    for i1 in range(N):
        for i2 in range(N):
            if not Om[i1, i2]:
                continue
            e = 0.0
            if i1 - 1 >= 0 and not Om[i1 - 1, i2]: e += k1 * i1 * (N - i1)
            if i1 + 1 <= N - 1 and not Om[i1 + 1, i2]: e += k1 * (i1 + 1) * (N - i1 - 1)
            if i2 - 1 >= 0 and not Om[i1, i2 - 1]: e += k2 * i2 * (N - i2)
            if i2 + 1 <= N - 1 and not Om[i1, i2 + 1]: e += k2 * (i2 + 1) * (N - i2 - 1)
            E[i1, i2] = e
    return E, k1, k2

def single_gap(Om):
    for Z in (Om, Om.T):
        for r in Z:
            for k in range(1, len(r) - 1):
                if r[k - 1] and not r[k] and r[k + 1]:
                    return True
    return False

def check(N, Om, A1, A2, label):
    X = config(N, A1, A2)
    th = Om.reshape(-1).astype(float); Th = np.diag(th); Tb = np.eye(N * N) - Th
    Eop = sum(Th @ x @ Tb @ x @ Th for x in X)
    box = lambda Y: sum(x @ (x @ Y - Y @ x) - (x @ Y - Y @ x) @ x for x in X)
    hs = 0.5 * np.trace(Th @ box(Th)).real
    Ef, k1, k2 = formula(N, Om, A1, A2)
    off = np.abs(Eop - np.diag(np.diag(Eop))).max()
    dev = np.abs(np.diag(Eop).real - Ef.reshape(-1)).max()
    ev = np.linalg.eigvalsh(Eop)
    T_op = np.sqrt(np.clip(ev, 0, None)).sum(); T_f = np.sqrt(Ef).sum()
    edge = np.hstack([Th @ x @ Tb for x in X])
    rank = np.linalg.matrix_rank(edge, tol=1e-8); nsite = int((Ef > 0).sum())
    print('%-34s N=%2d single-gap=%-5s offdiag=%.1e diag-dev=%.1e  TrE-(1/2)Tr(Th Box Th)=%.1e  T: op %.6f formula %.6f  rank %d sites %d'
          % (label, N, single_gap(Om), off, dev, np.trace(Eop).real - hs, T_op, T_f, rank, nsite))
    return off, dev, abs(np.trace(Eop).real - hs), abs(T_op - T_f), rank - nsite, Ef, k1, k2

worst = 0.0
for N in (6, 9, 12):
    ii1, ii2 = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
    for trial in range(2):
        A1 = rng.normal(size=(3, 3)); A2 = rng.normal(size=(3, 3))
        # product block
        M1, M2 = rng.integers(1, N, size=2)
        Om = (ii1 < M1) & (ii2 < M2)
        off, dev, h, t, rk, Ef, k1, k2 = check(N, Om, A1, A2, 'product P(x)Q M1=%d M2=%d' % (M1, M2))
        s1 = np.sqrt(k1 * M1 * (N - M1)); s2 = np.sqrt(k2 * M2 * (N - M2))
        Tp = (M2 - 1) * s1 + (M1 - 1) * s2 + np.sqrt(s1 ** 2 + s2 ** 2)
        e_prod = max(abs(Ef.sum() - (M2 * s1 ** 2 + M1 * s2 ** 2)), abs(np.sqrt(Ef).sum() - Tp), abs(rk), abs(int((Ef > 0).sum()) - (M1 + M2 - 1)))
        print('    product closed forms: |s^2 - (M2 s1^2 + M1 s2^2)|, |T - T_prod|, rank-(M1+M2-1): max dev %.1e' % e_prod)
        worst = max(worst, off, dev, h, t, abs(rk), e_prod)
        # oblique half-plane block a i1 + b i2 < c
        a, b = 1.0, np.sqrt(2) * rng.uniform(0.3, 1.2)
        Om = a * ii1 + b * ii2 < 0.5 * (a + b) * (N - 1) + 0.1
        off, dev, h, t, rk, *_ = check(N, Om, A1, A2, 'half-plane b/a=%.3f' % b)
        worst = max(worst, off, dev, h, t, abs(rk))
        # two separated discs (sections have gaps >= 2)
        Om = ((ii1 - 1.5) ** 2 + (ii2 - 1.5) ** 2 < 3.0) | ((ii1 - (N - 2.5)) ** 2 + (ii2 - (N - 2.5)) ** 2 < 3.0)
        off, dev, h, t, rk, *_ = check(N, Om, A1, A2, 'two separated discs')
        worst = max(worst, off, dev, h, t, abs(rk))
print('max deviation over gap-free cases: %.2e' % worst)
assert worst < 1e-8

# single-site gap: off-diagonal entries appear iff A is non-conformal on the (1,2) plane
N = 8
ii1, ii2 = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
Om = (ii1 != 3) & (ii2 < 5)
A1 = np.diag([1.0, 2.0, 1.0]); A2 = np.eye(3)
off, *_ = check(N, Om, A1, A2, 'single gap, A1 non-conformal')
assert off > 1e-3
A1 = np.diag([1.5, 1.5, 0.7])
off2, *_ = check(N, Om, A1, A2, 'single gap, A1 conformal on (1,2)')
assert off2 < 1e-8
print('PASS e1')
