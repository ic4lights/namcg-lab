"""
Shared exact leading-symbol machinery for the CP^{1,2} level-one sector (model of proposals 013/014):
S_i = (e_i ^ vhat + e_j ^ e_k) restricted to indices 0..3, vhat = (y4,0,0,0,y0)/ell5, ell5^2 = y0^2 - y4^2,
s_i^mu = S_i^{mu rho} q_rho, h^{mu nu} = sum_i (s_i^mu c_i^nu + s_i^nu c_i^mu), linearised Einstein operator of eta.
All objects exact (sympy Rational).  Component ordering of c: (nu, i) -> 3*nu + i.
"""
import sympy as sp, random, itertools
eta = sp.diag(-1, 1, 1, 1)
idx = [(i, j) for i in range(4) for j in range(i, 4)]
wt = [1 if a == b else 2 for (a, b) in idx]


def Smats(y0, y4, chi=1):
    ell5 = sp.sqrt(sp.Integer(y0)**2 - sp.Integer(y4)**2)
    v = sp.Matrix([y4, 0, 0, 0, y0])/ell5
    e = [sp.Matrix([0]*(i+1)+[1]+[0]*(3-i)) for i in range(3)]
    wedge = lambda a, b: a*b.T - b*a.T
    out = []
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        W5 = wedge(e[i], v) + chi*wedge(e[j], e[k])
        out.append(W5[:4, :4])
    return out


def lin_einstein(h, p):
    """linearised Einstein tensor G_{mu nu}[h] (lower indices) in Fourier space (d -> i p) of g = eta + h  (h lower)."""
    gi = eta.inv(); hu = gi*h; tr = hu.trace(); pu = gi*p; p2 = (p.T*pu)[0]; ph = h*pu; pph = (pu.T*h*pu)[0]
    Ric = sp.Matrix(4, 4, lambda a, b: sp.Rational(1, 2)*(-ph[b]*p[a] - ph[a]*p[b] + p2*h[a, b] + p[a]*p[b]*tr))
    return Ric - sp.Rational(1, 2)*eta*(-pph + p2*tr)


class Sector:
    def __init__(self, y0, y4, qv):
        self.y0, self.y4 = sp.Integer(y0), sp.Integer(y4)
        self.l5sq = self.y0**2 - self.y4**2
        self.sig = self.y4**2/self.l5sq
        self.q = sp.Matrix(qv)
        self.qu = eta*self.q
        self.q2 = (self.q.T*self.qu)[0]
        S = Smats(y0, y4)
        self.S = S
        self.s = [S[i]*self.q for i in range(3)]                     # s_i^mu
        self.G = sp.Matrix(3, 3, lambda i, j: (self.s[i].T*eta*self.s[j])[0])
        self.qperp2 = self.q2 + (self.q[0]*self.y0)**2/self.l5sq      # q_perp^2 = q^2 + (q.y)^2/ell5^2, q.y = q_0 y^0
        self.build()

    def build(self):
        q, qu = self.q, self.qu
        H = sp.zeros(10, 12)
        for col, (nu, i) in enumerate([(nu, i) for nu in range(4) for i in range(3)]):
            h = sp.zeros(4, 4)
            for mu in range(4):
                for n2 in range(4):
                    h[mu, n2] = (self.s[i][mu] if n2 == nu else 0) + (self.s[i][n2] if mu == nu else 0)
            for r, (a, b) in enumerate(idx):
                H[r, col] = h[a, b]
        self.H = H
        Em = sp.zeros(10, 10)
        for c2 in range(10):
            hh = sp.zeros(4, 4)
            a0, b0 = idx[c2]
            hh[a0, b0] = 1
            hh[b0, a0] = 1
            if a0 == b0:
                hh[a0, a0] = 1
            Gt = lin_einstein(eta*hh*eta, q)
            for r, (a, b) in enumerate(idx):
                Em[r, c2] = wt[r]*Gt[a, b]
        self.Em = Em
        Mm = sp.zeros(12, 12)
        for b in range(4):
            for i in range(3):
                for nu in range(4):
                    Mm[b*3+i, nu*3+i] = eta[b, b]*((self.q2 if b == nu else 0) - qu[b]*q[nu])
        self.Mlow = Mm
        Gv = sp.zeros(12, 3)
        for i in range(3):
            for nu in range(4):
                Gv[nu*3+i, i] = qu[nu]
        self.Gv = Gv
        full = Gv
        for k in range(12):
            e = sp.zeros(12, 1)
            e[k] = 1
            tm = full.row_join(e)
            if tm.rank() > full.rank():
                full = tm
        self.Cm = full[:, 3:]

    def hup(self, c):
        v = self.H*c
        h = sp.zeros(4, 4)
        for r, (a, b) in enumerate(idx):
            h[a, b] = h[b, a] = v[r]
        return h

    def E_of_h(self, h_up):
        return lin_einstein(eta*h_up*eta, self.q)

    def Pperp_low(self):
        return eta - self.q*self.q.T/self.q2

    def conserved_T(self, rr):
        qu = self.qu
        Pi = sp.eye(4) - qu*self.q.T/self.q2
        X = sp.Matrix(4, 4, lambda a, b: rr())
        X = X + X.T
        return Pi.T*X*Pi

    def solve(self, Lam, w, Tl):
        Tv = sp.Matrix([wt[r]*Tl[a, b] for r, (a, b) in enumerate(idx)])
        Wf = Lam*self.Mlow + w*self.H.T*self.Em*self.H
        J = self.H.T*Tv
        Cm = self.Cm
        c9 = (Cm.T*Wf*Cm).LUsolve(Cm.T*J)
        c = Cm*c9
        assert (Wf*c - J).applyfunc(sp.simplify) == sp.zeros(12, 1), "equation not satisfied"
        return c
