"""
Tangent space T of the Theta-built metrics {G = (Theta^T eta Theta)^{-1}} at a constant background Theta-bar (6-dim inside the 10-dim
space of symmetric tensors) versus the pure-gauge perturbations S_p = { p_mu xi_nu + p_nu xi_mu } of a plane wave of momentum p.
dim(T cap S_p) = 6 + 4 - rank[T | S_p].   Also: T cap S_p for G^{-1}-type variables gives the same dimension (checked by using K).
Usage: python check_class_vs_diffeo.py
"""
import sympy as sp, random, itertools
random.seed(2)
th = sp.symbols('t01 t02 t03 t12 t13 t23')
def build(s0, vals):
    eta = sp.diag(s0, 1, 1, 1)
    T = sp.Matrix([[0, th[0], th[1], th[2]], [-th[0], 0, th[3], th[4]], [-th[1], -th[3], 0, th[5]], [-th[2], -th[4], -th[5], 0]])
    Kinv = (T.T*eta*T).inv()
    iu = [(i, j) for i in range(4) for j in range(i, 4)]
    vec = sp.Matrix([Kinv[i, j] for (i, j) in iu])
    Jm = vec.jacobian(sp.Matrix(th)).subs(dict(zip(th, vals)))
    return Jm, iu, Kinv.subs(dict(zip(th, vals)))
for s0 in (-1, 1):
    for vals in ([1, 0, 0, 0, 0, 1], [1, 2, -1, 3, 2, 5]):
        vals = [sp.Rational(v) for v in vals]
        Jm, iu, Gbar = build(s0, vals)
        ranks = []
        for _ in range(6):
            p = [sp.Rational(random.randint(-5, 5), 1) for _ in range(4)]
            if all(v == 0 for v in p): continue
            cols = []
            for k in range(4):
                xi = [0]*4; xi[k] = 1
                cols.append(sp.Matrix([ (p[i]*xi[j] + p[j]*xi[i]) for (i, j) in iu]))
            S = sp.Matrix.hstack(*cols)
            r = sp.Matrix.hstack(Jm, S).rank()
            ranks.append(6 + 4 - r)
        print("eta s0=%d, Theta-bar comps %s: rank(T)=%d, dim(T cap S_p) for random p:" % (s0, [str(v) for v in vals], Jm.rank()), ranks)
