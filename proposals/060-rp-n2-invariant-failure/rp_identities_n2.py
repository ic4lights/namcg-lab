"""Symbolic checks for proposal 060 (reflection positivity failure, N=2 invariant algebra).

Conventions follow appH-microscopic-proofs.tex L1554:
    A_mu = sum_a A_mu^a sigma^a / 2,   G_ab = eta^{mu nu} A_mu^a A_nu^b.
We truncate the ten matrix coordinates to mu in {0,1,2} (one time, two space).
This covers every type of term in S_E (zero, one, or two time indices; the
two-time-index commutator [A_0,A_0] vanishes), so the checks are the general
ones with three named coordinates.

Checks:
 (1) Tr(A_0 A_1) = (1/2) sum_a A_0^a A_1^a                      (probe 1)
 (2) Tr([A_0,A_1] A_2) = (i/2) eps^{abc} A_0^a A_1^b A_2^c      (probe 2)
 (3) theta-oddness of both probes under theta: A_0^a -> -A_0^a
 (4) S_E is theta-invariant (truncated: terms (01),(02),(12))
 (5) the Pfaffian Gram G~_ab = sum_mu A^a_mu A^b_mu is theta-invariant
 (6) Tr(A_0 A_1) on R_1: A_0 = e^{-3 pi i/8} A~_0, A_1 = e^{pi i/8} A~_1
     equals e^{-pi i/4} * (1/2) sum_a A~_0^a A~_1^a  (continuation sign)
 (7) SU(2) covariance: for U the general quaternionic SU(2)-type matrix with
     U U^dagger = s I,  Tr(U X U^dagger) = s Tr(X) for X = [A_0,A_1] A_2,
     hence the normalized conjugation U/sqrt(s) leaves the probe invariant.
 (8) Gaussian toy reflection pairing: f = x0 x1, theta: x0 -> -x0,
     weight w = exp(-x0^2 - x1^2): normalized <f^theta, f>_theta = -1/4,
     and the even/odd split identity on a second test f = 1 + x0 x1.
"""
import sympy as sp

I = sp.I

s1 = sp.Symbol("s1", real=True)
s2 = sp.Symbol("s2", real=True)
s3 = sp.Symbol("s3", real=True)
x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4", real=True)

# Pauli matrices and the manuscript normalization A_mu = A^a_mu sigma^a / 2
sig1 = sp.Matrix([[0, 1], [1, 0]])
sig2 = sp.Matrix([[0, -I], [I, 0]])
sig3 = sp.Matrix([[1, 0], [0, -1]])
sigs = {1: sig1, 2: sig2, 3: sig3}

mu_list = [0, 1, 2]
a_list = [1, 2, 3]
Acoef = sp.zeros(3, 3)  # Acoef[mu_index, a_index]
symnames = {}
for m, mu in enumerate(mu_list):
    for a in a_list:
        symnames[(mu, a)] = sp.Symbol("A%d_%d" % (mu, a), real=True)

def Amat(mu):
    M = sp.zeros(2, 2)
    for a in a_list:
        M = M + symnames[(mu, a)] * sigs[a] / 2
    return sp.simplify(M)

A0, A1, A2 = Amat(0), Amat(1), Amat(2)

# (1) probe 1
lhs1 = sp.simplify((A0 * A1).trace())
rhs1 = sp.Rational(1, 2) * sum(symnames[(0, a)] * symnames[(1, a)] for a in a_list)
c1 = sp.simplify(lhs1 - rhs1)

# (2) probe 2
comm01 = sp.simplify(A0 * A1 - A1 * A0)
lhs2 = sp.simplify((comm01 * A2).trace())
eps = {(1,2,3):1,(2,3,1):1,(3,1,2):1,(2,1,3):-1,(3,2,1):-1,(1,3,2):-1}
rhs2 = I/2 * sum(eps[(a,b,c)] * symnames[(0,a)] * symnames[(1,b)] * symnames[(2,c)]
                 for a in a_list for b in a_list for c in a_list if (a,b,c) in eps)
c2 = sp.simplify(lhs2 - rhs2)

# (3) theta-oddness: substitute A_0^a -> -A_0^a
def theta_expr(e):
    rep = {symnames[(0, a)]: -symnames[(0, a)] for a in a_list}
    return sp.simplify(e.subs(rep))

c3a = sp.simplify(theta_expr(lhs1) + lhs1)     # f1(theta A) = -f1(A)?
c3b = sp.simplify(theta_expr(lhs2) + lhs2)     # f2(theta A) = -f2(A)?

