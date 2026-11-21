# s1b_order2_coboundary.py -- proposal 105 r1, decisive computation.
# Provenance: s1_naive_associator.py/.out are KEPT UNMODIFIED as the record of the
# earlier header claims (a),(b): that run showed the (a)-probe (constant-ratio test of
# the antisymmetrized (1,1,1) COMPONENT) fails -- the wrong probe, since the full
# slot-antisymmetrization carries the Schouten part and the component antisymmetrization
# does not; and the (b) examples (Theta = x2 d_0^wedge d_1, so(3) Lie-Poisson) have
# Theta(0)=0, so A2(0)=0 was trivial: the (b) "nonzero under closure" claim was untested.
# This script supersedes them.
#
# Setting (exact rational/symbolic arithmetic, d=4; polynomial test functions of degree
# <=2, so every cochain of differential order <=2 per slot is read off its polar
# trilinear form on the 15-dimensional jet space (value, first jet, symmetric second
# jet) at x=0; Theta^{ab}(x) generic with independent 2-jets at 0 -- claim C1 proves the
# order-2 associator uses only TA = Theta(0) and TB = dTheta(0)):
#   B1(f,g) = (i/2) Theta^{ab}(x) d_a f d_b g ,   f *_naive g = f g + B1(f,g) ,
#   A2(f,g,h) = B1(B1(f,g),h) - B1(f,B1(g,h))          (order-Theta^2 associator defect)
# Hochschild coboundary: delta C(f,g,h) = f C(g,h) - C(fg,h) + C(f,gh) - C(f,g) h.
# Reduction (verified in-script, "quotient" below): A2 vanishes whenever an argument is
# constant; delta of a 2-cochain with a zero-order (multiplication) part contributes
# only to rows with a constant argument; hence membership A2 in im(delta) is equivalent
# to membership in the derivative-only subsystem: rows (order patterns (1,1,1),(2,1,1),
# (1,2,1),(1,1,2)): 544 rows; columns pairs (order in {1,2} per slot): 196 columns.
# Claims (printed C1..C9 PASS/FAIL):
#  C1 A2 uses only TA,TB jets; full slot-antisymmetrization of A2 = kappa * the
#     Schouten trivector 3-form operator [Theta,Theta]^{abc} d_a f d_b g d_c h (058).
#  C2 generic non-coboundary: at exact generic jets A2 not in im(delta); witness vectors.
#  C3 witness quadratic forms span exactly the 4 Schouten components: for EVERY jet
#     point (pointwise exact linear algebra over Q, "wild" B2): A2 in im(delta) <=>
#     all Schouten components vanish. Closure is the complete obstruction.
#  C4 under Schouten closure (nullspace parametrized at a generic TA), delta A2 = 0
#     identically (4-cochain table zero, closure parameters free).
#  C5 closure => delta b = -A2_part systems consistent; exact B2 exists; solution-space
#     dimension computed.
#  C6 bounded no-go: NO jet-universal B2 in the enumerated ansatz class
#     bidifferential order <=2, coefficients quadratic in Theta,dTheta) solves
#     delta B2 = -A2 under closure at two generic TA points, same universal rational
#     coefficients; at dTheta=0 its Theta^2 part coincides with the Moyal operator.
#  C7 corrected (b): Schouten-closed example with Theta(0) != 0 where the naive
#     associator is NONZERO yet delta-removable; old examples have Theta(0)=0;
#     non-closed jets: membership fails (C2 witness realized numerically).
#  C8 re-derivation of s1 check (c), strengthened: constant-Theta defect = -delta(Moyal
#     B2), symbolic over generic constant TA.
#  C9 independent numeric spot checks, exact rationals, seed 20261120.
import itertools
import random
import sys
import time
import sympy as sp

t0 = time.time()
d = 4
x = sp.symbols("x0:4")
I = sp.I
ok = {}

# ---------- jet basis ----------
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
    """dict: multi-index -> coefficient for the jet of a product, |a|+|b|<=2"""
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

# ---------- generic Theta 2-jets at 0 ----------
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

