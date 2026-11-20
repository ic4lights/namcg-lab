# num103.py -- item 101 (replaces num102: vectorised circle integral; drops unused var line).
# rho_hat(d) = C sum_w eps(w) kw(w.lam-d), C=200/3, lam=(.6,.3,.1). f(P2)=(1/2)oint rho dtheta vs
# fresh 3M Haar MC z-scores; endpoint f(1/3+)=pi*rho(1/3); E[P2] from MC vs (1+sum p^2)/4.
# Run: python -I num103.py
import numpy as np, itertools
L = np.array([0.6, 0.3, 0.1])
perms = list(itertools.permutations(range(3)))
SG = np.array([(-1 if sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) % 2 else 1) for p in perms])
WL = np.array([[L[list(p)] for _ in [0]][0] for p in perms])   # placeholder fixed below
WL = np.array([[L[p[0]], L[p[1]]] for p in perms])
def rho_vec(d1, d2):
    tot = np.zeros(np.broadcast(d1, d2).shape)
    for k in range(6):
        g1 = WL[k,0] - d1; g2 = WL[k,1] - d2
        c1, c2 = g1, g1 + g2
        tot = tot + SG[k] * np.where((c1 > 0) & (c2 > 0), np.minimum(c1, c2), 0.0)
    return (200.0/3.0) * tot
rng = np.random.default_rng(101202607)
N = 3_000_000
A = (rng.standard_normal((N,3,3)) + 1j*rng.standard_normal((N,3,3)))/np.sqrt(2)
Q, Rr = np.linalg.qr(A); dr = np.diagonal(Rr, axis1=1, axis2=2)
b = np.abs(Q * (dr/np.abs(dr))[:, None, :])**2
P2 = ((b @ L)**2).sum(1)
print("E[P2] MC %.6f vs (1+sum p^2)/4 = %.6f  z=%.2f" %
      (P2.mean(), (1+ (L**2).sum())/4, (P2.mean()-(1+(L**2).sum())/4)/(P2.std()/np.sqrt(N))))
th = np.linspace(0, 2*np.pi, 200001)
ct, st = np.cos(th), np.sin(th)
def fexact(P2v):
    r = np.sqrt(max(P2v - 1/3.0, 0.0))
    return 0.5 * np.trapezoid(rho_vec(1/3 + r*ct, 1/3 + r*st), th)
print("f(1/3+)= %.6f ; pi*rho(1/3) = %.6f" % (fexact(1/3+1e-12), np.pi*rho_vec(np.array(1/3), np.array(1/3))))
edges = np.linspace(1/3, 0.46, 27)
hist, _ = np.histogram(P2, bins=edges, density=True)
ctr = 0.5*(edges[1:]+edges[:-1])
fe = np.array([fexact(v) for v in ctr])
z = (hist - fe)/np.sqrt(np.maximum(hist, fe)/N/(edges[1]-edges[0]))
print("bin ctr: mc fexact z")
print(np.array2string(np.vstack([ctr, hist, fe, z]).T, precision=4, max_line_width=135))
print("max |z| = %.2f" % np.abs(z).max())
np.save("fcurve_101.npy", np.vstack([ctr, hist, fe, z]))
print("done num103")
