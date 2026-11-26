"""
076 / s2.  Static response of the two scalar singlets (eps_1 on T, eps_y on P T) at the frozen base point y0
(y^i = 0), static q = k e_3 (q.y0 = 0), with the recorded matter coupling, in the normalisation of the identity
of the paragraph on the tadpole of the static scalar channel (exact sympy algebra).

Units: Ft = (L/2m^4) x (density), so that the induced kinetic term of sigma_1 is q^2 sigma_1^2 and a density
coefficient C of sigma_1^2 enters as (L/2m^4) C.  Inputs (from s1 and the recorded forms):
  sigma_1 = -(4 eps_1 + eps_y);
  tree density (rho_M/2g^2)(l^2+m^2) [ (6 + lam q^2) eps_1^2 + 2 eps_1 eps_y ],  lam = 2 m^2/3   (s1);
  r := (L/2m^4)(rho_M/2g^2)(l^2+m^2) = vartheta varpi/m^2, L = 32 pi^2 m^6/A, varpi = 8 pi^2 rho_M m^6/(g^2 A),
       vartheta = (l^2+m^2)/m^2;
  loop and induced terms through sigma_1 alone:  (q^2 + mu) sigma_1^2  (hypothesis H_n), with
       mu = (L/2m^4) Sum_{non-tree}(C_i - T_i) + q_*^2|_chi;
  dust source coupled to h_beta^{00}, h_beta = dgamma - (beta_K/2) eta t, dgamma^{mu nu} = m^2 (kappa + kappa^T)^{mu nu}
       for X = (1 + kappa) T, kappa = eps_1 + eps_y P.
Run:  python -I s2_static_singlet_response.py
"""
import sympy as sp
import numpy as np

q2, mu, r, lam, bK, J = sp.symbols("q2 mu r lam beta_K J", real=True)
e1, ey, sg, z = sp.symbols("eps_1 eps_y sigma z", real=True)
m, ell, rhoM, g, A, pi = sp.symbols("m ell rho_M g A pi", positive=True)

# 1. r = vartheta varpi / m^2
Lc = 32 * sp.pi**2 * m**6 / A
varpi = 8 * sp.pi**2 * rhoM * m**6 / (g**2 * A)
vth = (ell**2 + m**2) / m**2
r_expr = Lc / (2 * m**4) * rhoM / (2 * g**2) * (ell**2 + m**2)
print("1. r - vartheta varpi/m^2 =", sp.simplify(r_expr - vth * varpi / m**2))
assert sp.simplify(r_expr - vth * varpi / m**2) == 0

# metric data of the singlets
eta = sp.diag(-1, 1, 1, 1)
P = sp.zeros(4, 4); P[0, 0] = 1                      # P^a_b
kap = e1 * sp.eye(4) + ey * P
dgam = m**2 * (kap * eta.inv() + (kap * eta.inv()).T)  # dgamma^{mu nu}
t = sp.expand(sum(eta[a, a] * dgam[a, a] for a in range(4)))
sig1 = sp.expand(-t / (2 * m**2))
print("   sigma_1 =", sig1, "; dgamma^00 =", sp.expand(dgam[0, 0]), "; dgamma^11 =", sp.expand(dgam[1, 1]))
assert sp.expand(sig1 + 4 * e1 + ey) == 0
hb = dgam - bK / 2 * eta.inv() * t
src = sp.expand(hb[0, 0] / (2 * m**2))                # source per J
print("   h_beta^00/2m^2 =", sp.collect(src, [e1, ey]))

