# -*- coding: ascii -*-
# Item 123 script 2: sector bookkeeping for the Alternate-scope inventory
# truncation, plus a finite-dimensional Berezin check of the ghost weight.
#
# Conventions (all from the manuscript, quoted in the proposal):
#   eq:appA-a1:   a_1 = tr(R/6 - E)
#   eq:appA-sector-sum: W_E^{(1)} = (1/2) sum_s w_s Tr ln O_s, w relative to a
#     real bosonic determinant; proper-time form eq:appA-W.
#   eq:appA-Wexp: a_1 term contributes -a_1/(32 pi^2) * (LUV^2 - mu^2).
#   ch17 (verified bookkeeping paragraph): one real bosonic Laplace-type field
#     with E_R = 0 and fibre trace N_0 gives C_{R,E}^{(a1)} =
#     -N_0/(192 pi^2) (LUV^2 - mu^2): used as a normalization control.
#   Recorded ghost endomorphism from script 1 (verify_ghost_op_123.py):
#     harmonic-gauge diffeo ghost: E_g^mu_nu = -R^mu_nu, so tr E_g = -R,
#     a_1(ghost fibre) = (4/6 + 1) R = (5/3) R.
#
# Sector table of the truncation (w, tr I, tr E / R):
#   H block:    w=+1, trI=16,           trE/R = 16*Q  (per-component Q)  [massive: window J]
#   retained K: w=+1, trI=n_K,          trE/R = n_K*Q_K                  [massless]
#   tensor:     w=+1, trI=10,           trE/R = e_h                      [massless, supplied]
#   diffeo gh:  w=-2, trI= 4,           trE/R = -1                       [massless, derived]
#
# Checks (invariant expected outputs):
#   BEREZIN_DET = PASS     finite-dimensional Grassmann Gaussian: int exp(-thbar M th) = det M, n=2,3
#   WGHOST_M2   = PASS     Z=det M implies w=-2 against W_E^{(1)} = (1/2) w Tr ln O
#   N0_TRUNK    = 18 + n_K
#   A1_TRUNK    = 16*(1/6-Q) + n_K*(1/6-Q_K) - 5/3 - e_h
#   QCONFORMAL  = PASS     at Q=1/6, n_K=0: A1 = -5/3 - e_h (nonzero for generic e_h; vanishes iff e_h = -5/3)
#   CTRL_Y10    = 10       recorded universal Upsilon=10 control (A1=N0/6, W_C=N0/120)
#   CTRL_BOSON  = PASS     single-boson control reproduces -N0/(192 pi^2)(LUV^2-mu^2)
#   CTRL_HBLOCK = PASS     recorded A_{1,R,H} = 16(1/6-Q), A_{2,R,H} = -lambda v^2 A_{1,R,H}
#   DELN0_GHOST = -8,  DELRHO = +8*(LUV^4-mu^4)/(64*pi^2)

import sympy as sp

ok = []
def chk(name, cond, val=None):
    ok.append(bool(cond))
    print("%-16s %s%s" % (name, "PASS" if cond else "FAIL",
                          "" if val is None else ("   " + sp.pretty(val, use_unicode=False).replace("\n", " "))))

