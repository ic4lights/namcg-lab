"""
Vector fields on the bundle of Lorentz frames, used by the scripts of package 050.

Coordinates: y^mu (d of them) and u_a^b (d^2 entries, the Lorentz subbundle is u eta u^T = eta).
Given a coframe-independent frame e_b^mu(y) and a connection w_mu^c_d(y) (flat indices, w_{mu c d} antisymmetric),

  D_a = u_a^b e_b^mu ( d/dy^mu - sum_f u_f^d w_mu^c_d d/du_f^c ),
  S_cd : delta u_a^b = (eta_{a d} u_c^b - eta_{a c} u_d^b)   (acts on the first index of u).

No metric enters the matrix equation other than the constant eta of the matrix contraction.
"""
import sympy as sp
from fractions import Fraction


def eta_matrix(d):
    return sp.diag(*([-1] + [1]*(d-1)))


class Bundle:
    def __init__(self, d):
        self.d = d
        self.y = sp.symbols('y0:%d' % d, real=True)
        self.u = [[sp.Symbol('u%d_%d' % (a, b), real=True) for b in range(d)] for a in range(d)]
        self.coords = list(self.y) + [self.u[a][b] for a in range(d) for b in range(d)]
        self.N = len(self.coords)
        self.eta = eta_matrix(d)

    def uindex(self, a, b):
        return self.d + self.d*a + b

    def apply(self, V, f):
        return sum(V[k]*sp.diff(f, self.coords[k]) for k in range(self.N) if V[k] != 0)

    def comm(self, V, W):
        out = []
        for k in range(self.N):
            out.append(sp.expand(self.apply(V, W[k]) - self.apply(W, V[k])))
        return out

    def horizontal(self, e, w):
        """e[b][mu], w[mu] = d x d matrix w^c_d. Returns list D_a with lower a."""
        d = self.d
        D = []
        for a in range(d):
            V = [sp.S.Zero]*self.N
            for mu in range(d):
                co = sum(self.u[a][b]*e[b][mu] for b in range(d))
                V[mu] = sp.expand(co)
                for f in range(d):
                    for c in range(d):
                        t = -sum(self.u[f][dd]*w[mu][c, dd] for dd in range(d))
                        V[self.uindex(f, c)] = sp.expand(V[self.uindex(f, c)] + co*t)
            D.append(V)
        return D

    def vertical(self):
        """S[(c,d)] with c<d, lower flat indices, acting on the first index of u."""
        d = self.d
        S = {}
        for c in range(d):
            for e_ in range(c+1, d):
                V = [sp.S.Zero]*self.N
                for a in range(d):
                    for b in range(d):
                        val = self.eta[a, e_]*self.u[c][b] - self.eta[a, c]*self.u[e_][b]
                        V[self.uindex(a, b)] = val
                S[(c, e_)] = V
        return S

    def at(self, expr, point):
        return sp.nsimplify(expr.subs(point)) if hasattr(expr, 'subs') else expr

    def decompose(self, V, D, S, point):
        """Solve V = sum_a alpha^a D_a + sum beta^{cd} S_cd at a point (exact linear algebra)."""
        d = self.d
        keys = sorted(S.keys())
        vecs = [D[a] for a in range(d)] + [S[k] for k in keys]
        A = sp.Matrix([[v[k].subs(point) if v[k] != 0 else 0 for v in vecs] for k in range(self.N)])
        b = sp.Matrix([V[k].subs(point) if V[k] != 0 else 0 for k in range(self.N)])
        Aug = A.row_join(b)
        rr, piv = Aug.rref()
        n = len(vecs)
        assert n not in piv, 'V not in the span of D and S at this point'
        assert len(piv) == n, 'D and S are not independent at this point'
        sol = [rr[i, n] for i in range(n)]
        return sol[:d], {keys[i]: sol[d+i] for i in range(len(keys))}


def rational_boost(d, axis, num, den):
    """Rational Lorentz boost in the (0,axis) plane: cosh=(n^2+m^2)/(n^2-m^2), sinh=2nm/(n^2-m^2)."""
    M = sp.eye(d)
    c = sp.Rational(den*den+num*num, den*den-num*num)
    s = sp.Rational(2*den*num, den*den-num*num)
    M[0, 0] = c; M[axis, axis] = c; M[0, axis] = s; M[axis, 0] = s
    return M


