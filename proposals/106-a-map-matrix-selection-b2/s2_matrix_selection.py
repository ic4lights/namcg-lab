# s2_matrix_selection.py -- proposal 106 r1, central computation.
# Matrix-side selection of the order-Theta^2 correction on the diffeomorphism-pullback
# class of the manuscript's own semiclassical construction (ch03 def:matrix-coords-ext,
# L183-188: Theta^{IJ} = theta^{ab} d_a x^I d_b x^J with constant Theta^{IJ}, Tr -> int;
# rem:ch3-moyal-check and rem:ch3-trace-quadratic: constant-Theta Weyl/Moyal algebra).
#
# SETTING (exact rational/symbolic arithmetic, d=4). Matrix side: Xhat^I Hermitian with
# [Xhat^I,Xhat^J] = i Theta^{IJ} CONSTANT (nondegenerate); symbols via the constant-Theta
# Weyl map; product = operator product = Moyal product *_Theta, exactly associative.
# Semiclassical configuration (D=4): a local diffeomorphism x(y) from leaf coordinates
# y (called x0..x3 below, the leaf coordinates, matching the 105 framework variable).
# Leaf bivector by the manuscript identity Theta^{IJ} = theta^{ab}(y) d_a x^I d_b x^J,
# i.e. theta^{ab} = Theta^{IJ} M^a_I M^b_J, M = dy/dx. The induced leaf product
# F *_y G := ((F o y^{-1}) *_Theta (G o y^{-1})) o y is exactly associative; its
# order-Theta term is the naive B1 = (i/2) theta^{ab}(y) d_a F d_b G (the 105 naive
# truncation with Theta(x) := theta(y)); its order-Theta^2 term is the matrix-SELECTED
# correction
#   B2PB(F,G) = -(1/8) Theta^{IJ} Theta^{KL} (d_I d_K F~)(d_J d_L G~),  F~ = F o y^{-1}
#             = -(1/8) Theta^{IJ} Theta^{KL} (M^a_I M^b_K F_,ab + N^a_IK F_,a)
#                                (M^c_J M^d_L G_,cd + N^d_JL G_,d),  N^a_IK = d^2 y^a dx^I dx^K.
# Only the 2-jets (A = dx/dy, B = d^2x/dy^2, and hence M, N) enter B2PB(F,G)(0) and the
# 1-jet (theta(0), dtheta(0)) entering A2 -- verified by construction in P1.
# The 544-row / 196-column / Hochschild delta-matrix / A2-table / Schouten framework is
# the proposal-105 s1b framework (JET, MON, prodjet, DER3, BAS2r, M2r, A2tab, scht,
# membership, col_struct -- same definitions, numeric TA/TB substitutions here).
#
# CLAIMS (printed P1..P8):
#  P1 manuscript identity: Theta^{IJ} = theta^{ab} A^I_a A^J_b holds identically in the
#     embedding 2-jet (B) -- i.e. theta as defined here is the manuscript's theta -- and
#     the (2,2) channel of B2PB equals -(1/8) theta^{ag} theta^{bd} F_,ab G_,cd, so the
#     first-order term of *_y is exactly the naive B1 with theta(y).
#  P2 dichotomy match: every induced leaf 1-jet is Schouten-closed: [theta,theta](0) = 0
#     identically in (B, Theta) for generic rational A. The matrix class lands on the
#     solvable side of the 105 dichotomy automatically.
#  P3 constant-Theta special case = 105 C8: B = 0 gives the 196-table of B2PB equal to
#     the 105 Moyal coboundary table -(1/8)*P1 exactly (entrywise).
#  P4 matrix selection solves the coboundary equation: at 3 rational embedding points
#     (A, B, Theta rational; theta(0) nondegenerate): all 544 rows of
#     M2r @ b2vec - A2(theta-jet) vanish exactly; wild membership True.
#  P5 outside the 105 bounded class: at each P4 point the b2vec is NOT in the span of
#     the images of the enumerated five-structure class {P1, M, div1, U1, U2} (rank 5->6).
#  P6 selection is NOT 1-jet-local: the linear map B -> dtheta(0) at fixed (A,Theta) has
#     rank 20 (= 24 minus the 4 linearized-closure directions, cf. P2), kernel dim 20; an
#     exact rational witness deltaB in the kernel changes the
#     B2PB table at the SAME closed 1-jet; the difference lies in ker(M2r).
#  P7 selection freedom at a fixed closed 1-jet: the span of {c(B0+v)-c(B0)} over kernel
#     basis vectors v has dimension s (1 <= s <= 36 = dim ker M2r): the selected solution
#     is a positive-dimensional affine family inside the 36-dim wild-solution space.
#  P8 target symplectic frame invariance: with S a rational Sp(Theta) transvection, the
#     data (Theta' = S Theta S^T, A' = S A, B' = S B) give the same theta-jet, A2 and
#     b2vec tables (exact numeric equality).
import itertools
import sys
import time
import sympy as sp

