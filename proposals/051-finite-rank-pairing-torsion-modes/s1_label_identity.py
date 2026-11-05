"""051 s1: the first-order class about flat space in commutant labels. Exact symbolic identities, d = 4.

Conventions are those of 050 s3:
   D_a -> D_a - h_a^c D_c + (1/2) w_a^{cd} S_cd,
   T_ab^c = d_a h_b^c - d_b h_a^c + w_b^c_a - w_a^c_b,  w_b^c_a = w_b^{cf} eta_fa,
   R_ab^{cd} = d_a w_b^{cd} - d_b w_a^{cd},
   E1_b^e = - d^a T_ab^e + R_ab^{ae},  E2_b^{de} = d^a R_ab^{de},  E3_b = d^a(d_a tau_b - d_b tau_a),  tau_a = (1/2) T_ac^c.

Change of variables with arbitrary functions fP_b^c(y) and fJ_b^{cd}(y) = - fJ_b^{dc}(y):
   h_b^c = fP_b^c + y_g fJ_b^{gc},    w_b^{cd} = fJ_b^{cd}.
Checks, for arbitrary functions:
   A  T_ab^c = FP_ab^c + y_g FJ_ab^{gc}, R_ab^{cd} = FJ_ab^{cd}, F = d_a f_b - d_b f_a.
   B  E2_b^{de} = Mx[fJ^{de}]_b and E1_b^e + y_g E2_b^{ge} = - Mx[fP^e]_b, Mx[f]_b = d^a(d_a f_b - d_b f_a).
   C  E3_b is a combination of the Maxwell expressions and their first derivatives (explicit formula, residual 0).
   D  vector fields: D_a = u_a^b d/dy^b and V = - u_a^c lam_c^b d/du_a^b - y_g lam^{gc} d/dy^c have zero Lie bracket.
   E  the plane-wave solutions: on e^{iq.y}, eps.q = 0, q^2 = 0, the J-label mode has y-linear h and solves E1,E2,E3.
   F  counts at null q: for a transverse pair eps, lam -> q.lam has rank 3, so 6 chains; labels 2 x 11 = 22 = 20 + 2.
Symbolic output is a check; the argument is in proposal-r1.md."""
import itertools, sys
import sympy as sp

d = 4
eta = [-1, 1, 1, 1]
y_up = sp.symbols('y0:4', real=True)
pairs = [(c, f) for c in range(d) for f in range(c + 1, d)]

fP = [[sp.Function('P_%d_%d' % (b, c))(*y_up) for c in range(d)] for b in range(d)]
fJ = [[[sp.S.Zero] * d for _ in range(d)] for _ in range(d)]
for b in range(d):
    for (c, f) in pairs:
        g = sp.Function('J_%d_%d%d' % (b, c, f))(*y_up)
        fJ[b][c][f] = g
        fJ[b][f][c] = -g

ylow = [eta[g] * y_up[g] for g in range(d)]
dl = lambda a, x: sp.diff(x, y_up[a])              # d_a = d/dy^a, lower index
du = lambda a, x: eta[a] * sp.diff(x, y_up[a])     # d^a


def fields(fP_, fJ_):
    h = [[fP_[b][c] + sum(ylow[g] * fJ_[b][g][c] for g in range(d)) for c in range(d)] for b in range(d)]
    return h, fJ_


def torsion(h, w):
    return [[[dl(a, h[b][c]) - dl(b, h[a][c]) + w[b][c][a] * eta[a] - w[a][c][b] * eta[b] for c in range(d)]
             for b in range(d)] for a in range(d)]


def curvature(w):
    return [[[[dl(a, w[b][c][f]) - dl(b, w[a][c][f]) for f in range(d)] for c in range(d)]
             for b in range(d)] for a in range(d)]


def E12(h, w):
    T = torsion(h, w)
    R = curvature(w)
    E1 = [[-sum(du(a, T[a][b][e]) for a in range(d)) + sum(R[a][b][a][e] for a in range(d)) for e in range(d)] for b in range(d)]
    E2 = [[[sum(du(a, R[a][b][c][f]) for a in range(d)) for f in range(d)] for c in range(d)] for b in range(d)]
    return T, R, E1, E2


