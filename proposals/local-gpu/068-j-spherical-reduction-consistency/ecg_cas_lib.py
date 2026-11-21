"""068-j-spherical-reduction-consistency: shared CAS library.

Conventions, derived from the manuscript before any computation:
- ch09 (after eq:ECG): signature (-,+,+,+); 'with the Riemann convention
  for which R > 0 on spheres'. eq:ECG invariant P = 12 R_a^c_b^d R_c^e_d^f
  R_e^a_f^b + R_ab^cd R_cd^ef R_ef^ab - 12 R_abcd R^ac R^bd
  + 8 R_a^b R_b^c R_c^a. eq:S-ECG: S = int d4x sqrt(-g) [ (R - 2 Lambda_eff)
  / (16 pi G_eff) + beta_ECG P ].
- appH (Problem J): reduced Lagrangian L[N,f] = N r^2 (R - 2 Lambda_eff
  + kappa P), kappa = 16 pi G_eff beta_ECG, per unit coordinate time and
  angular volume. The unique static spherical form with measure
  N r^2 sin(theta) is ds^2 = -N(r)^2 dt^2 + dr^2/f(r) + r^2 dOmega^2
  (reduces to eq:sss of ch13 at N = 1).
- Reduced coupling alpha = -kappa (appH; ch09: alpha = -16 pi G_eff
  beta_ECG; ch13).

Riemann convention used here:
  R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc}
              + Gamma^a_{ce} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{bc},
i.e. [nabla_c, nabla_d] v^a = R^a_{bcd} v^b. T0a enforces R(unit 2-sphere)
= +2, matching the manuscript statement; T1c pins the sign of the recovered
functional B[f] against the recorded one.

Index implementation of eq:ECG (cubic_P): the mixed factor is read as
R_a^c_b^d = g^{cp} g^{dq} R_{apbq} = M2[c,d,a,b] (the bivector map).  With
this reading the two chain terms of eq:ECG coincide as full index sums
(verified symbolically: c1 - c2 = 0), and the full index sum equals
8*tr(X^3) on the antisymmetric-pair basis (verified symbolically:
c1 - 8*trX3 = 0); the earlier 4*tr(X^3) factor was an implementation
error.  An alternative slot reading R_a^c_b^d := g^{cp} R^a_{p b d} is
also a scalar contraction but does NOT coincide with the second chain
term (verified nonzero difference), so the eq:ECG reading is
reading-sensitive; the literal scalar reading is the one implemented.
Validation anchors of the implementation: T0a (R = +2 on spheres),
T0b (R = 0 on the Schwarzschild profile), T0d (theta-independence of
P[N,f]), and the closed forms printed for P[1-2M/r] and P[N=1,f].
The recorded appH Problem-J identities are NOT reproduced by this
implementation; that is the bounded discrepancy recorded by checks
T1a/T1b/T1b2/T2b in stage1 (see proposal-r1.md), not a convention
validation.
"""
import sys
import time
import sympy as sp

t0 = time.time()
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='ascii', errors='backslashreplace')
    except Exception:
        pass


def hb(msg):
    print('[hb %.1f s] %s' % (time.time() - t0, msg), file=sys.stderr)
    sys.stderr.flush()


print('sympy %s python %s' % (sp.__version__, sys.version.split()[0]))

r = sp.symbols('r')
M, LAM, ALP, kap = sp.symbols('M Lambda_eff alpha kappa', real=True)
th, ph = sp.symbols('theta phi')
RESULTS = []
FAILS = []


def fn(name):
    return sp.Function(name)(r)


def report(tag, cond, dur=None):
    if dur is None:
        dur = time.time() - t0
    ok = bool(cond)
    RESULTS.append((tag, ok))
    if not ok:
        FAILS.append(tag)
    # stdout is the byte-reproducible record; wall-clock goes to stderr
    print('%s : %s' % (tag, 'PASS' if ok else 'FAIL'))
    print('[t=%.3f s] %s' % (dur, tag), file=sys.stderr)
    sys.stderr.flush()


def show(tag, expr):
    s = sp.srepr(expr) if len(str(expr)) > 800 else str(expr)
    print('%s: %s' % (tag, s))


def zero(expr):
    return sp.simplify(expr) == 0


