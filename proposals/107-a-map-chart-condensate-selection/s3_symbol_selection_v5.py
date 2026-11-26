# s3_symbol_selection_v5.py -- proposal 107 r1, central computation (AUTHORITATIVE).
# v4 ran all claims PASS except Q3pt, whose right-nullspace bug this version fixes
# (invisible basis must be the LEFT nullspace of the pairing matrix). Supersedes
# v4/v3/v2/s3, all retained as provenance.
# Chart-condensate selection of the order-Theta^2 correction: what the model's own
# Weyl symbol map (ch03 rem:ch3-trace-quadratic; appH finite-N 't Hooft-torus data)
# selects, and the reach of matrix-side selection at order Theta^2 inside the
# diffeomorphism-pullback class of item 106 (appH sec:status-A).
#
# SETTING. Matrix side (class (H1)-(H3) of 106): Xhat^I Hermitian,
# [Xhat^I,Xhat^J] = i Theta^{IJ} CONSTANT nondegenerate; constant-Theta Weyl map;
# product = operator product = Moyal, exactly associative; finite-N model is the
# 't Hooft torus pair UV = e^{i Theta} VU with Weyl-ordered modes
# W_u = e^{-i Theta m n/2} U^m V^n, u=(m,n) in Z_N^2 (appH, integrated paragraph).
# Semiclassical configuration and pullback data (A,B,Theta) -> (M,N,theta(0),dtheta(0))
# and the selected table c(B) = B2PB table: the item-106 framework, definitions copied
# byte-for-byte from proposals/106-a-map-chart-condensate-selection/s2_matrix_selection.py
# (JET/MON/prodjet/BAS2r/DER3/M2r/antisym6/pf6/pullback_data/cvec). The A2 table, scht
# and mk_struct of s2 are NOT needed here (no coboundary-membership claims); the M2r
# rank/ker framework parity is asserted.
#
# CLAIMS (printed Q1..Q4; exact rational/symbolic arithmetic except Q1c numerics):
#  Q1 finite-N Weyl symbol map data (th formal; th = 2*pi/5 only in Q1c):
#     Q1a left-ordered mode phase d(u,v) = e^{i th n p} satisfies the 2-cocycle
#         (associativity of the operator product) exactly.
#     Q1b Weyl-ordered mode phase c(u,v) = e^{-i th sigma(u,v)/2}, sigma(u,v)=m q - n p,
#         also a 2-cocycle; its commutator coefficient c(u,v) - c(v,u) equals
#         -2i sin(th sigma/2) EXACTLY; Taylor in th: = -i th sigma + i (th sigma)^3/24
#         + O(th^5), i.e. agrees with the Poisson bracket i th sigma through order th^2
#         and first deviates at order th^3; c(u,v) = d(u,v) * d-phi(u,v) exactly with the
#         quadratic phase phi(u) = e^{i th m n/2} (ordering = coboundary gauge); the
#         structure constants c(u,v) depend on the labels and th only (no chart, field,
#         or embedding symbol appears).
#     Q1c 5x5 't Hooft numerics: Tr(W_u W_v) = N delta_{u+v=0} e^{-2 i th m n} and
#         Tr(B_u B_v) = N delta_{u+v=0} e^{i th n p} for Weyl- resp. left-ordered modes,
#         and |Tr| per mode is ordering-independent (max abs errors < 1e-10).
#  Q2 reach = chart 2-jet image. Framework parity: rank(M2r)=160, dim ker(M2r)=36,
#     dim ker(M2r^T)=384 (rank-nullity); selection map B -> dtheta(0) at fixed (A,Theta)
#     has rank 20, kernel dim 20; at each of two rational base points B0: all 20
#     kernel-direction table changes lie in ker(M2r) (544 rows each), leave dtheta(0)
#     fixed, are nonzero, and their span has dimension 20.
#  Q3 the 16 invisible directions. At each point: the pairing matrix between ker(M2r)
#     (dim 36) and the 20 selection-change directions has rank 20; hence exactly
#     36 - 20 = 16 kernel directions are orthogonal to the whole reachable set; an
#     explicit 16-vector basis is exhibited, each vector verified in ker(M2r) and
#     orthogonal to every reachable direction. Same at both rational points.
#  Q4 symplectic covariance: with S the 106 rational Sp(Theta_std) transvection, the
#     data (A,B,Theta) -> (S A, S B, S Theta S^T) leaves the theta-jet and the selected
#     table invariant (106 P8 content, re-verified), while the torus symbol datum
#     (th, ordering) mentions no chart data at all (Q1b free-symbol check).
import hashlib
import itertools
import os
import sys
import time
import sympy as sp

