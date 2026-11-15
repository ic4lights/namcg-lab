"""070 s1: sector endomorphisms of the Poisson-limit operators at random two-jets (exact rationals).
Euclidean section eta = delta, four coordinates, alpha = 1.
Operators (D_mu f = Theta^{mu nu} d_nu f):
  scalar  O_s = -D_mu D_mu
  vector  (O_v a)_mu = -D^2 a_mu - 2 {Theta_{mu nu}, a_nu}
  Dirac   O_f = -(gamma^mu D_mu)^2 = O_s - (1/2) gamma^{mu nu} {Theta_{mu nu}, .}
Each is -(G^{nu rho} d_nu d_rho + A^rho d_rho) with G^{nu rho} = Theta^{mu nu} Theta^{mu rho}.
Vassilevich (hep-th/0306138, eqs 2.2-2.4): w_d = (1/2) G_{nu d}(A^nu + G^{mu s} Gamma^nu_{mu s}),
  E_V = -G^{nu mu}(d_mu w_nu + w_nu w_mu - w_s Gamma^s_{nu mu});  manuscript E = -E_V, a_1 = tr(R/6 - E).
Checks, per random closed omega:
  (a) E_s = -(1/2) Box_G ln rho + (1/4)|d ln rho|^2_G =: e
  (b) tr E_v = 4 e - X,  X := sum (d_rho Theta^{mu nu})^2 contracted = -tr(b_s b^s)
  (c) tr E_f = 4 e - X/2
  => sum_i w_i tr(R/6 - E_i) = N_tot (R/6 - e) + (1 - n_D/2) X, N_tot = N_s + 2 - 4 n_D.
Re-run: python proposals/070-b-content-class/s1_weighted_a1.py
"""
import random, sympy as sp
random.seed(70)
x = sp.symbols('x0:4')
I2 = sp.eye(2); s1 = sp.Matrix([[0,1],[1,0]]); s2 = sp.Matrix([[0,-sp.I],[sp.I,0]]); s3 = sp.Matrix([[1,0],[0,-1]])
kron = sp.kronecker_product
gam = [kron(s1, s1), kron(s1, s2), kron(s1, s3), kron(s2, I2)]
for a in range(4):
    for b in range(4):
        assert gam[a]*gam[b] + gam[b]*gam[a] == 2*(1 if a == b else 0)*sp.eye(4)

def rnd(): return sp.Rational(random.randint(-4, 4), random.randint(1, 3))

def jet_theta():
    # omega = omega0 + dA, A cubic polynomial one-form; Theta = omega^{-1} to second order at x = 0
    while True:
        w0 = sp.zeros(4, 4)
        for i in range(4):
            for j in range(i+1, 4):
                w0[i, j] = rnd(); w0[j, i] = -w0[i, j]
        if w0.det() != 0: break
    mons = sorted([m for m in sp.itermonomials(x, 3) if sp.Poly(m, *x).total_degree() in (2, 3)], key=sp.default_sort_key)
    A = [sum(rnd()*m for m in random.sample(mons, 7)) for _ in range(4)]
    dA = sp.Matrix(4, 4, lambda i, j: sp.diff(A[j], x[i]) - sp.diff(A[i], x[j]))
    def part(M, d):
        return M.applyfunc(lambda e: sum(c*sp.prod([v**p for v, p in zip(x, mon)])
                                         for mon, c in sp.Poly(e, *x).terms() if sum(mon) == d) if e != 0 else 0)
    w1, w2 = part(dA, 1), part(dA, 2)
    T0 = w0.inv()
    T = T0 - T0*w1*T0 - T0*w2*T0 + T0*w1*T0*w1*T0
    return T.applyfunc(sp.expand)

def at0(e): return sp.simplify(sp.sympify(e).subs({v: 0 for v in x}))

