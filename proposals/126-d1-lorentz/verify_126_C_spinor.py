# verify_126_C_spinor.py -- chain 126, Part C: exact curved finite-N realization of the
# D1 class relations (appH L1617-1621) on the spinor module, N = 4 (complex).
#
# Model: Hilbert space C^4; D_a = gamma_a (Clifford, {gamma_a,gamma_b} = 2 eta_ab I),
# S_cd = s * (1/4)[gamma_c, gamma_d] where the overall sign s = +-1 is FIXED by the
# first class relation (C1) from the data, not chosen. Then both class relations hold
# EXACTLY with Lorentzian eta:
#   (r1) [S_cd, D_a] = eta_ad D_c - eta_ac D_d                      (48 checks)
#   (r2) [D_a, D_b]  = 1/2 R_ab^{cd} S_cd,  R_ab^{cd} = 4 s (d_a^c d_b^d - d_b^c d_a^d)
#        T = 0, F = 0 (constant-curvature Riemannian-type tensor).
# Matrix equation of the class (appH L1626-1630, T = 0, constant R, F = 0):
#   [D^a,[D_a,D_b]] must equal R_ab^{ae} D_e. Direct Clifford computation gives 12 D_b
#   while R_ab^{ae} D_e = 12 s D_b: consistency FORCES s = +1 (C3). With s = +1 the
#   model has R_ab{}^{ae} = 12 d_b^e, i.e. via the manuscript identification
#   R_ab{}^{ae} = -Ric_b{}^e at T = 0 (appH L1628), Ric = -12 eta: an Einstein,
#   maximally symmetric solution of the same algebraic type as the flat-point example
#   (appH L1638-1675) but CURVED and at N = 4, where the flat Part B model has zero
#   kinetic term.
# Structural facts verified exactly:
#   * structure: gamma_0 anti-Hermitian, gamma_i Hermitian; Sigma_0i Hermitian,
#     Sigma_ij anti-Hermitian. The spinor SO(3,1) action is NOT unitary; by Part A the
#     mixed * structure is FORCED at finite N (no basis choice makes all S anti-Hermitian).
#   - End(C^4) = Cl_{3,1} = M_4(C) is a class module: the 16 Dirac bilinears
#     {1, gamma_a, S_cd (c<d), gamma_a gamma5, gamma5} are linearly independent (rank 16:
#     they span all of End) and all [S,.], [D,.] structure constants on this basis are
#     rational. (Note: S_cd gamma5 are NOT new elements - the dual tensor map is an
#     automorphism of span{S_cd}; the 16-basis uses the axial vectors gamma_a gamma5.)
#   - Kinetic operator L = (1/4) eta^{ab}[D_a,[D_b, .]] preserves each of the five
#     Clifford-grade sectors and acts as a scalar on each:
#       L(1) = 0 (only harmonic sector), L(gamma_e) = 3 s gamma_e, L(S_cd) = 2 s S_cd,
#       L(gamma5) and L(gamma_a gamma5) with exact eigenvalues computed (C5e, C5f).
#     All non-scalar eigenvalues are nonzero: the curved finite model propagates on
#     every nontrivial sector, unlike the flat Part B model where L vanishes on span{1,S,D}.
# CONTROLS:
#   - Euclidean delta in (r1) must fail (signature teeth);
#   - contracted R-coefficient 36 delta (instead of 12 delta) must fail C3;
#   - the sector test must discriminate: L(1) = 0 while L(gamma_1) != 0, and the
#     gamma-sector and S-sector eigenvalues differ (no "L = lambda Id" degeneracy);
#   - curvature teeth: the flat Part B D_a = E_{a,4} give [D^a,[D_a,D_b]] = 0 != 12 D_b.
import sympy as sp

FAIL = []
def chk(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAIL.append(name)

eta = sp.MutableDenseMatrix(sp.diag(-1, 1, 1, 1))
I2 = sp.eye(2)
Z2 = sp.zeros(2, 2)
paulis = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]),
          sp.Matrix([[1, 0], [0, -1]])]   # true Pauli matrices: sigma_2^2 = +I