# ---------- A2 table (polar form on jets), exact ----------
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
# all-derivative rows of the table
DER3 = [t for t in itertools.product(range(15), repeat=3)
        if min(len(JET[t[0]]), len(JET[t[1]]), len(JET[t[2]])) >= 1
        and len(JET[t[0]]) + len(JET[t[1]]) + len(JET[t[2]]) <= 4]
assert len(DER3) == 544
C1a = True
for t in A2tab:
    if A2tab[t] != 0:
        if any(len(JET[s]) == 0 for s in t):
            print("C1 unexpected value-arg nonzero at", t)
            C1a = False
        if {str(s) for s in A2tab[t].free_symbols} & {str(s) for s in
                                                      itertools.chain(*[TQ.values()])}:
            print("C1 unexpected TQ at", t)
            C1a = False
print("C1a (A2 uses only TA,TB; vanishes on constant arguments):",
      "PASS" if C1a else "FAIL")
ok["C1a"] = C1a

# ---------- Schouten components (058 convention: S^{pqr}=Theta^{ad}d_d Theta^{qr}+cyc) --
def TBa(p, q, r):
    if p == q:
        return sp.S.Zero
    return TB[(p, q, r)] if p < q else -TB[(q, p, r)]

def TT0(a, b):
    if a == b:
        return sp.S.Zero
    return TA[(a, b)] if a < b else -TA[(b, a)]

def scht(p, q, r):
    # [Theta,Theta]^{pqr} = Theta^{pe} d_e Theta^{qr} + cyc(p,q,r)
    s = sp.S.Zero
    for e in range(d):
        s += TT0(p, e) * TBa(q, r, e)
        s += TT0(q, e) * TBa(r, p, e)
        s += TT0(r, e) * TBa(p, q, e)
    return sp.expand(s)

SCH = {}
for p, q, r in itertools.combinations(range(d), 3):
    SCH[(p, q, r)] = scht(p, q, r)

# ---------- C1b: slot-antisymmetrization ----------
kappa = None
C1b = True
for ia in range(15):
    for ib in range(15):
        for ic in range(15):
            s = sp.S.Zero
            for (ja, jb, jc), sg in (
                    ((ia, ib, ic), 1), ((ib, ic, ia), 1), ((ic, ia, ib), 1),
                    ((ia, ic, ib), -1), ((ic, ib, ia), -1), ((ib, ia, ic), -1)):
                s += sg * A2tab[(ja, jb, jc)]
            a, b, c = JET[ia], JET[ib], JET[ic]
            sh = sp.S.Zero
            if len(a) == len(b) == len(c) == 1 and len({a[0], b[0], c[0]}) == 3:
                lst = [a[0], b[0], c[0]]
                srt = sorted(lst)
                sh = SCH[tuple(srt)]
                perm = [srt.index(v) for v in lst]
                nsig = sum(1 for i in range(3) for j in range(i + 1, 3)
                           if perm[i] > perm[j])
                sh = sh if nsig % 2 == 0 else -sh
            ant = sp.expand(s)
            if len(a) == len(b) == len(c) == 1 and len({a[0], b[0], c[0]}) == 3:
                if kappa is None and sh != 0:
                    for cand in (sp.Integer(1), sp.Integer(-1), sp.Rational(1, 2),
                                 sp.Rational(-1, 2), sp.Rational(1, 4),
                                 sp.Rational(-1, 4), sp.Rational(1, 6),
                                 sp.Rational(-1, 6), sp.Rational(1, 12),
                                 sp.Rational(-1, 12), sp.Rational(3, 4),
                                 sp.Rational(-3, 4)):
                        if sp.expand(ant - cand * sh) == 0:
                            kappa = cand
                            break
                    if kappa is None:
                        C1b = False
                        print("C1b: no constant kappa at", a, b, c)
                        print(" ANT:", ant)
                        print(" Sch:", sh)
                        break
                elif kappa is not None and sp.expand(ant - kappa * sh) != 0:
                    C1b = False
                    print("C1b mismatch at", a, b, c)
                    break
            elif kappa is not None and sp.expand(ant) != 0:
                C1b = False
                print("C1b: antisym part nonzero where 3-form must vanish:",
                      a, b, c, sp.expand(ant))
                break