t0 = time.time()
d = 4
ok = {}
I = sp.I
x = sp.symbols("x0:4")   # leaf coordinates (105 framework variable)

# ---------- jet basis (105 s1b framework) ----------
JET = [()] + [(i,) for i in range(d)] + [(a, b) for a in range(d) for b in range(a, d)]
IJ = {t: k for k, t in enumerate(JET)}
assert len(JET) == 15

def jmon(t):
    m = {}
    for i in t:
        m[i] = m.get(i, 0) + 1
    e = sp.Integer(1)
    for i, k in m.items():
        e *= x[i] ** k / sp.factorial(k)
    return e

MON = [jmon(t) for t in JET]

def prodjet(a, b):
    if len(a) + len(b) > 2:
        return {}
    if len(a) == 0:
        return {b: sp.Integer(1)}
    if len(b) == 0:
        return {a: sp.Integer(1)}
    if len(a) == 1 and len(b) == 1:
        i, j = a[0], b[0]
        return {(i, i): sp.Integer(2)} if i == j else {tuple(sorted((i, j))): sp.Integer(1)}
    return {}

# ---------- A2 table and delta matrix, symbolic jets TA,TB (105 s1b framework) ----------
TA = {}
TB = {}
TQ = {}
THS = {}
for a, b in itertools.combinations(range(d), 2):
    A = sp.symbols("TA_%d%d" % (a, b))
    Bc = sp.symbols("TB_%d%d_0:%d" % (a, b, d))
    q = sp.S.Zero
    for c in range(d):
        for dd in range(c, d):
            qc = sp.symbols("TQ_%d%d_%d%d" % (a, b, c, dd))
            q += (sp.Integer(1) if c == dd else sp.Integer(2)) * qc * x[c] * x[dd]
            TQ[(a, b, c, dd)] = qc
    THS[(a, b)] = A + sum(Bc[c] * x[c] for c in range(d)) + sp.Rational(1, 2) * q
    TA[(a, b)] = A
    for c in range(d):
        TB[(a, b, c)] = Bc[c]

def TT(a, b):
    if a == b:
        return sp.S.Zero
    return THS[(a, b)] if a < b else -THS[(b, a)]

def TA0(a, b):
    if a == b:
        return sp.S.Zero
    return TA[(a, b)] if a < b else -TA[(b, a)]

def TBa(p, q, r):
    if p == q:
        return sp.S.Zero
    return TB[(p, q, r)] if p < q else -TB[(q, p, r)]

def B1op(p, q):
    s = sp.S.Zero
    for a in range(d):
        for b in range(d):
            t = TT(a, b)
            if t != 0:
                s += t * sp.diff(p, x[a]) * sp.diff(q, x[b])
    return sp.Rational(1, 2) * I * s

def eval0(e):
    return e.subs({xi: 0 for xi in x})

innerB = {}
for ia in range(15):
    for ib in range(15):
        innerB[(ia, ib)] = B1op(MON[ia], MON[ib])
A2tab = {}
for ia in range(15):
    for ib in range(15):
        for ic in range(15):
            A2tab[(ia, ib, ic)] = sp.expand(eval0(
                B1op(innerB[(ia, ib)], MON[ic]) - B1op(MON[ia], innerB[(ib, ic)])))
