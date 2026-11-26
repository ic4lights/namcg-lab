"""s3: Lie-dragging and regularity of the Poisson frame Theta (B-R2 hypotheses).

Frame variable Theta^{mu A} = Theta^{mu nu} delta_nu^A  (chart index mu, matrix/internal index A).
Normal-plane rotation (Euclid) / boost (Lorentz) generator omega, xi^mu = omega^mu_nu x^nu.
  pure diffeomorphism Lie derivative on the chart index only:   (L Theta)^{mu A} = xi.d Theta^{mu A} - omega^mu_rho Theta^{rho A}
  joint (chart + internal) derivative:  (L~ Theta)^{mu A} = xi.d Theta^{mu A} - omega^mu_rho Theta^{rho A} - Theta^{mu B} omega^A_B
Checks
 1. constant Theta_bar = a e12 + b e34 : L~ = 0, L != 0  (so Lie-dragged only up to the internal rotation)
 2. generic constant Theta_bar: L~ = 0 iff [omega, Theta_bar]=0  (dimension of the invariant subspace)
 3. replica family Theta^{12}=1/f(r), Theta^{34}=1: L~ = 0 for arbitrary f(r) (Euclid) ; boost version in Lorentz signature
 4. regularity at Sigma for f=r^{n-1}: Theta^{12}=r^{1-n}, curvature/torsion invariants
 5. a non-linear chart change moves Theta out of the slice eta_{AB} e^B_mu antisymmetric
"""
import sympy as sp
from sympy import Rational as Q

x1, x2, x3, x4 = X = sp.symbols('x1:5', real=True)
a, b, n, eps = sp.symbols('a b n epsilon', real=True)

def Lie_pure(Th, om):
    xi = om*sp.Matrix(X)
    out = sp.zeros(4, 4)
    for m in range(4):
        for A in range(4):
            out[m, A] = sum(xi[k]*sp.diff(Th[m, A], X[k]) for k in range(4)) - sum(om[m, r]*Th[r, A] for r in range(4))
    return out.applyfunc(sp.simplify)

def Lie_joint(Th, om):
    xi = om*sp.Matrix(X)
    out = sp.zeros(4, 4)
    for m in range(4):
        for A in range(4):
            out[m, A] = (sum(xi[k]*sp.diff(Th[m, A], X[k]) for k in range(4)) - sum(om[m, r]*Th[r, A] for r in range(4))
                         - sum(Th[m, B]*om[A, B] for B in range(4)))
    return out.applyfunc(sp.simplify)

def e(i, j):
    M = sp.zeros(4, 4); M[i-1, j-1] = 1; M[j-1, i-1] = -1
    return M

J12 = e(1, 2)

print("1. constant aligned Theta_bar = a e12 + b e34, normal-plane rotation J12")
Th = a*e(1, 2) + b*e(3, 4)
print("   pure  L Theta =", Lie_pure(Th, J12).tolist())
print("   joint L~Theta =", Lie_joint(Th, J12).tolist())

print("2. generic constant antisymmetric Theta_bar: joint derivative = -[omega,Theta]-type; invariant subspace")
t = sp.symbols('t12 t13 t14 t23 t24 t34')
Tg = sp.zeros(4, 4)
idx = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
for s, (i, j) in zip(t, idx):
    Tg[i, j] = s; Tg[j, i] = -s
Lj = Lie_joint(Tg, J12)
eqs = [sp.expand(Lj[i, j]) for i in range(4) for j in range(4) if Lj[i, j] != 0]
sol = sp.solve(eqs, t, dict=True)
print("   condition L~=0 solved:", sol, " -> free parameters: t12, t34 (2 of 6)")
sd = a*(e(1, 2) + e(3, 4))
print("   self-dual a(e12+e34): joint derivative zero:", Lie_joint(sd, J12) == sp.zeros(4, 4),
      "; a(e13-e24) (also self-dual): joint derivative =", Lie_joint(a*(e(1, 3) - e(2, 4)), J12).tolist())

print("3. replica family Theta^{12}=1/f(r), Theta^{34}=1")
f = sp.Function('f')
r = sp.sqrt(x1**2 + x2**2)
Thf = sp.zeros(4, 4); Thf[0, 1] = 1/f(r); Thf[1, 0] = -1/f(r); Thf[2, 3] = 1; Thf[3, 2] = -1
print("   Euclid, joint derivative:", Lie_joint(Thf, J12).applyfunc(sp.simplify).is_zero_matrix)
print("   pure derivative (nonzero entries):", {(i, j): sp.simplify(v) for (i, j), v in
                                              {(i, j): Lie_pure(Thf, J12)[i, j] for i in range(4) for j in range(4)}.items() if v != 0})
# Lorentz: normal plane (x1=t, x2=x), boost generator K = [[0,1],[1,0]] on (t,x); invariant interval s = x^2 - t^2
Kb = sp.zeros(4, 4); Kb[0, 1] = 1; Kb[1, 0] = 1
sI = x2**2 - x1**2
Thl = sp.zeros(4, 4); Thl[0, 1] = 1/f(sI); Thl[1, 0] = -1/f(sI); Thl[2, 3] = 1; Thl[3, 2] = -1
xi = Kb*sp.Matrix(X)
res = sp.zeros(4, 4)
for m in range(4):
    for A in range(4):
        res[m, A] = (sum(xi[k]*sp.diff(Thl[m, A], X[k]) for k in range(4)) - sum(Kb[m, rr]*Thl[rr, A] for rr in range(4))
                     - sum(Thl[m, B]*Kb[A, B] for B in range(4)))
