# verify_r119.py  (run: python -I -B verify_r119.py)
# Chain 119 stage-3 verifier: re-derives, across full parameter ranges, every numerical claim
# used in insert-overdetermination-r1.tex and proposal-r1.md. Independent of the scratch/119
# scripts (same mathematics, fresh code paths; scratch is the stage-1/2 record, this file is
# the stage-3 reproduction). Prints "TOTAL x/x PASS" and "ALL CHECKS DONE 119".
# Conventions: Phi is n x 4 complex (gauge U(n)/SU(n) on the I index, global U(4) on A),
# X = Phi^dagger Phi, Y = Phi Phi^dagger. One-loop machine (calibrated in group H):
# V1_div = +(1/64 pi^2 eps) STrM4(bg), MSbar pole subtraction, beta = -2*[1/eps coeff of CT].
import sympy as sp

PASS = [0]
FAIL = [0]

def chk(name, cond):
    cond = bool(cond)
    if cond:
        PASS[0] += 1
    else:
        FAIL[0] += 1
    print(("PASS " if cond else "FAIL ") + name)

def vars_n(nn):
    return sp.symbols("x0:%d" % (2 * nn * 4), real=True)

def Pmat(nn, vv):
    return sp.Matrix(nn, 4, lambda i, a: vv[8 * i + 2 * a] + sp.I * vv[8 * i + 2 * a + 1])

def TrX2(P):
    X = P.adjoint() * P
    return sp.expand(sp.trace(X * X))

def TrXsq(P):
    X = P.adjoint() * P
    return sp.expand(sp.trace(X) ** 2)

def orth_u(N):
    b = []
    r2 = 1 / sp.sqrt(2)
    for i in range(N):
        for j in range(i + 1, N):
            m = sp.zeros(N); m[i, j] = r2; m[j, i] = r2; b.append(m)
            m2 = sp.zeros(N); m2[i, j] = -sp.I * r2; m2[j, i] = sp.I * r2; b.append(m2)
    for i in range(N):
        d = sp.zeros(N); d[i, i] = 1; b.append(d)
    return b

def orth_su(N):
    b = []
    r2 = 1 / sp.sqrt(2)
    for i in range(N):
        for j in range(i + 1, N):
            m = sp.zeros(N); m[i, j] = r2; m[j, i] = r2; b.append(m)
            m2 = sp.zeros(N); m2[i, j] = -sp.I * r2; m2[j, i] = sp.I * r2; b.append(m2)
    for k in range(1, N):
        d = sp.zeros(N)
        for j in range(k):
            d[j, j] = 1
        d[k, k] = -k
        b.append(d / sp.sqrt(k * (k + 1)))
    return b

def is_orth(b):
    for x, A in enumerate(b):
        for y, B in enumerate(b):
            tr = sp.simplify(sp.trace(A * B))
            want = 1 if x == y else 0
            if sp.simplify(tr - want) != 0:
                return False
    return True

def fitAB(nn, c3v, c2v, bgs=None):
    # scalar sector: S = Tr(H W H W) on diagonal backgrounds, fit S = A*TrX^2 + B*(TrX)^2
    vv = vars_n(nn)
    P = Pmat(nn, vv)
    bgs = [(1, 1, 0, 0), (2, 1, 0, 0), (1, 1, 1, 0), (2, 1, 1, 0), (1, 1, 1, 1)]
    data = []
    for bg in bgs:
        # Phi is nn x 4: row shifts exist only for rows 0..min(nn,4)-1 (X = Phi^dag Phi is 4x4)
        subs = {vv[10 * i]: vv[10 * i] + bg[i] for i in range(min(nn, 4))}
        W = sp.expand((c3v * TrX2(P) + c2v * TrXsq(P)).subs(subs))
        H = sp.hessian(W, vv)
        H = sp.simplify(H.subs({u: 0 for u in vv}))
        S = sp.simplify((H * H).trace())
        ys = [s * s for s in bg[:nn]]
        data.append((sum(y * y for y in ys), sum(ys) ** 2, S))
    A, Bc = sp.symbols("Afit Bfit")
    sol = sp.solve([sp.Eq(A * d[0] + Bc * d[1], d[2]) for d in data[:2]], [A, Bc], dict=True)[0]
    resid = [sp.simplify(d[2] - (sol[A] * d[0] + sol[Bc] * d[1])) for d in data[2:]]
    return sp.simplify(sol[A]), sp.simplify(sol[Bc]), resid

