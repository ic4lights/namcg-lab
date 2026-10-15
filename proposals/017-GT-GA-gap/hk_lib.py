"""
Second-order heat-trace machinery for Poisson-limit operators (proposal 017).

Setting (Euclidean eta = delta, as in the Poisson-limit paragraph of Appendix H, Problem F):
  Theta(x) = Thetabar + eps*T*sin(p.x),  T^{mu nu} = -(q^mu u^nu - u^mu q^nu),  q = Thetabar p,
  rho = 1/Pf(Theta),  D_mu f = Theta^{mu r} d_r f   (f -> {x^mu, f}),
  operators act on L^2(rho d^4x); O' = rho^{1/2} O rho^{-1/2} is symmetric on L^2(d^4x).
We write  O'(e^{ik.x} c) = e^{ik.x} sum_n z^n M_n(k) c ,  z = e^{i p.x},  M_n = sum_j eps^j M_n^{(j)}.
Second-order trace per unit volume (s = 1):
  T2 = -int_k tr[e^{-A(k)} V2_0(k)] + (1/2) int_0^1 dt int_k sum_{n=+-1} tr[V_{-n}(k+nP) e^{-tA(k+nP)} V_n(k) e^{-(1-t)A(k)}]
with A = M_0^{(0)}, V_n = M_n^{(1)}, V2_0 = M_0^{(2)}.   P = lam*p, p -> lam p exactly, so that
  (4 pi)^2 T2(lam) = c_2 lam^2 + c_4 lam^4 + c_6 lam^6 + ...  with c_2 <-> a_0 term, c_4 <-> a_1 term.
"""
import sympy as sp
import numpy as np

z, eps, lam = sp.symbols('z eps lam')
kk = sp.symbols('k1:5')
uu = sp.symbols('u1:5')
I = sp.I


def trunc(expr, order=2):
    expr = sp.expand(expr)
    return sum(expr.coeff(eps, j) * eps**j for j in range(order + 1))


def pfaff_sym(Th):
    return Th[0, 1] * Th[2, 3] - Th[0, 2] * Th[1, 3] + Th[0, 3] * Th[1, 2]


class Background:
    def __init__(self, a0, b0, p):
        self.Tb = sp.zeros(4, 4)
        self.Tb[0, 1], self.Tb[1, 0], self.Tb[2, 3], self.Tb[3, 2] = a0, -a0, b0, -b0
        self.p = sp.Matrix(p)
        self.P = lam * self.p
        self.w = self.Tb * self.P
        u = sp.Matrix(uu)
        self.T = -(self.w * u.T - u * self.w.T)
        s = (z - 1 / z) / (2 * I)
        self.Th = self.Tb + eps * self.T * s
        Pf = sp.expand(pfaff_sym(self.Th))
        self.Pf0 = sp.nsimplify(pfaff_sym(self.Tb))
        x = trunc((Pf - self.Pf0) / self.Pf0)
        sq = sp.sqrt(self.Pf0)
        self.rinv_half = trunc(sq * (1 + x / 2 - trunc(x * x) / 8))        # rho^{-1/2} = sqrt(Pf)
        self.r_half = trunc((1 / sq) * (1 - x / 2 + 3 * trunc(x * x) / 8))  # rho^{1/2}
        self.rhobar = 1 / self.Pf0

    def dth(self, f):
        return I * z * sp.diff(f, z)

    def dx(self, r, f):
        return trunc(I * kk[r] * f + self.P[r] * self.dth(f))

    def D(self, m, f):
        return trunc(sum(self.Th[m, r] * self.dx(r, f) for r in range(4)))


def extract(Mexpr, n):
    """coefficient of z^n, split by eps order."""
    e = sp.expand(Mexpr)
    cn = e.coeff(z, n)
    return [sp.expand(cn.coeff(eps, j)) for j in range(3)]


def build_vector(bg, kappa):
    """O = -D_mu D_mu + kappa D_nu D_mu(.)_mu - 2 Y ,  Y a_nu = {Theta_{nu l}, a_l}  (matrix model, 't Hooft family)."""
    M = [[None] * 4 for _ in range(4)]
    for j in range(4):
        a = [bg.rinv_half if m == j else sp.Integer(0) for m in range(4)]
        div = trunc(sum(bg.D(m, a[m]) for m in range(4)))
        res = []
        for nu in range(4):
            t1 = -sum(bg.D(m, bg.D(m, a[nu])) for m in range(4))
            t2 = kappa * bg.D(nu, div)
            Y = 0
            for lam_ in range(4):
                dTh = bg.P  # d_rho Theta_{nu lam} = P_rho dth(Theta)
                dT = bg.dth(bg.Th[nu, lam_])
                for r in range(4):
                    for sg in range(4):
                        Y += bg.Th[r, sg] * bg.P[r] * dT * bg.dx(sg, a[lam_])
            val = trunc(bg.r_half * trunc(t1 + t2 - 2 * trunc(Y)))
            res.append(val)
        for nu in range(4):
            M[nu][j] = res[nu]
    return M


