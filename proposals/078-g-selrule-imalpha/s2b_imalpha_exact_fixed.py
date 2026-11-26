# s2b_imalpha_exact_fixed.py
# Fixed regeneration of s2_imalpha_exact.py (078 session 2, 2026-11-17).
# LINEAGE (see manifest.md): the predecessor s2_imalpha_exact.out is a crash trace -
# it died at line 42, sp.diff(Dsimple, a2), ValueError "Can't calculate derivative
# wrt a1 + d" because a2 is the Python sum a1+d, not a symbol. Sections (B),(C),(D)
# never ran. Two fixes applied:
#  (i) slope line: derivative taken wrt d at fixed a1 (a2 = a1 + d, so d/dd at fixed
#      a1 equals d/da2 at fixed a1; the printed quantity dD/da2 at a2=a1 is unchanged).
#  (iii) U2 assert (never executed in the predecessor, hence untested): |U2(eps)-U2(0)| < 1e-9
#      is wrong, U2 varies linearly in eps; replaced by exact finite-eps closed-form match
#      plus linear-approach bounds.
#  (ii) eigenvalue methodology: the predecessor fed -2j*M to np.linalg.eigvalsh. That
#      is invalid: -2iM is NOT Hermitian (block (1,2) is -2iZ0, while block (2,1)^dag
#      is -2iI), and eigvalsh silently uses only the lower triangle (symmetrized row
#      blocks would give +/-2*sqrt(a^2+1), dropping n). All spectra here are computed
#      from the genuinely Hermitian charge Q~ = -2i(UR^dag - RU^dag) (asserted
#      Hermitian), keeping the 2q nonzero eigenvalues (the rank <= 2q factorization),
#      cross-checked against the exact row-pair closed forms.
# Class: q=2 coincident-copy block data of 077 (N fixed, q fixed); commuting subclass
#   C0 = diag(alpha_1, alpha_2), K = diag(n1, n2), spectrum = union of the two row
#   pairs lam_f+- = -2 Im a_f +- 2 sqrt((Im a_f)^2 + n_f), a_f = Im alpha_f.
# Checks:
#  (A) symbolic: norm-equalization n1=n2=n>0, a1>0, a2=a1+d (d>0): sorted order
#      e = [l2-,l1-,l2+,l1+]; shipped D statistic D = ((a2-a1)+(r2-r1))/(a2+r2);
#      D=0 iff d=0; exact linear onset dD/da2|eq = 1/sqrt(a1^2+n); U2 Tr-form at
#      a1=a2 equals 4a1^2(a1^2+n)/(4a1^4+4a1^2 n+n^2) > 0 for a1>0 (U2 does NOT
#      vanish on the Im-matched norm-equalized double pair unless a1=0: D, not U2,
#      is the exact norm-equalized selector).
#  (B) symbolic: commuting q=2 double spectrum (shared row root) iff a1=a2 AND n1=n2
#      (resultant tests at the three degeneracy branches); row factor never
#      self-coalesces (disc<0 for A,N>0). NOTE: "double spectrum" here = the q=2
#      double-pair/tiling multiset of 077; a single multiplicity-2 eigenvalue can
#      also occur off-diagonal (see s3 (F)) - these are different loci.
#  (C) numeric through the Hermitian charge: norm-equalized mismatched data realize
#      the predicted pairs exactly; D(eps) linear with slope 1 (log-log); U2 at
#      eps=1e-4 equals the closed-form limit (diagnostic; rank-full guard asserted).
#  (D) numeric non-commuting control: at 300 random non-scalar (H,K), K>0, the four
#      nonzero eigenvalues of the charge are distinct: no multiplicity 2 off the
#      scalar locus.
# No manuscript I/O. Run: python -I s2b_imalpha_exact_fixed.py > s2b_imalpha_exact_fixed.out 2>&1
import numpy as np
import sympy as sp

# ---------------- (A) symbolic closed forms ----------------
a1, d, n = sp.symbols('a1 d n', positive=True)      # a2 = a1 + d: strict ordering
a2 = a1 + d
r1 = sp.sqrt(a1**2 + n); r2 = sp.sqrt(a2**2 + n)
# sorted eigenvalues (lam^- decreasing in a; lam^- < 0 < lam^+; middle gap
# e[2]-e[1] = 2(r2+r1) - 2d > 0 since r2 > a2 and d = a2-a1 < a2 < r2):
e = [-2*a2 - 2*r2, -2*a1 - 2*r1, -2*a2 + 2*r2, -2*a1 + 2*r1]
gap1 = sp.simplify(e[1] - e[0]); gap2 = sp.simplify(e[3] - e[2]); gapm = sp.simplify(e[2] - e[1])
print("(A) gaps: g1 =", gap1, "  g2 =", gap2, "  gmid =", gapm)
print("(A) g1-g2 =", sp.simplify(gap1 - gap2), " equals 4(r2-r1):",
      sp.simplify((gap1 - gap2) - 4*(r2 - r1)) == 0)
