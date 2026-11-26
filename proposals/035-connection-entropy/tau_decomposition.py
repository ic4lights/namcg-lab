"""B-R3 data: fit  tau_Omega = a W + b R_Sigma + c R + d X' + f e  over the 20 exact points of 033 data.json
(pointwise exact rationals; families: 029 SD example, rotation-invariant SD, non-SD J=0, non-SD J!=0, generic closed omega).
Also test tau - X'/2 = R_Sigma - 2W - R/3 (LC value) and the Euler-type combination."""
import json, sympy as sp
d = json.load(open('data.json'))
f = lambda r, k: sp.Rational(r[k])
unk = sp.symbols('a b c d f')
rows = []; rhs = []
for r in d:
    rows.append([f(r,'W'), f(r,'Rsig'), f(r,'R'), f(r,'Xp'), f(r,'e')]); rhs.append(f(r,'tau'))
M = sp.Matrix(rows); y = sp.Matrix(rhs)
print('rank M', M.rank(), 'rank [M|y]', M.row_join(y).rank())
sol = sp.linsolve((M, y), *unk)
print('tau = a W + b Rsig + c R + d Xp + f e :', sol)
for name, sel in (('all', range(len(d))), ('tg only', [i for i,r in enumerate(d) if r.get('sigma_tg')])):
    idx = list(sel)
    M2 = sp.Matrix([rows[i] for i in idx]); y2 = sp.Matrix([rhs[i] for i in idx])
    print(name, len(idx), 'pts rank', M2.rank(), M2.row_join(y2).rank(), sp.linsolve((M2, y2), *unk))
# individual hypotheses
for i, r in enumerate(d):
    W, Rs, R, X, e, tau = (f(r,k) for k in ('W','Rsig','R','Xp','e','tau'))
    print(i, r['family'][:22].ljust(22), 'tau-Rsig+2W+R/3 =', sp.nsimplify(tau-Rs+2*W+R/3), ' X\'/2 =', X/2, ' e-R/6 =', e-R/6, ' tau - X\'/2 - Rsig =', tau-X/2-Rs)