def rational_rotation(d, i, j, num, den):
    M = sp.eye(d)
    c = sp.Rational(den*den-num*num, den*den+num*num)
    s = sp.Rational(2*den*num, den*den+num*num)
    M[i, i] = c; M[j, j] = c; M[i, j] = -s; M[j, i] = s
    return M


def levi_civita_connection(e, y, eta):
    """
    e[b][mu] frame (rows b). Returns w[mu] = matrix w^c_d with de^c + w^c_d ^ e^d = 0.
    """
    d = len(y)
    E = sp.Matrix(e)
    th = E.inv()                     # th[mu,b] coframe e^b_mu
    th = th.applyfunc(sp.simplify)
    # structure: de^c_{mu nu}
    C = [[[sp.diff(th[nu, c], y[mu]) - sp.diff(th[mu, c], y[nu]) for nu in range(d)] for mu in range(d)] for c in range(d)]
    # anholonomy in flat indices: c_ab^c = e_a^mu e_b^nu de^c_{mu nu}
    c_ = [[[sp.simplify(sum(E[a, mu]*E[b, nu]*C[c][mu][nu] for mu in range(d) for nu in range(d))) for c in range(d)] for b in range(d)] for a in range(d)]
    lower = lambda a, b, c: sum(eta[c, g]*c_[a][b][g] for g in range(d))
    # w_{a|bc} from Koszul:  w_{a b c} = 1/2 (c_{ab c} + c_{ca b} - c_{bc a})
    wflat = [[[sp.simplify(sp.Rational(1, 2)*(lower(a, b, c) + lower(c, a, b) - lower(b, c, a))) for c in range(d)] for b in range(d)] for a in range(d)]
    # w_mu^c_d = th_mu^a eta^{c g} w_{a g d} with the sign fixed by the torsion-free condition, tested in check_torsion_free
    w = []
    for mu in range(d):
        m = sp.zeros(d, d)
        for c in range(d):
            for dd in range(d):
                m[c, dd] = sp.simplify(sum(th[mu, a]*eta[c, c]*wflat[a][c][dd] for a in range(d)))
        w.append(m)
    return w, th


def check_torsion_free(w, th, y, eta):
    d = len(y)
    bad = 0
    for c in range(d):
        for mu in range(d):
            for nu in range(mu+1, d):
                val = sp.diff(th[nu, c], y[mu]) - sp.diff(th[mu, c], y[nu]) \
                    + sum(w[mu][c, g]*th[nu, g] - w[nu][c, g]*th[mu, g] for g in range(d))
                if sp.simplify(val) != 0:
                    bad += 1
    anti = 0
    for mu in range(d):
        low = eta*w[mu]
        if sp.simplify(low + low.T) != sp.zeros(d, d):
            anti += 1
    return bad, anti


def ricci_flat_index(e, w, th, y, eta):
    """Riemann and Ricci in flat indices of the section u = 1, from w (any metric connection)."""
    d = len(y)
    E = sp.Matrix(e)
    Rm = {}
    for mu in range(d):
        for nu in range(d):
            Rm[(mu, nu)] = (w[nu].diff(y[mu]) - w[mu].diff(y[nu]) + w[mu]*w[nu] - w[nu]*w[mu]).applyfunc(sp.simplify)
    # R_ab^c_d
    R = [[sp.zeros(d, d) for b in range(d)] for a in range(d)]
    for a in range(d):
        for b in range(d):
            m = sp.zeros(d, d)
            for mu in range(d):
                for nu in range(d):
                    m += E[a, mu]*E[b, nu]*Rm[(mu, nu)]
            R[a][b] = m.applyfunc(sp.simplify)
    # Ricci_bd = R_ab^a_d
    Ric = sp.zeros(d, d)
    for b in range(d):
        for dd in range(d):
            Ric[b, dd] = sp.simplify(sum(R[a][b][a, dd] for a in range(d)))
    return R, Ric