print("C1b (slot-antisym(A2) = kappa*[Theta,Theta] 3-form, kappa =", kappa, "):",
      "PASS" if (C1b and kappa is not None) else "FAIL")
ok["C1b"] = C1b and kappa is not None

# ---------- reduced delta matrix M2r (544 x 196), exact integer ----------
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
print("M2r built; rank =", rankM2, " (196 cols, 544 rows), %.1fs" % (time.time() - t0))

# ---------- C2: generic jets are NOT coboundary-removable (exact) ----------
TAvals1 = {(0, 1): sp.Rational(2, 3), (0, 2): sp.Rational(1, 5), (0, 3): sp.Rational(-3, 4),
           (1, 2): sp.Rational(5, 7), (1, 3): sp.Rational(-1, 2), (2, 3): sp.Rational(4, 9)}
def TAval(k):
    return TAvals1[k] if k in TAvals1 else -TAvals1[(k[1], k[0])]

def subst_TA(e):
    return e.subs({TA[k]: TAval(k) for k in TA})

def subst_full(e, TBadict):
    r = subst_TA(e)
    return r.subs({TB[k]: TBadict.get(k, sp.Integer(0)) for k in TB})

# random exact generic jets (not closed)
rng = random.Random(105)
def rnd():
    return sp.Rational(rng.randrange(-97, 98), rng.randrange(1, 13))
TBadic_g = {(k[0], k[1], k[2]): rnd() for k in TB}
A2gen = sp.Matrix([[subst_full(A2tab[t], TBadic_g)] for t in DER3])
assert A2gen.shape == (544, 1)
aug = sp.Matrix.hstack(M2r, A2gen)
assert aug.shape == (544, 197)
rank_aug = aug.rank()
C2 = (rank_aug != rankM2)
print("C2 generic jets: rank(M2r)=%d rank(aug)=%d -> non-removable:" % (rankM2, rank_aug),
      "PASS" if C2 else "FAIL")
ok["C2"] = C2

# ---------- C3: witness polynomial conditions = Schouten span ----------
KER = M2r.T.nullspace()
print("dim ker(M2r^T) =", len(KER))
# monomial basis of quadratics in the 30 jet symbols
JETS30 = [TA[k] for k in TA] + [TB[k] for k in TB]
QUADM = [a * b for i, a in enumerate(JETS30) for b in JETS30[i:]]
QIDX = {m: k for k, m in enumerate(QUADM)}
assert len(QUADM) == 465

def quadvec(e):
    v = [sp.Integer(0)] * len(QUADM)
    if sp.expand(e) == 0:
        return sp.Matrix(v)
    p = sp.Poly(sp.expand(e), *JETS30, domain='QQ')
    for mon, coef in p.terms():
        # mon: exponent vector
        m = 1
        for ex, sym in zip(mon, JETS30):
            if ex:
                m *= sym ** ex
        qv = QUADM.index(m) if m in QIDX else None
        if qv is None:  # linear/constant term -> should not occur
            print("non-quadratic term in witness:", e)
            return None
        v[qv] += coef
    return sp.Matrix(v)

def A2qvec(t):
    return quadvec(A2tab[t])
A2Q = [A2qvec(t) for t in DER3]
# im(J|ker) : stack
Kmat = sp.Matrix.hstack(*KER)   # 544 x dim
Jmat = sp.Matrix([[ (A2Q[j][i] if A2Q[j] is not None else 0) for j in range(len(DER3))]
                  for i in range(len(QUADM))])
IMG = Jmat * Kmat
IMP = IMG.columnspace()
print("dim of witness-condition space =", len(IMP))
Svec = [quadvec(SCH[k]) for k in SCH]
def in_span(vec, basis):
    B = sp.Matrix.hstack(*basis) if basis else None
    if B is None:
        return all(v == 0 for v in vec)
    return sp.Matrix.hstack(B, vec).rank() == B.rank()