_self = os.path.abspath(__file__)
_b = open(_self, "rb").read()
print("checked script: %s %d bytes sha256/16 %s"
      % (_self.replace(os.sep, "/"), len(_b), hashlib.sha256(_b).hexdigest()[:16]))
print("python: %s" % sys.version.split()[0])

t0 = time.time()
d = 4
ok = {}
I = sp.I
x = sp.symbols("x0:4")   # leaf coordinates (105/106 framework variable)

# ---------- jet basis (105 s1b / 106 s2 framework, same definitions) ----------
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

BAS2r = [t for t in itertools.product(range(15), repeat=2)
         if len(JET[t[0]]) >= 1 and len(JET[t[1]]) >= 1]
IDX2r = {t: k for k, t in enumerate(BAS2r)}
assert len(BAS2r) == 196

DER3 = [t for t in itertools.product(range(15), repeat=3)
        if min(len(JET[t[0]]), len(JET[t[1]]), len(JET[t[2]])) >= 1
        and len(JET[t[0]]) + len(JET[t[1]]) + len(JET[t[2]]) <= 4]
assert len(DER3) == 544

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
KER = M2r.nullspace()
print("M2r rank = %d, dim ker(M2r) = %d, dim ker(M2r^T) = %d (by rank-nullity), %.1fs"
      % (rankM2, len(KER), 544 - rankM2, time.time() - t0))
ok["framework"] = (rankM2 == 160 and len(KER) == 36 and 544 - rankM2 == 384)

# ---------- embedding model (106 s2 definitions) ----------
A0 = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]  # generic rational, det 1

def antisym6(vals):
    def TH(Ii, Jj):
        if Ii == Jj:
            return sp.S.Zero
        return vals.get((Ii, Jj), 0) if Ii < Jj else -vals.get((Jj, Ii), 0)
    return TH

def pf6(TH):
    return TH(0, 1) * TH(2, 3) - TH(0, 2) * TH(1, 3) + TH(0, 3) * TH(1, 2)

def pullback_data(Amat, Bsym, TH):
    A = sp.Matrix(Amat)
    Mm = A.inv()
    N = {}
    for a in range(d):
        for Ii in range(d):
            for Jj in range(Ii, d):
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
    """196-table of B2PB(MON_P, MON_Q)|0 (106 cvec, unchanged)."""
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
                            s2 += (TH(Ii, Jj) * TH(Kk, Ll) * Mm[a, Ii] * Mm[b, Kk]
                                   * N[(c, min(Jj, Ll), max(Jj, Ll))])
            C21[(a, b, c)] = sp.Rational(-1, 8) * sp.expand(s2)
            s3 = sp.S.Zero
            for Ii in range(d):
                for Jj in range(d):
                    for Kk in range(d):
                        for Ll in range(d):
                            s3 += (TH(Ii, Jj) * TH(Kk, Ll)
                                   * N[(a, min(Ii, Kk), max(Ii, Kk))]
                                   * Mm[c, Jj] * Mm[b, Ll])
            C12[(a, c, b)] = sp.Rational(-1, 8) * sp.expand(s3)
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
    return sp.Matrix(vec)

# ================= Q1: finite-N Weyl symbol map data =================
th = sp.symbols("th", real=True)   # formal torus angle (th = 2 pi p / N on Z_N^2)

def sig(u, v):
    return u[0] * v[1] - u[1] * v[0]          # sigma(u,v) = m q - n p

def dph(u, v):                                # left-ordered product phase
    return sp.exp(I * th * u[1] * v[0])

def cph(u, v):                                # Weyl-ordered product phase
    return sp.exp(-I * th * sig(u, v) / 2)

LB = list(itertools.product(range(-2, 3), repeat=2))     # label box, 25 modes
TLB = list(itertools.product(range(-1, 2), repeat=2))    # smaller box for triples
trip = list(itertools.product(TLB, repeat=3))

