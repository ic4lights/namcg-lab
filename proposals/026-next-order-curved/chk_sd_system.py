"""(i) closed SD omega=b_i eta^i  <=>  div b = 0, d_4 b = -curl b  (checked on solution space);
   (ii) SD (or ASD) Theta: G^{mn} = delta/rho and J = 0 identically (analytic: J^nu = Box_G x^nu - G^{mu nu} d_mu ln rho);
   (iii) pointwise bound rho |Theta|^2 >= 4 with equality iff SD/ASD (random check)."""
import sympy as sp, numpy as np, random, itertools
import lib, sd_family
X = sd_family.X
for anti in (False, True):
    bsol, eta = sd_family.sd_solution(deg=3, seed=3, anti=anti, b0=(1, 2, 3))
    div = sp.expand(sum(sp.diff(bsol[i], X[i]) for i in range(3)))
    curl = [sum(sp.LeviCivita(j, k, i)*sp.diff(bsol[i], X[k]) for k in range(3) for i in range(3)) for j in range(3)]
    if not anti:
        res = [sp.expand(sp.diff(bsol[j], X[3]) + curl[j]) for j in range(3)]
    else:
        res = [sp.expand(sp.diff(bsol[j], X[3]) - curl[j]) for j in range(3)]
    print('ASD' if anti else 'SD ', ': div b =', div, '; d_4 b %s curl b residual =' % ('-' if not anti else '+'), res)
# (ii)
x = sp.symbols('x1:5')
f = sp.Function('f')
bs = [sp.Function('b%d' % i)(*x) for i in range(1, 4)]
eta = lib.eta3()
w = sum((bs[i]*eta[i] for i in range(3)), sp.zeros(4, 4))
Th = lib.inv_antisym(w)
GG = sp.simplify(Th.T*Th)
nb2 = sum(b**2 for b in bs)
print('G^{mn} - delta/rho (rho=|b|^2, since Theta = -b.eta/|b|^2 => G^{mn} = delta/|b|^2):', sp.simplify(GG - sp.eye(4)/nb2) == sp.zeros(4, 4))
# (iii)
rng = np.random.default_rng(0)
et = [np.array(e.tolist(), float) for e in lib.eta3()]; eb = [np.array(e.tolist(), float) for e in lib.etabar()]
mn = 1e9
for _ in range(2000):
    a = rng.normal(size=3); b = rng.normal(size=3)
    T = sum(a[i]*et[i] + b[i]*eb[i] for i in range(3))
    pf = T[0, 1]*T[2, 3] - T[0, 2]*T[1, 3] + T[0, 3]*T[1, 2]
    val = np.sum(T*T)/abs(pf)
    mn = min(mn, val)
print('min over random of Theta^{mn}Theta^{mn}/|Pf Theta| (i.e. rho |Theta|^2) =', mn, ' (>= 4)')
T = 2*et[0] + 0.7*et[1]
pf = T[0, 1]*T[2, 3] - T[0, 2]*T[1, 3] + T[0, 3]*T[1, 2]
print('SD value:', np.sum(T*T)/abs(pf))