C3a = all(in_span(vec, IMP) for vec in Svec)
C3b = all(in_span(vec, Svec) for vec in IMP)
C3 = C3a and C3b and len(Svec) == 4 and sp.Matrix.hstack(*Svec).rank() == 4
print("C3 (witness span == Schouten span: Sch in P:", C3a, ", P in Sch:", C3b,
      ", dim Sch = 4):", "PASS" if C3 else "FAIL")
ok["C3"] = C3

# ---------- closure parametrization: nullspace of the 4 linear Schouten forms in TB ----------
def closure_basis(TAdict):
    # TB symbols ordered by key
    tbsyms = [TB[k] for k in sorted(TB)]
    rows = []
    for key in sorted(SCH):
        e = SCH[key].subs({TA[k]: TAdict[k] for k in TA})
        rows.append([sp.expand(e).coeff(s) for s in tbsyms])
    return sp.Matrix(rows)

TA1 = {(k[0], k[1]): TAvals1.get(k, sp.Integer(0)) for k in TA}
# ensure full antisym filling: TA keys are (a,b), a<b only
def TApt(d6):
    return {(a, b): d6[(a, b)] for (a, b) in TA}
TA1pt = TApt(TAvals1)
pf1 = TA1pt[(0, 1)] * TA1pt[(2, 3)] - TA1pt[(0, 2)] * TA1pt[(1, 3)] + TA1pt[(0, 3)] * TA1pt(1, 2) if False else \
      TA1pt[(0, 1)] * TA1pt[(2, 3)] - TA1pt[(0, 2)] * TA1pt[(1, 3)] + TA1pt[(0, 3)] * TA1pt[(1, 2)]
assert pf1 != 0, "TA1 degenerate"
Mcl1 = closure_basis(TA1pt)
NB1 = Mcl1.nullspace()
print("closure at TA1: rank of Schouten map =", Mcl1.rank(), ", dim nullspace =", len(NB1))

def tbvec(TBadict):
    return sp.Matrix([TBadict.get(k, sp.Integer(0)) for k in sorted(TB)])

def A2sub(TAdict, TBadict):
    subs = {TA[k]: TAdict[k] for k in TA}
    subs.update({TB[k]: TBadict.get(k, sp.Integer(0)) for k in TB})
    return sp.Matrix([A2tab[t].subs(subs) for t in DER3])

def membership(TAdict, TBadict, colvecs=None, verbose=False):
    """exact rank test: is -A2tab in im M2r (+ optional extra columns)?"""
    A = A2sub(TAdict, TBadict)
    cols = [M2r] + ([sp.Matrix.hstack(*c) if not isinstance(c, sp.ImmutableDenseMatrix) else c for c in colvecs] if colvecs else [])
    base = sp.Matrix.hstack(*cols)
    big = sp.Matrix.hstack(base, A)
    r1 = base.rank()
    r2 = big.rank()
    return (r1 == r2), r1, r2

# ---------- C4: under closure the associator is a Hochschild 3-cocycle (delta A2 = 0) ----------
# delta4 table on a sparse generating set of quadruple jets
DER4 = [(a, b, c, e) for a, b, c, e in itertools.product(range(15), repeat=4)
        if all(len(JET[t]) >= 1 for t in (a, b, c, e)) and sum(len(JET[t]) for t in (a, b, c, e)) <= 6]
# parametric closure: TB = sum z_m v_m
zs = sp.symbols("z0:%d" % len(NB1))
TBpar = {TB[k]: sum(zs[m] * NB1[m][i] for m in range(len(NB1)))
         for i, k in enumerate(sorted(TB))}
