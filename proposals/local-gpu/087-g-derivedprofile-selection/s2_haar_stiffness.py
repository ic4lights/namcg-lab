# S2: Haar/Dirichlet(1,...,1) second moments, exact stiffness of the frame
# quadratic form Sigma_pi, degeneracy of the stiffness, and the universal
# per-frame upper bound. Exact symbolic where marked; floats where marked.
import sympy as sp
from sympy import beta, symbols, integrate, Rational, Matrix, zoo
import random

# --- (1) Dirichlet(1,...,1) simplex moments by the beta integral:
# E[q_i]   = B(2,1)/B(1,1)/D... use the standard Dirichlet moment formula
# E[q_i^a q_j^b] = Gamma(alpha) Gamma(alpha+a+b) / (Gamma(alpha+a) Gamma(alpha+b))
# at alpha_k = 1: E[q_i] = 1/D, E[q_i^2] = 2/(D(D+1)), E[q_i q_j] = 1/(D(D+1)).
# Verify by direct integration for D = 2, 3, 4.
for D in (2, 3, 4):
    a = symbols(' '.join('t%d' % k for k in range(1, D)), positive=True)
    if not isinstance(a, tuple):
        a = (a,)
    tot = 1
    for x in a:
        tot = tot * x
    dom = [sp.S.Zero, 1]
    lims = []
    prev = 1
    for x in a:
        lims.append((x, 0, prev)); prev = prev - x
    Z = 1
    # integrate the constant 1 over the simplex with the Dirichlet(1) density:
    norm = integrate(1, *lims[::-1])  # = 1/(D-1)!
    # E[q_1^2] with q_1 = 1 - t1 - ... :
    q1 = 1 - sum(a)
    e2 = integrate(q1**2, *lims[::-1]) / norm
    q2 = a[0]
    e12 = integrate(q1**2 * 1, (a[0], 0, 1)) if D == 2 else None
    assert sp.simplify(e2 - Rational(2, D * (D + 1))) == 0, (D, e2)
print("S2.1 Dirichlet(1) simplex second moment E[q_i^2]=2/(D(D+1)): symbolic "
      "beta-integral check D=2,3,4 OK (E[q_i]=1/D, E[q_i q_j]=1/(D(D+1)) by "
      "the same formula)")

# --- (2) exact form of Sigma_Haar = E[diag(q) - q q^T] and the 085 identity
for D in range(2, 9):
    S = Matrix(D, D, lambda i, j: (Rational(1, D) - Rational(2, D * (D + 1)))
               if i == j else -Rational(1, D * (D + 1)))
    J = Matrix.ones(D, D)
    I = Matrix.eye(D)
    Pc = I - J / D
    assert S == Pc / (D + 1)
    # g^T S g = (sum g^2 - W^2/D)/(D+1) = (D sum g^2 - W^2)/(D(D+1))
    g = symbols('g0:%d' % D)
    W = sum(g)
    lhs = sp.expand((Matrix(g).T * S * Matrix(g))[0])
    rhs = sp.expand((D * sum(x**2 for x in g) - W**2) / (D * (D + 1)))
    assert sp.simplify(lhs - rhs) == 0
    # eigenvalues: 0 (constants) and 1/(D+1) (multiplicity D-1)
    ev = sorted([sp.nsimplify(v) for v in S.eigenvals()])
    assert ev[0] == 0 and all(v == Rational(1, D + 1) for v in ev[1:])
print("S2.2 Sigma_Haar = (I - J/D)/(D+1) exact for D=2..8; spectrum {0, "
      "(D+1)^-1 (mult D-1)}; g^T Sigma g = (D sum g^2 - W^2)/(D(D+1)) = "
      "085 identity, symbolic OK")

# --- (3) stiffness: E_pi Gamma >= lam+ ||g - gbar||^2 (connected G_pi), and
# lam+ -> 0 for measures concentrating on single-coordinate frames.
# pi_eps = (1-eps) delta_{e1} + eps Haar: Sigma = eps/(D+1) (I - J/D) exactly,
# so lam+ = eps/(D+1) -> 0 while the locus stays {uniform} for every eps>0.
for D in (3, 4, 5):
    eps = Rational(1, 1000)
    Seps = (eps / (D + 1)) * (Matrix.eye(D) - Matrix.ones(D, D) / D)
    g = symbols('g0:%d' % D)
    qform = sp.expand((Matrix(g).T * Seps * Matrix(g))[0])
    gc = [x - sum(g) / D for x in g]
    tgt = eps / (D + 1) * sum(x**2 for x in gc)
    assert sp.simplify(qform - tgt) == 0
    ev = sorted(Seps.eigenvals())
    assert ev[0] == 0 and ev[1] == eps / (D + 1)
print("S2.3 mixture (1-eps)delta_e1 + eps Haar: Sigma = eps/(D+1)(I-J/D) "
      "exact, lam+ = eps/(D+1) with eps=1/1000, D=3,4,5; locus still "
      "{uniform}: stiffness degenerates, locus does not")

# --- (4) universal per-frame bound Gamma(u) <= (max g - min g)^2/4
# (Bhatia-Davis for the discrete law q) and hence <= ||g - gbar||^2 / 2.
random.seed(11)
worst_ratio = 0.0
for _ in range(4000):
    D = random.randint(2, 7)
    r = [random.random() for _ in range(D)]
    s = sum(r); q = [x / s for x in r]
    g = [random.uniform(-3, 3) for _ in range(D)]
    m = sum(qi * gi for qi, gi in zip(q, g))
    var = sum(qi * (gi - m)**2 for qi, gi in zip(q, g))
    rng = max(g) - min(g)
    assert var <= rng * rng / 4 + 1e-12
    gbar = sum(g) / D
    nn = sum((gi - gbar)**2 for gi in g)
    assert var <= nn / 2 + 1e-12
    if nn > 1e-9:
        worst_ratio = max(worst_ratio, var / nn)
print("S2.4 per-frame upper bounds Var_q(g) <= (max-min)^2/4 and <= ||g-c||^2/2: "
      "4000 random (q,g) OK; worst sampled ratio Var/||g-c||^2 = %.6f (<=1/2)"
      % worst_ratio)
print("S2 DONE")
