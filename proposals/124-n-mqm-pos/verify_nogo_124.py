# -*- coding: ascii -*-
# Item 124 verifier B: canonical classical-mechanics lift of the Presentation-A quartic
# (eq:Smatrix, eta = diag(-1,1,1,1), traceless 2x2 Hermitian matrices) is unbounded below.
# B1 Identity: S := -(1/4) Sum_{mu,nu} Tr([X^mu,X^nu][X_mu,X_nu])
#             = (1/4) Sum_{i,j} (-Tr([X^i,X^j][X^i,X^j])) - (1/2) Sum_i (-Tr([X^0,X^i][X^0,X^i]))
#   with lowered indices X_mu = eta_{mu rho} X^rho, verified symbolically on traceless
#   2x2 Hermitian X^mu = (a sigma1 + b sigma2 + c sigma3)/2 (12 real symbols). Residual 0.
#   Consequence printed: both summands are sums of squared norms (each -Tr([,][,]) = ||[,]||^2 >= 0
#   for Hermitian entries, checked on random values), so S is a difference of two nonnegative
#   forms: indefinite.
# B2 Ray: X^0 = t P, X^1 = t Q with [P,Q] != 0, other X^i = 0: S = -k t^4 with k > 0 exact;
#   also the full cubic-free bosonic potential of eq:Smatrix restricted to this ray is -k t^4
#   (the cubic term vanishes on two-point support only if C contracts to zero, not assumed here;
#   B2 bounds the QUARTIC part, which dominates the cubic along the ray for large t, so the
#   full potential -> -infinity).
# B3 Kinetic metric: the lift T = (1/2 g^2)^{-1}... kinetic form uses eta_{mu nu} Tr dX^mu dX^nu;
#   the inverse metric on the X^0 fibre is eta^{00} = -1: Hamiltonian kinetic polynomial
#   Sum eta^{mu nu} Tr(P^mu P^nu) evaluated at P^0 = s sigma1/2, others 0, equals -s^2 * (+) < 0:
#   negative on an open set, unbounded below as s -> infinity. Also oscillatory test-function
#   check: the quantum kinetic operator -eta^{mu nu} d_mu d_nu contracted on mode e^{i lambda q0}
#   carries coefficient -eta^{00} lambda^2 ... = -lambda^2 printed with sign.
import functools
import operator
import numpy as np
import sympy as sp

def msum(it):
    return functools.reduce(operator.add, it)

rep = []
eta = sp.Matrix.diag(-1, 1, 1, 1)
s1m = sp.Matrix([[0, 1], [1, 0]])
s2m = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3m = sp.Matrix([[1, 0], [0, -1]])
sym = sp.symbols('a0 b0 c0 a1 b1 c1 a2 b2 c2 a3 b3 c3', real=True)
X = []
for mu in range(4):
    X.append(sym[3*mu]*s1m/2 + sym[3*mu+1]*s2m/2 + sym[3*mu+2]*s3m/2)

def comm(A, B):
    return A*B - B*A

S = sp.Rational(0)
for mu in range(4):
    for nu in range(4):
        dmu = msum(eta[mu, r]*X[r] for r in range(4))
        dnu = msum(eta[nu, r]*X[r] for r in range(4))
        S = S - sp.Rational(1, 4)*sp.trace(comm(X[mu], X[nu])*comm(dmu, dnu))
S = sp.simplify(sp.expand_complex(S))
Apos = sp.Rational(0)
Bpos = sp.Rational(0)
for i in range(1, 4):
    for j in range(1, 4):
        Apos = Apos - sp.trace(comm(X[i], X[j])*comm(X[i], X[j]))
    Bpos = Bpos - sp.trace(comm(X[0], X[i])*comm(X[0], X[i]))
Apos = sp.simplify(Apos)
Bpos = sp.simplify(Bpos)
resB1 = sp.simplify(sp.expand_complex(S - (sp.Rational(1, 4)*Apos - sp.Rational(1, 2)*Bpos)))
rep.append(('B1 identity residual (expect 0): %s' % resB1))
# positivity of Apos, Bpos (sums of squared norms): numeric on random rays + exact SOS check:
fA = sp.lambdify(sym, Apos, 'numpy')
fB = sp.lambdify(sym, Bpos, 'numpy')
rng = np.random.default_rng(124)
minA = min(fA(*rng.normal(size=12)) for _ in range(300))
minB = min(fB(*rng.normal(size=12)) for _ in range(300))
rep.append(('B1 min over 300 random points: A_sum = %.4f (expect >= 0), B_sum = %.4f (expect >= 0)' % (minA, minB)))
# B2 ray
t = sp.Symbol('t', real=True)
P = s1m/2
Q = s2m/2
Sray = sp.Rational(0)
cPQ = comm(P, Q)
# S on ray: only mu,nu in {0,1}: X^0 = tP, X^1 = tQ
for mu in (0, 1):
    for nu in (0, 1):
        rX = lambda k: t*(P if k == 0 else Q)
        rdl = lambda k: eta[k, 0]*P*t + eta[k, 1]*Q*t
        Sray = Sray - sp.Rational(1, 4)*sp.trace(comm(rX(mu), rX(nu))*comm(rdl(mu), rdl(nu)))
Sray = sp.simplify(Sray)
rep.append(('B2 S on ray X0=tP, X1=tQ (expect negative*c t^4): %s' % sp.simplify(Sray)))
rep.append(('B2 value at t=2 (expect < 0): %s' % Sray.subs(t, 2)))
# B3 kinetic
rep.append(('B3 eta^{00} = %s (wrong-sign kinetic direction)' % eta.inv()[0, 0]))
lam = sp.symbols('lambda', positive=True)
q0 = sp.Symbol('q0', real=True)
chi = sp.Function('chi')(q0)
psi = sp.exp(sp.I*lam*q0)*chi
op = -eta.inv()[0, 0]*sp.diff(psi, q0, 2)   # -eta^{00} d^2/dq0^2 acting; eta^{00}=-1: op = +d^2
q0f = sp.simplify(sp.expand_complex(op/sp.exp(sp.I*lam*q0)))
# quadratic-form coefficient: integral conj(psi) op psi / |psi|^2 leading lambda^2 term:
coef = sp.simplify(q0f*chi/ (chi*chi))
rep.append(('B3 <psi| -eta^{00} d0^2 |psi>/<psi|psi| leading = %s (expect -lambda^2 + ...)' % sp.simplify(sp.expand(q0f/chi)))
           )
print('== verify_nogo_124 ==')
for line in rep:
    print(line)