def endo(T, lin):
    """lin[rho] = fibre matrix (k x k) added to the scalar first-order coefficient. Returns E (manuscript sign) at 0."""
    k = lin[0].shape[0]
    Ginv = (T.T*T).applyfunc(sp.expand)            # G^{nu rho} = Theta^{mu nu} Theta^{mu rho}
    Gi0 = Ginv.subs({v: 0 for v in x}); G0 = Gi0.inv()
    dGinv = [sp.diff(Ginv, v) for v in x]
    dG0 = [-(G0*dGinv[m].subs({v: 0 for v in x})*G0) for m in range(4)]
    # second derivative of G at 0
    d2Ginv = [[sp.diff(Ginv, x[m], x[n]).subs({v: 0 for v in x}) for n in range(4)] for m in range(4)]
    dGi0 = [dGinv[m].subs({v: 0 for v in x}) for m in range(4)]
    d2G0 = [[-(dG0[n]*dGi0[m]*G0) - G0*d2Ginv[m][n]*G0 - G0*dGi0[m]*dG0[n] for n in range(4)] for m in range(4)]
    def Gam(n_, m_, s_):   # Gamma^n_{m s} at 0
        return sum(Gi0[n_, l]*(dG0[m_][l, s_] + dG0[s_][l, m_] - dG0[l][m_, s_]) for l in range(4))/2
    def dGam(a, n_, m_, s_):  # d_a Gamma^n_{m s} at 0
        t = sum(dGi0[a][n_, l]*(dG0[m_][l, s_] + dG0[s_][l, m_] - dG0[l][m_, s_]) for l in range(4))/2
        t += sum(Gi0[n_, l]*(d2G0[a][m_][l, s_] + d2G0[a][s_][l, m_] - d2G0[a][l][m_, s_]) for l in range(4))/2
        return t
    As = [sum(T[m, n]*sp.diff(T[m, r], x[n]) for m in range(4) for n in range(4)) for r in range(4)]
    Afull = [As[r]*sp.eye(k) + lin[r] for r in range(4)]
    A0 = [M.subs({v: 0 for v in x}) for M in Afull]
    dA0 = [[sp.diff(Afull[r], x[a]).subs({v: 0 for v in x}) for r in range(4)] for a in range(4)]
    def w(d):
        return sum((G0[n, d]*(A0[n] + sum(Gi0[m, s]*Gam(n, m, s) for m in range(4) for s in range(4))*sp.eye(k)) for n in range(4)), sp.zeros(k, k))/2
    def dw(a, d):
        t = sp.zeros(k, k)
        for n in range(4):
            c = sum(Gi0[m, s]*Gam(n, m, s) for m in range(4) for s in range(4))
            dc = sum(dGi0[a][m, s]*Gam(n, m, s) + Gi0[m, s]*dGam(a, n, m, s) for m in range(4) for s in range(4))
            t += dG0[a][n, d]*(A0[n] + c*sp.eye(k)) + G0[n, d]*(dA0[a][n] + dc*sp.eye(k))
        return t/2
    W = [w(d) for d in range(4)]
    EV = sp.zeros(k, k)
    for n in range(4):
        for m in range(4):
            EV -= Gi0[n, m]*(dw(m, n) + W[n]*W[m] - sum((W[s]*Gam(s, n, m) for s in range(4)), sp.zeros(k, k)))
    return (-EV).applyfunc(sp.expand)

def scalar_e(T):
    Ginv = (T.T*T).applyfunc(sp.expand)
    pf = T[0, 1]*T[2, 3] - T[0, 2]*T[1, 3] + T[0, 3]*T[1, 2]      # Pf Theta ; rho = 1/|Pf Theta|, sqrt G = rho^2
    lnrho = -sp.log(pf**2)/2
    sq = pf**(-2)
    box = sum(sp.diff(sq*Ginv[m, n]*sp.diff(lnrho, x[n]), x[m]) for m in range(4) for n in range(4))/sq
    grad2 = sum(Ginv[m, n]*sp.diff(lnrho, x[m])*sp.diff(lnrho, x[n]) for m in range(4) for n in range(4))
    return at0(-box/2 + grad2/4)

ok = True
for trial in range(4):
    T = jet_theta()
    # Jacobi identity of the two-jet representative at 0 to first order (closure of omega)
    jac = max(abs(at0(sum(T[i, l]*sp.diff(T[j, k], x[l]) + T[j, l]*sp.diff(T[k, i], x[l]) + T[k, l]*sp.diff(T[i, j], x[l]) for l in range(4))))
              for i in range(4) for j in range(4) for k in range(4))
    M = [sp.Matrix(4, 4, lambda mu, nu: sum(T[a, r]*sp.diff(T[mu, nu], x[a]) for a in range(4))) for r in range(4)]  # Theta^{a r} d_a Theta^{mu nu}
    Es = endo(T, [sp.zeros(1, 1)]*4)[0, 0]
    Ev = endo(T, [2*M[r] for r in range(4)])
    lift = [sum(((gam[m]*gam[n] - gam[n]*gam[m])/2*M[r][m, n] for m in range(4) for n in range(4)), sp.zeros(4, 4))/2 for r in range(4)]
    Ef = endo(T, lift)
    e = scalar_e(T)
    X = at0(sum(sp.diff(T[m, n], x[r])**2 for m in range(4) for n in range(4) for r in range(4)))
    ra, rb, rc = sp.simplify(Es - e), sp.simplify(Ev.trace() - (4*e - X)), sp.simplify(Ef.trace() - (4*e - X/2))
    print(f"trial {trial}: Jacobi(0)={jac}  e={e}  X={X}  (a) E_s-e={ra}  (b) trE_v-(4e-X)={rb}  (c) trE_f-(4e-X/2)={rc}")
    ok &= (jac == 0 and ra == 0 and rb == 0 and rc == 0 and X > 0)
Ns, nD, Rm, e, X = sp.symbols('N_s n_D R e X')
a1 = Ns*(Rm/6 - e) + (4*(Rm/6 - e) + X) - 2*(Rm/6 - e) - nD*(4*(Rm/6 - e) + X/2)
print("weighted a_1 - [N_tot(R/6-e) + (1-n_D/2) X] =", sp.simplify(a1 - ((Ns + 2 - 4*nD)*(Rm/6 - e) + (1 - nD/2)*X)))
print("weighted a_1 at (6,2):", sp.simplify(a1.subs({Ns: 6, nD: 2})))
print("S1 PASS" if ok else "S1 FAIL")
