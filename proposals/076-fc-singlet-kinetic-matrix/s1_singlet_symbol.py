"""
076 / s1.  Tree symbol of the two static scalar singlets w_1 = T and w_y = P T of the conjugate-coordinate class
(Poisson limit, leaf CP^{1,2} of so(4,2), units R=1, bilinear coefficient mu^2=-3), at the base point y0 with
y^i = 0, so that P = P_{y0} is the projector on the time direction:  P^a_b = delta^a_0 delta^0_b.

The Lie-Poisson algebra, the field equation and the Hessian L are those of
proposals/074-f-tree-nonderivative-wave/s2_liepoisson_q0_hessian.py, which is imported read-only (its head only).

Checks (both signs s of the bracket):
 (a) exact: L(T) = 6T, L(PT) = 2(1-P)T;
 (b) exact: for w in {T, PT} and the base functions y^mu = M^{mu5}, the Taylor form
        L(f w) = f L w + d_mu f B^mu(w) + d_mu d_nu f R^{mu nu}(w),
        B^mu(w)   = L(y^mu w) - y^mu L(w),
        2R^{mu nu}(w) = L(y^mu y^nu w) - y^mu L(y^nu w) - y^nu L(y^mu w) + y^mu y^nu L(w),
     with  R^{mu nu}(w)_a = -m^2 ( eta^{mu nu} w_a - (delta^mu_a w^nu + delta^nu_a w^mu)/2 ),  m = M^{45},
     and the third-order Taylor coefficient zero (L is a second-order operator in the base functions);
 (c) fibre averages over the fibre over y0 (SO(3) Haar quadrature, exact for these polynomial degrees):
     N_ij = <w_i . L w_j>   (expect [[6,2],[0,0]] (l^2+m^2)),
     the static kinetic matrix Z_ij(k) = m^2 (q^2 <w_i.w_j> - <(q.w_i)(q.w_j)>), q = k e_3
       (expect diag(2/3 m^2 k^2 (l^2+m^2), 0)), and the same from -q q <w_i R w_j>,
     the first-order coefficients B^mu_ij = <w_i . B^mu(w_j)> and the antisymmetric part
       K^mu = (B^mu_1y - B^mu_y1)/2 (expect K^i = 0 for i=1,2,3, so K.q = 0 for static q),
     <T_mu M^{mu rho}> (expect only rho=0 non-zero, so <T.v> = 0 for static q);
 (d) the covariant fibre moment <T^mu T^nu>(y) = ( -(y.y) eta^{mu nu} + y^mu y^nu )/3 at random base points,
     and from it, exactly (sympy), q_nu d_mu [ eta^{mu nu}<T.PT> - <T^(mu (PT)^nu)> ](y0) = 0 for static q
     and <T R^{mu nu} PT>(y0) = 0, so the R-term contributes nothing to the antisymmetric first-order term.
Run:  python -I s1_singlet_symbol.py
"""
import pathlib
import numpy as np
import sympy as sp
from scipy.linalg import expm

HERE = pathlib.Path(__file__).resolve().parent
SRC074 = HERE.parent / "074-f-tree-nonderivative-wave" / "s2_liepoisson_q0_hessian.py"
head = SRC074.read_text().split("eps = sp.Symbol(\"eps\")")[0]
ns = {}
exec(compile(head, "s2_074_head", "exec"), ns)
make_bracket, Lrecorded, Mf, gens = ns["make_bracket"], ns["Lrecorded"], ns["M"], ns["gens"]
eta4 = [-1, 1, 1, 1]
T = [Mf(a, 4) for a in range(4)]
Y = [Mf(mu, 5) for mu in range(4)]
m = Mf(4, 5)
PT = [T[0], 0, 0, 0]          # (P T)^a = delta^a_0 T^0 for y0 along e_0
W = {"1": T, "y": PT}
mu2 = -3


def lower(v):
    return [eta4[a] * v[a] for a in range(4)]


def sub(u, v):
    return [sp.expand(a - b) for a, b in zip(u, v)]


def mul(f, v):
    return [sp.expand(f * a) for a in v]


