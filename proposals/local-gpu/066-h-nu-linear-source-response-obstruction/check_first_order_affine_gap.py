"""Proposal 066, check 2.

(a) Analytic perturbation of a ladder: for H(lam) = H0 + lam*V (finite matrix
    truncation of the conditional-lemma ladder, V Hermitian, non-degenerate
    gaps), the level spacings are series in lam with only integer powers; the
    gap is affine at first order.
(b) Counterexample outside the class: a lam-dependent coupling sqrt(lam) gives
    a gap 2*sqrt(lam): a half-integer power appears exactly when the source
    dependence is not of the analytic form H0 + lam*V.
(c) Gap equations: Delta(Delta + m) = lam has an analytic small-lam branch
    (Delta ~ lam/m); Delta^2 = lam gives Delta ~ sqrt(lam) and is not
    first-order perturbation theory of a fixed operator.
(d) Single-mode coherent displacement (the conditional-lemma state): a unitary
    Weyl displacement leaves the spectrum of the modular Hamiltonian
    K = -ln rho invariant; the relative entropy and the mean modular-energy
    shift are exactly beta*|alpha|^2, i.e. linear in the intensity.

Symbolic output is a check, not a proof.
"""
import sympy as sp

lam = sp.symbols('lambda_', positive=True)
D, a1, e1, v = sp.symbols('Delta a e nu', real=True)
E = sp.symbols('E')

# (a) two-level truncation of a ladder: E0 = 0, E1 = Delta at lam = 0.
H = sp.Matrix([[lam*a1, lam*v], [lam*v, D + lam*e1]])
char = sp.det(H - E*sp.eye(2))
r = sp.solve(sp.Eq(char, 0), E)
# r[0] - r[1] is plus/minus the square root of the discriminant; the gap is
# that non-negative root difference, written directly:
disc = sp.simplify((r[0] - r[1])**2)
gap_expr = sp.sqrt(disc)
print("(a) exact gap of H0 + lambda*V (2x2):")
print("    ", gap_expr)
print("    series =", sp.series(gap_expr, lam, 0, 4).removeO())

import numpy as np
H0 = np.diag([0.0, 1.0, 2.0])
V = np.array([[0.3, 0.4, 0.0], [0.4, -0.2, 0.5], [0.0, 0.5, 0.1]])
for L in (1e-2, 1e-3, 1e-4):
    w = np.linalg.eigvalsh(H0 + L*V)
    lin1 = (w[1] - w[0] - 1.0)/L
    lin2 = (w[2] - w[1] - 1.0)/L
    print("    lambda =%.0e : (gap1-shift)/lambda = %.6f , (gap2-shift)/lambda = %.6f"
          % (L, lin1, lin2))
print("    finite limits (gap shifts = difference of diagonal first-order level")
print("    shifts): V11 - V00 =", V[1, 1] - V[0, 0], " , V22 - V11 =", V[2, 2] - V[1, 1])

# (b) non-analytic coupling outside the class
print()
print("(b) gap of H = [[0, sqrt(lam)],[sqrt(lam), 0]] :",
      sp.simplify(sp.sqrt(4*lam)), "; series:", sp.series(2*sp.sqrt(lam), lam, 0, 3))

# (c) gap equations
m = sp.symbols('m', positive=True)
Ds = sp.symbols('Delta_', positive=True)
s1 = sp.solve(sp.Eq(Ds*(Ds + m) - lam, 0), Ds)
print()
print("(c) Delta(Delta+m)=lam positive root:", s1)
print("    series:", sp.series(s1[0], lam, 0, 3).removeO())
print("    Delta^2 = (1+beta)*lam  ->  Delta ~ sqrt(1+beta)*sqrt(lam)"
      " (fractional power; not an H0 + lambda*V expansion of a fixed operator)")

# (d) coherent displacement of the conditional-lemma thermal ladder (single mode)
import mpmath as mp
mp.mp.dps = 30
beta_n = mp.mpf('0.7')
amp = mp.mpf('0.37')
dim = 30
adag = mp.zeros(dim, dim)
for i in range(dim - 1):
    adag[i + 1, i] = mp.sqrt(i + 1)
a_op = adag.T
Gen = amp*adag - mp.conj(amp)*a_op          # anti-Hermitian generator
Dmat = mp.expm(Gen)
qf = mp.e**(-beta_n)
w = [(1 - qf)*qf**i for i in range(dim)]
rho0 = mp.zeros(dim, dim)
for i in range(dim):
    rho0[i, i] = w[i]
rho1 = Dmat*rho0*Dmat**-1

def spectrum(M):
    vals = mp.eig(M)[0]
    return sorted(mp.re(z) for z in vals)

w0 = spectrum(rho0)
w1 = spectrum(rho1)
maxspecdiff = max(abs(u - v) for u, v in zip(w0, w1))
print()
print("(d) spectrum of K = -ln rho under a Weyl displacement: max eigenvalue difference =",
      mp.nstr(maxspecdiff, 5))
Tr_rho1_ln_rho1 = mp.fsum(wi*mp.log(wi) for wi in w1 if wi > mp.mpf('1e-40'))
Tr_rho1_ln_rho0 = mp.fsum(rho1[i, i]*mp.log(w[i]) for i in range(dim))
Srel = Tr_rho1_ln_rho1 - Tr_rho1_ln_rho0
pred = beta_n*amp**2
print("    truncated S(rho_alpha || rho_0) =", mp.nstr(Srel, 12),
      "; exact beta*|alpha|^2 =", mp.nstr(pred, 12))
mean_n0 = mp.fsum(i*w[i] for i in range(dim))
mean_n1 = mp.re(mp.fsum(rho1[i, i]*i for i in range(dim)))
print("    <K>_1 - <K>_0 =", mp.nstr(beta_n*(mean_n1 - mean_n0), 12),
      "(linear in intensity |alpha|^2 ); |alpha|^2 =", mp.nstr(amp**2, 8))