# exponents are bilinear integer polynomials in th: extract by differentiating at th=0
def exponent_of(phfun, u, v):
    return sp.simplify(sp.diff(phfun(u, v), th).subs(th, 0))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

bad_a = [t for t in trip
         if sp.expand(exponent_of(dph, t[0], t[1])
                      + exponent_of(dph, add(t[0], t[1]), t[2])
                      - exponent_of(dph, t[1], t[2])
                      - exponent_of(dph, t[0], add(t[1], t[2]))) != 0]
Q1a = (len(bad_a) == 0)
print("Q1a left-ordered phase cocycle (associativity) over %d label triples, exponents "
      "agree exactly: %s" % (len(trip), "PASS" if Q1a else "FAIL %s" % bad_a[:2]))
ok["Q1a"] = Q1a

bad_b = [t for t in trip
         if sp.expand(exponent_of(cph, t[0], t[1])
                      + exponent_of(cph, add(t[0], t[1]), t[2])
                      - exponent_of(cph, t[1], t[2])
                      - exponent_of(cph, t[0], add(t[1], t[2]))) != 0]
pairs = list(itertools.product(LB, repeat=2))
bad_c = [p for p in pairs
         if sp.simplify(cph(p[0], p[1]) - cph(p[1], p[0]) + 2 * I * sp.sin(th * sig(*p) / 2)) != 0]
# Taylor at a pair with sigma != 0: c(u,v)-c(v,u) = -2i sin(th sigma/2)
#   = -i th sigma + i (th sigma)^3/24 + O(th^5)
p0 = ((1, 0), (0, 1))                          # sigma = 1
ser = sp.series(cph(*p0) - cph(p0[1], p0[0]), th, 0, 5).removeO()
sg = sig(*p0)
bad_t = sp.simplify(ser - (-I * th * sg + I * (th * sg) ** 3 / 24))
# ordering gauge: c = d * delta-phi with phi(u)=e^{i th m n/2}: dphi(u,v)=phi(u)phi(v)/phi(u+v)
def phi(u):
    return sp.exp(I * th * u[0] * u[1] / 2)
def dphi(u, v):
    return sp.simplify(phi(u) * phi(v) / phi(add(u, v)))
bad_g = [p for p in pairs if sp.simplify(cph(p[0], p[1]) - dph(p[0], p[1]) * dphi(p[0], p[1])) != 0]
# structure constants: labels + th only
sc_free = set()
for p in pairs:
    sc_free |= (cph(p[0], p[1]).free_symbols - {th})
Q1b = (len(bad_b) == 0 and len(bad_c) == 0 and bad_t == 0 and len(bad_g) == 0
       and len(sc_free) == 0)
print("Q1b Weyl phase cocycle (%d triples, %d failures); commutator = -2i sin(th sigma/2)"
      " exactly (%d pairs, %d failures); Taylor -i th sigma + i (th sigma)^3/24 + O(th^5):"
      " %s; gauge c = d*delta-phi with phi = e^{i th m n/2} (%d pairs, %d failures); struct-"
      " constants free of any non-label symbol: %s"
      % (len(trip), len(bad_b), len(pairs), len(bad_c), "PASS" if bad_t == 0 else "FAIL",
         len(pairs), len(bad_g), "PASS" if len(sc_free) == 0 else "FAIL %s" % sc_free))
ok["Q1b"] = Q1b

# Q1c: explicit 5x5 't Hooft matrices, th = 2 pi /5, numeric check of the exact laws
import cmath
N = 5
ang = 2 * cmath.pi / N
w = complex(cmath.cos(2 * cmath.pi / N), cmath.sin(2 * cmath.pi / N))
U = [[0.0] * N for _ in range(N)]
for i in range(N):
    U[(i + 1) % N][i] = 1.0

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def Um(m):
    mm = m % N
    A = [[0j] * N for _ in range(N)]
    for i in range(N):
        A[(i + mm) % N][i] = 1.0
    return A

def Vn(n):
    A = [[0j] * N for _ in range(N)]
    for i in range(N):
        A[i][i] = w ** (n * i)
    return A

def Weyl(m, n):
    ph = cmath.exp(-1j * ang * m * n / 2)
    MM = matmul(Um(m), Vn(n))
    return [[ph * MM[i][j] for j in range(N)] for i in range(N)]