def E3(T):
    tau = [sp.Rational(1, 2) * sum(T[a][c][c] for c in range(d)) for a in range(d)]
    return tau, [sum(du(a, dl(a, tau[b]) - dl(b, tau[a])) for a in range(d)) for b in range(d)]


def maxwell(f):
    return [sum(du(a, dl(a, f[b]) - dl(b, f[a])) for a in range(d)) for b in range(d)]


h, w = fields(fP, fJ)
T, R, E1, E2 = E12(h, w)
res = 0
for a, b, c in itertools.product(range(d), repeat=3):
    FP = dl(a, fP[b][c]) - dl(b, fP[a][c])
    yF = sum(ylow[g] * (dl(a, fJ[b][g][c]) - dl(b, fJ[a][g][c])) for g in range(d))
    res += abs(sp.expand(T[a][b][c] - FP - yF) != 0)
print('A  T = FP + y FJ on all components: failures', res)
assert res == 0
res = 0
for b in range(d):
    for e in range(d):
        mxP = maxwell([fP[x][e] for x in range(d)])[b]
        if sp.expand(E1[b][e] + sum(ylow[g] * E2[b][g][e] for g in range(d)) + mxP) != 0:
            res += 1
    for (c, f) in pairs:
        if sp.expand(E2[b][c][f] - maxwell([fJ[x][c][f] for x in range(d)])[b]) != 0:
            res += 1
print('B  E2 = Mx[fJ], E1 + y_g E2^{g e} = - Mx[fP]: failures', res)
assert res == 0

# C: 2 E3_b = d_c E1_b^c - eta_bg E2_c^{gc}, identically in (h, w).  Hand derivation in proposal-r1.md, Section 3.
tau, e3 = E3(T)
res = 0
for b in range(d):
    rhs = sum(dl(c, E1[b][c]) for c in range(d)) - eta[b] * sum(E2[c][b][c] for c in range(d))
    if sp.expand(2 * e3[b] - rhs) != 0:
        res += 1
print('C  2 E3_b = d_c E1_b^c - eta_bg E2_c^{gc}: failures', res)
assert res == 0

# D: Lie bracket of vector fields on (y, u) with u a general 4 x 4 matrix of coordinates.
u = [[sp.Symbol('u%d_%d' % (a, b)) for b in range(d)] for a in range(d)]
lam_up = [[sp.S.Zero] * d for _ in range(d)]
for n, (c, f) in enumerate(pairs):
    v = sp.Symbol('l%d%d' % (c, f))
    lam_up[c][f] = v
    lam_up[f][c] = -v
lam_mixed = [[eta[c] * lam_up[c][b] for b in range(d)] for c in range(d)]   # lam_c^b = eta_cf lam^{fb}
coords = list(y_up) + [u[a][b] for a in range(d) for b in range(d)]


def D_field(a):
    out = {x: sp.S.Zero for x in coords}
    for b in range(d):
        out[y_up[b]] = u[a][b]
    return out


V = {x: sp.S.Zero for x in coords}
for a in range(d):
    for b in range(d):
        V[u[a][b]] = -sum(u[a][c] * lam_mixed[c][b] for c in range(d))
for c in range(d):
    V[y_up[c]] = -sum(ylow[g] * lam_up[g][c] for g in range(d))


def bracket(A, B):
    return {x: sp.expand(sum(A[z] * sp.diff(B[x], z) - B[z] * sp.diff(A[x], z) for z in coords)) for x in coords}


fails = 0
for a in range(d):
    br = bracket(V, D_field(a))
    fails += sum(1 for x in coords if br[x] != 0)
print('D  [V, D_a] = 0 on all components, all a: failures', fails)
assert fails == 0

# E: plane-wave J-label modes, at a null q with rational components, every transverse eps and lam in a basis.
q_low = [sp.Integer(-5), sp.Integer(3), sp.Integer(4), sp.Integer(0)]
q_up = [eta[a] * q_low[a] for a in range(d)]
assert sum(q_low[a] * q_up[a] for a in range(d)) == 0
phase = sp.exp(sp.I * sum(q_low[a] * y_up[a] for a in range(d)))
epss = [[sp.S.Zero, sp.S.Zero, sp.S.Zero, sp.S.One], [sp.S.Zero, sp.Integer(4), sp.Integer(-3), sp.S.Zero]]   # eps_a lower
for e_ in epss:
    assert sum(e_[a] * q_up[a] for a in range(d)) == 0
