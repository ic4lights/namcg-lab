"""The family omega = d(h(r) Lambda^3), Lambda^3 = (x1 dx2 - x2 dx1) + (x3 dx4 - x4 dx3), is invariant under the two commuting rotations
R_12(a) (plane x1x2) and R_34(a) (plane x3x4):  Theta(R x) = R Theta(x) R^T.  Each fixes a 2-plane (x3=x4=0, resp. x1=x2=0) pointwise, and
G, rho are invariant, so the fixed plane is a totally geodesic entangling surface for the pulled-back replica.  Numerical check (mpmath, 50 digits)
for the closed-form non-BPS solution h = 1 + sqrt(1 - C/r^4)."""
import mpmath as mp
import lib
from chk_J_cartesian import theta_num
mp.mp.dps = 50
Cv = mp.mpf('-0.8')
hf = lambda r: 1 + mp.sqrt(1 - Cv/r**4)
hp = lambda r: (2*Cv/r**5)/mp.sqrt(1 - Cv/r**4)
x = [mp.mpf('0.7'), mp.mpf('-1.1'), mp.mpf('0.4'), mp.mpf('0.9')]
def rot(plane, a):
    R = mp.eye(4)
    i, j = plane
    R[i, i] = mp.cos(a); R[i, j] = -mp.sin(a); R[j, i] = mp.sin(a); R[j, j] = mp.cos(a)
    return R
for plane in ((0, 1), (2, 3)):
    R = rot(plane, mp.mpf('0.77'))
    xr = list(R*mp.matrix(x))
    lhs = theta_num(xr, hf, hp)
    rhs = R*theta_num(x, hf, hp)*R.T
    print('rotation in plane', tuple(p+1 for p in plane), ': max |Theta(Rx) - R Theta(x) R^T| =', mp.nstr(max(abs(lhs[i, j]-rhs[i, j]) for i in range(4) for j in range(4)), 5))
