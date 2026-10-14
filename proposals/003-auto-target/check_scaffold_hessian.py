"""Check 1 (proposal 003): Hessian of the displayed action on the flat scaffold.

Euclidean action of eq:Smicro at A_mu = 0 on g^(0) = delta:
    S_E = int Tr(d Phi^dag d Phi) + V,  V = (lam/4) Tr(Phi^dag Phi - v^2 I)^2.
Write Phi = phi0*I + sum_a (h_a + i k_a) T_a with Hermitian T_a, Tr(T_a T_b) = delta_ab,
so Tr(d delta^dag d delta) = sum (d h_a)^2 + (d k_a)^2 (checked below).
Then S'' = 2(-d^2 + E) with E = (1/2) Hess V.  We verify:
  (i)   kinetic Hessian is field independent (2 * identity on 32 real components);
  (ii)  at Phi_bar = phi0 I:  E_H = (lam/2)(3 phi0^2 - v^2) (x16), E_K = (lam/2)(phi0^2 - v^2) (x16);
  (iii) Hess V at a random non-constant-free background point contains no derivative data
        (trivially: V has no derivatives) -- recorded as the structural premise of Lemma 1;
  (iv)  conformally flat metric g = Omega^2 delta in 4D: sqrt(g) R = -6 Omega Box Omega
        (R > 0 on spheres), so the emergent-metric a_1 term gives
        Gamma_E > -(N0 Lambda^2/(192 pi^2)) * 6 (d sigma)^2 / v^2 = -(N0 Lambda^2/(32 pi^2 v^2)) (d sigma)^2.
"""
import itertools
import sympy as sp

lam, v, phi0 = sp.symbols('lambda v phi0', positive=True)

# Hermitian basis of 4x4 matrices orthonormal under Tr(T_a T_b)
def herm_basis(n=4):
    B = []
    for i in range(n):
        M = sp.zeros(n); M[i, i] = 1; B.append(M)
    for i, j in itertools.combinations(range(n), 2):
        M = sp.zeros(n); M[i, j] = M[j, i] = 1/sp.sqrt(2); B.append(M)
        M = sp.zeros(n); M[i, j] = -sp.I/sp.sqrt(2); M[j, i] = sp.I/sp.sqrt(2); B.append(M)
    return B

T = herm_basis()
assert len(T) == 16
for a in range(16):
    for b in range(16):
        assert sp.simplify((T[a]*T[b]).trace() - (1 if a == b else 0)) == 0

h = sp.symbols('h0:16', real=True)
k = sp.symbols('k0:16', real=True)
delta = sum(((h[a] + sp.I*k[a])*T[a] for a in range(16)), sp.zeros(4))
Phi = phi0*sp.eye(4) + delta

# (i) kinetic quadratic form: Tr(delta^dag delta) with delta -> d delta
kin = sp.expand((delta.H*delta).trace())
kin_target = sum(x**2 for x in h) + sum(x**2 for x in k)
print('(i) Tr(delta^dag delta) == sum h^2 + k^2 :', sp.simplify(kin - kin_target) == 0)

# (ii) potential Hessian at delta = 0
X = Phi.H*Phi - v**2*sp.eye(4)
V = sp.expand(lam/4*(X*X).trace())
vars_ = list(h) + list(k)
subs0 = {x: 0 for x in vars_}
grad = [sp.simplify(sp.diff(V, x).subs(subs0)) for x in vars_]
print('(ii) gradient at Phi_bar = phi0 I (should vanish only at phi0 = v):',
      sorted(set(sp.factor(g) for g in grad), key=str))
Hess = sp.Matrix(32, 32, lambda i, j: sp.diff(V, vars_[i], vars_[j]).subs(subs0))
E = (Hess/2).applyfunc(sp.simplify)
offdiag = [E[i, j] for i in range(32) for j in range(32) if i != j and E[i, j] != 0]
print('(ii) off-diagonal entries of E:', offdiag)
EH = set(sp.factor(E[i, i]) for i in range(16))
EK = set(sp.factor(E[i, i]) for i in range(16, 32))
print('(ii) E_H entries:', EH, ' target:', sp.factor(lam/2*(3*phi0**2 - v**2)))
print('(ii) E_K entries:', EK, ' target:', sp.factor(lam/2*(phi0**2 - v**2)))
sig = sp.symbols('sigma', real=True)
EHs = sp.expand((lam/2*(3*phi0**2 - v**2)).subs(phi0, v + sig))
EKs = sp.expand((lam/2*(phi0**2 - v**2)).subs(phi0, v + sig))
print('     at phi0 = v + sigma:  E_H =', EHs, ';  E_K =', EKs)
print('     dE_H/dsigma|0 =', sp.diff(EHs, sig).subs(sig, 0), '; dE_K/dsigma|0 =', sp.diff(EKs, sig).subs(sig, 0))
trE = 16*EHs + 16*EKs
print('     tr E(sigma) (no derivatives; enters only via Lambda^2 tr E):', sp.factor(trE))

# tree-level sigma normalisation: Phi_bar = (v + sigma) I  -> Tr(d Phi^dag d Phi) = 4 (d sigma)^2
print('     Tr(I) (d sigma)^2 coefficient N =', sp.eye(4).trace())

# (iv) conformally flat 4D Euclidean metric: sqrt(g) R
x = sp.symbols('x0:4', real=True)
Om = sp.Function('Omega')(*x)
g = Om**2*sp.eye(4)
ginv = g.inv()
dim = 4
Gam = [[[sum(ginv[l, m]*(sp.diff(g[m, i], x[j]) + sp.diff(g[m, j], x[i]) - sp.diff(g[i, j], x[m]))
             for m in range(dim))/2 for j in range(dim)] for i in range(dim)] for l in range(dim)]
def Riem(r, s, m, n):  # R^r_{smn}
    return (sp.diff(Gam[r][n][s], x[m]) - sp.diff(Gam[r][m][s], x[n])
            + sum(Gam[r][m][l]*Gam[l][n][s] - Gam[r][n][l]*Gam[l][m][s] for l in range(dim)))
Ric = sp.Matrix(dim, dim, lambda s, n: sum(Riem(r, s, r, n) for r in range(dim)))
R = sp.simplify(sum(ginv[i, j]*Ric[i, j] for i in range(dim) for j in range(dim)))
boxOm = sum(sp.diff(Om, xi, 2) for xi in x)
print('(iv) sqrt(g) R + 6 Omega Box Omega =', sp.simplify(Om**4*R + 6*Om*boxOm))
# sphere check of sign: unit S^4 via stereographic Omega = 2/(1+r^2) gives R = 12
r2 = sum(xi**2 for xi in x)
Rs = sp.simplify(R.subs(Om, 2/(1 + r2)).doit())
print('     R on stereographic unit S^4 (expect +12):', sp.simplify(Rs))
N0, LUV = sp.symbols('N_0 Lambda_UV', positive=True)
coef = -N0*LUV**2/(192*sp.pi**2)*6/v**2
print('(iv) emergent-metric a_1 term: Gamma_E coefficient of (d sigma)^2 =', sp.simplify(coef),
      ' (= -N0 Lambda^2/(32 pi^2 v^2))')
