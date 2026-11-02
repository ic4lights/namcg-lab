"""
s2b: the order-zero part of the matrix equation, exact on jets, d = 3.
Order-zero functions are carried by an extra coordinate th: DD_a = D_a + W_a d/dth, W_a = u_a^b What_b(y) (equivariant).
With [DD_a,DD_b] = -T_ab^c DD_c + (1/2) R S + Phi_ab d/dth, checks that the d/dth coefficient of [DD^a,[DD_a,DD_b]], in the basis (DD_e, S, d/dth), is
    DD^a Phi_ab - T_ab^c Phi^a_c ,
and that the D_e and S coefficients are those of s2 (unchanged by W).
"""
import random
import sympy as sp
from sympy import QQ, ring
d = 3
random.seed(7)
names = ['y%d' % i for i in range(d)] + ['u%d_%d' % (a, b) for a in range(d) for b in range(d)] + ['th']
Rg, *gens = ring(names, QQ)
M = sp.eye(d); c, s_ = sp.Rational(5, 4), sp.Rational(3, 4); M[0, 0] = c; M[1, 1] = c; M[0, 1] = s_; M[1, 0] = s_
ORDER = 2
y = [gens[i] + QQ(i+1, 7) for i in range(d)]
u = [[gens[d+d*a+b] + QQ(int(M[a, b].p), int(M[a, b].q)) for b in range(d)] for a in range(d)]
N = len(gens); TH = N-1
eta = [-1, 1, 1]
uidx = lambda a, b: d+d*a+b
def tr(p):
    return Rg.from_dict({m: v for m, v in p.terms() if sum(m) <= ORDER})
rr = lambda: QQ(random.randint(-3, 3), random.randint(1, 4))
linear = lambda: Rg(rr()) + sum(y[i]*rr() for i in range(d))
quad = lambda: tr(linear() + sum(y[i]*y[j]*rr() for i in range(d) for j in range(d)))
e = [[Rg(1) if i == j else (quad() if j > i else Rg(0)) for j in range(d)] for i in range(d)]
th = [[Rg(0) for _ in range(d)] for _ in range(d)]
for i in reversed(range(d)):
    for j in range(d):
        th[i][j] = (Rg(1) if i == j else Rg(0)) - sum((tr(e[i][k]*th[k][j]) for k in range(i+1, d)), Rg(0))
w = []
for mu in range(d):
    m = [[Rg(0) for _ in range(d)] for _ in range(d)]
    for c_ in range(d):
        for f in range(c_+1, d):
            val = linear(); m[c_][f] = val*eta[c_]; m[f][c_] = -val*eta[f]
    w.append(m)
What = [quad() for _ in range(d)]
Uinv = [[u[b][a]*(eta[a]*eta[b]) for b in range(d)] for a in range(d)]
def apply(V, f):
    out = Rg(0)
    for k in range(N):
        if V[k] != 0:
            out += tr(V[k]*f.diff(gens[k]))
    return out
def comm(V, W_):
    return [apply(V, W_[k]) - apply(W_, V[k]) for k in range(N)]
D = []
W = [tr(sum((u[a][b]*What[b] for b in range(d)), Rg(0))) for a in range(d)]
for a in range(d):
    V = [Rg(0)]*N
    for mu in range(d):
        co = tr(sum((u[a][b]*e[b][mu] for b in range(d)), Rg(0)))
        V[mu] = co
        for f in range(d):
            for c_ in range(d):
                t = tr(sum((u[f][g]*w[mu][c_][g] for g in range(d)), Rg(0)))
                V[uidx(f, c_)] = tr(V[uidx(f, c_)] - co*t)
    V[TH] = W[a]
    D.append(V)
def coeffs(V):
    alpha = [Rg(0)]*d
    for a in range(d):
        alpha[a] = sum((tr(tr(V[mu]*th[mu][b])*Uinv[b][a]) for mu in range(d) for b in range(d)), Rg(0))
    dV = [[V[uidx(a, b)] - sum((tr(alpha[c_]*D[c_][uidx(a, b)]) for c_ in range(d)), Rg(0)) for b in range(d)] for a in range(d)]
    beta = [[sum((tr(dV[g][b]*Uinv[b][f]) for b in range(d)), Rg(0))*eta[g] for g in range(d)] for f in range(d)]
    zero = V[TH] - sum((tr(alpha[c_]*W[c_]) for c_ in range(d)), Rg(0))
    return alpha, beta, zero
Fab, Tc, Rc, Ph = {}, {}, {}, {}
for a in range(d):
    for b in range(a+1, d):
        F = comm(D[a], D[b]); Fab[(a, b)] = F
        al, be, ze = coeffs(F)
        Tc[(a, b)] = [-v for v in al]; Rc[(a, b)] = be; Ph[(a, b)] = ze
def F(a, b):
    if a == b: return [Rg(0)]*N
    return Fab[(a, b)] if a < b else [-v for v in Fab[(b, a)]]
T = lambda a, b, c_: Rg(0) if a == b else (Tc[(a, b)][c_] if a < b else -Tc[(b, a)][c_])
P = lambda a, b: Rg(0) if a == b else (Ph[(a, b)] if a < b else -Ph[(b, a)])
R = lambda a, b, f, g: Rg(0) if a == b else (Rc[(a, b)][f][g] if a < b else -Rc[(b, a)][f][g])
ev = lambda p: p.coeff(1) if p != 0 else QQ(0)
ok0 = okD = True; mx = 0
for b in range(d):
    V = [Rg(0)]*N
    for a in range(d):
        cc = comm(D[a], F(a, b))
        V = [V[k] + cc[k]*eta[a] for k in range(N)]
    al, be, ze = coeffs(V)
    rhs = Rg(0)
    for a in range(d):
        rhs += apply(D[a], P(a, b))*eta[a]
        for c_ in range(d):
            rhs += -tr(T(a, b, c_)*P(a, c_))*eta[a]
    mx = max(mx, abs(ev(ze)))
    ok0 &= ev(ze) == ev(rhs)
    for g in range(d):
        r2 = Rg(0)
        for a in range(d):
            r2 += -apply(D[a], T(a, b, g))*eta[a]
            for c_ in range(d):
                r2 += tr(T(a, b, c_)*T(a, c_, g))*eta[a]
            r2 += R(a, b, a, g)
        okD &= ev(al[g]) == ev(r2)
print(f'order-zero formula DD^a Phi_ab - T_ab^c Phi^a_c: {ok0}; D-part formula with W present: {okD}; max |order-zero coefficient| {float(mx):.4g}')