def fb(A, B, C, Dd):          # explicit 4x4 from four explicit 2x2 blocks
    return A.row_join(B).col_join(C.row_join(Dd))
g0 = fb(Z2, I2, -I2, Z2)
gam = [g0] + [fb(Z2, ps, ps, Z2) for ps in paulis]

def cb(A, B):
    return A * B - B * A
def ab(A, B):
    return A * B + B * A

# --- C0 Clifford relation and * structure
bad = [(a, b) for a in range(4) for b in range(4)
       if sp.simplify(ab(gam[a], gam[b]) - 2 * eta[a, b] * sp.eye(4)) != sp.zeros(4, 4)]
chk("C0a Clifford {gamma_a,gamma_b} = 2 eta_ab I exactly (16 checks)", not bad)
chk("C0b * structure: gamma_0 anti-Hermitian, gamma_i Hermitian",
    sp.simplify(gam[0] + gam[0].H) == sp.zeros(4, 4)
    and all(sp.simplify(g - g.H) == sp.zeros(4, 4) for g in gam[1:]))  # .H = conj-transpose

pairs = [(c, d) for c in range(4) for d in range(c + 1, 4)]
Sig = {p: sp.Rational(1, 4) * cb(gam[p[0]], gam[p[1]]) for p in pairs}
chk("C0c * structure: Sigma_0i Hermitian, Sigma_ij anti-Hermitian (mixed, forced by Part A)",
    all(sp.simplify(Sig[(0, j)] - Sig[(0, j)].H) == sp.zeros(4, 4) for j in (1, 2, 3))
    and all(sp.simplify(Sig[(i, j)] + Sig[(i, j)].H) == sp.zeros(4, 4)
            for (i, j) in pairs if i > 0))

def Sraw(c, d):
    if c == d:
        return sp.zeros(4, 4)
    p = (min(c, d), max(c, d))
    sgn = 1 if c < d else -1
    return sgn * Sig[p]

# --- C1 first class relation fixes the overall sign s of the spin generators
def rel_violations(Sf, metric):
    badl = []
    for c in range(4):
        for d in range(4):
            if c == d:
                continue
            for a in range(4):
                if sp.simplify(cb(Sf(c, d), gam[a])
                               - (metric[a, d] * gam[c] - metric[a, c] * gam[d])) != sp.zeros(4, 4):
                    badl.append((c, d, a))
    return badl
v_plus = rel_violations(Sraw, eta)
v_minus = rel_violations(lambda c, d: -Sraw(c, d), eta)
s = 1 if len(v_plus) == 0 else -1
chk("C1 exists s with [S_cd,D_a] = eta_ad D_c - eta_ac D_d exactly, 48 checks (viol +:%d -:%d -> s=%+d)"
    % (len(v_plus), len(v_minus), s), min(len(v_plus), len(v_minus)) == 0)
def Scls(c, d):           # the CLASS generator S_cd = s * Sigma_cd
    return s * Sraw(c, d)

# --- C2 second relation in terms of the class generator: R = 4 s (delta-delta)
def check_second(cval):
    badl = []
    for a in range(4):
        for b in range(4):
            if a == b:
                continue
            rhs = sp.zeros(4, 4)
            for cc in range(4):
                for dd in range(4):
                    if cc == dd:
                        continue
                    R = cval * ((1 if a == cc else 0) * (1 if b == dd else 0)
                                - (1 if a == dd else 0) * (1 if b == cc else 0))
                    rhs = rhs + sp.Rational(1, 2) * R * Scls(cc, dd)
            if sp.simplify(cb(gam[a], gam[b]) - rhs) != sp.zeros(4, 4):
                badl.append((a, b))
    return badl
chk("C2 [D_a,D_b] = 1/2 R_ab^{cd} S_cd exactly, R = 4s(delta-delta), T = F = 0 (12 checks)",
    not check_second(4 * s))
chk("C2b [gamma_a,gamma_b] != 0 for some pair (curved: R cannot be set to zero)",
    any(cb(gam[a], gam[b]) != sp.zeros(4, 4) for a in range(4) for b in range(4)))

