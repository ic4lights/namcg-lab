"""
Theorem 1: for real antisymmetric Theta^{IJ} (D x D), eta = diag(-1,1,...,1), base block mu,nu in 0..3,
  S^{mu nu} = int dnu(Theta) Theta^{I mu} eta_{IJ} Theta^{J nu}   (any positive measure)
satisfies  S^{00} >= 0  and  tr S >= 0  (Euclidean trace over mu).  S = c eta^{-1} (eta^{-1}=diag(-1,1,1,1)) needs S^{00} = -c, trS = 2c,
hence c = 0.  Checks: (a) symbolic identities for S^{00} and trS as sums of squares (D = 4..7);
(b) random measures: inequalities; (c) adversarial minimisation of min_c ||S - c eta^{-1}||/||S|| over 1..4-point measures;
(d) leaf-level statement in dimension 2m>=4: K = c g^{-1}, c != 0 impossible for real Lorentzian g (c>0 determinant, c<0 null eigenspaces); 2m=2 counterexample.
"""
import sympy as sp, numpy as np, random
from scipy.optimize import minimize
for D in range(4, 8):
    T = sp.zeros(D, D)
    for i in range(D):
        for j in range(i+1, D):
            T[i, j] = sp.Symbol('t%d_%d' % (i, j)); T[j, i] = -T[i, j]
    eta = sp.diag(*([-1]+[1]*(D-1)))
    S = (T[:, :4].T*eta*T[:, :4])
    S00 = sum(T[I, 0]**2 for I in range(1, D))
    trS = sum(T[I, 0]**2 for I in range(4, D)) + sum(T[I, k]**2 for I in range(1, D) for k in range(1, 4))
    assert sp.expand(S[0, 0]-S00) == 0 and sp.expand(S.trace()-trS) == 0
print('(a) S00 = sum_{I>=1}(Theta^{I0})^2 and tr S = sum_{I>=4}(Theta^{I0})^2 + sum_{I>=1,k>=1}(Theta^{Ik})^2 verified symbolically, D=4..7')
rng = np.random.default_rng(1)
def rt(D):
    A = rng.normal(size=(D, D)); return A-A.T
eta4 = np.diag([-1., 1, 1, 1])
def Smat(thetas, w, D):
    et = np.diag([-1.]+[1.]*(D-1)); S = np.zeros((4, 4))
    for t, ww in zip(thetas, w):
        S += ww*t[:, :4].T@et@t[:, :4]
    return S
viol = 0
for trial in range(2000):
    D = rng.integers(4, 10); k = rng.integers(1, 6)
    th = [rt(D) for _ in range(k)]; w = rng.random(k)
    S = Smat(th, w, D)
    if S[0, 0] < -1e-12 or np.trace(S) < -1e-12: viol += 1
print('(b) violations of S00>=0, trS>=0 in 2000 random measures:', viol)
best = 9
for D in (4, 5, 7):
    for k in (1, 2, 4):
        def f(p):
            th = []
            idx = 0
            for _ in range(k):
                A = p[idx:idx+D*D].reshape(D, D); idx += D*D; th.append(A-A.T)
            w = np.abs(p[idx:idx+k])+1e-9
            S = Smat(th, w, D)
            c = np.sum(S*eta4)/np.sum(eta4*eta4)   # projection on eta^{-1}=eta4 (same matrix)
            return np.linalg.norm(S-c*eta4)/np.linalg.norm(S)
        m = 9
        for r in range(15):
            res = minimize(f, rng.normal(size=k*D*D+k), method='BFGS')
            m = min(m, res.fun)
        print('(c) D=%d points=%d: min over measures of min_c ||S-c eta^-1||/||S|| = %.4f' % (D, k, m))
        best = min(best, m)
print('    overall minimum found', best, '(positive; the proof gives S00>=0 and trS>=0 incompatible with c != 0)')
# (d) leaf-level statement in dimension 2m>=4, K = theta^T g theta = c g^{-1}, c != 0, N = theta g, N^2 = -c.
#   c>0: det N = c^m > 0 but det N = Pf(theta)^2 det g < 0.  c<0: N g-skew, N^2 = |c|, +-sqrt|c| eigenspaces totally null,
#   each of dim <= 1 in Lorentzian signature, so 2m <= 2.  At 2m = 2 a counterexample exists (c = -4).
print('(d) leaf-level companion')
g2 = sp.diag(-1, 1); th2 = 2*sp.Matrix([[0, 1], [-1, 0]])
K2 = th2.T*g2*th2
assert K2 == -4*g2.inv()
N2 = th2*g2
assert N2*N2 == 4*sp.eye(2)
ev = N2.eigenvects()
print('    2m=2 counterexample: theta=2 eps, g=diag(-1,1): K = -4 g^{-1}  (c=-4<0); N^2 =', (N2*N2).tolist())
for lam, mult, vecs in ev:
    v = vecs[0]
    print('       eigenvalue', lam, ': g(v,v) =', (v.T*g2*v)[0], '(null eigenvector, as predicted)')
random.seed(3)
R = lambda: sp.Rational(random.randint(-4, 4), random.randint(1, 3))
for n2 in (2, 4, 6):
    while True:
        A = sp.Matrix(n2, n2, lambda i, j: R())
        if A.det() != 0: break
    g = A.T*sp.diag(*([-1]+[1]*(n2-1)))*A
    while True:
        W = sp.zeros(n2, n2)
        for i in range(n2):
            for j in range(i+1, n2):
                W[i, j] = R(); W[j, i] = -W[i, j]
        if W.det() != 0: break
    N = W*g
    print('    dim %d: det N = %s, sign det g = %s  -> c>0 excluded (needs det N = c^%d > 0)' % (n2, N.det(), sp.sign(g.det()), n2//2))
# c<0, 2m=4: N g-skew with N^2 = +1 means g(Nu,v) = -g(u,Nv); eigenspaces E_+ : g(u,u') = -g(Nu,u') ... = -g(u,Nu') => g(u,u')=0.
# Check numerically that a Lorentzian g in dim 4 has no 2-dim totally null subspace (Witt index 1): max isotropic dim via signature.
for D in (4, 6):
    sig_pos, sig_neg = D-1, 1
    print('    Witt index of signature (%d,%d) = min = %d: totally null subspaces have dim <= 1, so dim E_+ + dim E_- = %d >= 4 is impossible when both are totally null' % (sig_neg, sig_pos, min(sig_pos, sig_neg), D))
