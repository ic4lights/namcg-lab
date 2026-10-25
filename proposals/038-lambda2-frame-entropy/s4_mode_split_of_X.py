"""s4: on the delta-rho = 0 plane-wave modes about a constant (anti-)self-dual Theta_bar, split the quadratic form of X = T_{lmn}T^{lmn}
into its irreducible torsion parts (vector V, axial S, tensor q) and compare with the Einstein form.

Mode (033/036 convention): Theta = Theta_bar + eps*T, T^{mu nu} = Theta_bar^{mu rho} d_rho a^nu - (mu<->nu), a^nu = u^nu cos(p.x).
With omega = Theta^{-1}:  omega^(1)_{mu nu} = sin(p.x) (p_mu w_nu - p_nu w_mu), w = omega_bar u  (closed),
torsion T^A_{mu nu} = -d_A omega_{mu nu},  T_{l mu nu} = e^A_l T^A_{mu nu},  e^A_l = omega_bar_{l A}.   First order T is all that enters X^(2), S^2, q^2, V^2.
delta rho = 0  <=>  V = 0 at first order.
Prediction from the exact identity R = -calT - 2 div V, calT = -2/3 V^2 - 1/4 S^2 + 1/2 q^2 (s1) and from the ledger eigenvalues
(X: 1, rho R[g_rho]: -1/4 on the delta rho=0 modes):   <S^2>/<X> = 1/3,  <q^2>/<X> = 2/3,  <R>/<X> = -1/4.
"""
import random
import sympy as sp
from sympy import Rational as Q

random.seed(7)
d = 4

def eta_plus():
    out = []
    for i in range(3):
        M = sp.zeros(4, 4)
        for a in range(3):
            for b in range(3):
                M[a, b] = sp.LeviCivita(i, a, b)
            M[a, 3] = 1 if a == i else 0
            M[3, a] = -1 if a == i else 0
        out.append(M)
    return out

def eta_minus():
    out = []
    for i in range(3):
        M = sp.zeros(4, 4)
        for a in range(3):
            for b in range(3):
                M[a, b] = sp.LeviCivita(i, a, b)
            M[a, 3] = -1 if a == i else 0
            M[3, a] = 1 if a == i else 0
        out.append(M)
    return out

def rnd(lo=-4, hi=4):
    return Q(random.randint(lo, hi), random.randint(1, 3))

def run(omb, ntrials=6):
    omb = omb.copy()
    Gbar_inv = (omb.inv()).T*(omb.inv())          # G^{mu nu} = Theta^{a mu}Theta^{a nu}
    Gb = Gbar_inv.inv()
    g0 = Gb[0, 0]
    assert Gb == g0*sp.eye(4)
    res = []
    for _ in range(ntrials):
        p = sp.Matrix([rnd() for _ in range(4)])
        if p == sp.zeros(4, 1):
            continue
        v = sp.symbols('v0:4')
        u = sp.Matrix(v)
        w = omb*u
        r = omb*p                                   # r_l = omega_bar_{lA} p_A
        # delta rho = 0 :  V_mu = -(r.w) p_mu * (1/g0)  ->  r.w = 0
        cond = sp.expand((r.T*w)[0])
        vv = [rnd() for _ in range(3)]
        sol = sp.solve(cond.subs(dict(zip(v[:3], vv))), v[3], dict=True)
        if not sol:
            continue
        vals = dict(zip(v[:3], vv)); vals[v[3]] = sol[0][v[3]]
        uu = u.subs(vals); ww = omb*uu
        # amplitude of the cos(p.x) factor set to 1 (phase average multiplies X, S^2, q^2, V^2 by the same 1/2)
        T = [[[-r[l]*(p[m]*ww[n] - p[n]*ww[m]) for n in range(d)] for m in range(d)] for l in range(d)]
        Gi = Gbar_inv
        def up(T):
            return [[[sum(Gi[l, a]*Gi[m, b]*Gi[n, c]*T[a][b][c] for a in range(d) for b in range(d) for c in range(d))
                      for n in range(d)] for m in range(d)] for l in range(d)]
        Tu = up(T)
        TT = sum(T[l][m][n]*Tu[l][m][n] for l in range(d) for m in range(d) for n in range(d))
        TTp = sum(T[l][m][n]*Tu[m][l][n] for l in range(d) for m in range(d) for n in range(d))
        V = [sum(Gi[l, n]*T[l][m][n] for l in range(d) for n in range(d)) for m in range(d)]
        V2 = sum(Gi[m, n]*V[m]*V[n] for m in range(d) for n in range(d))
        S = [[[sum(sg*T[a][b][c] for (a, b, c), sg in [((l, m, n), 1), ((m, n, l), 1), ((n, l, m), 1), ((m, l, n), -1), ((l, n, m), -1), ((n, m, l), -1)])/6
               for n in range(d)] for m in range(d)] for l in range(d)]
        Su = up(S)
        S2 = sum(S[l][m][n]*Su[l][m][n] for l in range(d) for m in range(d) for n in range(d))
        calT = TT/4 + TTp/2 - V2
        if TT == 0:
            continue
        q2 = TT - sp.Rational(2, 3)*V2 - S2
        res.append((sp.nsimplify(V2), sp.nsimplify(S2/TT), sp.nsimplify(q2/TT), sp.nsimplify(-calT/TT)))
    return res

