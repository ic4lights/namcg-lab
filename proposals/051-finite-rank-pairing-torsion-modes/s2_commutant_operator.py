"""051 s2: commutant labels at operator level. Exact arithmetic except part C (floating point, residual printed).

 A  Flat class, d = 4, u a general 4 x 4 coordinate matrix (the identities use only X_a = i u_a^b d_b):
    on a test function F(y,u), with J the derivation V of s1 and q rational and not null, K^{ef} = eta^{ab} u_a^e u_b^f,
      [X^b,[X_b, e^{iq.y} J]] F = (K.q.q) e^{iq.y} J F,
    and for R, the fibre part of V alone, the same operator gives
      (K.q.q) e^{iq.y} R F + c i (K q lam)^c e^{iq.y} d_c F, with the number c printed; K = eta on the Lorentz locus.
 B  Q_a = u_a^c (k_c + (1 - Lam)_c^d p_d) has Q.Q = (k + (1-Lam)p).(k + (1-Lam)p) for Lorentz u, Lam, at exact points.
 C  Finite matrices: if C commutes with every X_a, then
      E_b[A] = [X^a,[X_a,A_b]] - [X^a,[X_b,A_a]] + [A^a,[X_a,X_b]]
    obeys E_b[(1/2){f,C}] = (1/2){E_b[f],C} for every f.  Random X_a tensor 1, C = 1 tensor c, f random.
 D  Group case: the left-invariant fields E_a4 and the right-invariant fields on GL(5) coordinates g^A_B have zero
    Lie bracket, sampled generators, exact.
Symbolic output is a check; the argument is in proposal-r1.md."""
import random
import numpy as np
import sympy as sp

d = 4
eta = [-1, 1, 1, 1]
y = sp.symbols('y0:4', real=True)
u = [[sp.Symbol('u%d_%d' % (a, b)) for b in range(d)] for a in range(d)]
ylow = [eta[g] * y[g] for g in range(d)]
q = [sp.Integer(1), sp.Integer(2), sp.Rational(-1, 3), sp.Integer(2)]   # lower index, not null
q2 = sum(eta[a] * q[a] * q[a] for a in range(d))
assert q2 != 0
pairs = [(c, f) for c in range(d) for f in range(c + 1, d)]
phase = sp.exp(sp.I * sum(q[a] * y[a] for a in range(d)))


def X(a, F):
    return sp.I * sum(u[a][b] * sp.diff(F, y[b]) for b in range(d))


def lam_pair(c0, f0):
    l = [[sp.S.Zero] * d for _ in range(d)]
    l[c0][f0] = sp.S.One
    l[f0][c0] = -sp.S.One
    return l


def Rfib(l, F):
    lm = [[eta[c] * l[c][b] for b in range(d)] for c in range(d)]
    return -sum(sum(u[a][c] * lm[c][b] for c in range(d)) * sp.diff(F, u[a][b]) for a in range(d) for b in range(d))


def Jop(l, F):
    return Rfib(l, F) - sum(ylow[g] * l[g][c] * sp.diff(F, y[c]) for g in range(d) for c in range(d))


def box(O, F):
    """[X^a,[X_a,O]] F"""
    def inner(G, a):
        return X(a, O(G)) - O(X(a, G))
    out = sp.S.Zero
    for a in range(d):
        out += eta[a] * (X(a, inner(F, a)) - inner(X(a, F), a))
    return out


# u is a general coordinate matrix here, so q^2 is replaced by K^{ef} q_e q_f with K^{ef} = eta^{ab} u_a^e u_b^f,
# which equals q^2 on the Lorentz locus; the operators are derivations, so nothing else uses the locus.
Kuu = [[sum(eta[a] * u[a][e] * u[a][f] for a in range(d)) for f in range(d)] for e in range(d)]
qKq = sum(Kuu[e][f] * q[e] * q[f] for e in range(d) for f in range(d))
rng = random.Random(51)
F = sum(sp.Rational(rng.randint(-5, 5), rng.randint(1, 3)) * y[rng.randrange(d)] * y[rng.randrange(d)]
        * u[rng.randrange(d)][rng.randrange(d)] * u[rng.randrange(d)][rng.randrange(d)] for _ in range(4)) + y[0] * y[1] * y[2] * u[0][1]
