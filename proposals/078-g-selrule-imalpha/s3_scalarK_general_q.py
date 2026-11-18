# s3_scalarK_general_q.py
# General-q exact spectrum reduction for the coincident-copy edge charge, and the
# double-pair locus. Data: U = I_q kron u (qN x q isometry), R any qN x q, C0 = U^dag R,
# H = Im C0 = (C0-C0^dag)/(2i), K = R^dag(I - U U^dag)R PSD, T = -2i M,
# M = [[C0^dag, Z0],[-I_q, -C0]], Z0 = R^dag R (077 pencil).
# Checks (all spectra from the Hermitian charge Q~ = -2i(U R^dag - R U^dag), never from
# eigvalsh of the non-Hermitian -2iM; the 2q nonzero eigenvalues are kept):
#  (A) symbolic q=2: det(lam I_4 - T) = det(lam^2 I_2 + 4 lam H - 4K) identically, for
#      GENERIC Hermitian H and K (monic quadratic reduction at the lam level); and the
#      exact Re-invisibility with coupling: C0 = A + iH with A generic Hermitian, Z0 =
#      K + C0^dag C0 (A appears through BOTH C0 and Z0): the char poly of T is
#      independent of every A entry.
#  (B) scalar-K spectrum theorem (numeric q=2..6): K = n I, n>0: spec(T) =
#      union_f { -2 h_f +- 2 sqrt(h_f^2+n) }, h_f = eig(H); Re C0 = A invisible.
#  (C) double-pair = Im-part coincidence: min gap of spec(T) equals the predicted min
#      over the pair multiset; spacing lower bound min(c(M,n)*sep(eig H),
#      4n/(sqrt(M^2+n)+M)) with c = 2(1-M/sqrt(M^2+n)) > 0 (150 trials, q=3);
#      onset of the gap in the mismatch eps is exactly linear (q=2 log-log slopes).
#  (D) involution lam -> -4n/lam preserves spec(T), is fixed-point free over the reals
#      (|lam + 4n/lam| >= 4 sqrt(n)), and pairs each Row-length pair with itself.
#  (E) general-K (per-row) q=2 double-eigenvalue locus: EXACT rational example
#      (h,n) rows (3,7),(5,11): -2*3+2*sqrt(9+7) = -2*5+2*sqrt(25+11) = 2, so the quartic
#      g = f1 f2, f_i = lam^2+4 h_i lam - 4 n_i, has a DOUBLE root at lam=2 with
#      Im-part mismatch AND norm mismatch; symbolic: disc(g) = disc(f1)disc(f2)res(f1,f2)^2,
#      disc(f_i) = 16(h_i^2+n_i) > 0 (rows never self-coalesce at n>0), disc(g) and res
#      not identically zero => the double-eigenvalue locus is the zero set of ONE real
#      polynomial in the 8 real params of (H,K): a genuine hypersurface (codim exactly 1
#      in the general class), NOT codim-1 in the scalar-K subclass (there it is
#      {eig H repeated}: codim 3 in the q^2+1 params (H,n); verified by the linear
#      three-parameter onset in (G)).
#  (F) general-K q=2 numeric: 400 random (H,K), K>0: fully simple spectrum (400/400).
#  (G) codim-3 onset in the scalar-K class: H = h I_q + eps*V, V traceless Hermitian
#      with simple spectrum: min gap of spec(T) ~ const*|eps| (linear, 3 independent
#      directions in the complement of the scalar locus).
# No manuscript I/O. Run: python -I s3_scalarK_general_q.py > s3_scalarK_general_q.out 2>&1
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261117 + 3)

# ---------------- (A) symbolic: monic reduction + coupled Re-invisibility, q=2 ----------------
def herm_sy(name, q):
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

q = 2
lam = sp.Symbol('lam')
Hx, Kx = herm_sy('h', q), herm_sy('k', q)
C0x = sp.I*Hx
Z0x = Kx + (-sp.I*Hx)@(sp.I*Hx)
Mx = sp.zeros(2*q, 2*q)
Mx[:q, :q] = C0x.adjoint(); Mx[:q, q:] = Z0x
Mx[q:, :q] = -sp.eye(q);    Mx[q:, q:] = -C0x
lhs = sp.expand((lam*sp.eye(2*q) - (-2*sp.I)*Mx).det())
rhs = sp.expand((sp.eye(q)*lam**2 + 4*lam*Hx - 4*Kx).det())
print("(A) det(lam I - T) - det(lam^2 I + 4 lam H - 4 K) identically zero (generic Herm H,K):",
      sp.expand(lhs - rhs) == 0)
assert sp.expand(lhs - rhs) == 0
# coupled Re-invisibility: C0 = A + iH, A generic Hermitian; Z0 = K + C0^dag C0
Ax = herm_sy('a', q)
C0a = Ax + sp.I*Hx
Z0a = Kx + C0a.adjoint()@C0a          # K := R^dag P R held fixed
Ma = sp.zeros(2*q, 2*q)
Ma[:q, :q] = C0a.adjoint(); Ma[:q, q:] = Z0a
Ma[q:, :q] = -sp.eye(q);    Ma[q:, q:] = -C0a
lhsA = sp.expand((lam*sp.eye(2*q) - (-2*sp.I)*Ma).det())
diffA = sp.expand(lhsA - lhs)
print("(A) Re-invisibility with A entering C0 AND Z0: char-poly difference identically zero:",
      diffA == 0)
