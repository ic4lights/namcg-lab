"""
Proposal 059 (local round 2), check E1: equivariant S^2 toy, exact sympy.

Class relations of Appendix H, Problem D ("First-order equivariant class"),
compact toy: Euclidean contraction delta_ab, structure group SO(2):
  (I)  [S_cd, D_a] = d_ad D_c - d_ac D_d
  (II) [D_a, D_b]  = -T_ab^c D_c + 1/2 R_ab^cd S_cd + F_ab
Base: unit S^2, e_1 = d_th, e_2 = csc(th) d_ph, omega^12 = -cos(th) d ph,
fibre angle psi, xi = d_psi.  Frame bundle Z = SO(3), coordinates (th,ph,psi).

Checks:
 (A) non-equivariant lifts Eh_a = e_a - omega_a xi (the r3 toy): [xi,Eh_a]=0,
     so (I) fails for every S_12 = s xi; [Eh_1,Eh_2] = -cot Eh_2 - xi; the xi
     coefficient is -1 in basis (Eh_a, xi) and -csc^2 in basis (e_a, xi).
 (B) equivariant lifts D_a = u_a^b Eh_b, u = rotation by psi with orientation
     sgn; T = 0 fixes sgn = -1, u = [[cos, -sin],[sin, cos]] (sgn = +1 has
     T != 0); then (I) holds with S_12 = +xi (and fails for -xi), (II) holds
     with T = 0, R_12^12 = -1, F = 0 (constant coefficients), i.e.
     [D_1,D_2] = -S_12.  Hermiticity term t_a = 0 (divergence-free in
     sin(th) dth dph dpsi).  Ricci: -R_ab^ae = +delta (unit sphere).
 (C) local rotation: [lam S_12, D_a] = lam^c_a D_c - (D_a lam) S_12 for
     generic real lam(th,ph) (lam^12 = lam, det u = 1).
 (D) lifted Killing fields rhot_i = rho_i + c_i xi, rho_i = eps_ijk x_j d_k:
     [rhot_i, D_a] = 0, [rhot_i, xi] = 0, [rhot_i,rhot_j] = -eps_ijk rhot_k;
     bundle redundancy sum_i x_i rhot_i = -xi = -S_12 (vertical),
     base redundancy sum_i x_i rho_i = 0.
 (E) Casimir identity on generic f(th,ph,psi):
     sum_i rhot_i^2 = D_1^2 + D_2^2 + S_12^2;
     on psi-independent f: D_1^2 + D_2^2 = Laplace-Beltrami of S^2;
     -(D_1^2+D_2^2) Y_lm = l(l+1) Y_lm for l <= 4, all 2l+1 values of m.
Run:  python -I d1_equivariant_toy_symbolic.py
"""
import sympy as sp

th, ph, ps = sp.symbols("theta phi psi", real=True)
X = (th, ph, ps)
res = []


def rep(ok, name):
    res.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + name)


def simp(e):
    return sp.simplify(sp.trigsimp(sp.expand(e)))


class V:
    def __init__(self, *c):
        self.c = [simp(x) for x in c]

    def __call__(self, f):
        return sum(ci * sp.diff(f, xi) for ci, xi in zip(self.c, X))

    def br(self, o):
        return V(*[self(o.c[k]) - o(self.c[k]) for k in range(3)])

    def __add__(self, o):
        return V(*[a + b for a, b in zip(self.c, o.c)])

    def __sub__(self, o):
        return V(*[a - b for a, b in zip(self.c, o.c)])

    def sc(self, g):
        return V(*[g * a for a in self.c])

    def zero(self):
        return all(simp(a) == 0 for a in self.c)


def decompose(W, basis):
    """Solve W = sum k_i basis_i pointwise (basis = 3 vector fields)."""
    M = sp.Matrix([[b.c[r] for b in basis] for r in range(3)])
    k = M.LUsolve(sp.Matrix(W.c))
    return [simp(x) for x in k]


xi = V(0, 0, 1)
e1 = V(1, 0, 0)
e2 = V(0, 1 / sp.sin(th), 0)
w = [sp.Integer(0), -sp.cos(th) / sp.sin(th)]          # omega^12(e_a)
Eh = [e1 - xi.sc(w[0]), e2 - xi.sc(w[1])]

# (A) non-equivariant lifts
rep(xi.br(Eh[0]).zero() and xi.br(Eh[1]).zero(),
    "(A) [xi, Eh_a] = 0: relation (I) fails for S_12 = s*xi, any s")
