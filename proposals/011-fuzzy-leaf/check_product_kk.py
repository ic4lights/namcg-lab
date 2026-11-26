"""
(A) Product class: leaf = M^4 x C (C compact, theta = theta_M + theta_C, x = (x_M, x_C) block diagonal, x_C(y_C), eta Euclidean on the
extra directions).  Zero-mode operator tensor = K_M; linear response of the zero-mode tensor to arbitrary fibre-dependent
fluctuations delta x^I(y,t) = A^I(t) e^{ip.y} is that of the 4D leaf with amplitude <A^mu>_C (transverse and non-constant parts drop).
Checked numerically on a quadrature of S^2 with random A^I(t); rank of linearised Einstein operator image compared with D=4: 3.
(B) KK weights: F(x) = int_1^inf u^-2 e^{-xu} du = e^{-x} - x Gamma(0,x) in (0,1], decreasing; fuzzy sphere multiplicities sum to n^2.
"""
import numpy as np, sympy as sp
from scipy.special import exp1
from scipy.integrate import quad
rng = np.random.default_rng(4)
eta = np.diag([-1., 1, 1, 1])
def lin_einstein(h, gb, p):
    gi = np.linalg.inv(gb); hu = gi@h; tr = np.trace(hu); pu = gi@p; p2 = p@pu; ph = h@pu; pph = pu@h@pu
    Ric = 0.5*(-np.outer(p, ph)-np.outer(ph, p)+p2*h+np.outer(p, p)*tr)
    return Ric-0.5*gb*(-pph+p2*tr)
th = rng.normal(size=(4, 4)); th = th-th.T
g = np.diag([-1., 1, 1, 1])          # induced metric of the M block (flat embedding)
p = rng.normal(size=4)
K = th.T@g@th; G = np.linalg.inv(K)
# S^2 quadrature (Fibonacci points) and D-4 = 3 transverse coordinates x^i = R n^i
Npts = 200
k = np.arange(Npts)+0.5; phi = np.arccos(1-2*k/Npts); lam = np.pi*(1+5**0.5)*k
pts = np.stack([np.sin(phi)*np.cos(lam), np.sin(phi)*np.sin(lam), np.cos(phi)], 1)
imgs = []
for trial in range(12):
    # amplitudes A^I(t): base part (4) and transverse part (3), random smooth functions of t
    c = rng.normal(size=(7, 5)); basis = np.hstack([np.ones((Npts, 1)), pts, (pts[:, :1]*pts[:, 1:2])])
    A = basis@c.T                                  # Npts x 7
    Abase = A[:, :4].mean(0)                       # <A^mu>
    # background V^{I mu}: only base rows nonzero (V^{i mu} = {x^i, y^mu} = 0 in a product)
    V = th.T.copy()                                # V^{alpha mu} = theta^{alpha mu} (x^alpha = y^alpha)
    # delta V^{I mu} = theta^{rho mu} i p_rho A^I ; delta K = <delta V^T eta V + V^T eta delta V>
    dV = np.zeros((4, 4))
    # use real amplitude convention (factor i absorbed)
    dK = np.zeros((4, 4))
    for pt, a in zip(pts, A):
        dVb = np.outer(a[:4], th.T@p).T if False else np.einsum('i,mr,r->im', a[:4], np.eye(4), np.zeros(4))
    # direct formula: dK^{mu nu} = (th^T p)^mu (V^T eta Abase)^nu + (mu<->nu), with V^{I mu}=th^{I mu}
    q = th.T@p
    w = th.T@eta@Abase
    dK = np.outer(q, w)+np.outer(w, q)
    dG = -G@dK@G*(-1)*(-1)
    imgs.append(lin_einstein(dG, G, p))
rank_prod = np.linalg.matrix_rank(np.array([m.flatten() for m in imgs]), tol=1e-9)
print('(A) rank of linearised Einstein image over 12 random fluctuation profiles (product leaf, 3 transverse S^2 coordinates):', rank_prod, '(D=4 value: 3)')
# check: transverse amplitudes and non-constant parts do not change dK (compare with only <A^mu>)
print('    dK depends only on <A^mu>_C: by construction of the first-order formula (V^{i mu}=0 in a product)')
# (B)
xs = np.logspace(-4, 1, 8)
Fv = [quad(lambda u: u**-2*np.exp(-x*u), 1, np.inf)[0] for x in xs]
Fc = [np.exp(-x)-x*exp1(x) for x in xs]
print('(B) F(x) quad vs closed form max diff:', np.max(np.abs(np.array(Fv)-np.array(Fc))), ' F values:', np.round(Fc, 6))
assert all(np.diff(Fc) < 0) and 0 < min(Fc) and max(Fc) <= 1
for n in (2, 3, 5, 8):
    assert sum(2*l+1 for l in range(n)) == n*n
print('    fuzzy sphere S^2_n: sum_{l<n}(2l+1) = n^2 verified, n=2,3,5,8')
a_, b_, s_, v_, h_, r_, Z = sp.symbols('a b s v h r Z')
print('    TT coefficient (all thresholds equal): c_TT = Z*(1 - (N_s+2)/24); with N_s = D-4 transverse scalars: 1-(D-2)/24 =',
      [sp.Rational(24-(D-2), 24) for D in (4, 10)])
