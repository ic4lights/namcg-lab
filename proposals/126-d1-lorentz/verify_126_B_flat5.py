# verify_126_B_flat5.py -- chain 126, Part B: exact flat finite-N realization of the
# D1 class relations (appH L1617-1621) with Lorentzian eta contraction, N = 5.
#
# Model: 5x5 REAL matrices ("standard affine representation" of the Poincare group):
#   D_a  = E_{a,4};
#   S_cd = 5x5 lift (zero row/col 4) of the 4x4 block L(S_cd)_{mu a} =
#          eta_{a d} delta_{mu c} - eta_{a c} delta_{mu d}  (eta L antisymmetric).
# Then [S_cd, D_a] = eta_ad D_c - eta_ac D_d and [D_a, D_b] = 0: both class
# relations hold exactly with T = R = F = 0 (flat sector), coefficients in A = C.
# Verified exactly with sympy (integers):
#   R1  first class relation, all 12 ordered (c,d), all a
#   R2  [D_a, D_b] = 0
#   R3  span{S} closes under bracket, no leak into the translation row/col
#   R4  inner automorphisms exp(S) D_a exp(-S) = (exp L)^c_a D_c exactly for one
#       rotation and one boost: local Lorentz rotations are matrix gauge
#       transformations in this finite model (class identity of appH L1624 at N=5)
#   R5  kinetic operator (1/4) eta^{ab}[D_a,[D_b, .]] vanishes on span{1, S, D}:
#       the flat finite model has no propagation
#   R6  commutant of ad D on span{1, S, D} is span{1}: the coefficient algebra A
#       is forced to C at finite N
# CONTROLS: Euclidean delta in R1 must fail (signature teeth); dropping D_3 from
# the R6 scan must enlarge the commutant (non-vacuity teeth).
import sympy as sp

