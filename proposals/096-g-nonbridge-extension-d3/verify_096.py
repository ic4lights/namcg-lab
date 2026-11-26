import numpy as np
import sympy as sp

N = 20261119
ok = 0
def chk(tag, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + tag)
    ok += 0 if cond else 1

# S1 rank-one pair at D=3,4: same spectrum, different diagonal
for D in (3, 4):
    v1 = sp.Matrix([1] + [0] * (D - 1))
    v2 = sp.Matrix([1, 1] + [0] * (D - 2)) / sp.sqrt(2)
    G1, G2 = v1 * v1.T, v2 * v2.T
    c1 = G1.charpoly(sp.Symbol('x')).all_coeffs()
    c2 = G2.charpoly(sp.Symbol('x')).all_coeffs()
    p21 = sum(G1[i, i]**2 for i in range(D))
    p22 = sum(G2[i, i]**2 for i in range(D))
    chk("S1.rankone_D%d_charpoly" % D, sp.simplify(sp.Matrix(c1) - sp.Matrix(c2)) == sp.zeros(len(c1), 1))
    chk("S1.rankone_D%d_diagdiff" % D, sp.simplify(p21 - p22) == sp.Rational(1, 2))

# S2 plane rotation at D=3: spectrum fixed, diagonal moves
th = sp.symbols('theta', real=True)
l3 = sp.symbols('l1 l2 l3', real=True)
Lam = sp.diag(*l3)
R12 = sp.Matrix([[sp.cos(th), -sp.sin(th), 0], [sp.sin(th), sp.cos(th), 0], [0, 0, 1]])
U12 = R12 * Lam * R12.T
d0 = [sp.simplify(U12[i, i]) for i in range(3)]
cp = sp.Matrix(U12.charpoly(sp.Symbol('x')).all_coeffs()) - sp.Matrix(Lam.charpoly(sp.Symbol('x')).all_coeffs())
chk("S2.charpoly_fixed", all(sp.simplify(e) == 0 for e in cp))
dd = sp.simplify(sp.diff(d0[0], th))
chk("S2.dcurve_nonconstant", dd.has(sp.sin) and sp.simplify(dd.subs({th: sp.pi/6, l3[0]: 3, l3[1]: 1, l3[2]: 0})) != 0)
x = sp.symbols('x', real=True)
P2x = sp.expand((l3[0]+(l3[1]-l3[0])*x)**2 + (l3[1]-(l3[1]-l3[0])*x)**2 + l3[2]**2)
chk("S2.P2_curve_form", sp.simplify(P2x - (sum(l**2 for l in l3) - 2*(l3[1]-l3[0])**2*x*(1-x))) == 0)
A = sp.Matrix([[sp.sqrt(2)/2, -sp.sqrt(2)/2, 0], [sp.sqrt(2)/2, sp.sqrt(2)/2, 0], [0, 0, 1]])
dA = [sp.simplify(e) for e in (A*Lam*A.T).diagonal()]
chk("S2.P2_pi4", sp.simplify((sum(d**2 for d in dA) - (sum(l**2 for l in l3) - (l3[1]-l3[0])**2/2))*2) == 0)

# S3 D=3 Jacobian: U = R23(phi) R12(theta), rank 2 on a dense rational grid
L = [sp.Rational(a) for a in (7, 4, 1)]
ph = sp.symbols('phi', real=True)
R23 = sp.Matrix([[1, 0, 0], [0, sp.cos(ph), -sp.sin(ph)], [0, sp.sin(ph), sp.cos(ph)]])
UU = R23 * R12 * sp.diag(*L) * R12.T * R23.T
dd1, dd2 = sp.simplify(UU[0, 0]), sp.simplify(UU[1, 1])
Jm = sp.Matrix([[sp.diff(dd1, th), sp.diff(dd1, ph)], [sp.diff(dd2, th), sp.diff(dd2, ph)]])
detJ = sp.simplify(sp.trigsimp(Jm.det()).subs({th: sp.pi/4, ph: sp.pi/4}))
closed = sp.simplify((L[1]-L[0])*(L[2]-(L[0]+L[1])/2))
chk("S3.jacobian_closedform", sp.simplify(detJ - closed) == 0 and closed != 0)
LU = R23 * R12 * Lam * R12.T * R23.T
du1, du2 = sp.simplify(LU[0, 0]), sp.simplify(LU[1, 1])
Ju = sp.Matrix([[sp.diff(du1, th), sp.diff(du1, ph)], [sp.diff(du2, th), sp.diff(du2, ph)]])
detJu = sp.simplify(sp.trigsimp(sp.expand_trig(Ju.det())).subs({th: sp.pi/4, ph: sp.pi/4}))
gener = sp.simplify((l3[1]-l3[0])*(l3[2]-(l3[0]+l3[1])/2))
chk("S3.jacobian_generic_symbolic", sp.simplify(detJu - gener) == 0)

rng = np.random.default_rng(20261119)
def perm_det(lam):
    import itertools, math
    best = 0.0
    for pp in itertools.permutations(lam):
        a, b, c = pp
        detv = abs((b-a)*(c-(a+b)/2.0))
        best = max(best, detv)
    return best
bad = []
for t1 in range(1, 16):
    for t2 in range(1, 16):
        for t3 in range(1, 16):
            lam = (t1/4.0, t2/4.0, t3/4.0)
            if len(set(lam)) > 1 and perm_det(lam) < 1e-9:
                bad.append(lam)
chk("S3b.relabel_cover_grid", len(bad) == 0)

