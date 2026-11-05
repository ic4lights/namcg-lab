"""s1: the eta dependence of the Poisson-class invariants is a dependence on gamma = phi^* eta.

(a) Covariance.  A closed two-form omega in the matrix chart x (eta constant) is pulled
    back by a random polynomial chart change x = phi(y).  The invariants X, TT', V^2, calT,
    div V and R_G are computed in the chart y with the pulled-back metric gamma = phi^* eta
    (non-constant, flat) and the gamma-covariant torsion of e = gamma^{-1} omega^T; they equal
    the same invariants computed in the matrix chart with eta and partial derivatives.
(b) The identity R_G + calT + 2 div V = R_W, with R_W the Weitzenboeck scalar built from
    Riem(gamma), holds at random jets of a NON-flat gamma; for flat gamma R_W = 0 and it
    reduces to the merged identity R = -calT - 2 div V.
Exact rational arithmetic at the base point.  Both signatures.
"""
import random
import sympy as sp
from jetlib import H, N, P, mconst, mmul, mT, torsion_package, trunc

random.seed(42)
x = sp.symbols('x0:4')


def rr(a=-3, b=3, den=4):
    return sp.Rational(random.randint(a * den, b * den), den)


def random_closed_omega(scale=sp.Rational(1, 3)):
    # constant invertible part + d(A), A cubic polynomial
    om0 = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i + 1, 4):
            v = rr()
            om0[i, j] = v
            om0[j, i] = -v
    while om0.det() == 0:
        return random_closed_omega(scale)
    A = []
    for mu in range(4):
        a = 0
        for i in range(4):
            for j in range(i, 4):
                a += scale * rr() * x[i] * x[j]
                for k in range(j, 4):
                    a += scale * rr() / 3 * x[i] * x[j] * x[k]
        A.append(a)
    om = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            om[m, n] = om0[m, n] + sp.diff(A[n], x[m]) - sp.diff(A[m], x[n])
    return om


def run(eta, label):
    out = []
    om_x = random_closed_omega()
    x0 = [rr(-1, 1, 3) for _ in range(4)]
    # (i) matrix chart: gamma = eta, expansion x = x0 + h
    sub = {x[i]: x0[i] + H[i] for i in range(4)}
    om_h = [[P(om_x[i, j].subs(sub)) for j in range(4)] for i in range(4)]
    gam_h = mconst(eta)
    r1 = torsion_package(gam_h, om_h)
    # (ii) chart y: x = x0 + L h + q(h) + c(h); y = h
    L = sp.Matrix(4, 4, lambda i, j: (1 if i == j else 0) + rr(-1, 1, 4))
    phi = []
    for i in range(4):
        e = x0[i] + sum(L[i, j] * H[j] for j in range(4))
        for a in range(4):
            for b in range(a, 4):
                e += rr(-1, 1, 6) * H[a] * H[b]
                for c in range(b, 4):
                    e += rr(-1, 1, 8) * H[a] * H[b] * H[c]
        phi.append(e)
    J = sp.Matrix(4, 4, lambda i, j: sp.diff(phi[i], H[j]))   # J[i][j] = d x^i / d y^j
    subphi = {x[i]: phi[i] for i in range(4)}
    om_phi = sp.Matrix(4, 4, lambda i, j: sp.expand(om_x[i, j].subs(subphi)))
    om_y = J.T * om_phi * J
    gam_y = J.T * eta * J
    om_yP = [[P(om_y[i, j]) for j in range(4)] for i in range(4)]
    gam_yP = [[P(gam_y[i, j]) for j in range(4)] for i in range(4)]
    r2 = torsion_package(gam_yP, om_yP)
    out.append(f"[{label}] (a) covariance, matrix chart vs random chart with gamma = phi^* eta:")
    for k in ['X', 'TTp', 'V2', 'calT', 'divV', 'R_G']:
        out.append(f"   {k:5s}: matrix chart {float(r1[k]): .10f}   y chart {float(r2[k]): .10f}   exact difference {sp.nsimplify(r1[k] - r2[k])}")
    out.append(f"   R_W in matrix chart = {r1['R_W']}, in y chart = {r2['R_W']} (flat gamma)")
    out.append(f"   R_G + calT + 2 divV: matrix chart {r1['R_G'] + r1['calT'] + 2 * r1['divV']}, y chart {r2['R_G'] + r2['calT'] + 2 * r2['divV']}")
    # (b) non-flat gamma
    for trial in range(3):
        om_x2 = random_closed_omega()
        sub0 = {x[i]: H[i] for i in range(4)}
        om2 = [[P(om_x2[i, j].subs(sub0)) for j in range(4)] for i in range(4)]
        g = sp.Matrix(eta)
        for i in range(4):
            for j in range(i, 4):
                pert = sum(rr(-1, 1, 5) * H[a] * H[b] for a in range(4) for b in range(a, 4)) + rr(-1, 1, 5) * H[(i + j) % 4]
                g[i, j] += pert
                if i != j:
                    g[j, i] = g[i, j]
        gP = [[P(g[i, j]) for j in range(4)] for i in range(4)]
        r3 = torsion_package(gP, om2)
        lhs = r3['R_G'] + r3['calT'] + 2 * r3['divV']
        out.append(f"[{label}] (b) non-flat gamma, trial {trial}: R_G+calT+2divV = {float(lhs): .12f}, R_W = {float(r3['R_W']): .12f}, exact lhs - R_W = {sp.simplify(lhs - r3['R_W'])}, R_W != 0: {r3['R_W'] != 0}")
    return out


if __name__ == '__main__':
    lines = []
    lines += run(sp.eye(4), 'Euclid')
    lines += run(sp.diag(-1, 1, 1, 1), 'Lorentz')
    print("\n".join(lines))