# quadratic form Ft in (eps_1, eps_y)
tree = r * ((6 + lam * q2) * e1**2 + 2 * e1 * ey)
Ft = (q2 + mu) * sig1**2 + tree
# 2. basis (sigma, z): (eps_1, eps_y) = x (1,0) + z (1,-4), sigma = -4x
sub_sz = {e1: -sg / 4 + z, ey: -4 * z}
tree_sz = sp.expand(tree.subs(sub_sz))
print("2. tree form in (sigma, z):", sp.collect(tree_sz, [sg, z]))
cz2 = tree_sz.coeff(z, 2); czs = tree_sz.coeff(z, 1).coeff(sg, 1); cs2 = tree_sz.coeff(sg, 2).subs(z, 0)
schur = sp.simplify(cs2 - czs**2 / (4 * cz2))
print("   Schur complement of the tree form over z at fixed sigma:", sp.factor(schur), "(expect r/(2 - lam q2))")
assert sp.simplify(schur - r / (2 - lam * q2)) == 0
print("   at q=0:", schur.subs(q2, 0), "; first order in q2:", sp.series(schur, q2, 0, 2).removeO())
# stationary combination at q=0
zs = sp.solve(sp.diff(tree_sz.subs(q2, 0), z), z)[0]
e1s, eys = sp.simplify((-sg / 4 + z).subs(z, zs)), sp.simplify((-4 * z).subs(z, zs))
print("   stationary z at q=0:", zs, "-> eps_1 =", e1s, ", eps_y =", eys)
assert sp.simplify(zs + sg / 4) == 0 and sp.simplify(e1s + sg / 2) == 0 and sp.simplify(eys - sg) == 0
dg_s = dgam.subs({e1: e1s, ey: eys})
t_s = sp.simplify(t.subs({e1: e1s, ey: eys}))
hb_s = sp.simplify(hb.subs({e1: e1s, ey: eys}))
print("3. on it: dgamma =", [sp.simplify(dg_s[i, i]) for i in range(4)], "(isotropic: -m^2 sigma delta^{mu nu});",
      "t =", t_s, "; h_beta^11/h_beta^00 =", sp.simplify(hb_s[1, 1] / hb_s[0, 0]))
assert all(sp.simplify(dg_s[i, i] + m**2 * sg) == 0 for i in range(4))
assert sp.simplify(hb_s[1, 1] / hb_s[0, 0] - (1 - bK) / (1 + bK)) == 0
# non-derivative eigen-directions of L, for the record: L T = 6T, L((1-4P)T) = -2 (1-4P)T
n_src = sp.expand(src.subs({e1: 1, ey: -4}))
d_src = sp.expand(src.subs({e1: 1, ey: 0}))
print("4. charge of the sigma_1-neutral singlet (1-4P)T:", n_src, "(no beta_K); of the dilatation T:", d_src,
      "; of the rescaling P T:", sp.expand(src.subs({e1: 0, ey: 1})))
assert n_src == 6 / sp.Integer(2) * 1 and sp.expand(n_src - 3) == 0

# 4b. the y y channel alone (eps_1 = 0) reproduces the recorded response -L rho0^2 (1 - beta_K/2)^2 / (q^2 + mu)
v = sp.Matrix([e1, ey])
Mfull = sp.hessian(Ft, v) / 2
c = sp.Matrix([sp.diff(src, e1), sp.diff(src, ey)])
Gyy = sp.simplify(c[1]**2 / Mfull[1, 1])
print("   y y channel alone: c^2/M =", sp.factor(Gyy), " (response -L rho0^2 c^2/M with J = 2 L rho0/m^2)")
assert sp.simplify(Gyy - (1 - bK / 2)**2 / (q2 + mu)) == 0

# 5. full static response Gamma = c^T M^{-1} c, poles
Gam = sp.simplify((c.T * Mfull.inv() * c)[0])
num, den = sp.fraction(sp.factor(Gam))
print("5. Gamma(q2) = c^T M^-1 c ; denominator:", sp.factor(den))
detM = sp.factor(Mfull.det())
print("   det M =", detM)
target = sp.expand(-r * ((q2 + mu) * (2 - lam * q2) + r))
assert sp.simplify(sp.expand(Mfull.det()) - target) == 0
roots = sp.solve(sp.Eq((q2 + mu) * (2 - lam * q2) + r, 0), q2)
prod_roots = sp.simplify(roots[0] * roots[1])
print("   pole condition (q2 + mu)(2 - lam q2) + r = 0; product of the roots =", prod_roots,
      "; sum =", sp.simplify(roots[0] + roots[1]))
assert sp.simplify(prod_roots + (2 * mu + r) / lam) == 0
# minimal model mu = 0: roots
rt0 = [sp.simplify(x.subs(mu, 0)) for x in roots]
print("   mu = 0:", rt0, " with lam r = (2/3) vartheta varpi")
# 6. eliminate z with the source at q = 0: effective sigma form
Fsz = sp.expand((Ft - J * src).subs(sub_sz).subs(q2, 0))
zsol = sp.solve(sp.diff(Fsz, z), z)[0]
Feff = sp.expand(Fsz.subs(z, zsol))
print("6. q=0, z eliminated with the source: z =", sp.simplify(zsol), "; Ft_eff =", sp.collect(Feff, [sg, J]))
assert sp.simplify(Feff.coeff(sg, 2) - (mu + r / 2)) == 0
assert sp.simplify(Feff.coeff(sg, 1) - J * (1 + bK) / 2) == 0
assert sp.simplify(Feff.subs(sg, 0) - 9 * J**2 / (8 * r)) == 0