# --- C3 matrix equation of the class: direct double commutator vs R_ab^{ae} D_e
def ddouble(b):
    tot = sp.zeros(4, 4)
    for a in range(4):
        for c in range(4):
            if eta[a, c] != 0:
                tot = tot + eta[a, c] * cb(gam[c], cb(gam[a], gam[b]))
    return sp.simplify(tot)
bad3a = [b for b in range(4) if sp.simplify(ddouble(b) - 12 * gam[b]) != sp.zeros(4, 4)]
chk("C3a [D^a,[D_a,D_b]] = 12 D_b exactly (direct Clifford, all b)", not bad3a)
bad3b = [b for b in range(4)
         if sp.simplify(ddouble(b) - 12 * s * gam[b]) != sp.zeros(4, 4)]
chk("C3b matrix equation [D^a,[D_a,D_b]] = R_ab^{ae} D_e (R = 4s(delta-delta)): forces s=+1",
    (not bad3b) and s == 1)
print("   C3: R_ab{}^{ae} = 12 s delta_b^e; direct = 12 D_b; F = 0 consistency forces s = %+d" % s)
# CONTROL: wrong contracted coefficient 36 delta must FAIL the same test
firedC = sp.simplify(ddouble(1) - 36 * gam[1]) != sp.zeros(4, 4)
print(("CONTROL-FIRED " if firedC else "CONTROL-DEAD ") +
      "contracted R-coefficient 36 (instead of 12) fails the matrix-equation test")
if not firedC:
    FAIL.append("CONTROL C3")
# CONTROL (curvature teeth): the flat Part B generators D_a = E_{a,4} satisfy
# [D^a,[D_a,D_b]] = 0 while D_b != 0: the C3 identity is a curved-model identity.
Db = [sp.zeros(5, 5) for _ in range(4)]
for a in range(4):
    Db[a][a, 4] = 1
flat2 = sp.zeros(5, 5)
for a in range(4):
    for c in range(4):
        if eta[a, c] != 0:
            x = Db[c] * Db[a] - Db[a] * Db[c]
            flat2 = flat2 + eta[a, c] * (Db[c] * x - x * Db[c])
firedC2 = (flat2 == sp.zeros(5, 5)) and all(Db[b] != sp.zeros(5, 5) for b in range(4))
print(("CONTROL-FIRED " if firedC2 else "CONTROL-DEAD ") +
      "flat Part B D gives [D^a,[D_a,D_b]] = 0 != 12 D_b (C3 is curvature, not identity)")
if not firedC2:
    FAIL.append("CONTROL C3flat")

# --- C4 End(C^4) = Cl_{3,1} = M_4(C) class module on the 16 Dirac bilinears
g5 = sp.simplify(gam[0] * gam[1] * gam[2] * gam[3])
g5sq = sp.simplify(g5 * g5)
chk("C4a gamma5 anticommutes with all gamma_a; gamma5^2 = %s I" % g5sq[0, 0],
    all(sp.simplify(ab(g5, gam[a])) == sp.zeros(4, 4) for a in range(4))
    and g5sq == g5sq[0, 0] * sp.eye(4))
basis = [sp.eye(4)] + list(gam) + [Scls(p[0], p[1]) for p in pairs] \
        + [g * g5 for g in gam] + [g5]
Mb = sp.Matrix([list(sp.Matrix(b).reshape(16, 1)) for b in basis]).T   # 16 x 16
chk("C4b 16 Dirac-bilinear basis {1, gamma_a, S_cd, gamma_a gamma5, gamma5} rank 16",
    Mb.rank() == 16)
scbad = []
for Xg in [Scls(c, d) for c in range(4) for d in range(c + 1, 4)] + gam:
    for bI, bE in enumerate(basis):
        cm = sp.Matrix(sp.simplify(cb(Xg, bE))).reshape(16, 1)
        coeff = Mb.solve(cm)
        if any((not c.is_rational) for c in coeff):
            scbad.append(bI)
chk("C4c all [S,.], [D,.] structure constants on the 16-basis are rational (Cl_3,1 = M_4(C))",
    not scbad)

