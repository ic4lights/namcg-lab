# num104.py -- item 101 (replaces num103: level sets of P2 are ELLIPSES in (d1,d2), not circles;
# P2 = 1/3 + 3a^2 + b^2 in eigen-coords a=(dx+dy)/sqrt2, b=(dx-dy)/sqrt2. Coarea with the exact
# Jacobian gives f(P2) = (1/(2*sqrt3)) * int_0^2pi rho_hat(c + ellipse(theta)) dtheta; endpoint
# f(1/3+) = pi*rho_hat(c)/sqrt3. Checked against fresh 3M-sample Haar MC z-scores per bin.
# Run: python -I num104.py
import numpy as np, itertools
L = np.array([0.6, 0.3, 0.1])
perms = list(itertools.permutations(range(3)))
SG = np.array([-1 if sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) % 2 else 1 for p in perms])
WL = np.array([[L[p[0]], L[p[1]]] for p in perms])
def rho_vec(d1, d2):
    tot = np.zeros(np.broadcast(d1, d2).shape)
    for k in range(6):
        g1 = WL[k,0] - d1; g2 = WL[k,1] - d2
        tot = tot + SG[k] * np.where((g1 > 0) & (g1 + g2 > 0), np.minimum(g1, g1 + g2), 0.0)
    return (200.0/3.0) * tot
th = np.linspace(0, 2*np.pi, 400001)
ct, st = np.cos(th), np.sin(th)
def fexact(P2v):
    s = np.sqrt(max(P2v - 1/3.0, 0.0))
    a = s*ct/np.sqrt(3.0); b = s*st
    dx = (a+b)/np.sqrt(2.0); dy = (a-b)/np.sqrt(2.0)
    return np.trapezoid(rho_vec(1/3 + dx, 1/3 + dy), th)/(2*np.sqrt(3.0))
print("f(1/3+) = %.6f ;  pi*rho(c)/sqrt3 = %.6f ;  rho(c) = %.6f" %
      (fexact(1/3+1e-12), np.pi*rho_vec(np.array(1/3), np.array(1/3))/np.sqrt(3), rho_vec(np.array(1/3), np.array(1/3))))
for q in (0.34, 0.4599999):
    print("f(%.4f) = %.6f" % (q, fexact(q)))
rng = np.random.default_rng(101202611)
N = 3_000_000
A = (rng.standard_normal((N,3,3)) + 1j*rng.standard_normal((N,3,3)))/np.sqrt(2)
Q, Rr = np.linalg.qr(A); dr = np.diagonal(Rr, axis1=1, axis2=2)
b = np.abs(Q * (dr/np.abs(dr))[:, None, :])**2
P2 = ((b @ L)**2).sum(1)
print("E[P2] MC %.6f+-%.6f vs exact (1+sum p^2)/4 = %.6f" % (P2.mean(), P2.std()/np.sqrt(N), 0.365))
edges = np.unique(np.concatenate([np.linspace(1/3, 0.34, 10), np.linspace(0.34, 0.46, 13), [0.4585, 0.4595, 0.46]]))
hist, _ = np.histogram(P2, bins=edges, density=True)
ctr = 0.5*(edges[1:]+edges[:-1]); dw = np.diff(edges)
fe = np.array([fexact(v) for v in ctr])
z = (hist - fe)/np.sqrt(np.maximum(hist, fe)/(N*dw))
print("bin ctr: mc fexact z")
print(np.array2string(np.vstack([ctr, hist, fe, z]).T, precision=4, max_line_width=135))
print("max |z| = %.2f" % np.abs(z).max())
np.save("fcurve_101c.npy", np.vstack([ctr, hist, fe, z]))
print("done num104")
