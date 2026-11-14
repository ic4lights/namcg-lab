"""
067 e6 (round 2, findings F6 and F2): Monte Carlo for the classicalised edge charge Q = -2i (Y - Y^dagger),
Y = sum_a X^a_{S S'} Pi^a_{S' S}  [arXiv:2408.05274 Eq. (4.4)], on S^2_N x S^2_N (round factors A_f = nu_f 1).

Gaussian momenta, independent in a, variance f(l1,l2) on the (spin l1) (x) (spin l2) matrices, of the two forms
   "asym":  f = (l1/2) 1[l1<=lc1] 1[l2<=lc2]                                (the form of e3 Part 3)
   "sym" :  f = (l1/2) 1[l1<=lc1] 1[l2<=lc2] + 1[l1<=lc2] (l2/2) 1[l2<=lc1]  (sum of two independent Gaussians)
Exact second moment (e3 Part 1):  <Y Y^dagger> = diag(Et_u),  Et_u = sum_{links u->v} kappa_link D_v,
   D_v = sum_{j in Omega} <|Pi_{vj}|^2>.

Part A (F6): cap x whole second sphere, N = 8, 12, 16, M1 = N/2, lc1 = N-1, lc2 = 3 (asym): all N edge sites are
   equivalent, Et_u = s1^2 W.  <sum pos Q> against 2 sqrt(W) T (T = N s1) and against 2 sqrt(W) s (s = sqrt(N) s1).
Part B (F2): blocks whose edge sites are NOT equivalent (product blocks and oblique half-planes; N = 12 and 16):
   <sum pos Q> against the local estimate  L = 2 sum_u sqrt(Et_u)
   and against the non-local combination   G = 2 sqrt(r sum_u Et_u)   (r = number of edge sites).
   L <= G always (Cauchy-Schwarz), with equality iff all Et_u are equal; L/G is printed.
The momenta are not constrained to Tr Q = 0.  Seeded; output to stdout only.
"""
import numpy as np

rng = np.random.default_rng(67006)
NS = 60

def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]

def config(N, nu1, nu2):
    J = su2(N); I = np.eye(N)
    return [np.kron(nu1 * J[a], I) for a in range(3)] + [np.kron(I, nu2 * J[a]) for a in range(3)]

def spin_projectors(N):
    J = su2(N); I = np.eye(N)
    C = np.zeros((N * N, N * N), complex)
    for Ja in J:
        ad = np.kron(Ja, I) - np.kron(I, Ja.T)
        C += ad @ ad
    assert np.abs(C.imag).max() < 1e-12
    lam, V = np.linalg.eigh(C.real)
    l = np.rint((-1 + np.sqrt(1 + 4 * np.clip(lam, 0, None))) / 2).astype(int)
    assert np.allclose(l * (l + 1), lam, atol=1e-8)
    return [V[:, l == k] @ V[:, l == k].T for k in range(N)]

class Setup:
    def __init__(self, N):
        self.N = N; self.P = spin_projectors(N)
        self.pd = np.array([np.diag(p).reshape(N, N) for p in self.P])       # pd[l][v, j] = (P_l)_{(v j),(v j)}
        self.ii1, self.ii2 = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")

    def filt(self, fl):
        return sum(np.sqrt(fl[l]) * self.P[l] for l in range(self.N)), np.tensordot(fl, self.pd, axes=1)

    def sample(self, Fa, Fb):
        N = self.N
        Z = rng.normal(size=(N * N, N * N)) + 1j * rng.normal(size=(N * N, N * N)); G = (Z + Z.conj().T) / 2
        G4 = G.reshape(N, N, N, N).transpose(0, 2, 1, 3).reshape(N * N, N * N)
        G4 = Fa @ G4 @ Fb.T
        return G4.reshape(N, N, N, N).transpose(0, 2, 1, 3).reshape(N * N, N * N)

def run(S, Om, nu1, nu2, lc1, lc2, kind):
    N = S.N; X = config(N, nu1, nu2)
    fa = np.array([0.5 * l if l <= lc1 else 0.0 for l in range(N)]); fb = np.array([1.0 if l <= lc2 else 0.0 for l in range(N)])
    Fa, Ga = S.filt(fa); Fb, Gb = S.filt(fb)
    Omf = Om.astype(float)
    Dg = Ga @ Omf @ Gb.T                                   # D[v1, v2] = sum_{j in Omega} Ga[v1, j1] Gb[v2, j2]
    if kind == "sym": Dg = Dg + Gb @ Omf @ Ga.T
    k1, k2 = nu1 ** 2 / 2, nu2 ** 2 / 2
    Et = np.zeros((N, N))
    for i1 in range(N):
        for i2 in range(N):
            if not Om[i1, i2]: continue
            e = 0.0
            if i1 - 1 >= 0 and not Om[i1 - 1, i2]: e += k1 * i1 * (N - i1) * Dg[i1 - 1, i2]
            if i1 + 1 < N and not Om[i1 + 1, i2]: e += k1 * (i1 + 1) * (N - i1 - 1) * Dg[i1 + 1, i2]
            if i2 - 1 >= 0 and not Om[i1, i2 - 1]: e += k2 * i2 * (N - i2) * Dg[i1, i2 - 1]
            if i2 + 1 < N and not Om[i1, i2 + 1]: e += k2 * (i2 + 1) * (N - i2 - 1) * Dg[i1, i2 + 1]
            Et[i1, i2] = e
    et = Et[Et > 0]; r = len(et)
    inn = np.flatnonzero(Om.reshape(-1)); out = np.flatnonzero(~Om.reshape(-1))
    pos = []; tr = []
    for smp in range(NS):
        Y = 0
        for a in range(6):
            Pi = S.sample(Fa, Fb)
            if kind == "sym": Pi = Pi + S.sample(Fb, Fa)
            Y = Y + X[a][np.ix_(inn, out)] @ Pi[np.ix_(out, inn)]
        Q = -2j * (Y - Y.conj().T)
        ev = np.linalg.eigvalsh(Q); pos.append(ev[ev > 0].sum()); tr.append(np.trace(Y @ Y.conj().T).real)
    pos = np.array(pos)
    assert abs(np.mean(tr) / et.sum() - 1) < 0.05, np.mean(tr) / et.sum()      # sampler reproduces the exact second moment
    return dict(M=len(inn), r=r, et=et, pos=pos.mean(), err=pos.std() / np.sqrt(NS), tr=np.mean(tr) / et.sum())