results = {}
for s in (1, -1):
    br = make_bracket(s)
    L = lambda A: Lrecorded(A, br, s, mu2)  # lower index output
    LT, LPT = L(T), L(PT)
    oka = all(sp.expand(LT[a] - 6 * lower(T)[a]) == 0 for a in range(4)) and \
        all(sp.expand(LPT[a] - 2 * lower(sub(T, PT))[a]) == 0 for a in range(4))
    print(f"s={s}: (a) L(T)=6T and L(PT)=2(1-P)T exactly: {oka}")
    assert oka
    B, R = {}, {}
    okR, ok3 = True, True
    for key, w in W.items():
        Lw = L(w)
        Lyw = [L(mul(Y[mu], w)) for mu in range(4)]
        B[key] = [sub(Lyw[mu], mul(Y[mu], Lw)) for mu in range(4)]
        R[key] = {}
        wl = lower(w)
        for mu in range(4):
            for nu in range(mu, 4):
                Lyy = L(mul(Y[mu] * Y[nu], w))
                r2 = [sp.expand(Lyy[a] - Y[mu] * Lyw[nu][a] - Y[nu] * Lyw[mu][a] + Y[mu] * Y[nu] * Lw[a]) for a in range(4)]
                r = [x / 2 for x in r2]
                R[key][(mu, nu)] = r
                target = []
                for a in range(4):
                    val = (eta4[mu] if mu == nu else 0) * wl[a]
                    val -= sp.Rational(1, 2) * ((1 if a == mu else 0) * w[nu] + (1 if a == nu else 0) * w[mu])
                    target.append(sp.expand(-m**2 * val))
                okR = okR and all(sp.expand(r[a] - target[a]) == 0 for a in range(4))
        # third-order Taylor coefficient for one triple (mu,nu,la) = (1,2,3) and (0,0,3)
        for (a1, a2, a3) in ((1, 2, 3), (0, 0, 3), (3, 3, 3)):
            f1, f2, f3 = Y[a1], Y[a2], Y[a3]
            def Lm(fs):
                prod = sp.Integer(1)
                for f in fs:
                    prod *= f
                return L(mul(prod, w))
            # third finite difference: sum over subsets with signs
            import itertools
            tot = [0] * 4
            idx = [f1, f2, f3]
            for k in range(4):
                for sub_ in itertools.combinations(range(3), k):
                    inside = [idx[i] for i in sub_]
                    outside = [idx[i] for i in range(3) if i not in sub_]
                    prod_out = sp.Integer(1)
                    for f in outside:
                        prod_out *= f
                    val = Lm(inside)
                    sign = (-1) ** (3 - k)
                    tot = [sp.expand(tot[a] + sign * prod_out * val[a]) for a in range(4)]
            ok3 = ok3 and all(t == 0 for t in tot)
    print(f"s={s}: (b) R^(mu nu)(w) = -m^2(eta^(mu nu) w_a - (delta^mu_a w^nu + delta^nu_a w^mu)/2) exactly: {okR};"
          f" third-order Taylor coefficient zero: {ok3}")
    assert okR and ok3
    results[s] = (B, R, LT, LPT)

# (c) fibre averages at y0, numerical on an explicit orbit point; SO(3) Haar quadrature
rng = np.random.default_rng(7)
eta6 = np.diag([-1., 1, 1, 1, 1, -1])
E4 = np.diag([-1., 1, 1, 1])
ell = 1.3
M0 = np.zeros((6, 6))
for (A, Bb) in ((0, 5), (1, 2), (3, 4)):
    M0[A, Bb] = ell; M0[Bb, A] = -ell


def random_g(scale=0.8):
    X = rng.normal(size=(6, 6)) * scale
    X = X - X.T
    return expm(eta6 @ X)


def boost_to_rest(Mm):
    y = Mm[:4, 5]
    b = y[1:] / y[0]
    gam = 1 / np.sqrt(1 - b @ b)
    Lb = np.eye(4)
    Lb[0, 0] = gam; Lb[0, 1:] = -gam * b; Lb[1:, 0] = -gam * b
    Lb[1:, 1:] += (gam - 1) * np.outer(b, b) / (b @ b)
    G = np.eye(6); G[:4, :4] = Lb
    return G @ Mm @ G.T