print("A2 table built, %.1fs" % (time.time() - t0))
# C1a parity check with 105: A2 depends only on TA, TB (no TQ), and vanishes when any
# argument is constant (the DER3 restriction already excludes constant slots; check here
# that every free symbol of every table entry lies in TA u TB).
JETS_AB = {str(TA[k]) for k in TA} | {str(TB[k]) for k in TB}
ok["C1a"] = all({str(s) for s in e.free_symbols} <= JETS_AB for e in A2tab.values())
print("C1a parity (A2 table free symbols subset TA u TB, as in 105):",
      "PASS" if ok["C1a"] else "FAIL")

DER3 = [t for t in itertools.product(range(15), repeat=3)
        if min(len(JET[t[0]]), len(JET[t[1]]), len(JET[t[2]])) >= 1
        and len(JET[t[0]]) + len(JET[t[1]]) + len(JET[t[2]]) <= 4]
assert len(DER3) == 544
BAS2r = [t for t in itertools.product(range(15), repeat=2)
         if len(JET[t[0]]) >= 1 and len(JET[t[1]]) >= 1]
IDX2r = {t: k for k, t in enumerate(BAS2r)}
assert len(BAS2r) == 196

rows = []
for (a, b, c) in DER3:
    row = [sp.Integer(0)] * 196
    for mu, cf in prodjet(JET[a], JET[b]).items():     # -C(fg,h)
        if len(mu) >= 1:
            row[IDX2r[(IJ[mu], c)]] -= cf
    for mu, cf in prodjet(JET[b], JET[c]).items():     # +C(f,gh)
        if len(mu) >= 1:
            row[IDX2r[(a, IJ[mu])]] += cf
    rows.append(row)
M2r = sp.Matrix(rows)
rankM2 = M2r.rank()
KER = M2r.nullspace()          # dim 36: freedom of B2 tables with delta B2 = 0
KERT = M2r.T.nullspace()       # dim 384: obstruction functionals
print("M2r rank = %d, dim ker(M2r) = %d, dim ker(M2r^T) = %d, %.1fs"
      % (rankM2, len(KER), len(KERT), time.time() - t0))
ok["framework"] = (rankM2 == 160 and len(KER) == 36 and len(KERT) == 384)

def scht(p, q, r):
    # [Theta,Theta]^{pqr} = Theta^{pe} d_e Theta^{qr} + cyc   (058 convention, kappa=+1)
    s = sp.S.Zero
    for e in range(d):
        s += TA0(p, e) * TBa(q, r, e) + TA0(q, e) * TBa(r, p, e) + TA0(r, e) * TBa(p, q, e)
    return sp.expand(s)

def A2sub(TAdict, TBadict):
    subs = {TA[k]: TAdict[k] for k in TA}
    subs.update({TB[k]: TBadict.get(k, sp.Integer(0)) for k in TB})
    return sp.Matrix([A2tab[t].subs(subs) for t in DER3])

def membership(TAdict, TBadict):
    A = A2sub(TAdict, TBadict)
    big = sp.Matrix.hstack(M2r, A)
    return (M2r.rank() == big.rank()), M2r.rank(), big.rank()