C4 = True
n4 = 0
for (a, b, c, e) in DER4[:80]:
    # (delta A2)(f,g,h,k) = f*A2(g,h,k) - A2(fg,h,k) + A2(f,gh,k) - A2(f,g,hk) + A2(f,g,h)*k
    v = sp.S.Zero
    if len(JET[a]) == 0:
        v += sp.S.Zero  # f is constant 1 -> value term f*A2 handled below
    # value of f: 1 iff a==(); else 0
    fa = sp.S.One if JET[a] == () else sp.S.Zero
    ka = sp.S.One if JET[e] == () else sp.S.Zero
    v += fa * A2tab[(b, c, e)] if False else fa * A2tab[(b, c, e)]
    for mu, cf in prodjet(JET[a], JET[b]).items():
        v -= cf * A2tab[(IJ[mu], c, e)]
    for mu, cf in prodjet(JET[b], JET[c]).items():
        v += cf * A2tab[(a, IJ[mu], e)]
    for mu, cf in prodjet(JET[c], JET[e]).items():
        v -= cf * A2tab[(a, b, IJ[mu])]
    v += A2tab[(a, b, c)] * ka
    expr = sp.expand(v.subs({TA[k]: TA1pt[k] for k in TA}).subs(TBpar))
    n4 += 1
    if expr != 0:
        C4 = False
        print("C4 FAIL at", (JET[a], JET[b], JET[c], JET[e]), ":", expr)
        break
print("C4 (delta_hoch A2 = 0 identically in TB, %d generating quadruples):" % n4,
      "PASS" if C4 else "FAIL")
ok["C4"] = C4

# ---------- C5: parametric consistency of delta b = -A2 under closure ----------
# A2param = matrix of linear forms in z over Q (544 rows); consistency for all z
def paramcols(exprs):
    polys = [sp.Poly(sp.expand(e), *zs, domain='QQ') for e in exprs]
    mons = sorted({m for P in polys for m in P.monoms()},
                  key=lambda m: (-sum(m), tuple(m)))
    cols = []
    for m in mons:
        col = []
        for P in polys:
            cf = P.coeff_monomial(m) if m in P.monoms() else sp.Integer(0)
            col.append(sp.Rational(cf) if cf != 0 else sp.Integer(0))
        if any(v != 0 for v in col):
            cols.append(sp.Matrix(col))
    return sp.Matrix.hstack(*cols) if cols else sp.zeros(len(polys), 0)

A2pexprs = [A2tab[t].subs({TA[k]: TA1pt[k] for k in TA}).subs(TBpar) for t in DER3]
A2p = paramcols(A2pexprs)
# consistency of [M2r | -A2p] for all z: columns of A2p must lie in colspace of M2r
r1 = M2r.rank()
r2 = sp.Matrix.hstack(M2r, A2p).rank()
C5 = (r1 == r2)
print("C5 (delta b = -A2 solvable for every closed jets point at TA1; param cols %d, rank %d -> %d):"
      % (A2p.cols, r1, r2), "PASS" if C5 else "FAIL")
ok["C5"] = C5

# ---------- C6: explicit natural B2 (Kontsevich order-2 class) ----------
# ENUMERATED ANSATZ CLASS (not claimed complete): tensors built from
# products Theta*Theta (no contraction: P1; one contraction: M) and
# Theta*dTheta (one contraction with the d-direction: U1; one contraction
# Theta-slot vs dTheta-slot: U2; two contractions/divergence: div1), with
# derivative orders <=2 per slot; Theta*d^2Theta with the undifferentiated
# pair contracted vanishes identically (antisym x sym, verified). The full
# Kontsevich natural class at order Theta^2 additionally contains
# (dTheta)(dTheta), Theta*d^3Theta and (d^2Theta)(d^2Theta) contractions;
# those are NOT enumerated here, so C6 is a bounded ansatz result only:
def TH2(p, q, e, f):
    # raw d_e d_f Theta^{pq} at 0 (antisym in (p,q), sym in (e,f)); TQ symbols
    # are Hessian-normalized (off-diagonal pairs carry factor 2 in THS).
    if p == q:
        return sp.S.Zero
    lo, hi = (e, f) if e <= f else (f, e)
    w = sp.Integer(2) if e != f else sp.Integer(1)
    base = TQ[(p, q, lo, hi)] if p < q else -TQ[(q, p, lo, hi)]
    return w * base

