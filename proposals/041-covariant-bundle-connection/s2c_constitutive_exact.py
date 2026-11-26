"""s2c: exact (rational) verification of s2: Hessian of L(omega) = |Pf omega| eta_ac eta_bd Theta^{ab} Theta^{cd} at rational points equals
2*Maxwell_G + b*Axion with b = -sgn(Pf Theta) I1/8 exactly (sympy, no finite differences)."""
import sympy as sp, itertools, random
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
w = sp.symbols('w0:6')
W = sp.zeros(4, 4)
for v, (i, j) in zip(w, pairs):
    W[i, j] = v; W[j, i] = -v
Pf = W[0, 1]*W[2, 3] - W[0, 2]*W[1, 3] + W[0, 3]*W[1, 2]
Th = W.inv()
def lc(a, b, c, d):
    return sp.LeviCivita(a, b, c, d)
random.seed(2)
for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    eta = sp.diag(*etad)
    I1 = sum(eta[a, c]*eta[b, d]*Th[a, b]*Th[c, d] for a in range(4) for b in range(4) for c in range(4) for d in range(4))
    for trial in range(3):
        pt = {v: sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for v in w}
        pf0 = Pf.subs(pt)
        if pf0 == 0: continue
        s = sp.sign(pf0)
        L = s*Pf*I1                         # |Pf| = s*Pf near the point
        H = sp.Matrix(6, 6, lambda i, j: sp.diff(L, w[i], w[j]).subs(pt))
        W0 = W.subs(pt); Th0 = W0.inv(); K = Th0.T*eta*Th0        # K^{mu nu} = eta_ab Th^{a mu} Th^{b nu}
        rho = abs(pf0)
        Mx = sp.Matrix(6, 6, lambda I, Jx: 2*rho*(K[pairs[I][0], pairs[Jx][0]]*K[pairs[I][1], pairs[Jx][1]] - K[pairs[I][0], pairs[Jx][1]]*K[pairs[I][1], pairs[Jx][0]]))
        Ax = sp.Matrix(6, 6, lambda I, Jx: 8*lc(*pairs[I], *pairs[Jx]))
        PfTh = (Th0[0, 1]*Th0[2, 3] - Th0[0, 2]*Th0[1, 3] + Th0[0, 3]*Th0[1, 2])
        b = -sp.sign(PfTh)*I1.subs(pt)/8
        diff = sp.simplify(H - 2*Mx - b*Ax)
        print(f'eta={etad} trial {trial}: Pf={pf0}, I1={I1.subs(pt)}, b={b};  H - 2 Mx - b Ax == 0 : {diff == sp.zeros(6, 6)}')
