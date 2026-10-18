"""027 script 10: representation sum rules for the spin (J.Sigma) coupling and the Zeeman character, for the IKKT-type content in the four-matrix class.
Sigma_V^{ab}: (Sigma^{ab})^c_d = eta^{ac} delta^b_d - eta^{bc} delta^a_d (vector of SO(3,1));  Sigma_D^{ab} = (1/4)[gamma^a, gamma^b] (Dirac, 4 complex components).
 (1) same commutation relations; (2) tr(Sigma_D Sigma_D) = (1/2) tr(Sigma_V Sigma_V) for all index pairs;
 (3) Zeeman characters.  F with magnetic pair B (12-plane, eta F eigenvalues +-iB) and electric pair A (03-plane, eigenvalues +-A);  Z_R = -i Sigma_R^{ab} F_{ab};
     vector: eigenvalues +-2B (real), +-2iA;  Dirac: +-B +-iA.
     str(s) := tr_V e^{-isZ_V} + (6 scalars - 2 ghosts) - (1/2)*4*tr_D e^{-isZ_D}   [16 real fermion components = 4 Majorana, each complexifying to a Dirac 4]
 (4) counting:  N_b - N_f = (4 + 6 - 2) - (1/2)*16 = 0 ;   index sum rule:  1*T_V - (1/2)*4*T_D = T_V (1 - 2*(1/2)) = 0."""
import sympy as sp, itertools
s, A, B = sp.symbols('s A B', positive=True)
eta = sp.diag(-1, 1, 1, 1)
def SigV(a, b):
    M = sp.zeros(4, 4)
    for c in range(4):
        for d in range(4):
            M[c, d] = eta[a, c]*(1 if b == d else 0) - eta[b, c]*(1 if a == d else 0)     # eta^{ac}: eta is its own inverse
    return M
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Zm = sp.Matrix([[1, 0], [0, -1]])
kp = sp.kronecker_product
g0 = sp.I*kp(X, I2); g1 = kp(Y, X); g2 = kp(Y, Y); g3 = kp(Y, Zm)       # {g_a,g_b} = 2 eta_ab with eta=(-,+,+,+): g0^2=-1
G = [g0, g1, g2, g3]
for a in range(4):
    for b in range(4):
        assert sp.simplify(G[a]*G[b] + G[b]*G[a] - 2*eta[a, b]*sp.eye(4)) == sp.zeros(4, 4)
def SigD(a, b): return (G[a]*G[b] - G[b]*G[a])/4
# (1) commutation relations: [S^{ab}, S^{cd}] = eta^{bc} S^{ad} - eta^{ac} S^{bd} - eta^{bd} S^{ac} + eta^{ad} S^{bc}   (fit sign from the vector)
def comm_ok(S):
    ok = True
    for a, b, c, d in itertools.product(range(4), repeat=4):
        lhs = S(a, b)*S(c, d) - S(c, d)*S(a, b)
        rhs = eta[b, c]*S(a, d) - eta[a, c]*S(b, d) - eta[b, d]*S(a, c) + eta[a, d]*S(b, c)
        ok &= sp.simplify(lhs - rhs) == sp.zeros(lhs.shape[0], lhs.shape[1])
    return ok
sgn = None
for sg in (1, -1):
    okV = comm_ok(lambda a, b, sg=sg: sg*SigV(a, b))
    print("vector with sign", sg, "satisfies the structure constants:", okV)
    if okV: sgn = sg
for sg in (1, -1):
    print("Dirac with sign", sg, ":", comm_ok(lambda a, b, sg=sg: sg*SigD(a, b)))
# (2) index ratio
ratios = set()
for a, b, c, d in itertools.product(range(4), repeat=4):
    tv = (SigV(a, b)*SigV(c, d)).trace(); td = (SigD(a, b)*SigD(c, d)).trace()
    if tv != 0 or td != 0:
        ratios.add(sp.simplify(td/tv))
print("tr(Sigma_D Sigma_D)/tr(Sigma_V Sigma_V) over all index choices:", ratios)
# (3) Zeeman characters.  F_{12}=B-type rotation, F_{03}=A-type boost; Z = -i Sigma^{ab}F_{ab}  (sum over all a,b, both orders)
def Zmat(S, FB, FA):
    return -sp.I*2*(FB*S(1, 2) + FA*S(0, 3))
ZV = Zmat(lambda a, b: sgn*SigV(a, b), B, A); ZD = Zmat(SigD, B, A)
print("eigenvalues Z_V:", sorted(ZV.eigenvals().keys(), key=str), " Z_D:", sorted(ZD.eigenvals().keys(), key=str))
trV = sum(m*sp.exp(-sp.I*s*ev) for ev, m in ZV.eigenvals().items()); trD = sum(m*sp.exp(-sp.I*s*ev) for ev, m in ZD.eigenvals().items())
st = sp.simplify(trV + 4 - 2*trD)
target = 4*(sp.cos(s*B) - sp.cosh(s*A))**2
print("str(s) - 4 (cos sB - cosh sA)^2 =", sp.simplify((st - target).rewrite(sp.exp).expand()))
print("series of str(s):", sp.series(st.rewrite(sp.exp), s, 0, 6).removeO().simplify(), " vs  s^4 (A^2+B^2)^2 :", sp.factor(sp.series(target, s, 0, 6).removeO()))
print("s^2 coefficients:  vector", sp.series(trV.rewrite(sp.exp), s, 0, 4).removeO().coeff(s, 2), "  Dirac", sp.series(trD.rewrite(sp.exp), s, 0, 4).removeO().coeff(s, 2), " -> 1*vec -2*Dirac ->", sp.simplify(sp.series(trV.rewrite(sp.exp), s, 0, 4).removeO().coeff(s, 2) - 2*sp.series(trD.rewrite(sp.exp), s, 0, 4).removeO().coeff(s, 2)))
# bosonic only (non-supersymmetric) s^2 coefficient: vector + n_ex scalars - 2 ghosts  : 4 q_F with q_F = A^2 - B^2 ; plus orbital (Landau) factor handled separately
print("q_F = A^2-B^2 ; vector s^2 coefficient / q_F =", sp.simplify(sp.series(trV.rewrite(sp.exp), s, 0, 4).removeO().coeff(s, 2)/(A**2 - B**2)))
