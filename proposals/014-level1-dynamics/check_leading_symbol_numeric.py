"""
Numerical check on the explicit CP^{1,2} realisation (proposals/013 cp12_realisation.py) that the linearised EOM operator
  L(A)_a = -{T^b,{T_b,A_a}} - {T^b,{A_b,T_a}} - {A^b,{T_b,T_a}} + mu^2 A_a ,  mu^2 = -3
acting on A^a = c^a e^{i lam q.y} F  (y^mu = M^{mu5}, F = a first-harmonic fibre function, here M^{12}) has the leading symbol
  L_a ~ lam^2 m^2 F e^{i lam q.y} (q^2 c_a - q_a q.c),   m = M^{45}
(the Maxwell operator, pointwise in the fibre), with remainder O(lam).  Brackets are evaluated with the ambient Lie-Poisson bracket
(sympy derivatives in the 15 variables M^{AB}), then evaluated at an orbit point z.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '013-cp12-einstein-rank'))
import numpy as np, sympy as sp
import cp12_realisation as R

# sign convention: PB(A,B,C,D,z) = s * lie(...)
rng = np.random.default_rng(5)
z = R.rand_z_pos(rng)
Mz = R.Mfun(z)
chk = []
for (A, B, C, D) in [(0, 4, 1, 4), (0, 4, 0, 5), (1, 2, 2, 4), (3, 4, 0, 5)]:
    p = R.PB(A, B, C, D, z); l = R.lie(A, B, C, D, Mz)
    chk.append(p/l if abs(l) > 1e-9 else None)
print("PB/lie ratios (s):", chk)
s = int(round(np.median([c for c in chk if c is not None])))
print("s =", s)
eta6 = [-1, 1, 1, 1, 1, -1]; e4 = [-1, 1, 1, 1]
pairs = [(A, B) for A in range(6) for B in range(A+1, 6)]
Ms = {p: sp.Symbol('M%d%d' % p) for p in pairs}
def M(A, B):
    if A == B: return 0
    return Ms[(A, B)] if A < B else -Ms[(B, A)]
def lie(A, B, C, D):
    e = lambda X, Y: eta6[X] if X == Y else 0
    return s*(e(A, C)*M(B, D) - e(A, D)*M(B, C) - e(B, C)*M(A, D) + e(B, D)*M(A, C))
brM = {(p, r): sp.expand(lie(p[0], p[1], r[0], r[1])) for p in pairs for r in pairs}
def PB(f, g):
    out = 0
    df = {p: sp.diff(f, Ms[p]) for p in pairs}; dg = {p: sp.diff(g, Ms[p]) for p in pairs}
    for p in pairs:
        if df[p] == 0: continue
        for r in pairs:
            if dg[r] == 0: continue
            out += df[p]*dg[r]*brM[(p, r)]
    return out
lam = sp.Symbol('lam')
qv = [sp.Rational(3, 10), sp.Rational(-2, 10), sp.Rational(5, 10), sp.Rational(1, 10)]     # q_mu (lower)
cv = [sp.Rational(1, 3), sp.Rational(-1, 2), sp.Rational(2, 7), sp.Rational(1, 5)]          # c^a (upper)
phi = sum(qv[m]*M(m, 5) for m in range(4))
F = M(1, 2)
T = [M(a, 4) for a in range(4)]; Tl = [e4[a]*T[a] for a in range(4)]
Aup = [cv[a]*sp.exp(sp.I*lam*phi)*F for a in range(4)]; Alo = [e4[a]*Aup[a] for a in range(4)]
mu2 = -3
vals = {Ms[p]: Mz[p[0], p[1]] for p in pairs}
q2 = sum(e4[a]*(e4[a]*qv[a])*0 for a in range(4))
qup = [e4[a]*qv[a] for a in range(4)]
q2 = sum(qv[a]*qup[a] for a in range(4)); qc = sum(qv[a]*cv[a] for a in range(4))
m = Mz[4, 5]
def Lcomp(a):
    L = -sum(e4[b]*PB(T[b], PB(T[b], Alo[a])) for b in range(4))
    L -= sum(PB(T[b], PB(Alo[b], Tl[a])) for b in range(4))
    L -= sum(PB(Aup[b], PB(Tl[b], Tl[a])) for b in range(4))
    L += mu2*Alo[a]
    return L
Ls = [Lcomp(a) for a in range(4)]
Fz = float(F.subs(vals)) if hasattr(F, 'subs') else Mz[1, 2]
phiz = float(phi.subs(vals))
print("m = M^45 =", m, " F =", Fz, " phi =", phiz, " q^2 =", float(q2), " q.c =", float(qc))
for lv in (10., 30., 100., 300., 1000.):
    row = []
    for a in range(4):
        val = complex(Ls[a].subs(vals).subs(lam, lv).evalf())
        pred = lv**2*m**2*Fz*np.exp(1j*lv*phiz)*(float(q2)*float(e4[a]*cv[a]) - float(qv[a])*float(qc))
        row.append(abs(val - pred)/abs(lv**2*m**2*Fz))
    print("lam=%7.0f  |L - lam^2 m^2 F e (q^2 c_a - q_a q.c)| / (lam^2 m^2 |F|) per component:" % lv, ["%.3e" % r for r in row])