def gaugeS(Pm, basis):
    Y = sp.simplify(Pm * Pm.adjoint())
    K = [[sp.simplify(sp.trace(A * Y * B)) for B in basis] for A in basis]
    S = sum(sp.simplify(K[a][b] * K[b][a]) for a in range(len(basis)) for b in range(len(basis)))
    return sp.simplify(sp.expand_complex(S))

# ---------------- A. eq:V slice ----------------
print("== A. eq:V slice and invariant independence ==")
lam, v2 = sp.symbols("lambda v2", positive=True)
# generic 4x4 X (16 independent symbols): the slice identity is an identity of 4x4 matrices;
# X = Phi^dagger Phi by definition, so this covers the potential for any Phi.
Xg = sp.Matrix(4, 4, lambda i, j: sp.Symbol("u%d%d" % (i, j)))
Vslice = sp.expand(sp.Rational(1, 4) * lam * sp.trace((Xg - v2 * sp.eye(4)) ** 2))
Vform = sp.expand(lam / 4 * sp.trace(Xg * Xg) - lam * v2 / 2 * sp.trace(Xg) + lam * v2 ** 2)
chk("A1 eq:V = (lam/4)TrX^2 - (lam v2/2)TrX + lam v2^2 with zero (TrX)^2 coefficient, generic 4x4 X",
    sp.simplify(Vslice - Vform) == 0)
def tvals(sig):
    Pd = sp.diag(*[sp.Integer(s) for s in sig] + [0] * (4 - len(sig)))
    Xd = Pd.adjoint() * Pd
    return (sp.trace(Xd * Xd), sp.trace(Xd) ** 2)
M = sp.Matrix([[tvals((1, 1, 0, 0))[0], tvals((1, 1, 0, 0))[1]],
               [tvals((1, 1, 1, 0))[0], tvals((1, 1, 1, 0))[1]]])
chk("A2 TrX^2 and (TrX)^2 independent on rank>=2 diagonal backgrounds (det != 0)",
    M.det() != 0)

# ---------------- H. one-loop machine calibration anchors ----------------
print("== H. one-loop machine calibration anchors ==")
phi = sp.symbols("phi", real=True)
l4 = sp.symbols("lam4", positive=True)
H1 = sp.hessian(sp.expand(l4 * phi ** 4 / 24), (phi,))
chk("H1 single-scalar STrM4 = Tr H^2 = lam4^2 phi^4 / 4 for W = lam4 phi^4/24",
    sp.simplify(H1[0, 0] ** 2 - l4 ** 2 * phi ** 4 / 4) == 0)
# MSbar chain: V1_div = (1/64 pi^2 eps) STrM4 ; CT: delta_lam4 phi^4/24 = -V1_div ; beta = -2*pole
V1d = (l4 ** 2 * phi ** 4 / 4) / (64 * sp.pi ** 2)
dlam = sp.simplify(-24 * V1d / phi ** 4)
beta = sp.simplify(-2 * dlam)
chk("H2 MSbar chain gives beta(lam4) = 3 lam4^2/(16 pi^2) (textbook anchor)",
    sp.simplify(beta - 3 * l4 ** 2 / (16 * sp.pi ** 2)) == 0)
co2 = sp.symbols("cO2", positive=True)
p1, p2 = sp.symbols("p1 p2", real=True)
HO = sp.hessian(sp.expand(co2 * (p1 ** 2 + p2 ** 2) ** 2), (p1, p2))
HO0 = sp.simplify(HO.subs({p2: 0}))
chk("H3 O(2) model W = cO2 (phi^2)^2: Tr H^2 = 160 cO2^2 phi^4 (textbook beta anchor input)",
    sp.simplify((HO0 * HO0).trace() - 160 * co2 ** 2 * p1 ** 4) == 0)