# ------------------------------------------------------------ Part A
print("Part A  cap x whole sphere, M1 = N/2, nu = (1, 1.4), lc1 = N-1, lc2 = 3, asym, %d samples" % NS)
print("     N    M    r   <TrYY^+>/sum Et   <sum pos Q>/(2 sqrt(W) T)   <sum pos Q>/(2 sqrt(W) s)   spread of Et_u")
setups = {}
for N in (8, 12, 16):
    S = setups[N] = Setup(N)
    R = run(S, S.ii1 < N // 2, 1.0, 1.4, N - 1, 3, "asym")
    et = R["et"]; assert R["r"] == N and np.ptp(et) < 1e-9 * et.mean()
    T = np.sqrt(et).sum(); s = np.sqrt(et.sum())           # sqrt(W) T and sqrt(W) s
    print("  %4d %4d %4d      %.4f            %.4f +- %.4f             %.4f                 %.1e"
          % (N, R["M"], R["r"], R["tr"], R["pos"] / (2 * T), R["err"] / (2 * T), R["pos"] / (2 * s), np.ptp(et) / et.mean()))

# ------------------------------------------------------------ Part B
print("Part B  blocks with inequivalent edge sites, %d samples;  L = 2 sum_u sqrt(Et_u),  G = 2 sqrt(r sum_u Et_u)" % NS)
print("     N  block                      state        nu2/nu1    M    r   max/min Et   L/G     <sum pos Q>/L        <sum pos Q>/G")
resB = []
for N in (12, 16):
    S = setups[N]; i1, i2 = S.ii1, S.ii2; h = N // 2
    blocks = (("product %dx%d" % (h, h // 2), (i1 < h) & (i2 < h // 2)),
              ("product %dx%d" % (h // 2, h + 1), (i1 < h // 2) & (i2 < h + 1)),
              ("half-plane b/a=0.41", 1.0 * i1 + 0.41 * i2 < 0.705 * (N - 1)),
              ("half-plane b/a=1/sqrt3", 1.0 * i1 + 3 ** -0.5 * i2 < 0.79 * (N - 1)))
    for name, Om in blocks:
        for kind, lc1, lc2 in (("asym", N - 1, 3), ("sym", N - 1, 3)):
            for nu2 in (1.0, 3.0):
                R = run(S, Om, 1.0, nu2, lc1, lc2, kind)
                et = R["et"]; L = 2 * np.sqrt(et).sum(); G = 2 * np.sqrt(R["r"] * et.sum())
                assert 2 * R["r"] <= R["M"]
                resB.append((N, name, kind, nu2, L / G, R["pos"] / L, R["pos"] / G))
                print("  %4d  %-24s  %-4s lc=(%2d,%d)   %3.1f    %4d %4d   %8.2f   %.4f   %.4f +- %.4f     %.4f"
                      % (N, name, kind, lc1, lc2, nu2, R["M"], R["r"], et.max() / et.min(), L / G, R["pos"] / L, R["err"] / L, R["pos"] / G))
a = np.array([[t[4], t[5], t[6]] for t in resB])
print("Part B summary over %d cases: L/G in [%.3f, %.3f]" % (len(a), a[:, 0].min(), a[:, 0].max()))
print("   ratio to L in [%.3f, %.3f], mean %.3f, relative spread (std/mean) %.3f" % (a[:, 1].min(), a[:, 1].max(), a[:, 1].mean(), a[:, 1].std() / a[:, 1].mean()))
print("   ratio to G in [%.3f, %.3f], mean %.3f, relative spread (std/mean) %.3f" % (a[:, 2].min(), a[:, 2].max(), a[:, 2].mean(), a[:, 2].std() / a[:, 2].mean()))
sel = a[a[:, 0] < 0.95]
if len(sel):
    print("   cases with L/G < 0.95 (%d): ratio to L in [%.3f, %.3f], spread %.3f; ratio to G in [%.3f, %.3f], spread %.3f"
          % (len(sel), sel[:, 1].min(), sel[:, 1].max(), sel[:, 1].std() / sel[:, 1].mean(), sel[:, 2].min(), sel[:, 2].max(), sel[:, 2].std() / sel[:, 2].mean()))
print("   correlation of (ratio to L) with L/G: %+.3f ;  of (ratio to G) with L/G: %+.3f" % (np.corrcoef(a[:, 0], a[:, 1])[0, 1], np.corrcoef(a[:, 0], a[:, 2])[0, 1]))
print("PASS e6")