for name, mats in (("SD", eta_plus()), ("ASD", eta_minus())):
    omb = mats[2] + sp.Rational(1, 2)*mats[0]*0   # a single (anti-)self-dual constant omega_bar = eta^3 (g0 = 1)
    print(name, " omega_bar = eta^3 ; rows: (V^2, S^2/X, q^2/X, <R>/<X> = -calT/X)")
    for row in run(omb):
        print("   ", row)
omb = 3*eta_plus()[1] + 2*eta_plus()[2]
print("SD, omega_bar = 3 eta^2 + 2 eta^3 (|b|^2=13):")
for row in run(omb):
    print("   ", row)

print("\nPolarisation of the mode-null remainder Z = 2 S^2 - q^2 (= X + 4R on the delta-rho=0 modes):")
def torsion_of_mode(omb, p, u):
    w = omb*u; r = omb*p
    return [[[-r[l]*(p[m]*w[n] - p[n]*w[m]) for n in range(d)] for m in range(d)] for l in range(d)]
def zform(omb, T1, T2):
    Gi = (omb.inv()).T*(omb.inv())
    def up(T):
        return [[[sum(Gi[l, a]*Gi[m, b]*Gi[n, c]*T[a][b][c] for a in range(d) for b in range(d) for c in range(d))
                  for n in range(d)] for m in range(d)] for l in range(d)]
    def parts(T):
        V = [sum(Gi[l, n]*T[l][m][n] for l in range(d) for n in range(d)) for m in range(d)]
        S = [[[sum(sg*T[a][b][c] for (a, b, c), sg in [((l, m, n), 1), ((m, n, l), 1), ((n, l, m), 1), ((m, l, n), -1), ((l, n, m), -1), ((n, m, l), -1)])/6
               for n in range(d)] for m in range(d)] for l in range(d)]
        return V, S
    def ip3(A, B):
        Bu = up(B)
        return sum(A[l][m][n]*Bu[l][m][n] for l in range(d) for m in range(d) for n in range(d))
    V1, S1 = parts(T1); V2, S2 = parts(T2)
    # q = T - vector part - S ; with V=0 for these modes q = T - S
    q1 = [[[T1[l][m][n]-S1[l][m][n] for n in range(d)] for m in range(d)] for l in range(d)]
    q2 = [[[T2[l][m][n]-S2[l][m][n] for n in range(d)] for m in range(d)] for l in range(d)]
    return 2*ip3(S1, S2) - ip3(q1, q2), ip3(T1, T2)
omb = eta_plus()[2]
def mode(seed):
    random.seed(seed)
    while True:
        p = sp.Matrix([rnd() for _ in range(4)])
        v = sp.symbols('v0:4'); u = sp.Matrix(v); w = omb*u; r = omb*p
        vv = [rnd() for _ in range(3)]
        sol = sp.solve(sp.expand((r.T*w)[0]).subs(dict(zip(v[:3], vv))), v[3], dict=True)
        if not sol or p == sp.zeros(4, 1):
            continue
        vals = dict(zip(v[:3], vv)); vals[v[3]] = sol[0][v[3]]
        uu = u.subs(vals)
        T = torsion_of_mode(omb, p, uu)
        if any(T[l][m][n] != 0 for l in range(d) for m in range(d) for n in range(d)):
            return T
for s in range(4):
    T1 = mode(100+s); T2 = mode(200+s)
    z11, x11 = zform(omb, T1, T1); z22, x22 = zform(omb, T2, T2); z12, x12 = zform(omb, T1, T2)
    print(f"  pair {s}: Z(m1,m1)={sp.nsimplify(z11)}, Z(m2,m2)={sp.nsimplify(z22)}  (both 0), cross term Z(m1,m2)={sp.nsimplify(z12)}, X(m1,m2)={sp.nsimplify(x12)}")