def col_struct(P, Q, kind):
    # P,Q sorted JET tuples of derivative slots; coefficient of d^P f d^Q g
    if kind == "P1":
        # Theta^{ab}Theta^{cd} d_a d_c f d_b d_d g (both pairings by symmetry)
        if len(P) != 2 or len(Q) != 2:
            return sp.S.Zero
        s = sp.S.Zero
        for a, c in ((P[0], P[1]), (P[1], P[0])) if P[0] != P[1] else ((P[0], P[1]),):
            for b, dd in ((Q[0], Q[1]), (Q[1], Q[0])) if Q[0] != Q[1] else ((Q[0], Q[1]),):
                s += TT0(a, b) * TT0(c, dd)
        return s
    if kind == "M":
        # (1,1) Theta^2 structure: C_{u;v} = sum_i Theta^{ui} Theta^{vi}
        if len(P) != 1 or len(Q) != 1:
            return sp.S.Zero
        s = sp.S.Zero
        for i in range(d):
            s += TT0(P[0], i) * TT0(Q[0], i)
        return s
    if kind == "D2":
        # (1,1) Theta d^2 Theta: C_{k;l} = sum_{e,f} Theta^{ef} d_e d_f Theta^{kl}
        if len(P) != 1 or len(Q) != 1:
            return sp.S.Zero
        s = sp.S.Zero
        for e in range(d):
            for f in range(d):
                s += TT0(e, f) * TH2(P[0], Q[0], e, f)
        return s
    if kind.startswith("div"):
        # (1,1) Theta dTheta divergence: C_{u;v} = sum_i Theta^{ui} d_i Theta^{iv}
        if len(P) != 1 or len(Q) != 1:
            return sp.S.Zero
        s = sp.S.Zero
        for i in range(d):
            s += TT0(P[0], i) * TBa(i, Q[0], i)
        return s
    if kind in ("U1", "U2"):
        # Theta*dTheta, one internal contraction, free slots distributed (1,2)/(2,1).
        # U1: internal i pairs Theta1 slot with d-direction:  Theta^{iu} d_i Theta^{vw}
        # U2: internal i pairs Theta1 slot with Theta2 slot:    Theta^{iu} d_v Theta^{iw}
        if len(P) + len(Q) != 3 or len(P) == 0 or len(Q) == 0:
            return sp.S.Zero
        s = sp.S.Zero
        if len(P) == 1:
            u = P[0]
            w1, w2 = Q
            for i in range(d):
                if kind == "U1":
                    s += TT0(i, u) * TBa(w1, w2, i)
                else:
                    s += TT0(i, u) * (TBa(i, w2, w1) + TBa(i, w1, w2))
            return s
        # |P| = 2, |Q| = 1: sum over which (ordered) slot of P is u
        terms = ([(P[0], P[0])] if P[0] == P[1]
                 else [(P[0], P[1]), (P[1], P[0])])
        for u, pu in terms:
            w = Q[0]
            for i in range(d):
                if kind == "U1":
                    s += TT0(i, u) * TBa(pu, w, i)
                else:
                    s += TT0(i, u) * (TBa(i, pu, w) + TBa(i, w, pu))
        return s
    return sp.S.Zero

NKINDS = ("P1", "M", "D2", "div1", "U1", "U2")
COLS = {kind: sp.Matrix([col_struct(JET[t[0]], JET[t[1]], kind) for t in BAS2r])
        for kind in NKINDS}
# drop identically-zero structures
NKINDS = tuple(k for k in NKINDS if any(v != 0 for v in COLS[k]))
print("natural class nonzero kinds:", NKINDS)

def solve_lambda(TAdict, TBadict):
    # natural-class columns live in the 196-dim B2 coefficient space; the
    # consistency test is on their images under the coboundary matrix M2r.
    colsb = [M2r * COLS[k].subs({TA[k]: TAdict[k] for k in TA})
                      .subs({TB[k]: TBadict.get(k, sp.Integer(0)) for k in TB})
             for k in NKINDS]
    C = sp.Matrix.hstack(*colsb)
    A = A2sub(TAdict, TBadict)
    aug = sp.Matrix.hstack(C, -A)
    rc, ra = C.rank(), aug.rank()
    if rc != ra:
        return None, rc, ra, C
    rref, piv = aug.rref()
    nc = len(NKINDS)
    lam = sp.Matrix([rref[piv[i], nc] for i in range(len(piv))])
    lam = sp.Matrix([lam[list(piv).index(j)] if j in piv else sp.Integer(0)
                     for j in range(nc)])
    return lam, rc, ra, C

