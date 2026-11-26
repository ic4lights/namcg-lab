# verify_r120.py  (run: python -I -B verify_r120.py)
# Chain 120 stage-2 verifier: re-derives, across full parameter ranges and at boundary and
# degenerate points, every claim used in insert-commutator-lift-r1.tex. Independent code
# path from the scratch/120 stage-1 scripts (same mathematics, fresh machinery).
# Conventions: Moyal/Weyl star with constant real antisymmetric Theta^{mu nu} (contravariant),
# metric g = eta = diag(-1,1,1,1) raised/lowered numerically; embedding Xhat^mu = x^mu.I +
# Theta^{mu rho} A_rho with A_rho (LOWERED index) Hermitian matrix symbol; K^{ij} =
# theta^{a i} g_{a b} theta^{b j} (= (Th.T*g*Th)[i][j] here, def:matrix-coords-ext);
# X = Phi^dagger Phi; C = [Phi, Phi^dagger]; W1 = Tr(C^dagger C).
# Prints "TOTAL x/x PASS" and "ALL CHECKS DONE 120".
import hashlib
import io
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = [0]
FAIL = [0]


def chk(name, cond):
    cond = bool(cond)
    if cond:
        PASS[0] += 1
    else:
        FAIL[0] += 1
    print(("PASS " if cond else "FAIL ") + name)


# ---------------- payload artifact integrity ----------------
PAY = os.path.join(HERE, "insert-commutator-lift-r1.tex")
pay = io.open(PAY, "rb").read()
chk("P1 payload bytes=5287 sha1[:12]=a5aa77dc90a3",
    len(pay) == 5287 and hashlib.sha1(pay).hexdigest()[:12] == "a5aa77dc90a3")
try:
    ptxt = pay.decode("ascii")
    ok = True
except UnicodeDecodeError:
    ok = False
chk("P2 payload pure ASCII", ok)
chk("P3 payload CRLF lines, ends CRLF, no tab/BOM/$",
    ptxt.count("\r") == ptxt.count("\n") and ptxt.endswith("\r\n")
    and "\t" not in ptxt and "$" not in ptxt and not ptxt.startswith("\ufeff"))
chk("P4 no label/cite/Tr macros",
    "\\label" not in ptxt and "\\cite" not in ptxt and "\\Tr" not in ptxt)
import re
refs = set(re.findall(r"\\(?:eq)?ref\{([^}]*)\}", ptxt))
ALLOWED = {"eq:Smatrix", "eq:Dmu-Phi", "eq:Smicro", "eq:dictionary", "ass:dictionary",
           "def:matrix-coords-ext", "ass:emergent-op", "eq:V", "eq:vacuum-manifold",
           "eq:LUV-def", "sec:ch3-relate"}
chk("P5 refs subset of grep-confirmed unique labels: %d refs" % len(refs),
    refs <= ALLOWED)
MARK = ["[\\hat X^\\mu,\\Phi]_\\star=\\mathrm i\\Theta^{\\mu\\nu}(\\partial_\\nu\\Phi-\\mathrm i[A_\\nu,\\Phi]_\\star)",
        "-\\Theta^{\\mu\\nu}\\Phi A_\\nu",
        "proportional to \\(K^{\\mu\\nu}\\) of Definition~\\ref{def:matrix-coords-ext}",
        "W_1=\\operatorname{Tr}([\\Phi,\\Phi^\\dagger])^2",
        "\\((0,0)\\) for every group choice",
        "closes none of Problem~D, Problem~D1, or Problem~A"]
chk("P6 central claim strings present (6)", all(m in ptxt for m in MARK))
chk("P7 no process/status/priority/completion words",
    not any(w in ptxt.lower() for w in ("status", "priority", "completion", "todo", "fixme")))

# ---------------- Moyal machinery ----------------
xs = sp.symbols("x0:4")
g = sp.diag(-1, 1, 1, 1)
THSyms = {}
for i in range(4):
    for j in range(4):
        THSyms[(i, j)] = 0
for i, j in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
    s = sp.Symbol("t%d%d" % (i, j), real=True)
    THSyms[(i, j)] = s
    THSyms[(j, i)] = -s


def thmat(vals=None):
    """4x4 contravariant Theta as list-of-dicts? return dict (i,j)->expr."""
    if vals is None:
        return dict(THSyms)
    return vals


def mzero(n):
    return sp.zeros(n)


def mdiff(sym, a):
    """d/dx_a on symbol dict."""
    out = []
    for e, C in sym:
        if e[a]:
            e2 = list(e)
            e2[a] -= 1
            out.append((tuple(e2), C * e[a]))
    return out


def madd(*ss):
    out = []
    for s in ss:
        out.extend(s)
    return out


def mmul_scalar(sym, s):
    return [(e, C * s) for e, C in sym]


def star(F, G, Th, pmax=2):
    """Moyal star of two matrix-valued polynomial symbols (dict list), exact for
    deg F + deg G <= 3 (terms p<=2); here both operands deg<=2 so p<=2 suffices."""
    # p=0
    res = []
    for e1, C1 in F:
        for e2, C2 in G:
            e = tuple(a + b for a, b in zip(e1, e2))
            res.append((e, C1 * C2))
    d = D1op(F, G, Th)
    res = madd(res, mmul_scalar(d, sp.I / 2))
    d2 = D1op(d, G, Th) if False else D2op(F, G, Th)
    res = madd(res, mmul_scalar(d2, sp.Rational(-1, 8)))
    return res


def D1op(F, G, Th):
    out = []
    dF = [mdiff(F, a) for a in range(4)]
    dG = [mdiff(G, b) for b in range(4)]
    for a in range(4):
        for b in range(4):
            th = Th[(a, b)]
            if th == 0:
                continue
            for e1, C1 in dF[a]:
                for e2, C2 in dG[b]:
                    e = tuple(p + q for p, q in zip(e1, e2))
                    out.append((e, C1 * C2 * th))
    return out


def D2op(F, G, Th):
    out = []
    dF = [[mdiff(mdiff(F, a), c) for a in range(4)] for c in range(4)]
    dG = [[mdiff(mdiff(G, b), d) for b in range(4)] for d in range(4)]
    for a in range(4):
        for b in range(4):
            tab = Th[(a, b)]
            if tab == 0:
                continue
            for c in range(4):
                for d in range(4):
                    tcd = Th[(c, d)]
                    if tcd == 0:
                        continue
                    fac = tab * tcd
                    for e1, C1 in dF[c][a]:
                        for e2, C2 in dG[d][b]:
                            e = tuple(p + q for p, q in zip(e1, e2))
                            out.append((e, C1 * C2 * fac))
    return out


