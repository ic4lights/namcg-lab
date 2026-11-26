"""027 script 12: centre flux on ker sigma(Box).  For xi in the 2-plane ker S (covectors annihilating all D^a = J^{a4}, i.e. the nilpotent centre variable zeta), the Zeeman field is
F_ab(xi) = xi(J_ab) and  q_c(xi) := A^2 - B^2 = -K31(xi) = -F_ab F^ab / 2.  Report the two eigenvalues of -K31 restricted to ker S (whitened coordinates |u|^2+|z|^2 normalisation) vs a = y4/ell,
and the electric/magnetic character (A,B) of eta F(xi) on the plane."""
import numpy as np
from cone_window_geometry import *
from flux_window_growth import Fpack, classify
rng = np.random.default_rng(23)
rows = []
for t in range(40):
    z = rand_z_pos(rng, rng.uniform(0.3, 4)); M0 = Mfun(z); y = M0[:5, 5]
    try:
        r = analyse(M0)
    except Exception:
        continue
    T = r['T']; S = r['S']; F = r['F']
    ell2 = -(y @ np.diag([-1., 1, 1, 1, 1]) @ y); a = abs(y[4])/np.sqrt(ell2)
    sw, V = np.linalg.eigh(S); ker = V[:, np.abs(sw) < 1e-8]
    K31 = T.T @ F['C31'] @ T
    qc = np.linalg.eigvalsh(-ker.T @ K31 @ ker)
    _, C = Fpack(M0)
    chars = []
    for th in np.linspace(0, np.pi, 5, endpoint=False):
        xi = T @ (ker @ np.array([np.cos(th), np.sin(th)]))
        A, B, ev = classify(np.einsum('abk,k->ab', C, xi)); chars.append((A, B))
    rows.append((a, qc[0], qc[1], chars))
rows.sort()
print("   a     | eig of q_c = A^2-B^2 on ker S | (A,B) at 5 directions (first two) | a^2-1")
for a, q0, q1, ch in rows[::3]:
    print("%7.3f | %9.5f %9.5f | %s | %8.3f" % (a, q0, q1, np.round(ch[:2], 4).tolist(), a*a - 1))
neg = sum(1 for a, q0, q1, ch in rows if q1 < 0); pos = sum(1 for a, q0, q1, ch in rows if q0 > 0)
print("points with both eigenvalues <0 (magnetic dominated):", sum(1 for a, q0, q1, ch in rows if q1 < 0), " both >0 (electric dominated):", pos, " of", len(rows))
