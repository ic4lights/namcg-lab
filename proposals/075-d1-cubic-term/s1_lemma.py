"""075 s1: the cubic term of eq:Smatrix on finite Hermitian matrices, and the rigidity lemma.

Action (g = 1):  S = -1/4 Tr([X^m,X^n][X_m,X_n]) + 1/6 Tr(C_{mnl}[X^m,X^n]X^l),  X_m = eta_mn X^n,
eta = diag(-1,1,1,1), eps^{0123} = +1 (so eps_{0123} = -1).
Checks:
 (a) only the totally antisymmetric part of C contributes (random complex C, random Hermitian X);
 (b) for C = i c eps_{mnls} v^s the action is real, and dS = Tr(dX^l G_l) with
     G_l = [X^n,[X_n,X_l]] + (i c/2) eps_{lmns} v^s [X^m,X^n]      (finite differences);
 (c) the fuzzy-sphere normalisation of appH (C_ijk = i c3 eps_ijk, 3 Euclidean directions): X = chi J, chi = c3/2;
 (d) covariance: for Lambda in SO+(3,1), G_l[Lambda X; v] = Lambda_l^l' G_l'[X; Lambda^{-1} v];
 (e) span{Lambda v - v : Lambda in SO+(3,1)} = R^4 for timelike, spacelike and null v;
 (f) the map F^{cd} -> eps_{bcdf} F^{cd} (antisymmetric F, all b,f) is injective (rank 6);
 (g) consequence on a non-commuting configuration: if G[X; v] = 0 and G[X; Lambda^-1 v] = 0 then
     eps_{lmns} w^s [X^m,X^n] = 0 for w = v - Lambda^{-1} v (identity, checked by subtraction)."""
import itertools
import numpy as np

rng = np.random.default_rng(75)
eta = np.diag([-1.0, 1, 1, 1])
eps = np.zeros((4, 4, 4, 4))
for p in itertools.permutations(range(4)):
    eps[p] = np.linalg.det(np.eye(4)[list(p)])
epsL = -eps                     # eps_{abcd}, eps_{0123} = -1