def simplify_sym(sym):
    acc = {}
    for e, C in sym:
        C = sp.expand(C)
        if e in acc:
            acc[e] = acc[e] + C
        else:
            acc[e] = C
    return [(e, C) for e, C in acc.items() if C != 0]  # Repair R2: coefficients are pre-expanded; heuristic simplify is the T5c black hole


def sym_matrix(sym, n):
    M = sp.zeros(n)
    for e, C in sym:
        for i in range(n):
            for j in range(n):
                M[i, j] += C[i, j] * mon(e)
    return sp.expand(M)


def mon(e):
    r = 1
    for a in range(4):
        r *= xs[a] ** e[a]
    return r


def dnu(sym, nu):
    return mdiff(sym, nu)


MONOS = [(0, 0, 0, 0)] + [tuple(1 if a == k else 0 for a in range(4)) for k in range(4)] + \
        [tuple(2 if a == k else 0 for a in range(4)) for k in range(4)] + \
        [tuple(int(a in (i, j)) for a in range(4)) for i in range(4) for j in range(i + 1, 4)]


def genmat(n, name):
    return sp.Matrix(n, n, lambda i, j: sp.Symbol("%s%d%d" % (name, i, j)))


def gmat(n, name):
    return sp.Matrix(n, n, lambda i, j: sp.Symbol("%s%d%d" % (name, i, j), real=True))


def xhat_sym(mu, Alo, Th, eA, n):
    """Xhat^mu = x^mu.I + Theta^{mu rho} A_rho, A_rho = Alo[rho] x^{eA}."""
    s = [(tuple(1 if a == mu else 0 for a in range(4)), sp.eye(n))]
    for rho in range(4):
        if Th[(mu, rho)] != 0:
            s.append((eA, Alo[rho] * Th[(mu, rho)]))
    return s


def bridge_pair(mu, eA, eP, n, Th, hermitA=False, vals=None):
    """LHS-RHS of the bridge identity for A = M x^eA (all four rho), Phi = N x^eP."""
    if hermitA:
        Ms = []
        for rho in range(4):
            H = gmat(n, "h%d" % rho)
            U = sp.Matrix(n, n, lambda i, j: sp.Symbol("u%d_%d%d" % (rho, i, j), complex=True))
            M = H + sp.I * (U + U.adjoint())
            Ms.append(M)
    else:
        Ms = [genmat(n, "m%d" % rho) for rho in range(4)]
    N = genmat(n, "p")
    Alo = Ms
    Xmu = xhat_sym(mu, Alo, Th, eA, n)
    Phi = [(eP, N)]
    LHS = madd(star(Xmu, Phi, Th), mmul_scalar(star(Phi, Xmu, Th), -1))
    RHS = []
    for nu in range(4):
        if Th[(mu, nu)] == 0:
            continue
        # partial_nu Phi
        t1 = dnu(Phi, nu)
        # [A_nu, Phi]_star
        Aonly = [(eA, Alo[nu])]
        br = madd(star(Aonly, Phi, Th), mmul_scalar(star(Phi, Aonly, Th), -1))
        inner = madd(t1, mmul_scalar(br, -sp.I))
        RHS = madd(RHS, mmul_scalar(inner, sp.I * Th[(mu, nu)] * g[nu, nu] if False else sp.I * Th[(mu, nu)]))
    diff = simplify_sym(madd(LHS, mmul_scalar(RHS, -1)))
    D = sym_matrix(diff, n)
    if vals is not None:
        D = D.subs(vals)
    return sp.simplify(D)


# ---- T2 bridge identity ----
ok = True
for mu in range(4):
    D = bridge_pair(mu, (1, 0, 0, 0), (0, 0, 0, 0), 2, THSyms)
    ok = ok and D == sp.zeros(2)
chk("T2a bridge identity symbolic Theta, A linear, Phi const, all mu, n=2 generic", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (0, 0, 0, 0), (0, 1, 0, 0), 2, THSyms)
    ok = ok and D == sp.zeros(2)
chk("T2b bridge identity symbolic Theta, A const, Phi linear, all mu", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (2, 0, 0, 0), (1, 1, 0, 0), 2, THSyms)
    ok = ok and D == sp.zeros(2)
chk("T2c bridge identity symbolic Theta, A quad, Phi mixed deg2, all mu", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (0, 0, 1, 0), (0, 0, 0, 2), 3, THSyms)
    ok = ok and D == sp.zeros(3)
chk("T2d bridge identity n=3 symbolic Theta, all mu", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (0, 1, 0, 1), (1, 1, 1, 1), 4, THSyms)
    ok = ok and D == sp.zeros(4)
chk("T2e bridge identity n=4 symbolic Theta, all mu", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (0, 0, 0, 2), (1, 0, 1, 0), 2, THSyms, hermitA=True)
    ok = ok and D == sp.zeros(2)
chk("T2f bridge identity Hermitian A, symbolic Theta, all mu, n=2", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (1, 1, 0, 0), (1, 0, 0, 0), 2, THSyms)
    ok = ok and D == sp.zeros(2)
chk("T2g bridge identity A mixed deg2, Phi linear, symbolic Theta, all mu", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (1, 0, 0, 0), (0, 0, 1, 1), 2, THSyms)
    ok = ok and D == sp.zeros(2)
chk("T2h bridge identity A linear, Phi mixed deg2, symbolic Theta, all mu", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (0, 0, 0, 0), (0, 0, 0, 1), 2, THSyms, hermitA=True)
    ok = ok and D == sp.zeros(2)
chk("T2i bridge identity Hermitian A const + Phi linear, all mu", ok)
ok = True
for mu in range(4):
    D = bridge_pair(mu, (0, 2, 0, 0), (0, 0, 0, 0), 2, THSyms)
    ok = ok and D == sp.zeros(2)
chk("T2j bridge identity A quad x2, Phi const, symbolic Theta, all mu", ok)
# ---- T2k: monomial-class sweep, numeric Theta (Integers), generic symbolic coeffs ----
ThN = dict(THSyms)
for (i, j), v in [((0, 1), 2), ((0, 2), 3), ((0, 3), 5), ((1, 2), 7), ((1, 3), 11), ((2, 3), 13)]:
    ThN[(i, j)] = sp.Integer(v)
    ThN[(j, i)] = sp.Integer(-v)
PAIRS = [(a, b) for a in MONOS[:5] for b in MONOS[:5]]
PAIRS += [(MONOS[k], (0, 0, 0, 0)) for k in range(5, 9)]
PAIRS += [((0, 0, 0, 0), MONOS[k]) for k in range(5, 9)]
PAIRS += [((1, 1, 0, 0), (1, 1, 0, 0)), ((0, 0, 1, 1), (1, 0, 1, 0)), ((2, 0, 0, 0), (0, 1, 2, 0))]
cnt = 0
ok = True
for (eA, eP) in PAIRS:
    for mu in range(4):
        D = bridge_pair(mu, eA, eP, 2, ThN)
        if D != sp.zeros(2):
            ok = False
            print("  fail pair", eA, eP, mu)
        cnt += 1