def build_scalar(bg):
    a = bg.rinv_half
    val = trunc(bg.r_half * trunc(-sum(bg.D(m, bg.D(m, a)) for m in range(4))))
    return [[val]]


def gamma_euclid():
    s0 = sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -I], [I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    def kron(a, b):
        return sp.kronecker_product(a, b)
    g = [kron(s1, s0), kron(s2, s0), kron(s3, s1), kron(s3, s2)]
    return g


def build_dirac_squared(bg):
    """O_f = -(Dslash)^2 with Dslash = gamma^mu D_mu on 4-component spinors; Dslash is antihermitian on L^2(rho),
    so O_f = (i Dslash)^2 is symmetric positive."""
    g = gamma_euclid()
    M = [[None] * 4 for _ in range(4)]
    for j in range(4):
        psi = [bg.rinv_half if m == j else sp.Integer(0) for m in range(4)]
        def Dsl(v):
            out = []
            for a_ in range(4):
                out.append(trunc(sum(g[m][a_, b_] * bg.D(m, v[b_]) for m in range(4) for b_ in range(4) if g[m][a_, b_] != 0)))
            return out
        v1 = Dsl(psi)
        v2 = Dsl(v1)
        for a_ in range(4):
            M[a_][j] = trunc(bg.r_half * (-v2[a_]))
    return M


def mats_from(M, n_list=(-1, 0, 1)):
    """returns dict: (n, order) -> sympy Matrix (entries polynomial in k, lam, u)."""
    out = {}
    d = len(M)
    for n in n_list:
        for j in range(3):
            out[(n, j)] = sp.zeros(d, d)
    for a_ in range(d):
        for b_ in range(d):
            for n in n_list:
                ex = extract(M[a_][b_], n)
                for j in range(3):
                    out[(n, j)][a_, b_] = ex[j]
    return out


def eom_vec(bg):
    """E_nu = D_mu Theta_{mu nu} = Theta^{mu r} d_r Theta^{mu nu}  (Poisson-limit tree-level equation of motion)."""
    E = []
    for nu in range(4):
        val = 0
        for m in range(4):
            for r in range(4):
                val += bg.Th[m, r] * bg.P[r] * bg.dth(bg.Th[m, nu])
        E.append(trunc(val))
    return E


def build_vector_c(bg, cc):
    """gauge function F = D_mu a_mu + c E_mu a_mu (alpha=1):
       O_c = O_0 + c [ E_nu div - D_nu (E . ) ] + c^2 E_nu E_mu ,   O_0 = -D_mu D_mu - 2Y."""
    E = eom_vec(bg)
    M = [[None] * 4 for _ in range(4)]
    for j in range(4):
        a = [bg.rinv_half if m == j else sp.Integer(0) for m in range(4)]
        div = trunc(sum(bg.D(m, a[m]) for m in range(4)))
        Ea = trunc(sum(E[m] * a[m] for m in range(4)))
        res = []
        for nu in range(4):
            t1 = -sum(bg.D(m, bg.D(m, a[nu])) for m in range(4))
            Y = 0
            for l_ in range(4):
                dT = bg.dth(bg.Th[nu, l_])
                for r in range(4):
                    for sg in range(4):
                        Y += bg.Th[r, sg] * bg.P[r] * dT * bg.dx(sg, a[l_])
            t2 = cc * (E[nu] * div - bg.D(nu, Ea))
            t3 = cc ** 2 * E[nu] * Ea
            res.append(trunc(bg.r_half * trunc(t1 - 2 * trunc(Y) + t2 + t3)))
        for nu in range(4):
            M[nu][j] = res[nu]
    return M


def build_ghost_c(bg, cc):
    """Faddeev-Popov operator for F = D.a + c E.a :  M xi = -(D_mu D_mu xi + c E_mu D_mu xi)."""
    E = eom_vec(bg)
    a = bg.rinv_half
    val = -sum(bg.D(m, bg.D(m, a)) for m in range(4)) - cc * sum(E[m] * bg.D(m, a) for m in range(4))
    return [[trunc(bg.r_half * trunc(val))]]