assert diffA == 0

# ---------------- helpers: Hermitian-charge spectra ----------------
def make_u(N):
    u = rng.normal(size=N) + 1j*rng.normal(size=N); return u/np.linalg.norm(u)
def charge_spec(u, q, H, K, A=None):
    N = len(u); U = np.kron(np.eye(q), u.reshape(-1, 1)); P = np.eye(q*N) - U@U.conj().T
    Vp = np.linalg.svd(P)[0][:, :q]
    C0 = (A if A is not None else 0.0) + 1j*H
    R = U@C0 + Vp@np.linalg.cholesky(K).conj().T
    Q = -2j*(U@R.conj().T - R@U.conj().T)
    assert np.allclose(Q, Q.conj().T, atol=1e-11)
    ev = np.linalg.eigvalsh(Q)
    o = np.argsort(np.abs(ev))
    assert np.abs(ev[o[:q*N-2*q]]).max() < 1e-9      # rank exactly 2q here
    return np.sort(ev[o[q*N-2*q:]])
def rand_herm(q):
    Ar = rng.normal(size=(q, q)) + 1j*rng.normal(size=(q, q)); return (Ar + Ar.conj().T)/2

# ---------------- (B) scalar-K spectrum theorem, q=2..6 ----------------
worstB = 0.0; worstA = 0.0
for q in range(2, 7):
    N = 3*q + 2
    u = make_u(N)
    h = np.sort(rng.normal(size=q) + np.arange(q))          # simple, distinct
    H = np.diag(h); n0 = 1.3 + 0.7*q
    ev = charge_spec(u, q, H, n0*np.eye(q))
    assert np.abs(ev).min() > 1e-8                          # rank-full guard (K = n0 I > 0)
    pred = np.sort(np.array([x for hf in h for x in (-2*hf - 2*np.sqrt(hf**2 + n0),
                                                     -2*hf + 2*np.sqrt(hf**2 + n0))]))
    dev = np.abs(ev - pred).max(); worstB = max(worstB, dev)
    A = rand_herm(q)*3.1                                    # large arbitrary Re part
    evA = charge_spec(u, q, H, n0*np.eye(q), A=A)
    worstA = max(worstA, np.abs(evA - ev).max())
    print("(B) q=%d: union-of-pairs dev %.3e ; Re A dev %.3e" % (q, dev, worstA))
assert worstB < 1e-9 and worstA < 1e-9
print("(B) global worst: union %.3e ; Re-invisibility %.3e" % (worstB, worstA))

# ---------------- (C) double pair = coincidence; spacing bound; onset ----------------
u6 = make_u(11)
mism_ok = 0
for _ in range(150):
    q3 = 3; h = np.sort(rng.uniform(-2.5, 2.5, size=q3))
    if np.diff(h).min() < 0.05: continue
    n0 = rng.uniform(0.4, 4.0); Mx_ = np.abs(h).max()
    ev = charge_spec(u6, q3, np.diag(h), n0*np.eye(q3))
    pred = np.sort(np.array([x for hf in h for x in (-2*hf - 2*np.sqrt(hf**2 + n0),
                                                     -2*hf + 2*np.sqrt(hf**2 + n0))]))
    assert np.abs(ev - pred).max() < 1e-9
    mingap = np.diff(ev).min()
    pred_gap = np.diff(pred).min()
    assert abs(mingap - pred_gap) < 1e-9
    c = 2*(1 - Mx_/np.sqrt(Mx_**2 + n0))
    bound = min(c*np.diff(h).min(), 4*n0/(np.sqrt(n0**2 + Mx_**2) + Mx_))
    assert bound > 0 and mingap >= bound - 1e-12
    mism_ok += 1
print("(C) mismatched Im data: %d/150 trials: spectrum = pairs, simple, bound holds" % mism_ok)
assert mism_ok >= 130
eps_list = [1e-4, 1e-3, 1e-2, 1e-1]
gaps = [np.diff(charge_spec(u6, 2, np.diag([0.8, 0.8 + e]), 3.7*np.eye(2))).min()
        for e in eps_list]
slopes = [np.log(gaps[i+1]/gaps[i])/np.log(eps_list[i+1]/eps_list[i]) for i in range(3)]
print("(C) gap-vs-eps log-log slopes (expect 1):", np.round(slopes, 4), " gaps:",
      ["%.3e" % g for g in gaps])
assert all(abs(s - 1) < 0.02 for s in slopes)

# ---------------- (D) involution lam -> -4n/lam ----------------
u8 = make_u(14)
worstD = 0.0; worstFP = 0.0
for _ in range(40):
    qD = rng.integers(2, 6); n0 = rng.uniform(0.5, 5.0)
    h = np.sort(rng.uniform(-3, 3, size=qD))
    ev = charge_spec(u8, qD, np.diag(h), n0*np.eye(qD))
    mapped = np.sort(-4*n0/ev)
    worstD = max(worstD, np.abs(mapped - ev).max())
    worstFP = max(worstFP, 4*np.sqrt(n0) - np.abs(ev + 4*n0/ev).min())