chk("T2k sweep %d monomial pairs x 4 mu, numeric Theta, generic coeffs, n=2" % cnt, ok)


def bridge_pair_hermPhi(mu, eA, eP, Th):
    n = 2
    Ms = [genmat(n, "m" + str(rho)) for rho in range(4)]
    pp, ss = sp.symbols("p s", real=True)
    qq = sp.Symbol("q", complex=True)
    N = sp.Matrix([[pp, qq], [sp.conjugate(qq), ss]])
    Xmu = xhat_sym(mu, Ms, Th, eA, n)
    Phi = [(eP, N)]
    LHS = madd(star(Xmu, Phi, Th), mmul_scalar(star(Phi, Xmu, Th), -1))
    RHS = []
    for nu in range(4):
        if Th[(mu, nu)] == 0:
            continue
        Aonly = [(eA, Ms[nu])]
        br = madd(star(Aonly, Phi, Th), mmul_scalar(star(Phi, Aonly, Th), -1))
        inner = madd(dnu(Phi, nu), mmul_scalar(br, -sp.I))
        RHS = madd(RHS, mmul_scalar(inner, sp.I * Th[(mu, nu)]))
    return sp.simplify(sym_matrix(simplify_sym(madd(LHS, mmul_scalar(RHS, -1))), n))


# ---- T2l: Theta = 0 boundary: LHS and RHS vanish separately ----
ThZ = {}
for k in THSyms:
    ThZ[k] = sp.Integer(0)
ok = True
for mu in range(4):
    N = genmat(2, "q")
    Xmu = [(tuple(1 if a2 == mu else 0 for a2 in range(4)), sp.eye(2))]
    Phi = [((1, 0, 0, 0), N)]
    L = sp.simplify(sym_matrix(simplify_sym(madd(star(Xmu, Phi, ThZ), mmul_scalar(star(Phi, Xmu, ThZ), -1))), 2))
    ok = ok and (L == sp.zeros(2))
chk("T2l Theta=0: star-commutator [x^mu.I, Phi(x)] vanishes for all mu (both sides 0)", ok)

# ---- T2m: degenerate (single-block, rank 2) Theta ----
ThR = {}
for i in range(4):
    for j in range(4):
        ThR[(i, j)] = sp.Integer(0)
e01 = sp.Symbol("e01", real=True)
ThR[(0, 1)] = e01
ThR[(1, 0)] = -e01
ok = True
for mu in range(4):
    D = bridge_pair(mu, (1, 2, 0, 0), (0, 0, 1, 0), 2, ThR)
    ok = ok and D == sp.zeros(2)
chk("T2m bridge identity for degenerate rank-2 Theta (single block), all mu", ok)

# ---- T2n: Phi Hermitian-structured and general, symbolic Theta ----
ok = True
for mu in range(4):
    D = bridge_pair_hermPhi(mu, (0, 0, 0, 0), (0, 0, 0, 1), THSyms)
    ok = ok and D == sp.zeros(2)
for mu in range(4):
    D = bridge_pair_hermPhi(mu, (1, 0, 0, 0), (1, 0, 0, 0), THSyms)
    ok = ok and D == sp.zeros(2)
chk("T2n bridge identity with Hermitian-structured Phi (real diag, conj offdiag), const+linear A", ok)
# ---- T3: printed left action is incompatible: mismatch = -Theta^{mu nu} Phi *_star A_nu ----
def left_action_mismatch(mu, eA, eP, n, Th):
    Ms = [genmat(n, "m" + str(rho)) for rho in range(4)]
    N = genmat(n, "p")
    Xmu = xhat_sym(mu, Ms, Th, eA, n)
    Phi = [(eP, N)]
    LHS = madd(star(Xmu, Phi, Th), mmul_scalar(star(Phi, Xmu, Th), -1))
    RHSla = []
    tgt = sp.zeros(n)
    for nu in range(4):
        if Th[(mu, nu)] == 0:
            continue
        Aonly = [(eA, Ms[nu])]
        # printed: i Theta^{mu nu} D_nu Phi with D = d - i A (left action)
        #      = i Theta d(Phi) + Theta (A *_star Phi)
        term = madd(mmul_scalar(dnu(Phi, nu), sp.I), star(Aonly, Phi, Th))
        RHSla = madd(RHSla, mmul_scalar(term, Th[(mu, nu)]))
        tgt = tgt + sp.expand(Th[(mu, nu)]) * sym_matrix(star(Phi, Aonly, Th), n)
    Diff = sp.simplify(sym_matrix(simplify_sym(madd(LHS, mmul_scalar(RHSla, -1))), n))
    return sp.simplify(Diff + tgt), Diff, N, Ms


ok = True
for mu in range(4):
    for (eA, eP, n) in [((1, 0, 0, 0), (0, 0, 0, 0), 2), ((0, 0, 1, 0), (2, 0, 0, 0), 2),
                        ((0, 0, 0, 0), (0, 1, 0, 0), 3), ((1, 1, 0, 0), (1, 0, 0, 0), 2)]:
        resid, _, _, _ = left_action_mismatch(mu, eA, eP, n, THSyms)
        ok = ok and resid == sp.zeros(n)
chk("T3a LHS - printed-left-action-RHS = -Theta^{mu nu}(Phi *_star A_nu) exactly (4 classes x 4 mu)", ok)

# for constant Phi the star product is the ordinary product: mismatch = -Theta Phi A
resid0, D0, N0, M0 = left_action_mismatch(0, (1, 0, 0, 0), (0, 0, 0, 0), 2, THSyms)
tgt0 = sp.zeros(2)
for nu in range(4):
    tgt0 = tgt0 - sp.expand(THSyms[(0, nu)] * mon((1, 0, 0, 0)) * (N0 * M0[nu]))
chk("T3a2 constant Phi: mismatch equals the right-action product -Theta^{0 nu} Phi A_nu exactly",
    sp.expand(D0 - tgt0) == sp.zeros(2))
chk("T3a3 teeth: this mismatch is nonzero for generic data (no commutator produces it)",
    D0 != sp.zeros(2))

# u(1) invisibility at dictionary order: with A_nu = alpha_nu I the ordinary
# commutator [A_nu, Phi] = 0, while the printed connection term A_nu Phi is nonzero.
ok = True
aa = [sp.Symbol("al" + str(r), complex=True) for r in range(4)]
Nu = genmat(2, "p")
for nu in range(4):
    Acomm = aa[nu] * sp.eye(2) * Nu - Nu * aa[nu] * sp.eye(2)
    ok = ok and sp.simplify(Acomm) == sp.zeros(2)
    ok = ok and (aa[nu] * sp.eye(2) * Nu != sp.zeros(2))
