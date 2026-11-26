"""050 s9 (r2): the formulas of replacement R21 as written. (E_AB)^C_D = delta^C_A eta_BD - delta^C_B eta_AD on so(4,1), with
eta = diag(-1,1,1,1,1), A = 0..4, a = 0..3. Left-invariant fields on g represent the matrix commutator, and Y^A = g^A_4.
The field of E acts on g by g -> g(1 + tE), so the matrix identities carry over to the fields. Exact."""
import sympy as sp

n = 5
eta = sp.diag(-1, 1, 1, 1, 1)


def E(A, B):
    M = sp.zeros(n, n)
    for C in range(n):
        for D in range(n):
            M[C, D] = (1 if C == A else 0) * eta[B, D] - (1 if C == B else 0) * eta[A, D]
    return M


comm = lambda X, Y: X * Y - Y * X
print("Lie algebra: E_AB eta^{-1} antisymmetric:", all((E(A, B) * eta.inv()) == -(E(A, B) * eta.inv()).T for A in range(n) for B in range(n)))
T = [E(a, 4) for a in range(4)]
Tu = [eta[a, a] * T[a] for a in range(4)]
print("[E_a4, E_b4] = -E_ab:", all(comm(T[a], T[b]) == -E(a, b) for a in range(4) for b in range(4)))
print("[S_cd, D_a] = eta_ad D_c - eta_ac D_d with S = E_cd, D_a = E_a4:",
      all(comm(E(c, f), T[a]) == eta[a, f] * T[c] - eta[a, c] * T[f] for a in range(4) for c in range(4) for f in range(4)))
print("[T_a,[T^a,T^b]] = -3 T^b:", all(sum((comm(T[a], comm(Tu[a], Tu[b])) for a in range(4)), sp.zeros(n, n)) == -3 * Tu[b] for b in range(4)))
X = [sp.I * T[a] for a in range(4)]
Xu = [sp.I * Tu[a] for a in range(4)]
lhs = [sum((comm(Xu[b], comm(X[b], X[a])) for b in range(4)), sp.zeros(n, n)) for a in range(4)]
mu2 = sp.Symbol("mu2")
print("[X^b,[X_b,X_a]] = -mu^2 X_a with X_a = i E_a4 holds at mu^2 = -3:", all(lhs[a] == 3 * X[a] for a in range(4)))
print("relation with R: [D_a,D_b] = (1/2) R_ab^{cd} S_cd gives R_ab^{cd} = -(delta delta - delta delta), R_ab^{ae} = -3 delta_b^e, so Ric_b^e = 3 delta_b^e = -mu^2 delta_b^e")
g = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"g{i}{j}"))
Y = [g[A, 4] for A in range(n)]
print("E_ab annihilates Y^A (the field acts by g -> g E_ab):", all(((g * E(a, b))[A, 4]) == 0 for a in range(4) for b in range(4) for A in range(n)))
print("D_a Y^A = g^A_a (for E_a4, using eta_44 = 1):", all((g * T[a])[A, 4] == g[A, a] for a in range(4) for A in range(n)))
b1 = sp.Rational(3, 5), sp.Rational(4, 5)
Lb = sp.eye(n)
Lb[0, 0] = sp.Rational(5, 4); Lb[0, 4] = sp.Rational(3, 4); Lb[4, 0] = sp.Rational(3, 4); Lb[4, 4] = sp.Rational(5, 4)
Lr = sp.eye(n)
Lr[1, 1] = b1[0]; Lr[1, 4] = -b1[1]; Lr[4, 1] = b1[1]; Lr[4, 4] = b1[0]
g0 = Lb * Lr
print("sample element is in SO(4,1): g eta^{-1} g^T = eta^{-1}:", g0 * eta.inv() * g0.T == eta.inv())
print("eta^{ab} g^A_a g^B_b = eta^{AB} - Y^A Y^B at the sample:",
      all(sum(eta[a, a] * g0[A, a] * g0[B, a] for a in range(4)) == eta[A, B] - g0[A, 4] * g0[B, 4] for A in range(n) for B in range(n)))
print("Y.Y = eta_AB Y^A Y^B = 1 (unit de Sitter):", sum(eta[A, A] * g0[A, 4] ** 2 for A in range(n)))
print("so(3,1) spanned by E_ab acts irreducibly on span(E_a4), the isotropy of a symmetric pair: a subalgebra strictly containing it contains some E_a4 combination, then all, hence maximal (used in R6)")