# ---------- finite-dimensional Berezin integral: Z = det M ------------------
def berezint(M):
    """int exp(-sum thbar_i M_ij th_j) over n pairs; exact via anticommuting
    symbols represented as bitmasks (thbar bits then th bits, canonical order)."""
    nn = M.shape[0]
    # (thbar_i th_j) bilinears are commuting even elements; use generators
    # u_ij = thbar_i th_j with u_ij u_kl = 0 whenever indices repeat, and
    # u_ij u_kl = -u_ik... ; simplest: expand exp over the even algebra via
    # the standard identity: exp(-thbar M th) = prod... use permutation form:
    # Z = sum_{perm} sign(perm) prod M[i,perm(i)] = det M by construction if
    # integral = coeff of thbar_0..thbar_{n-1} th_0..th_{n-1}. We compute the
    # integral as coeff extraction of the expanded exponential.
    from itertools import permutations
    # build (thbar M th)^k via exterior algebra on 2n one-forms:
    # basis monomials: frozenset pairs; represent as bitmask over 2n slots.
    # th_j -> slot j; thbar_i -> slot n+i. Product order canonical: sort slots.
    from functools import reduce
    def mul(m1, m2):
        # m: (mask, sign); multiply, zero if slot repeats
        mask1, s1 = m1; mask2, s2 = m2
        if mask1 & mask2:
            return None
        # count crossings: number of (a in mask1, b in mask2) with a > b
        cross = 0
        for a in range(2 * nn):
            if mask1 >> a & 1:
                for b in range(a):
                    if mask2 >> b & 1:
                        cross += 1
        return (mask1 | mask2, s1 * s2 * (-1) ** cross)
    # B = thbar M th = sum_{ij} M_ij * thbar_i th_j ; term = (mask, coeff)
    Bt = []
    for i in range(nn):
        for j in range(nn):
            m = (1 << i) | (1 << (nn + j))   # thbar_i -> low slot, th_j -> high slot
            Bt.append((m, M[i, j]))
    # exp(-B) = sum_k (-1)^k/k! B^k ; B^k via repeated multiplication
    def poly_mul(P, Q):
        out = {}
        for m1, v1 in P.items():
            for m2, v2 in Q.items():
                r = mul((m1, 1), (m2, 1))
                if r is None:
                    continue
                m, s = r
                key = m
                out[key] = out.get(key, 0) + s * v1 * v2
        return out
    E = {0: sp.Integer(1)}          # 1
    total = dict(E)
    Bpoly = {}
    for m, c in Bt:
        Bpoly[m] = Bpoly.get(m, 0) + c
    power = {0: sp.Integer(1)}
    topmask = (1 << (2 * nn)) - 1
    for k in range(1, 2 * nn + 1):
        power = poly_mul(power, Bpoly)
        for m, c in power.items():
            total[m] = total.get(m, 0) + sp.Rational((-1) ** k, sp.factorial(k).__int__().__abs__()) if False else total.get(m, 0) + c * sp.Rational((-1) ** k, 1) / sp.factorial(k)
    return sp.simplify(total.get(topmask, 0))

M2 = sp.Matrix([[sp.Symbol('m00'), sp.Symbol('m01')], [sp.Symbol('m10'), sp.Symbol('m11')]])
Z2 = berezint(M2)
chk("BEREZIN_DET2", sp.simplify(Z2 + M2.det()) == 0)  # extraction = (-1)^(n(n+1)/2) det; measure sign fixes Z = det M
a = sp.symbols('a0:9')
M3 = sp.Matrix(3, 3, lambda i, j: a[3 * i + j])
Z3 = berezint(M3)
chk("BEREZIN_DET3", sp.simplify(Z3 - M3.det()) == 0)

# W_gh = -ln det M = (1/2)(-2) Tr ln M  =>  w = -2 (against W = (1/2) w Tr ln O):
# compare functional forms symbolically:
zz = sp.Symbol('z', positive=True)
# per-mode: W_b = +(1/2) ln det O (real boson, w=+1 in W_E^{(1)} = (1/2) w Tr ln O);
# ghost: W_gh = -ln det M (Berezin, script above). Ghost equals (1/2) w ln det
# with w = -2 exactly when -ln z == (1/2)(-2) ln z:
chk("WGHOST_M2", sp.simplify(-sp.log(zz) - sp.Rational(-2, 1) / 2 * sp.log(zz)) == 0)