chk("T3b central u(1) part invisible to commutators but nonzero in printed left action", ok)


def Kmat(Th, conv="Kdef"):
    Tm = sp.Matrix(4, 4, lambda a, b: Th[(a, b)])
    if conv == "Kdef":
        return sp.expand(Tm * g * Tm)
    return sp.expand(Tm.T * g * Tm)


# ---- T4a: kinetic tensor of the shift-symmetric lift is proportional to K exactly ----
Ys = [genmat(2, "y" + str(c)) for c in range(4)]
Bm = []
for mu in range(4):
    Gm = sp.zeros(2)
    for c in range(4):
        for b in range(4):
            if g[mu, c] * THSyms[(c, b)] != 0:
                Gm = Gm + g[mu, c] * THSyms[(c, b)] * Ys[b]
    Bm.append(sp.I * sp.expand(Gm))
liftq = sp.expand(sum(-sp.Rational(1, 2) * g[mu, nu] * (Bm[mu] * Bm[nu]).trace()
                      for mu in range(4) for nu in range(4)))
Kd = Kmat(THSyms)
targetq = sp.expand(sum(sp.Rational(-1, 2) * Kd[b, d] * (Ys[b] * Ys[d]).trace()
                        for b in range(4) for d in range(4)))
chk("T4a lift kinetic form = -(kappa/2) K^{bd} Tr(d_b Phi d_d Phi) exactly, symbolic Theta (kappa=1)",
    sp.expand(liftq - targetq) == 0)

Ks = Kmat(THSyms, "Ksym")
chk("T4b K = Theta g Theta symmetric; other index convention Theta^T g Theta = -K",
    (Kd - Kd.T) == sp.zeros(4) and (Ks + Kd.T) == sp.zeros(4))

# ---- T4c: K = c g forces Theta = 0 (real): explicit sum-of-squares certificate ----
cc = sp.Symbol("c", real=True)
Q0 = THSyms[(0, 1)] ** 2 + THSyms[(0, 2)] ** 2 + THSyms[(0, 3)] ** 2
cval = -Kd[0, 0]
chk("T4c1 K00 + c = 0 gives c = sum (Theta0i)^2 >= 0", sp.expand(cval - Q0) == 0)
F = [sp.expand(Kd[i, i] - cval) for i in (1, 2, 3)]
sq = [THSyms[(0, 2)] ** 2 + THSyms[(0, 3)] ** 2 + THSyms[(1, 2)] ** 2 + THSyms[(1, 3)] ** 2,
      THSyms[(0, 1)] ** 2 + THSyms[(0, 3)] ** 2 + THSyms[(1, 2)] ** 2 + THSyms[(2, 3)] ** 2,
      THSyms[(0, 1)] ** 2 + THSyms[(0, 2)] ** 2 + THSyms[(1, 3)] ** 2 + THSyms[(2, 3)] ** 2]
ok = all(sp.expand(F[i] + sq[i]) == 0 for i in range(3))
Qall = sum((THSyms[(i, j)]) ** 2 for i in range(4) for j in range(i + 1, 4))
ok = ok and sp.expand(sum(F) + 2 * Qall) == 0
chk("T4c2 Kii - c = -(sum of squares) and sum = -2|Theta|^2: K = c g only real sol Theta=0, c=0", ok)

# ---- T4d: canonical block data K = diag(-e^2, e^2, -b^2, -b^2) ----
ee, bb = sp.symbols("e b", real=True)
ThB = {}
for i in range(4):
    for j in range(4):
        ThB[(i, j)] = sp.Integer(0)
ThB[(0, 1)] = ee
ThB[(1, 0)] = -ee
ThB[(2, 3)] = bb
ThB[(3, 2)] = -bb
KB = Kmat(ThB)
chk("T4d canonical K = Theta g Theta = diag(-e^2, e^2, -b^2, -b^2)",
    KB == sp.diag(-ee ** 2, ee ** 2, -bb ** 2, -bb ** 2))

# ---- T4e: numeric teeth: K not g-proportional at generic blocks ----
ThX = {}
for i in range(4):
    for j in range(4):
        ThX[(i, j)] = sp.Integer(0)
for (i, j), v in [((0, 1), 2), ((2, 3), 3)]:
    ThX[(i, j)] = sp.Integer(v)
    ThX[(j, i)] = sp.Integer(-v)
KX = Kmat(ThX)
chk("T4e teeth (t01,t23)=(2,3): K00*g22 - K22*g00 = -13 != 0 (not g-proportional)",
    KX[0, 0] * g[2, 2] - KX[2, 2] * g[0, 0] == -13)

# ---- T4g: purely spatial Theta: row/col 0 of K vanish and det K = 0 ----
s12, s13, s23 = sp.symbols("s12 s13 s23", real=True)
ThS = {}
for i in range(4):
    for j in range(4):
        ThS[(i, j)] = sp.Integer(0)
for (i, j), sv in [((1, 2), s12), ((1, 3), s13), ((2, 3), s23)]:
    ThS[(i, j)] = sv
    ThS[(j, i)] = -sv
KSp = Kmat(ThS)
chk("T4g spatial Theta: K^{0 mu} = 0 (no time-derivative term) and det K = 0 (degenerate)",
    all(KSp[0, m] == 0 and KSp[m, 0] == 0 for m in range(4)) and sp.expand(KSp.det()) == 0)
# ---- T5: frame-mode blindness of the class ----
def mmulp(f, gg):
    out = []
    for e1, C1 in f:
        for e2, C2 in gg:
            e = tuple(a + b for a, b in zip(e1, e2))
            out.append((e, C1 * C2))
    return out


def polymat(f, n):
    return sym_matrix(simplify_sym(f), n)


def e4(k):
    return tuple(1 if j == k else 0 for j in range(4))


a0 = sp.Symbol("a0", complex=True)
aq = [sp.Symbol("aq" + str(j), complex=True) for j in range(4)] + \
     [sp.Symbol("aq" + str(j) + str(j), complex=True) for j in range(4)] + [sp.Symbol("aq12", complex=True)]
TERMS = [((0, 0, 0, 0), a0)] + [(e4(j), aq[j]) for j in range(4)] + \
        [(tuple(2 if k == j else 0 for k in range(4)), aq[4 + j]) for j in range(4)] + [((1, 1, 0, 0), aq[8])]


def frame_bracket(mu, Adeg, terms, Th, n, shift=0):
    Ms = [genmat(n, "m" + str(rho)) for rho in range(4)]
    Xmu = xhat_sym(mu, Ms, Th, Adeg, n)
    phi = [(e, c * sp.eye(n)) for (e, c) in terms]
    if shift != 0:
        phi = madd(phi, [((0, 0, 0, 0), shift * sp.eye(n))])
    B = madd(star(Xmu, phi, Th), mmul_scalar(star(phi, Xmu, Th), -1))
    return sp.simplify(polymat(B, n)), Ms


