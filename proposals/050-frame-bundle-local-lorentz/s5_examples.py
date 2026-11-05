"""
s5: exact side checks.
(a) so(4,1) in the regular representation: T_a = E_{a4}, M_ab = E_ab act on functions of g in SO(4,1) by g -> g exp(tE).
    Y^A = g^A_4 is annihilated by M_ab; [T_a,Y^A] = g^A_a; eta^{ab} g^A_a g^B_b = eta^{AB} - Y^A Y^B; [T^a,[T_a,T_b]] = -3 T_b.
    U(2) is not conjugate into SO(3,1): the compact tori have ranks 2 and 1.
(b) spinor: gamma^a u_a^b = rho(u) gamma^b rho(u)^{-1}, X = (1/4) w_ab gamma^a gamma^b satisfies [X,gamma^c] = - gamma^d w^c_d.
(c) rank of the curvature map on bivectors: S_cd from commutators.
(d) five matrices: a null Kaluza-Klein wave, Ricci(5) = 0 iff Ricci(4)_ab = (1/2) F_ac F_b^c.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
from scipy.linalg import expm
from bundlelib import *

print('# (a) regular representation of so(4,1)')
G = np.diag([-1., 1, 1, 1, 1])
def E(A, B):
    m = np.zeros((5, 5))
    m[A, B] = G[B, B]; m[B, A] = -G[A, A]
    return m
com = lambda x, y: x @ y - y @ x
T = [E(a, 4) for a in range(4)]
res = 0
for b in range(4):
    v = sum(G[a, a]*com(T[a], com(T[a], T[b])) for a in range(4))
    res = max(res, np.max(np.abs(v + 3*T[b])))
print(' [T^a,[T_a,T_b]] = -3 T_b residual', res)
# closure rule of the vertical part with the frame
res = 0
for c in range(4):
    for d_ in range(c+1, 4):
        for a in range(4):
            v = com(E(c, d_), T[a])
            sgn = None
            for s in (1, -1):
                w = s*(G[a, d_]*T[c] - G[a, c]*T[d_])
                if np.max(np.abs(v-w)) < 1e-14:
                    sgn = s
            assert sgn is not None
print(' [M_cd,T_a] is a Lorentz rotation of the index a: yes')
rng = np.random.default_rng(50)
gen = sum(rng.normal()*E(i, j) for i in range(5) for j in range(i+1, 5))
g = expm(0.7*gen)
res1 = res2 = 0
Y = g[:, 4]
for c in range(4):
    for d_ in range(c+1, 4):
        res1 = max(res1, np.max(np.abs((g @ E(c, d_))[:, 4])))
Gi = G
Kam = sum(G[a, a]*np.outer(g[:, a], g[:, a]) for a in range(4))
res2 = np.max(np.abs(Kam - (Gi - np.outer(Y, Y))))
print(' (g M_cd)^A_4 = 0 residual', res1, '; eta^{ab} g^A_a g^B_b = eta^{AB} - Y^A Y^B residual', res2, '; Y.Y =', Y @ G @ Y)

print('# (b) spinor identity')
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]], complex); s3 = np.array([[1, 0], [0, -1]], complex); I2 = np.eye(2, dtype=complex)
gam = [1j*np.kron(s1, I2), np.kron(s2, I2), np.kron(s3, s1), np.kron(s3, s2)]
eta4 = np.diag([-1., 1, 1, 1])
assert all(np.max(np.abs(gam[a] @ gam[b] + gam[b] @ gam[a] - 2*eta4[a, b]*np.eye(4))) < 1e-14 for a in range(4) for b in range(4))
wl = rng.normal(size=(4, 4)); wl = wl - wl.T          # w_{ab}
gamlow = [eta4[a, a]*gam[a] for a in range(4)]
X = 0.25*sum(wl[a, b]*gam[a] @ gam[b] for a in range(4) for b in range(4))
wmix = eta4 @ wl     # w^c_d
res = 0
for c in range(4):
    lhs = X @ gam[c] - gam[c] @ X
    rhs = -sum(gam[d_]*wmix[c, d_] for d_ in range(4))
    res = max(res, np.max(np.abs(lhs-rhs)))
print(' [X,gamma^c] + gamma^d w^c_d residual', res)
# finite: rho(u) = exp(X) with v = exp(-w) gives gamma^a v_a^b = rho gamma^b rho^{-1} for v_a^b = (exp(-w^T...))
v = expm(-wmix)      # v[c,d] = (delta - w)^c_d: first index c is the upper (second) index of u_d^c
rho = expm(X)
res = 0
for c in range(4):
    lhs = sum(gam[d_]*v[c, d_] for d_ in range(4))
    rhs = rho @ gam[c] @ np.linalg.inv(rho)
    res = max(res, np.max(np.abs(lhs-rhs)))
print(' gamma^d v_d^c = rho gamma^c rho^{-1} residual', res)

print('# (c) curvature as a map on bivectors, exact')
B4 = Bundle(4)
y = B4.y; eta = B4.eta
def curvature_rank(e, pt):
    w, th = levi_civita_connection(e, y, eta)
    R, Ric = ricci_flat_index(e, w, th, y, eta)
    pairs = [(c, f) for c in range(4) for f in range(c+1, 4)]
    Mx = sp.zeros(6, 6)
    for i, (a, b) in enumerate(pairs):
        for j, (c, f) in enumerate(pairs):
            Mx[i, j] = sp.nsimplify(sp.simplify(R[a][b][c, f].subs(pt)))
    return Mx.rank(), Mx
t, r, X_, ph = y
f = 1 - 2/r
e = [[1/sp.sqrt(f), 0, 0, 0], [0, sp.sqrt(f), 0, 0], [0, 0, sp.sqrt(1-X_**2)/r, 0], [0, 0, 0, 1/(r*sp.sqrt(1-X_**2))]]
for rv, xv in [(sp.Rational(8, 3), sp.Rational(3, 5)), (sp.Rational(25, 8)*2, sp.Rational(5, 13))]:
    rk, Mx = curvature_rank(e, {t: 1, r: rv, X_: xv, ph: 1})
    print(f' Schwarzschild r={rv} (M=1), cos(theta)={xv}: rank {rk} of 6; nonzero entries {sorted(set(abs(v) for v in Mx if v!=0))}')
U, Vv, x, z = y
H = (x**2 - z**2)*(1 + U)
th_ = sp.Matrix([[(1-H)/2, (1+H)/2, 0, 0], [-sp.Rational(1, 2), sp.Rational(1, 2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
rk, Mx = curvature_rank(th_.inv().tolist(), {U: sp.Rational(1, 3), Vv: 2, x: sp.Rational(3, 2), z: sp.Rational(5, 7)})
print(f' Ricci-flat pp-wave: rank {rk} of 6')
s = y[0]
e = [[1/(3*s**2), 0, 0, 0], [0, s, 0, 0], [0, 0, s**-2, 0], [0, 0, 0, s**-2]]
rk, Mx = curvature_rank(e, {y[0]: sp.Rational(3, 2), y[1]: 1, y[2]: 2, y[3]: 3})
print(f' Kasner (-1/3,2/3,2/3): rank {rk} of 6')

print('# (d) null Kaluza-Klein wave with five matrices')
y5 = sp.symbols('y0:5', real=True)
eta5 = eta_matrix(5)
U, Vv, x, z, w5 = y5
c = sp.Function('c')(U); fU = sp.Function('f')(U)
c_, f_ = sp.Symbol('c0'), sp.Symbol('f0')
# take constants c0, f0: H = c0 x^2, A = f0 x dU; ds^2 = dU (dV + H dU) + dx^2 + dz^2 + (dw + A)^2
H5 = c_*x**2
A5 = f_*x
th5 = sp.Matrix([[(1-H5)/2, (1+H5)/2, 0, 0, 0], [-sp.Rational(1, 2), sp.Rational(1, 2), 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [A5, A5*0, 0, 0, 1]])
# rows: y-index of the one-form; columns: flat index, e^4 = dw + A dU, so th[0,4]=A, th[4,4]=1
th5 = sp.Matrix([[(1-H5)/2, (1+H5)/2, 0, 0, A5], [-sp.Rational(1, 2), sp.Rational(1, 2), 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
e5 = th5.inv().applyfunc(sp.simplify).tolist()
w, th = levi_civita_connection(e5, y5, eta5)
bad, anti = check_torsion_free(w, th, y5, eta5)
R, Ric5 = ricci_flat_index(e5, w, th, y5, eta5)
print(' torsion-free checks', bad, anti, '; Ric(5) flat components nonzero:', {(i, j): sp.simplify(Ric5[i, j]) for i in range(5) for j in range(i, 5) if sp.simplify(Ric5[i, j]) != 0})
# 4d metric alone
y4 = y5[:4]
th4 = th5[:4, :4]
e4 = th4.inv().applyfunc(sp.simplify).tolist()
w4, t4 = levi_civita_connection(e4, list(y4), eta_matrix(4))
R4, Ric4 = ricci_flat_index(e4, w4, t4, list(y4), eta_matrix(4))
print(' Ric(4) nonzero:', {(i, j): sp.simplify(Ric4[i, j]) for i in range(4) for j in range(i, 4) if sp.simplify(Ric4[i, j]) != 0})
print(' F = f0 e^2 ^ (e^0 + e^1), so (1/2) F_0c F_0^c = f0^2/2 = Ric(4)_00 exactly when c0 = -f0^2/2')
print(' Ric(5) at c0=-f0^2/2:', sp.simplify(Ric5.subs(c_, -f_**2/2)))

print('# (e) central Theta on the flat bundle: a_a = -(1/2) Theta_ab (u^{-1} y)^b')
B = Bundle(4)
Th = sp.Matrix([[0, 2, 0, 0], [-2, 0, 0, 0], [0, 0, 0, 3], [0, 0, -3, 0]])
eta = B.eta
Um = sp.Matrix(4, 4, lambda a, b: B.u[a][b])
Uinv = eta*Um.T*eta    # (u^{-1})_b^a, rows b columns a... u_a^b (u^-1)_b^c = delta_a^c
yv = sp.Matrix(B.y)
# y'^b = y^c (u^{-1})_c^b  (flat D_a = u_a^c d_c, so D_a y'^b = u_a^c (u^{-1})_c^b = delta_a^b)
yp = (yv.T*Uinv).T
a_ = [-sp.Rational(1, 2)*sum(Th[i, b]*yp[b] for b in range(4)) for i in range(4)]
e_flat = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
w_flat = [sp.zeros(4, 4) for _ in range(4)]
Dflat = B.horizontal(e_flat, w_flat)
L = rational_boost(4, 1, 1, 3)*rational_rotation(4, 1, 2, 1, 2)
pt = {B.y[i]: sp.Rational(i+1, 3) for i in range(4)}
pt.update({B.u[a][b]: L[a, b] for a in range(4) for b in range(4)})
vals = sp.Matrix(4, 4, lambda i, j: (B.apply(Dflat[i], a_[j]) - B.apply(Dflat[j], a_[i])).subs(pt))
print(' D_a a_b - D_b a_a - Theta_ab =', (vals-Th).applyfunc(sp.simplify) == sp.zeros(4, 4), '; note D_a acts through u_a^c d_c only, and u is held fixed by the flat D_a')