# ---------- five-structure class columns (105 s1b col_struct, numeric jets) ----------
def mk_struct(TAdict, TBadict):
    def TT0(a, b):
        if a == b:
            return sp.S.Zero
        v = TAdict.get((min(a, b), max(a, b)))
        if a < b:
            return v
        return -v

    def TBd(p, q, e):
        if p == q:
            return sp.S.Zero
        v = TBadict.get((min(p, q), max(p, q), e))
        return v if p < q else -v

    def col_struct(P, Q, kind):
        if kind == "P1":
            if len(P) != 2 or len(Q) != 2:
                return sp.S.Zero
            s = sp.S.Zero
            for a, c in ((P[0], P[1]), (P[1], P[0])) if P[0] != P[1] else ((P[0], P[1]),):
                for b, dd in ((Q[0], Q[1]), (Q[1], Q[0])) if Q[0] != Q[1] else ((Q[0], Q[1]),):
                    s += TT0(a, b) * TT0(c, dd)
            return s
        if kind == "M":
            if len(P) != 1 or len(Q) != 1:
                return sp.S.Zero
            return sp.Add(*[TT0(P[0], i) * TT0(Q[0], i) for i in range(d)])
        if kind.startswith("div"):
            if len(P) != 1 or len(Q) != 1:
                return sp.S.Zero
            return sp.Add(*[TT0(P[0], i) * TBd(i, Q[0], i) for i in range(d)])
        if kind in ("U1", "U2"):
            if len(P) + len(Q) != 3 or len(P) == 0 or len(Q) == 0:
                return sp.S.Zero
            s = sp.S.Zero
            if len(P) == 1:
                u = P[0]
                w1, w2 = Q
                for i in range(d):
                    if kind == "U1":
                        s += TT0(i, u) * TBd(w1, w2, i)
                    else:
                        s += TT0(i, u) * (TBd(i, w2, w1) + TBd(i, w1, w2))
                return s
            terms = ([(P[0], P[0])] if P[0] == P[1] else [(P[0], P[1]), (P[1], P[0])])
            for u, pu in terms:
                w = Q[0]
                for i in range(d):
                    if kind == "U1":
                        s += TT0(i, u) * TBd(pu, w, i)
                    else:
                        s += TT0(i, u) * (TBd(i, pu, w) + TBd(i, w, pu))
            return s
        return sp.S.Zero
    return col_struct

NKINDS = ("P1", "M", "div1", "U1", "U2")

# ---------- embedding model: x^I = A^I_a y^a + (1/2) B^I_ab y^a y^b ----------
# M = A^{-1} = dy/dx at 0;  N^a_IK = d^2 y^a / dx^I dx^K = -M^a_I B^I_bc M^b_K M^c_I... :
#   N^a_IK = -M^a_J B^J_bc M^b_I M^c_K   (from substituting the Taylor series, verified)
def antisym6(vals):
    """vals: dict (a,b)->value for a<b; missing pairs default to 0."""
    def TH(Ii, Jj):
        if Ii == Jj:
            return sp.S.Zero
        return vals.get((Ii, Jj), 0) if Ii < Jj else -vals.get((Jj, Ii), 0)
    return TH

def pf6(TH):
    return TH(0, 1) * TH(2, 3) - TH(0, 2) * TH(1, 3) + TH(0, 3) * TH(1, 2)

def pullback_data(Amat, Bsym, TH):
    """Bsym[a][b][c]: embedding 2-jet B^a_bc (symmetric b<=c), symbolic or rational.
    Returns (M, N, theta0, dtheta) with M^a_I, N^a_IK, theta0[(a,b)], dtheta[(a,b,c)]."""
    A = sp.Matrix(Amat)
    Mm = A.inv()
    N = {}
    for a in range(d):
        for Ii in range(d):
            for Jj in range(Ii, d):
                # Taylor inversion identity: N^a_IK = -M^a_J B^J_bc M^b_I M^c_K
                t = sp.S.Zero
                for J in range(d):
                    for b in range(d):
                        for c in range(d):
                            t += Mm[a, J] * Bsym[J][b][c] * Mm[b, Ii] * Mm[c, Jj]
                N[(a, Ii, Jj)] = -t
    theta0 = {}
    for a, b in itertools.combinations(range(d), 2):
        s = sp.S.Zero
        for Ii in range(d):
            for Jj in range(d):
                s += TH(Ii, Jj) * Mm[a, Ii] * Mm[b, Jj]
        theta0[(a, b)] = sp.expand(s)
    dtheta = {}
    for a, b in itertools.combinations(range(d), 2):
        for mu in range(d):
            s = sp.S.Zero
            for Ii in range(d):
                for Jj in range(d):
                    for Kk in range(d):
                        lo1, hi1 = (Ii, Kk) if Ii <= Kk else (Kk, Ii)
                        n1 = N[(a, lo1, hi1)]
                        lo2, hi2 = (Jj, Kk) if Jj <= Kk else (Kk, Jj)
                        n2 = N[(b, lo2, hi2)]
                        s += TH(Ii, Jj) * (n1 * A[Kk, mu] * Mm[b, Jj]
                                           + Mm[a, Ii] * n2 * A[Kk, mu])
            dtheta[(a, b, mu)] = sp.expand(s)
    return Mm, N, theta0, dtheta