while True:
    g_ = random_g()
    Mm = g_ @ M0 @ g_.T
    if Mm[0, 5] < 0:
        continue
    Mrest = boost_to_rest(Mm)
    if Mrest[4, 5] > 0.5:
        break
yv, mv, Tv = Mrest[:4, 5], Mrest[4, 5], Mrest[:4, 4]
assert np.abs(yv[1:]).max() < 1e-10
TT = ell**2 + mv**2


def euler(a, b, c):
    def Rz(t):
        return np.array([[np.cos(t), -np.sin(t), 0], [np.sin(t), np.cos(t), 0], [0, 0, 1]])
    def Ry(t):
        return np.array([[np.cos(t), 0, np.sin(t)], [0, 1, 0], [-np.sin(t), 0, np.cos(t)]])
    return Rz(a) @ Ry(b) @ Rz(c)


nq = 14
xg, wg = np.polynomial.legendre.leggauss(nq)
angs = 2 * np.pi * np.arange(nq) / nq
pts, wts = [], []
for xb, wb in zip(xg, wg):
    for a in angs:
        for c in angs:
            G = np.eye(6); G[1:4, 1:4] = euler(a, np.arccos(xb), c)
            pts.append(G @ Mrest @ G.T); wts.append(wb)
wts = np.array(wts) / np.sum(wts)
pairs = [(A, Bb) for A in range(6) for Bb in range(A + 1, 6)]
vals = np.array([[p[A, Bb] for (A, Bb) in pairs] for p in pts])
assert np.abs(vals[:, [pairs.index((mu, 5)) for mu in range(4)]] - yv).max() < 1e-10


def avg(expr):
    f = sp.lambdify(gens, expr, "numpy")
    out = f(*[vals[:, i] for i in range(15)])
    return float(np.sum(wts * np.broadcast_to(out, wts.shape)))


def dot_up_low(w_up, v_low):
    return sp.expand(sum(w_up[a] * v_low[a] for a in range(4)))


for s in (1, -1):
    B, R, LT, LPT = results[s]
    Lw = {"1": LT, "y": LPT}
    keys = ["1", "y"]
    N = np.array([[avg(dot_up_low(W[i], Lw[j])) for j in keys] for i in keys]) / TT
    print(f"s={s}: (c) N_ij=<w_i.L w_j>/(l^2+m^2) = {np.round(N, 9).tolist()}  (expect [[6,2],[0,0]]; symmetrised [[6,1],[1,0]])")
    assert np.allclose(N, [[6, 2], [0, 0]], atol=1e-9)
    k = 1.0
    ql = [0, 0, 0, k]  # q_mu lower, static, q.y0 = 0
    Z = np.zeros((2, 2)); ZR = np.zeros((2, 2))
    for ii, i in enumerate(keys):
        for jj, j in enumerate(keys):
            wiwj = sum(eta4[a] * W[i][a] * W[j][a] for a in range(4))
            qwi = sum(ql[a] * W[i][a] for a in range(4)); qwj = sum(ql[a] * W[j][a] for a in range(4))
            q2 = sum(eta4[a] * ql[a] ** 2 for a in range(4))
            Z[ii, jj] = avg(sp.expand(m**2 * (q2 * wiwj - qwi * qwj)))
            ZR[ii, jj] = avg(sp.expand(-sum(ql[mu] * ql[nu] * (1 if mu == nu else 2) *
                                            dot_up_low(W[i], R[j][(min(mu, nu), max(mu, nu))])
                                            for mu in range(4) for nu in range(mu, 4))))
    Zn = Z / (mv**2 * k**2 * TT)
    print(f"s={s}: (c) static kinetic matrix Z/(m^2 k^2 (l^2+m^2)) = {np.round(Zn, 9).tolist()} (expect [[2/3,0],[0,0]]);"
          f" from -qq<w R w>: {np.round(ZR / (mv**2 * k**2 * TT), 9).tolist()}")
    assert np.allclose(Zn, [[2 / 3, 0], [0, 0]], atol=1e-9) and np.allclose(ZR, Z, atol=1e-8)
    Bm = {(i, j): np.array([avg(dot_up_low(W[i], B[j][mu])) for mu in range(4)]) for i in keys for j in keys}
    K = (Bm[("1", "y")] - Bm[("y", "1")]) / 2
    Ssym = {(i, j): (Bm[(i, j)] + Bm[(j, i)]) / 2 for i in keys for j in keys}
    print(f"s={s}: (c) K^mu = (B_1y - B_y1)/2 over (l^2+m^2)|y0| = {np.round(K / (TT * yv[0]), 9).tolist()} ; "
          f"spatial parts of all B^mu_ij: max {max(np.abs(Bm[x][1:]).max() for x in Bm):.1e}")
    assert max(np.abs(Bm[x][1:]).max() for x in Bm) < 1e-8
    TM = np.array([avg(sp.expand(sum(eta4[mu] * T[mu] * Mf(mu, rho) for mu in range(4)))) for rho in range(4)])
    print(f"s={s}: (c) <T_mu M^(mu rho)> = {np.round(TM, 9).tolist()} (only rho=0 may be non-zero)")
    assert np.abs(TM[1:]).max() < 1e-8