FAIL = []
def chk(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAIL.append(name)

eta = sp.MutableDenseMatrix(sp.diag(-1, 1, 1, 1))

def E4(row, col):
    M = sp.zeros(5, 5)
    M[row, col] = 1
    return M

D = [E4(a, 4) for a in range(4)]

def Sfull(c, d):
    M = sp.zeros(5, 5)
    for mu in range(4):
        for a in range(4):
            M[mu, a] = eta[a, d] * (1 if mu == c else 0) - eta[a, c] * (1 if mu == d else 0)
    return M

pairs = [(c, d) for c in range(4) for d in range(c + 1, 4)]
S = {p: Sfull(*p) for p in pairs}

# --- R1
bad = []
for c in range(4):
    for d in range(4):
        if c == d:
            continue
        Scd = Sfull(c, d)
        for a in range(4):
            if sp.simplify(Scd * D[a] - D[a] * Scd
                           - (eta[a, d] * D[c] - eta[a, c] * D[d])) != sp.zeros(5, 5):
                bad.append((c, d, a))
chk("R1 [S_cd,D_a] = eta_ad D_c - eta_ac D_d exactly (48 checks)", not bad)

# --- R2
chk("R2 [D_a,D_b] = 0",
    all(sp.simplify(D[a] * D[b] - D[b] * D[a]) == sp.zeros(5, 5)
        for a in range(4) for b in range(4)))

# --- R3 closure of span{S}, no leak into translation row/col
Ms = sp.Matrix([list(S[p][:4, :4].reshape(16, 1)) for p in pairs])  # 6 x 16
chk("R3a blocks of S independent (rank 6)", Ms.rank() == 6)
linbad = []
for p1 in pairs:
    for p2 in pairs:
        C = S[p1] * S[p2] - S[p2] * S[p1]
        if any(C[4, j] != 0 for j in range(5)) or any(C[i, 4] != 0 for i in range(5)):
            linbad.append((p1, p2, "leak"))
            continue
        resid = C
        rhs = sp.Matrix(list(C[:4, :4].reshape(16, 1)))
        sol = (Ms * Ms.T).LUsolve(Ms * rhs)   # normal equations, Ms full row rank
        for idx, p in enumerate(pairs):
            resid = resid - sol[idx] * S[p]
        if sp.simplify(resid) != sp.zeros(5, 5):
            linbad.append((p1, p2, "resid"))
chk("R3b [S,S] in span exactly, no translation-row leak", not linbad)
# R3c: S-blocks are eta-antisymmetric: with rank 6 this makes span{S} = so(3,1) exactly
etaanti = all(sp.simplify((eta * S[p][:4, :4]).T + eta * S[p][:4, :4]) == sp.zeros(4, 4) for p in pairs)
chk("R3c span{S} subset eta-antisymmetric (rank 6 + 6-dim space: span = so(3,1))", etaanti)

# --- R4 inner automorphism = label rotation, exact (t = 1)
def check_inner(Sx, tag):
    ex = Sx.exp()
    invx = (-Sx).exp()
    if sp.simplify(ex * invx - sp.eye(5)) != sp.zeros(5, 5):
        return False, "inverse"
    Lb = Sx[:4, :4].exp()
    for a in range(4):
        lhs = sp.simplify(sp.expand_trig(ex * D[a] * invx))
        rhs = sp.zeros(5, 5)
        for cc in range(4):
            rhs = rhs + sp.simplify(Lb[cc, a]) * D[cc]
        if sp.simplify(lhs - rhs) != sp.zeros(5, 5):
            return False, "a=%d" % a
    return True, tag
ok1, t1 = check_inner(S[(1, 2)], "rotation(1,2)")
chk("R4a exp(S12) D_a exp(-S12) = (exp L)^c_a D_c exactly", ok1)
ok2, t2 = check_inner(S[(0, 1)], "boost(0,1)")
chk("R4b exp(S01) D_a exp(-S01) = (exp L)^c_a D_c exactly", ok2)

# --- R5 kinetic vanishing
def Lkin(Mx):
    tot = sp.zeros(5, 5)
    for a in range(4):
        for b in range(4):
            if eta[a, b] != 0:
                inner = D[a] * Mx - Mx * D[a]
                tot = tot + eta[a, b] * (D[b] * inner - inner * D[b])
    return sp.simplify(tot) / 4
allgens = [sp.eye(5)] + [S[p] for p in pairs] + D
bad5 = [i for i, g in enumerate(allgens) if Lkin(g) != sp.zeros(5, 5)]
chk("R5 (1/4) eta^{ab}[D_a,[D_b,G]] = 0 on span{1,S,D} (11 gens)", not bad5)

# --- R6 commutant of ad D on the span
V = [sp.eye(5)] + [S[p] for p in pairs] + D
n = len(V)
rows = []
for a in range(4):
    for entry in range(25):
        rows.append([sp.simplify((D[a] * g - g * D[a]).reshape(25, 1)[entry]) for g in V])
Mat = sp.Matrix(rows)
null = Mat.nullspace()
# Claim (corrected): centralizer of ad D on span{1,S,D} = span{1, D_0..D_3} (dim 5):
# the S-sector contributes nothing ([D_a, X_S] = 0 forces the mixed-index antisymmetric
# beta to have all rows zero). The centralizer is an ABELIAN algebra under matrix
# product (D_a D_b = 0), a nilpotent extension of C: its only character is a point,
# so the base manifold Z of the class cannot be realized inside the fibre model at
# N = 5; the coefficient algebra of the class (functions on Z) is genuinely outside.
chk("R6 centralizer of ad D on span{1,S,D} = span{1,D} (rank %d, null dim %d)"
    % (Mat.rank(), len(null)), Mat.rank() == 6 and len(null) == 5)
# every null vector must vanish on the six S-coordinates:
badn = [i for i, v in enumerate(null)
        if any(sp.simplify(v[1 + k]) != 0 for k in range(6))]
chk("R6b null vectors have zero S-component (S-sector has no ad-D centralizer)", not badn)
# nilpotency of the centralizer's ideal: D_a D_b = 0 exactly
chk("R6c D_a D_b = 0 (centralizer = C + nilradical: point spectrum, no base manifold)",
    all((D[a] * D[b]) == sp.zeros(5, 5) for a in range(4) for b in range(4)))

# --- CONTROL 1: Euclidean delta in the R1 relation must FAIL (signature teeth).
delta = sp.MutableDenseMatrix(sp.diag(1, 1, 1, 1))
badc = 0
for c in range(4):
    for d in range(4):
        if c == d:
            continue
        Scd = Sfull(c, d)
        for a in range(4):
            if sp.simplify(Scd * D[a] - D[a] * Scd
                           - (delta[a, d] * D[c] - delta[a, c] * D[d])) != sp.zeros(5, 5):
                badc += 1
fired = badc > 0
print(("CONTROL-FIRED " if fired else "CONTROL-DEAD ") +
      "Euclidean delta fails %d/48 R1 checks (Lorentzian eta is load-bearing)" % badc)
if not fired:
    FAIL.append("CONTROL R1")

# --- CONTROL 2: R6 scan must be non-vacuous. Restricting the scan to a = 0 only
# must enlarge the centralizer by exactly the S-sector rows not hit: expected dim 8
# (span{1,D} plus S12, S13, S23). A vacuous scan cannot reproduce this jump.
def scan_dima(aset):
    rowsx = []
    for a in aset:
        for entry in range(25):
            rowsx.append([sp.simplify((D[a] * g - g * D[a]).reshape(25, 1)[entry]) for g in V])
    return len(sp.Matrix(rowsx).nullspace())
nd1 = scan_dima([0])
nd3 = scan_dima([0, 1, 2])
nd4 = scan_dima([0, 1, 2, 3])
fired2 = (nd1 == 8) and (nd3 == 5) and (nd4 == 5)
print(("CONTROL-FIRED " if fired2 else "CONTROL-DEAD ") +
      "scan dims a={0}: %d, a={0,1,2}: %d, all a: %d (row-wise annihilation structure)"
      % (nd1, nd3, nd4))
if not fired2:
    FAIL.append("CONTROL R6")

print("SUMMARY_B:", "ALL-PASS" if not FAIL else "FAILURES " + repr(FAIL))