assert sp.simplify((gap1 - gap2) - 4*(r2 - r1)) == 0        # so max gap = gap1 for d>0
Dclosed = sp.simplify(gap1 / (2*a2 + 2*r2))                  # max|e| = |e[0]| = 2a2+2r2
Dsimple = sp.simplify(((a2 - a1) + (r2 - r1))/(a2 + r2))
print("(A) D closed form (norm-equalized mismatch, a2>a1) =", sp.simplify(Dclosed))
print("(A) D == ((a2-a1)+(r2-r1))/(a2+r2):", sp.simplify(Dclosed - Dsimple) == 0)
assert sp.simplify(Dclosed - Dsimple) == 0
assert sp.simplify(Dsimple.subs(d, 0)) == 0                       # D=0 iff Im match
# FIX (i): derivative wrt d at fixed a1; equals d/da2 at fixed a1 since a2 = a1 + d:
slope = sp.simplify(sp.diff(Dsimple, d).subs(d, 0))
print("(A) exact linear onset dD/da2 at a2=a1 [FIXED line]:", slope)     # expect 1/sqrt(a1^2+n)
assert sp.simplify(slope - 1/r1) == 0
# U2 (shipped Tr-form): U2 = Tr e^4 / (4 (Tr e^2/4)^2) - 1
Tr2 = sum(x**2 for x in e); Tr4 = sum(x**4 for x in e)
U2closed = sp.simplify(4*Tr4/Tr2**2 - 1)
U2eq = sp.simplify(U2closed.subs(d, 0))
print("(A) U2 at a1=a2 (norm equalized, pairs coincide):", sp.factor(U2eq))
assert sp.simplify(U2eq - 4*a1**2*(a1**2 + n)/(4*a1**4 + 4*a1**2*n + n**2)) == 0
assert (4*a1**2*(a1**2 + n)/(4*a1**4 + 4*a1**2*n + n**2)).is_positive  # >0 for a1>0
U2lim = sp.simplify(sp.limit(U2eq, a1, 0))
print("(A) U2 -> 0 as a -> 0 (symmetric multiset):", U2lim == 0); assert U2lim == 0

# ---------------- (B) resultant criterion, commuting class ----------------
t = sp.Symbol('t')
A1, A2, N1, N2 = sp.symbols('A1 A2 N1 N2', positive=True)
f1 = t**2 + 2*sp.I*A1*t + N1
f2 = t**2 + 2*sp.I*A2*t + N2
res = sp.factor(sp.resultant(sp.expand(f1), sp.expand(f2), t))
dd = sp.Symbol('d', positive=True)
print("(B) resultant(f1,f2) =", res)
print("(B) res(a2=a1,n2=n1) =", sp.simplify(res.subs({A2: A1, N2: N1})))
print("(B) res(a2=a1,n2=n1+d) =", sp.factor(res.subs({A2: A1, N2: N1 + dd})))
print("(B) res(n2=n1,a2=a1+d) =", sp.factor(res.subs({N2: N1, A2: A1 + dd})))
assert sp.simplify(res.subs({A2: A1, N2: N1})) == 0
assert res.subs({A2: A1, N2: N1 + dd}) != 0
assert res.subs({N2: N1, A2: A1 + dd}) != 0
# row pair itself never has a double root at K>0: discriminant -4(A^2+N) < 0:
disc1 = sp.simplify(sp.discriminant(sp.expand(f1), t))
print("(B) discriminant of row factor:", disc1, "< 0 for A1,N1>0:", disc1.is_negative)
assert disc1.is_negative

# ---------------- (C) numeric through the Hermitian charge ----------------
# FIX (ii): spectra from Q~ = -2i(UR^dag - RU^dag), Hermitian by construction.
rng = np.random.default_rng(20261117 + 2)
q, N = 2, 6
u = rng.normal(size=N) + 1j*rng.normal(size=N); u /= np.linalg.norm(u)
U = np.kron(np.eye(q), u.reshape(-1, 1)); P = np.eye(q*N) - U@U.conj().T
Vp = np.linalg.svd(P)[0][:, :q]                    # orthonormal basis of range(P)
def realize(H, K):                                  # U^dag R = iH (Im C0 = H), R^dag P R = K
    return U @ (1j*H) + Vp @ np.linalg.cholesky(K).conj().T