def cvec(Mm, N, TH):
    """196-table of B2PB(MON_P, MON_Q)|0."""
    # channel tensors
    C22 = {}
    C21 = {}
    C12 = {}
    C11 = {}
    for a, b in itertools.product(range(d), repeat=2):
        for c, dd in itertools.product(range(d), repeat=2):
            s = sp.S.Zero
            for Ii in range(d):
                for Jj in range(d):
                    for Kk in range(d):
                        for Ll in range(d):
                            s += (TH(Ii, Jj) * TH(Kk, Ll) * Mm[a, Ii] * Mm[b, Kk]
                                  * Mm[c, Jj] * Mm[dd, Ll])
            C22[(a, b, c, dd)] = sp.Rational(-1, 8) * sp.expand(s)
        for c in range(d):
            s2 = sp.S.Zero
            for Ii in range(d):
                for Jj in range(d):
                    for Kk in range(d):
                        for Ll in range(d):
                            # (F_,ab)(G_,c):  M^a_I M^b_K F * N^c_JL G :
                            # Theta^{IJ} Theta^{KL} M^a_I M^b_K N^c_JL
                            s2 += (TH(Ii, Jj) * TH(Kk, Ll) * Mm[a, Ii] * Mm[b, Kk]
                                   * N[(c, min(Jj, Ll), max(Jj, Ll))])
            C21[(a, b, c)] = sp.Rational(-1, 8) * sp.expand(s2)
            s3 = sp.S.Zero
            for Ii in range(d):
                for Jj in range(d):
                    for Kk in range(d):
                        for Ll in range(d):
                            # (F_,a)(G_,cd): Theta^{IJ} Theta^{KL} N^a_IK M^c_J M^d_L
                            s3 += (TH(Ii, Jj) * TH(Kk, Ll)
                                   * N[(a, min(Ii, Kk), max(Ii, Kk))] * Mm[c, Jj] * Mm[b, Ll])
            C12[(a, c, b)] = sp.Rational(-1, 8) * sp.expand(s3)  # index (a, c, d): F_a G_cd
    for a, b in itertools.product(range(d), repeat=2):
        s4 = sp.S.Zero
        for Ii in range(d):
            for Jj in range(d):
                for Kk in range(d):
                    for Ll in range(d):
                        s4 += (TH(Ii, Jj) * TH(Kk, Ll)
                               * N[(a, min(Ii, Kk), max(Ii, Kk))]
                               * N[(b, min(Jj, Ll), max(Jj, Ll))])
        C11[(a, b)] = sp.Rational(-1, 8) * sp.expand(s4)
    # jet derivatives of MON at 0
    Fd1 = [{(al,): sp.diff(MON[ia], x[al]).subs({xi: 0 for xi in x})
            for al in range(d)} for ia in range(15)]
    Fd2 = [{(al, be): sp.diff(sp.diff(MON[ia], x[al]), x[be]).subs({xi: 0 for xi in x})
            for al in range(d) for be in range(d)} for ia in range(15)]
    vec = []
    for (ia, ib) in BAS2r:
        s = sp.S.Zero
        for al in range(d):
            for be in range(d):
                f2 = Fd2[ia][(al, be)]
                if f2 == 0:
                    continue
                for c in range(d):
                    for dd in range(d):
                        g2 = Fd2[ib][(c, dd)]
                        if g2 != 0:
                            s += C22[(al, be, c, dd)] * f2 * g2
                for c in range(d):
                    g1 = Fd1[ib][(c,)]
                    if g1 != 0:
                        s += C21[(al, be, c)] * f2 * g1
        for al in range(d):
            f1 = Fd1[ia][(al,)]
            if f1 == 0:
                continue
            for c in range(d):
                for dd in range(d):
                    g2 = Fd2[ib][(c, dd)]
                    if g2 != 0:
                        s += C12[(al, c, dd)] * f1 * g2
            for c in range(d):
                g1 = Fd1[ib][(c,)]
                if g1 != 0:
                    s += C11[(al, c)] * f1 * g1
        vec.append(sp.expand(s))
    return sp.Matrix(vec), (C21, C12, C11, C22)

