# jac101.py -- symbolic check of the coarea Jacobian: on Q(d)=P2-1/3=3a^2+b^2 with the ellipse
# parametrization u1(t)=(c*cos(t)/sqrt3 + c*sin(t))/sqrt2, u2(t)=(c*cos(t)/sqrt3 - c*sin(t))/sqrt2,
# (u3 eliminated by trace zero, d3 = 1/3 - u1 - u2): (i) Q is constant on the curve,
# (ii) speed/|grad Q| = 1/(2*sqrt(3)) identically, so dl/|grad Q| = dt/(2*sqrt(3)).
import sympy as sp
t, c = sp.symbols("t c", positive=True)
s3, r2 = sp.sqrt(3), sp.sqrt(2)
u1 = (c*sp.cos(t)/s3 + c*sp.sin(t))/r2
u2 = (c*sp.cos(t)/s3 - c*sp.sin(t))/r2
u3 = -u1 - u2
a = (u1 + u2)/r2
b = (u1 - u2)/r2
Q = sp.simplify(3*a**2 + b**2)          # should be c**2 (= P2 - 1/3)
Qd = sp.simplify(u1**2 + u2**2 + u3**2) # P2 - 1/3 computed from all three u_i
speed = sp.sqrt(sp.simplify(sp.diff(u1, t)**2 + sp.diff(u2, t)**2 + sp.diff(u3, t)**2))
U1, U2, U3 = sp.symbols("U1 U2 U3")
g = sp.Matrix([2*U1, 2*U2, 2*U3]).subs({U1: u1, U2: u2, U3: u3})
gnorm = sp.sqrt(sp.simplify(g.dot(g)))
ratio = sp.simplify(speed/gnorm)
print("Q(param) =", Q, " | P2-1/3 on curve =", sp.simplify(Qd), " (both must equal c**2)")
print("speed/|grad Q| =", ratio, " (must equal 1/(2*sqrt(3)))")
print("target 1/(2*sqrt(3)) =", sp.nsimplify(1/(2*s3)), " diff:", sp.simplify(ratio - 1/(2*s3)))
assert Q == c**2 and sp.simplify(Qd - c**2) == 0 and sp.simplify(ratio - 1/(2*s3)) == 0
print("JACOBIAN CHECK PASS")
