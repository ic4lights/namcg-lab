"""Shared Seeley-DeWitt tools (formal, complex symmetric metric allowed).  D = -(G^{mu nu} d_mu d_nu + A^mu d_mu + B) acting on rank-r bundle (B, A^mu matrices or scalars).
Vassilevich (Phys.Rept. 388 (2003), eq. 2.6-2.7 notation): omega_nu = 1/2 G_{nu mu}(A^mu + G^{sg rho}Gamma^mu_{sg rho}), E = B - G^{nu mu}(d_nu omega_mu + omega_nu omega_mu - omega_sg Gamma^sg_{nu mu}),
first coefficient density  tr(E + R/6)  (diagonal of exp(-D) = (4 pi)^{-d/2} det(G)^{1/2}... (1 + tr(E+R/6)/r + ...))."""
import sympy as sp

def christoffel(Gup, Glo, y):
    n = len(y)
    return [[[sum(Gup[a, d]*(sp.diff(Glo[d, b], y[c]) + sp.diff(Glo[d, c], y[b]) - sp.diff(Glo[b, c], y[d])) for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]

def ricci_scalar(Ginv, G, Gam, y):
    n = len(y)
    def Ric(b, c):
        r = 0
        for a in range(n):
            r += sp.diff(Gam[a][b][c], y[a]) - sp.diff(Gam[a][b][a], y[c])
            for d in range(n):
                r += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
        return r
    return sum(Ginv[b, c]*Ric(b, c) for b in range(n) for c in range(n))

def sd_first(Ginv, A, B, y, pt, rank=1, Gcov=None):
    """A: list of n entries (scalars or rank x rank Matrices), B: scalar or Matrix.  Returns (tr E, R/6) as exact/numeric at point pt (dict)."""
    n = len(y)
    G = Gcov if Gcov is not None else Ginv.inv()
    Gam = christoffel(Ginv, G, y)
    om = []
    for nu in range(n):
        acc = sp.zeros(rank, rank) if rank > 1 else 0
        for mu in range(n):
            gam = sum(Ginv[s_, r_]*Gam[mu][s_][r_] for s_ in range(n) for r_ in range(n))
            acc = acc + G[nu, mu]*(A[mu] + gam*(sp.eye(rank) if rank > 1 else 1))
        om.append(acc/2)
    E = B
    for nu in range(n):
        for mu in range(n):
            term = sp.diff(om[mu], y[nu]) + om[nu]*om[mu] - sum((Gam[s_][nu][mu]*om[s_] for s_ in range(n)), sp.zeros(rank, rank) if rank > 1 else 0)
            E = E - Ginv[nu, mu]*term
    R = ricci_scalar(Ginv, G, Gam, y)
    Ept = E.subs(pt) if hasattr(E, 'subs') else E
    Rpt = R.subs(pt)
    trE = Ept.trace() if hasattr(Ept, 'trace') else Ept
    return trE, Rpt/6, Ept
