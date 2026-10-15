"""
(1) K_Theta^{-1} is the composite metric g = eta_{AB} e^A_mu e^B_nu of ch04 (def:composite-metric) for the coframe
        e^A_nu := (Theta^{-1})_{nu}{}^{A}   [ e^A_nu = eta^{AB} omega_{nu B},  omega := Theta^{-1} the symplectic form, omega_{nu B} Theta^{B rho} = delta_nu^rho ],
    verified for random antisymmetric Theta and both signatures; the frame is 'antisymmetric' (e_{A nu} = -e_{nu A} after lowering A with eta).
(2) Rank of Theta -> K_Theta^{-1} (pointwise, 6 -> 10): Jacobian rank 6; the Theta-built metrics form a 6-dim subfamily of the 10-dim
    space of metrics; K eta (mixed) has two doubly degenerate eigenvalues.
(3) Conformal-frame formula, 4D:  int sqrt(g) Omega^2 R[g] = int sqrt(ghat)[ Rhat - 6 (d ln Omega)^2_hat ],  ghat = Omega^2 g
    (checked on a diagonal family: the pointwise difference equals 6 d_mu(sqrt(g) Omega g^{mu nu} d_nu Omega)).
"""
import sympy as sp, random
random.seed(5)
n = 4
for s0 in (-1, 1):
    eta = sp.diag(s0, 1, 1, 1)
    M = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i+1, 4):
            v = sp.Rational(random.randint(-5, 5), 3); M[i, j] = v; M[j, i] = -v
    Th = M                                          # Theta^{mu nu}
    K = Th.T*eta*Th                                  # K^{rs} = Theta^{a r} eta_{ab} Theta^{b s}
    omega = Th.inv()                                 # omega_{nu B} (matrix inverse): omega*Th = 1
    e = omega*eta.inv()                              # e_nu^A = omega_{nu B} eta^{BA}
    g = e*eta*e.T                                    # g_{mu nu} = eta_{AB} e_mu^A e_nu^B  -> (e eta e^T)_{mu nu}
    print("signature s0=%d: K^{-1} == e eta e^T :" % s0, sp.simplify(K.inv() - g) == sp.zeros(4, 4),
          "; e_{A nu}=eta_{AB} e_nu^B antisymmetric:", sp.simplify((e*eta) + (e*eta).T) == sp.zeros(4, 4))
    S = K*eta
    print("   eigenvalues of K eta (mixed):", {sp.nsimplify(k): v for k, v in S.eigenvals().items()})
# (2) rank of the map Theta -> K^{-1}
th = sp.symbols('t01 t02 t03 t12 t13 t23')
eta = sp.diag(-1, 1, 1, 1)
T = sp.Matrix([[0, th[0], th[1], th[2]], [-th[0], 0, th[3], th[4]], [-th[1], -th[3], 0, th[5]], [-th[2], -th[4], -th[5], 0]])
Kinv = (T.T*eta*T).inv()
iu = [(i, j) for i in range(4) for j in range(i, 4)]
vec = sp.Matrix([Kinv[i, j] for (i, j) in iu])
Jm = vec.jacobian(sp.Matrix(th))
pt = dict(zip(th, [sp.Rational(v) for v in (1, 2, -1, 3, 2, 5)]))
print("rank of d(K^{-1})/d(Theta) at a random point (6 params -> 10 comps):", Jm.subs(pt).rank())
# (3) conformal frame formula
x = sp.symbols('x0:4'); u = sp.Function('u')(x[0], x[1]); w = sp.Function('w')(x[0], x[1]); Om = sp.Function('Om')(x[0], x[1])
def Rsc(g):
    gi = g.inv()
    Gm = [[[sum(gi[l, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(4))/2
            for c in range(4)] for b in range(4)] for l in range(4)]
    def Riem(a, b, c, d):
        return (sp.diff(Gm[a][b][d], x[c]) - sp.diff(Gm[a][b][c], x[d]) + sum(Gm[a][c][e]*Gm[e][b][d] - Gm[a][d][e]*Gm[e][b][c] for e in range(4)))
    Ric = sp.Matrix(4, 4, lambda b, d: sum(Riem(a, b, a, d) for a in range(4)))
    return sp.simplify(sum(gi[p, q]*Ric[p, q] for p in range(4) for q in range(4)))
g = sp.diag(sp.exp(u), -sp.exp(u), sp.exp(w), sp.exp(w))       # det g != unimodular on purpose
sg = sp.exp(u + w)
gh = Om**2*g; sgh = Om**4*sg
R = Rsc(g); Rh = Rsc(gh)
ghi = gh.inv()
dl = sum(ghi[m, k]*sp.diff(sp.log(Om), x[m])*sp.diff(sp.log(Om), x[k]) for m in range(4) for k in range(4))
lhs = sg*Om**2*R
rhs = sgh*(Rh - 6*dl)
gi0 = g.inv()
diff = sp.simplify(lhs - rhs)
div = sum(sp.diff(sg*sum(gi0[m, k]*Om*sp.diff(Om, x[k]) for k in range(4)), x[m]) for m in range(4))
print("(3) conformal-frame formula: lhs - rhs - 6*d_mu( sqrt(g) Om g^{mu nu} d_nu Om ) =", sp.simplify(diff - 6*div), "(a total derivative, so the integrals agree)")
