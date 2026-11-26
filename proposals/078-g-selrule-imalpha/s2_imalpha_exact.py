# s2_imalpha_exact.py
# The Im-alpha branch at EXACT-spectra level (no N-scaling, no leading order).
# Class: q=2 coincident-copy block-cut data of 077 (N>=4, fixed q); commuting subclass
#   C0 = diag(alpha_1, alpha_2), K = diag(n1, n2) (copy-diagonal momenta), spectrum = union
#   of the two row pairs lam_f+- = -2 Im a_f +- 2 sqrt((Im a_f)^2 + n_f), a_f = Im alpha_f.
# Checks:
#  (A) symbolic: norm-equalization n1=n2=n>0, a1>0, a2=a1+d (d>0): sorted order
#      e = [l2-,l1-,l2+,l1+] (gap1-gap2 = 4(r2-r1) > 0 since r(a)=sqrt(a^2+n) strictly increases);
#      shipped D statistic D = ((a2-a1)+(r2-r1))/(a2+r2); D=0 iff d=0; exact linear onset
#      dD/da2|eq = 1/sqrt(a1^2+n); U2 Tr-form at a1=a2 equals
#      4a1^2(a1^2+n)/(4a1^4+4a1^2 n+n^2) > 0 for a1>0 (U2 does NOT vanish on the Im-matched
#      norm-equalized double pair unless a1=0): D, not U2, is the exact norm-equalized selector.
#  (B) symbolic: commuting q=2 double spectrum (shared row root) iff a1=a2 AND n1=n2
#      (resultant tests at the three degeneracy branches); row factor never self-coalesces (disc<0).
#  (C) numeric through the full 4x4 pencil: norm-equalized mismatched data realize the
#      predicted pairs exactly; D(eps) linear with slope 1 (log-log); U2 at eps=1e-4 equals
#      the closed-form limit (nonzero: U2 is not the exact selector for a>0).
#  (D) numeric non-commuting control: at 300 random non-scalar (H,K) with K>0 the 4
#      eigenvalues of T are distinct: no multiplicity 2 off the scalar locus.
# No manuscript I/O. Run: python -I s2_imalpha_exact.py > s2_imalpha_exact.out 2>&1
import numpy as np
import sympy as sp

# ---------------- (A) symbolic closed forms ----------------
a1, d, n = sp.symbols('a1 d n', positive=True)      # a2 = a1 + d: strict ordering
a2 = a1 + d
r1 = sp.sqrt(a1**2 + n); r2 = sp.sqrt(a2**2 + n)
# sorted eigenvalues (lam^- decreasing in a; lam^- < 0 < lam^+; middle gap
# e[2]-e[1] = 2(r2+r1) - 2d > 2(r2-r1... ) > 0 since r2 > a2 and d = a2-a1 < a2 < r2):
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
slope = sp.simplify(sp.diff(Dsimple, a2).subs(d, 0))
print("(A) exact linear onset dD/da2 at a2=a1:", slope)           # expect 1/sqrt(a1^2+n)
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

# ---------------- (C) numeric through the full pencil ----------------
rng = np.random.default_rng(20261117 + 2)
q, N = 2, 6
u = rng.normal(size=N) + 1j*rng.normal(size=N); u /= np.linalg.norm(u)
U = np.kron(np.eye(q), u.reshape(-1, 1)); P = np.eye(q*N) - U@U.conj().T
Vp = np.linalg.svd(P)[0][:, :q]                    # orthonormal basis of range(P)
def realize(H, K):                                  # U^dag R = iH (Im C0 = H), R^dag P R = K
    return U @ (1j*H) + Vp @ np.linalg.cholesky(K).conj().T
def Dstat(e):
    e = np.sort(e)
    return max(e[1] - e[0], e[3] - e[2])/np.abs(e).max()
def U2stat(e):
    return np.sum(e**4)/(4*(np.sum(e**2)/4)**2) - 1
def spec_of(a1v, a2v, n0):                          # spectrum via the FULL pencil T=-2iM
    R = realize(np.diag([a1v, a2v]), np.eye(q)*n0)
    C0 = U.conj().T @ R
    M = np.block([[C0.conj().T, R.conj().T@R], [-np.eye(q), -C0]])
    return np.sort(np.linalg.eigvalsh(-2j*M))
n0 = 3.7
for (a1v, a2v) in [(0.8, 0.8), (0.8, 0.8 + 1e-3), (0.8, 1.3), (0.8, 2.5)]:
    ev = spec_of(a1v, a2v, n0)
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
U2eq_closed = 4*0.8**2*(0.8**2 + n0)/(4*0.8**4 + 4*0.8**2*n0 + n0**2)
print("(C) U2 values:", ["%.6f" % x for x in U2s],
      " closed-form limit:", "%.6f" % U2eq_closed,
      " diff at eps=1e-4:", "%.2e" % abs(U2s[0] - U2eq_closed))
assert abs(U2s[0] - U2eq_closed) < 1e-9

# ---------------- (D) non-commuting control ----------------
nsimple = 0
for trial in range(300):
    Ar = rng.normal(size=(q, q)) + 1j*rng.normal(size=(q, q))
    Hm = (Ar + Ar.conj().T)/2                       # generic Hermitian (non-scalar a.s.)
    Bk = rng.normal(size=(q, q)) + 1j*rng.normal(size=(q, q))
    Km = Bk @ Bk.conj().T + 0.5*np.eye(q)           # positive definite
    M = np.block([[(1j*Hm).conj().T, Km + (1j*Hm).conj().T@(1j*Hm)],
                  [-np.eye(q), -(1j*Hm)]])
    ev = np.sort(np.linalg.eigvalsh(-2j*M))
    if np.diff(ev).min()/np.abs(ev).max() > 1e-7: nsimple += 1
print("(D) non-scalar (H,K), K>0: %d/300 with fully simple spectrum" % nsimple)
assert nsimple == 300
print("ALL S2 ASSERTS PASS")