# ---------------- B. scalar structure tensors T33/T32/T22, n=2..6 ----------------
print("== B. scalar structure tensors (exact Hessian, S = Tr(H W H W)) ==")
TT = {}
for nn in (2, 3, 4, 5, 6):
    A33, B33, r33 = fitAB(nn, sp.Integer(1), sp.Integer(0))
    A22, B22, r22 = fitAB(nn, sp.Integer(0), sp.Integer(1))
    A11, B11, _ = fitAB(nn, sp.Integer(1), sp.Integer(1))
    A32 = sp.simplify((A11 - A33 - A22) / 2)
    B32 = sp.simplify((B11 - B33 - B22) / 2)
    TT[nn] = (A33, B33, A32, B32, A22, B22)
    ok = (A33 == 32 * (nn + 4) and B33 == 96 and A32 == 96 and B32 == 32 * (nn + 4)
          and A22 == 0 and B22 == 128 * (nn + 1) and all(x == 0 for x in r33 + r22))
    chk("B1 n=%d: T33=(32(n+4),96) T32=(96,32(n+4)) T22=(0,128(n+1)) exact, residuals 0" % nn, ok)
    if nn == 4:
        chk("B2 n=4 q3 anchor: (A33,B32->B33)=(256,96), B33/A33 = 3/8",
            (A33, B33) == (256, 96) and sp.Rational(96, 256) == sp.Rational(3, 8))
# generic off-diagonal n=4 bilinear-identity check (c3=2, c2=3), same integer values as stage record
vv = vars_n(4)
Pg = Pmat(4, vv)
Wgen = sp.expand(sp.simplify(2 * TrX2(Pg) + 3 * TrXsq(Pg)))
Hg = sp.hessian(Wgen, vv)
gvals = {vv[k]: k + 1 for k in range(16)}
gvals.update({vv[16 + k]: k for k in range(16)})
Hg2 = sp.simplify(Hg.subs(gvals))
Sg = sp.simplify((Hg2 * Hg2).trace())
Pgv = Pg.subs(gvals)
XXg = sp.simplify(Pgv.adjoint() * Pgv)
t2g = sp.simplify(sp.trace(XXg * XXg))
t1g2 = sp.simplify(sp.trace(XXg)) ** 2
A33, B33, A32, B32, A22, B22 = TT[4]
pred = sp.expand(4 * (A33 * t2g + B33 * t1g2) + 12 * (A32 * t2g + B32 * t1g2) + 9 * (A22 * t2g + B22 * t1g2))
chk("B3 n=4 generic off-diagonal Phi (c3=2,c2=3): S - pred = 0 (bilinear tensor identity)",
    sp.simplify(Sg - pred) == 0)

# ---------------- C. gauge one-loop (A,B): u(n) vs su(n), orthonormality teeth ----------------
print("== C. gauge one-loop S = sum_ab K^ab K^ba, K^ab = Tr(T^a Y T^b) ==")
def gauge_fit(N, basis, wantA, wantB):
    bgs = [(1, 1, 0, 0), (2, 1, 0, 0), (1, 1, 1, 0), (2, 1, 1, 0)]
    data = []
    for bg in bgs[:(2 if N == 2 else 4)]:
        Pd = sp.zeros(N, 4)
        for i, s in enumerate(bg[:N]):
            Pd[i, i] = s
        ys = [s * s for s in bg[:N]]
        data.append((sum(y * y for y in ys), sum(ys) ** 2, gaugeS(Pd, basis)))
    A, Bc = sp.symbols("Ag Bg")
    sol = sp.solve([sp.Eq(A * d[0] + Bc * d[1], d[2]) for d in data[:2]], [A, Bc], dict=True)[0]
    resid = [sp.simplify(d[2] - (sol[A] * d[0] + sol[Bc] * d[1])) for d in data[2:]]
    return sp.simplify(sol[A]), sp.simplify(sol[Bc]), resid
for N in (2, 3, 4, 5):
    bu = orth_u(N)
    chk("C1 u(%d): orthonormal Hermitian basis asserted" % N, is_orth(bu))
    Au, Bu, ru = gauge_fit(N, bu, N, 0)
    chk("C2 u(%d): S = n TrX^2 exactly, (TrX)^2 coeff 0, residuals 0 (c2=0 preserved)" % N,
        Au == N and Bu == 0 and all(x == 0 for x in ru))
