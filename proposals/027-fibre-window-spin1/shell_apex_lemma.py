"""027 script 4: PV moment of the fibre-bounded cone window.  In whitened coordinates sigma(Box) = Q_L(u + w z),  Q_L = S_uu (eigenvalues (-c,a,a,a)),  window  {|z|^2 <= Q, 0 <= |u|^2-|z|^2 <= Lam2}.
P(r;p) := PV int_{|x-p|<r} d^4x / Q_L(x)  (x = u + w z, p = w z).  Facts proved in the proposal and checked here:
 (F1) for |p| < R :  P(R;p) = (R^2-|p|^2) I0/2 + p^T J p,   I0 = PV int_{S^3} dOmega/Q_L(n),  J_ij = PV int_{S^3} n_i n_j /Q_L(n)  (the odd term of rho_out^2 integrates to zero).
 (F2) hence for |p| < r the shell moment is exactly Lam2*I0/2.
 (F3) for |p| > r : P(r;p) is an integral over the cap of directions hitting the ball:  P = (1/2) int_cap dOmega 4 (n.p) sqrt((n.p)^2 + r^2 - |p|^2) / Q_L(n).
Numerical checks: brute-force x0-closed-form + 3D quadrature of P(r;p) against (F1) at |p|<r and against (F3) at |p|>r."""
import numpy as np, scipy.linalg as sl
from scipy.integrate import quad
from cone_window_geometry import *

def gauss_moment_data(lam):
    """lam = (-c, a1, a2, a3).  I0 = 2 pi^2 Re[ i int ds prod (1+i s lam)^(-1/2) ],  J_kk = pi^2 Re[ i int ds (1+ i s lam_k)^(-1) prod(...)^(-1/2) ] (eigenframe, diagonal)."""
    ph = np.exp(-1j*np.pi/4)
    def integ(k, part):
        def f(u):
            sv = u*ph
            val = np.prod([(1 + 1j*sv*l)**-0.5 for l in lam])
            if k is not None: val = val/(1 + 1j*sv*lam[k])
            r = 1j*ph*val
            return r.real if part == 0 else r.imag
        return quad(f, 0, np.inf, limit=400)[0]
    I0 = 2*np.pi**2*integ(None, 0)
    Jd = np.array([np.pi**2*integ(k, 0) for k in range(4)])
    return I0, Jd

def P_brute(lam, p, r, n1=48, n2=48, n3=64):
    """PV int_{|x-p|<r} d^4x/(-c x0^2 + sum a_k x_k^2), eigenframe coordinates; x0 integrated analytically, spatial 3D by Gauss quadrature in spherical coords centred at p_s."""
    c = -lam[0]; a = np.array(lam[1:])
    p0, ps = p[0], p[1:]
    xr, wr = np.polynomial.legendre.leggauss(n1)      # radial s in [0,r]
    xt, wt = np.polynomial.legendre.leggauss(n2)      # cos theta
    ph = (np.arange(n3) + 0.5)*2*np.pi/n3
    tot = 0.0
    for i in range(n1):
        rho = 0.5*r*(xr[i] + 1); wrho = 0.5*r*wr[i]
        h = np.sqrt(max(r*r - rho*rho, 0.0))
        for j in range(n2):
            ct = xt[j]; st = np.sqrt(1 - ct*ct)
            for k in range(n3):
                d = rho*np.array([st*np.cos(ph[k]), st*np.sin(ph[k]), ct])
                xs = ps + d
                A = float(np.sum(a*xs*xs))
                if A <= 0: continue
                sA = np.sqrt(A); sc = np.sqrt(c)
                def F(x0): return np.log(abs((sA + sc*x0)/(sA - sc*x0)))/(2*sA*sc)
                tot += wrho*wt[j]*(2*np.pi/n3)*rho*rho*(F(p0 + h) - F(p0 - h))
    return tot