# ---------------------------------------------------------------- geometry
def build_metric(gmat, coords):
    """coords: list of length n; the radial coordinate is coords[1].
    Rm[a,b,c,d] = R^a_{bcd}; RicL[b,d] = sum_a Rm[a,b,a,d];
    Rl[a,b,c,d] = g_{ae} Rm[e,b,c,d]; RicU[a,b] = g^{ae} RicL[e,b];
    RA[a,b] = g^{be} RicL[a,e] = R^a_b; M2[a,b,c,d] = g^{be} R^a_{e c d}."""
    n = len(coords)
    gL = sp.MutableDenseNDimArray(gmat, (n, n))
    Mg = sp.Matrix(n, n, lambda i, j: gL[i, j])
    gU = sp.MutableDenseNDimArray(list(Mg.inv()), (n, n))
    x = coords[1]

    def dd(expr, i):
        # partial derivative w.r.t. coords[i]; coords[i] may be the
        # non-symbol placeholder 0 for a cyclic coordinate with no
        # dependence (t), in which case the derivative vanishes.
        xi = coords[i]
        return 0 if not isinstance(xi, sp.Symbol) else sp.diff(expr, xi)
    Gamma = sp.MutableDenseNDimArray([0] * (n ** 3), (n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                Gamma[a, b, c] = sp.simplify(sp.Rational(1, 2) * sum(
                    gU[a, e] * (dd(gL[e, b], c) + dd(gL[e, c], b)
                                - dd(gL[b, c], e)) for e in range(n)))
    Rm = sp.MutableDenseNDimArray([0] * (n ** 4), (n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    term = (dd(Gamma[a, b, d], c) - dd(Gamma[a, b, c], d)
                            + sum(Gamma[a, c, e] * Gamma[e, b, d]
                                  - Gamma[a, d, e] * Gamma[e, b, c]
                                  for e in range(n)))
                    Rm[a, b, c, d] = 0 if term == 0 else sp.together(term)
    RicL = sp.MutableDenseNDimArray([0] * (n ** 2), (n, n))
    for b in range(n):
        for d in range(n):
            RicL[b, d] = sum(Rm[a, b, a, d] for a in range(n))
    Rscalar = sp.simplify(sp.together(sum(gU[b, d] * RicL[b, d]
                                          for b in range(n)
                                          for d in range(n))))
    Rl = sp.MutableDenseNDimArray([0] * (n ** 4), (n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    term = sum(gL[a, e] * Rm[e, b, c, d] for e in range(n))
                    Rl[a, b, c, d] = 0 if term == 0 else term
    RicU = sp.MutableDenseNDimArray([0] * (n ** 2), (n, n))
    for a in range(n):
        for b in range(n):
            term = sum(gU[a, e] * RicL[e, b] for e in range(n))
            RicU[a, b] = 0 if term == 0 else sp.together(term)
    RA = sp.MutableDenseNDimArray([0] * (n ** 2), (n, n))
    for a in range(n):
        for b in range(n):
            term = sum(gU[b, e] * RicL[a, e] for e in range(n))
            RA[a, b] = 0 if term == 0 else sp.together(term)
    M2 = sp.MutableDenseNDimArray([0] * (n ** 4), (n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    term = sum(gU[b, e] * Rm[a, e, c, d] for e in range(n))
                    M2[a, b, c, d] = 0 if term == 0 else term
    detgL = sp.simplify(Mg.det())
    return dict(gL=gL, gU=gU, Gamma=Gamma, Rm=Rm, Rl=Rl, M2=M2, RicL=RicL,
                RicU=RicU, RA=RA, Rscalar=Rscalar, detgL=detgL,
                sqrtg=sp.sqrt(detgL))


def cubic_P(gm):
    """eq:ECG invariant (ch09, eq:ecg):
    P = 12 R_a^c_b^d R_c^e_d^f R_e^a_f^b + R_ab^cd R_cd^ef R_ef^ab
        - 12 R_abcd R^ac R^bd + 8 R_a^b R_b^c R_c^a.
    Index implementation (reading recorded in the proposal): the mixed
    factor R_a^c_b^d = g^{cp} g^{dq} R_{apbq} = M2[c,d,a,b] (the
    bivector map), so book term1 and term2 are the same full
    contraction (the bivector-chain cube); a slot-shifted reading that
    still pairs all slots (g^{cp} R^a_{p b d}) is a different scalar (stage3
    T5c), while naive readings of the printed slots leave unpaired lower
    slots.  Chain is computed as 8*tr(X^3) on the antisymmetric-pair basis
    (M2 is antisymmetric in its first two slots for a Levi-Civita
    connection; verified symbolically, c1 - 8*trX3 = 0).
    T3 = sum Rl[a,b,c,d] RICU2[a,c] RICU2[b,d] with
    RICU2[a,c] = g^{ae} g^{cf} RicL[e,f] (both-index-raised Ricci, i.e.
    the book's R^{ac}); the mixed pairing RicU[a,c] = R^a_c would be a
    different contraction and was the source of an earlier theta-
    dependence failure; T4 = sum RA[a,b] RA[b,c] RA[c,a]."""
    n = gm['Rm'].shape[0]
    Rl, M2, RA, gU, RicL = gm['Rl'], gm['M2'], gm['RA'], gm['gU'], gm['RicL']
    R = range(n)
    pairs = [(i, j) for i in R for j in R if i < j]
    X = sp.zeros(len(pairs), len(pairs))
    for I, (a, b) in enumerate(pairs):
        for J, (c, d) in enumerate(pairs):
            X[I, J] = M2[a, b, c, d]
    m = len(pairs)
    # full index sum of M2[a,b,c,d] M2[c,d,e,f] M2[e,f,a,b] equals
    # 8*tr(X^3) on the antisymmetric-pair basis (verified symbolically)
    chain = 8 * sum(X[I, J] * X[J, K] * X[K, I]
                    for I in range(m) for J in range(m) for K in range(m))
    chain = sp.together(chain)
    RICU2 = sp.MutableDenseNDimArray([0] * (n ** 2), (n, n))
    for a in R:
        for c in R:
            t3 = sum(gU[a, e] * gU[c, f] * RicL[e, f]
                     for e in R for f in R)
            RICU2[a, c] = 0 if t3 == 0 else sp.together(t3)
    T3 = sum(Rl[a, b, c, d] * RICU2[a, c] * RICU2[b, d]
             for a in R for b in R for c in R for d in R)
    T4 = sum(RA[a, b] * RA[b, c] * RA[c, a] for a in R for b in R for c in R)
    return 12 * chain + chain - 12 * T3 + 8 * T4


def el(L, q, simp=sp.together):
    out = sp.diff(L, q) - sp.diff(sp.diff(L, q.diff(r)), r)
    q2 = q.diff(r, 2)
    if L.has(q2):
        out = out + sp.diff(sp.diff(L, q2), r, 2)
    return (out if simp is None else simp(out))


def maxd(expr, q):
    ds = [k for k in range(7) if expr.has(q.diff(r, k))]
    return max(ds) if ds else 0