print("   Lorentz boost, joint derivative:", res.applyfunc(sp.simplify).is_zero_matrix)
Rr = sp.symbols('Rr')
Rot = sp.Matrix([[sp.cos(Rr), -sp.sin(Rr), 0, 0], [sp.sin(Rr), sp.cos(Rr), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
print("   finite rotation: R Theta R^T == Theta at rotated point:",
      sp.simplify((Rot*Thf*Rot.T - Thf.subs({x1: x1*sp.cos(Rr) - x2*sp.sin(Rr), x2: x1*sp.sin(Rr) + x2*sp.cos(Rr)}, simultaneous=True))
                  .applyfunc(lambda z: sp.simplify(z.subs(f(sp.sqrt((x1*sp.cos(Rr)-x2*sp.sin(Rr))**2+(x1*sp.sin(Rr)+x2*sp.cos(Rr))**2)), f(r))))).is_zero_matrix)

print("4. regularity at Sigma = {x1=x2=0} for f = r^(n-1), omega=Theta^{-1}, e^A_mu = omega_{mu A}")
fr = r**(n - 1)
om12 = -fr    # Theta^{12} = 1/f  -> omega_{12} = -f  (Theta^{-1} of [[0,1/f],[-1/f,0]] is [[0,-f],[f,0]])
W = sp.zeros(4, 4); W[0, 1] = -fr; W[1, 0] = fr; W[2, 3] = -1; W[3, 2] = 1
Thc = W.inv().applyfunc(sp.simplify)
print("   Theta check:", Thc.applyfunc(sp.simplify).tolist())
E = W.copy()   # E[mu,A] = omega_{mu A}
G = (E*E.T).applyfunc(sp.simplify)
Gi = G.inv().applyfunc(sp.simplify)
# torsion T^A_{mu nu} = d_mu e^A_nu - d_nu e^A_mu
T = [[[sp.diff(E[nu, A], X[mu]) - sp.diff(E[mu, A], X[nu]) for nu in range(4)] for mu in range(4)] for A in range(4)]
Tl = [[[sum(E[l, A]*T[A][m][nn] for A in range(4)) for nn in range(4)] for m in range(4)] for l in range(4)]
TT = sum(Gi[l, l2]*Gi[m, m2]*Gi[nn, n2]*Tl[l][m][nn]*Tl[l2][m2][n2] for l in range(4) for l2 in range(4) for m in range(4)
         for m2 in range(4) for nn in range(4) for n2 in range(4))
TT = sp.simplify(TT)
print("   TT = X =", TT, "  (on r>0)")
ueps = sp.simplify(TT.subs(n, 1 + eps))
print("   first order in epsilon = n-1:", sp.series(ueps, eps, 0, 3))
# proper distance u from Sigma: ds^2 = f^2 (dr^2 + r^2 dtheta^2) with f=r^(n-1): u = r^n/n
u = r**n/n
print("   X*u^2 =", sp.simplify(TT*u**2), "  -> X ~ (n-1)^2 / u^2 up to a factor, unbounded at u->0 for n != 1")
print("   Theta^{12}=r^{1-n}: first order in eps:", sp.series(r**(1-n).subs(n, 1+eps) if False else (sp.sqrt(x1**2+x2**2))**(-eps), eps, 0, 2))
print("   -> Theta^{12} = 1 - eps*ln r + O(eps^2): log-singular at r=0 already at first order; Pf Theta -> 0 (n<1), infinity (n>1)")

print("5. non-linear chart change leaves the slice {eta_{AB}e^B_mu antisymmetric}")
Wc = sp.Matrix(4, 4, lambda i, j: 0)
y = sp.symbols('y1:5')
# take constant antisymmetric omega0 and the chart change x = y + 0.1*y^2 pattern (random)
om0 = sp.Matrix([[0, 2, -1, 3], [-2, 0, 1, 1], [1, -1, 0, 2], [-3, -1, -2, 0]])
xmap = [y[0] + y[1]**2/5, y[1] + y[2]*y[0]/7, y[2] + y[3]**2/3, y[3] + y[0]*y[1]/2]
Jac = sp.Matrix(4, 4, lambda i, j: sp.diff(xmap[i], y[j]))     # dx^i/dy^j
eprime = (Jac.T*om0)   # e'^A_mu = (dx^nu/dy^mu) e^A_nu with e^A_nu = om0[nu, A]
pt = {y[0]: Q(1, 3), y[1]: Q(2, 5), y[2]: Q(-1, 2), y[3]: Q(3, 7)}
ep = eprime.subs(pt)
print("   e'_{mu A} + e'_{A mu} (should vanish on the slice) =", (ep + ep.T).applyfunc(sp.nsimplify).tolist())