# (d) covariant fibre moment at random base points, then the R-term derivative exactly
worst = 0
for _ in range(3):
    g = random_g()
    Mm = g @ M0 @ g.T
    Mr = boost_to_rest(Mm) if Mm[0, 5] > 0 else None
    if Mr is None:
        continue
    # undo: the fibre over y = Lambda^{-1} y_rest is the Lambda^{-1}-image of the rest fibre
    y_r = Mr[:4, 5]
    Lam = expm(np.einsum('ij,jk->ik', E4, (lambda A: A - A.T)(rng.normal(size=(4, 4)) * 0.4)))
    G = np.eye(6); G[:4, :4] = Lam
    yb = Lam @ y_r
    mom = np.zeros((4, 4))
    for xb, wb in zip(xg, wg):
        for a in angs:
            for c in angs:
                Rg = np.eye(6); Rg[1:4, 1:4] = euler(a, np.arccos(xb), c)
                Pp = G @ (Rg @ Mr @ Rg.T) @ G.T
                Tp = Pp[:4, 4]
                mom += wb * np.outer(Tp, Tp)
    mom /= np.sum(wg) * nq * nq
    yy = yb @ E4 @ yb
    pred = (-(yy) * np.linalg.inv(E4) + np.outer(yb, yb)) / 3
    worst = max(worst, np.abs(mom - pred).max() / abs(yy))
print(f"(d) <T^mu T^nu>(y) = (-(y.y) eta^(mu nu) + y^mu y^nu)/3 at boosted base points: worst relative residual {worst:.1e}")
assert worst < 1e-9

yS = sp.symbols("y0:4")
y0S = sp.Symbol("Y0", positive=True)
etaS = sp.diag(-1, 1, 1, 1)
yvec = sp.Matrix(yS)
yy = (yvec.T * etaS * yvec)[0]
TTm = (-yy * etaS.inv() + yvec * yvec.T) / 3                 # <T^mu T^nu>(y), upper indices
Pm = sp.zeros(4, 4); Pm[0, 0] = 1                              # P^nu_la for y0 = (Y0,0,0,0)
TPT = TTm * Pm.T                                               # <T^mu (PT)^nu> = <T^mu T^la> P^nu_la
etaup = etaS.inv()
TdotPT = sum(etaS[a, a] * TPT[a, a] for a in range(4))
bracket = sp.Matrix(4, 4, lambda mu, nu: etaup[mu, nu] * TdotPT - (TPT[mu, nu] + TPT[nu, mu]) / 2)
at0 = {yS[0]: y0S, yS[1]: 0, yS[2]: 0, yS[3]: 0}
div = [sp.simplify(sum(sp.diff(bracket[mu, nu], yS[mu]) for mu in range(4)).subs(at0)) for nu in range(4)]
val0 = sp.simplify(bracket.subs(at0))
print("(d) <T R^(mu nu) PT>(y0) / (-m^2) =", val0.tolist(), "; d_mu of it, nu = 0..3:", div,
      "; contracted with static q (q_0 = 0):", sp.simplify(sum(div[nu] * [0, 1, 1, 1][nu] for nu in range(1, 4))))
assert val0 == sp.zeros(4, 4) and all(sp.simplify(d) == 0 for d in div[1:])
print("all checks passed")