# 7. a positive kinetic matrix and an indefinite q=0 form force a pole at q2 > 0 (random checks, extra PSD kinetic)
rng = np.random.default_rng(3)
cnt = 0
for _ in range(2000):
    rv, lv, mv = rng.uniform(0.01, 50), rng.uniform(0.05, 5), rng.uniform(-20, 20)
    if mv + rv / 2 <= 0:
        continue
    Bx = rng.normal(size=(2, 2)); Kx = Bx @ Bx.T * rng.uniform(0, 3)
    s4 = np.array([4., 1.])
    M0 = mv * np.outer(s4, s4) + rv * np.array([[6, 1], [1, 0]])
    K1 = np.outer(s4, s4) + rv * lv * np.array([[1, 0], [0, 0]]) + Kx
    # det(M0 + x K1) = 0, quadratic in x
    a2 = np.linalg.det(K1); a0 = np.linalg.det(M0)
    a1 = np.linalg.det(M0 + K1) - a2 - a0
    rts = np.roots([a2, a1, a0])
    assert a0 < 0 and np.sum((np.abs(rts.imag) < 1e-12) & (rts.real > 0)) == 1
    cnt += 1
print(f"7. det(M0) < 0 at q=0 and exactly one root q2 > 0 for {cnt} random cases with mu + r/2 > 0 and an extra PSD kinetic term")
print("   exact: det M0 =", sp.factor(Mfull.subs(q2, 0).det()), "< 0 for r > 0 whenever 2 mu + r > 0")

# 8. general loop entries on the singlet sector, with the value mu on the y y channel held (identity of the
#    paragraph on the tadpole): z' = z - sigma/4 is the deviation from the y y channel at fixed sigma.
b, nu, zp = sp.symbols("b nu zp", real=True)
tree_zp = sp.expand(tree_sz.subs(q2, 0).subs(z, zp + sg / 4))
print("8. tree form at q=0 in (sigma, z'):", tree_zp, "(the y y channel z'=0 gives 0)")
assert sp.expand(tree_zp - r * (-2 * sg * zp - 2 * zp**2)) == 0
F8 = sp.expand(tree_zp + mu * sg**2 + 2 * b * sg * zp + nu * zp**2)
sch8 = sp.simplify(F8.coeff(sg, 2).subs(zp, 0) - F8.coeff(zp, 1).coeff(sg, 1)**2 / (4 * F8.coeff(zp, 2)))
print("   q=0 constant after eliminating the neutral singlet:", sch8, "; its excess over mu:", sp.factor(sch8 - mu))
assert sp.simplify(sch8 - (mu - (b - r)**2 / (nu - 2 * r))) == 0
print("   so it exceeds the y y value mu only if nu - 2r < 0, the neutral singlet's own coefficient being negative;"
      " b = nu = 0 gives mu + r/2")
assert sp.simplify(sch8.subs({b: 0, nu: 0}) - (mu + r / 2)) == 0
# random check: no static pole at q2 >= 0 (both poles of Yukawa sign) => mu > 0 and constant <= mu
ok, n_ok = True, 0
for _ in range(20000):
    rv = rng.uniform(0.01, 20); mv = rng.uniform(-10, 10); bv = rng.uniform(-20, 20); nv = rng.uniform(-40, 40)
    lv = rng.uniform(0.05, 5)
    Bx = rng.normal(size=(2, 2)); Kx = Bx @ Bx.T * rng.uniform(0, 2)
    # basis (sigma, z'): eps_1 = -sigma/4 + z' + sigma/4 = z', eps_y = -4 z' - sigma
    M0 = np.array([[mv, bv - rv], [bv - rv, nv - 2 * rv]])
    # kinetic: q2 sigma^2 + r lam eps_1^2 = q2 (sigma^2 + r lam z'^2) + PSD extra
    K1 = np.array([[1, 0], [0, rv * lv]]) + Kx
    a2 = np.linalg.det(K1); a0 = np.linalg.det(M0); a1 = np.linalg.det(M0 + K1) - a2 - a0
    rts = np.roots([a2, a1, a0])
    nonneg = np.any((np.abs(rts.imag) < 1e-9) & (rts.real >= -1e-12))
    if not nonneg:
        n_ok += 1
        schv = mv - (bv - rv)**2 / (nv - 2 * rv)
        ok = ok and mv > 0 and schv <= mv + 1e-9 and nv - 2 * rv > 0