fails = 0
coef = set()
for (c0, f0) in pairs[:3]:
    l = lam_pair(c0, f0)
    lm = [[eta[c] * l[c][b] for b in range(d)] for c in range(d)]
    OJ = lambda G: phase * Jop(l, G)
    OR = lambda G: phase * Rfib(l, G)
    if sp.expand(sp.simplify((box(OJ, F) - qKq * phase * Jop(l, F)) / phase)) != 0:
        fails += 1
    # (K q lam)^c = K^{ef} q_e lam_f^c, which is q_g lam^{gc} on the Lorentz locus
    Kql = [sum(Kuu[e][f] * q[e] * lm[f][c] for e in range(d) for f in range(d)) for c in range(d)]
    base = sum(Kql[c] * sp.diff(F, y[c]) for c in range(d))
    rem = sp.expand(sp.simplify((box(OR, F) - qKq * phase * Rfib(l, F)) / phase))
    ok = False
    for cand in (2, -2):
        if sp.expand(rem - cand * sp.I * base) == 0:
            coef.add(cand)
            ok = True
    if not ok:
        fails += 1
print('A  box(e^{iqy} J) = (K.q.q) e^{iqy} J and box(e^{iqy} R) = (K.q.q) e^{iqy} R + c i (K q lam)^c e^{iqy} d_c, three generators: failures', fails, '; c =', coef)
assert fails == 0 and len(coef) == 1

Fr = sp.Rational
E = sp.diag(*eta)


def boost(a, b, t):
    m = sp.eye(d)
    ch, sh = (1 + t * t) / (1 - t * t), 2 * t / (1 - t * t)
    m[a, a] = ch; m[b, b] = ch; m[a, b] = sh; m[b, a] = sh
    return m


def rot(a, b, t):
    m = sp.eye(d)
    c, s = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    m[a, a] = c; m[b, b] = c; m[a, b] = -s; m[b, a] = s
    return m


U = boost(0, 1, Fr(1, 3)) * rot(1, 2, Fr(2, 5)) * boost(0, 3, Fr(1, 4))
L = rot(2, 3, Fr(1, 7)) * boost(0, 2, Fr(1, 5))
assert U * E * U.T == E and L * E * L.T == E
p = sp.Matrix([3, Fr(1, 2), -2, 5])
k = sp.Matrix([1, 1, 0, 0])
vec = k + (sp.eye(d) - L) * p
Qv = U * vec
print('B  Q.Q - (k + (1-Lam)p)^2 at an exact point:', (Qv.T * E * Qv)[0] - (vec.T * E * vec)[0])
assert (Qv.T * E * Qv)[0] == (vec.T * E * vec)[0]

np.random.seed(51)
n, m, D = 4, 3, 4
etaN = np.diag([-1.0, 1, 1, 1])


def herm(s):
    a = np.random.randn(s, s) + 1j * np.random.randn(s, s)
    return (a + a.conj().T) / 2


Xs = [np.kron(herm(n), np.eye(m)) for _ in range(D)]
c = np.kron(np.eye(n), herm(m))


def comm(A, B):
    return A @ B - B @ A


def acomm(A, B):
    return A @ B + B @ A


fs = [herm(n * m) for _ in range(D)]


def Elin(A):
    out = []
    for b in range(D):
        v = np.zeros_like(A[0])
        for a in range(D):
            v = v + etaN[a, a] * (comm(Xs[a], comm(Xs[a], A[b])) - comm(Xs[a], comm(Xs[b], A[a])) + comm(A[a], comm(Xs[a], Xs[b])))
        out.append(v)
    return out


L1 = Elin([acomm(f, c) / 2 for f in fs])
L2 = [acomm(x, c) / 2 for x in Elin(fs)]
res = max(np.abs(a - b).max() for a, b in zip(L1, L2))
print('C  max |E[(1/2){f,C}] - (1/2){E[f],C}| = %.2e (floating point)' % res)
assert res < 1e-9

D5 = 5
eta5 = [-1, 1, 1, 1, 1]
g = [[sp.Symbol('g%d_%d' % (A, B)) for B in range(D5)] for A in range(D5)]
coords = [g[A][B] for A in range(D5) for B in range(D5)]


