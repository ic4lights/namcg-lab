"""
060 / s3: kinetic tensors of the two four-matrix presentations of the orbit CP^{1,2} (explicit realisation,
cp12_realisation.py, same as packages 011/045-049).  eta6 = diag(-1,1,1,1,1,-1); T^a = M^{a4}, y^mu = M^{mu5},
m = M^{45}, t^mu = T^mu.  Lie-Poisson brackets of linear functions are linear in M.

 (a) orbit constraint  eta_CD M^{AC} M^{BD} = c eta^{AB}  (c = R^2), y.y = -c - m^2, t.t = c + m^2, t.y = 0.
 (b) Lie-Poisson bracket from z agrees with the linear formula lie(); sign fixed.
 (c) conjugate presentation: E^{a mu} = {T^a, y^mu} = +- m eta^{a mu}, gamma = eta_ab E E = m^2 eta^{mu nu}.
 (d) base presentation: theta^{mu nu} = {y^mu, y^nu}, gamma_pt = eta_ab theta^{a mu} theta^{b nu}
     = c eta + y y - t t; at rest its negative eigenvector is along t (spacelike).
 (e) fibre average at fixed y (rest frame; stabiliser SO(3) of the spatial axes acts transitively on the
     fibre two-sphere): [gamma] = diag(m^2, (2c - m^2)/3, ..); signature by m.
"""
import numpy as np
from cp12_realisation import Mfun, PB, lie, rand_z_pos, eta6

rng = np.random.default_rng(2026)
eta4 = np.diag([-1., 1, 1, 1])

def boost_to_rest(y):
    """Lorentz matrix L (4x4, on indices 0..3) with L y = (sqrt(-y.y),0,0,0) up to sign of y0."""
    yy = -(y @ eta4 @ y)
    y0 = np.sign(y[0])*np.sqrt(yy)
    u = y/y0  # unit timelike, u0 > 0 after sign
    if u[0] < 0:
        u = -u
    gam = u[0]; v = u[1:]/u[0]
    L = np.eye(4)
    v2 = v @ v
    L[0, 0] = gam; L[0, 1:] = -gam*v; L[1:, 0] = -gam*v
    if v2 > 0:
        L[1:, 1:] += (gam-1)*np.outer(v, v)/v2
    return L

def act(L4, M):
    L6 = np.eye(6); L6[:4, :4] = L4
    return L6 @ M @ L6.T

def rand_rot():
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    a, b, c, d = q
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d]])

def lie_br(A, B, C, D, M):
    return lie(A, B, C, D, M)

# (b) sign of lie() relative to the z-bracket
z = rand_z_pos(rng, n=2.0)
M = Mfun(z)
diffs = []
for (A, B, C, D) in [(0, 4, 1, 5), (1, 4, 1, 5), (0, 5, 2, 5), (2, 4, 3, 4), (0, 4, 0, 5)]:
    diffs.append((PB(A, B, C, D, z), lie_br(A, B, C, D, M)))
ratio = [p/l for p, l in diffs if abs(l) > 1e-9]
print("(b) z-bracket / lie() on sample pairs:", np.round(ratio, 10))
s_br = np.sign(np.mean(ratio))

maxres = {'a': 0, 'c': 0, 'd': 0}
print("(a,c,d) over 40 random orbit points (n = 2):")
for k in range(40):
    z = rand_z_pos(rng, n=2.0)
    M = Mfun(z)
    MeM = M @ eta6 @ M
    c = -(MeM @ eta6)[0, 0]  # eta_CD M^{AC} M^{BD} = -(M eta M)^{AB} = c eta^{AB}
    maxres['a'] = max(maxres['a'], np.max(np.abs(-MeM - c*eta6)))
    y = M[:4, 5]; t = M[:4, 4]; m = M[4, 5]
    E = np.array([[s_br*lie_br(a, 4, mu, 5, M) for mu in range(4)] for a in range(4)])
    sgn = np.sign(E[1, 1]/m)
    maxres['c'] = max(maxres['c'], np.max(np.abs(E - sgn*m*np.linalg.inv(eta4))))
    th = np.array([[s_br*lie_br(mu, 5, nu, 5, M) for nu in range(4)] for mu in range(4)])
    gpt = th.T @ eta4 @ th
    form = c*np.linalg.inv(eta4) + np.outer(y, y) - np.outer(t, t)
    maxres['d'] = max(maxres['d'], np.max(np.abs(gpt - form)))
    if k == 0:
        print(f"   sample: c = {c:.6f}, y.y = {y@eta4@y:.6f} (-c-m^2 = {-c-m*m:.6f}), t.t = {t@eta4@t:.6f} (c+m^2 = {c+m*m:.6f}), t.y = {t@eta4@y:.2e}")
