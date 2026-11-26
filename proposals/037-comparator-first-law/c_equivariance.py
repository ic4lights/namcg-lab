"""037-c: equivariance of the composite constraint omega = F[Theta] (Presentation A):  b_sigma^{mu nu} = G_{sigma tau} Theta^{rho tau} d_rho Theta^{mu nu},
G = K^{-1}, K^{mu nu} = sum_a Theta^{a mu} Theta^{a nu}  (eta = delta).
Which transformations of the chart x and of the matrix indices leave the law  b'_sigma^{mu nu}(x') = (J^{-1})^{s'}_sigma J^mu_{m'} J^nu_{n'} b_{s'}^{m'n'}(x)  intact?
Tested at a point x0, exact rational arithmetic, random quadratic Theta.  (J = Jacobian of the chart map, acting on ALL indices, as for a tensor.)
Cases: (A) diagonal rotation (chart and matrix indices rotated together, R in SO(4));  (B) chart-only rotation;  (C) matrix-index-only rotation;
(D) diagonal GL(4) map (non-orthogonal);  (E) a non-linear diffeomorphism of the chart (Theta transformed as a bivector)."""
import random, sympy as sp
from sympy import Rational as Q
random.seed(7)
X = sp.symbols('x1:5')
def rnd(): return Q(random.randint(-3, 3), random.randint(1, 3))
def rand_theta():
    Th0 = sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]]) + sp.Matrix(4, 4, lambda i, j: 0)
    Th = sp.zeros(4, 4)
    mons = [1] + list(X) + [X[i]*X[j] for i in range(4) for j in range(i, 4)]
    for i in range(4):
        for j in range(i+1, 4):
            e = sum((rnd()*m for m in mons), 0)
            Th[i, j] = e; Th[j, i] = -e
    return Th0 + Th/3
def b_of(Th, pt):
    sub = dict(zip(X, pt))
    T0 = Th.subs(sub); K = T0.T*T0; G = K.inv()
    dT = [Th.diff(X[r]).subs(sub) for r in range(4)]
    out = []
    for s in range(4):
        M = sp.zeros(4, 4)
        for t in range(4):
            for r in range(4):
                M += G[s, t]*T0[r, t]*dT[r]
        out.append(M)
    return out
def tensor_pred(b, J, Jm_=None):
    """b'_s = (J^-1)^{s'}_s  Jm b_{s'} Jm^T ; Jm defaults to J (tensor law); pass Jm_=I or J_=I to rotate only the matrix or only the form index."""
    Ji = J.inv(); Jm_ = J if Jm_ is None else Jm_
    return [sum((Ji[sp_, s]*Jm_*b[sp_]*Jm_.T for sp_ in range(4)), sp.zeros(4, 4)) for s in range(4)]
def rot12(c, s_):
    R = sp.eye(4); R[0, 0] = c; R[0, 1] = -s_; R[1, 0] = s_; R[1, 1] = c; return R
Th = rand_theta(); x0 = [Q(1, 2), Q(-1, 3), Q(1, 5), Q(2, 7)]
R = rot12(Q(3, 5), Q(4, 5)); Rinv = R.inv()
def check(name, ThNew, J, x0new, pt_old, Jm_=None):
    """ThNew(x') field; J Jacobian dx'/dx at pt_old; compare b'(x0new) with tensor_pred(b(pt_old))."""
    bn = b_of(ThNew, x0new); bp = tensor_pred(b_of(Th, pt_old), J, Jm_)
    d = max(abs(sp.nsimplify((bn[s] - bp[s]).norm())) for s in range(4))
    print('  %-48s mismatch ||b_new - tensor law(b)|| = %s' % (name, sp.nsimplify(d)))
    return d
print('(A) diagonal rotation R in the (1,2)-plane (Pythagorean 3/5,4/5):')
ThA = R*Th.subs(dict(zip(X, list(Rinv*sp.Matrix(X)))), simultaneous=True)*R.T
check('Theta\'(x\') = R Theta(R^-1 x\') R^T', ThA, R, list(R*sp.Matrix(x0)), x0)
print('(B) chart-only rotation (matrix indices untouched):')
ThB = Th.subs(dict(zip(X, list(Rinv*sp.Matrix(X)))), simultaneous=True)
check("Theta'(x') = Theta(R^-1 x'); form index rotates, matrix indices fixed", ThB, R, list(R*sp.Matrix(x0)), x0, Jm_=sp.eye(4))
print('(C) matrix-index-only rotation (chart untouched):')
ThC = R*Th*R.T
check("Theta'(x) = R Theta(x) R^T; matrix indices rotate, form index fixed", ThC, sp.eye(4), x0, x0, Jm_=R)
print('(D) diagonal GL(4) map A = diag(2,1,1,1) acting on chart and indices:')
A = sp.diag(2, 1, 1, 1); Ai = A.inv()
ThD = A*Th.subs(dict(zip(X, list(Ai*sp.Matrix(X)))), simultaneous=True)*A.T
check('Theta\'(x\') = A Theta(A^-1 x\') A^T', ThD, A, list(A*sp.Matrix(x0)), x0)
print('(E) non-linear diffeomorphism x\' = x + (1/5) x1^2 e2, Theta transformed as a bivector:')
# x' = phi(x); Theta'(x') = J Theta(x) J^T.  Build Theta' as a function of x via x (inverse not needed: pull back everything to x-chart parametrisation)
phi = sp.Matrix(X) + sp.Matrix([0, Q(1, 5)*X[0]**2, 0, 0]); Jm = phi.jacobian(X)
# derivatives with respect to x' via chain rule: d/dx'_r = (J^-1)^k_r d/dx_k
ThE = Jm*Th*Jm.T
sub = dict(zip(X, x0)); T0 = ThE.subs(sub); K = T0.T*T0; G = K.inv()
Ji = Jm.inv().subs(sub)
dT = [sum((Ji[k, r]*ThE.diff(X[k]).subs(sub) for k in range(4)), sp.zeros(4, 4)) for r in range(4)]
bE = []
for s in range(4):
    M = sp.zeros(4, 4)
    for t in range(4):
        for r in range(4):
            M += G[s, t]*T0[r, t]*dT[r]
    bE.append(M)
bp = tensor_pred(b_of(Th, x0), Jm.subs(sub))
d = max(abs(sp.nsimplify((bE[s] - bp[s]).norm())) for s in range(4))
print('  %-48s mismatch ||b_new - tensor law(b)|| = %s' % ('b of transformed Theta vs tensor law', sp.nsimplify(d)))