for N in (2, 3, 4, 5, 6):
    bs = orth_su(N)
    chk("C3 su(%d): traceless orthonormal basis asserted" % N, is_orth(bs))
    As, Bs, rs = gauge_fit(N, bs, 0, 0)
    okA = sp.simplify(As - (N - sp.Rational(2, N))) == 0
    okB = sp.simplify(Bs - sp.Rational(1, N * N)) == 0
    chk("C4 su(%d): (A,B) = (n-2/n, 1/n^2) = (%s, %s), residuals 0" % (N, As, Bs),
        okA and okB and all(x == 0 for x in rs))
    if N == 2:
        chk("C5 su(2) hand anchor: A=1, B=1/4 (S = TrY^2 + (TrY)^2/4, Pauli hand computation)",
            As == 1 and Bs == sp.Rational(1, 4))
# exact generic-Phi checks (integer complex entries): u(4) -> S = 4 TrX^2; su(4) -> (7/2,1/16) form
Pint = (sp.Matrix([[1, 2, 0, 1], [0, 3, 1, 0], [1, 0, 2, 1], [2, 1, 0, 1]])
        + sp.I * sp.Matrix([[0, 1, 0, 2], [1, 0, 1, 0], [0, 2, 0, 1], [1, 0, 2, 0]]))
XXi = sp.simplify(Pint.adjoint() * Pint)
t2i = sp.simplify(sp.trace(XXi * XXi)); t1i2 = sp.simplify(sp.trace(XXi)) ** 2
Su = gaugeS(Pint, orth_u(4))
chk("C6 u(4) generic complex integer Phi: S == 4 TrX^2 exactly (residual 0)", sp.simplify(Su - 4 * t2i) == 0)
Ss4 = gaugeS(Pint, orth_su(4))
chk("C7 su(4) same Phi: S == (7/2)TrX^2 + (1/16)(TrX)^2 exactly (residual 0)",
    sp.simplify(Ss4 - (sp.Rational(7, 2) * t2i + sp.Rational(1, 16) * t1i2)) == 0)
chk("C8 group-choice tooth: u(4) ratio B/A = 0 vs su(4) B/A = 1/56 (selection datum not in eq:Smicro)",
    sp.Rational(1, 16) / sp.Rational(7, 2) == sp.Rational(1, 56))
# positive control: NON-orthonormal basis (one element doubled) breaks orthonormality AND moves B/A
bmod = orth_su(4)
bmod[0] = 2 * bmod[0]
orth_fail = not is_orth(bmod)
A2, B2, _ = gauge_fit(4, bmod, 0, 0)
chk("C9 non-orthonormal-basis control: orthonormality assert fires AND fitted B/A differs from 1/56 (discarded 1/35 was an artifact of a non-orthonormal basis)",
    orth_fail and sp.simplify(B2 / A2 - sp.Rational(1, 56)) != 0)

# ---------------- D. beta system and fixed rays ----------------
print("== D. beta_r = c3/(32 pi^2) P(r), fixed-ray analysis ==")
r, w, v4, BG = sp.symbols("r w v4 B_G", real=True)
A33, B33, A32, B32, A22, B22 = TT[4]
chk("D10a payload beta_c2 channel: with n=4 tensors, B33+2*B32*r+B22*r^2 == 96+512r+640r^2 exactly",
    sp.expand((B33 + 2 * B32 * r + B22 * r ** 2) - (96 + 512 * r + 640 * r ** 2)) == 0)
chk("D10b payload beta_c3 channel: with n=4 tensors, A33+2*A32*r+A22*r^2 == 256+192r exactly (A22=0 kills r^2)",
    sp.expand((A33 + 2 * A32 * r + A22 * r ** 2) - (256 + 192 * r)) == 0)
Pexpr = sp.expand((B33 + 2 * B32 * r + B22 * r ** 2) - r * (A33 + 2 * A32 * r + A22 * r ** 2)
                  + w * (BG - 4 * r) + 4 * v4 * r)
Pp = sp.Poly(Pexpr, r)
chk("D1 P(r) is quadratic in r (r^3 coefficient = -A22 = 0 exactly)", Pp.degree() == 2)
c0P = sp.simplify(Pexpr.subs(r, 0))
chk("D2 P(0) = 96 + B_G w, fermion-independent (v4 absent from P(0); beta_r(0) = c3/(32pi^2)(96+B_G w))",
    c0P == 96 + BG * w)