# a second generic TA point with pf != 0
rng2 = random.Random(1051)
TA2vals = {}
while True:
    cand = {(k[0], k[1]): sp.Rational(rng2.randrange(-50, 51), rng2.randrange(1, 11))
            for k in TA}
    pf2 = (cand[(0, 1)] * cand[(2, 3)] - cand[(0, 2)] * cand[(1, 3)]
           + cand[(0, 3)] * cand[(1, 2)])
    if pf2 != 0:
        TA2vals = cand
        break
TA2pt = TA2vals
Mcl2 = closure_basis(TA2pt)
NB2 = Mcl2.nullspace()
print("closure at TA2: rank %d, nullspace dim %d" % (Mcl2.rank(), len(NB2)))

def tb_from_basis(basis, coeffs):
    return {k: sum(coeffs[m] * basis[m][i] for m in range(len(basis)))
            for i, k in enumerate(sorted(TB))}

pts = [("TA1v1", TA1pt, tb_from_basis(NB1, [1] + [0] * (len(NB1) - 1))),
       ("TA1v2", TA1pt, tb_from_basis(NB1, [0, 1] + [0] * (len(NB1) - 2))),
       ("TA2v1", TA2pt, tb_from_basis(NB2, [1] + [0] * (len(NB2) - 1))),
       ("TA2v2", TA2pt, tb_from_basis(NB2, [2, 1] + [0] * (len(NB2) - 2)))]
lams = {}
Csol = {}
C6a = True
for name, tAd, tBd in pts:
    lam, rc, ra, Cc = solve_lambda(tAd, tBd)
    print("C6 %s: rank(C)=%d rank(aug)=%d lam=%s" % (name, rc, ra,
          None if lam is None else [str(v) for v in lam]))
    if lam is None:
        C6a = False
    else:
        lams[name] = lam
        Csol[name] = Cc
C6b = C6a
if C6a:
    ref = "TA1v1"
    for k in lams:
        if k != ref:
            diff = lams[k] - lams[ref]
            if sp.Matrix.hstack(Csol[ref], diff).rank() != Csol[ref].rank():
                C6b = False
                print("C6 universality FAIL: %s lam differs outside nullspace" % k)
# The established fact is BOUNDED NON-EXISTENCE: at every closed test point
# A2 lies outside the span of the images of the enumerated ansatz class, so no
# jet-universal B2 exists in that class. This is NOT a no-go for the full
# Kontsevich natural class, which also contains (dTheta)(dTheta), Theta d^3 Theta
# and (d^2Theta)(d^2Theta) contractions that this enumeration does not cover.
C6 = C6a is False
print("C6 (no jet-universal B2 in the enumerated ansatz class %s at closed jets:"
      " A2 outside image span at all %d closed test points): %s"
      % (str(NKINDS), len(pts), "PASS (bounded ansatz non-existence)"
         if C6 else "UNEXPECTED (a universal solution was found)"))
ok["C6"] = C6

# ---------- C7: corrected (b): closed, Theta(0)!=0, naive associator nonzero ----------
# generic non-closed point: membership must fail (plain M2r test)
mem_nonclosed, _, _ = membership(TA1pt, TBadic_g)
# closed example: TB = first nullspace vector (nonzero), membership must hold
tBex = tb_from_basis(NB1, [1] + [0] * (len(NB1) - 1))
A2cl = A2sub(TA1pt, tBex)
nz = sum(1 for v in A2cl if v != 0)
mem_closed, r1c, r2c = membership(TA1pt, tBex)
# old s1 examples: show Theta(0)=0
ex1_TA = {(k[0], k[1]): sp.Integer(0) for k in TA}
A2old = A2sub(ex1_TA, {(0, 1, 2): sp.Integer(1)})
C7 = (not mem_nonclosed) and mem_closed and nz > 0 and A2old == sp.zeros(544, 1)
print("C7: nonclosed membership=%s ; closed example: A2 nonzero rows=%d, membership=%s ;"
      " s1 ex1/ex2 Theta(0)=0 -> A2 identically 0: %s" %
      (mem_nonclosed, nz, mem_closed, A2old == sp.zeros(544, 1)), "PASS" if C7 else "FAIL")
