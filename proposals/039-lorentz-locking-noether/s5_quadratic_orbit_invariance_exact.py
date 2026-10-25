"""s5: exact (rational) necessity of the TEGR direction, at quadratic order about a constant frame.

Flat background e-bar = 1, metric eta (any signature), plane wave e = 1 + ehat cos(p.x).  First-order torsion amplitude
  T_{l m n} = p_m ehat_{l n} - p_n ehat_{l m},  V_m = eta^{ln} T_{l m n},  W_m = (1/2) p_m tr ehat   (tr with eta).
Quadratic form  Q_a(ehat) = a1 T.T + a2 T_{lmn}T^{mln} + a3 V.V + a4 V.W + a5 W.W   (real amplitudes; the overall phase average is a common factor).
Rotation orbit:  ehat -> ehat + phi,  phi_{AB} = -phi_{BA} (lowered with eta).
Local rotation invariance of the density to quadratic order  <=>  Q_a(ehat + phi) = Q_a(ehat) for all ehat, phi and all p.
Solved here exactly with sympy for generic rational p, d = 3, 4, signatures (+,...,+) and (-,+,...,+).
"""
import itertools
import sympy as sp


def run(d, eta_diag, p):
    eta = sp.diag(*eta_diag)
    etai = eta.inv()
    a = sp.symbols('a1:6')

    def Tof(eh):
        return [[[p[m]*eh[l, n] - p[n]*eh[l, m] for n in range(d)] for m in range(d)] for l in range(d)]

    def Q(eh):
        T = Tof(eh)
        Tu = [[[sum(etai[l, l]*etai[m, m]*etai[n, n]*T[l][m][n] for _ in [0]) for n in range(d)] for m in range(d)] for l in range(d)]
        TT = sum(T[l][m][n]*Tu[l][m][n] for l in range(d) for m in range(d) for n in range(d))
        TTp = sum(T[l][m][n]*Tu[m][l][n]*(etai[l, l]*etai[m, m]*etai[n, n])/(etai[m, m]*etai[l, l]*etai[n, n]) for l in range(d) for m in range(d) for n in range(d))
        V = [sum(etai[l, l]*T[l][m][l] for l in range(d)) for m in range(d)]
        W = [sp.Rational(1, 2)*p[m]*sum(etai[l, l]*eh[l, l] for l in range(d)) for m in range(d)]
        V2 = sum(etai[m, m]*V[m]*V[m] for m in range(d))
        VW = sum(etai[m, m]*V[m]*W[m] for m in range(d))
        W2 = sum(etai[m, m]*W[m]*W[m] for m in range(d))
        return a[0]*TT + a[1]*TTp + a[2]*V2 + a[3]*VW + a[4]*W2

    # T_{l m n}T^{m l n}: mixed contraction needs T^{mln} = eta^{mm'}eta^{ll'}eta^{nn'} T_{m'l'n'}; implement exactly
    def Qfull(eh):
        T = Tof(eh)
        def up(l, m, n):
            return etai[l, l]*etai[m, m]*etai[n, n]*T[l][m][n]
        TT = sum(T[l][m][n]*up(l, m, n) for l in range(d) for m in range(d) for n in range(d))
        TTp = sum(T[l][m][n]*up(m, l, n) for l in range(d) for m in range(d) for n in range(d))
        V = [sum(etai[l, l]*T[l][m][l] for l in range(d)) for m in range(d)]
        W = [sp.Rational(1, 2)*p[m]*sum(etai[l, l]*eh[l, l] for l in range(d)) for m in range(d)]
        V2 = sum(etai[m, m]*V[m]*V[m] for m in range(d))
        VW = sum(etai[m, m]*V[m]*W[m] for m in range(d))
        W2 = sum(etai[m, m]*W[m]*W[m] for m in range(d))
        return a[0]*TT + a[1]*TTp + a[2]*V2 + a[3]*VW + a[4]*W2

    # polarisation: B(x,y) = (Q(x+y)-Q(x)-Q(y))/2; conditions Q(phi)=0, B(E_ab, phi)=0
    def E_(i, j):
        M = sp.zeros(d, d); M[i, j] = 1; return M
    phis = []
    for i in range(d):
        for j in range(i+1, d):
            M = sp.zeros(d, d)
            M[i, j] = 1; M[j, i] = -1       # lowered-index antisymmetric amplitude phi_{ij}; frame index lowered with eta
            phis.append(M*1)
    # phi lowered: ehat_{lA} += phi_{lA}; we work with ehat with first index lowered, so antisymmetric matrix in (l,A) lowered indices
    # the amplitude entering T_{l m n} is ehat_{l n} with l lowered by eta (e_A^mu eta_{AB} ... -> eta-lowered frame index): antisym in lowered pair
    eqs = []
    for ph in phis:
        eqs.append(sp.expand(Qfull(ph)))
        for i in range(d):
            for j in range(d):
                x = E_(i, j)
                eqs.append(sp.expand(Qfull(x + ph) - Qfull(x) - Qfull(ph)))
    eqs = [e for e in eqs if e != 0]
    sol = sp.solve(eqs, a, dict=True)
    return sol


if __name__ == "__main__":
    for d, eta_d in [(3, (1, 1, 1)), (3, (-1, 1, 1)), (4, (1, 1, 1, 1)), (4, (-1, 1, 1, 1))]:
        p = [sp.Rational(3, 5), sp.Rational(-2, 7), sp.Rational(5, 3), sp.Rational(1, 4)][:d]
        sol = run(d, eta_d, p)
        print(f"d={d} eta={eta_d}: solution of the orbit-invariance equations: {sol}")