c = decompose(Eh[0].br(Eh[1]), [Eh[0], Eh[1], xi])
rep(c[0] == 0 and simp(c[1] + sp.cot(th)) == 0 and c[2] == -1,
    "(A) [Eh_1,Eh_2] = -cot(th) Eh_2 - xi (xi-coefficient -1 in basis (Eh_a,xi))")
c = decompose(Eh[0].br(Eh[1]), [e1, e2, xi])
rep(simp(c[2] + 1 / sp.sin(th) ** 2) == 0,
    "(A) xi-coefficient of [Eh_1,Eh_2] in basis (e_a,xi) is -csc^2(th): basis dependent")

# (B) equivariant lifts
def lifts(sgn):
    u = sp.Matrix([[sp.cos(ps), sgn * sp.sin(ps)], [-sgn * sp.sin(ps), sp.cos(ps)]])
    D = [Eh[0].sc(u[a, 0]) + Eh[1].sc(u[a, 1]) for a in range(2)]
    return u, D

Tzero = {}
for sgn in (1, -1):
    u, D = lifts(sgn)
    k = decompose(D[0].br(D[1]), [D[0], D[1], xi])
    Tzero[sgn] = (k[0] == 0 and k[1] == 0)
    print(f"info  sgn={sgn:+d}: [D_1,D_2] = ({k[0]}) D_1 + ({k[1]}) D_2 + ({k[2]}) xi")
rep(Tzero[-1] and not Tzero[1],
    "(B) T = 0 fixes the orientation: u_a^b = [[cos psi, -sin psi],[sin psi, cos psi]] (sgn=-1); sgn=+1 has T != 0")

u, D = lifts(-1)
d = sp.eye(2)
# relation (I) with S_12 = sigma*xi: find sigma
sigma = None
for s_ in (1, -1):
    S_try = xi.sc(s_)
    if all((S_try.br(D[a]) - (D[0].sc(d[a, 1]) - D[1].sc(d[a, 0]))).zero() for a in range(2)):
        sigma = s_
rep(sigma is not None, f"(B) relation (I): [S_12,D_1] = -D_2, [S_12,D_2] = D_1 with S_12 = ({sigma}) xi")
rep(all(not (xi.sc(-sigma).br(D[a]) - (D[0].sc(d[a, 1]) - D[1].sc(d[a, 0]))).zero() for a in range(2)),
    "(B) relation (I) fails for S_12 = -sigma*xi: the sign of S_12 is fixed relative to the lift")
S = xi.sc(sigma)
k = decompose(D[0].br(D[1]), [D[0], D[1], S])
rep(k[0] == 0 and k[1] == 0, "(B) T_12^c = 0 (no D-component in [D_1,D_2])")
R1212 = k[2]
rep(R1212 == -1, "(B) [D_1,D_2] = R_12^12 S_12 with R_12^12 = -1 (constant), F_12 = 0")
# Ricci: R_ab^{ae} = -delta_b^e -> Ric = +1
rep(-R1212 == 1, "(B) Ric_b^e = -R_ab^ae = +delta_b^e (unit sphere, manuscript convention)")
okdiv = all(simp(sum(sp.diff(sp.sin(th) * Da.c[r], X[r]) for r in range(3)) / sp.sin(th)) == 0 for Da in D)
rep(okdiv, "(B) div_mu(D_a) = 0 in sin(th) dth dph dpsi: t_a = T_ac^c/2 = 0, D_a anti-Hermitian")
# su(2) form: (i D_1, i D_2, i*sigma*xi... ) check [iD_1,iD_2] = i*(i*S_12)*(-R)
rep(((D[0].br(D[1])) - S.sc(-1)).zero(), "(B) equivalently [D_1,D_2] = -S_12: (D_1, D_2, -S_12) close as so(3)")

# (C) local rotation with generic lambda(th,ph)
lam = sp.Function("lam", real=True)(th, ph)
okC = True
for a in range(2):
    lhs = S.sc(lam).br(D[a])
    # lam^{cd}: lam^{12} = lam, lam^{21} = -lam ; lam^c_a = lam^{ca}
    lamca = sp.Matrix([[0, lam], [-lam, 0]])
    rhs = D[0].sc(lamca[0, a]) + D[1].sc(lamca[1, a]) - S.sc(D[a](lam))
    okC &= (lhs - rhs).zero()
rep(okC, "(C) [lam S_12, D_a] = lam^c_a D_c - (D_a lam) S_12 for generic lam(th,ph)")

