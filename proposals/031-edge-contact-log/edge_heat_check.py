"""Edge-mode operator Delta_{F,w} = -w^{-1} div(w grad) on a closed surface: a_1 = (1/4pi) int (R/6 - |grad ln w|^2/4) (+ exact derivative).
(1) symbolic unitary equivalence  w^{1/2} Delta_{F,w} w^{-1/2} = -Lap + W,  W = (1/2) Lap ln w + (1/4)|grad ln w|^2  (conformally flat 2D metric).
(2) numerical heat-trace constant on the flat torus with w = exp(kappa cos x1): predicted a_1 = -pi kappa^2/8."""
import numpy as np, sympy as sp
x, y = sp.symbols('x y', real=True)
f = sp.Function('f')(x, y); v = sp.Function('v')(x, y); s = sp.Function('s')(x, y)     # w = e^f, metric e^{2s} delta
w = sp.exp(f)
sg = sp.exp(2*s)
# Delta_{F,w} u = -(1/w) (1/sqrt g) d_i( w sqrt g g^{ij} d_j u ),  2D: sqrt g g^{ij} = delta_ij
Lw = lambda u: -(1/w)*(1/sg)*(sp.diff(w*sp.diff(u, x), x) + sp.diff(w*sp.diff(u, y), y))
psi = sp.exp(-f/2)*v
lhs = sp.simplify(sp.exp(f/2)*Lw(psi))
Lap0 = lambda u: sp.diff(u, x, 2) + sp.diff(u, y, 2)
W0 = sp.Rational(1, 2)*Lap0(f) + sp.Rational(1, 4)*(sp.diff(f, x)**2 + sp.diff(f, y)**2)
rhs = (1/sg)*(-Lap0(v) + W0*v)                  # = -Lap_g v + W v with W in flat-coordinate normalisation divided by e^{2s}
print('symbolic equivalence residual:', sp.simplify(lhs - rhs))
# (2) torus numerics
kappa = 1.3
M = 90
n = np.arange(-M, M + 1)
Nn = len(n)
# W(x) = (1/2) f'' + (1/4) f'^2 with f = kappa cos x : f' = -kappa sin x, f'' = -kappa cos x
# Fourier matrix elements of W on e^{inx}: cos x -> (delta_{m,n+1}+delta_{m,n-1})/2 ; sin^2 x = (1 - cos 2x)/2
H = np.diag(n.astype(float)**2)
for i in range(Nn):
    if i + 1 < Nn:
        H[i, i + 1] += -0.5*kappa*0.5; H[i + 1, i] += -0.5*kappa*0.5
    H[i, i] += 0.25*kappa**2*0.5
    if i + 2 < Nn:
        H[i, i + 2] += 0.25*kappa**2*(-0.25); H[i + 2, i] += 0.25*kappa**2*(-0.25)
E = np.linalg.eigvalsh(H)
kk = np.arange(-60, 61)
for t in (0.004, 0.006, 0.01, 0.015):
    tr1 = np.exp(-t*E).sum(); th = np.exp(-t*kk.astype(float)**2).sum()
    T2 = tr1*th
    a1 = T2 - np.pi/t                    # A/(4 pi t) = (2pi)^2/(4 pi t) = pi/t
    print('t', t, ' Tr - pi/t =', a1, '  predicted a_1 =', -np.pi*kappa**2/8)
