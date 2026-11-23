"""075 s6 (sympy, exact): for an arbitrary real vector vsf^f, vanishing connection and constant structure constants
cbar_ab^d = 1/2 eps_ab^d_f vsf^f (eps^{0123} = +1, eta = diag(-1,1,1,1)):
 (1) Jacobi identity; (2) E along vsf is central (vsf^a cbar_ab^d = 0); (3) trace cbar_ac^c = 0 (so t = 0, F = 0);
 (4) first bracket with the cubic term, B1_b^e - 1/2 eps_b^{cd}_f vsf^f T_cd^e with T = -cbar and
     B1_b^e = T_ab^c T^a_c^e (constant section values, zero connection, R = 0), vanishes identically;
 (5) T_abc T^abc = 3/2 * vsf.vsf ... printed; (6) the second bracket vanishes since R = 0."""
import itertools
import sympy as sp
v = sp.symbols('v0:4', real=True)
eta = sp.diag(-1, 1, 1, 1)
R4 = range(4)
epsU = lambda a, b, c, d: sp.LeviCivita(a, b, c, d)
# eps_ab^d_f = eta_aa' eta_bb' eta_ff' eps^{a' b' d f'} (diagonal eta)
def emix(a, b, d, f):
    return eta[a, a] * eta[b, b] * eta[f, f] * epsU(a, b, d, f)
cb = [[[sp.Rational(1, 2) * sum(emix(a, b, d, f) * v[f] for f in R4) for d in R4] for b in R4] for a in R4]
jac = 0
for a, b, c, e in itertools.product(R4, repeat=4):
    J = sum(cb[a][b][d] * cb[d][c][e] + cb[b][c][d] * cb[d][a][e] + cb[c][a][d] * cb[d][b][e] for d in R4)
    jac += sp.expand(J) ** 2
print('(1) sum of squares of Jacobi components:', sp.simplify(jac))
print('(2) vsf^a cbar_ab^d:', set(sp.expand(sum(v[a] * cb[a][b][d] for a in R4)) for b in R4 for d in R4))
print('(3) cbar_ac^c:', set(sp.expand(sum(cb[a][c][c] for c in R4)) for a in R4))
T = [[[-cb[a][b][d] for d in R4] for b in R4] for a in R4]
res = set()
for b, e in itertools.product(R4, repeat=2):
    B1 = sum(eta[a, a] * T[a][b][c] * T[a][c][e] for a in R4 for c in R4)        # T_ab^c T^a_c^e
    cub = -sp.Rational(1, 2) * sum(eta[b, b] * eta[f, f] * epsU(b, c, d, f) * v[f] * T[c][d][e]
                                   for c in R4 for d in R4 for f in R4)
    res.add(sp.expand(B1 + cub))
print('(4) first bracket with cubic term, distinct components:', res)
TT = sp.expand(sum(eta[a, a] * eta[b, b] * eta[d, d] * T[a][b][d] ** 2 for a in R4 for b in R4 for d in R4))
VV = sp.expand(sum(eta[f, f] * v[f] ** 2 for f in R4))
print('(5) T_abc T^abc / (v.v) =', sp.simplify(TT / VV))
