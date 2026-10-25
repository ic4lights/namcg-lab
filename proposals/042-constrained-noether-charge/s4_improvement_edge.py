"""s4: an extension term f^{abcd} Riem(gamma)_{abcd} (zero on the class, gamma flat) shifts the
gamma-stress (eta-stress) by an identically conserved improvement and the Sigma charge by the
Wald term of f; the two shifts are equal by Stokes.

(i)  E^{bd} := Euler-Lagrange derivative of f^{abcd} R^{(1)}_{abcd}[h] w.r.t. h_{bd} at flat gamma
     equals -2 d_a d_c f^{abcd} (symmetrised in bd), for polynomial f with the algebraic
     symmetries of a curvature tensor;
(ii) for a Killing field xi of the flat metric (rotation / boost of the (x0,x1) plane),
     with Q^{ab} = -2 f^{abcd} d_c xi_d - 4 (d_d f^{abcd}) xi_c,
     d_b Q^{ab} = 2 xi_c E^{ac}  identically (exact polynomial identity; the d xi terms cancel
     by the first Bianchi symmetry of f and the Killing property of xi).
Hence int_C 2 xi_c E^{ac} dSigma_a = boundary integral of Q, and on Sigma (xi = 0)
Q^{ab} = -2 f^{abcd} d_c xi_d, the Wald form of f.  Both signatures.
"""
import itertools
import random
import sympy as sp

random.seed(3)
x = sp.symbols('x0:4')
N = 4


def rr():
    return sp.Rational(random.randint(-6, 6), 3)


def curv_tensor_from(S):
    # K^{abcd} = S^{ac} S^{bd} - S^{ad} S^{bc}, S symmetric: algebraic curvature tensor
    K = {}
    for a, b, c, d in itertools.product(range(N), repeat=4):
        K[(a, b, c, d)] = S[a, c] * S[b, d] - S[a, d] * S[b, c]
    return K


def random_poly(deg=3):
    mons = [m for m in itertools.product(range(deg + 1), repeat=4) if sum(m) <= deg]
    return 1 + sum(rr() * sp.Mul(*[x[i] ** m[i] for i in range(4)]) for m in random.sample(mons, 8))


def make_f():
    f = {k: 0 for k in itertools.product(range(N), repeat=4)}
    for _ in range(2):
        S = sp.Matrix(4, 4, lambda i, j: 0)
        for i in range(4):
            for j in range(i, 4):
                S[i, j] = S[j, i] = rr()
        K = curv_tensor_from(S)
        phi = random_poly()
        for k in f:
            f[k] += phi * K[k]
    return f