# (4) S_E invariance.  ||[A,B]||^2 = -Tr([A,B]^2) (commutator anti-Hermitian, real coefs)
def se_trunc():
    tot = 0
    for m, mu in enumerate(mu_list):
        for n, nu in enumerate(mu_list):
            if m < n:
                Am, An = Amat(mu), Amat(nu)
                Cm = sp.simplify(Am * An - An * Am)
                tot = tot + sp.simplify(-(Cm * Cm).trace())
    return sp.expand(tot / 4)   # factor 1/(4 g^2), g=1

SE = se_trunc()
c4 = sp.simplify(theta_expr(SE) - SE)

# (5) Gram G~_ab = sum_mu A^a_mu A^b_mu invariance under theta
G = sp.zeros(3, 3)
for ia, a in enumerate(a_list):
    for ib, b in enumerate(a_list):
        G[ia, ib] = sum(symnames[(mu, a)] * symnames[(mu, b)] for mu in mu_list)
Gth = G.applyfunc(lambda e: sp.simplify(e.subs({symnames[(0, a)]: -symnames[(0, a)] for a in a_list})))
c5 = sp.simplify(G - Gth)
# and det G transforms by (det D)^2 = 1 under the row flip; check det invariance:
c5b = sp.simplify(G.det() - Gth.det())

# (6) continuation phase on R_1
ph0 = sp.exp(-3 * sp.pi * I / 8)
ph1 = sp.exp(sp.pi * I / 8)
lhs6 = sp.simplify((ph0 * A0 * ph1 * A1).trace())
rhs6 = sp.exp(-sp.pi * I / 4) * rhs1
c6 = sp.simplify(lhs6 - rhs6)

# (7) SU(2)-type covariance with quaternionic parametrization
al = x1 + I * x2
be = x3 + I * x4
U = sp.Matrix([[al, be], [-sp.conjugate(be), sp.conjugate(al)]])
s = sp.simplify((U * U.adjoint())[0, 0])          # U U^dag = s I
X = sp.simplify(comm01 * A2)
lhs7 = sp.simplify((U * X * U.adjoint()).trace())
c7 = sp.simplify(lhs7 - s * sp.simplify(X.trace()))
c7s = sp.simplify(s - (x1**2 + x2**2 + x3**2 + x4**2))

# (8) Gaussian toy reflection pairing
y0, y1 = sp.symbols("y0 y1", real=True)
w = sp.exp(-(y0**2 + y1**2))
f = y0 * y1
ft = (-y0) * y1          # f^theta
Z = sp.integrate(sp.integrate(w, (y0, -sp.oo, sp.oo)), (y1, -sp.oo, sp.oo))
P = sp.integrate(sp.integrate(ft * f * w, (y0, -sp.oo, sp.oo)), (y1, -sp.oo, sp.oo))
c8 = sp.simplify(P / Z)          # expected -1/4
g = 1 + y0 * y1
gt = 1 - y0 * y1
Pg = sp.integrate(sp.integrate(gt * g * w, (y0, -sp.oo, sp.oo)), (y1, -sp.oo, sp.oo))
c8b = sp.simplify(Pg / Z)        # expected 1 - 1/4 = 3/4 ; split: 1*1 - <(y0y1)^2>

print("check (1) Tr(A0A1) - (1/2)sum_a A0^a A1^a =", c1)
print("check (2) Tr([A0,A1]A2) - (i/2)eps A0A1A2 =", c2)
print("check (3) probe1 theta-odd:", c3a, " probe2 theta-odd:", c3b)
print("check (4) S_E(theta A) - S_E(A) =", c4)
print("check (5) Gram theta-invariant:", c5, "; det Gram:", c5b)
print("check (6) R_1 continuation Tr(A0A1) - e^{-pi i/4}(1/2)sum =", c6)
print("check (7) Tr(U X U^dag) - s Tr X =", c7, "; s - (x1^2+..+x4^2) =", c7s)
print("check (8) normalized reflected pairing of f=y0y1 =", c8)
print("check (8b) normalized reflected pairing of g=1+y0y1 =", c8b)
allok = (c1 == 0 and c2 == 0 and c3a == 0 and c3b == 0 and c4 == 0
         and all(sp.simplify(e) == 0 for e in list(c5)) and c5b == 0
         and c6 == 0 and c7 == 0 and c7s == 0
         and c8 == sp.Rational(-1, 4) and c8b == sp.Rational(3, 4))
print("ALL_CHECKS_PASS:", allok)
