# num104b.py -- item 101 (num104 with bin-AVERAGE exact density, not bin-center: near the P2 endpoint
# f decays quadratically in (0.46-P2), so center-evaluation biases the last bins and inflated z there;
# a 24-midpoint average of fexact over each bin removes the bias. Same ellipse coarea and fresh MC.
# Run: python -I num104b.py
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
th = np.linspace(0, 2*np.pi, 200001)
ct, st = np.cos(th), np.sin(th)
def fexact(P2v):
    s = np.sqrt(max(P2v - 1/3.0, 0.0))
    a = s*ct/np.sqrt(3.0); b = s*st
    dx = (a+b)/np.sqrt(2.0); dy = (a-b)/np.sqrt(2.0)
    return np.trapezoid(rho_vec(1/3 + dx, 1/3 + dy), th)/(2*np.sqrt(3.0))
def favg(lo, hi, m=24):
    return np.mean([fexact(lo + (i+0.5)*(hi-lo)/m) for i in range(m)])
rng = np.random.default_rng(101202611)
N = 3_000_000
A = (rng.standard_normal((N,3,3)) + 1j*rng.standard_normal((N,3,3)))/np.sqrt(2)
Q, Rr = np.linalg.qr(A); dr = np.diagonal(Rr, axis1=1, axis2=2)
b = np.abs(Q * (dr/np.abs(dr))[:, None, :])**2
P2 = ((b @ L)**2).sum(1)
edges = np.unique(np.concatenate([np.linspace(1/3, 0.34, 10), np.linspace(0.34, 0.46, 13), [0.4585, 0.4595, 0.46]]))
cnt, _ = np.histogram(P2, bins=edges)
dw = np.diff(edges); hist = cnt/(N*dw)
ctr = 0.5*(edges[1:]+edges[:-1])
fa = np.array([favg(e0, e1) for e0, e1 in zip(edges[:-1], edges[1:])])
z = (hist - fa)/np.sqrt(np.maximum(hist, fa)/(N*dw))
print("ctr    counts   mc-hist   exact-bin-avg   z")
print(np.array2string(np.vstack([ctr, cnt, hist, fa, z]).T, precision=4, max_line_width=135, suppress_small=True))
print("max |z| = %.2f ;  endpoint tail f(0.455)=%.4e f(0.4599)=%.4e (quadratic in 0.46-P2?)" %
      (np.abs(z).max(), fexact(0.455), fexact(0.45999)))
np.save("fcurve_101d.npy", np.vstack([ctr, hist, fa, z, cnt]))
print("done num104b")
