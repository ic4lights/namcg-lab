"""030 script 4 (library): Gaussian moments, geometry of the frozen sector at an orbit point of CP^{1,2}, and the weight-2 integrand K(s).
Frozen-sector data at an orbit point M0 and a covector q (phi = q_mu y^mu):
  W_a (a=0..3): Hamiltonian field of T^a in tangent coordinates (4x6);  Y = q_mu Ham(y^mu) (6);  P = -sigma(Delta_{3/4}) (6x6, window exp(-xi^T P xi));
  kappa_a = W_a(phi) = <dphi, W_a>;  G0 = sum_a eta_a W_a W_a^T.
Integrand (Lorentzian, proper time s real, branch of det^{-1/2} by continuity from s=0):
  K(s) = (4 pi)^-3 det(P + i s G0)^(-1/2)  *  sum_n  i^n s^(n-1)/(n-1)!  < P_n(o, zeta) >,    o_a = xi.W_a, zeta = xi.Y,
with <.> the Gaussian average with weight exp(-xi^T (P + i s G0) xi) normalised to one (covariance (P+isG0)^-1/2)."""
import numpy as np, mpmath as mp, sympy as sp, pickle, functools, itertools
from geom28 import *
mp.mp.dps = 50
eta_a = np.array([-1., 1, 1, 1])

def frozen_data(M0, q):
    Pi, W, Yb, c, E = fields(M0)
    wf = window_forms(M0)
    P = wf['P']
    Y = sum(q[m] * Yb[m] for m in range(4))
    dphi = sum(q[m] * E[:, pidx[(m, 5)]] for m in range(4))
    kappa = np.array([dphi @ W[a] for a in range(4)])
    return dict(W=W, Y=Y, P=P, kappa=kappa, dphi=dphi, E=E, c=c, Yb=Yb, wf=wf)

class Gauss:
    """Gaussian with weight exp(-xi^T B xi), B = P + i s G0; linear forms L (rows)."""
    def __init__(self, P, G0, L, s):
        n = P.shape[0]
        Pm = mp.matrix(P.tolist()); Gm = mp.matrix(G0.tolist())
        B = Pm + 1j * s * Gm
        self.Binv = mp.inverse(B)
        Lm = mp.matrix(L.tolist())
        self.C = (Lm * self.Binv * Lm.T) / 2
        # determinant with continuous branch: det B = det P * prod (1 + i s lam), lam = eig(P^-1 G0)
        Pi_ = mp.inverse(Pm)
        lam = mp.eig(Pi_ * Gm, left=False, right=False)
        lam = [mp.re(x) for x in lam]
        pref = mp.sqrt(mp.det(Pm))
        for l in lam:
            if abs(l) > 1e-12 * max(1, max(abs(x) for x in lam)):
                pref *= mp.sqrt(1 + 1j * s * l)
        self.sqrtdet = pref
        self.cache = {}
    def moment(self, m):
        m = tuple(m)
        if sum(m) % 2:
            return mp.mpf(0)
        return self._mom(m)
    def _mom(self, m):
        if sum(m) == 0:
            return mp.mpf(1)
        if m in self.cache:
            return self.cache[m]
        i = next(k for k, v in enumerate(m) if v > 0)
        rest = list(m); rest[i] -= 1
        tot = mp.mpf(0)
        for j, v in enumerate(rest):
            if v > 0:
                r2 = list(rest); r2[j] -= 1
                tot += v * self.C[i, j] * self._mom(tuple(r2))
        # j == i contributions are included through rest[i] multiplicity (Isserlis)
        self.cache[m] = tot
        return tot

def load_terms(pk='eps2_eta4.pkl', name='r2', k=2):
    E = pickle.load(open(pk, 'rb'))
    o, zeta, al, ka = E['o'], E['zeta'], E['al'], E['ka']
    terms = {}
    for n, expr in E['res'][name][k].items():
        P = sp.Poly(expr, *o, zeta)
        lst = []
        for mon, cf in P.terms():
            f = sp.lambdify((*al, *ka), cf, 'mpmath')
            lst.append((mon, f))
        terms[n] = lst
    return terms

def Khat(terms, g, alpha, kappa):
    """sum_n i^n s^(n-1)/(n-1)! <P_n>  (s supplied separately)."""
    raise NotImplementedError

def integrand(terms, dat, alpha, s, with_pref=True, order_name=None):
    """returns K(s) (mp complex)."""
    W, Y, P = dat['W'], dat['Y'], dat['P']
    G0 = sum(eta_a[a] * np.outer(W[a], W[a]) for a in range(4))
    L = np.vstack([W, Y[None, :]])
    g = Gauss(P, G0, L, s)
    kap = dat['kappa']
    tot = mp.mpc(0)
    for n, lst in terms.items():
        sub = mp.mpc(0)
        for mon, f in lst:
            cf = f(*[mp.mpf(x) for x in alpha], *[mp.mpf(x) for x in kap])
            if cf == 0:
                continue
            sub += cf * g.moment(mon)
        tot += (1j) ** n * mp.mpmathify(s) ** (n - 1) / mp.factorial(n - 1) * sub
    if with_pref:
        nd = np.asarray(dat['P']).shape[0]
        tot = tot * (4 * mp.pi) ** (-mp.mpf(nd) / 2) / g.sqrtdet
    return tot, g