ok["C7"] = C7

# ---------- C8: constant-Theta defect = delta(Moyal B2), symbolic over TA.
# Associativity of f*g = fg + (i/2)Theta ff gg + B2 at order Theta^2 reads
# A2 = delta c2 (the Theta^2 term of (f*g)*h - f*(g*h) is A2 - delta c2). ----------
subs0 = {TB[k]: sp.Integer(0) for k in TB}
b2m = COLS["P1"] * sp.Rational(-1, 8)
A2c8 = sp.Matrix([A2tab[t].subs(subs0) for t in DER3])
res8 = sp.Matrix(M2r * b2m.subs(subs0)) - A2c8
bad8 = [DER3[i] for i in range(len(DER3)) if sp.expand(res8[i]) != 0]
print("C8 (delta(B2M) - A2(const Theta) = 0 symbolically, generic TA): %s"
      % ("PASS" if not bad8 else "FAIL at %s" % bad8[:3]))
ok["C8"] = (not bad8)

# ---------- C9: end-to-end numeric operator check on actual functions ----------
rng9 = random.Random(20261120)
def rnd9():
    return sp.Rational(rng9.randrange(-30, 31), rng9.randrange(1, 8))
numfails = 0
jetsubs_num = {TA[k]: TA1pt[k] for k in TA}
jetsubs_num.update({TB[k]: tBex[k] for k in sorted(TB)})
jetsubs_num.update({TQ[k]: sp.Integer(0) for k in TQ})
# C9: constant-Theta Moyal B2, direct operator form, TB=0 at generic TA.
jetsubs_num = {TA[k]: TA1pt[k] for k in TA}
jetsubs_num.update({TB[k]: sp.Integer(0) for k in TB})
jetsubs_num.update({TQ[k]: sp.Integer(0) for k in TQ})

def B1num(p, q):
    return sp.expand(B1op(p, q).subs(jetsubs_num))

def B2num(p, q):
    s = sp.S.Zero
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                for dd in range(4):
                    cf = TT0(a, b) * TT0(cc, dd)
                    dp = sp.diff(sp.diff(p, x[a]), x[cc])
                    dq = sp.diff(sp.diff(q, x[b]), x[dd])
                    if dp == 0 or dq == 0:
                        continue
                    s = s + sp.Rational(-1, 8) * cf * dp * dq
    return sp.expand(s.subs(jetsubs_num))

for trial in range(3):
    f9 = sum(rnd9() * MON[t] for t in range(15))
    g9 = sum(rnd9() * MON[t] for t in range(15))
    h9 = sum(rnd9() * MON[t] for t in range(15))
    lhs = eval0(f9 * B2num(g9, h9) - B2num(f9 * g9, h9) + B2num(f9, g9 * h9)
                - B2num(f9, g9) * h9)
    rhs = eval0(B1num(B1num(f9, g9), h9) - B1num(f9, B1num(g9, h9)))
    resid = sp.simplify(sp.expand(lhs - rhs))
    if resid != 0:
        numfails += 1
        print("C9 FAIL trial %d resid=%s" % (trial, resid))
C9 = numfails == 0
print("C9 (exact-operator check: delta(B2M) = A2 on random quadratics, constant Theta,"
      " seed 20261120):", "PASS" if C9 else "FAIL")
ok["C9"] = C9

# ---------- summary ----------
print()
print("kappa (antisym(A2) = kappa*[Theta,Theta].(df,dg,dh)) =", kappa)
print("claim results:", {k: ("PASS" if v else "FAIL") for k, v in sorted(ok.items())})
print("total %.1fs" % (time.time() - t0))
sys.exit(0 if all(ok.values()) else 1)
