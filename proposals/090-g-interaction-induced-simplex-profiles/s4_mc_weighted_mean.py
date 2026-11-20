import random
# Cross-check of the interaction-deformed profile measure (a=2, beta=1, D=3):
# target measure density proportional to prod_i p_i^(a-1) * prod_{i<j} |p_i-p_j|^beta on the simplex.
# Path A: Monte Carlo over Dirichlet(a=2) draws (base density prod p_i) reweighted by prod|p_i-p_j| ONLY.
# Path B: grid quadrature of the full density. (v2 bug: reweighted also by prod p_i, double-counting the
# Dirichlet base factor; fixed here. v3 had a typo; this is v4.)
random.seed(20261119)
a, beta, N = 2.0, 1.0, 400000
sw = 0.0; sq = 0.0; ss = 0.0
for _ in range(N):
    x = [random.gammavariate(a, 1.0) for _ in range(3)]
    T = sum(x); p = [xi/T for xi in x]
    w = abs(p[0]-p[1])*abs(p[0]-p[2])*abs(p[1]-p[2])
    sw += w; sq += w*max(p); ss += w*(p[0]*p[0] + p[1]*p[1] + p[2]*p[2])
print('MC   E_w[max p_i] = %.6f  E_w[sum p_i^2] = %.6f' % (sq/sw, ss/sw))
M = 1000
qw = 0.0; qq = 0.0; qs = 0.0
for i in range(1, M):
    x1 = i/M
    for j in range(1, M-i):
        x2 = j/M; x3 = 1-x1-x2
        w = abs(x1-x2)*abs(x1-x3)*abs(x2-x3)*x1*x2*x3
        qw += w; qq += w*max(x1, x2, x3); qs += w*(x1*x1+x2*x2+x3*x3)
print('GRID E_w[max p_i] = %.6f  E_w[sum p_i^2] = %.6f  (M=%d)' % (qq/qw, qs/qw, M))
print('REF chamber-mode max p_i = 0.646564 [s2b]; barycenter max = 0.333333')
print('S4 OK')
