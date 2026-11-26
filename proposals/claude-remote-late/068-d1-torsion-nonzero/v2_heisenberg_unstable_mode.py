"""V2. Exact unstable mode on the Heisenberg torsion background [E_3, E_1] = kappa E_2.

Coordinates as in v1: E_0 = d0, E_1 = d1 + (kappa y3/2) d2, E_2 = d2, E_3 = d3 - (kappa y1/2) d2,
right-invariant rho_1 = d1 - (kappa y3/2) d2, rho_3 = d3 + (kappa y1/2) d2, rho_0 = d0, rho_2 = d2.
Mode: phi = exp(i q0 y0 + i p y2 - kappa p (y1^2 + y3^2)/4), p > 0 (lowest Landau level of the
sector E_2 = i p), A = (0, phi, 0, i phi).
Checks (exact, sympy):
  (U1) Mz[A] = (q0^2 - p^2 + kappa p) * (0, phi, 0, i phi) for the contraction eta, so Mz[A] = 0 iff
       q0^2 = p (p - kappa);  F[A] != 0 (not pure gauge).
  (U2) For each right-invariant label J, the frame fluctuation h with f_b^I = A_b delta^I_J
       (h = -f Ainv) solves the linearised first two brackets (B1 = B2 = 0, w = 0) at that q0,
       and has nonzero linearised torsion.
  (U3) Growth rate Gamma(p) = sqrt(p (kappa - p)) on 0 < p < kappa, maximum kappa/2 at p = kappa/2.
  (U4) Contraction delta: Mz[A] = -(q0^2 + p^2 - kappa p) A on the same A, zero at real q0^2 = p(kappa - p).
Run: python -I v2_heisenberg_unstable_mode.py   (needs v1_reduction_symbolic.py in the same folder)
"""
import os
import sys
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v1_reduction_symbolic as v1   # noqa: E402

Y, kap, R4 = v1.Y, v1.kap, v1.R4
y0, y1, y2, y3 = Y
p, q0 = sp.symbols('p q0', positive=True)
E, Rr = v1.BGS['Heisenberg']
c = v1.struct(E)
ETA = v1.ETA
DELTA = [[1 if i == j else 0 for j in R4] for i in R4]

phi = sp.exp(sp.I * q0 * y0 + sp.I * p * y2 - kap * p * (y1 ** 2 + y3 ** 2) / 4)
A = [0, phi, 0, sp.I * phi]
lam = q0 ** 2 - p ** 2 + kap * p
M = v1.Mz(E, c, ETA, A)
u1 = all(sp.simplify(M[b] - lam * A[b]) == 0 for b in R4)
F = [[sp.simplify(v1.apply(E[a], A[b]) - v1.apply(E[b], A[a]) - sum(c[a][b][d] * A[d] for d in R4)) for b in R4] for a in R4]
print('(U1) Mz[A] = (q0^2 - p^2 + kappa p) A :', u1, '; F_32 / phi =', sp.simplify(F[3][2] / phi),
      '; F_01 / phi =', sp.simplify(F[0][1] / phi))

root = sp.sqrt(p * (p - kap))           # q0 at the root (imaginary for 0 < p < kappa)
Am = v1.frame_in_rho(E, Rr)
Ainv = sp.simplify(Am.inv())
zero_w = [[[0] * 4 for _ in R4] for _ in R4]
for J in R4:
    f = [[A[b] if I == J else 0 for I in R4] for b in R4]
    h = [[sp.expand(-sum(f[b][I] * Ainv[I, cc] for I in R4)) for cc in R4] for b in R4]
    B1, B2 = v1.brackets_lin(E, c, ETA, h, zero_w)
    B1r = [[sp.simplify((B1[b][e] / sp.exp(sp.I * q0 * y0)).subs(q0, root)) for e in R4] for b in R4]
    ok = all(x == 0 for row in B1r for x in row) and all(sp.simplify(B2[b][d][e]) == 0 for b in R4 for d in R4 for e in R4)
    # linearised torsion of the mode: -dC (w = 0)
    dT = [[[sp.simplify(-(sum(c[a][b][ff] * h[ff][d] for ff in R4) - v1.apply(E[a], h[b][d]) + v1.apply(E[b], h[a][d])
                         - sum(h[b][x] * c[a][x][d] for x in R4) + sum(h[a][x] * c[b][x][d] for x in R4)))
            for d in R4] for b in R4] for a in R4]
    nonzero_T = any(x != 0 for a in R4 for b in R4 for x in dT[a][b])
    print('(U2) label J = %d: B1 = B2 = 0 at q0^2 = p(p - kappa):' % J, ok, '; linearised torsion nonzero:', nonzero_T)

G = sp.sqrt(p * (kap - p))
pm = sp.solve(sp.diff(G ** 2, p), p)
print('(U3) Gamma^2 = p(kappa - p); stationary point p =', pm, '; Gamma there =', sp.simplify(G.subs(p, pm[0])))

Md = v1.Mz(E, c, DELTA, A)
u4 = all(sp.simplify(Md[b] + (q0 ** 2 + p ** 2 - kap * p) * A[b]) == 0 for b in R4)
print('(U4) delta contraction: Mz[A] = -(q0^2 + p^2 - kappa p) A :', u4)