def check(eta, xi_up, label):
    out = []
    f = make_f()  # f^{abcd} (all indices up)
    etai = eta.inv()
    # symmetry checks
    ok = all(sp.expand(f[(a, b, c, d)] + f[(b, a, c, d)]) == 0 and sp.expand(f[(a, b, c, d)] - f[(c, d, a, b)]) == 0
             and sp.expand(f[(a, b, c, d)] + f[(a, c, d, b)] + f[(a, d, b, c)]) == 0
             for a, b, c, d in itertools.product(range(N), repeat=4))
    out.append(f"[{label}] f has Riemann symmetries incl. first Bianchi: {ok}")
    # (i) linearised Riemann R^{(1)}_{abcd} = 1/2 (d_b d_c h_ad + d_a d_d h_bc - d_a d_c h_bd - d_b d_d h_ac)
    hs = {}
    for i in range(N):
        for j in range(i, N):
            hs[(i, j)] = sp.Function(f'h{i}{j}')(*x)
            hs[(j, i)] = hs[(i, j)]
    def dd(e, i, j):
        return sp.diff(e, x[i], x[j])
    L = 0
    for a, b, c, d in itertools.product(range(N), repeat=4):
        if f[(a, b, c, d)] == 0:
            continue
        R1 = sp.Rational(1, 2) * (dd(hs[(a, d)], b, c) + dd(hs[(b, c)], a, d) - dd(hs[(a, c)], b, d) - dd(hs[(b, d)], a, c))
        L += f[(a, b, c, d)] * R1
    L = sp.expand(L)
    allok = True
    for (i, j) in [(0, 0), (0, 1), (1, 2), (2, 3), (3, 3)]:
        hij = hs[(i, j)]
        EL = 0
        for m in range(N):
            for n in range(N):
                coeff = L.coeff(sp.Derivative(hij, x[m], x[n])) if m != n else L.coeff(sp.Derivative(hij, (x[m], 2)))
                if m != n and m > n:
                    continue
                EL += sp.diff(coeff, x[m], x[n])
        # predicted: -2 d_a d_c f^{a i c j} symmetrised, times multiplicity (h_ij = h_ji appears for both orders)
        pred = -2 * sum(sp.diff(f[(a, i, c, j)], x[a], x[c]) for a in range(N) for c in range(N))
        if i != j:
            pred = pred + -2 * sum(sp.diff(f[(a, j, c, i)], x[a], x[c]) for a in range(N) for c in range(N))
        allok &= sp.expand(EL - pred) == 0
    out.append(f"[{label}] (i) Euler-Lagrange derivative = -2 d_a d_c f^(a b c d) (sym): {allok}")
    # (ii) Noether-type identity with lowered indices; fl = f with all indices down
    fl = {}
    for a, b, c, d in itertools.product(range(N), repeat=4):
        fl[(a, b, c, d)] = sum(eta[a, p] * eta[b, q] * eta[c, r] * eta[d, s] * f[(p, q, r, s)]
                               for p in range(N) for q in range(N) for r in range(N) for s in range(N)
                               if f[(p, q, r, s)] != 0)
    xi_dn = [sum(eta[i, j] * xi_up[j] for j in range(N)) for i in range(N)]
    # work with all-up f and xi_up, d^a = eta^{ab} d_b
    def dup(e, a):
        return sum(etai[a, b] * sp.diff(e, x[b]) for b in range(N))
    Q = {}
    for a in range(N):
        for b in range(N):
            Q[(a, b)] = sp.expand(-2 * sum(f[(a, b, c, d)] * sp.diff(xi_dn[d], x[c]) for c in range(N) for d in range(N))
                                  - 4 * sum(sp.diff(f[(a, b, c, d)], x[d]) * xi_dn[c] for c in range(N) for d in range(N)))
    E = {}
    for a in range(N):
        for c in range(N):
            # E^{bd} = -2 d_a d_c f^{abcd}  ->  E^{ac} = -2 d_b d_d f^{b a d c}
            E[(a, c)] = -2 * sum(sp.diff(f[(b, a, d, c)], x[b], x[d]) for b in range(N) for d in range(N))
    ok2 = True
    for a in range(N):
        lhs = sum(sp.diff(Q[(a, b)], x[b]) for b in range(N))
        rhs = 2 * sum(xi_dn[c] * E[(a, c)] for c in range(N))
        ok2 &= sp.expand(lhs - rhs) == 0
    out.append(f"[{label}] (ii) d_b Q^(ab) = 2 xi_c E^(ac) identically: {ok2}")
    Qsig = {k: sp.expand(v.subs({x[0]: 0, x[1]: 0})) for k, v in Q.items()}
    wald = {(a, b): sp.expand((-2 * sum(f[(a, b, c, d)] * sp.diff(xi_dn[d], x[c]) for c in range(N) for d in range(N))).subs({x[0]: 0, x[1]: 0}))
            for a in range(N) for b in range(N)}
    out.append(f"[{label}]      on Sigma Q = -2 f^(abcd) d_c xi_d: {all(sp.expand(Qsig[k] - wald[k]) == 0 for k in Q)}; nonzero there: {any(wald[k] != 0 for k in wald)}")
    return out


lines = []
lines += check(sp.eye(4), [-x[1], x[0], 0, 0], 'Euclid')
lines += check(sp.diag(-1, 1, 1, 1), [x[1], x[0], 0, 0], 'Lorentz')
print("\n".join(lines))