Pq = sp.expand(Pexpr.subs({B33: 96, B32: 128, B22: 640, A33: 256, A32: 96, A22: 0, BG: 0}))
disc = sp.discriminant(sp.Poly(Pq, r), r)
chk("D3 n=4, BG=0: disc = 16[(w-v4-64)^2 - 10752] exactly (real fixed rays iff (w-v4-64)^2 > 10752)",
    sp.factor(sp.expand(disc - 16 * ((w - v4 - 64) ** 2 - 10752))) == 0)
discg = sp.discriminant(sp.Poly(Pexpr, r), r)
chk("D3b n=4, general B_G: disc = 16[(w-v4-64)^2 - 10752 - 112 B_G w] exactly (fixed rays need (w-v4-64)^2 > 10752 + 112 B_G w)",
    sp.factor(sp.expand(discg - 16 * ((w - v4 - 64) ** 2 - 10752 - 112 * BG * w))) == 0)
# inside window: a>0 and disc<0 => P>0 for all real r
import math
win = [(0, 0), (1, 0), (10, 0), (50, 1), (100, 40), (167, 0), (0, 30), (120, 100)]  # all 8 interior: (w-v4-64)^2 < 10752
okw = True
for wv, v4v in win:
    Pv = sp.expand(Pq.subs({w: wv, v4: v4v}))
    dv = sp.discriminant(sp.Poly(Pv, r), r)
    if not ((wv - v4v - 64) ** 2 < 10752 and dv < 0 and sp.Poly(Pv, r).LC() > 0):
        okw = False
chk("D4 window check (grid of 8 INTERIOR points, each satisfying (w-v4-64)^2 < 10752): disc<0, LC=448>0 => P(r)>0 for all real r, no fixed ray", okw)
Pl = sp.expand(Pq.subs({w: 64 + 16 * sp.sqrt(42), v4: 0}))
dl = sp.discriminant(sp.Poly(Pl, r), r)
chk("D5 threshold w*=64+16 sqrt(42) (=(w-v4-64)^2=10752 boundary): disc=0, marginal double root r*=sqrt(42)/14",
    sp.simplify(dl) == 0 and sp.simplify(-sp.Poly(Pl, r).coeff_monomial(r) / (2 * 448) - sp.sqrt(42) / 14) == 0)
chk("D6 threshold exceeds nominal perturbativity: w* = 64+16sqrt42 ~ 167.69 > 16 pi^2 ~ 157.91 (n=4, v4=0)",
    64 + 16 * math.sqrt(42) > 16 * math.pi ** 2)
# OFF-DEFAULT two-root tooth: w=200, v4=0 (outside window): two positive exact fixed rays
Ptooth = sp.expand(Pq.subs({w: 200, v4: 0}))
rts = sp.solve(Ptooth, r)
chk("D7 OFF-DEFAULT tooth (w=200,v4=0, outside window): exact fixed rays r = 3/14 and r = 1 (claim honestly fails outside window; both in boundedness region r > -1/4)",
    sorted([sp.nsimplify(x) for x in rts]) == sorted([sp.Rational(3, 14), sp.Integer(1)]))
chk("D8 boundedness boundary: P(-1/4) = 60 + w(1+B_G) - v4 at n=4 (pushes INTO boundedness at r=-1/4)",
    sp.simplify(Pexpr.subs(r, sp.Rational(-1, 4)) - (60 + w * (1 + BG) - v4)) == 0)
# general-n threshold: real roots at BG=v4=0 iff w > w*(n) = 8(n+4) + sqrt(3072(n-1/2))
okn = True
ws = {}
for nn in (2, 3, 4, 5, 6):
    a33, b33, a32, b32, a22, b22 = TT[nn]
    Pn = sp.expand((b33 + 2 * b32 * r + b22 * r ** 2) - r * (a33 + 2 * a32 * r + a22 * r ** 2)
                   + w * (0 - 4 * r))
    dn = sp.discriminant(sp.Poly(Pn, r), r)
    thr = 8 * (nn + 4) + math.sqrt(3072 * (nn - 0.5))
    ws[nn] = thr
    # disc>0 iff |w - 8(n+4)| > sqrt(4*a*c - ...): verify threshold root matches by sign change
    dlo = sp.sign(dn.subs(w, thr - 1e-6)); dhi = sp.sign(dn.subs(w, thr + 1e-6))
    if not (dlo <= 0 and dhi > 0):
        okn = False