def herm(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (A + A.conj().T) / 2


def comm(A, B):
    return A @ B - B @ A


def lower(X):
    return [sum(eta[m, n] * X[n] for n in range(4)) for m in range(4)]


def action(X, C):
    XL = lower(X)
    s4 = sum(np.trace(comm(X[m], X[n]) @ comm(XL[m], XL[n])) for m in range(4) for n in range(4))
    s3 = sum(C[m, n, l] * np.trace(comm(X[m], X[n]) @ X[l])
             for m in range(4) for n in range(4) for l in range(4))
    return -s4 / 4 + s3 / 6


def G(X, c, v):
    XL = lower(X)
    out = []
    for l in range(4):
        t = sum(comm(X[n], comm(XL[n], XL[l])) for n in range(4))
        t = t + 0.5j * c * sum(epsL[l, m, n, s] * v[s] * comm(X[m], X[n])
                               for m in range(4) for n in range(4) for s in range(4))
        out.append(t)
    return out


def boost(i, th):
    L = np.eye(4); L[0, 0] = L[i, i] = np.cosh(th); L[0, i] = L[i, 0] = np.sinh(th); return L


def rot(i, j, th):
    L = np.eye(4); L[i, i] = L[j, j] = np.cos(th); L[i, j] = -np.sin(th); L[j, i] = np.sin(th); return L


def rand_lorentz():
    L = np.eye(4)
    for _ in range(4):
        L = L @ boost(int(rng.integers(1, 4)), rng.normal()) @ rot(*rng.choice([1, 2, 3], 2, replace=False), rng.normal())
    return L


n = 5
X = [herm(n) for _ in range(4)]
# (a)
Cr = rng.normal(size=(4, 4, 4)) + 1j * rng.normal(size=(4, 4, 4))
Ca = sum(np.sign(np.linalg.det(np.eye(3)[list(p)])) * Cr.transpose(p) for p in itertools.permutations(range(3))) / 6
d_a = abs(action(X, Cr) - action(X, Ca)) / abs(action(X, Cr))
print('(a) |S[C] - S[C_antisym]| / |S| =', f'{d_a:.1e}')
# (b)
c = 0.7; v = np.array([1.3, 0.2, -0.4, 0.5])
C = 1j * c * np.einsum('mnls,s->mnl', epsL, v)
S0 = action(X, C)
print('(b) Im S =', f'{abs(S0.imag):.1e}', '(real action for C = i c eps v, c, v real)')
dX = [herm(n) for _ in range(4)]
h = 1e-6
fd = (action([X[m] + h * dX[m] for m in range(4)], C) - action([X[m] - h * dX[m] for m in range(4)], C)) / (2 * h)
Gs = G(X, c, v)
an = sum(np.trace(dX[l] @ Gs[l]) for l in range(4))
print('    finite difference', f'{fd.real:.8f}', ' Tr(dX^l G_l)', f'{an.real:.8f}', ' rel.diff', f'{abs(fd - an) / abs(an):.1e}')
# (c) fuzzy sphere
for j2 in (1, 2, 3):
    jj = j2 / 2; m_ = np.arange(jj, -jj - 1, -1); dim = len(m_)
    Jp = np.zeros((dim, dim))
    for k in range(1, dim):
        Jp[k - 1, k] = np.sqrt(jj * (jj + 1) - m_[k] * (m_[k] + 1))
    J = [(Jp + Jp.T) / 2, (Jp - Jp.T) / 2j, np.diag(m_)]
    c3 = 1.1; chi = c3 / 2
    e3 = np.zeros((3, 3, 3))
    for p in itertools.permutations(range(3)):
        e3[p] = np.linalg.det(np.eye(3)[list(p)])
    Y = [chi * Ji for Ji in J]
    res = max(np.abs(sum(comm(Y[k], comm(Y[k], Y[i])) for k in range(3))
                     + 0.5j * c3 * sum(e3[i, k, l] * comm(Y[k], Y[l]) for k in range(3) for l in range(3))).max()
              for i in range(3))
    print(f'(c) fuzzy sphere j={jj}: residual of the 3d equation at chi = c3/2:', f'{res:.1e}')
# (d)
Lam = rand_lorentz()
print('    Lambda in SO+(3,1): |L^T eta L - eta| =', f'{np.abs(Lam.T @ eta @ Lam - eta).max():.1e}', ' det =', f'{np.linalg.det(Lam):.6f}', ' L00 =', f'{Lam[0,0]:.3f}')
XLam = [sum(Lam[m, k] * X[k] for k in range(4)) for m in range(4)]
lhs = G(XLam, c, v)
G2 = G(X, c, np.linalg.solve(Lam, v))
LamL = eta @ Lam @ np.linalg.inv(eta)          # Lambda_l^{l'} on lower indices
rhs = [sum(LamL[l, k] * G2[k] for k in range(4)) for l in range(4)]
print('(d) covariance residual', f'{max(np.abs(lhs[l] - rhs[l]).max() for l in range(4)):.1e}')
# (e)
for name, vv in (('timelike', np.array([1.0, 0, 0, 0])), ('spacelike', np.array([0, 0, 0, 1.0])),
                 ('null', np.array([1.0, 0, 0, 1.0])), ('generic', v)):
    W = np.array([vv - np.linalg.solve(rand_lorentz(), vv) for _ in range(12)])
    print(f'(e) {name:9s} v: rank span(v - Lambda^-1 v) =', np.linalg.matrix_rank(W, 1e-9))
# (f)
pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]
Mf = np.zeros((16, 6))
for k, (a, b) in enumerate(pairs):
    F = np.zeros((4, 4)); F[a, b] = 1; F[b, a] = -1
    Mf[:, k] = np.einsum('bcdf,cd->bf', epsL, F).reshape(16)
print('(f) rank of F -> eps_{bcdf}F^{cd}:', np.linalg.matrix_rank(Mf))
# (g)
w = v - np.linalg.solve(Lam, v)
diff = [Gs[l] - G2[l] for l in range(4)]
direct = [0.5j * c * sum(epsL[l, m, k, s] * w[s] * comm(X[m], X[k]) for m in range(4) for k in range(4) for s in range(4)) for l in range(4)]
print('(g) G[X;v] - G[X;Lambda^-1 v] - (ic/2) eps(w)[X,X] =', f'{max(np.abs(diff[l] - direct[l]).max() for l in range(4)):.1e}')