print(f"   max residuals: eta_CD M^AC M^BD - c eta^AB: {maxres['a']:.1e};  E - (+-) m eta^-1: {maxres['c']:.1e};  gamma_pt - (c eta + yy - tt): {maxres['d']:.1e}")
print("   conjugate presentation: gamma = E^T eta E = m^2 eta^{-1}: signature (3,1) wherever m != 0, zero at m = 0")

print("(d,e) base presentation at rest, fibre average over SO(3) (4000 rotations per point):")
rows = []
for k in range(14):
    z = rand_z_pos(rng, n=2.0)
    M = Mfun(z)
    c = -((M @ eta6 @ M) @ eta6)[0, 0]
    L = boost_to_rest(M[:4, 5])
    Mr = act(L, M)
    y = Mr[:4, 5]; t = Mr[:4, 4]; m = Mr[4, 5]
    th = np.array([[s_br*lie_br(mu, 5, nu, 5, Mr) for nu in range(4)] for mu in range(4)])
    gpt = th.T @ eta4 @ th
    w, v = np.linalg.eigh(gpt[1:, 1:])
    neg_dir = v[:, np.argmin(w)]
    align = abs(neg_dir @ t[1:])/np.linalg.norm(t[1:])
    acc = np.zeros((4, 4))
    nrot = 4000
    for r in range(nrot):
        R = np.eye(4); R[1:, 1:] = rand_rot()
        Mq = act(R, Mr)
        thq = np.array([[s_br*lie_br(mu, 5, nu, 5, Mq) for nu in range(4)] for mu in range(4)])
        acc += thq.T @ eta4 @ thq
    acc /= nrot
    pred = np.diag([m*m, (2*c-m*m)/3, (2*c-m*m)/3, (2*c-m*m)/3])
    ev = np.linalg.eigvalsh(acc)
    sig = (int(np.sum(ev > 1e-6*c)), int(np.sum(ev < -1e-6*c)))
    rows.append((m*m/c, np.max(np.abs(acc-pred))/c, sig, min(w), align, y[1:]))
rows.sort()
for m2c, res, sig, wmin, align, ysp in rows:
    print(f"   m^2/c = {m2c:7.4f}: |[gamma] - diag(m^2,(2c-m^2)/3)|/c = {res:.3f} (MC);  signature (+,-) = {sig};  pointwise min eig (spatial) = {wmin:+.3f}, |cos(neg dir, t)| = {align:.6f};  |y_spatial| = {np.linalg.norm(ysp):.1e}")
print("   predicted: positive definite for 0 < m^2 < 2c, (1,3) for m^2 > 2c, degenerate at m^2 in {0, 2c}")

# exact fibre average (no Monte Carlo): average of t_i t_j over SO(3) is |t|^2/3 delta_ij
z = rand_z_pos(rng, n=2.0); M = Mfun(z); c = -((M @ eta6 @ M) @ eta6)[0, 0]
L = boost_to_rest(M[:4, 5]); Mr = act(L, M); t = Mr[:4, 4]; m = Mr[4, 5]
print(f"(e') exact: |t_spatial|^2 = {t[1:]@t[1:]:.6f}, c + m^2 = {c+m*m:.6f}; [gamma]^ii = c - |t|^2/3 = {(c - t[1:]@t[1:]/3):.6f} = (2c-m^2)/3 = {(2*c-m*m)/3:.6f}; [gamma]^00 = -c + y0^2 = {-c + Mr[0,5]**2:.6f} = m^2 = {m*m:.6f}")