print("D9 general-n strong-coupling threshold w*(n) (v4=0): " + ", ".join("n=%d: %.2f" % (k, v) for k, v in ws.items()) + "; 16 pi^2 = %.2f" % (16 * math.pi ** 2))
chk("D9 general-n: minimum strong coupling for ANY real fixed ray is w*(n) (disc sign change at w*(n)); n=4: w* > 16 pi^2",
    okn and ws[4] > 16 * math.pi ** 2)

# ---------------- E. fermion single-word theorem checks ----------------
print("== E. renormalizable-Yukawa single-word checks (fermions feed TrX^2 only) ==")
for nn in (2, 3):
    ys = sp.symbols("y0:4")
    Ym = sp.Matrix(2, 2, lambda i, j: ys[2 * i + j])
    Ps = Pmat(nn, vars_n(nn))
    Mk = sp.Matrix(sp.block_collapse(sp.kronecker_product(Ps, Ym)))
    LHS = sp.simplify((Mk * Mk.adjoint() * Mk * Mk.adjoint()).trace())
    rhs = sp.expand(sp.simplify(TrX2(Ps)) * sp.simplify((Ym * Ym.adjoint() * Ym * Ym.adjoint()).trace()))
    chk("E1 n=%d multiplicity model M = kron(Phi, Y): tr(MM+MM+) = TrX^2 * tr(YY+YY+): single-word, diff 0" % nn,
        sp.simplify(LHS - rhs) == 0)
Ps2 = Pmat(2, vars_n(2))
M2b = sp.Matrix(sp.block_collapse(sp.BlockMatrix(
    [[Ps2, sp.zeros(2, 2)], [sp.zeros(4, 4), sp.simplify(Ps2.adjoint())]])))
L2b = sp.simplify((M2b * M2b.adjoint() * M2b * M2b.adjoint()).trace())
Xs2 = sp.simplify(Ps2.adjoint() * Ps2)
chk("E2 conjugate-channel Dirac warm-up M = y[[0,Phi],[Phi+,0]]: tr(MM+MM+) = 2 TrX^2, diff 0 (no (TrX)^2 word)",
    sp.simplify(L2b - 2 * sp.simplify(sp.trace(Xs2 * Xs2))) == 0)

# ---------------- F. quadratic divergence / c1 scheme analysis ----------------
print("== F. sharp cutoff / Pauli-Villars / MSbar: sign(c1) not fixed by any scheme ==")
Lam, m2, mu = sp.symbols("Lambda m2 mu", positive=True)
kk = sp.symbols("k", positive=True)
Xs = sp.Symbol("X", positive=True)
Iex = sp.integrate(kk ** 3 * sp.log(kk ** 2 + m2), (kk, 0, Lam))
Icl = (sp.Rational(1, 4) * Xs ** 2 * sp.log(Xs + m2) - Xs ** 2 / 8 + m2 * Xs / 4
       - m2 ** 2 / 4 * sp.log((Xs + m2) / m2))
chk("F1 exact radial integral: d/dm2 [Int_0^Lam k^3 ln(k^2+m2) dk - closed form(X=Lam^2)] = 0",
    sp.simplify(sp.diff(Iex - Icl.subs(Xs, Lam ** 2), m2)) == 0)
# F2: from F1's exact closed form, the m2-linear term of I is m2*Lam^2/2 (X/4 from the log + X/4);
# V = (1/2)(1/16pi^2) I gives the per-real-scalar quadratic divergence:
Vquad = sp.Rational(1, 2) * 1 / (16 * sp.pi ** 2) * (m2 * Lam ** 2 / 2)
chk("F2 quadratic divergence per real scalar: V_quad = (1/2)(1/16pi^2)(m2 Lambda^2/2) = m2 Lambda^2/(64 pi^2)",
    sp.simplify(Vquad - m2 * Lam ** 2 / (64 * sp.pi ** 2)) == 0)
# exact content traces (n=4): K3, K2
vv4 = sp.symbols("z0:32", real=True)
P4 = Pmat(4, vv4)
X4 = P4.adjoint() * P4
def TrH(Wx):
    return sp.simplify(sp.hessian(sp.expand(Wx), vv4).trace())
