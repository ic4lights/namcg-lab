"""
074 / s4 (candidate for a later round; NOT part of the r2 insert).
Tree non-derivative term <w.L(w)> on the small-k limit of the equal-weight elimination profile at V=T,
(S1) dust source at rest in the frame of y, static q with q.y=0:
   alpha(n) = X v / (v.v + varpi),  X^{mu nu} = u^mu u^nu + (1/2) eta^{mu nu},  u = yhat,  v^mu = M^{mu rho} q_rho.
For m^2 k^2 << varpi:  alpha -> X v / varpi + O(k^3), i.e. (up to 1/varpi) the polynomial leaf function
   w^a = u^a (u.Mq) + (1/2) M^{a rho} q_rho      (u constant: the extension used here).
Checks:
 (a) exact (Lie-Poisson, both s): L(Mq) = 0, since Mq is proportional to the gauge direction {q.T, T};
 (b) exact: L(w) = L(w1), w1 = u (u.Mq), g = Mq/2; hence pointwise w.L(w) = k^2[(M^03)^2 - ((M^13)^2+(M^23)^2)/2]
     for q = k e_3, u = e_0, and on the fibre (M^03)^2 = (m^2/|y|^2) T_3^2, sum_{i<j} (M^ij)^2 = l^2, so
     <w.L(w)> = k^2 (m^2 - l^2)/3, <w.w> = k^2 (2 l^2 - m^2)/12, <w.v> = k^2 (m^2 + 2 l^2)/6;
 (c) fibre averages over y=(y0,0,0,0): <w.L(w)>, <w.w>, <(q.w)^2>, <w.v>, and the algebraic trace eta_{a mu}{w^a,y^mu};
 (d) per sigma_1^2 (r1 conventions, reproducing the level-one value (3 rho/2g^2)(k^-2 - m^2)):
     C = (rho/2g^2)[<wLw> + m^2(k^2<w.w> - <(q.w)^2>)] / sigma^2, sigma = -<w.v>/m.
Run:  python -I s4_equal_weight_profile_candidate.py
"""
import pathlib
import numpy as np
import sympy as sp
from scipy.linalg import expm

here = pathlib.Path(__file__).resolve().parent
src = (here / "s2_liepoisson_q0_hessian.py").read_text()
ns = {}
exec(compile(src.split("eps = sp.Symbol(\"eps\")")[0], "s2_head", "exec"), ns)
make_bracket, Lrec, T, gens, M, e4 = ns["make_bracket"], ns["Lrecorded"], ns["T"], ns["gens"], ns["M"], ns["eta4"]

u0, q3 = sp.symbols("u0 q3", real=True)
u = [u0, 0, 0, 0]          # u^a, constant, along y0 (rest frame of y), normalised later u.u=-1 -> u0=1
q = [0, 0, 0, q3]          # q^a, static, q.u = 0
ql = [e4[a] * q[a] for a in range(4)]
ul = [e4[a] * u[a] for a in range(4)]
Mq = [sp.expand(sum(M(a, r) * ql[r] for r in range(4))) for a in range(4)]   # (Mq)^a = M^{a rho} q_rho
uMq = sp.expand(sum(ul[a] * Mq[a] for a in range(4)))
w1 = [sp.expand(u[a] * uMq) for a in range(4)]
g = [sp.expand(sp.Rational(1, 2) * Mq[a]) for a in range(4)]
w = [w1[a] + g[a] for a in range(4)]

res = {}
for s in (1, -1):
    br = make_bracket(s)
    LMq = Lrec(Mq, br, s, -3)
    okA = all(sp.expand(x) == 0 for x in LMq)
    qT = sp.expand(sum(ql[a] * T[a] for a in range(4)))
    gauge = [sp.expand(br(qT, T[a])) for a in range(4)]
    ratio = [sp.simplify(gauge[a] / Mq[a]) for a in range(4) if Mq[a] != 0]
    print(f"s={s}: (a) L(Mq) = 0 exactly: {okA};  {{q.T, T^a}} / (Mq)^a = {set(ratio)}")
    assert okA
    Lw = Lrec(w, br, s, -3)           # lower index
    Lw1 = Lrec(w1, br, s, -3)
    okB = all(sp.expand(Lw[a] - Lw1[a]) == 0 for a in range(4))
    print(f"s={s}: (b) L(w) = L(w1) exactly: {okB};  w.L(w) at u0=1 =", sp.factor(sp.expand(sum(w[a] * Lw[a] for a in range(4)).subs(u0, 1))))
    assert okB
    wLw = sp.expand(sum(w[a] * Lw[a] for a in range(4)))
    ww = sp.expand(sum(e4[a] * w[a] * w[a] for a in range(4)))
    qw = sp.expand(sum(ql[a] * w[a] for a in range(4)))
    v = [sp.expand(sum(M(a, r) * ql[r] for r in range(4))) for a in range(4)]
    wv = sp.expand(sum(e4[a] * w[a] * v[a] for a in range(4)))
    y = [M(a, 5) for a in range(4)]
    trace = sp.expand(sum(e4[a] * br(w[a], y[a]) for a in range(4)))
    res[s] = dict(wLw=wLw, ww=ww, qw=qw, wv=wv, trace=trace)
    print(f"s={s}: q.w = {qw};  algebraic trace eta_(a mu){{w^a,y^mu}} = {sp.factor(trace)}")