ok = True
for mu in range(4):
    B, Ms = frame_bracket(mu, (1, 0, 0, 0), TERMS, THSyms, 2)
    Xmu = xhat_sym(mu, Ms, THSyms, (1, 0, 0, 0), 2)
    phiM = [(e, c * sp.eye(2)) for (e, c) in TERMS]
    dX = [mdiff(Xmu, aa) for aa in range(4)]
    dph = [mdiff(phiM, bb) for bb in range(4)]
    exp_list = []
    for aa in range(4):
        for bb in range(4):
            if THSyms[(aa, bb)] == 0:
                continue
            exp_list = madd(exp_list, mmul_scalar(mmulp(dX[aa], dph[bb]), sp.I * THSyms[(aa, bb)]))
    E = sp.simplify(polymat(exp_list, 2))
    ok = ok and (sp.expand(B - E) == sp.zeros(2))
chk("T5a [Xhat^mu, phi0(x) I]_star = i Theta^{ab} d_a Xhat^mu d_b phi0 I exactly (quadratic phi0, linear A)", ok)

B1, _ = frame_bracket(2, (1, 0, 0, 0), TERMS, THSyms, 2)
B2, _ = frame_bracket(2, (1, 0, 0, 0), TERMS, THSyms, 2, shift=sp.Symbol("sframe", complex=True))
chk("T5b frame bracket invariant under phi0 -> phi0 + const (frame only derivative-coupled)",
    sp.simplify(B2 - B1) == sp.zeros(2))


def lift_full(Phi_list, Asym, Th, n, Adeg=(1, 0, 0, 0)):
    Bs = []
    for mu in range(4):
        Xmu = xhat_sym(mu, Asym, Th, Adeg, n)
        Bmu = madd(star(Xmu, Phi_list, Th), mmul_scalar(star(Phi_list, Xmu, Th), -1))
        Bs.append(Bmu)
    tot = 0
    for mu in range(4):
        for nu in range(4):
            Sb = star(Bs[mu], Bs[nu], Th)
            tot = tot + (-sp.Rational(1, 2)) * g[mu, nu] * polymat(Sb, n).trace()
    return sp.expand(tot)


n = 2
Pc = [genmat(n, "c1"), genmat(n, "c2"), genmat(n, "c3"), genmat(n, "c4"), genmat(n, "c5"),
      genmat(n, "c6"), genmat(n, "c7")]
Phi_q = [((0, 0, 0, 0), Pc[0])] + [(e4(j), Pc[1 + j]) for j in range(4)] + \
        [(tuple(2 if k == j else 0 for k in range(4)), Pc[5 + j]) for j in range(2)]
Asym = [genmat(n, "M" + str(r)) for r in range(4)]
# Repair R1 (check-side, S2-final): the chunk-assembled T5c computed
# L1 = lift_full(...) and L2 = lift_full(...) and then sp.simplify(L2 - L1) on
# the fully EXPANDED difference: 16 truncated-star products of 2x2 matrices
# whose entries are quartic polynomials in 44 generic symbols; does not
# terminate in reasonable time (30+ min, 0-byte captures; blowup in
# sp.expand/Add). Rewrite verifies the IDENTICAL claim exactly: brackets
# compared exactly after simplify_sym, lift difference taken on the UNEXPANDED
# sums (identical unexpanded sums cancel in sympy Add without expand).
# Non-vacuity tooth added: a NON-scalar constant shift must change brackets.
# Claim string and inputs (generic quadratic Phi, linear A, numeric Theta) kept.
def brackets_full(Phi_list, Asym_, Th_, n_, Adeg=(1, 0, 0, 0)):
    Bs = []
    for mu in range(4):
        Xmu = xhat_sym(mu, Asym_, Th_, Adeg, n_)
        Bs.append(madd(star(Xmu, Phi_list, Th_), mmul_scalar(star(Phi_list, Xmu, Th_), -1)))
    return Bs
def lift_from_B(Bs, Th_, n_):
    tot = 0
    for mu in range(4):
        for nu in range(4):
            if g[mu, nu] == 0:
                continue
            Sb = star(Bs[mu], Bs[nu], Th_)
            tot = tot + (-sp.Rational(1, 2)) * g[mu, nu] * polymat(Sb, n_).trace()
    return tot
def mats_eq(Ba, Bb, n_):
    return sp.simplify(polymat(Ba, n_) - polymat(Bb, n_)) == sp.zeros(n_)
Bs1 = brackets_full(Phi_q, Asym, ThN, n)
Phi_q2 = madd(Phi_q, [((0, 0, 0, 0), sp.Symbol("ss", complex=True) * sp.eye(n))])
Bs2 = brackets_full(Phi_q2, Asym, ThN, n)
# Repair R3 (check-side, S2-final; verify_repair_log.txt): full generic-symbolic lift
# evaluation is intractable in this representation (probe_t5c.py, out-probe-t5c.txt:
# ~50 min per lift_from_B call on 21100-entry star lists). Since lift_from_B is a
# deterministic program in the four bracket polynomials, L(Phi + s I) = L(Phi) exactly
# follows from exact equality of the bracket polynomials (mats_eq: simplify of the
# difference of the 2x2 polynomial matrices == 0), plus substitutivity of equality.
# Six deterministic integer draws of the generic coefficient symbols additionally
# evaluate both lifts numerically with identical substitutions per draw. Claim string
# and input class (generic quadratic Phi, linear A, numeric Theta) unchanged.
eq_br = all(mats_eq(Ba, Bb, n) for Ba, Bb in zip(Bs1, Bs2))
DR = [-7, -3, 2, 5, 11, -13]
GENS = sorted({s for M in Pc + Asym for s in M.atoms(sp.Symbol)}, key=str)
def draw_reps(k):
    return {s: sp.Integer(DR[(i + k) % len(DR)]) for i, s in enumerate(GENS)}
def lift_at(Bs_raw, reps):
    Bs_sub = [[(e, C.xreplace(reps)) for e, C in B] for B in Bs_raw]
    return lift_from_B(Bs_sub, ThN, n)
ok_draws = True
for k in range(6):
    rp = draw_reps(k)
    ok_draws = ok_draws and (lift_at(Bs1, rp) == lift_at(Bs2, rp))
chk("T5c full star lift: L(Phi + s I) - L(Phi) = 0 exactly (quadratic Phi, linear A, numeric Theta)",
    eq_br and ok_draws)
Phi_q3 = madd(Phi_q, [((0, 0, 0, 0), sp.Symbol("snc", complex=True) * sp.diag(1, 0))])
Bs3 = brackets_full(Phi_q3, Asym, ThN, n)
chk("T5c-teeth: non-scalar constant shift changes the brackets (control: T5c non-vacuous)",
    not all(mats_eq(Ba, Bb, n) for Ba, Bb in zip(Bs1, Bs3)))

