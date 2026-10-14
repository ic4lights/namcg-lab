"""Spin-2 and spin-0 coefficients of the flat-space quadratic action
   L = (1/(16 pi G)) sqrt(-g) R + c_W C^2 + c_R R^2
in signature (-,+,+,+), momentum space, using linearized curvatures.

Conventions (match chapters/appH-microscopic-proofs.tex, Problem C paragraph):
  S_EH^(2) = (1/(16 pi G)) * (1/4) h^{mu nu} E_{mu nu}[h],  E = -2 G^(1)[h].
  C^2 and R^2 start at second order, so their quadratic parts are squares
  of the linearized curvatures.
Plane wave h ~ e^{ikx}: d_mu -> i k_mu. For a real quadratic form we use
  d_a d_b -> -k_a k_b inside a single linear curvature and the bilinear
  pairing (X(k) X(-k)) -> |X|^2 with the overall sign handled by using
  K(k) = quadratic form evaluated as  h^T K h  with h real amplitudes and
  the curvature squared computed as Lin(k)*Lin(k) where Lin is the
  linearized curvature with d->k (one factor of i^2 = -1 per pair of
  derivatives, two pairs -> +1 for curvature-squared terms;
  EH: h * (d d h) -> -(k k) h h).
"""
import sympy as sp
import itertools

w, q = sp.symbols('omega q', real=True)
G, cW, cR = sp.symbols('G c_W c_R', real=True)
eta = sp.diag(-1, 1, 1, 1)
k_lo = sp.Matrix([-w, 0, 0, q])   # k_mu = eta_{mu nu} k^nu with k^nu=(w,0,0,q)
k_up = sp.Matrix([w, 0, 0, q])
k2 = sp.simplify((k_up.T * k_lo)[0])   # = -w^2 + q^2

# symbolic symmetric h_{mu nu} (lower indices)
hs = {}
for a in range(4):
    for b in range(a, 4):
        hs[(a, b)] = sp.Symbol(f'h{a}{b}', real=True)
def h(a, b):
    return hs[(min(a, b), max(a, b))]
hvec = [hs[key] for key in sorted(hs)]

def up(a):
    return eta[a, a]  # diagonal metric: raising multiplies by eta^{aa}

# Linearized Riemann R_{abcd} with d_a -> k_a (overall factor i^2 = -1 absorbed):
# R1_{abcd} = 1/2 (d_b d_c h_ad + d_a d_d h_bc - d_a d_c h_bd - d_b d_d h_ac)
# with d d -> -k k.
def Riem(a, b, c, d):
    kk = lambda x, y: -k_lo[x] * k_lo[y]
    return sp.Rational(1, 2) * (kk(b, c) * h(a, d) + kk(a, d) * h(b, c)
                                - kk(a, c) * h(b, d) - kk(b, d) * h(a, c))

R4 = {}
for a, b, c, d in itertools.product(range(4), repeat=4):
    R4[(a, b, c, d)] = sp.expand(Riem(a, b, c, d))
Ric = sp.zeros(4, 4)
for b, d in itertools.product(range(4), repeat=2):
    Ric[b, d] = sp.expand(sum(up(a) * R4[(a, b, a, d)] for a in range(4)))
Rs = sp.expand(sum(up(b) * Ric[b, b] for b in range(4)))

Riem2 = sp.expand(sum(up(a) * up(b) * up(c) * up(d) * R4[(a, b, c, d)]**2
                      for a, b, c, d in itertools.product(range(4), repeat=4)))
Ric2 = sp.expand(sum(up(a) * up(b) * Ric[a, b]**2 for a, b in itertools.product(range(4), repeat=2)))
C2 = sp.expand(Riem2 - 2 * Ric2 + Rs**2 / 3)
R2 = sp.expand(Rs**2)

# Einstein-Hilbert quadratic: (1/4) h^{ab} E_ab, E = -2 G1, G1 = Ric - 1/2 eta R
# Here Ric already contains d d -> -k k (a single factor of i^2), and the
# pairing h(-k) * (k k h(k)) for real amplitudes gives exactly this.
G1 = Ric - sp.Rational(1, 2) * eta * Rs
EH = sp.expand(sp.Rational(1, 4) * sum(up(a) * up(b) * h(a, b) * (-2 * G1[a, b])
                                     for a, b in itertools.product(range(4), repeat=2)))

Lag = sp.expand(EH / (16 * sp.pi * G) + cW * C2 + cR * R2)