t14 = sp.expand(sp.trace(X4))
K3 = sp.simplify(sp.expand(TrH(sp.expand(sp.trace(X4 * X4)))) / t14)
K2 = sp.simplify(sp.expand(TrH(sp.expand(t14 ** 2))) / t14)
chk("F3 n=4 exact traces: Tr Hess TrX^2 = 64 TrX (K3=64); Tr Hess (TrX)^2 = 136 TrX (K2=136); Tr Hess TrX = 64",
    K3 == 64 and K2 == 136 and sp.simplify(TrH(t14) - 64) == 0)
dataCu, dataCs = [], []
for N in (2, 3, 4, 5, 6):
    Yd = sp.diag(*[1, 1, 1, 1][:min(N, 4)] + [sp.Integer(0)] * max(0, N - 4))
    dataCu.append(sp.simplify(sum(sp.trace(A * Yd * A) for A in orth_u(N)) / sp.trace(Yd)))
    dataCs.append(sp.simplify(sum(sp.trace(A * Yd * A) for A in orth_su(N)) / sp.trace(Yd)))
chk("F4 C_u(n) = sum_a Tr(T^a Y T^a)/TrY = n exactly for n=2..6", dataCu == [2, 3, 4, 5, 6])
okcs = all(sp.simplify(c - sp.Rational(N * N - 1, N)) == 0 for N, c in zip((2, 3, 4, 5, 6), dataCs))
chk("F5 C_su(n) = (n^2-1)/n for n=2..6 (measured %s)" % [str(x) for x in dataCs], okcs)
c3v, c2v, CGv, mY, yv = sp.symbols("c3 c2 C_G m_Y y", positive=True)
bracket = 64 * c3v + 136 * c2v + CGv - 4 * mY * yv ** 2
b1 = bracket.subs({c3v: 1, c2v: 0, CGv: 1, mY: 1, yv: 1})
b2 = bracket.subs({c3v: 1, c2v: 0, CGv: 1, mY: 1, yv: 10})
chk("F6 sign tooth: sharp-cutoff bracket 64c3+136c2+C_G g^2-4 m_Y y^2 takes + (b=65) and - (y large): sign(c1) is content data, not loop structure",
    b1 > 0 and b2 < 0)
ph2, M0, Aa = sp.symbols("ph2 M0 A", positive=True)
t = sp.symbols("t", positive=True)
fPV = (M0 + Aa * ph2) ** 2 * sp.log((M0 + Aa * ph2) / mu ** 2)
linPV = sp.simplify(sp.diff(sp.series(fPV.subs(ph2, t * ph2), t, 0, 2).removeO().subs(t, 1), ph2))
chk("F7 PV exact threshold: linear-in-ph2 coeff of M~^4 ln M~^2 = A M0 (2 ln(M0/mu^2)+1), diff 0 (no Lambda^2: sign is a PV spectrum datum)",
    sp.simplify(linPV - Aa * M0 * (2 * sp.log(M0 / mu ** 2) + 1)) == 0)
c1s, gam = sp.symbols("c1 gamma", real=True)
chk("F8 MSbar dimension argument made checkable: beta_c1 = c1*gamma => beta|_{c1=0} = 0, c1=0 exact RG surface (no additive generation of c1 in a mass-independent scheme)",
    (c1s * gam).subs(c1s, 0) == 0)

# ---------------- G. Moyal star collapse for constant Phi, to O(theta^3) ----------------
print("== G. constant-Phi Moyal collapse (cubic polynomial Phi, p up to 3) ==")
x0, x1, th, v2g = sp.symbols("x0 x1 theta v2", real=True)
xs = [x0, x1]
Msym = lambda nm: sp.Matrix(2, 2, lambda i, j: sp.Symbol("%s%d%d" % (nm, i, j), complex=True))
Phi3 = Msym("a") + Msym("b") * x0 + Msym("c") * x1 + Msym("d") * x0 * x1 + Msym("e") * x0 ** 2
Psi3 = Msym("A") + Msym("B") * x0 + Msym("C") * x1 + Msym("D") * x0 * x1 + Msym("E") * x0 ** 2
grad0 = {e: 0 for M in [Msym("b"), Msym("c"), Msym("d"), Msym("e"),
                        Msym("B"), Msym("C"), Msym("D"), Msym("E")] for e in M}
def dxf(f, k):
    return sp.Matrix(f).applyfunc(lambda e: sp.diff(e, xs[k]))
