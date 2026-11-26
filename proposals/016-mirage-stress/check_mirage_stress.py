"""
Leading-symbol tree + induced system of the level-one amplitudes (CP^{1,2} class, proposals 013/014), exact rational.
Action (Fourier space): S = 1/2 c^T [ Lam * Mlow + w * H^T Em H ] c - c^T H^T wt.T   (Lam: tree coefficient of (1/2) c M c;
w: coefficient of the linearised Einstein form h.G[h] = c^T H^T Em H c; T: conserved source, coupling sum h^{mu nu} T_{mu nu}).
Checks:
 (a) G = qperp2*1 - (y0/ell5)^2 k k^T  (symbolic q), s_i.q = 0, G k = -sigma q^2 k.
 (b) decomposition c = D s + gamma q (D = C G^{-1}, C_ij = c_i.s_j): Maxwell form = q^2 tr(D G D^T);  h = sum_ij (D_ij+D_ji) s_i s_j + gauge;
     for transverse h: E[h] = (q^2/2)(h - P tr h).
 (c) full solution: X := w E[h] - T is symmetric, conserved, s_i^mu X_{mu nu} = -(Lam/2)(M c)_{i nu},
     X = -(Lam/2) sum_i stilde^i (x) (M c)_i (stilde^i = G^{-1}_{ik} s_k); inert equation (C symmetric).
 (d) Sylvester form h_low = (eta Q) Y + Y (Q eta) with Y = -2X/(Lam q^2), Q = sum_i s_i s_i^T.
 (e) modified Einstein equation  w E + (Lam/2) L^{-1}[ 2E - P tr E ] = T,   L[Z] = (eta Q) Z + Z (Q eta).
"""
import sympy as sp, random
from lib_ls import *
random.seed(3)


def rr():
    return sp.Rational(random.randint(-5, 5), random.randint(1, 3))


y0, y4 = 5, 3
qs = sp.Matrix(sp.symbols('q0:4'))
S = Smats(y0, y4)
sv = [S[i]*qs for i in range(3)]
l5sq = sp.Integer(y0)**2 - y4**2
G = sp.Matrix(3, 3, lambda i, j: sp.expand((sv[i].T*eta*sv[j])[0]))
q2 = sp.expand((qs.T*eta*qs)[0])
qperp2 = sp.expand(q2 + (qs[0]*y0)**2/l5sq)
kk = sp.Matrix([qs[1], qs[2], qs[3]])
Gclosed = qperp2*sp.eye(3) - (sp.Integer(y0)**2/l5sq)*kk*kk.T
print("(a) s_i.q = 0 (symbolic):", all(sp.expand((qs.T*sv[i])[0]) == 0 for i in range(3)))
print("(a) Gram G = qperp2 1 - (y0^2/ell5^2) k k^T (symbolic):", (G - Gclosed).applyfunc(sp.expand) == sp.zeros(3, 3))
sig = sp.Integer(y4)**2/l5sq
print("(a) G k = -sigma q^2 k (symbolic):", (G*kk + sig*q2*kk).applyfunc(sp.expand) == sp.zeros(3, 1))

