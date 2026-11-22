#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
110: locked-sector coincidence value of the bilocal composite.

Data (live manuscript): G_{mu nu}(x,x) = v^-2 eta_AB Phi^A_mu Phi^B_nu
(eq:bilocal-frame-op with U(x,x)=I); locked polar data Phi = (v+sigma) *
Lambda * e (eq:polar, Repair II eq:vev-is-frame); eta = diag(-1,1,1,1).
Matrices below carry internal index A (row) and spacetime index mu (column):
G = Phi^T eta Phi.

L1  Boost*rotation family satisfies Lambda^T eta Lambda = eta.
L2  G(x,x)[(v+sigma) Lambda e] = (1+sigma/v)^2 E^T eta E exactly for that
    family and generic e: coincidence is the composite metric
    (eq:g-from-e) up to the positive radial factor; the internal (left)
    coset phase drops.  Checked symbolically (trigsimp) and numerically.
L3  det(E^T eta E) = det(eta) det(E)^2 (square locked frame), and
    G[E] is invariant under the left internal action E -> Lambda E
    (local-Lorentz redundancy of eq:g-from-e).  The right action on
    spacetime indices is NOT an invariance (it pushes G forward by O^T G O).
L4  Concrete inverter examples: E = I and E = boost give G = eta,
    det G = -1; E = diag(2,3,5,7) gives det G = -44100 exactly;
    rank-deficient E gives det G = 0.
L5  N>4 internal space: G = E^T eta_N E is no longer det(eta)*(det locked)^2;
    degenerate locked block can be made invertible by extra rows
    (equivalence of non-degeneracy with square-frame invertibility is a
    square-frame statement).
Symbolic output is a check, not a proof.
Re-run: python -I check_locked_coincidence.py   (expects ALL CHECKS PASS)
"""
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)
fails = []
def ck(name, cond):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)

def iszero4(M):
    return all(sp.simplify(sp.trigsimp(sp.expand(x))) == 0 for x in M)

def iszero4_num(M):
    return all(abs(sp.N(x, 30)) < sp.Float("1e-25") for x in M)

# --- L1: explicit Lorentz family (boost-x * rot-z)
xi, phi = sp.symbols('xi phi')
Bx = sp.Matrix([[sp.cosh(xi), sp.sinh(xi), 0, 0],
                [sp.sinh(xi), sp.cosh(xi), 0, 0],
                [0, 0, 1, 0], [0, 0, 0, 1]])
Rz = sp.Matrix([[1, 0, 0, 0], [0, sp.cos(phi), -sp.sin(phi), 0],
                [0, sp.sin(phi), sp.cos(phi), 0], [0, 0, 0, 1]])
Lam = sp.simplify(Bx * Rz)
ck("L1 Lorentz: Lam^T eta Lam = eta", iszero4(Lam.T*eta*Lam - eta))

# --- L2: coincidence with radial + coset factor
v, sgm = sp.symbols('v sigma', positive=True)
E = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"e{i}{j}"))
Phi = (v + sgm) / v * (Lam * E)      # Phi^A_mu, v-normalised: (1+sigma/v) Lam E
Gx = Phi.T * eta * Phi
tgt = ((v + sgm) / v)**2 * (E.T * eta * E)
ck("L2 G(x,x) = (1+sigma/v)^2 E^T eta E (coset drops)", iszero4(Gx - tgt))
ck("L2b vacuum sigma=0: G(x,x) = E^T eta E (constant of proportionality 1)",
   iszero4((Gx - E.T*eta*E).subs(sgm, 0)))
num = {xi: sp.Rational(3, 7), phi: sp.Rational(-5, 11), v: 4, sgm: sp.Rational(1, 3)}
num.update({E[i, j]: sp.Rational(2*i + 3*j + 1, 11) for i in range(4) for j in range(4)})
ck("L2c numeric random-instance agreement", iszero4_num((Gx - tgt).subs(num)))

# --- L3: determinant identity and left internal action
dG = sp.simplify((E.T*eta*E).det())
dE = sp.simplify(E.det())
ck("L3 det(E^T eta E) = det(eta) det(E)^2", sp.simplify(dG + dE**2) == 0)
ck("L3b left internal action invisible: (Lam E)^T eta (Lam E) = E^T eta E",
   iszero4((Lam*E).T*eta*(Lam*E) - E.T*eta*E))
ck("L3c right spacetime action is a pushforward: (E Bx)^T eta (E Bx) != E^T eta E",
   not iszero4_num(((E*Bx).T*eta*(E*Bx) - E.T*eta*E).subs(
       {xi: sp.Rational(1, 2), **{E[i, j]: sp.Rational(i + 2*j + 1, 7)
                                  for i in range(4) for j in range(4)}})))

# --- L4: concrete invertibility data
I4 = sp.eye(4)
ck("L4a E=I: G = eta, det = -1", (I4.T*eta*I4) == eta and (I4.T*eta*I4).det() == -1)
Gbx = sp.simplify(Bx.T*eta*Bx)
ck("L4b E=boost: G = eta", Gbx == eta)
Dd = sp.diag(2, 3, 5, 7)
ck("L4c E=diag(2,3,5,7): det G = -(2*3*5*7)^2 = -44100",
   (Dd.T*eta*Dd).det() == -44100)
R3 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
ck("L4d rank-3 E: det G = 0", (R3.T*eta*R3).det() == 0)
# radial scaling: quadratic form
aa = sp.symbols('alpha')
ck("L4e quadratic scaling G[(1+a)E] = (1+a)^2 G[E]",
   iszero4(((1+aa)*E).T*eta*((1+aa)*E) - (1+aa)**2*(E.T*eta*E)))

# --- L5: enlarged internal space N=6
eta6 = sp.diag(-1, 1, 1, 1, 1, 1)
E6 = sp.Matrix([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
                [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
G6 = E6.T*eta6*E6
locked = E6[:4, :]
ck("L5 locked block degenerate but N=6 composite invertible",
   locked.det() == 0 and G6.det() != 0)
print("G6 =", G6.tolist(), "det G6 =", G6.det(), "det locked =", locked.det())

print("FAILURES:", fails)
print("ALL CHECKS PASS" if not fails else "CHECKS FAILED")
