"""
Proposal 059, check 1 (symbolic, exact arithmetic, sympy 1.14).

Compact toy for the first-order equivariant class of Appendix H
(sec:status-D, "First-order equivariant class ..." paragraphs). Base = unit
2-sphere, structure group = SO(2) (compact stand-in for SO(3,1)),
connection = Levi-Civita. Verifies exactly:

 (1) the SO(3) fundamental (rotation) vector fields rho_i on S^2 derived
     from Cartesian coordinates, their brackets [rho_i,rho_j] =
     -eps_{ijk} rho_k, the brackets of L_pm = rho_1 +/- i rho_2 with
     CONSTANT structure coefficients, and the frame redundancy
     sum_i x_i rho_i = 0;
 (2) orthonormal frame e_1 = d_theta, e_2 = d_phi/sin(theta):
     [e_1,e_2] = -cot(theta) e_2 (torsion coefficient T_12^2 = cot(theta));
     torsion-free connection form omega^{12} = -cos(theta) d phi (check
     d theta^2 + omega^2_1 ^ theta^1 = 0 on (e_1,e_2)); curvature
     R_12^12 = e_1(w_2) - e_2(w_1) - omega^{12}([e_1,e_2]) = 1;
 (3) horizontal lifts D_a = e_a - omega_a d/du on the principal SO(2)
     bundle satisfy the full operator identity
        [D_1, D_2] = -cot(theta) D_2 - xi,   xi = d/du,
     while the vertical part of [D_1,D_2] alone is -csc^2(theta) xi,
     i.e. the commutator of two first-order operators carries a
     zeroth-order (fibre, class "S-term") part because the curvature is
     nonzero: first-order operators do not close under the commutator;
 (4) the local-rotation identity in the U(1) case,
     [lambda xi, D_a] = -(D_a lambda) xi for a generic real function
     lambda(theta,phi), the U(1) shadow of
     [1/2 lambda^{cd} S_cd, D_a] = lambda^c_a D_c - 1/2 (D_a lambda^{cd}) S_cd.

Run:  python -I d1_toy_class_symbolic.py   (stdout; saved next to it)
"""
import sympy as sp

th, ph, u = sp.symbols("theta phi u", real=True)
x, y, z = sp.symbols("x y z", real=True)

class VF3:
    """Vector field a d/dtheta + b d/dphi + c d/du."""
    def __init__(self, a, b, c=0):
        self.a = sp.simplify(sp.expand_trig(sp.expand_complex(sp.simplify(a))))
        self.b = sp.simplify(sp.expand_trig(sp.expand_complex(sp.simplify(b))))
        self.c = sp.simplify(sp.expand_trig(sp.expand_complex(sp.simplify(c))))
    def apply(self, f):
        return sp.simplify(sp.expand_trig(sp.expand_complex(sp.simplify(
            self.a*sp.diff(f, th) + self.b*sp.diff(f, ph) + self.c*sp.diff(f, u)))))
    def bracket(self, o):
        return VF3(self.apply(o.a) - o.apply(self.a),
                   self.apply(o.b) - o.apply(self.b),
                   self.apply(o.c) - o.apply(self.c))
    def __add__(self, o): return VF3(self.a+o.a, self.b+o.b, self.c+o.c)
    def __neg__(self): return VF3(-self.a, -self.b, -self.c)
    def __sub__(self, o): return self + (-o)
    def scale(self, g): return VF3(g*self.a, g*self.b, g*self.c)
    def iszero(self): return all(sp.simplify(g) == 0 for g in (self.a, self.b, self.c))

VF = VF3
res = []
def rep(ok, name, extra=""):
    res.append(ok); print(f"{'PASS' if ok else 'FAIL'}  {name}  {extra}")

# ---------- (1) rotation fields from Cartesian fundamental fields ----------
r = sp.sqrt(x**2 + y**2 + z**2)
Th, Ph = sp.acos(z/r), sp.atan2(y, x)
sub = {x: sp.sin(th)*sp.cos(ph), y: sp.sin(th)*sp.sin(ph), z: sp.cos(th)}
def sph_basis(Vx, Vy, Vz):
    a = sp.diff(Th, x)*Vx + sp.diff(Th, y)*Vy + sp.diff(Th, z)*Vz
    b = sp.diff(Ph, x)*Vx + sp.diff(Ph, y)*Vy + sp.diff(Ph, z)*Vz
    a = sp.simplify(sp.expand_trig(sp.simplify(a.subs(sub))))
    b = sp.simplify(sp.expand_trig(sp.simplify(b.subs(sub))))
    a = a.replace(sp.Abs(sp.sin(th)), sp.sin(th))   # theta in (0, pi)
    b = b.replace(sp.Abs(sp.sin(th)), sp.sin(th))
    return VF(a, b)
