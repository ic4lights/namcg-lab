"""027 script 13: closed forms for the Zeeman field F_ab(xi) = xi(J_ab) (whitened unit covectors), a = y4/ell, at 40 random orbit points:
 centre plane (xi in ker sigma(Box)):   A_c^2 = 1/(2(1+2a^2)),  B_c^2 = a^2/(2(1+2a^2)),  A_c^2-B_c^2 = (1-a^2)/(2(1+2a^2));
 vertical pencil plane:                 A_v^2 = a^2/2,   B_v^2 = 1/2 ;
 base plane (invariant-sector momenta): B = 0,  max_dir A_b^2 = (1+a^2)/2 (A_b = |xi ^ y|-type boost rate)."""
import numpy as np
from cone_window_geometry import *
from flux_window_growth import Fpack, classify
rng = np.random.default_rng(31)
dev = np.zeros(5); n = 0
for t in range(60):
    z = rand_z_pos(rng, rng.uniform(0.3, 4)); M0 = Mfun(z); y = M0[:5, 5]
    try: r = analyse(M0)
    except Exception: continue
    T, S = r['T'], r['S']; _, C = Fpack(M0)
    ell2 = -(y @ np.diag([-1., 1, 1, 1, 1]) @ y); a = abs(y[4])/np.sqrt(ell2); u = a*a
    sw, V = np.linalg.eigh(S); ker = V[:, np.abs(sw) < 1e-8]
    vals = []
    for th in np.linspace(0, np.pi, 7, endpoint=False):
        xi = T @ (ker @ np.array([np.cos(th), np.sin(th)])); A, B, _ = classify(np.einsum('abk,k->ab', C, xi)); vals.append((A, B))
    dev[0] = max(dev[0], max(abs(A**2 - 1/(2*(1 + 2*u))) for A, B in vals)); dev[1] = max(dev[1], max(abs(B**2 - u/(2*(1 + 2*u))) for A, B in vals))
    vv = []
    for th in np.linspace(0, np.pi, 7, endpoint=False):
        xi = T @ np.concatenate([np.zeros(4), [np.cos(th), np.sin(th)]]); A, B, _ = classify(np.einsum('abk,k->ab', C, xi)); vv.append((A, B))
    dev[2] = max(dev[2], max(abs(A**2 - u/2) + abs(B**2 - 0.5) for A, B in vv))
    amax = 0; bmax = 0
    for k in range(3000):
        v = rng.normal(size=4); v /= np.linalg.norm(v); xi = T @ np.concatenate([v, [0, 0]]); A, B, _ = classify(np.einsum('abk,k->ab', C, xi)); amax = max(amax, A); bmax = max(bmax, B)
    dev[3] = max(dev[3], abs(amax**2 - (1 + u)/2)); dev[4] = max(dev[4], bmax)
    n += 1
print("points:", n, "| max |A_c^2 - formula| %.1e | max |B_c^2 - formula| %.1e | vertical-plane deviation %.1e | |max_dir A_b^2 - (1+a^2)/2| (3000 dirs) %.1e | max B on base %.1e" % tuple(dev))