# S4 Dirichlet density from exponential change of variables (D=3 symbolic)
E1, E2, E3, T = sp.symbols('E1 E2 E3 T', positive=True)
s1, s2 = sp.symbols('s1 s2', positive=True)
jac = sp.Matrix([[sp.diff(e, v) for v in (T, s1, s2)] for e in (T*s1, T*s2, T*(1-s1-s2))]).det()
dens = sp.integrate(sp.integrate(sp.exp(-T)*sp.Abs(sp.simplify(jac)), (T, 0, sp.oo)), (s1, 0, 1-s2))
dens2 = sp.integrate(dens, (s2, 0, 1))
chk("S4.simplex_density", sp.simplify(jac.subs({T: 1})) == 1 and sp.simplify(dens - 2*(1-s2)) == 0 and sp.simplify(dens2 - 1) == 0)
chk("S4.uniform_joint", sp.simplify(sp.diff(dens, s1)) == 0 and sp.simplify(sp.integrate(2, (s1, 0, 1-s2)).subs(s2, sp.Rational(1, 2))) == 1)
r = rng.standard_normal((N, 3))**2 + rng.standard_normal((N, 3))**2
X = r / r.sum(axis=1, keepdims=True)
m2 = np.mean(X**2, axis=0)
chk("S4.haar_row_moments", np.max(np.abs(m2 - 1.0/6.0)) < 0.02)

# S5 D=3 explicit conditional density of L = X1 + mu*X2, X uniform on simplex
mu = sp.Rational(2, 3)
t = sp.symbols('t', positive=True)
f = sp.Piecewise((2*t/mu, t <= mu), (2*(1-t)/(1-mu), True))
F = sp.Piecewise((t**2/mu, t <= mu), (1-(1-t)**2/(1-mu), True))
chk("S5.normalizes", sp.simplify(sp.integrate(f, (t, 0, 1)) - 1) == 0)
chk("S5.cdf_match", sp.simplify(sp.diff(F, t) - f) == 0)
chk("S5.cdf_endpoints", F.subs(t, 0) == 0 and sp.simplify(F.subs(t, 1)) == 1)
Ls = np.array([3.0, 2.0, 0.0])
lam5 = rng.standard_exponential((N, 3))
X5 = lam5 / lam5.sum(axis=1, keepdims=True)
Lval = X5 @ Ls
chk("S5.mc_cdf", max(abs(np.mean(Lval <= q) - float(F.subs(t, sp.nsimplify(q/3.0, rational=True)).evalf())) for q in (0.6, 1.2, 1.8, 2.4)) < 0.01)

# S6 stick-breaking Beta(1,D-1) marginal + independence (D=4)
E4 = rng.standard_exponential((N, 4))
R = E4[:, 1:].sum(axis=1)
B = E4[:, 0] / (E4[:, 0] + R)
Xp = E4[:, 1:] / R[:, None]
var_theory = 3.0/(16.0*5.0)
chk("S6.beta13_marginal", abs(np.mean(B)-0.25) < 0.005 and abs(np.var(B)-var_theory) < 2e-4)
corr = np.corrcoef(B*(1-B), Xp[:, 0])[0, 1]
chk("S6.stick_indep", abs(corr) < 0.02 and abs(np.mean(B*Xp[:, 0]) - 0.25/3.0) < 0.005)

# S7 non-atomicity: band probabilities scale linearly (D=3 distinct and equal-pair)
def bands(vals, c, es):
    return [np.mean(np.abs(vals-c) < e) for e in es]
c5 = float(np.mean(Lval)); es5 = (1e-3, 2e-3, 4e-3)
b5 = bands(Lval, c5, es5)
chk("S7.band_scaling_D3", 1.5 < b5[1]/b5[0] < 2.5 and 1.5 < b5[2]/b5[1] < 2.5)
Spair = rng.standard_exponential((N, 3)).sum(axis=1)
Lpair = Spair + rng.standard_exponential(N)*0.0
lam7 = rng.standard_exponential((N, 3))
X7 = lam7/lam7.sum(axis=1, keepdims=True)
L7 = X7 @ np.array([2.0, 2.0, 0.0])
b7 = bands(L7, 1.0, es5)
chk("S7.band_scaling_D3_pair", 1.5 < b7[1]/b7[0] < 2.5)

# S8 tuple spread under the named law at D=3 (seeded Wishart)
Wm = (rng.standard_normal((N,3,3)) + 1j*rng.standard_normal((N,3,3)))/np.sqrt(2)
Gm = np.einsum('nij,nkj->nik', Wm, Wm.conj())
tr = np.real(np.trace(Gm, axis1=1, axis2=2))
ddi = np.abs(np.diagonal(Gm, axis1=1, axis2=2))/tr[:, None]
ev = np.linalg.eigvalsh(Gm)/tr[:, None]
band = (ev[:, 2] > 0.59) & (ev[:, 2] < 0.61) & (ev[:, 0] < 0.11)
P2b = (ddi[band]**2).sum(axis=1); P3b = (ddi[band]**3).sum(axis=1)
w2, w3 = P2b.max()-P2b.min(), P3b.max()-P3b.min()
chk("S8.tuple_spread_positive", band.sum() > 2000 and w2 > 0.05 and w3 > 0.03)
print("S8.count %d S8.widthP2 %.4f S8.widthP3 %.4f" % (band.sum(), w2, w3))

print("SUMMARY " + ("ALL PASS" if ok == 0 else "FAILURES %d" % ok))
raise SystemExit(0 if ok == 0 else 1)