fails = 0
for e_ in epss:
    for (c0, f0) in pairs:
        l_up = [[sp.S.Zero] * d for _ in range(d)]
        l_up[c0][f0] = sp.S.One
        l_up[f0][c0] = -sp.S.One
        fPz = [[sp.S.Zero] * d for _ in range(d)]
        fJz = [[[e_[b] * l_up[c][f] * phase for f in range(d)] for c in range(d)] for b in range(d)]
        hz, wz = fields(fPz, fJz)
        Tz, Rz, E1z, E2z = E12(hz, wz)
        _, E3z = E3(Tz)
        all_e = [x for r in E1z for x in r] + [x for r in E2z for r2 in r for x in r2] + list(E3z)
        fails += sum(1 for x in all_e if sp.simplify(x) != 0)
print('E  y-linear J-label modes solve E1, E2, E3 at null q with eps.q = 0: failures', fails)
assert fails == 0

# F: counts at null q.
M = sp.zeros(d, len(pairs))
for n, (c0, f0) in enumerate(pairs):
    # (q.lam)^c = q_g lam^{gc}
    for c in range(d):
        v = sp.S.Zero
        if c == f0:
            v += q_low[c0]
        if c == c0:
            v -= q_low[f0]
        M[c, n] = v
r = M.rank()
print('F  rank of lam -> q.lam at null q:', r, '; kernel', len(pairs) - r, '; image inside q-perp:',
      all(sum(q_low[c] * M[c, n] for c in range(d)) == 0 for n in range(len(pairs))))
assert r == 3
print('   two transverse polarisations: J-label modes with q.lam != 0 (partners of chains):', 2 * r,
      '; J-label modes with q.lam = 0:', 2 * (len(pairs) - r), '; P-label modes:', 2 * d)
print('   fixed-q eigenmodes:', 2 * d + 2 * (len(pairs) - r), '(8 simple + 6 eigenvectors of chains); with the 6 partners:',
      2 * d + 2 * (len(pairs) - r) + 2 * r)
print('   labels 1 + 4 + 6 = 11, physical polarisations 22 = 20 + 2 (the label 1 is the order-zero Maxwell field)')
# G: the fibre part of V is (1/2) lam^{cd} u^e_c u^f_d S_ef, at an exact Lorentz point, with S_ef of 050:
#    (S_ef u)_a^b = eta_af u_e^b - eta_ae u_f^b, u^e_c = eta^{eh} u_h^g eta_gc.
Fr = sp.Rational
def _boost(a, b, t):
    m = sp.eye(d); ch, sh = (1 + t * t) / (1 - t * t), 2 * t / (1 - t * t)
    m[a, a] = ch; m[b, b] = ch; m[a, b] = sh; m[b, a] = sh
    return m
def _rot(a, b, t):
    m = sp.eye(d); c, s_ = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    m[a, a] = c; m[b, b] = c; m[a, b] = -s_; m[b, a] = s_
    return m
U0 = _boost(0, 1, Fr(1, 3)) * _rot(1, 2, Fr(2, 5)) * _boost(0, 3, Fr(1, 4))
E0 = sp.diag(*eta)
assert U0 * E0 * U0.T == E0
Uup = E0 * U0 * E0    # u^e_c
fails = 0
for (c0, f0) in pairs:
    l = [[sp.S.Zero] * d for _ in range(d)]
    l[c0][f0] = sp.S.One
    l[f0][c0] = -sp.S.One
    for a in range(d):
        for b in range(d):
            lhs = sum(sp.Rational(1, 2) * l[c][dd] * Uup[e, c] * Uup[f, dd] * (eta[a] * (a == f) * U0[e, b] - eta[a] * (a == e) * U0[f, b])
                      for c in range(d) for dd in range(d) for e in range(d) for f in range(d))
            rhs = -sum(U0[a, c] * eta[c] * l[c][b] for c in range(d))
            if sp.nsimplify(lhs - rhs) != 0:
                fails += 1
print('G  (1/2) lam^{cd} u^e_c u^f_d (S_ef u)_a^b = - u_a^c lam_c^b at an exact Lorentz point: failures', fails)
assert fails == 0
print('ALL ASSERTIONS PASSED')