def Wbare(m, n):
    return matmul(Um(m), Vn(n))

def tr(M):
    return sum(M[i][i] for i in range(N))

maxerr_p = 0.0
maxerr_g = 0.0
for m in range(-2, 3):
    for n in range(-2, 3):
        for p in range(-2, 3):
            for q in range(-2, 3):
                tW = tr(matmul(Weyl(m, n), Weyl(p, q)))
                tW_exact = (5.0 * cmath.exp(-2j * ang * m * n)
                            if (m + p) % 5 == 0 and (n + q) % 5 == 0 else 0.0)
                maxerr_p = max(maxerr_p, abs(tW - tW_exact))
                tB = tr(matmul(Wbare(m, n), Wbare(p, q)))
                tB_exact = (5.0 * cmath.exp(1j * ang * n * p)
                            if (m + p) % 5 == 0 and (n + q) % 5 == 0 else 0.0)
                maxerr_g = max(maxerr_g, abs(tB - tB_exact))
maxerr_abs = 0.0
for m in range(-2, 3):
    for n in range(-2, 3):
        maxerr_abs = max(maxerr_abs, abs(abs(tr(Weyl(m, n))) - abs(tr(Wbare(m, n)))))
Q1c = maxerr_p < 1e-10 and maxerr_g < 1e-10 and maxerr_abs < 1e-10
print("Q1c 5x5 't Hooft numerics: Tr(W_u W_v) = N delta_{u+v,0} e^{-2 i th m n}"
      " maxerr %.2e ; Tr(B_u B_v) = N delta_{u+v,0} e^{i th n p} maxerr %.2e ; |Tr|"
      " ordering-independent maxerr %.2e" % (maxerr_p, maxerr_g, maxerr_abs))
print("Q1c:", "PASS" if Q1c else "FAIL")
ok["Q1c"] = Q1c

# ============ Q2/Q3: reach of matrix selection = chart 2-jet image ============
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
THstd = antisym6({(0, 1): sp.Integer(1), (2, 3): sp.Integer(1)})
_, _, th0s, dth_s = pullback_data(A0, Bs, THstd)
rows6 = []
for k in sorted(dth_s):
    rows6.append([sp.expand(dth_s[k]).coeff(s) for s in bsyms])
Mb = sp.Matrix(rows6)
rk = Mb.rank()
NB = Mb.nullspace()
print("Q2: rank(B -> dtheta(0)) = %d (expect 20 = 24-4 closedness), kernel dim %d"
      % (rk, len(NB)))
ok["Q2map"] = (rk == 20 and len(NB) == 20)

import random
def make_B0(seed):
    r3 = random.Random(seed)
    B = {}
    for a in range(d):
        B[a] = {}
        for b in range(d):
            B[a][b] = {}
            for c in range(d):
                B[a][b][c] = (sp.Rational(r3.randrange(-5, 6), r3.randrange(1, 6))
                              if c >= b else None)
    for a in range(d):
        for b in range(d):
            for c in range(d):
                B[a][b][c] = B[a][min(b, c)][max(b, c)]
    return B