def charge_spec(H, K):                              # the 2q nonzero eigenvalues of Q~
    R = realize(H, K)
    Q = -2j*(U@R.conj().T - R@U.conj().T)
    assert np.allclose(Q, Q.conj().T, atol=1e-11)  # Hermitian
    ev = np.linalg.eigvalsh(Q)
    o = np.argsort(np.abs(ev))
    assert np.abs(ev[o[:q*N-2*q]]).max() < 1e-9    # exactly qN-2q zeros (rank 2q here)
    return np.sort(ev[o[q*N-2*q:]])
def Dstat(e):
    e = np.sort(e)
    return max(e[1] - e[0], e[3] - e[2])/np.abs(e).max()
def U2stat(e):
    return np.sum(e**4)/(4*(np.sum(e**2)/4)**2) - 1
def spec_of(a1v, a2v, n0):                          # spectrum via the Hermitian charge
    return charge_spec(np.diag([a1v, a2v]), np.eye(q)*n0)
n0 = 3.7
for (a1v, a2v) in [(0.8, 0.8), (0.8, 0.8 + 1e-3), (0.8, 1.3), (0.8, 2.5)]:
    ev = spec_of(a1v, a2v, n0)
    assert np.abs(ev).min() > 1e-6                 # rank-full (K = n0 I > 0)
    pred = sorted([x for av in (a1v, a2v) for x in (-2*av - 2*np.sqrt(av**2 + n0),
                                                     -2*av + 2*np.sqrt(av**2 + n0))])
    dev = np.abs(ev - pred).max()
    print("(C) a=(%.4f,%.4f): spec-vs-row-pairs dev %.3e   D=%.8f   U2=%.8f" %
          (a1v, a2v, dev, Dstat(ev), U2stat(ev)))
    assert dev < 1e-9
# exact linear onset of D in eps; U2 limit value at eps=0:
eps_list = [1e-4, 1e-3, 1e-2, 1e-1]
Ds = [Dstat(spec_of(0.8, 0.8 + eps, n0)) for eps in eps_list]
U2s = [U2stat(spec_of(0.8, 0.8 + eps, n0)) for eps in eps_list]
slD = [np.log(Ds[i+1]/Ds[i])/np.log(eps_list[i+1]/eps_list[i]) for i in range(3)]
print("(C) D vs eps log-log slopes (expect 1, exact):", np.round(slD, 4))
assert all(abs(s - 1) < 0.02 for s in slD)
def U2closed_val(a1v, a2v, n0v):                    # closed-form U2 at finite mismatch
    ev = [x for av in (a1v, a2v) for x in (-2*av - 2*np.sqrt(av**2 + n0v),
                                           -2*av + 2*np.sqrt(av**2 + n0v))]
    return np.sum(np.array(ev)**4)/(4*(np.sum(np.array(ev)**2)/4)**2) - 1
U2eq_closed = U2closed_val(0.8, 0.8, n0)
print("(C) U2 values (diagnostic):", ["%.6f" % x for x in U2s],
      " closed-form limit at eps=0:", "%.6f" % U2eq_closed,
      " diff(eps=1e-4, limit):", "%.2e" % abs(U2s[0] - U2eq_closed))
# FIX (iii): the predecessor asserted |U2(eps)-U2(0)| < 1e-9; U2 varies LINEARLY in eps
# (slope ~0.36 at these data), so that assert was wrong and would have failed. Correct
# checks: exact match to the finite-eps closed form, and linear approach to the limit.
assert abs(U2s[0] - U2closed_val(0.8, 0.8 + 1e-4, n0)) < 1e-12
assert abs(U2s[0] - U2eq_closed) < 1e-3 and abs(U2s[1] - U2eq_closed) < 1e-2
assert abs((U2s[0] - U2eq_closed)/1e-4 - (U2s[1] - U2eq_closed)/1e-3) < 1e-3

# ---------------- (D) non-commuting control ----------------
nsimple = 0
for trial in range(300):
    Ar = rng.normal(size=(q, q)) + 1j*rng.normal(size=(q, q))
    Hm = (Ar + Ar.conj().T)/2                       # generic Hermitian (non-scalar a.s.)
    Bk = rng.normal(size=(q, q)) + 1j*rng.normal(size=(q, q))
    Km = Bk @ Bk.conj().T + 0.5*np.eye(q)           # positive definite
    ev = charge_spec(Hm, Km)                        # FIX (ii): Hermitian-charge spectra
    if np.diff(ev).min()/np.abs(ev).max() > 1e-7: nsimple += 1
print("(D) non-scalar (H,K), K>0: %d/300 with fully simple spectrum" % nsimple)
assert nsimple == 300
print("ALL S2B ASSERTS PASS")