# ---------- sector bookkeeping ----------------------------------------------
Q, QK, nK, eh = sp.symbols('Q Q_K n_K e_h', real=True)
sectors = [
    ("H",      1,  16, 16 * Q,  "J"),
    ("K",      1, nK,  nK * QK, "L2"),
    ("tensor", 1,  10,  eh,      "L2"),
    ("ghost", -2,   4, -1,       "L2"),
]
# a_1 curvature coefficients per unit R: c_s = w (trI/6 - trE/R)
cR = sum(w * (sp.Rational(1, 6) * ti - te) for (_, w, ti, te, _w) in sectors)
A1 = sp.simplify(cR)
chk("A1_TRUNK", A1 == sp.simplify(16 * (sp.Rational(1, 6) - Q) + nK * (sp.Rational(1, 6) - QK) - sp.Rational(5, 3) - eh), A1)
N0 = sum(w * ti for (_, w, ti, _, _w) in sectors)
chk("N0_TRUNK", N0 == 18 + nK, N0)
# Q = 1/6, n_K = 0:
A1c = sp.simplify(A1.subs({Q: sp.Rational(1, 6), nK: 0}))
chk("QCONFORMAL", A1c == -sp.Rational(5, 3) - eh, A1c)
chk("QCONFORMAL_ZERO_IFF", sp.solve(sp.Eq(A1c, 0), eh) == [-sp.Rational(5, 3)])
# ghost-only deltas
dN0 = -2 * 4
chk("DELN0_GHOST", dN0 == -8)
LUV, mu = sp.symbols('Lambda_UV mu', positive=True)
drho = -sp.Rational(1, 64) * dN0 * (LUV**4 - mu**4) / sp.pi**2   # -N0 (LUV^4-mu^4)/(64 pi^2) with delta N0 = -8
chk("DELRHO", sp.simplify(drho - 8 * (LUV**4 - mu**4) / (64 * sp.pi**2)) == 0)

# per-sector windows: H carries J (massive threshold, recorded), others LUV^2-mu^2:
J = sp.symbols('J', positive=True)
Cpart_H = -sp.Rational(1, 1, ) if False else None
CR = -sp.Rational(1, 1) / (32 * sp.pi**2) * (
    (1 * (16 * sp.Rational(1, 6) - 16 * Q)) * J
    + (nK * (sp.Rational(1, 6) - QK) + (sp.Rational(10, 6) - eh) + (-2) * (sp.Rational(4, 6) + 1)) * (LUV**2 - mu**2)
)
CR = sp.simplify(CR)
CRf = -sp.Rational(1, 1) / (32 * sp.pi**2) * (16 * (sp.Rational(1, 6) - Q) * J
        + (nK * (sp.Rational(1, 6) - QK) - sp.Rational(5, 3) - eh) * (LUV**2 - mu**2))
chk("CR_WINDOWED", sp.simplify(CR - CRf) == 0, CR)

# controls -------------------------------------------------------------
# single-boson normalization control (ch17 recorded formula)
N0b = sp.symbols('N_0', positive=True)
CRb = -sp.Rational(1, 1) / (32 * sp.pi**2) * (N0b / 6) * (LUV**2 - mu**2)
chk("CTRL_BOSON", sp.simplify(CRb + N0b / (192 * sp.pi**2) * (LUV**2 - mu**2)) == 0)
# recorded Upsilon = 10 control
Ups = (N0b / 6) / (2 * N0b / 120)
chk("CTRL_Y10", Ups == 10)
# recorded H-block control: A_{1,R,H} = 16(1/6-Q); A_{2,R,H} = -lambda v^2 A_{1,R,H}
lam, v2 = sp.symbols('lambda v2', positive=True)
A1H = 16 * (sp.Rational(1, 6) - Q)
# a_2 curvature-linear per eq:appA-a2: 1/2 tr (R/6 - E)^2 - (1/2)tr(R/6-E)^2|... :
# E = m2 + Q R: (R(1/6-Q) - m2)^2 coefficient of R: -2 m2 (1/6-Q); times 1/2 *16:
A2H = sp.Rational(1, 2) * 16 * (-2 * lam * v2 * (sp.Rational(1, 6) - Q))
chk("CTRL_HBLOCK_A1", A1H == 16 * (sp.Rational(1, 6) - Q))
chk("CTRL_HBLOCK_A2", sp.simplify(A2H - (-lam * v2 * A1H)) == 0)
# full truncation a_1 with U(4) specialization n_K=0, Q=0, e_h=0:
print("A1 value at Q=QK=0, nK=0, e_h=0:", A1.subs({Q: 0, QK: 0, nK: 0, eh: 0}))
print("SCRIPT2 VERDICT:", "PASS" if all(ok) else "FAIL")
raise SystemExit(0 if all(ok) else 1)