# T5d: frame mode phi0(x) I: quadratic lift coefficient is exactly -K (derivative coupling only)
phi0M = [(e, c * sp.eye(n)) for (e, c) in TERMS]
Lf = lift_full(phi0M, [sp.zeros(n) for r in range(4)], THSyms, n)
dphiM = [mdiff(phi0M, bb) for bb in range(4)]
tgtf = 0
for b in range(4):
    for d in range(4):
        if Kd[b, d] == 0:
            continue
        pb = polymat(dphiM[b], n)[0, 0]
        pd = polymat(dphiM[d], n)[0, 0]
        tgtf = tgtf + sp.Rational(-1, 2) * Kd[b, d] * 2 * sp.expand(pb * pd)
chk("T5d frame-mode lift = -(kappa/2) K^{bd} d_b phi0 d_d phi0 Tr(I) exactly (frame couples only via K)",
    sp.expand(Lf - tgtf) == 0)

# T5e: no mass term: at A = 0 a constant Phi has zero bracket and zero lift (any Theta)
zeroA = [sp.zeros(n) for r in range(4)]
Phi_c = [((0, 0, 0, 0), genmat(n, "ph0"))]
ok = True
for mu in range(4):
    Xmu = xhat_sym(mu, zeroA, THSyms, (0, 0, 0, 0), n)
    Bmu = madd(star(Xmu, Phi_c, THSyms), mmul_scalar(star(Phi_c, Xmu, THSyms), -1))
    ok = ok and sp.simplify(polymat(Bmu, n)) == sp.zeros(n)
Lc = lift_full(Phi_c, zeroA, THSyms, n)
chk("T5e A=0: constant Phi has zero bracket (all mu) and zero lift: class supplies no mass term",
    ok and sp.simplify(Lc) == 0)

# T5f: Phi = v I (v real const): bracket vanishes for ANY A (vacuum is in the blind kernel):
# hence the gauge-quartic (seagull) coupling vanishes at Phi = v I: no gauge-boson mass.
vv = sp.Symbol("v", real=True)
Phi_v = [((0, 0, 0, 0), vv * sp.eye(n))]
ok = True
for mu in range(4):
    Xmu = xhat_sym(mu, Asym, THSyms, (1, 0, 0, 0), n)
    Bmu = madd(star(Xmu, Phi_v, THSyms), mmul_scalar(star(Phi_v, Xmu, THSyms), -1))
    ok = ok and sp.simplify(polymat(Bmu, n)) == sp.zeros(n)
Lv = lift_full(Phi_v, Asym, THSyms, n)
# teeth: generic constant Phi does NOT give zero bracket when A != 0 (seagull exists off vacuum)
Xteeth = xhat_sym(0, Asym, THSyms, (1, 0, 0, 0), n)
Phi_g = [((0, 0, 0, 0), genmat(n, "pg"))]
Bteeth = madd(star(Xteeth, Phi_g, THSyms), mmul_scalar(star(Phi_g, Xteeth, THSyms), -1))
chk("T5f Phi=v I: bracket and lift vanish for any A (quartic gauge coupling vanishes on vacuum); teeth: generic constant Phi off-vacuum has nonzero bracket",
    ok and sp.simplify(Lv) == 0 and sp.simplify(polymat(Bteeth, n)) != sp.zeros(n))
# ---- T6: W1 = Tr([Phi, Phi^dagger])^2 sector ----
def cmat(n, tag):
    R = sp.Matrix(n, n, lambda i, j: sp.Symbol("R" + tag + str(i) + str(j), real=True))
    Ii = sp.Matrix(n, n, lambda i, j: sp.Symbol("I" + tag + str(i) + str(j), real=True))
    return R + sp.I * Ii


def Cfun(M):
    return sp.expand(M * M.adjoint() - M.adjoint() * M)


def Wfun(M):
    C = Cfun(M)
    return sp.expand((C.adjoint() * C).trace())


Phi2 = cmat(2, "a")
C2 = Cfun(Phi2)
W2 = Wfun(Phi2)
ok = (sp.simplify(C2.adjoint() - C2) == sp.zeros(2))
ok = ok and (sp.simplify(W2 - (C2 * C2).trace()) == 0)
chk("T6a C = [Phi, Phi^dagger] Hermitian and W1 = Tr(C^2) = Tr(C^dagger C), generic complex n=2", ok)

samples = [sp.Matrix([[1, 2], [3, 4]]), sp.Matrix([[1 + sp.I, 2], [3, 4 - sp.I]]),
           sp.Matrix([[0, 5], [0, 0]]), sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[1, 2], [2, 1]]),
           sp.Matrix([[sp.I, 1 + sp.I], [0, 2 * sp.I]]), sp.Matrix([[3, 3], [3, 3]])]
ok = True
nz = 0
for M in samples:
    wv = sp.simplify(Wfun(M))
    Cj = Cfun(M)
    ok = ok and bool(wv.is_real) and (wv >= 0)
    ok = ok and (wv == sp.simplify((Cj.adjoint() * Cj).trace()))
    if wv != 0:
        nz += 1
ok = ok and nz == 4
for k in (3, 4, 6):
    ok = ok and (sp.simplify(Wfun(samples[k])) == 0)
for k in (0, 1, 2, 5):
    ok = ok and (sp.simplify(Wfun(samples[k])) > 0)
chk("T6b numeric teeth: W1 real >= 0 on 7 fixed matrices; > 0 on the 4 nonnormal, = 0 on the 3 normal", ok)

pp = sp.Symbol("pp", positive=True)
Wnil = sp.simplify(Wfun(sp.Matrix([[0, pp], [0, 0]])))
ok = (Wnil == 2 * pp ** 4)
ok = ok and (sp.simplify(Wfun(sp.Matrix([[pp, 0], [0, 2 * pp]]))) == 0)
chk("T6c nilpotent Phi=[[0,p],[0,0]]: W1 = 2 p^4 > 0; diagonal Phi: W1 = 0", ok)

aa, bb2 = sp.symbols("aa bb2", complex=True)
vv = sp.Symbol("vv", positive=True)
U2 = sp.Matrix([[aa, bb2], [-bb2.conjugate(), aa.conjugate()]])
ok = (sp.simplify(Wfun(vv * U2)) == 0)
H4 = sp.Rational(1, 2) * sp.Matrix([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]])
ok = ok and (H4 * H4 == sp.eye(4))
ok = ok and (sp.simplify(Wfun(vv * H4)) == 0)
H4t = H4.copy()
H4t[0, 1] = H4t[0, 1] + 1
ok = ok and (sp.simplify(Wfun(vv * H4t)) != 0)
chk("T6d W1 vanishes on v.U(2) (generalized unitary) and on v times rational orthogonal 4x4; teeth off-vacuum nonzero", ok)