# --- C5 kinetic operator L = (1/4) eta^{ab}[D_a,[D_b,.]] : sector eigenvalues
def Lkin(Mx):
    tot = sp.zeros(4, 4)
    for a in range(4):
        for c in range(4):
            if eta[a, c] != 0:
                tot = tot + eta[a, c] * cb(gam[c], cb(gam[a], Mx))
    return sp.simplify(tot) / 4
chk("C5a L(1) = 0 (only harmonic sector: constants)", Lkin(sp.eye(4)) == sp.zeros(4, 4))
bad5 = [e for e in range(4) if sp.simplify(Lkin(gam[e]) - 3 * s * gam[e]) != sp.zeros(4, 4)]
chk("C5c L(gamma_e) = 3 s gamma_e exactly (nonzero: curved model propagates)", not bad5)
bad5S = [p for p in pairs
         if sp.simplify(Lkin(Scls(*p)) - 2 * s * Scls(*p)) != sp.zeros(4, 4)]
chk("C5d L(S_cd) = 2 s S_cd exactly for all 6 (S-sector eigenvalue nonzero)", not bad5S)
# pseudoscalar and axial sectors: exact scalar multipliers, extracted entrywise
def sector_eigen(basisEls, tag):
    # returns exact scalar mu s.t. L(E) = mu E for every E in basisEls (all equal), or None
    mus = []
    for E in basisEls:
        pE = sp.simplify(Lkin(E))
        mu = None
        for i in range(4):
            for j in range(4):
                if E[i, j] != 0:
                    mu = sp.simplify(pE[i, j] / E[i, j])
                    break
            if mu is not None:
                break
        okm = all(sp.simplify(sp.simplify(Lkin(E2)) - mu * E2) == sp.zeros(4, 4)
                  for E2 in basisEls)
        mus.append((mu, okm))
    return mus
mus5 = sector_eigen([g5], "g5")
chk("C5e L(gamma5) = mu5 gamma5 exactly, mu5 = %s (computed, nonzero)" % mus5[0][0],
    mus5[0][1] and mus5[0][0] != 0)
musA = sector_eigen([g * g5 for g in gam], "Ag5")
mA = musA[0][0]
chk("C5f L(gamma_a gamma5) = muA (gamma_a gamma5) exactly for all 4, muA = %s" % mA,
    all(ok for (_, ok) in musA) and all(m == mA for (m, _) in musA))
chk("C5g all non-scalar sector eigenvalues nonzero and mutually distinct "
    "(3s, 2s, mu5, muA) = (%s, %s, %s, %s)" % (3 * s, 2 * s, mus5[0][0], mA),
    all(v != 0 for v in (3 * s, 2 * s, mus5[0][0], mA))
    and len(set([3 * s, 2 * s, mus5[0][0], mA])) == 4)
fired5 = (Lkin(sp.eye(4)) == sp.zeros(4, 4)) and (Lkin(gam[1]) != sp.zeros(4, 4)) \
         and (sp.simplify(Lkin(gam[1]) / (3 * s) - Lkin(Scls(1, 2)) / (2 * s)) != sp.zeros(4, 4))
print(("CONTROL-FIRED " if fired5 else "CONTROL-DEAD ") +
      "kinetic: L(1) = 0 but L(gamma_1) != 0 and gamma-sector != S-sector (discriminating)")
if not fired5:
    FAIL.append("CONTROL C5")

# --- CONTROL: Euclidean delta in (r1) must fail (signature teeth for the spinor model)
delta = sp.MutableDenseMatrix(sp.diag(1, 1, 1, 1))
badc2 = len(rel_violations(Scls, delta))
fired1 = badc2 > 0
print(("CONTROL-FIRED " if fired1 else "CONTROL-DEAD ") +
      "Euclidean delta fails %d/48 (r1) checks on the spinor model (eta load-bearing)" % badc2)
if not fired1:
    FAIL.append("CONTROL C1delta")

print("SUMMARY_C:", "ALL-PASS" if not FAIL else "FAILURES " + repr(FAIL))