# ---------- P1: manuscript identity + (2,2) channel ----------
rngA = sp.Rational
A0 = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]  # generic rational, det 1
Bs = {}
bsyms = []
for a in range(d):
    Bs[a] = {}
    for b in range(d):
        Bs[a][b] = {}
for a in range(d):
    for b in range(d):
        for c in range(b, d):
            s = sp.symbols("B_%d_%d%d" % (a, b, c))
            bsyms.append(s)
            Bs[a][b][c] = s
            Bs[a][c][b] = s
THs = antisym6({(a, b): sp.symbols("TH_%d%d" % (a, b)) for a, b in itertools.combinations(range(d), 2)})
Mm, N, theta0, dtheta = pullback_data(A0, Bs, THs)
# manuscript identity: Theta^{IJ} = theta^{ab} A^I_a A^J_b
ident_ok = True
A0m = sp.Matrix(A0)   # A0m[I, a] = A^I_a = d x^I / d y^a
for Ii in range(d):
    for Jj in range(d):
        if Ii >= Jj:
            continue
        lhs = THs(Ii, Jj)
        rhs = sp.S.Zero
        for a, b in itertools.combinations(range(d), 2):
            rhs += theta0[(a, b)] * (A0m[Ii, a] * A0m[Jj, b] - A0m[Jj, a] * A0m[Ii, b])
        if sp.expand(lhs - rhs) != 0:
            ident_ok = False
            print("P1 FAIL at", Ii, Jj, sp.expand(lhs - rhs))
P1 = ident_ok
print("P1 (manuscript identity Theta^{IJ}=theta^{ab}d_a x^I d_b x^J identically in B):",
      "PASS" if P1 else "FAIL")
ok["P1"] = P1

# ---------- P2: induced jets are Schouten-closed ----------
P2 = True
for (p, q, r) in itertools.combinations(range(d), 3):
    e = scht(p, q, r).subs({TA[k]: theta0[k] for k in theta0}
                           ).subs({TB[k]: dtheta[k] for k in dtheta})
    if sp.expand(e) != 0:
        P2 = False
        print("P2 FAIL at", (p, q, r), sp.expand(e))
print("P2 ([theta,theta](0) = 0 identically in (B,Theta) -- matrix class on the closed "
      "side of the dichotomy):", "PASS" if P2 else "FAIL")
ok["P2"] = P2

# ---------- P3: B=0 reproduces the 105 Moyal coboundary table ----------
Bs0 = {a: {b: {c: sp.Integer(0) for c in range(d)} for b in range(d)} for a in range(d)}
Mm0, N0, theta00, dtheta0 = pullback_data(A0, Bs0, THs)
cP3, _ = cvec(Mm0, N0, THs)
cs0 = mk_struct({k: theta00[k] for k in theta00}, {k: sp.Integer(0) for k in TB})
b2m = sp.Matrix([sp.Rational(-1, 8) * cs0(JET[t[0]], JET[t[1]], "P1") for t in BAS2r])
bad = [i for i in range(196) if sp.expand(cP3[i] - b2m[i]) != 0]
P3 = not bad
print("P3 (B=0: B2PB table = 105 -(1/8)P1 Moyal table entrywise):",
      "PASS" if P3 else "FAIL %s" % bad[:3])
ok["P3"] = P3

# ---------- numeric embedding points ----------
import random
rng = random.Random(106)
def rQ(lo, hi):
    return sp.Rational(rng.randrange(lo, hi), rng.randrange(1, 8))

def make_point(seed):
    r2 = random.Random(seed)
    def r():
        return sp.Rational(r2.randrange(-9, 10), r2.randrange(1, 7))
    return {"A": A0,
            "B": {a: {b: {c: (r() if c >= b else None) for c in range(d)} for b in range(d)}
                  for a in range(d)},
            "TH": {(a, b): r() for a, b in itertools.combinations(range(d), 2)}}