def shift_variant(M, s):
    return sp.simplify(Cfun(M + s * sp.eye(M.rows)) - Cfun(M))


s2 = sp.Symbol("s2r", real=True) + sp.I * sp.Symbol("s2i", real=True)
s3 = sp.Symbol("s3r", real=True) + sp.I * sp.Symbol("s3i", real=True)
Phi3 = cmat(3, "b")
ok = (shift_variant(Phi2, s2) == sp.zeros(2))
ok = ok and (shift_variant(Phi3, s3) == sp.zeros(3))
chk("T6e C(Phi + s I) = C(Phi) exactly for generic complex Phi, n=2 and n=3 (W1 shift-invariant)", ok)

# ---- independent z/zc formalism: exact nullspace tests for shift invariants ----
zz = sp.Matrix(2, 2, lambda i, j: sp.Symbol("z" + str(i) + str(j), complex=True))
zzd = sp.Matrix(2, 2, lambda i, j: sp.Symbol("c" + str(i) + str(j), complex=True))
ss = sp.Symbol("ss", complex=True)
ssc = sp.Symbol("cc", complex=True)
zl = [zz[i, j] for i in range(2) for j in range(2)]
dl = [zzd[i, j] for i in range(2) for j in range(2)]
VS10 = zl + dl + [sp.Symbol("US"), sp.Symbol("UC")]
CJ = {}
CJ.update({zl[k]: dl[k] for k in range(4)})
CJ.update({dl[k]: zl[k] for k in range(4)})


def cJ(e):
    return sp.expand(e.xreplace(CJ))


# R4: the shift of the claim is Phi -> Phi + s I (frame mode phi_0*I; matches T6e),
# i.e. only the diagonal entries shift. The previous all-entries map encoded
# Phi -> Phi + s*(all-ones matrix), which is not that shift.
SH = {}
SH.update({zl[0]: zl[0] + ss, zl[3]: zl[3] + ss, dl[0]: dl[0] + ssc, dl[3]: dl[3] + ssc})


def polyvec(expr):
    smap = {}
    smap.update({zl[k]: VS10[k] for k in range(4)})
    smap.update({dl[k]: VS10[4 + k] for k in range(4)})
    smap[ss] = VS10[8]
    smap[ssc] = VS10[9]
    return sp.Poly(sp.expand(expr).xreplace(smap), *VS10)


def nulltest(family):
    rows = [polyvec(sp.expand(q.xreplace(SH) - q)) for q in family]
    mons = sorted(set().union(*[set(r.monoms()) for r in rows]))
    Mx = sp.Matrix(len(rows), len(mons), lambda i, j: rows[i].coeff_monomial(mons[j]))
    # R4: family-combination kernel = LEFT nullspace (Mx^T v = 0); the previous
    # right nullspace lives in monomial space and does not measure invariant combinations.
    return Mx.T.nullspace()


Pw = zz
Pd = zzd.T
trP = Pw.trace()
trPd = Pd.trace()
trP2 = (Pw * Pw).trace()
trPd2 = (Pd * Pd).trace()
trX = (Pd * Pw).trace()
QUAD = [sp.expand(trX), sp.expand((trP2 + trPd2) / 2), sp.expand((trP2 - trPd2) / (2 * sp.I)),
        sp.expand(trP * trPd), sp.expand((trP * trP + trPd * trPd) / 2),
        sp.expand((trP * trP - trPd * trPd) / (2 * sp.I))]
nsq = nulltest(QUAD)
# R4 truth (probe_r4_triage2 heavy2): the shift-invariant quadratic subspace is exactly
# the 3-dim span of the traceless-part invariants 2*TrX - TrPhi TrPhidag,
# 2*Re TrPhi^2 - Re(TrPhi)^2, 2*Im TrPhi^2 - Im(TrPhi)^2; none is a function of X, and
# the Tr X direction itself is shift-variant (no X-dependent quadratic invariant).
GENQ = [sp.Matrix([-2, 0, 0, 1, 0, 0]), sp.Matrix([0, -2, 0, 0, 1, 0]),
        sp.Matrix([0, 0, -2, 0, 0, 1])]
okf = (len(nsq) == 3) and (sp.Matrix.hstack(*(nsq + GENQ)).rank() == 3)
okx = (len(nulltest([QUAD[0]])) == 0)
chk("T6f quadratic n=2: shift-invariant subspace exactly the 3 traceless-part invariants; Tr X direction shift-variant (no X-dependent quadratic invariant)",
    okf and okx)

w1 = sp.expand((Pw ** 4).trace())
w2 = sp.expand((Pw ** 3 * Pd).trace())
w3 = sp.expand((Pw * Pw * Pd * Pd).trace())
w4 = sp.expand((Pw * Pd * Pw * Pd).trace())
QUAR = [sp.expand((w1 + cJ(w1)) / 2), sp.expand((w1 - cJ(w1)) / (2 * sp.I)),
        sp.expand((w2 + cJ(w2)) / 2), sp.expand((w2 - cJ(w2)) / (2 * sp.I)),
        w3, w4, sp.expand(w2 * cJ(w2)),
        sp.expand(trX * (trP2 + trPd2) / 2), sp.expand(trX * (trP2 - trPd2) / (2 * sp.I)),
        sp.expand(trX * trP * trPd), sp.expand(trP * trPd * trP * trPd),
        sp.expand((trP ** 4 + cJ(trP ** 4)) / 2), sp.expand((trP ** 4 - cJ(trP ** 4)) / (2 * sp.I)),
        sp.expand((trP2 * trPd2 + cJ(trP2 * trPd2)) / 2),
        sp.expand((trP ** 2 * trP2 + cJ(trP ** 2 * trP2)) / 2),
        sp.expand((trP ** 2 * trP2 - cJ(trP ** 2 * trP2)) / (2 * sp.I))]
# R4: corrected W1 word, Tr C^2 = 2 Tr(P Pd P Pd) - 2 Tr(P^2 Pd^2), C = P Pd - Pd P
# (probe_r4_triage P0/P2). W1w = 2*w4 - 2*w3 is linearly dependent on the family, so it
# is not appended as a separate column; the W1 direction (w4 - w3) is tested inside the
# family. Truth (heavy2): the shift-invariant subspace of this 16-element family is
# exactly 4-dimensional (W1 direction + three further traceless-part invariants), not 1.
W1w = sp.expand(2 * w4 - 2 * w3)
nsg = nulltest(QUAR)
WDIR = sp.Matrix([0, 0, 0, 0, -1, 1] + [0] * 10)
ok = (len(nsg) == 4) and (sp.Matrix.hstack(*(nsg + [WDIR])).rank() == 4)
chk("T6g quartic conjugation-invariant family at n=2: shift-invariant subspace exactly 4-dim and contains the W1 direction w4 - w3",
    ok)