rho1 = sph_basis(0, -z,  y)      # rho_i = +eps_ijk x_j d/dx_k (fundamental
                                 # rotation fields; their brackets carry -eps)
rho2 = sph_basis(z,  0, -x)
rho3 = sph_basis(-y,  x, 0)
print("rho_1 =", rho1.a, "d_th +", rho1.b, "d_ph ; rho_2 =", rho2.a, "d_th +", rho2.b, "d_ph ; rho_3 =", rho3.b, "d_ph")
rep((rho1.bracket(rho2) + rho3).iszero(), "[rho_1,rho_2] = -rho_3")
rep((rho2.bracket(rho3) + rho1).iszero(), "[rho_2,rho_3] = -rho_1")
rep((rho3.bracket(rho1) + rho2).iszero(), "[rho_3,rho_1] = -rho_2")
red = VF(rho1.a*sp.sin(th)*sp.cos(ph) + rho2.a*sp.sin(th)*sp.sin(ph) + rho3.a*sp.cos(th),
         rho1.b*sp.sin(th)*sp.cos(ph) + rho2.b*sp.sin(th)*sp.sin(ph) + rho3.b*sp.cos(th))
rep(red.iszero(), "frame redundancy  x_i rho_i = 0")
Lp = rho1 + rho2.scale(sp.I); Lm = rho1 - rho2.scale(sp.I); L3 = rho3
rep((Lp.bracket(Lm) - L3.scale(2*sp.I)).iszero(), "[L_+,L_-] = 2i L_3  (constant structure coefficients)")

# ---------- (2) orthonormal frame, connection, curvature ----------
e1 = VF(1, 0); e2 = VF(0, 1/sp.sin(th))
cofe2 = sp.simplify((e1.bracket(e2)).b / e2.b)     # [e1,e2] = cofe2 e2
T12 = sp.simplify(-cofe2)                          # [e_a,e_b] = -T_ab^c e_c
rep(sp.simplify(T12 - sp.cos(th)/sp.sin(th)) == 0, "T_12^2 = cot(theta)",
    f"([e_1,e_2] = {cofe2} e_2)")
w1, w2 = sp.Integer(0), -sp.cos(th)/sp.sin(th)     # omega^{12} = w_a theta^a
R12 = sp.simplify(e1.apply(w2) - e2.apply(w1) - w2*cofe2)
rep(sp.simplify(R12 - 1) == 0, "R_12^12 = e_1(w_2) - e_2(w_1) - omega^{12}([e_1,e_2]) = 1", f"(value {R12})")
# torsion-free: d theta^2(e1,e2) + (omega^2_1 ^ theta^1)(e1,e2) = 0 ; omega^2_1 = -omega^{12}
dth2_12 = sp.diff(sp.sin(th), th)*(1/sp.sin(th))   # d(sin th dphi)(e1,e2)
w21_2 = -w2
tors12 = sp.simplify(dth2_12 - w21_2)
rep(tors12 == 0, "torsion-free: d theta^2 + omega^2_1 ^ theta^1 vanishes on (e_1,e_2)", f"({dth2_12} - {w21_2})")

# ---------- (3) horizontal lifts; full bundle identity ----------
D1 = VF(e1.a, e1.b, -w1)
D2 = VF(e2.a, e2.b, -w2)
xi = VF(0, 0, 1)
lhs = D1.bracket(D2)
rhs = D2.scale(-T12) + (-xi)                        # -cot(theta) D_2 - xi
rep((lhs - rhs).iszero(), "FULL operator identity [D_1,D_2] = -cot(theta) D_2 - xi on the bundle")
rep(sp.simplify(lhs.c + 1/sp.sin(th)**2) == 0 and sp.simplify(lhs.c) != 0,
    "vertical part of [D_1,D_2] alone = -csc^2(theta) xi, nonzero: first-order operators do not close; the class 1/2 R S slot carries the zeroth-order term")

# ---------- (4) local rotation, U(1) shadow ----------
lam = sp.cos(th)**2*sp.sin(ph) + th*sp.sin(th)*sp.cos(ph)
for D, nm in ((D1, "D_1"), (D2, "D_2")):
    gen = VF(0, 0, lam)                             # lambda xi
    rep((gen.bracket(D) - VF(0, 0, -D.apply(lam))).iszero(),
        f"local rotation  [lambda xi, {nm}] = -({nm} lambda) xi")

print()
print("ALL PASS" if all(res) else "SOME FAIL")