# (D) Killing fields and their lifts
x = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
# rho_i = eps_ijk x_j d/dx_k pushed to (th,ph): components via dth/dx_k, dph/dx_k
J = sp.Matrix([[sp.diff(xk, q) for q in (th, ph)] for xk in x])   # dx_k/dq
G = (J.T * J)
Jinv = (G.inv() * J.T).applyfunc(simp)                              # dq/dx_k on sphere
rho = []
for i in range(3):
    vk = [sum(sp.LeviCivita(i, j, k) * x[j] for j in range(3)) for k in range(3)]
    q = Jinv * sp.Matrix(vk)
    rho.append(V(q[0], q[1], 0))
rep(all(simp(rho[i](x[i])) == 0 for i in range(3)) and
    (rho[0].br(rho[1]) + rho[2]).zero(),
    "(D) rho_i = eps_ijk x_j d_k tangent, [rho_1,rho_2] = -rho_3")
# lifts: the d_psi components below solve [rho_i + c_i xi, D_a] = 0 (the
# bracket's D-components force c_i, its xi-component is then checked to vanish)
cvals = [-sp.cos(ph) / sp.sin(th), -sp.sin(ph) / sp.sin(th), sp.Integer(0)]
rhot = []
for i in range(3):
    rhot.append(rho[i] + xi.sc(cvals[i]))
    print(f"info  rhot_{i+1} = rho_{i+1} + ({cvals[i]}) xi ;  rho_{i+1} = {rho[i].c[:2]}")
okD = all(rt.br(D[a]).zero() for rt in rhot for a in range(2)) and all(rt.br(xi).zero() for rt in rhot)
rep(okD, "(D) [rhot_i, D_a] = 0 and [rhot_i, xi] = 0 (lifts commute with the class operators)")
rep((rhot[0].br(rhot[1]) + rhot[2]).zero() and (rhot[1].br(rhot[2]) + rhot[0]).zero(),
    "(D) [rhot_i, rhot_j] = -eps_ijk rhot_k")
base_red = rho[0].sc(x[0]) + rho[1].sc(x[1]) + rho[2].sc(x[2])
rep(base_red.zero(), "(D) base redundancy sum_i x_i rho_i = 0")
bund_red = rhot[0].sc(x[0]) + rhot[1].sc(x[1]) + rhot[2].sc(x[2])
sig = simp(bund_red.c[2])
rep(simp(bund_red.c[0]) == 0 and simp(bund_red.c[1]) == 0 and sig in (1, -1),
    f"(D) bundle redundancy sum_i x_i rhot_i = ({sig}) xi = ({sig*sigma}) S_12: vertical, zero on base functions")

# (E) Casimir identity on a generic function
f = sp.Function("f")(th, ph, ps)
lhs = sum(rt(rt(f)) for rt in rhot)
rhs = D[0](D[0](f)) + D[1](D[1](f)) + xi(xi(f))
rep(simp(sp.expand(lhs - rhs)) == 0, "(E) sum_i rhot_i^2 = D_1^2 + D_2^2 + xi^2 on generic f(th,ph,psi)")
g = sp.Function("g")(th, ph)
LB = sp.diff(sp.sin(th) * sp.diff(g, th), th) / sp.sin(th) + sp.diff(g, ph, 2) / sp.sin(th) ** 2
rep(simp(D[0](D[0](g)) + D[1](D[1](g)) - LB) == 0,
    "(E) on psi-independent g: D_1^2 + D_2^2 = Laplace-Beltrami of the unit S^2")
okY = True
for l in range(5):
    for m in range(-l, l + 1):
        tt = sp.Symbol("tt")
        Pm = sp.diff(sp.legendre(l, tt), tt, abs(m)).subs(tt, sp.cos(th))
        Y = sp.exp(sp.I * m * ph) * sp.sin(th) ** abs(m) * Pm   # unnormalised Y_lm
        # D_1^2 + D_2^2 = LB on psi-independent functions (previous check, generic g)
        LBY = sp.diff(sp.sin(th) * sp.diff(Y, th), th) / sp.sin(th) + sp.diff(Y, ph, 2) / sp.sin(th) ** 2
        val = sp.simplify(-LBY - l * (l + 1) * Y)
        okY &= (val == 0)
rep(okY, "(E) ghost -(D_1^2+D_2^2) on base functions: Y_lm eigenvalue l(l+1), all 2l+1 m, l<=4")

print()
print("ALL PASS" if all(res) else "SOME FAIL")