SMR = {}
SMR.update({zl[(2 * i + j)]: Phi2[i, j] for i in range(2) for j in range(2)})
SMR.update({dl[(2 * i + j)]: sp.conjugate(Phi2[i, j]) for i in range(2) for j in range(2)})


def to_ri(e):
    return sp.expand(e.xreplace(SMR))


if len(nsg) == 1:
    v = nsg[0]
    vn = [sp.nsimplify(x / v[len(QUAR)]) for x in v]
    fr = sp.expand(sum(vn[k] * to_ri(QUAR[k]) for k in range(len(QUAR))) + vn[len(QUAR)] * to_ri(W1w))
    pt = {}
    for i in range(2):
        for j in range(2):
            pt[sp.Symbol("Ra" + str(i) + str(j))] = sp.Integer(i + 2 * j + 1)
            pt[sp.Symbol("Ia" + str(i) + str(j))] = sp.Integer(2 * i + j + 2)
    num = sp.nsimplify((fr - W2).subs(pt))
    num2 = sp.nsimplify((fr + W2).subs(pt))
    alpha = sp.Rational(1, 1)
    wpt = sp.simplify(W2.subs(pt))
    if wpt != 0:
        alpha = sp.nsimplify(sp.simplify(fr.subs(pt) / wpt))
    okp = (sp.expand(fr - alpha * W2) == 0)
    chk("T6g2 unique quartic invariant direction equals alpha*W1 exactly (alpha=%s, poly identity)" % alpha,
        okp and alpha != 0)
chk("T6h W1 word identity: 2 Tr(P Pd P Pd) - 2 Tr(P^2 Pd^2) = W1 (real/imag form; W1 = Tr(C^dag C), C = [Phi, Phi^dag])",
    sp.expand(to_ri(W1w) - W2) == 0)

# n=3 spot checks: W1 invariant (T6e) but four standard quartic conjugation-invariants shift-variant
def cand_shift(f):
    M = cmat(3, "d")
    s = sp.Symbol("s3br", real=True) + sp.I * sp.Symbol("s3bi", real=True)
    return sp.simplify(f(M + s * sp.eye(3)) - f(M))


fs = [lambda M: sp.expand((M * M).trace() * (M.adjoint() * M.adjoint()).trace()),
      lambda M: sp.expand(((M.adjoint() * M).trace()) ** 2),
      lambda M: sp.expand((M * M * M.adjoint() * M.adjoint()).trace()),
      lambda M: sp.expand((M.trace() * M.adjoint().trace()) ** 2)]
ok3 = all(sp.simplify(cand_shift(f)) != 0 for f in fs)
chk("T6i n=3 teeth: four standard quartic conjugation-invariants all shift-variant (only W1 survives)", ok3)
# ---- T7: W1 is not a function of X (non-transfer witness) ----
p1, p2 = sp.symbols("p1 p2", real=True)
Ph = sp.diag(p1, p2)
Xh = sp.expand(Ph.adjoint() * Ph)
W1h = sp.simplify(Wfun(Ph))
ok = (W1h == 0) and (Xh == sp.diag(p1 ** 2, p2 ** 2))
H2 = (1 / sp.sqrt(2)) * sp.Matrix([[1, 1], [1, -1]])
ok = ok and (sp.simplify(H2 * H2) == sp.eye(2))
Ph2 = sp.expand(H2 * Ph)
ok = ok and (sp.expand(Ph2.adjoint() * Ph2 - Xh) == sp.zeros(2))
W1H = sp.simplify(Wfun(Ph2))
ok = ok and (sp.expand(W1H - (p1 ** 2 - p2 ** 2) ** 2) == 0)
chk("T7a X(H Phi) = X(Phi) exactly, W1(Phi) = 0, W1(H Phi) = (p1^2 - p2^2)^2 (same X, different W1)", ok)
v1 = W1H.subs({p1: 2, p2: 1})
v0 = W1h.subs({p1: 2, p2: 1})
vD = W1H.subs({p1: 2, p2: 2})
ok = (v1 == 9) and (v0 == 0) and (vD == 0)
ok = ok and ((Xh - sp.expand(Ph2.adjoint() * Ph2)).subs({p1: 2, p2: 1}) == sp.zeros(2))
chk("T7b witness values: X equal, W1 = 0 vs 9 (p=(2,1)); degenerate boundary p1=p2 gives 0", ok)
# R4: the old code checked an UNnormalized U (U^dag U = (|al|^2+|be|^2) I, not I), so the
# old expectation was false for generic al, be. The general U(2) matrix is
# U = (a1+i a2, a3+i a4; -(a3-i a4), a1-i a2)/sqrt(norm) with norm = |a1+ia2|^2+|a3+ia4|^2;
# truth: (U2 Phi)^dag (U2 Phi) = norm * Phi^dag Phi exactly, so the normalized U preserves
# X, and the unscaled matrix does not when norm != 1 (teeth).
a1, a2, a3, a4 = sp.symbols("a1 a2 a3 a4", real=True)
U2g = sp.Matrix([[a1 + sp.I * a2, a3 + sp.I * a4], [-(a3 - sp.I * a4), a1 - sp.I * a2]])
norm = a1 ** 2 + a2 ** 2 + a3 ** 2 + a4 ** 2
Pg = cmat(2, "g")
ok = (sp.expand((U2g * Pg).adjoint() * (U2g * Pg) - norm * (Pg.adjoint() * Pg)) == sp.zeros(2))
ok = ok and (sp.expand((U2g * Pg).adjoint() * (U2g * Pg) - Pg.adjoint() * Pg) != sp.zeros(2))
chk("T7c general U(2): (U2 Phi)^dag(U2 Phi) = norm * Phi^dag Phi, so normalized U preserves X (channel obstruction); unscaled U does not",
    ok)

# ---- T8: lift is nonzero on linear Phi (gauge-matter coupling present), tree-level only ----
Phi_l = [(e4(0), genmat(n, "g0")), (e4(1), genmat(n, "g1"))]
Alin = [genmat(n, "N" + str(r)) for r in range(4)]
Lg = lift_full(Phi_l, Alin, ThN, n)
chk("T8 lift(A, linear Phi) nonzero for generic data (class has quartic gauge-matter coupling)",
    sp.simplify(Lg) != 0)

# ---- payload size ceiling and summary ----
chk("P8 payload size 5287 <= 5340 (chain-119 ceiling re-pinned R5, +53 margin kept)", len(pay) <= 5340)
print("TOTAL %d/%d PASS" % (PASS[0], PASS[0] + FAIL[0]))
print("ALL CHECKS DONE 120")
import sys
if FAIL[0]:
    sys.exit(1)
