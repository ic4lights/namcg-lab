"""
s1: operator identities on the bundle of Lorentz frames, exact at rational points.

For each frame (e, w = Levi-Civita connection):
 (i)  [S_cd, D_a] = eta_{ad} D_c - eta_{ac} D_d   and  [S,S] closes,
 (ii) [D_a, D_b] has no D component (torsion zero) and equals (1/2) R_ab^{cd} S_cd,
 (iii) [D^a,[D_a,D_b]] = -Ric_b^e D_e + (S part), with Ric computed independently from w,
       the coefficient of S being (1/2) nabla^a R_ab^{cd}.
Backgrounds: pp-wave (Ricci flat and not), Schwarzschild, Kasner, de Sitter (conformal chart), S^2 x R^2.
Run from any directory: only bundlelib next to this file is needed.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from bundlelib import *

d = 4
B = Bundle(d)
y = B.y
eta = B.eta




def frame_from_coframe(th):
    # th[mu, b]; returns e[b][mu] with e_b^mu th_mu^c = delta
    return th.inv().tolist()


cases = {}
U, Vv, x, z = y
Hrf = (x**2 - z**2)*(1 + U)
Hnr = (x**2 + z**2)*(1 + U)
for name, H, pt in [('ppwave_ricci_flat', Hrf, {U: sp.Rational(1, 3), Vv: 2, x: sp.Rational(3, 2), z: sp.Rational(5, 7)}),
                    ('ppwave_not_flat', Hnr, {U: sp.Rational(1, 3), Vv: 2, x: sp.Rational(3, 2), z: sp.Rational(5, 7)})]:
    th = sp.Matrix([[(1-H)/2, (1+H)/2, 0, 0], [-sp.Rational(1, 2), sp.Rational(1, 2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cases[name] = (frame_from_coframe(th), pt)

# Schwarzschild, coordinates (t, r, X = cos theta, phi), M = 1
t, r, X, ph = y
f = 1 - 2/r
e = [[1/sp.sqrt(f), 0, 0, 0], [0, sp.sqrt(f), 0, 0], [0, 0, sp.sqrt(1-X**2)/r, 0], [0, 0, 0, 1/(r*sp.sqrt(1-X**2))]]
cases['schwarzschild'] = (e, {t: 1, r: sp.Rational(8, 3), X: sp.Rational(3, 5), ph: 1})

# Kasner p = (-1/3, 2/3, 2/3), written with t = s^3 so that every entry is rational in s
s = y[0]
# ds^2 = -dt^2 + s^-2 dx1^2 + s^4 (dx2^2+dx3^2), t = s^3, dt = 3 s^2 ds
e = [[1/(3*s**2), 0, 0, 0], [0, s, 0, 0], [0, 0, s**-2, 0], [0, 0, 0, s**-2]]
cases['kasner'] = (e, {y[0]: sp.Rational(3, 2), y[1]: 1, y[2]: 2, y[3]: 3})

# de Sitter, conformal chart ds^2 = (-dT^2 + dx^2)/T^2
T0 = y[0]
e = [[T0 if i == j else 0 for j in range(4)] for i in range(4)]
cases['de_sitter'] = (e, {y[0]: sp.Rational(3, 2), y[1]: 1, y[2]: 2, y[3]: 3})

# S^2 x R^2 : (T, x, X=cos theta, phi)
X = y[2]
e = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, sp.sqrt(1-X**2), 0], [0, 0, 0, 1/sp.sqrt(1-X**2)]]
cases['S2xR2'] = (e, {y[0]: 1, y[1]: 2, y[2]: sp.Rational(3, 5), y[3]: 1})

# a rational Lorentz matrix for the point on the fibre
L = rational_boost(4, 1, 1, 3)*rational_rotation(4, 1, 2, 1, 2)*rational_boost(4, 3, 1, 2)*rational_rotation(4, 2, 3, 2, 3)
assert (L*eta*L.T - eta) == sp.zeros(4, 4)
fib = {B.u[a][b]: L[a, b] for a in range(4) for b in range(4)}

print('# s1 operator identities. Exact rational evaluation at one point of the bundle for each background.')
for name, (e, pt) in cases.items():
    t0 = time.time()
    w, th = levi_civita_connection(e, y, eta)
    bad, anti = check_torsion_free(w, th, y, eta)
    R, Ric = ricci_flat_index(e, w, th, y, eta)
    D = B.horizontal(e, w)
    S = B.vertical()
    point = dict(pt); point.update(fib)
    # (i)
    ok1 = True
    for (c, f_), Sv in S.items():
        for a in range(4):
            lhs = B.comm(Sv, D[a])
            rhs = [eta[a, f_]*D[c][k] - eta[a, c]*D[f_][k] for k in range(B.N)]
            if any(sp.simplify((lhs[k]-rhs[k]).subs(point)) != 0 for k in range(B.N)):
                ok1 = False
    # (ii), (iii)
    Fab = {}
    tors = 0
    for a in range(4):
        for b in range(a+1, 4):
            Fab[(a, b)] = B.comm(D[a], D[b])
            al, be = B.decompose([sp.nsimplify(v) if v == 0 else v for v in Fab[(a, b)]], D, S, point)
            if any(sp.simplify(v) != 0 for v in al):
                tors += 1
    def F(a, b):
        if a == b:
            return [sp.S.Zero]*B.N
        if a < b:
            return Fab[(a, b)]
        return [-v for v in Fab[(b, a)]]
    # Ricci at the point of the fibre: Ric_{(a)(b)} = L_a^c L_b^d Ric_cd
    Ric_pt = sp.simplify((L*Ric*L.T).subs(pt))
    res = []
    for b in range(4):
        V = [sp.S.Zero]*B.N
        for a in range(4):
            cc = B.comm(D[a], F(a, b))
            for k in range(B.N):
                V[k] += eta[a, a]*cc[k]
        al, be = B.decompose(V, D, S, point)
        # alpha^e D_e with lower-index D_e: compare with -Ric_b^e = -Ric_{b f} eta^{f e}
        expected = [-Ric_pt[b, g]*eta[g, g] for g in range(4)]
        diff = [sp.simplify(al[g]-expected[g]) for g in range(4)]
        res.append((all(v == 0 for v in diff), all(sp.simplify(v) == 0 for v in be.values())))
    ric_flat = all(sp.simplify(v) == 0 for v in Ric_pt)
    print(f'{name:20s} torsion-free(bad={bad},anti={anti}) [S,D]rule={ok1} D-part of [D,D] nonzero in {tors} pairs; '
          f'Ric=0:{ric_flat}; [D^a,[D_a,D_b]]=-Ric_b^e D_e for all b:{all(r[0] for r in res)}; S-part zero for all b:{all(r[1] for r in res)}; '
          f'Ric_flat_diag(section u=1)={[sp.nsimplify(sp.simplify(Ric[i,i].subs(pt))) for i in range(4)]}; {time.time()-t0:.1f}s', flush=True)
