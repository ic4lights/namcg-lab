# jac101b.py -- coarea Jacobian for the pushforward of rho_hat by P2 at D=3 (supersedes jac101.py,
# which wrongly took a 3-component gradient; the fibre density lives on the trace plane with
# orthonormal eigen-coordinates (a,b), so dl and |grad Q| must be taken in (a,b)).
# Claims checked: (i) Q(a,b)=3a^2+b^2 equals P2-1/3 = sum_i u_i^2 on the trace plane;
# (ii) on the level curve a(t)=c cos t/sqrt3, b(t)=c sin t: speed/|grad Q| = 1/(2 sqrt3)
# identically, hence dl/|grad Q| = dt/(2 sqrt3) exactly (the factor in the insert's coarea formula).
import sympy as sp
t, c = sp.symbols("t c", positive=True)
s3, r2 = sp.sqrt(3), sp.sqrt(2)
a = c*sp.cos(t)/s3
b = c*sp.sin(t)
# trace-zero plane: u1 = (a + b)/sqrt2 ... invert: a=(u1+u2)/sqrt2, b=(u1-u2)/sqrt2, u3=-u1-u2
u1 = (a + b)/r2
u2 = (a - b)/r2
u3 = -u1 - u2
Qp = sp.simplify(u1**2 + u2**2 + u3**2)   # P2 - 1/3 in u-coords
print("3a^2+b^2 - (P2-1/3 on plane) =", sp.simplify(3*a**2 + b**2 - Qp), " (must be 0)")
speed = sp.sqrt(sp.simplify(sp.diff(a, t)**2 + sp.diff(b, t)**2))
gnorm = sp.sqrt(sp.simplify((6*a)**2 + (2*b)**2))
ratio = sp.simplify(speed/gnorm)
print("speed/|grad Q| =", ratio, " diff from 1/(2*sqrt(3)):", sp.simplify(ratio - 1/(2*s3)))
assert sp.simplify(3*a**2 + b**2 - Qp) == 0 and sp.simplify(ratio - 1/(2*s3)) == 0
print("JACOBIAN CHECK PASS")
