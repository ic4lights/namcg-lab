"""
074 / s3.  Orbit identities, the local q=0 forms and the frozen-symbol channel (numerical on an explicit
realisation of the orbit, plus exact sympy algebra for the localisation identity and the bounds).

Run:  python -I s3_orbit_local_forms.py
"""
import numpy as np
import sympy as sp
from scipy.linalg import expm

rng = np.random.default_rng(11)
eta6 = np.diag([-1., 1, 1, 1, 1, -1])
eta4 = np.diag([-1., 1, 1, 1])
ell = 1.3


def random_g(scale=0.8):
    A = rng.normal(size=(6, 6)) * scale
    A = A - A.T
    X = eta6 @ A  # X^T eta + eta X = 0
    return expm(X)


M0 = np.zeros((6, 6))
for (A, B) in ((0, 5), (1, 2), (3, 4)):
    M0[A, B] = ell; M0[B, A] = -ell
assert np.allclose((eta6 @ M0) @ (eta6 @ M0), -ell**2 * np.eye(6))


def data(Mm):
    y = Mm[:4, 5].copy(); m = Mm[4, 5]; T = Mm[:4, 4].copy()
    return y, m, T


def boost_to_rest(Mm):
    """Lorentz transformation of the indices 0..3 (inside SO(4,2)) bringing y^mu to (y^0,0,0,0)."""
    y, m, T = data(Mm)
    yy = y @ eta4 @ y
    n = np.sqrt(-yy)
    if y[0] < 0:
        Mm = -Mm; y, m, T = data(Mm)  # the other orbit orientation; not used for the averages
    b = y[1:] / y[0]
    gam = 1 / np.sqrt(1 - b @ b)
    L = np.eye(4)
    L[0, 0] = gam; L[0, 1:] = -gam * b; L[1:, 0] = -gam * b
    L[1:, 1:] += (gam - 1) * np.outer(b, b) / (b @ b)
    G = np.eye(6); G[:4, :4] = L
    Mn = G @ Mm @ G.T
    return Mn


def rot3(R):
    G = np.eye(6); G[1:4, 1:4] = R
    return G


def random_rotation():
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    a, b, c, d = q
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d]])


# (i) pointwise orbit identities at random points
worst = 0
for _ in range(200):
    g_ = random_g(); Mm = g_ @ M0 @ g_.T
    y, m, T = data(Mm)
    TT = T @ eta4 @ T; yy = y @ eta4 @ y
    yM = (eta4 @ y) @ Mm[:4, :4]  # y_mu M^{mu rho}
    errs = [abs((eta6 @ Mm @ eta6 @ Mm + ell**2 * np.eye(6)).max()),
            abs(TT - (ell**2 + m**2)), abs(yy + ell**2 + m**2), abs(T @ eta4 @ y),
            np.abs(yM - m * T).max()]
    MM = np.einsum('ab,cd,ac,bd->', Mm[:4, :4], Mm[:4, :4], eta4, eta4)
    errs.append(abs(MM - (2 * ell**2 - 2 * m**2)))
    worst = max(worst, max(e / (1 + abs(m))**2 for e in errs))
print(f"(i) on 200 random orbit points: (eta M)^2=-l^2, T.T=l^2+m^2, y.y=-(l^2+m^2), T.y=0, y_mu M^(mu rho)=m T^rho,"
      f" M_ab M^ab=2l^2-2m^2 ; worst relative residual {worst:.1e}")
assert worst < 1e-9

# (ii) fibre at a base point with y^i = 0, sampled by the SO(3) of the indices 1..3
while True:  # a point on the sheet y^4 > 0 with y^0 > 0
    Mrest = boost_to_rest((lambda g: g @ M0 @ g.T)(random_g()))
    y, m, T = data(Mrest)
    if m > 0.5 and y[0] > 0:
        break
assert np.abs(y[1:]).max() < 1e-10
samples = []
for _ in range(40000):
    R = random_rotation()
    samples.append(rot3(R) @ Mrest @ rot3(R).T)
