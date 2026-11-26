"""Second-order solvability of J = 0 about a constant Theta_bar (Euclidean section) for a quadratic first-order Maxwell solution a.
psi = x + eps a + eps^2 a2, a2 cubic (80 unknown coefficients);  Theta = (psi^* omega_bar)^{-1};  J_n = Theta^{mr} d_r Theta^{mn}.
Solve J^(2) = 0 (linear in a2) : report whether the system is consistent (obstruction = 0)."""
import numpy as np, sympy as sp, itertools
rng = np.random.default_rng(5)
x = sp.symbols('x1:5'); eps = sp.symbols('eps')
Tb = sp.Matrix([[0, 1, 0, sp.Rational(3, 10)], [-1, 0, 0, 0], [-sp.Rational(3, 10), 0, 0, 2], [0, 0, -2, 0]])
# make antisymmetric with all pairs: add (1,3) entry
Tb = sp.Matrix([[0, 1, sp.Rational(3, 10), 0], [-1, 0, 0, -sp.Rational(3, 20)], [-sp.Rational(3, 10), 0, 0, 2], [0, sp.Rational(3, 20), -2, 0]])
assert Tb.T == -Tb
wbar = Tb.inv()
K = Tb.T*Tb
# first-order quadratic solution a: nullspace of J1 map
pairs = [(r, s) for r in range(4) for s in range(r, 4)]
def J1_of_H(H):
    out = []
    for n in range(4):
        t = sum(K[r, s]*H[n][r][s] for r in range(4) for s in range(4))
        t -= sum(Tb[n, r]*Tb[m, s]*H[m][r][s] for r in range(4) for m in range(4) for s in range(4))
        out.append(t)
    return out
hs = sp.symbols('h0:40')
def Hmat(hv):
    H = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for n in range(4):
        for k, (r, s) in enumerate(pairs):
            H[n][r][s] = hv[n*10+k]; H[n][s][r] = hv[n*10+k]
    return H
eqs1 = J1_of_H(Hmat(hs))
A1, _ = sp.linear_eq_to_matrix(eqs1, list(hs))
nsp = A1.nullspace()
vec = sum((sp.Rational(int(rng.integers(-3, 4)), 1)*v for v in nsp), sp.zeros(40, 1))
hv = list(vec)
H = Hmat(hv)
print('J1 residual:', [sp.simplify(v) for v in J1_of_H(H)])
a = [sum(sp.Rational(1, 2)*H[n][r][s]*x[r]*x[s] for r in range(4) for s in range(4)) for n in range(4)]
# a2 cubic with unknown coefficients
mons3 = [m for m in itertools.product(range(4), repeat=4) if sum(m) == 3]
cs = sp.symbols('c0:%d' % (4*len(mons3)))
a2 = [sum(cs[n*len(mons3)+k]*sp.prod([x[i]**mons3[k][i] for i in range(4)]) for k in range(len(mons3))) for n in range(4)]
def jac(v):
    return sp.Matrix(4, 4, lambda r, m: sp.diff(v[m], x[r]))     # (d psi)^m_r  as [r,m]
dpsi = sp.eye(4) + eps*jac(a) + eps**2*jac(a2)      # [rho, mu] = d_rho psi^mu
om = (dpsi*wbar*dpsi.T)                              # omega_{rho sigma} = d_rho psi^mu wbar_{mu nu} d_sigma psi^nu
om = om.applyfunc(lambda e: sp.expand(e))
om0 = om.subs(eps, 0)
d1 = om.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0))
d2 = om.applyfunc(lambda e: sp.diff(e, eps, 2).subs(eps, 0)/2)
Th0 = Tb
Th1 = (-Th0*d1*Th0).applyfunc(sp.expand)
Th2 = (Th0*d1*Th0*d1*Th0 - Th0*d2*Th0).applyfunc(sp.expand)
def Jvec(Th):
    return [sum(Th0[m, r]*sp.diff(Th[m, n], x[r]) for m in range(4) for r in range(4)) for n in range(4)]
J2 = [sp.expand(a_ + b_) for a_, b_ in zip(
    Jvec(Th2),
    [sum(Th1[m, r]*sp.diff(Th1[m, n], x[r]) for m in range(4) for r in range(4)) for n in range(4)])]
print('J^(1) (should vanish):', [sp.simplify(v) for v in Jvec(Th1)])
eqs = []
for e in J2:
    P = sp.Poly(e, *x)
    eqs += list(P.coeffs())
print('number of scalar equations:', len(eqs))
Alin, bvec = sp.linear_eq_to_matrix(eqs, list(cs))
Alin = sp.Matrix(Alin); bvec = sp.Matrix(bvec)
rank_A = Alin.rank(); rank_Ab = Alin.row_join(bvec).rank()
print('rank A =', rank_A, ' rank [A|b] =', rank_Ab, ' => second-order equation solvable by a cubic a2:', rank_A == rank_Ab)