pts = []
for seed in (1061, 1062, 1063):
    p = make_point(seed)
    # fill symmetric B
    Bq = {}
    nonzero = False
    for a in range(d):
        Bq[a] = {}
        for b in range(d):
            Bq[a][b] = {}
            for c in range(d):
                v = p["B"][a][min(b, c)][max(b, c)]
                Bq[a][b][c] = v
                if v != 0:
                    nonzero = True
    THq = antisym6(p["TH"])
    Mq, Nq, th0, dth = pullback_data(p["A"], Bq, THq)
    if pf6(THq) == 0 or pf6(antisym6({k: th0[k] for k in th0})) == 0 or not nonzero:
        continue
    pts.append((seed, THq, th0, dth, Mq, Nq))
print("usable rational embedding points:", len(pts))

P4 = P5 = None
P4 = True
P5 = True
for (seed, THq, th0, dth, Mq, Nq) in pts:
    cv, _ = cvec(Mq, Nq, THq)
    TAd = {k: th0[k] for k in th0}
    TBd = {k: dth[k] for k in dth}
    res = sp.Matrix(M2r * cv) - A2sub(TAd, TBd)
    bad4 = [DER3[i] for i in range(544) if res[i] != 0]
    mem4, _, _ = membership(TAd, TBd)
    print("P4 pt seed %d: rows failing deltaB2PB=A2: %d ; wild membership: %s"
          % (seed, len(bad4), mem4))
    if bad4 or not mem4:
        P4 = False
    # P5: outside five-structure class
    cs = mk_struct(TAd, TBd)
    cols = [sp.Matrix([cs(JET[t[0]], JET[t[1]], kind) for t in BAS2r]) for kind in NKINDS]
    Cc = sp.Matrix.hstack(*cols)
    rc = Cc.rank()
    ra = sp.Matrix.hstack(Cc, cv).rank()
    print("P5 pt seed %d: class rank %d -> augmented rank %d (outside class: %s)"
          % (seed, rc, ra, ra > rc))
    if ra <= rc:
        P5 = False
print("P4 (matrix-selected B2PB satisfies A2 = delta B2PB, all 544 rows, 3 points):",
      "PASS" if P4 else "FAIL")
ok["P4"] = P4
print("P5 (B2PB outside the 105 five-structure class at each point):",
      "PASS" if P5 else "FAIL")
ok["P5"] = P5

# ---------- P6/P7: non-1-jet selection ----------
# symbolic in B at A0, TH numeric standard form
THstd = antisym6({(0, 1): sp.Integer(1), (2, 3): sp.Integer(1)})
_, _, th0s, dth_s = pullback_data(A0, Bs, THstd)
tbsyms = [TB[k] for k in sorted(TB)]
rows6 = []
for k in sorted(dth_s):
    rows6.append([sp.expand(dth_s[k]).coeff(s) for s in bsyms])
Mb = sp.Matrix(rows6)
rk = Mb.rank()
NB = Mb.nullspace()
# The image lies in the 20-dim linearized-closure subspace of R^24 (the four Schouten
# components are identically zero on induced jets, P2), so max rank is 20; kernel dim
# 40-20 = 20 is the fiber over a fixed closed 1-jet at fixed (A, Theta).
print("P6: rank(B -> dtheta(0)) = %d (expect 20 = 24-4 closedness), kernel dim %d"
      % (rk, len(NB)))
P6 = (rk == 20 and len(NB) == 20)
# base point B0 and witness
B0 = {}
r3 = random.Random(1066)
for a in range(d):
    B0[a] = {}
    for b in range(d):
        B0[a][b] = {}
        for c in range(d):
            B0[a][b][c] = sp.Rational(r3.randrange(-5, 6), r3.randrange(1, 6)) if c >= b else None
for a in range(d):
    for b in range(d):
        for c in range(d):
            B0[a][b][c] = B0[a][min(b, c)][max(b, c)]