Ts = np.array([data(x)[2] for x in samples])
ys = np.array([data(x)[0] for x in samples])
assert np.abs(ys - y).max() < 1e-10  # y fixed on the sampled fibre
TT = ell**2 + m**2
mom = Ts.T @ Ts / len(Ts)
print(f"(ii) fibre over y=(y0,0,0,0), y4=m={m:.4f}: max|T^0|={np.abs(Ts[:,0]).max():.1e};"
      f" <T^i T^j>/(T.T/3) = diag {np.round(np.diag(mom)[1:]/(TT/3),3)}, offdiag max {np.abs(mom[1:,1:]-np.diag(np.diag(mom)[1:])).max()/(TT/3):.3f}")
assert np.abs(Ts[:, 0]).max() < 1e-9 and np.allclose(np.diag(mom)[1:] / (TT / 3), 1, atol=0.03)

# (iii) local q=0 form on the static singlet sector, kappa = d1*1 + dy*P_y,  A.L(A) = -2 kT.kT + 2 tr k T.kT
yhat = y / np.sqrt(-(y @ eta4 @ y))
P = np.outer(yhat, yhat) @ eta4 / (yhat @ eta4 @ yhat)  # P^a_b
def form(d1, dy):
    k = d1 * np.eye(4) + dy * P
    vals = []
    for Tn in Ts[:4000]:
        kT = k @ Tn
        vals.append(-2 * kT @ eta4 @ kT + 2 * np.trace(k) * (Tn @ eta4 @ kT))
    return np.mean(vals)
c11 = form(1, 0); cyy = form(0, 1); c1y = (form(1, 1) - c11 - cyy) / 2
print(f"(iii) <A.L(A)>/(l^2+m^2) on kappa=d1+dy P_y: d1^2 {c11/TT:.6f} (expect 6), dy^2 {cyy/TT:.2e} (expect 0),"
      f" 2 d1 dy {2*c1y/TT:.6f} (expect 2)")
assert abs(c11 / TT - 6) < 1e-9 and abs(cyy / TT) < 1e-9 and abs(2 * c1y / TT - 2) < 1e-9
# trace of the metric perturbation: delta gamma = m^2 (kappa + kappa^T) (indices raised), t = 2 m^2 tr kappa
# sigma_1 = -t/2m^2 = -(4 d1 + dy).  Stationary value at fixed sigma_1 over the sigma_1-neutral direction:
d1, dy, sg = sp.symbols("d1 dy sigma")
f = 6 * d1**2 + 2 * d1 * dy
fs = sp.expand(f.subs(dy, -sg - 4 * d1))
d1s = sp.solve(sp.diff(fs, d1), d1)[0]
print("     form at fixed sigma_1 with dy = -sigma-4 d1:", fs, "; stationary at d1 =", d1s, "value", sp.simplify(fs.subs(d1, d1s)),
      "; curvature in d1:", sp.diff(fs, d1, 2))
print("     pure trace (dy=0):", sp.expand(f.subs({dy: 0, d1: -sg / 4})), "; yy channel (d1=0):", f.subs(d1, 0))
print("     canonical pointwise density along the dilatation, 6 M.M - 6 T.T over l^2+m^2 at this point:",
      round((6 * (2 * ell**2 - 2 * m**2) - 6 * TT) / TT, 4), "(presentation dependent; A.L(A) gives 12)")

# (iv) localisation (IMS) identity in the Lie-Poisson algebra: 2 f L(fA) - f^2 L(A) - L(f^2 A) = 2 (Df.Df) A - 2 Df (Df.A)
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("s2", pathlib.Path(__file__).with_name("s2_liepoisson_q0_hessian.py"))
src = pathlib.Path(__file__).with_name("s2_liepoisson_q0_hessian.py").read_text()
head = src.split("eps = sp.Symbol(\"eps\")")[0]
ns = {}
exec(compile(head, "s2_head", "exec"), ns)
br = ns["make_bracket"](1)
Lrec = ns["Lrecorded"]; Tg = ns["T"]; gens = ns["gens"]; e4 = ns["eta4"]
import random
random.seed(5)
fpol = sum(random.randint(-2, 2) * gens[random.randrange(15)] for _ in range(4)) + gens[0] * gens[7]
A = [sum(random.randint(-2, 2) * gens[random.randrange(15)] for _ in range(3)) for _ in range(4)]
lhs = [sp.expand(2 * fpol * l1 - fpol**2 * l2 - l3) for l1, l2, l3 in zip(
    Lrec([fpol * x for x in A], br, 1, -3), Lrec(A, br, 1, -3), Lrec([fpol**2 * x for x in A], br, 1, -3))]