for seed in (1070, 1071):
    B0 = make_B0(seed)
    Mq0, Nq0, th06, dth6 = pullback_data(A0, B0, THstd)
    assert pf6(antisym6({k: th06[k] for k in th06})) != 0
    c0 = cvec(Mq0, Nq0, THstd)
    diffs = []
    allok = True
    for m, v in enumerate(NB):
        Bp = {}
        for a in range(d):
            Bp[a] = {}
            for b in range(d):
                Bp[a][b] = {}
                for c in range(d):
                    Bp[a][b][c] = (B0[a][min(b, c)][max(b, c)]
                                   + v[bsyms.index(Bs[a][min(b, c)][max(b, c)])])
        M1, N1, _, dth1 = pullback_data(A0, Bp, THstd)
        c1 = cvec(M1, N1, THstd)
        dv = c1 - c0
        jet_same = all(sp.expand(dth1[k] - dth6[k]) == 0 for k in dth6)
        ker_ok = all(sp.Matrix(M2r * dv)[i] == 0 for i in range(544))
        nz = sum(1 for wv in dv if wv != 0)
        if not (jet_same and ker_ok and nz > 0):
            allok = False
            print("Q2 pt %d: kernel vector %d: jet_same %s ker %s nz %d -- UNEXPECTED"
                  % (seed, m, jet_same, ker_ok, nz))
        diffs.append(dv)
    spanM = sp.Matrix.hstack(*diffs)
    sdim = spanM.rank()
    print("Q2 pt seed %d: all 20 kernel directions: dtheta fixed, table changes in ker(M2r),"
          " nonzero: %s ; span dim %d (expect 20)" % (seed, allok, sdim))
    ok["Q2pt%d" % seed] = allok and sdim == 20
    # Q3: pairing of ker(M2r) (36) against the 20 reachable directions
    R = sp.Matrix([[sp.expand(KER[i].dot(diffs[j])) for j in range(20)] for i in range(36)])
    rR = R.rank()
    inv = R.T.nullspace()   # LEFT nullspace (coefficients c in R^36, c^T R = 0)
    invis = []
    for iv in inv:
        vv = sp.zeros(196, 1)
        for k in range(36):
            if iv[k] != 0:
                vv = vv + iv[k] * KER[k]
        invis.append(vv)
    invis_ok = all(all(sp.Matrix(M2r * iv)[r] == 0 for r in range(544)) and
                   any(e != 0 for e in iv) for iv in invis)
    orth_ok = all(all(sp.expand(iv.dot(dv)) == 0 for dv in diffs) for iv in invis)
    print("Q3 pt seed %d: pairing rank %d (expect 20) -> invisible dim %d (expect 16);"
          " explicit basis all in ker(M2r): %s ; orthogonal to whole reachable span: %s"
          % (seed, rR, 36 - rR, invis_ok, orth_ok))
    ok["Q3pt%d" % seed] = (rR == 20 and len(inv) == 16 and invis_ok and orth_ok)

# ================= Q4: symplectic covariance of datum + image =================
S = sp.Matrix([[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 3, 1]])
Tstd = sp.Matrix([[THstd(a, b) for b in range(d)] for a in range(d)])
Sok = (S * Tstd * S.T == Tstd)
TH8 = {(a, b): sp.S.Zero for a, b in itertools.combinations(range(d), 2)}
for a, b in itertools.combinations(range(d), 2):
    v = sp.S.Zero
    for Kk in range(d):
        for Ll in range(d):
            v += S[a, Kk] * S[b, Ll] * THstd(Kk, Ll)
    TH8[(a, b)] = v
B0q = make_B0(1070)
A8 = (S * sp.Matrix(A0)).tolist()
B8 = {}
for a in range(d):
    B8[a] = {}
    for b in range(d):
        B8[a][b] = {}
        for c in range(d):
            v = sp.S.Zero
            for Kk in range(d):
                v += S[a, Kk] * B0q[Kk][b][c]
            B8[a][b][c] = v
M8, N8, th8, dth8 = pullback_data(A8, B8, antisym6(TH8))
c8 = cvec(M8, N8, antisym6(TH8))
Mq0, Nq0, th06q, dth6q = pullback_data(A0, B0q, THstd)
c0q = cvec(Mq0, Nq0, THstd)
Q4 = (Sok
      and sp.Matrix([sp.expand(th8[k] - th06q[k]) for k in th8]) == sp.zeros(6, 1)
      and sp.Matrix([sp.expand(dth8[k] - dth6q[k]) for k in dth8]) == sp.zeros(24, 1)
      and sp.Matrix([sp.expand(c8[i] - c0q[i]) for i in range(196)]) == sp.zeros(196, 1))
print("Q4 (rational Sp(Theta_std) transvection: S Theta S^T = Theta; (A,B,TH) -> (SA,SB,"
      "S TH S^T) leaves the theta-jet and the selected table invariant; the torus symbol"
      " datum (th, ordering) mentions no chart data at all -- Q1b free-symbol check):",
      "PASS" if Q4 else "FAIL")
ok["Q4"] = Q4

# ---------- summary ----------
print()
print("claim results:", {k: ("PASS" if v else "FAIL") for k, v in sorted(ok.items())})
print("total %.1fs" % (time.time() - t0))
sys.exit(0 if all(ok.values()) else 1)
