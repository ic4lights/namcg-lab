"""
Closure test for the choice of base functions (second step of the 011 ranking).

Candidates: Lorentz-vector generators u^mu = alpha T^mu + beta y^mu  (T^mu = M^{mu4}, y^mu = M^{mu5}; these are the only
SO(3,1) vector generators of so(4,2)).  Define the Poisson-limit operator Box = eta_{ab}{T^a,{T^b, . }}.  The reduction to a
four-dimensional operator on functions of u^mu without a fibre average requires that Box maps functions of u to functions of u:
  (C1) K_u^{mu nu} = eta_{ab}{T^a,u^mu}{T^b,u^nu} is constant on the common level sets of u^mu,
  (C2) Box u^mu is a function of u.
Analytic input (Lie-Poisson, s^2 = 1):  {T^a,T^mu} = s M^{a mu},  {T^a,y^mu} = s eta^{a mu} m  (m = M^{45}),
  K_u^{mu nu} = alpha^2 eta_{ab} M^{a mu} M^{b nu} + beta^2 m^2 eta^{mu nu}  (cross terms cancel by antisymmetry of M^{mu nu}),
  Box T^mu = -3 T^mu,  Box y^mu = -y^mu.
Numerical test: on the six-dimensional leaf (z in C^4 mod phase, z^dag H z = n) a function F is a function of u iff its
gradient lies in the span of the gradients of u^mu and of the constraint N = z^dag H z (real 8-dim ambient space).
"""
import numpy as np
from cp12_realisation import *
np.set_printoptions(precision=6, suppress=True, linewidth=150)
rng = np.random.default_rng(7)
etam = np.diag([-1., 1, 1, 1])

def fields(p, alpha, beta):
    z = p[:4] + 1j*p[4:]
    M = Mfun(z)
    Tm = np.array([M[mu, 4] for mu in range(4)]); ym = np.array([M[mu, 5] for mu in range(4)])
    u = alpha*Tm + beta*ym
    Mam = M[:4, :4]                                   # M^{a mu}
    Ku = alpha**2*(Mam.T @ etam @ Mam) + beta**2*(M[4, 5]**2)*etam
    boxu = alpha*(-3*Tm) + beta*(-ym)
    N = np.real(z.conj() @ H @ z)
    return u, Ku, boxu, N

def grad(fun, p, h=1e-6):
    cols = []
    for i in range(8):
        d = np.zeros(8); d[i] = h
        cols.append((fun(p + d) - fun(p - d))/(2*h))
    return np.array(cols).T                            # (nfun x 8)

print("rank test on a six-dimensional leaf: rank[grad u, grad N] should be 5; adding grad K_u and grad Box u shows the failure of closure")
for (alpha, beta) in [(0., 1.), (1., 0.), (1., 1.), (0.3, 1.), (1., 0.2)]:
    out = []
    for t in range(4):
        z = rand_z_pos(rng, rng.uniform(1, 3)); p = np.concatenate([z.real, z.imag])
        Gu = grad(lambda q: fields(q, alpha, beta)[0], p)
        GN = grad(lambda q: np.array([fields(q, alpha, beta)[3]]), p)
        GK = grad(lambda q: fields(q, alpha, beta)[1][np.triu_indices(4)], p)
        GB = grad(lambda q: fields(q, alpha, beta)[2], p)
        def rk(Mx):
            sv = np.linalg.svd(Mx, compute_uv=False)
            return int(np.sum(sv > 1e-5*sv[0]))
        base = rk(np.vstack([Gu, GN]))
        r1 = rk(np.vstack([Gu, GN, GK])); r2 = rk(np.vstack([Gu, GN, GB]))
        out.append((base, r1, r2))
    print("  alpha=%.1f beta=%.1f : (rank[du,dN], +dK_u, +dBox u) at 4 points:" % (alpha, beta), out)
print("Result reading: (0,1): all ranks 5 -> K_u and Box u are functions of y (closed);  alpha != 0 -> ranks exceed 5 (K_u fibre dependent via M^{a mu}M_a^nu; Box u = -3 alpha T - beta y not a function of u).")

ratios = []
dev1 = 0; dev2 = 0
srat = []
for t in range(20):
    z = rand_z_pos(rng, rng.uniform(1, 3)); M = Mfun(z)
    for (A, B, C, D) in [(0, 4, 1, 5), (2, 4, 2, 5), (0, 1, 1, 2)]:
        rhs = lie(A, B, C, D, M)
        if abs(rhs) > 1e-6: srat.append(PB(A, B, C, D, z)/rhs)
    s = float(np.sign(np.mean(srat)))
    for mu in range(4):
        # Box T^mu = eta_{ab} {T^a, {T^b, T^mu}},  {T^b,T^mu} = s M^{b mu} = PB(b,4,mu,4)  (a function), then bracket with T^a
        boxT = sum(etam[a, a]*PB(a, 4, a, mu, z)*s for a in range(4))      # {T^b,T^mu} = s M^{b mu} => {T^a, s M^{a mu}} = s PB(a,4,a,mu)
        dev1 = max(dev1, abs(boxT - (-3*M[mu, 4])))
        boxy = s*PB(mu, 4, 4, 5, z)                                         # Box y^mu = s {T^mu, M^{45}}
        dev2 = max(dev2, abs(boxy - (-M[mu, 5])))
print("Direct check of Box T^mu = -3 T^mu and Box y^mu = -y^mu (R=1): max deviations %.2e, %.2e" % (dev1, dev2))