Df = [br(Tg[a], fpol) for a in range(4)]
DfDf = sum(e4[a] * Df[a] * Df[a] for a in range(4))
DfA = sum(e4[a] * Df[a] * e4[a] * A[a] * e4[a] for a in range(4))  # (D^a f) eta_ab A^b
rhs = [sp.expand(2 * DfDf * e4[a] * A[a] - 2 * e4[a] * Df[a] * DfA) for a in range(4)]
ok4 = all(sp.expand(l - r) == 0 for l, r in zip(lhs, rhs))
print("(iv) [f,[L,f]] is the multiplication 2(Df.Df) - 2 Df (Df . ) : no f, no second derivative of f:", ok4)
assert ok4

# (v) frozen-symbol static channel along y y at q.y = 0: v^mu = M^{mu rho} q_rho, yhat.v = (m/|y|) q.T
k = 0.7
q = np.array([0, 0, 0, k])  # lower-index q_rho = eta_rho sigma q^sigma with q^3 = k
ql = eta4 @ q
vs = np.array([x[:4, :4] @ ql for x in samples])
yv = vs @ eta4 @ yhat
qT = Ts @ ql
ratio = np.max(np.abs(np.abs(yv) - abs(m) / np.sqrt(TT) * np.abs(qT)))
print(f"(v) |yhat.v| = (|m|/|y|) |q.T| on the fibre: max deviation {ratio:.1e};"
      f" <(yhat.v)^2>/(m^2 k^2/3) = {np.mean(yv**2)/(m**2*k**2/3):.4f}")
assert ratio < 1e-9 and abs(np.mean(yv**2) / (m**2 * k**2 / 3) - 1) < 0.03
# the part of v correlated with the level-one function q.T is along yhat (s_3 parallel to yhat)
corr = (vs * qT[:, None]).mean(0)
print("     <v^mu (q.T)> =", np.round(corr, 5), " (only the time component is nonzero)")
assert np.abs(corr[1:]).max() < 0.02 * abs(corr[0])
# bound: alpha = f yhat, tree = (rho/4g^2) m^2 q^2 <alpha.alpha> = -(rho/4g^2) m^2 k^2 <f^2>,
# t = 2m <f yhat.v>, sigma = -t/2m^2; Cauchy-Schwarz <f^2> >= <f yhat.v>^2/<(yhat.v)^2>
rho, g, mm, kk, sig = sp.symbols("rho g m k sigma", positive=True)
fyv = -sig * mm  # <f yhat.v> = t/2m = -m sigma
f2min = fyv**2 / (mm**2 * kk**2 / 3)
tree_max = sp.simplify(-(rho / (4 * g**2)) * mm**2 * kk**2 * f2min)
print("     frozen tree form in the y y channel <=", tree_max, " (phase-averaged; equality at f proportional to q.T)")
A_, pi = sp.symbols("A pi", positive=True)
L_ = 32 * sp.pi**2 * mm**6 / A_
varpi = 8 * sp.pi**2 * rho * mm**6 / (g**2 * A_)
Ptree = sp.simplify(tree_max / (4 * mm**4 * sig**2))  # coefficient of t^2, t = -2 m^2 sigma
shift = sp.simplify(4 * Ptree * L_)  # q_*^2 contribution of a phase-averaged term P t^2 is 4 P L
print("     its contribution to the constant of the first pole:", shift, "=", sp.simplify(shift / (varpi / mm**2)), "* varpi/m^2")
assert sp.simplify(shift + 3 * varpi / mm**2) == 0
print("all checks passed")
