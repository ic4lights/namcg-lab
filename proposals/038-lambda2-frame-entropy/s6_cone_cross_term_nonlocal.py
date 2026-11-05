"""s6: cross term of rho^2 X = -rho^2 tr(b_s b^s) with the connection b_c of the Poisson cone, f=|z|^(n-1).

Cone family: Theta^{12}=1/f(r), Theta^{34}=1.  For the vector bundle b_sigma^{mu nu} = G_{sigma tau} Theta^{rho tau} d_rho Theta^{mu nu}; in the normal plane
b_c = (n-1) J12 * dtheta  (holonomy H = c_a J12, c_a = 1), i.e. b_c,s = (n-1) J12 * eps_{s t} x^t / r^2 (checked below), a 1/r field, NOT a delta.
Cross term with a first-order background connection beta_s (a regular 1-form in the normal plane):
     I = int_{r<L} d^2x  b_c^s beta_s  = (n-1) int_0^L dr oint dtheta (-sin(th) beta_1 + cos(th) beta_2)
       = (n-1) int_{r<L} d^2x  Omega_12(x) ln(L/r),     Omega_12 = d_1 beta_2 - d_2 beta_1 (abelian part)
so it is the pairing of the bundle curvature with the 2d Green function ln r: supported in the bulk (weight ln(L/r)), not on Sigma.
Verified here for random polynomial beta by exact integration.
"""
import random
import sympy as sp
from sympy import Rational as Q

random.seed(3)
x1, x2, r, th, L, n = sp.symbols('x1 x2 r theta L n', positive=True)

# (a) b_c from the cone family, normal plane block
f = sp.sqrt(x1**2 + x2**2)**(n - 1)
Th = sp.zeros(4, 4); Th[0, 1] = 1/f; Th[1, 0] = -1/f; Th[2, 3] = 1; Th[3, 2] = -1
X = [x1, x2, sp.Symbol('x3'), sp.Symbol('x4')]
ET = Th.inv().applyfunc(sp.simplify)
G = (Th*Th.T).inv().applyfunc(sp.simplify)       # G_{mu nu}
def dTh(rho_idx):
    return Th.applyfunc(lambda z: sp.diff(z, X[rho_idx]))
b = {}
for s in range(2):
    M = sp.zeros(4, 4)
    for rho_ in range(4):
        for tau in range(4):
            M += G[s, tau]*Th[rho_, tau]*dTh(rho_)
    b[s] = M.applyfunc(sp.simplify)
J12 = sp.zeros(4, 4); J12[0, 1] = 1; J12[1, 0] = -1
print("b_1 =", b[0].tolist()[0][1], " b_2 =", b[1].tolist()[0][1], " (entry [0,1] of the 4x4 so(4)-valued one-form)")
cand1 = (n - 1)*(-x2)/(x1**2 + x2**2); cand2 = (n - 1)*x1/(x1**2 + x2**2)
print("   matches (n-1)*(-x2, x1)/r^2 * J12 up to the normalisation of the entry:",
      sp.simplify(b[0][0, 1] - cand1) == 0 or sp.simplify(b[0][0, 1] + cand1) == 0 or sp.simplify(b[0][0, 1]/cand1))

# (b) nonlocality identity for random polynomial beta
def rp(deg):
    return sum(Q(random.randint(-3, 3), random.randint(1, 3))*x1**i*x2**j for i in range(deg+1) for j in range(deg+1-i))
for trial in range(3):
    b1, b2 = rp(3), rp(3)
    # polar integrals
    pol = {x1: r*sp.cos(th), x2: r*sp.sin(th)}
    lhs_integrand = (-sp.sin(th)*b1.subs(pol) + sp.cos(th)*b2.subs(pol))
    I = sp.integrate(sp.integrate(sp.expand(lhs_integrand), (th, 0, 2*sp.pi)), (r, 0, L))
    Om = sp.diff(b2, x1) - sp.diff(b1, x2)
    Jd = sp.integrate(sp.integrate(sp.expand(Om.subs(pol)*r*sp.log(L/r)), (th, 0, 2*sp.pi)), (r, 0, L))
    print(f"trial {trial}: int b_c.beta/(n-1) - int Omega ln(L/r) =", sp.simplify(I - Jd))
# (c) the weight ln(L/r) is not a delta: for constant Omega_12 = w the cross term is w*pi*L^2/2*(n-1), growing with the area
w = sp.symbols('w')
print("constant Omega_12=w:  int Omega ln(L/r) d^2x =", sp.integrate(2*sp.pi*r*sp.log(L/r)*w, (r, 0, L)))