# (c) numerical fibre averages on an explicit orbit point with y^i = 0 (as in s3)
rng = np.random.default_rng(11)
eta6 = np.diag([-1., 1, 1, 1, 1, -1]); eta4 = np.diag([-1., 1, 1, 1]); ell = 1.3
M0 = np.zeros((6, 6))
for (A, B) in ((0, 5), (1, 2), (3, 4)):
    M0[A, B] = ell; M0[B, A] = -ell
def random_g(scale=0.8):
    Aa = rng.normal(size=(6, 6)) * scale; Aa = Aa - Aa.T
    return expm(eta6 @ Aa)
def boost(Mm):
    y = Mm[:4, 5]
    if y[0] < 0: Mm = -Mm; y = Mm[:4, 5]
    b = y[1:] / y[0]; gam = 1 / np.sqrt(1 - b @ b)
    L = np.eye(4); L[0, 0] = gam; L[0, 1:] = -gam * b; L[1:, 0] = -gam * b
    L[1:, 1:] += (gam - 1) * np.outer(b, b) / (b @ b)
    G = np.eye(6); G[:4, :4] = L
    return G @ Mm @ G.T
def rotq():
    qq = rng.normal(size=4); qq /= np.linalg.norm(qq); a, b, c, d = qq
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)], [2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d]])
for trial in range(2):
    while True:
        Mr = boost((lambda G: G @ M0 @ G.T)(random_g()))
        if Mr[4, 5] > 0.5 and Mr[0, 5] > 0: break
    m = Mr[4, 5]; y2 = ell**2 + m**2
    pts = []
    for _ in range(20000):
        R = np.eye(6); R[1:4, 1:4] = rotq(); pts.append(R @ Mr @ R.T)
    kval = 0.37
    subs_base = {u0: 1, q3: kval}
    for s in (1, -1):
        fns = {key: sp.lambdify(gens, expr.subs(subs_base), "numpy") for key, expr in res[s].items()}
        def val(Mm, f):
            args = [Mm[A, B] for A in range(6) for B in range(A + 1, 6)]
            return f(*args)
        av = {key: np.mean([val(p, f) for p in pts]) for key, f in fns.items()}
        k2 = kval**2
        pred = dict(wLw=k2 * (m**2 - ell**2) / 3, ww=k2 * (2 * ell**2 - m**2) / 12, wv=k2 * (m**2 + 2 * ell**2) / 6)
        print(f"trial {trial} s={s} m={m:.3f}: <wLw>/(k^2(m^2-l^2)/3)={av['wLw']/pred['wLw']:.4f}  "
              f"<w.w>/(k^2(2l^2-m^2)/12)={av['ww']/pred['ww']:.4f}  <w.v>/(k^2(m^2+2l^2)/6)={av['wv']/pred['wv']:.4f}  "
              f"max|q.w|={max(abs(val(p, fns['qw'])) for p in pts[:200]):.1e}  max|trace|={max(abs(val(p, fns['trace'])) for p in pts[:200]):.1e}")
        assert abs(av['wLw'] / pred['wLw'] - 1) < 0.03 and abs(av['wv'] / pred['wv'] - 1) < 0.03
        assert abs(av['ww'] / pred['ww'] - 1) < 0.05

# (d) symbolic per-sigma_1^2 coefficients, r1 conventions
rho, gg, mm, kk, ll, A_ = sp.symbols("rho g m k ell A", positive=True)
def C(wLw, ww, qw2, wv):
    sig = -wv / mm
    return sp.simplify((rho / (2 * gg**2)) * (wLw + mm**2 * (kk**2 * ww - qw2)) / sig**2)
y2 = ll**2 + mm**2
C1 = C(y2 / 3, -y2 / 3, 0, mm * kk * sp.sqrt(y2) / 3)           # level one, w = yhat (qhat.T)
Cew = C(kk**2 * (mm**2 - ll**2) / 3, kk**2 * (2 * ll**2 - mm**2) / 12, 0, kk**2 * (mm**2 + 2 * ll**2) / 6)
print("level-one  C =", sp.factor(C1))
print("equal-weight small-k profile  C =", sp.factor(Cew))
conv = 16 * sp.pi**2 * mm**2 / A_                                  # L/2m^4 with L = 32 pi^2 m^6/A
varpi = 8 * sp.pi**2 * rho * mm**6 / (gg**2 * A_)
nd = sp.simplify(conv * (rho / (2 * gg**2)) * (kk**2 * (mm**2 - ll**2) / 3) / (kk**2 * (mm**2 + 2 * ll**2) / (6 * mm))**2 / varpi)
ls = sp.simplify(conv * (rho / (2 * gg**2)) * mm**2 * kk**2 * (kk**2 * (2 * ll**2 - mm**2) / 12) /
                 (kk**2 * (mm**2 + 2 * ll**2) / (6 * mm))**2 / varpi)
print("normalised: non-derivative =", sp.factor(nd), "* varpi ;  leading symbol =", sp.factor(ls), "* varpi")
print("  at ell -> 0: non-derivative", sp.limit(nd, ll, 0), "* varpi ; leading symbol", sp.limit(ls, ll, 0), "* varpi")
assert sp.simplify(sp.limit(ls, ll, 0) + 3 / mm**2) == 0
print("s4 done")