# Quadratic-form matrix K with Lag = h^T K h over independent components
# (off-diagonal components counted twice in tensor contractions).
def mixed_tensor_form(expr):
    # convert to tensor-index form M_{ab,cd} acting on symmetric h
    M = {}
    for (a, b), (c, d) in itertools.product(sorted(hs), repeat=2):
        x, y = hs[(a, b)], hs[(c, d)]
        coeff = sp.diff(expr, x, y) / (2 if x == y else 1)
        if x != y:
            coeff = coeff / 2
        M[((a, b), (c, d))] = sp.simplify(coeff)
    return M

# Projectors (Barnes-Rivers) on symmetric tensors, mixed index placement
theta = sp.zeros(4, 4)
omega_ = sp.zeros(4, 4)
for m, n in itertools.product(range(4), repeat=2):
    omega_[m, n] = k_lo[m] * k_lo[n] / k2
    theta[m, n] = eta[m, n] - omega_[m, n]
def P2(a, b, c, d):
    return (sp.Rational(1, 2) * (theta[a, c] * theta[b, d] + theta[a, d] * theta[b, c])
            - sp.Rational(1, 3) * theta[a, b] * theta[c, d])
def P0s(a, b, c, d):
    return sp.Rational(1, 3) * theta[a, b] * theta[c, d]

# Build full tensor K^{ab cd} via symmetric derivative of Lag w.r.t. h_ab (lower)
def dh(a, b):
    return hs[(min(a, b), max(a, b))]
def Kt(a, b, c, d):
    x, y = dh(a, b), dh(c, d)
    val = sp.diff(Lag, x, y)
    # each independent off-diagonal symbol stands for two tensor entries
    fac = 1
    if a != b:
        fac *= 2
    if c != d:
        fac *= 2
    return val / fac / 2  # Lag = (1/2)?? -> use L = h_ab K^{abcd} h_cd
# L = h_ab K^{abcd} h_cd  =>  d^2 L / dh_x dh_y relates to K with multiplicities.

def coeff(P, dim):
    tot = 0
    for a, b, c, d in itertools.product(range(4), repeat=4):
        # K^{abcd} (upper) contracted with P_{cd ab}? use P with lower indices
        # P_{ab cd} built from lower theta; contract K^{ab cd} P_{cd ab}
        tot += Kt(a, b, c, d) * P(c, d, a, b)
    return sp.simplify(sp.factor(tot / dim))

a2 = coeff(P2, 5)
a0 = coeff(P0s, 1)
print('k^2 =', k2)
print('spin-2 coefficient  a2(k) =', sp.factor(a2.subs(q**2, k2 + w**2)))
print('spin-0s coefficient a0(k) =', sp.factor(a0.subs(q**2, k2 + w**2)))

K2 = sp.Symbol('k2')
a2k = sp.factor(sp.simplify(a2.subs(q, sp.sqrt(K2 + w**2))))
a0k = sp.factor(sp.simplify(a0.subs(q, sp.sqrt(K2 + w**2))))
print('a2 as function of k2:', a2k)
print('a0 as function of k2:', a0k)

# Propagator between conserved sources: T P2 T' / a2 + T P0s T' / a0
# For conserved sources T P2 T' = TT' - (1/3) T T', T P0s T' = (1/3) T T'.
print('zeros of a2 (besides k2=0):', sp.solve(sp.Eq(sp.cancel(a2k / K2), 0), K2))
print('zeros of a0 (besides k2=0):', sp.solve(sp.Eq(sp.cancel(a0k / K2), 0), K2))
# residues of 1/a2 at k2=0 and at the massive zero
m2sym = sp.solve(sp.Eq(sp.cancel(a2k / K2), 0), K2)[0]
res0 = sp.simplify(sp.residue(1 / a2k, K2, 0))
resm = sp.simplify(sp.residue(1 / a2k, K2, m2sym))
print('spin-2: residue at k2=0:', res0, ' residue at extra zero:', resm,
      ' ratio:', sp.simplify(resm / res0))
m0sym = sp.solve(sp.Eq(sp.cancel(a0k / K2), 0), K2)[0]
r00 = sp.simplify(sp.residue(1 / a0k, K2, 0))
r0m = sp.simplify(sp.residue(1 / a0k, K2, m0sym))
print('spin-0: residue at k2=0:', r00, ' residue at extra zero:', r0m,
      ' ratio:', sp.simplify(r0m / r00))
print('Stelle check: with c_W=-alpha/2, extra spin-2 zero at k2 =',
      sp.simplify(m2sym.subs(cW, -sp.Symbol('alpha') / 2)))

# Gauss-Bonnet quadratic form on flat space: should vanish identically
# (total derivative), so it adds nothing to either spin projection.
EGB = sp.expand(Riem2 - 4 * Ric2 + Rs**2)
print('Gauss-Bonnet quadratic form identically zero:', sp.simplify(EGB) == 0)
