"""027 script 5: sharp fibre-bounded cone-window PV moment  M(Lam2, Q) = |det T| * [ (pi/2) I0 Q Lam2 + (Q^2/4) * Delta ],   Delta = int_0^{2pi} dtheta delta(theta),
delta = P_quad(1;q) - P(1;q),  q = O^T w e(theta)  (|q| = coth tau),   P_quad(r;p) = (r^2-|p|^2) I0/2 + p^T J p  (analytic continuation of the apex-inside formula),  P = true PV ball integral (brute force).
Derivation (proposal): for |p| < R_out the outer ball gives P_quad exactly; the inner ball (radius r=|z|, centre p=wz) gives P_quad when |p|<r and P_brute when |p|>r.
 => M/|detT| = int d^2z [ Lam2 I0/2 + r^2 delta ]  with  int_{|z|^2<=Q} d^2z r^2 delta = (Q^2/4) Delta  and  int d^2z Lam2 I0/2 = pi Q Lam2 I0/2 .
Checks: |w| = coth(tau); I0 against the closed form; Lam2* = threshold ratio Lam2/Q above which M>0."""
import numpy as np, warnings
from scipy.integrate import quad
from cone_window_geometry import *
from shell_apex_lemma import gauss_moment_data
warnings.filterwarnings('ignore')

def P_brute_vec(lam, p, r, n1=56, n2=56, n3=56):
    c = -lam[0]; a = np.array(lam[1:])
    p0, ps = p[0], p[1:]
    xr, wr = np.polynomial.legendre.leggauss(n1); xt, wt = np.polynomial.legendre.leggauss(n2)
    rho = 0.5*r*(xr + 1); wrho = 0.5*r*wr
    ph = (np.arange(n3) + 0.5)*2*np.pi/n3
    R, CT, PH = np.meshgrid(rho, xt, ph, indexing='ij')
    ST = np.sqrt(1 - CT**2)
    W = (wrho[:, None, None]*wt[None, :, None]*(2*np.pi/n3))*R**2
    X1 = ps[0] + R*ST*np.cos(PH); X2 = ps[1] + R*ST*np.sin(PH); X3 = ps[2] + R*CT
    A = a[0]*X1**2 + a[1]*X2**2 + a[2]*X3**2
    h = np.sqrt(np.maximum(r*r - R*R, 0.0))
    sA = np.sqrt(np.maximum(A, 1e-300)); sc = np.sqrt(c)
    F = lambda x0: np.log(np.abs((sA + sc*x0)/(sA - sc*x0 + 1e-300) + 1e-300))/(2*sA*sc)
    val = F(p0 + h) - F(p0 - h)
    return float(np.sum(W*val))

def analyse_point(M0, nth=16, **kw):
    r = analyse(M0)
    ev, O = np.linalg.eigh(r['S'][:4, :4])
    lam = list(ev)                       # ascending: (-c, a1, a2, a3)
    I0, Jd = gauss_moment_data(lam)
    w = r['w']
    sv = np.linalg.svd(w, compute_uv=False)
    th = (np.arange(nth) + 0.5)*np.pi/nth       # delta is pi-periodic
    J = np.diag(Jd)
    deltas = []
    for t in th:
        e = np.array([np.cos(t), np.sin(t)])
        q = O.T @ (w @ e)
        Pq = 0.5*(1 - q@q)*I0 + q@J@q
        Pt = P_brute_vec(lam, q, 1.0, **kw) if q@q > 1 else Pq
        deltas.append(Pq - Pt)
    Delta = np.mean(deltas)*2*np.pi             # integral over 2pi
    return dict(lam=lam, I0=I0, sv=sv, Delta=Delta, deltas=np.array(deltas), T=r['T'])

if __name__ == "__main__":
    rng = np.random.default_rng(11)
    print("  y4^2   ell^2  tau-ish a=m/ell | coth(tau) |w| | c    a_k            | I0     | Delta=int delta dtheta | Lam2*/Q = -Delta/(2 pi I0) | delta(theta) range")
    for t in range(10):
        z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); y = M0[:5, 5]
        ell2 = -(y @ np.diag([-1., 1, 1, 1, 1]) @ y); aa = abs(y[4])/np.sqrt(ell2)
        d = analyse_point(M0)
        thr = -d['Delta']/(2*np.pi*d['I0'])
        print("%8.4f %7.4f %7.4f | %7.4f %7.4f | %6.3f %s | %9.3f | %12.4f | %10.4f | %s" % (y[4]**2, ell2, aa, np.sqrt(1 + 1/aa**2), d['sv'][0], -d['lam'][0], np.round(d['lam'][1:], 3), d['I0'], d['Delta'], thr, (round(d['deltas'].min(), 3), round(d['deltas'].max(), 3))))