def P_cap(lam, S, p, r, nphi=200, nnu=24):
    """(F3): apex outside the ball (|p|>r).  S = diag(lam) in eigenframe; p in eigenframe."""
    S = np.diag(lam); pn = np.linalg.norm(p)
    phat = p/pn
    # orthonormal complement of phat in R^4
    Q, _ = np.linalg.qr(np.column_stack([phat, np.eye(4)[:, :3]])) if False else np.linalg.qr(np.column_stack([phat, np.random.default_rng(0).normal(size=(4, 3))]))
    Q = Q*np.sign(Q[:, 0] @ phat); E = Q[:, 1:4]
    phimax = np.arcsin(r/pn)
    xt, wt = np.polynomial.legendre.leggauss(nnu)
    tot = 0.0
    for i in range(nnu):
        ct = xt[i]; st = np.sqrt(1 - ct*ct)
        for k in range(2*nnu):
            ph = (k + 0.5)*np.pi/nnu
            nu = E @ np.array([st*np.cos(ph), st*np.sin(ph), ct])
            qpp = phat @ S @ phat; qpn = phat @ S @ nu; qnn = nu @ S @ nu
            sig = lambda f: np.cos(f)**2*qpp + 2*np.cos(f)*np.sin(f)*qpn + np.sin(f)**2*qnn
            g = lambda f: 4*pn*np.cos(f)*np.sqrt(max((pn*np.cos(f))**2 + r*r - pn*pn, 0.0))*np.sin(f)**2
            # roots of sigma in (0,phimax): tan f solves qnn T^2 + 2 qpn T + qpp = 0
            roots = []
            disc = qpn**2 - qnn*qpp
            if abs(qnn) > 1e-14 and disc > 0:
                for sgn in (1, -1):
                    T = (-qpn + sgn*np.sqrt(disc))/qnn
                    f0 = np.arctan(T)
                    if 0 < f0 < phimax: roots.append(f0)
            roots = sorted(roots)
            edges = [0.0] + [0.5*(roots[i] + roots[i+1]) for i in range(len(roots) - 1)] + [phimax]
            if not roots:
                val = quad(lambda f: g(f)/sig(f), 0, phimax, limit=200)[0]
            else:
                val = 0.0
                for i0, f0 in enumerate(roots):
                    dsig = lambda f: -2*np.cos(f)*np.sin(f)*qpp + 2*np.cos(2*f)*qpn + 2*np.sin(f)*np.cos(f)*qnn
                    def h(f, f0=f0):
                        if abs(f - f0) < 1e-10: return g(f0)/dsig(f0)
                        return g(f)*(f - f0)/sig(f)
                    val += quad(h, edges[i0], edges[i0+1], weight='cauchy', wvar=f0, limit=200)[0]
            tot += wt[i]*(np.pi/nnu)*val
    return 0.5*tot

if __name__ == "__main__":
    rng = np.random.default_rng(2)
    c, a = 0.5, 0.7271
    lam = [-c, a, a, a]
    I0, Jd = gauss_moment_data(lam)
    print("I0 =", I0, " closed form (a,a,a isotropic): 2 pi^2 * 2/(a+c) =", 2*np.pi**2*2/(a + c))
    print("J_kk =", Jd, " check trace identity  sum_k J_kk/lam_k = I0*? (wave-equation: tr(S^-1 J) = I0 tr(S^-1)/2):", np.sum(Jd/np.array(lam)), I0*np.sum(1/np.array(lam))/2)
    # (F1) check at |p|<r
    p = np.array([0.3, 0.2, -0.1, 0.25]); r = 1.0
    quad_ext = 0.5*(r**2 - p@p)*I0 + p@np.diag(Jd)@p
    pb = P_brute(lam, p, r)
    print("(F1) |p|=%.3f r=1:  quadratic formula %.5f   brute force %.5f" % (np.linalg.norm(p), quad_ext, pb))
    # (F3) |p|>r
    p = np.array([0.9, 0.5, -0.3, 0.6]); print("|p| =", np.linalg.norm(p))
    pb = P_brute(lam, p, r, n1=40, n2=40, n3=48)
    pc = P_cap(lam, None, p, r)
    print("(F3) |p|>r: brute force %.5f   cap formula %.5f   quadratic-extension (not valid) %.5f" % (pb, pc, 0.5*(r**2 - p@p)*I0 + p@np.diag(Jd)@p))
