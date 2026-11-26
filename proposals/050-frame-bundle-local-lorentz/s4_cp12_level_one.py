"""
s4: matrix gauge transformations on the frame T^a of the conjugate-coordinate class (leaf CP^{1,2}, Poisson limit).

(a) on an explicit realisation: M^{mu nu} = [ y^4 (y^mu T^nu - y^nu T^mu) + sig ell eps^{mu nu rho lam} y_rho T_lam ] / (y.y), find sig;
    T.T as a function of y; relation of the fibre to n.
(b) Lambda = xi_mu(y) T^mu: {Lambda,T^nu} = s xi_mu M^{mu nu} - s m T^mu d^nu xi_mu (exact, Lie-Poisson; checked against brackets of the realisation).
(c) the algebraic part with xi.y = 0 is the bivector lam^{nu}_sigma of W_y, boost part tied to the displacement of y;
    W_y is not a subalgebra of so(3,1) for y^4 != 0: exact rational span at base points.
(d) selection rule: Lambda = f(y) (zeta(y).T)^J, zeta null on y-perp, gives {Lambda,T^a} of pure level J on the fibre (numerical projection).
(e) ratio of the rotation to the derivative term at the frozen point.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
from scipy.linalg import expm
import cp12_realisation as cp

np.set_printoptions(precision=6, suppress=True, linewidth=140)
eta = np.diag([-1., 1, 1, 1])

def levi():
    from itertools import permutations
    e = np.zeros((4, 4, 4, 4))
    for p in permutations(range(4)):
        sign = 1
        pl = list(p)
        for i in range(4):
            for j in range(i+1, 4):
                if pl[i] > pl[j]:
                    sign = -sign
        e[p] = sign
    return e
EPS = levi()

rng = np.random.default_rng(50)
print('# (a) relation of M^{mu nu} to T and y at random points of the orbit (eps^{0123}=+1)')
sigs, maxres, Tsq = [], 0, []
s_val = None
for trial in range(40):
    z = cp.rand_z_pos(rng, n=2.0)
    M = cp.Mfun(z)
    y = M[:4, 5]; T = M[:4, 4]; m = M[4, 5]
    ylow = eta @ y; Tlow = eta @ T
    Y = y @ ylow
    ell2 = -(Y + m*m)
    if m < 0.05 or ell2 < 1e-6:
        continue
    ell = np.sqrt(ell2)
    M2 = M[:4, :4]
    for sig in (1, -1):
        pred = (m*(np.outer(y, T) - np.outer(T, y)) + sig*ell*np.einsum('abcd,c,d->ab', EPS, ylow, Tlow))/Y
        r = np.max(np.abs(pred-M2))
        if r < 1e-9:
            sigs.append(sig)
            maxres = max(maxres, r)
    Tsq.append((Y, m, T @ Tlow, ell))
print(' sign sigma found:', set(sigs), 'samples', len(sigs), 'max residual', maxres)
if Tsq:
    arr = np.array(Tsq)
    # test T.T = ell^2 (y0^2)/ell^2... at rest T^i = (y0/ell) n^i, |n| to be found: T.T * ell^2/(-Y) = |n|^2
    n2 = arr[:, 2]*arr[:, 3]**2/(-arr[:, 0])
    print(' |n|^2 := T.T ell^2/(-y.y) over samples: min, max', n2.min(), n2.max(), '; ell^2', (arr[:, 3]**2).min(), (arr[:, 3]**2).max())

print('# (b) bracket identities on the realisation')
z = cp.rand_z_pos(rng, n=2.0)
M = cp.Mfun(z)
# sign s from {T^a,y^mu} = s eta^{a mu} m
br = np.array([[cp.PB(a, 4, mu, 5, z) for mu in range(4)] for a in range(4)])
s = np.sign(br[1, 1]/M[4, 5])
print(' {T^a,y^mu} - s eta m max residual', np.max(np.abs(br - s*eta*M[4, 5])), ' s =', s)
tt = np.array([[cp.PB(a, 4, b, 4, z) for b in range(4)] for a in range(4)])
print(' {T^a,T^b} - s M^{ab} max residual', np.max(np.abs(tt - s*M[:4, :4])))
yy = np.array([[cp.PB(a, 5, b, 5, z) for b in range(4)] for a in range(4)])
print(' {y^a,y^b} + s M^{ab} max residual', np.max(np.abs(yy + s*M[:4, :4])))

print('# (c) exact: the bivectors lam(xi) at rational base points')
def lam_matrix(y0, y4, xi):
    ell = sp.sqrt(y0**2-y4**2)
    y = sp.Matrix([y0, 0, 0, 0]); ylow = sp.Matrix([-y0, 0, 0, 0]); Y = -y0**2
    xiu = sp.Matrix(xi)
    xil = sp.Matrix([-xiu[0], xiu[1], xiu[2], xiu[3]])
    L = sp.zeros(4, 4)  # lam^{nu sigma} with upper indices; acting on T_sigma
    from sympy import LeviCivita
    for nu in range(4):
        for sg in range(4):
            val = y4*(xiu[nu]*y[sg] - y[nu]*xiu[sg])
            for mu in range(4):
                for rho in range(4):
                    val += ell*LeviCivita(mu, nu, rho, sg)*xil[mu]*ylow[rho]
            L[nu, sg] = val/Y
    return L
H = sp.diag(-1, 1, 1, 1)
for (y0, y4) in [(5, 3), (13, 5), (5, 4), (25, 7)]:
    y0, y4 = sp.Integer(y0), sp.Integer(y4)
    W = [lam_matrix(y0, y4, xi) for xi in ([0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])]
    # as mixed matrices lam^nu_sigma: A = L H
    As = [w*H for w in W]
    vec = lambda m: list(m)
    rW = sp.Matrix([vec(a) for a in As]).rank()
    comm = [As[i]*As[j]-As[j]*As[i] for i in range(3) for j in range(i+1, 3)]
    rJ = sp.Matrix([vec(a) for a in As+comm]).rank()
    anti = all(sp.simplify(w+w.T) == sp.zeros(4, 4) for w in W)
    boost = W[0][0, 1]; rot = W[0][2, 3]
    print(f' (y0,y4)=({y0},{y4}) ell={sp.sqrt(y0**2-y4**2)}: dim W={rW}, antisym {anti}, dim(W+[W,W])={rJ}, xi=e_1: boost entry lam^(01)={boost}, rotation entry lam^(23)={rot}, ratio rotation/boost={sp.nsimplify(rot/boost)}')
y4_0 = sp.Integer(0); y0_0 = sp.Integer(5)
W = [lam_matrix(y0_0, y4_0, xi)*H for xi in ([0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])]
comm = [W[i]*W[j]-W[j]*W[i] for i in range(3) for j in range(i+1, 3)]
print(' at y4=0 (frame degenerate there): dim(W+[W,W]) =', sp.Matrix([list(a) for a in W+comm]).rank())

print('# (d) selection rule on the fibre')
# work at a base point at rest, by the Lie-Poisson formula with exact expressions for T and M as functions of (y, n)
def TM(y0, y4, ell, n, sig):
    # at rest y=(y0,0,0,0), y^4=y4: T^i=(y0/ell) n^i, M^{i0}=(y4/ell) n^i, M^{ij}: from the fitted form
    T = np.array([0, *(y0/ell*n)])
    y = np.array([y0, 0, 0, 0.]); ylow = eta @ y; Tlow = eta @ T; Y = y @ ylow
    M = (y4*(np.outer(y, T)-np.outer(T, y)) + sig*ell*np.einsum('abcd,c,d->ab', EPS, ylow, Tlow))/Y
    return T, M

# boost taking (y_ref) to y: used to give zeta(y) a nontrivial dependence on y
def zeta_field(yv, ell):
    y4 = np.sqrt(-(yv @ eta @ yv) - ell*ell)
    u = yv/np.sqrt(-(yv @ eta @ yv))
    # generic local rotation angle of the fixed null vector, then boost to the frame of u
    th = 0.4*yv[1] - 0.3*yv[2] + 0.2*yv[0]
    ph = 0.3*yv[3] + 0.1*yv[1]
    a = np.array([np.cos(ph)*np.cos(th), np.cos(ph)*np.sin(th), -np.sin(ph)])
    b = np.array([-np.sin(th), np.cos(th), 0.])
    z3 = a + 1j*b     # null in R^3
    gam = u[0]; vec = u[1:]
    # boost: zeta^0 = vec.z3, zeta^i = z3^i + vec^i (vec.z3)/(1+gam)
    d0 = vec @ z3
    return np.array([d0, *(z3 + vec*d0/(1+gam))])

def f_field(yv):
    return 1 + 0.3*yv[1] + 0.2*yv[0]*yv[2]

ell = 4.0; y0 = 5.0; y4 = np.sqrt(y0**2-ell**2)
sig = list(set(sigs))[0]
def dlambda(a, J, n, h=1e-5):
    """{Lambda,T^a} at y=(y0,0,0,0), fibre point n, Lambda = f(y)(zeta(y).T)^J."""
    T, M = TM(y0, y4, ell, n, sig)
    Tl = eta @ T
    yb = np.array([y0, 0, 0, 0.])
    z0 = zeta_field(yb, ell)
    zl = eta @ z0
    zt = zl @ T
    # {g(y),T^a} = -s m eta^{a rho} d_rho g
    dg = lambda fun, rho: (fun(yb + h*np.eye(4)[rho]) - fun(yb - h*np.eye(4)[rho]))/(2*h)
    e_a = eta[a, a]
    df = -s*y4*e_a*dg(f_field, a)
    # zeta_mu(y) T^mu with T fixed: derivative of zeta_mu
    dz = -s*y4*e_a*dg(lambda Y: (eta @ zeta_field(Y, ell)) @ T, a)
    # {zeta_mu T^mu,T^a} at fixed zeta = s zeta_mu M^{mu a}
    fibre = s*(zl @ M[:, a])
    f0 = f_field(yb)
    return df*zt**J + f0*J*zt**(J-1)*(dz + fibre)

from scipy.special import sph_harm_y
theta_nodes, wts = np.polynomial.legendre.leggauss(24)
phis = np.linspace(0, 2*np.pi, 48, endpoint=False)
nmax = 6
for J in (1, 2, 3, 4):
    lev = np.zeros((4, nmax+1))
    for a in range(4):
        vals = {}
        for i, x in enumerate(theta_nodes):
            for j, ph in enumerate(phis):
                st = np.sqrt(1-x*x)
                n = ell*np.array([st*np.cos(ph), st*np.sin(ph), x])
                # |n| = ell in units R=1, see (a)
                vals[(i, j)] = dlambda(a, J, n)
        for L in range(nmax+1):
            tot = 0.
            for mm in range(-L, L+1):
                c = 0j
                for i, x in enumerate(theta_nodes):
                    th = np.arccos(x)
                    for j, ph in enumerate(phis):
                        c += wts[i]*(2*np.pi/len(phis))*vals[(i, j)]*np.conj(sph_harm_y(L, mm, th, ph))
                tot += abs(c)**2
            lev[a, L] = np.sqrt(tot)
    norm = lev.max()
    print(f' J={J}: norm of {{Lambda,T^a}} per fibre level L=0..{nmax}, each a, divided by the largest entry')
    print(lev/norm)

print('# (e) algebraic against derivative part: T^j rotates at rate ell/y0 per unit xi, the derivative term has m|q| per unit xi')
for (a0, a4) in [(5, 3), (13, 5), (5, 4), (25, 7)]:
    l = (a0*a0-a4*a4)**0.5
    print(f' (y0,y4)=({a0},{a4}), ell={l:.0f}: derivative/rotation at |q| ell = 1 is m y0/ell^2 = {a4*a0/l/l:.4f} = sinh(tau)cosh(tau) with sinh tau = m/ell')