for (y0, y4) in [(5, 3), (13, 5)]:
    print("==== base point (y0,y4) =", (y0, y4), " ell5^2 =", y0**2 - y4**2)
    qlist = [[0, sp.Rational(1, 3), -5, 3], [7, 1, 2, -1], [3, 1, 0, 0], [2, 5, 1, 1], [sp.Rational(1, 2), -3, 2, 4]]
    for qv in qlist:
        sc = Sector(y0, y4, qv)
        if sc.q2 == 0:
            continue
        print("-- q =", list(sc.q), " q^2 =", sc.q2, " qperp^2 =", sc.qperp2)
        c = sp.Matrix([rr() for _ in range(12)])
        cvec = [[c[3*nu+i] for nu in range(4)] for i in range(3)]
        Cmat = sp.Matrix(3, 3, lambda i, j: (sp.Matrix(cvec[i]).T*eta*sc.s[j])[0])
        Dm = Cmat*sc.G.inv()
        Mq = (c.T*sc.Mlow*c)[0]
        print("   (b) Maxwell form c^T Mlow c = q^2 tr(D G D^T):", sp.simplify(Mq - sc.q2*(Dm*sc.G*Dm.T).trace()) == 0)
        h = sc.hup(c)
        hD = sp.zeros(4, 4)
        for i in range(3):
            for j in range(3):
                hD += (Dm[i, j] + Dm[j, i])*sc.s[i]*sc.s[j].T
        gam = [(sc.q.T*sp.Matrix(cvec[i]))[0]/sc.q2 for i in range(3)]
        hg = sum((gam[i]*(sc.s[i]*sc.qu.T + sc.qu*sc.s[i].T) for i in range(3)), sp.zeros(4, 4))
        print("       h(c) = h(D) + h(gauge gamma q):", (h - hD - hg).applyfunc(sp.simplify) == sp.zeros(4, 4))
        P = sc.Pperp_low()
        hDl = eta*hD*eta
        Eh = lin_einstein(hDl, sc.q)
        trh = (eta.inv()*hDl).trace()
        print("       E[h_T] = (q^2/2)(h - P tr h):", (Eh - sc.q2/2*(hDl - P*trh)).applyfunc(sp.simplify) == sp.zeros(4, 4))
        Lam, w = sp.Rational(3, 7), sp.Rational(2)
        Tl = sc.conserved_T(rr)
        cs = sc.solve(Lam, w, Tl)
        hs = sc.hup(cs)
        Es = sc.E_of_h(hs)
        X = w*Es - Tl
        print("   (c) X symmetric:", (X - X.T).applyfunc(sp.simplify) == sp.zeros(4, 4),
              "; q^mu X_{mu nu} = 0:", (sc.qu.T*X).applyfunc(sp.simplify) == sp.zeros(1, 4))
        csv = [[cs[3*nu+i] for nu in range(4)] for i in range(3)]
        Mc = [sp.Matrix([(sc.Mlow[3*b+i, :]*cs)[0] for b in range(4)]) for i in range(3)]
        okc = all((sc.s[i].T*X - (-Lam/2)*Mc[i].T).applyfunc(sp.simplify) == sp.zeros(1, 4) for i in range(3))
        print("       s_i^mu X_{mu nu} = -(Lam/2)(M c)_{i nu}:", okc)
        Gi = sc.G.inv()
        stl = [sum((Gi[i, k]*sc.s[k] for k in range(3)), sp.zeros(4, 1)) for i in range(3)]
        Xclosed = sum(((eta*stl[i])*Mc[i].T for i in range(3)), sp.zeros(4, 4))*(-Lam/2)
        print("       X = -(Lam/2) sum_i stilde^i (x) (M c)_i (no symmetrisation imposed):", (X - Xclosed).applyfunc(sp.simplify) == sp.zeros(4, 4))
        Cs = sp.Matrix(3, 3, lambda i, j: (sp.Matrix(csv[i]).T*eta*sc.s[j])[0])
        print("       inert equation C = C^T on shell:", (Cs - Cs.T).applyfunc(sp.simplify) == sp.zeros(3, 3))
        Y = -2*X/(Lam*sc.q2)
        Qm = sum((sc.s[i]*sc.s[i].T for i in range(3)), sp.zeros(4, 4))
        syl = (eta*Qm)*Y + Y*(Qm*eta)
        hDs = sp.zeros(4, 4)
        Dms = Cs*Gi
        for i in range(3):
            for j in range(3):
                hDs += (Dms[i, j] + Dms[j, i])*sc.s[i]*sc.s[j].T
        print("   (d) h_T(low) = (eta Q) Y + Y (Q eta),  Y = -2X/(Lam q^2):", (eta*hDs*eta - syl).applyfunc(sp.simplify) == sp.zeros(4, 4))
        trE = (eta.inv()*Es).trace()
        R = 2*Es - P*trE
        basis = []
        for i in range(3):
            for j in range(i, 3):
                basis.append(eta*(sc.s[i]*sc.s[j].T + sc.s[j]*sc.s[i].T)*eta)
        zs = sp.symbols('z0:6')
        Z = sum((zs[k]*basis[k] for k in range(6)), sp.zeros(4, 4))
        LZ = (eta*Qm)*Z + Z*(Qm*eta)
        eqs = list((LZ - R).applyfunc(sp.expand))
        sol = sp.solve(eqs, zs, dict=True)
        if not sol:
            print("   (e) L-equation unsolvable at this q (singular L)")
        else:
            Zs = Z.subs(sol[0])
            res = (w*Es + (Lam/2)*Zs - Tl).applyfunc(sp.simplify)
            print("   (e) w E + (Lam/2) L^{-1}[2E - P tr E] = T :", res == sp.zeros(4, 4))
