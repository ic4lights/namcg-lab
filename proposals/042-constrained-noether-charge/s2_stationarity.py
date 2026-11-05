"""s2: stationarity of the class fields under the joint flow, in covariant variables.

xi = rotation (Euclid) or boost (Lorentz) of the (x0,x1) plane; Sigma = {x0 = x1 = 0}.
Checks (symbolic, exact):
  - L_xi eta = 0 (xi is a Killing field of gamma = eta in the matrix chart);
  - the tensorial Lie derivative L_xi omega (both indices transformed, i.e. chart and matrix
    index rotated together) vanishes for omega in span{e01, e23} (constant) and for the cone
    family Theta^{01} = 1/f(r), Theta^{23} = 1, and does not vanish for a generic constant omega;
  - the (1,1) tensor e^alpha_mu = gamma^{alpha beta} omega_{mu beta} and G = omega gamma^{-1} omega^T
    are Lie-dragged;
  - the frame with an internal index (form index only transformed) is NOT dragged:
    L^int_xi e^A_mu = (d xi)^A_B e^B_mu, a rigid rotation (038);
  - the matrix coordinates X^a = x^a: L_xi X^a = xi^a = (d xi)^a_b X^b, the rigid eta-rotation;
  - at Sigma, B^a_b = d_b xi^a commutes with e (needed for the Wald comparison of s3).
"""
import sympy as sp

x = sp.symbols('x0:4', real=True)
a, c = sp.symbols('a c', nonzero=True)
f = sp.Function('f')


def lie_2form(xi, om):
    n = 4
    L = sp.zeros(n, n)
    for m in range(n):
        for nn in range(n):
            s = sum(xi[l] * sp.diff(om[m, nn], x[l]) for l in range(n))
            s += sum(om[l, nn] * sp.diff(xi[l], x[m]) for l in range(n))
            s += sum(om[m, l] * sp.diff(xi[l], x[nn]) for l in range(n))
            L[m, nn] = sp.simplify(s)
    return L


def lie_2cov(xi, g):
    return lie_2form(xi, g)  # same transformation law for any (0,2) tensor


def lie_11(xi, E, internal=False):
    # E[al][mu] = e^al_mu ; tensorial: xi.dE - E^be_mu d_be xi^al + E^al_be d_mu xi^be
    n = 4
    L = sp.zeros(n, n)
    for al in range(n):
        for mu in range(n):
            s = sum(xi[l] * sp.diff(E[al, mu], x[l]) for l in range(n))
            s += sum(E[al, b] * sp.diff(xi[b], x[mu]) for b in range(n))
            if not internal:
                s -= sum(E[b, mu] * sp.diff(xi[al], x[b]) for b in range(n))
            L[al, mu] = sp.simplify(s)
    return L


def run(eta, xi, rsq, label):
    out = [f"== {label} =="]
    out.append(f"L_xi eta = 0: {lie_2cov(xi, eta) == sp.zeros(4, 4)}")
    B = sp.Matrix(4, 4, lambda i, j: sp.diff(xi[i], x[j]))  # B^a_b = d_b xi^a
    cases = {}
    om1 = sp.zeros(4, 4); om1[0, 1] = a; om1[1, 0] = -a; om1[2, 3] = c; om1[3, 2] = -c
    cases['constant, span{e01,e23}'] = om1
    om2 = sp.zeros(4, 4); fr = f(rsq); om2[0, 1] = -fr; om2[1, 0] = fr; om2[2, 3] = -1; om2[3, 2] = 1
    cases['cone family Theta^01=1/f(r), Theta^23=1'] = om2
    om3 = sp.Matrix([[0, 1, 2, 3], [-1, 0, 5, 7], [-2, -5, 0, 11], [-3, -7, -11, 0]])
    cases['generic constant omega'] = om3
    for name, om in cases.items():
        Lom = lie_2form(xi, om)
        E = eta.inv() * om.T
        G = om * eta.inv() * om.T
        LE = lie_11(xi, E)
        LEint = lie_11(xi, E, internal=True)
        LG = lie_2cov(xi, G)
        out.append(f"[{name}]")
        out.append(f"   tensorial L_xi omega = 0: {Lom == sp.zeros(4, 4)}")
        out.append(f"   L_xi e (1,1 tensor) = 0: {LE == sp.zeros(4, 4)};  L_xi G = 0: {sp.simplify(LG) == sp.zeros(4, 4)}")
        out.append(f"   internal-index L_xi e - B e = 0: {sp.simplify(LEint - B * E) == sp.zeros(4, 4)};  internal L_xi e = 0: {LEint == sp.zeros(4, 4)}")
        E0 = E.subs({x[0]: 0, x[1]: 0})
        out.append(f"   [e, B] = 0 at Sigma: {sp.simplify(E0 * B - B * E0) == sp.zeros(4, 4)}")
    Xa = sp.Matrix(x)
    LX = sp.Matrix([sum(xi[l] * sp.diff(Xa[i], x[l]) for l in range(4)) for i in range(4)])
    out.append(f"matrix coordinates: L_xi X^a - B^a_b X^b = 0: {sp.simplify(LX - B * Xa) == sp.zeros(4, 1)}, L_xi X = 0: {LX == sp.zeros(4, 1)}")
    out.append(f"B (eta-lowered) antisymmetric: {sp.simplify(eta * B + (eta * B).T) == sp.zeros(4, 4)}")
    return out


lines = []
lines += run(sp.eye(4), [-x[1], x[0], 0, 0], x[0] ** 2 + x[1] ** 2, 'Euclid, rotation of (x0,x1)')
lines += run(sp.diag(-1, 1, 1, 1), [x[1], x[0], 0, 0], -x[0] ** 2 + x[1] ** 2, 'Lorentz, boost of (x0,x1)')
print("\n".join(lines))
