# check_payload_killing_126.resume.py -- verify payload numbers tr(ad_J12 ad_J12) = -4,
# tr(ad_K1 ad_K1) = +4 for so(3,1) with generators (M_cd)^mu_nu = d^mu_c eta_dn - d^mu_d eta_cn
# (same convention as verify_126_B_flat5.py Sfull and payload-126.txt), and the identity
# B(X,Y) = 2 tr(XY) used by verify_126_A_nogo.py A2b. Exact rationals via sympy.
import sympy as sp
eta = sp.MutableDenseMatrix(sp.diag(-1, 1, 1, 1))
def M4(c, d):  # 4x4 vector-representation generator (mixed index (M)^mu_nu)
    M = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            M[mu, nu] = (1 if mu == c else 0) * eta[d, nu] - (1 if mu == d else 0) * eta[c, nu]
    return M
pairs = [(c, d) for c in range(4) for d in range(c + 1, 4)]
gens = [M4(*p) for p in pairs]
# structure constants in pair basis
f = sp.MutableDenseMatrix.zeros(6, 6)
# adjoint matrices: ad_{e_i} e_j = sum_k f^k_{ij} e_k; get via solving brackets
br = {}
for i in range(6):
    for j in range(6):
        C = gens[i] * gens[j] - gens[j] * gens[i]
        # solve C = sum_k c_k gens[k]
        cols = [sp.Matrix(g).reshape(16, 1) for g in gens]
        A = sp.Matrix.hstack(*cols)
        sol = A.solve(sp.Matrix(C).reshape(16, 1))
        br[(i, j)] = [sol[k] for k in range(6)]
def adjmat(i):
    Ad = sp.MutableDenseMatrix.zeros(6, 6)
    for j in range(6):
        for k in range(6):
            Ad[k, j] = br[(i, j)][k]
    return sp.Matrix(Ad)
tr2 = [ (adjmat(i) * adjmat(i)).trace() for i in range(6) ]
idx = {p: k for k, p in enumerate(pairs)}
print("basis pairs:", pairs)
print("tr(ad^2) per generator:", tr2)
print("J12 index:", idx[(1, 2)], " K1 index:", idx[(0, 1)])
ok1 = tr2[idx[(1, 2)]] == -4
ok2 = tr2[idx[(0, 1)]] == 4
# identity B(X,Y) = 2 tr(XY) on a random integer pair
import random
random.seed(126)
co = [random.randint(-3, 3) for _ in range(6)]
co2 = [random.randint(-3, 3) for _ in range(6)]
X = sp.zeros(4, 4); Y = sp.zeros(4, 4)
for i in range(6):
    X = X + co[i] * gens[i]
    Y = Y + co2[i] * gens[i]
BX = sum(co[i] * co2[j] * (adjmat(i) * adjmat(j)).trace() for i in range(6) for j in range(6))
ok3 = sp.simplify(BX - 2 * (X * Y).trace()) == 0
print("KILLING-CHECK:", "PASS" if (ok1 and ok2 and ok3) else "FAIL",
      "J12=-4:", ok1, "K1=+4:", ok2, "B=2tr(XY):", ok3)