print(f"   {n_ok} random cases with a positive-definite kinetic matrix and no static pole at q2 >= 0:"
      f" all have mu > 0, nu > 2r and a constant <= mu: {ok}")
assert ok and n_ok > 100

# 9. Yukawa condition against the exchange of chi, with the other entries set to zero
Up, Ucc, CT = sp.symbols("Uprime U_chichi C_tree", positive=True)
qchi = -Lc * Up**2 / (4 * m**4 * Ucc)
lhs = Lc / (2 * m**4) * CT
print("9. (L/2m^4) C_tree + q_*^2|chi =", sp.factor(sp.simplify(lhs + qchi)), "-> positive iff C_tree > U'^2/(2 U_chichi)")
assert sp.simplify((lhs + qchi) - Lc / (2 * m**4) * (CT - Up**2 / (2 * Ucc))) == 0
Cstat = rhoM / (4 * g**2) * (ell**2 + m**2)
print("   C_tree on the stationary combination = (rho_M/4g^2)(l^2+m^2); (L/2m^4) C_tree - vartheta varpi/(2m^2) =",
      sp.simplify(Lc / (2 * m**4) * Cstat - vth * varpi / (2 * m**2)))
assert sp.simplify(Lc / (2 * m**4) * Cstat - vth * varpi / (2 * m**2)) == 0

# 10. massless limit mu = -r/2: the null vector of M(0) is the stationary combination
M00 = Mfull.subs({q2: 0, mu: -r / 2})
ns_ = M00.nullspace()[0]
print("10. mu = -r/2: null vector of M(0) (eps_1, eps_y) ~", list(sp.simplify(ns_ / ns_[1])), "(expect (-1/2, 1))")
assert sp.simplify(ns_[0] / ns_[1] + sp.Rational(1, 2)) == 0
# 11. the linearised Einstein-Hilbert form on the singlet metric data, for static q (not the induced form of the class)
qv = sp.Matrix([0, 0, 0, sp.Symbol("k", positive=True)])  # q_mu lower
etaU = eta.inv()
hU = dgam  # h^{mu nu}
hL = eta * hU * eta
def contr(X, Y_):
    return sum(X[i, j] * Y_[i, j] for i in range(4) for j in range(4))
qq = (qv.T * etaU * qv)[0]
tr_h = sum(eta[i, j] * hU[i, j] for i in range(4) for j in range(4))
qh = hU * qv  # (q.h)^mu
EH = sp.expand(-sp.Rational(1, 2) * qq * contr(hU, hL) + (qh.T * eta * qh)[0] - (qv.T * hU * qv)[0] * tr_h
               + sp.Rational(1, 2) * qq * tr_h**2)
print("11. Fierz-Pauli form on h = dgamma(eps_1, eps_y), static q:", sp.factor(EH))
xi = sp.Matrix(sp.symbols("xi0:4"))
hg = qv * xi.T + xi * qv.T  # pure gauge h_{mu nu} (lower), raise
hgU = etaU * hg * etaU
trg = sum(eta[i, j] * hgU[i, j] for i in range(4) for j in range(4))
qhg = hgU * qv
EHg = sp.expand(-sp.Rational(1, 2) * qq * contr(hgU, eta * hgU * eta) + (qhg.T * eta * qhg)[0] - (qv.T * hgU * qv)[0] * trg
                + sp.Rational(1, 2) * qq * trg**2)
print("    gauge check (form on a pure-gauge h):", EHg)
assert EHg == 0
assert sp.expand(EH - 4 * m**4 * qq * (3 * e1**2 + 2 * e1 * ey)) == 0
print("    = 4 m^4 q^2 (3 eps_1^2 + 2 eps_1 eps_y): indefinite (det [[3,1],[1,0]] = -1), zero on the y y channel")
print("all checks passed")