def gen(A, B):
    M = sp.zeros(D5, D5)
    M[A, B] += eta5[B]
    M[B, A] -= eta5[A]
    return M


G = sp.Matrix(D5, D5, lambda i, j: g[i][j])


def left(A, B):
    W = G * gen(A, B)
    return {g[i][j]: W[i, j] for i in range(D5) for j in range(D5)}


def right(A, B):
    W = gen(A, B) * G
    return {g[i][j]: W[i, j] for i in range(D5) for j in range(D5)}


def lie(P, Q_):
    return [sp.expand(sum(P[z] * sp.diff(Q_[x], z) - Q_[z] * sp.diff(P[x], z) for z in coords)) for x in coords]


fails = 0
for a in range(4):
    for (A, B) in [(0, 1), (0, 4), (2, 3), (3, 4)]:
        fails += sum(1 for v in lie(left(a, 4), right(A, B)) if v != 0)
print('D  [left E_a4, right E_AB] = 0 on sampled generators: failures', fails)
assert fails == 0
# E: de Sitter class.  D_a = left-invariant field of E_a4 on coordinates g^A_B; polynomial computation, evaluated on an exact
# SO(4,1) element.  f_b = g^A_b a_A(Y), Y^A = g^A_4, a dressed one-form.  Hand result: [D_a,D_b] f^a = 3 f_b on the group, so the
# linearised operator with the bilinear term has no non-derivative term, and for f_b = D_b Lam the curl vanishes.
def Dleft(a, F):
    W = left(a, 4)
    return sum(W[z] * sp.diff(F, z) for z in coords)
eta4_ = eta5[:4]
Y = [g[A][4] for A in range(D5)]
aA = [Y[1] * Y[2], Y[0] ** 2, Y[3], Y[0] * Y[3], Y[4] * Y[1]]
fb = [sum(g[A][b] * aA[A] for A in range(D5)) for b in range(4)]
fup = [eta4_[b] * fb[b] for b in range(4)]
def bfive(a, b, t):
    m = sp.eye(D5); ch, sh = (1 + t * t) / (1 - t * t), 2 * t / (1 - t * t)
    m[a, a] = ch; m[b, b] = ch; m[a, b] = sh; m[b, a] = sh
    return m
def rfive(a, b, t):
    m = sp.eye(D5); c_, s_ = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    m[a, a] = c_; m[b, b] = c_; m[a, b] = -s_; m[b, a] = s_
    return m
g0 = bfive(0, 1, Fr(1, 3)) * rfive(1, 2, Fr(2, 5)) * rfive(3, 4, Fr(1, 2)) * bfive(0, 4, Fr(1, 5)) * rfive(2, 4, Fr(3, 7))
E5 = sp.diag(*eta5)
assert g0 * E5 * g0.T == E5 and g0.T * E5 * g0 == E5
sub = {g[A][B]: g0[A, B] for A in range(D5) for B in range(D5)}
ratios = []
for b in range(4):
    val = sum(Dleft(a, Dleft(b, fup[a])) - Dleft(b, Dleft(a, fup[a])) for a in range(4))
    v = sp.nsimplify(val.subs(sub))
    w_ = sp.nsimplify(fb[b].subs(sub))
    ratios.append((v, w_))
print('E  [D_a,D_b] f^a versus f_b at an exact SO(4,1) point: ratios', [sp.nsimplify(v / w_) if w_ != 0 else None for v, w_ in ratios])
assert len({sp.nsimplify(v / w_) for v, w_ in ratios if w_ != 0}) == 1
# background equation: [D^a,[D_a,D_b]] = c D_b on functions, c read off on a test function
test = Y[1] * Y[2] + Y[0]
for b in range(2):
    lhs = sum(eta4_[a] * (Dleft(a, Dleft(a, Dleft(b, test)) - Dleft(b, Dleft(a, test))) - (Dleft(a, Dleft(b, Dleft(a, test))) - Dleft(b, Dleft(a, Dleft(a, test))))) for a in range(4))
    rhs = Dleft(b, test)
    print('   [D^a,[D_a,D_b]] / D_b on a test function, b = %d:' % b, sp.nsimplify((lhs / rhs).subs(sub)))
print('ALL ASSERTIONS PASSED')
