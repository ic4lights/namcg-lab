#!/usr/bin/env python3
"""Check of the polar a-integral of n2_fourier.py against direct three-dimensional Gauss-Legendre quadrature in at,
at sample W, on contours with complex Q_k, for the specs used later (cos with real and complex zeta, Gaussian
shift, moments).  Writes nothing; print to stdout (saved as check_a_integral.txt)."""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n2_fourier import a_integral, a_integral_zero_exact, Angles, LAM, Ru

def setup(w, eps, alpha, beta):
    w1, w2, w3 = w
    sk = [w2+w3, w1+w3, w1+w2]
    Q = [np.array([np.exp(-2j*alpha)*(eps+1j*LAM*np.exp(2j*beta)*sk[k])]) for k in range(3)]
    pref = np.exp(-2j*alpha+4j*beta)
    Cc = [np.array([pref*w2*w3]), np.array([pref*w1*w3]), np.array([pref*w1*w2])]
    D0 = np.array([np.exp(6j*beta)*w1*w2*w3])
    return Q, Cc, D0

def brute(Q, Cc, D0, spec, n=120, L=None):
    Qs = [q[0] for q in Q]
    if L is None:
        L = 7.0/np.sqrt(min(np.real(q) for q in Qs))
    x, wx = np.polynomial.legendre.leggauss(n); g = L*x; wg = L*wx
    A1, A2, A3 = np.meshgrid(g, g, g, indexing='ij')
    WW = wg[:, None, None]*wg[None, :, None]*wg[None, None, :]
    r = np.sqrt(A1**2+A2**2+A3**2)
    base = np.exp(-Qs[0]*A1**2-Qs[1]*A2**2-Qs[2]*A3**2)*(D0[0]-Cc[0][0]*A1**2-Cc[1][0]*A2**2-Cc[2][0]*A3**2)**4
    if spec[0] == 'mom':
        f = 2*r**(2*spec[1])
    else:
        f = 2*np.cos(spec[1]*r)*np.exp(-spec[2]*r**2)
    return np.sum(WW*base*f)

if __name__ == "__main__":
    import sys as _s
    angp = (64, 12)
    ang = Angles(*angp)
    print('angular rule (n_logtheta, n_phi) =', angp)
    cases = [((0.7, 1.3, 2.9), 0.0, *Ru(1.0)), ((0.7, 1.3, 2.9), 0.2, *Ru(0.6)), ((0.05, 0.4, 3.0), 0.0, *Ru(0.8)),
             ((0.05, 0.4, 3.0), 0.1, 0.5, 0.1)]
    for (w, eps, al, be) in cases:
        Q, Cc, D0 = setup(sorted(w, reverse=True), eps, al, be)
        specs = [('cos', 0, 0), ('cos', 0.6, 0), ('cos', 1.0*np.exp(-0.2j), 0), ('cos', 0.8*np.exp(-1j*al), 0.05*np.exp(-2j*al)),
                 ('mom', 1), ('mom', 3)]
        fast = a_integral(Q, Cc, D0, specs, ang)[:, 0]
        print(f"w={w} eps={eps} alpha={al:.4f} beta={be:.4f}  exact-moment Z: {a_integral_zero_exact(Q, Cc, D0)[0]:.10e}")
        for sp, fv in zip(specs, fast):
            bv = brute(Q, Cc, D0, sp)
            print(f"   {str(sp):60s} polar {fv:.10e}  direct {bv:.10e}  rel.diff {abs(fv-bv)/abs(bv):.1e}")