print("(D) involution spec-invariance worst dev %.3e ; fixed-point-free margin worst %.3e" %
      (worstD, worstFP))
assert worstD < 1e-9 and worstFP < 1e-9

# ---------------- (E) general-K double-eigenvalue locus: exact example + discriminant ----
lams = sp.Symbol('lam')
h1v, h2v, n1v, n2v = sp.symbols('h1 h2 n1 n2', positive=True)
f1 = lams**2 + 4*h1v*lams - 4*n1v; f2 = lams**2 + 4*h2v*lams - 4*n2v
g = sp.expand(f1*f2)
discg = sp.expand(sp.discriminant(g, lams))
ident = sp.expand(sp.discriminant(f1, lams)*sp.discriminant(f2, lams)
                  *sp.resultant(f1, f2, lams)**2)
print("(E) disc(f1 f2) = disc(f1)disc(f2)res(f1,f2)^2 identically:", discg == ident)
assert discg == ident
print("(E) disc(f_i) = 16(h_i^2+n_i):", sp.simplify(sp.discriminant(f1, lams) - 16*(h1v**2 + n1v)) == 0,
      "; >0 for positive data:", (16*(h1v**2 + n1v)).is_positive)
assert sp.simplify(sp.discriminant(f1, lams) - 16*(h1v**2 + n1v)) == 0
sub_ex = {h1v: 3, n1v: 7, h2v: 5, n2v: 11}          # shared root: v = -3+sqrt(16) = 1 = n2-form
gex = sp.expand(g.subs(sub_ex))
print("(E) exact example g = (lam^2+12lam-28)(lam^2+20lam-44):", sp.factor(gex))
print("(E) g(2) =", gex.subs(lams, 2), " g'(2) =", sp.diff(gex, lams).subs(lams, 2),
      " g''(2) =", sp.diff(gex, lams, 2).subs(lams, 2))
assert gex.subs(lams, 2) == 0 and sp.diff(gex, lams).subs(lams, 2) == 0
assert sp.diff(gex, lams, 2).subs(lams, 2) != 0
print("(E) disc(g) not identically zero:", discg != 0,
      "; generic sample disc =", discg.subs({h1v: 1, h2v: 2, n1v: 3, n2v: 6}))
assert discg != 0 and discg.subs({h1v: 1, h2v: 2, n1v: 3, n2v: 6}) != 0
uE = make_u(8)
evE = charge_spec(uE, 2, np.diag([3.0, 5.0]), np.diag([7.0, 11.0]))
print("(E) charge spectrum (exact example):", np.round(evE, 10), " (mult-2 at lam=2)")
assert np.abs(evE - np.array([-22.0, -14.0, 2.0, 2.0])).max() < 1e-9
gapsE = np.diff(np.sort(evE))
assert gapsE[2] < 1e-9 and min(gapsE[0], gapsE[1]) > 5   # multiplicity exactly 2
evP = charge_spec(uE, 2, np.diag([3.0, 5.0]), np.diag([7.0, 11.001]))
gP = np.diff(np.sort(evP)).min()
print("(E) split under n2 -> 11+1e-3: min gap %.3e (linear splitting)" % gP)
assert 1e-5 < gP < 1e-1

# ---------------- (F) general-K q=2 simplicity sampling ----------------
nsimp = 0; worstrelF = 0.0
for _ in range(400):
    Hm = rand_herm(2); Bk = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
    Km = Bk @ Bk.conj().T + 0.3*np.eye(2)
    evF = charge_spec(uE, 2, Hm, Km)
    rel = np.diff(evF).min()/np.abs(evF).max()
    worstrelF = max(worstrelF, rel)
    if rel > 1e-7: nsimp += 1
print("(F) general-K q=2: %d/400 fully simple spectrum" % nsimp)
assert nsimp == 400

# ---------------- (G) codim-3 onset in the scalar-K class ----------------
uG = make_u(11); qG = 3; hG = 0.9; nG = 2.0
worstG = 0.0
for direction in range(3):
    V = rand_herm(qG); V = V - np.trace(V)/qG*np.eye(qG)
    while np.diff(np.linalg.eigvalsh(V)).min() < 0.2:
        V = rand_herm(qG); V = V - np.trace(V)/qG*np.eye(qG)
    gs = [np.diff(charge_spec(uG, qG, hG*np.eye(qG) + e*V, nG*np.eye(qG))).min()
          for e in [1e-4, 1e-3, 1e-2]]
    sl = [np.log(gs[i+1]/gs[i])/np.log(10.0) for i in range(2)]
    worstG = max(worstG, max(abs(s - 1) for s in sl))
    print("(G) traceless direction %d: gap-vs-eps log-log slopes %s" % (direction, np.round(sl, 4)))
assert worstG < 0.02
print("ALL S3 ASSERTS PASS")
