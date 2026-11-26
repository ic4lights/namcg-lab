"""s4: Is the replica family Theta^{12} = 1/f(x1,x2), Theta^{34} = 1, f = |z|^{n-1}, stationary under local frame rotations?

For the density kappa sqrtG X the rotation (Goldstone) equation is  A_{AB} = d_m( sqrtG P_X^{m|ln} e^A_l e^B_n ) (superpotential of s1, a1=1).
We evaluate A_{AB} for X, and for the invariant combination N and for W^2 as controls, on the family at a generic point (x1,x2) = (0.8, 0.5), d = 4, Euclidean eta,
for several n.  e^A_mu = eta^{AB} omega_{mu B},  omega = -f dx1^dx2 + dx3^dx4 (Theta = omega^{-1}).
"""
import sys
import numpy as np
import sympy as sp
sys.path.insert(0, '.')
from tj import Jets
import s1_rotation_noether_identity as s1

D = 4


def family_E(J, n, x0=(0.8, 0.5)):
    x1, x2 = sp.symbols('x1 x2')
    f = (x1**2 + x2**2)**sp.Rational(1, 2)**0 if False else (x1**2 + x2**2)**((sp.Float(n) - 1)/2)
    # Taylor jet of f about x0 in local variables y_i = x_i - x0_i, up to order J.ORD
    y1, y2 = sp.symbols('y1 y2')
    fy = f.subs({x1: x0[0] + y1, x2: x0[1] + y2})
    ser = sp.series(sp.series(fy, y1, 0, J.ORD+1).removeO(), y2, 0, J.ORD+1).removeO()
    poly = sp.Poly(sp.expand(ser), y1, y2)
    fj = np.zeros(J.M)
    for (a, b), co in poly.terms():
        if a + b <= J.ORD:
            fj[J.idx[(a, b, 0, 0)]] = float(co)
    E = np.zeros((D, D, J.M))
    # omega_{12} = -f, omega_{21} = f, omega_{34} = 1, omega_{43} = -1 ; e^A_mu = omega_{mu A} (eta = 1)
    om = np.zeros((D, D, J.M))
    om[0, 1] = -fj; om[1, 0] = fj
    om[2, 3, 0] = 1.0; om[3, 2, 0] = -1.0
    for A in range(D):
        for m in range(D):
            E[A, m] = om[m, A]
    return E


if __name__ == "__main__":
    eta = np.eye(D)
    J = Jets(D, 2)
    Nvec = np.array([0.25, 0.5, -1, 0, 0]); Xvec = np.array([1.0, 0, 0, 0, 0]); W2 = np.array([0, 0, 0, 0, 1.0])
    Svec = np.array([1/3, -2/3, 0, 0, 0])
    for n in (1.0, 0.8, 1.2):
        E = family_E(J, n)
        g = s1.geometry(J, E, eta, D)
        res = {}
        for name, al in [("X", Xvec), ("S^2", Svec), ("N", Nvec), ("W^2", W2)]:
            Q = s1.superpotential(J, g, D, al)
            dv = s1.divergence_at0(J, Q, D)
            res[name] = np.max(np.abs(dv))
        sc = s1.scalars(J, g, D)[:, 0]
        TT, TTp, V2, VW, W2v = sc
        print(f"n={n}: max|A_AB| for X: {res['X']:.4e}, S^2: {res['S^2']:.4e}, N: {res['N']:.1e}, W^2: {res['W^2']:.1e}   | X={TT:.4f}, S^2={(TT-2*TTp)/3:.4f}, V.V={V2:.4f}, W.W={W2v:.4f}")

    # control: generic Theta-class 2-jets (closed omega = dA), where S^2 != 0 and A[X] != 0
    from tj import random_class
    print("generic Theta-class jets (Euclidean and Lorentzian eta):")
    for eta_d in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        etad = np.diag(np.array(eta_d, float))
        for seed in (1, 2):
            c = random_class(J, seed, eta_d)
            etai = np.linalg.inv(etad)
            om = c['om']
            E = np.einsum('AB,mBc->Amc', etai, om)
            g = s1.geometry(J, E, etad, D)
            out = []
            for name, al in [("X", Xvec), ("S^2", Svec), ("N", Nvec), ("W^2", W2)]:
                Q = s1.superpotential(J, g, D, al)
                out.append(f"{name}: {np.max(np.abs(s1.divergence_at0(J, Q, D))):.2e}")
            sc = s1.scalars(J, g, D)[:, 0]
            print(f"  eta={eta_d} seed={seed}: max|A_AB| " + ", ".join(out) + f" | S^2 = {(sc[0]-2*sc[1])/3:.4f}, V.V - W.W = {sc[2]-sc[4]:.1e}")
