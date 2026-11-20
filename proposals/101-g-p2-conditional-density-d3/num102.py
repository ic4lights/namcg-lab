# num102.py -- item 101 (replaces num101; adds MC-vs-f check and fixes det import / fan orientation).
# rho_hat(d) = C sum_w eps(w) kw(w.lam-d), C=200/3 (Z=3/200, lam=(.6,.3,.1)); HCIZ Laplace check +
# f(P2)=(1/2)int rho_hat(c+r e(theta))dtheta, r=sqrt(P2-1/3), vs fresh 3M Haar MC (z-scores per bin).
# Run: python -I num102.py
import numpy as np, itertools
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 25
L = [0.6, 0.3, 0.1]
perms = list(itertools.permutations(range(3)))
def sg(p): return -1 if sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) % 2 else 1
def kwf(g1, g2):
    c1, c2 = g1, g1 + g2
    return min(c1, c2) if (c1 > 1e-300 and c2 > 1e-300) else 0.0
def rhoh(d1, d2): return (200.0/3.0) * sum(sg(w) * kwf(L[w[0]] - d1, L[w[1]] - d2) for w in perms)
# HCIZ check with mp det
Lm = [mp.mpf(6)/10, mp.mpf(3)/10, mp.mpf(1)/10]
def lap(s1, s2):
    V = [[mp.mpf(6)/10, mp.mpf(3)/10],[mp.mpf(6)/10, mp.mpf(1)/10],[mp.mpf(3)/10, mp.mpf(1)/10],
         [mp.mpf(1)/10, mp.mpf(3)/10],[mp.mpf(1)/10, mp.mpf(6)/10],[mp.mpf(3)/10, mp.mpf(6)/10]]
    ap = (mp.mpf(1)/3, mp.mpf(1)/3); tot = mp.mpf(0)
    for k in range(6):
        b, c = V[k], V[(k+1) % 6]
        ja = abs((b[0]-ap[0])*(c[1]-b[1]) - (b[1]-ap[1])*(c[0]-b[0]))
        f = lambda ss, tt: float(rhoh(ap[0]+ss*(b[0]-ap[0])+ss*tt*(c[0]-b[0]), ap[1]+ss*(b[1]-ap[1])+ss*tt*(c[1]-b[1]))) \
            * mp.exp(-(s1*(ap[0]+ss*(b[0]-ap[0])+ss*tt*(c[0]-b[0]))+s2*(ap[1]+ss*(b[1]-ap[1])+ss*tt*(c[1]-b[1])))) * ss
        tot += mp.quad(lambda ss: mp.quad(lambda tt: f(ss, tt), [0, 1]), [0, 1]) * ja
    return tot
def hciz(s1, s2):
    a = [-s1, -s2, mp.mpf(0)]
    M = mp.matrix(3, 3, lambda i, j: mp.exp(a[i]*Lm[j]))
    D = lambda v: (v[0]-v[1])*(v[0]-v[2])*(v[1]-v[2])
    return M.det() / (D(a)*D(Lm))
mx = mp.mpf(0)
for (s1, s2) in [(mp.mpf(1)/2, -mp.mpf(1)/3), (mp.mpf(3), mp.mpf(5)), (-mp.mpf(1)/4, mp.mpf(7)/2), (mp.mpf(11)/3, -mp.mpf(2)/7)]:
    A = lap(s1, s2)/lap(mpf0 := mp.mpf(0), mp.mpf(0)); B = hciz(s1, s2)
    r = abs(A-B)/abs(B); mx = max(mx, r); print("rel HCIZ s=(%s,%s): %.2e" % (s1, s2, r))
print("max rel:", mp.nstr(mx, 3), " Z=", mp.nstr(lap(mp.mpf(0), mp.mpf(0)), 12))
# f(P2) vs fresh MC
rng = np.random.default_rng(101202607)
N = 3_000_000
A = (rng.standard_normal((N,3,3)) + 1j*rng.standard_normal((N,3,3)))/np.sqrt(2)
Q, Rr = np.linalg.qr(A); dd = np.diagonal(Rr, axis1=1, axis2=2)
b = np.abs(Q * (dd/np.abs(dd))[:, None, :])**2
P2 = ((b @ np.array(L))**2).sum(1)
th = np.linspace(0, 2*np.pi, 200001)
et = np.stack([np.cos(th), np.sin(th)])
def fexact(P2v):
    r = np.sqrt(max(P2v - 1/3.0, 0.0))
    vals = np.array([rhoh(1/3 + r*et[0][i], 1/3 + r*et[1][i]) for i in range(len(th))])
    return 0.5 * np.trapezoid(vals, th)
print("f(1/3+)= %.6f ; pi*rho(1/3) = %.6f" % (fexact(1/3+1e-12), np.pi*rhoh(1/3, 1/3)))
edges = np.linspace(1/3, 0.46, 27)
hist, _ = np.histogram(P2, bins=edges, density=True)
ctr = 0.5*(edges[1:]+edges[:-1])
fe = np.array([fexact(v) for v in ctr])
var = np.array([fexact(v)*(1/np.diff(edges)[0] - fexact(v)) for v in ctr])  # binom var/dens^2 approx
z = (hist - fe)/np.sqrt(np.maximum(hist, fe)/len(P2)/np.diff(edges)[0])
print("bin ctr mc fexact z:")
print(np.array2string(np.vstack([ctr, hist, fe, z]).T, precision=4, max_line_width=135))
print("max |z| =", np.abs(z).max(), " (N=%d)" % len(P2))
print("done num102")
