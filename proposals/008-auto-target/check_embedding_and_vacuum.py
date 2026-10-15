"""
(A) Embedding realisation (D >= 4 hermitian matrices X^I, leaf coordinates y^mu, Phi^I_mu := d_mu x^I):
    K^{mu nu} := eta_{IJ} {x^I, y^mu}{x^J, y^nu},  {x^I, y^mu} = Phi^I_a theta^{a mu}   =>   K = theta^T g theta,  g = Phi^T eta_D Phi.
    Checked numerically for random Phi (D x 4), theta (4 x 4 antisymmetric). Then K = c g^{-1} would need N^2 = -c, N = theta g (mixed),
    which has no real solution for Lorentzian g (see check_theta_image.py (4)).
(B) Compatibility of the Theta-coframe e = eta^{-1} omega_hat (omega_hat = (Theta/l^2)^{-1}) with the vacuum manifold Phi^T Phi = v^2 1 of the
    displayed potential (real locked block):  e^T e = 1  <=>  omega_hat^2 = -1 (omega_hat a complex structure).
    For omega_hat = J0 = diag(eps, eps): G = e^T eta e = diag(1,-1,1,1) (Lorentzian, emergent time is the x^1 direction);
    for J = R J0 R^T generally G = 1 - 2 n n^T with n = -J e_0 a spatial unit vector.
    Tangent count: directions dTheta (6) with delta e tangent to the vacuum manifold e*so(4): dimension 2.
"""
import numpy as np, sympy as sp
rng = np.random.default_rng(3)
# (A)
for D, sig in ((4, -1), (6, -1), (10, -1)):
    etaD = np.diag([sig] + [1.0]*(D-1))
    Phi = rng.normal(size=(D, 4))
    th = rng.normal(size=(4, 4)); th = th - th.T
    X = Phi.T@etaD@Phi
    g = X
    K1 = np.zeros((4, 4))
    brk = np.einsum('Ia,am->Im', Phi, th)               # {x^I, y^mu}
    for I in range(D):
        for J in range(D):
            K1 += etaD[I, J]*np.outer(brk[I], brk[J])
    K2 = th.T@g@th
    ev = np.linalg.eigvalsh(g)
    print("(A) D=%2d: K = theta^T g theta : %s ; signature of g = (%d neg, %d pos)" % (D, np.allclose(K1, K2), (ev < 0).sum(), (ev > 0).sum()))
# (B)
eta = sp.diag(-1, 1, 1, 1)
eps2 = sp.Matrix([[0, 1], [-1, 0]])
J0 = sp.diag(eps2, eps2)
e = eta.inv()*J0
print("(B) e^T e =", (e.T*e).tolist(), "; G = e^T eta e =", (e.T*eta*e).tolist())
# general complex structure of the same duality class: J = R J0 R^T, R in SO(4) acting as SO(3) on the three self-dual forms
def rot_gen(i, j, a):
    R = sp.eye(4); R[i, i] = sp.cos(a); R[j, j] = sp.cos(a); R[i, j] = -sp.sin(a); R[j, i] = sp.sin(a); return R
a, b, c = sp.symbols('a b c', real=True)
R = rot_gen(0, 1, a)*rot_gen(1, 2, b)*rot_gen(0, 3, c)
J = sp.simplify(R*J0*R.T)
print("    J antisymmetric orthogonal complex structure for J = R J0 R^T (R generic SO(4)):", sp.simplify(J + J.T) == sp.zeros(4, 4), sp.simplify(J*J + sp.eye(4)) == sp.zeros(4, 4))
eJ = eta.inv()*J
GJ = sp.simplify(eJ.T*eta*eJ)
n = sp.simplify(-J[:, 0])                      # -J e_0
print("    G(J) == 1 - 2 n n^T with n = -J e_0 :", sp.simplify(GJ - (sp.eye(4) - 2*n*n.T)) == sp.zeros(4, 4), "; n.e_0 =", sp.simplify(n[0]), "; |n|^2 =", sp.simplify((n.T*n)[0]))
# tangent count at e = eta^{-1} J0
w = sp.symbols('w0:6')
dTh = sp.Matrix([[0, w[0], w[1], w[2]], [-w[0], 0, w[3], w[4]], [-w[1], -w[3], 0, w[5]], [-w[2], -w[4], -w[5], 0]])
Th0 = J0.inv()                                  # Theta_hat = omega_hat^{-1}
dom = -J0*dTh*J0                                # d(omega_hat) = -omega Theta' omega
de = eta.inv()*dom
Hh = sp.expand((e.T*de + de.T*e)/2)             # Hermitian part: the part that costs potential energy
rowsH = [Hh[i, j] for i in range(4) for j in range(i, 4)]
Mh = sp.Matrix([[sp.diff(r, s) for s in w] for r in rowsH])
print("    delta e tangent to the vacuum manifold {Phi^T Phi = v^2}: dimension of the kernel of dTheta -> Sym(e^T de) =", 6 - Mh.rank(), "; massive (V^(2) = lam v^2 Tr H^2) directions:", Mh.rank())