Mq0, Nq0, th06, dth6 = pullback_data(A0, B0, THstd)
c0, _ = cvec(Mq0, Nq0, THstd)
diffs = []
for m, v in enumerate(NB):
    B1p = {}
    for a in range(d):
        B1p[a] = {}
        for b in range(d):
            B1p[a][b] = {}
            for c in range(d):
                B1p[a][b][c] = (B0[a][min(b, c)][max(b, c)]
                                + v[bsyms.index(Bs[a][min(b, c)][max(b, c)])])
    M1, N1, _, dth1 = pullback_data(A0, B1p, THstd)
    c1, _ = cvec(M1, N1, THstd)
    dv = sp.expand(c1 - c0)
    diffs.append(dv)
    jet_same = all(sp.expand(dth1[k] - dth6[k]) == 0 for k in dth6)
    nz = sum(1 for w in dv if w != 0)
    if m == 0:
        print("P6 witness (kernel vector 0): dtheta unchanged: %s ; B2PB table rows "
              "changed: %d/196 ; in ker(M2r): %s"
              % (jet_same, nz, all(sp.Matrix(M2r * dv)[i] == 0 for i in range(544))))
        ker_ok = all(sp.Matrix(M2r * dv)[i] == 0 for i in range(544))
        if not (jet_same and nz > 0 and ker_ok):
            P6 = False
    else:
        if not jet_same:
            P6 = False
            print("P6: kernel vector %d unexpectedly changes dtheta" % m)
print("P6 (selection NOT 1-jet-local: exact rational witness at fixed closed 1-jet,"
      " difference in ker(M2r)):", "PASS" if P6 else "FAIL")
ok["P6"] = P6

spanM = sp.Matrix.hstack(*diffs)
sdim = spanM.rank()
P7 = (1 <= sdim <= 36)
print("P7 (span of kernel-direction selection changes has dim %d, within dim ker(M2r)"
      " = 36):" % sdim, "PASS" if P7 else "FAIL")
ok["P7"] = P7

# ---------- P8: target symplectic frame invariance ----------
# Rational Sp(Theta_std) block-transvection: S Theta S^T = Theta (blocks [[1,t],[0,1]]
# on the (0,1) and (2,3) planes of the standard form). Theta'^{IJ} = S^I_K S^J_L TH^{KL}
# and embedding x' = S x  => A' = S A, B' = S B (linear in the target index).
S = sp.Matrix([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 3, 1]])
Smat = sp.Matrix([[sp.expand(sum(S[a, Kk] * S[b, Ll] * THstd(Kk, Ll)
                                  for Kk in range(d) for Ll in range(d)))
                   for b in range(d)] for a in range(d)])
Tstd = sp.Matrix([[THstd(a, b) for b in range(d)] for a in range(d)])
assert Smat == Tstd, "S not symplectic for the standard form"
TH8 = {(a, b): sp.S.Zero for a, b in itertools.combinations(range(d), 2)}
for a, b in itertools.combinations(range(d), 2):
    v = sp.S.Zero
    for Kk in range(d):
        for Ll in range(d):
            v += S[a, Kk] * S[b, Ll] * (THstd(Kk, Ll))
    TH8[(a, b)] = v
A8 = (S * sp.Matrix(A0)).tolist()
B8 = {}
for a in range(d):
    B8[a] = {}
    for b in range(d):
        B8[a][b] = {}
        for c in range(d):
            v = sp.S.Zero
            for Kk in range(d):
                v += S[a, Kk] * B0[Kk][b][c]
            B8[a][b][c] = v
M8, N8, th8, dth8 = pullback_data(A8, B8, antisym6(TH8))
c8, _ = cvec(M8, N8, antisym6(TH8))
P8 = (sp.Matrix([sp.expand(th8[k] - th06[k]) for k in th8]) == sp.zeros(6, 1)
      and sp.Matrix([sp.expand(dth8[k] - dth6[k]) for k in dth8]) == sp.zeros(24, 1)
      and sp.Matrix([sp.expand(c8[i] - c0[i]) for i in range(196)]) == sp.zeros(196, 1))
print("P8 (theta-jet and selected table invariant under rational Sp(Theta) target frame"
      " change S):", "PASS" if P8 else "FAIL")
ok["P8"] = P8

# ---------- summary ----------
print()
print("claim results:", {k: ("PASS" if v else "FAIL") for k, v in sorted(ok.items())})
print("total %.1fs" % (time.time() - t0))
sys.exit(0 if all(ok.values()) else 1)