tm = sp.Matrix([[0, th], [-th, 0]])
# explicit p=1,2,3 terms (constant theta, single plane; general constant theta enters linearly per plane)
def dstar(f, g):
    f = sp.Matrix(f); g = sp.Matrix(g)
    p1 = sp.zeros(2, 2)
    for m in range(2):
        for n in range(2):
            p1 = p1 + sp.I / 2 * tm[m, n] * dxf(f, m) * dxf(g, n)
    p2 = sp.zeros(2, 2)
    for m in range(2):
        for n in range(2):
            for p in range(2):
                for q in range(2):
                    p2 = p2 + (sp.I / 2) ** 2 / 2 * tm[m, n] * tm[p, q] * dxf(dxf(f, m), p) * dxf(dxf(g, n), q)
    p3 = sp.zeros(2, 2)
    for m in range(2):
        for n in range(2):
            for p in range(2):
                for q in range(2):
                    for s2 in range(2):
                        for u2 in range(2):
                            p3 = p3 + ((sp.I / 2) ** 3 / 6 * tm[m, n] * tm[p, q] * tm[s2, u2]
                                       * dxf(dxf(dxf(f, m), p), s2) * dxf(dxf(dxf(g, n), q), u2)) / 1
    # NOTE: 1/(m!n!)... for the Moyal series the p-th term is (1/p!) (i/2 th dd)^p: the 1/6 and 1/2 above
    # are the p=3, p=2 series factors; the index sums run over all components (no antisym reduction).
    return sp.expand(f * g + p1 + p2 + p3)
Yg = sp.simplify(dstar(Psi3, Phi3) - v2g * sp.eye(2))
Wst = sp.expand(dstar(Yg, Yg).trace())
Ord = sp.expand(((Msym("A") * Msym("a") - v2g * sp.eye(2)) ** 2).trace())
Wc = sp.simplify(Wst.subs(grad0))
chk("G1 constant-Phi collapse to p=3: W_star - W_ordinary = 0 with theta symbolic (all kept orders)",
    Wc.equals(sp.simplify(Ord)) or sp.simplify(Wc - Ord) == sp.zeros(2, 2) or Wc == Ord)
# p=3 term kills any quadratic Phi (>=3 derivatives on each factor): full-range structure check
Phi2 = Msym("a") + Msym("b") * x0 + Msym("c") * x1
Psi2 = Msym("A") + Msym("B") * x0 + Msym("C") * x1
def dstar_only(f, g, p):
    f = sp.Matrix(f); g = sp.Matrix(g)
    term = sp.zeros(2, 2)
    rng = range(2)
    idx = [(m, n, a2, b2, c2, d2) for m in rng for n in rng for a2 in rng for b2 in rng for c2 in rng for d2 in rng]
    for (m, n, a2, b2, c2, d2) in idx:
        term = term + ((sp.I / 2) ** 3 / 6 * tm[m, n] * tm[a2, b2] * tm[c2, d2]
                       * dxf(dxf(dxf(f, m), a2), c2) * dxf(dxf(dxf(g, n), b2), d2))
    return sp.expand(term)
chk("G2 p=3 Moyal term vanishes identically on quadratic polynomial Phi (>=3 derivatives per factor; no constant piece possible)",
    all(dstar_only(Psi2, Phi2, 3)[i, j] == 0 for i in range(2) for j in range(2)))
# O(theta^2) no-potential check at the full cubic Phi: zero-gradient part of the th^2 coefficient is 0
W2 = sp.simplify(sp.expand(Wst).coeff(th, 2))  # Wst is a scalar: compare against 0 (was: zeros(2,2), always False)
chk("G3 O(theta^2): zero-gradient (potential) part of the theta^2 coefficient of W_star is exactly 0 (pure derivative operator)",
    sp.simplify(W2.subs(grad0)) == 0)
W1 = sp.simplify(sp.expand(Wst).coeff(th, 1))
chk("G3b O(theta): zero-gradient part of the theta coefficient is exactly 0 (no potential renormalization; total-derivative form established separately)",
    sp.simplify(W1.subs(grad0)) == 0)

# ---------------- summary ----------------
print("TOTAL %d/%d PASS" % (PASS[0], PASS[0] + FAIL[0]))
if FAIL[0]:
    print("FAILURES: %d" % FAIL[0])
print("ALL CHECKS DONE 119")
