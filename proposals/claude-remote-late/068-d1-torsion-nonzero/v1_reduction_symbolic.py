"""V1. Exact reduction of the linearised first two brackets on left-invariant backgrounds.

Background: a four-dimensional Lie group G in explicit coordinates y, left-invariant
fields E_a with [E_a, E_b] = c_ab^d E_d, connection wbar = 0, so Tbar = -c, Rbar = 0.
Fluctuation (section values): delta D_a = -h_a^c D_c + (1/2) w_a^{cd} S_cd, with h, w
ARBITRARY functions of y (sympy undefined functions), so every identity below is exact
for all smooth fluctuations, not at sampled momenta.

The linearised brackets are re-implemented here from the closed formulas of the class
(appH, display after 'Matrix equation.'), independently of core.py:
  B1_b^e   = -nabla^a T_ab^e + T_ab^c T^a_c^e + R_ab^{ae}
  B2_b^{de}=  nabla^a R_ab^{de} - T_ab^c R^a_c^{de}
Order-zero operator of the class (third bracket, linearised, T = -c):
  F_ab[A] = E_a A_b - E_b A_a - c_ab^d A_d,   Mz_b[A] = E^a F_ab + c_ab^c F^a_c.
Claims checked (exact, sympy):
  (R1) delta B2_b^{de}[h, w] = Mz_b[w^{de}]            (no h, every background below)
  (R2) delta B1_b^e[h, 0]   = sum_I Mz_b[f^I] (Ainv)_I^e,  f_b^I = -h_b^c A_c^I,
       where E_c = A_c^I rho_I and rho_I are right-invariant fields ([rho_I, E_a] = 0).
Run: python -I v1_reduction_symbolic.py
"""
import itertools
import sympy as sp

Y = sp.symbols('y0:4', real=True)
y0, y1, y2, y3 = Y
kap = sp.symbols('kappa', positive=True)
R4 = range(4)


def apply(V, f):
    return sum(V[m] * sp.diff(f, Y[m]) for m in R4)


def vcomm(V, W):
    return [sp.simplify(apply(V, W[m]) - apply(W, V[m])) for m in R4]


def iszero(x):
    """Exact zero test. Expand (polynomial and exponential coefficients); for trigonometric
    coefficients replace cos(phi), sin(phi) by symbols C, S and reduce modulo C^2 + S^2 - 1."""
    e = sp.expand(sp.powsimp(sp.expand(x)))
    if e == 0:
        return True
    trig = list(e.atoms(sp.cos, sp.sin))
    if trig:
        base = (Y[0] + Y[3]) / 2          # every trigonometric argument used below is an integer multiple
        t, C, S = sp.symbols('t_ C_ S_')
        sub = {}
        for f in trig:
            k = sp.simplify(f.args[0] / base)
            assert k.is_integer, f
            sub[f] = sp.expand_trig(f.func(k * t)).subs({sp.cos(t): C, sp.sin(t): S})
        e2 = sp.expand(e.xreplace(sub))
        if e2.has(sp.cos, sp.sin):
            return sp.simplify(e) == 0
        return sp.expand(sp.rem(sp.Poly(e2, S), sp.Poly(S ** 2 + C ** 2 - 1, S)).as_expr()) == 0
    return sp.simplify(e) == 0

def comb(*terms):
    out = [0] * 4
    for s, V in terms:
        out = [out[m] + s * V[m] for m in R4]
    return out


def struct(E):
    Em = sp.Matrix([[E[a][m] for m in R4] for a in R4])   # row a = components E_a^mu
    Einv = sp.simplify(Em.inv())
    c = [[[0] * 4 for _ in R4] for _ in R4]
    for a in R4:
        for b in R4:
            co = sp.simplify(sp.Matrix([vcomm(E[a], E[b])]) * Einv)
            for d in R4:
                c[a][b][d] = sp.simplify(co[d])
    return c


def frame_in_rho(E, R):
    Em = sp.Matrix([[E[a][m] for m in R4] for a in R4])
    Rm = sp.Matrix([[R[a][m] for m in R4] for a in R4])
    return sp.simplify(Em * Rm.inv())                       # E_c = A[c, I] rho_I


def brackets_lin(E, c, eta, h, w):
    Ef = lambda a, f: apply(E[a], f)
    dC = [[[sum(c[a][b][f] * h[f][d] for f in R4) - Ef(a, h[b][d]) + Ef(b, h[a][d])
            - sum(h[b][x] * c[a][x][d] for x in R4) + sum(h[a][x] * c[b][x][d] for x in R4)
            for d in R4] for b in R4] for a in R4]
    dOm = [[[sum(w[a][x][d] * eta[d][b] for d in R4) for x in R4] for b in R4] for a in R4]   # Om_ab^x
    Tb = [[[-c[a][b][d] for d in R4] for b in R4] for a in R4]
    dT = [[[-dC[a][b][d] - dOm[a][b][d] + dOm[b][a][d] for d in R4] for b in R4] for a in R4]
    dR = [[[[Ef(a, dOm[b][cc][f]) - Ef(b, dOm[a][cc][f]) - sum(c[a][b][d] * dOm[d][cc][f] for d in R4)
             for f in R4] for cc in R4] for b in R4] for a in R4]          # R_ab^f_cc
    dRup = [[[[sum(eta[cc][e] * dR[a][b][cc][f] for cc in R4) for e in R4] for f in R4] for b in R4] for a in R4]

    def nT(x, a, b, e):    # linearised nabla_x T_ab^e with Ombar = 0
        return (Ef(x, dT[a][b][e])
                + sum(dOm[x][a][zz] * Tb[zz][b][e] for zz in R4)
                + sum(dOm[x][b][zz] * Tb[a][zz][e] for zz in R4)
                - sum(dOm[x][zz][e] * Tb[a][b][zz] for zz in R4))
    Tbup = [[[sum(eta[a][x] * Tb[x][cc][e] for x in R4) for e in R4] for cc in R4] for a in R4]
    dTup = [[[sum(eta[a][x] * dT[x][cc][e] for x in R4) for e in R4] for cc in R4] for a in R4]
    B1 = [[sp.expand(-sum(eta[x][a] * nT(x, a, b, e) for x in R4 for a in R4)
                     + sum(Tb[a][b][cc] * dTup[a][cc][e] + dT[a][b][cc] * Tbup[a][cc][e] for a in R4 for cc in R4)
                     + sum(dRup[x][b][x][e] for x in R4)) for e in R4] for b in R4]
    dRupup = [[[[sum(eta[a][x] * dRup[x][cc][d][e] for x in R4) for e in R4] for d in R4] for cc in R4] for a in R4]
    B2 = [[[sp.expand(sum(eta[x][a] * Ef(x, dRup[a][b][d][e]) for x in R4 for a in R4)
                      - sum(Tb[a][b][cc] * dRupup[a][cc][d][e] for a in R4 for cc in R4))
            for e in R4] for d in R4] for b in R4]
    return B1, B2


def Mz(E, c, eta, A):
    F = [[apply(E[a], A[b]) - apply(E[b], A[a]) - sum(c[a][b][d] * A[d] for d in R4) for b in R4] for a in R4]
    return [sp.expand(sum(eta[x][a] * apply(E[x], F[a][b]) for x in R4 for a in R4)
                      + sum(c[a][b][cc] * eta[a][x] * F[x][cc] for a in R4 for cc in R4 for x in R4)) for b in R4]


d0, d1, d2, d3 = [[1 if m == k else 0 for m in R4] for k in R4]

BGS = {}
BGS['flat'] = ([d0, d1, d2, d3], [d0, d1, d2, d3])
# Heisenberg: [E_3, E_1] = kappa E_2; E_0, E_2 central (core.heisenberg)
BGS['Heisenberg'] = ([d0, comb((1, d1), (kap * y3 / 2, d2)), d2, comb((1, d3), (-kap * y1 / 2, d2))],
                     [d0, comb((1, d1), (-kap * y3 / 2, d2)), d2, comb((1, d3), (kap * y1 / 2, d2))])
# null rotation (core.null_rotation_g1): Z = E0 + E3 rotates (E1, E2) by [Z,E1] = E2, [Z,E2] = -E1; W = E0 - E3 central
phi = (y0 + y3) / 2
Zl = comb((1, d0), (1, d3))
Wc = comb((1, d0), (-1, d3))
E1n = [0, sp.cos(phi), sp.sin(phi), 0]
E2n = [0, -sp.sin(phi), sp.cos(phi), 0]
rZ = comb((1, Zl), (1, [0, -y2, y1, 0]))
BGS['null rotation'] = ([comb((sp.Rational(1, 2), Zl), (sp.Rational(1, 2), Wc)), E1n, E2n,
                         comb((sp.Rational(1, 2), Zl), (-sp.Rational(1, 2), Wc))],
                        [comb((sp.Rational(1, 2), rZ), (sp.Rational(1, 2), Wc)), d1, d2,
                         comb((sp.Rational(1, 2), rZ), (-sp.Rational(1, 2), Wc))])
# second algebra (core.second_algebra; non-unimodular)
BGS['second algebra'] = ([d0, d1, [0, 0, sp.exp(y0 + y1), 0], [0, 0, 0, sp.exp(y0 - y1)]],
                         [comb((1, d0), (y2, d2), (y3, d3)), comb((1, d1), (y2, d2), (-y3, d3)), d2, d3])

ETA = [[(-1 if (i == j == 0) else (1 if i == j else 0)) for j in R4] for i in R4]


def main():
    ok_all = True
    for name, (E, Rr) in BGS.items():
        c = struct(E)
        const = all(sp.diff(c[a][b][d], v) == 0 for a in R4 for b in R4 for d in R4 for v in Y)
        rho_comm = all(sp.simplify(x) == 0 for a in R4 for I in R4 for x in vcomm(E[a], Rr[I]))
        bgeq = all(sp.simplify(sum(c[a][b][d] * ETA[a][x] * c[x][d][e] for a in R4 for x in R4 for d in R4)) == 0
                   for b in R4 for e in R4)
        tr = [sp.simplify(sum(c[a][d][d] for d in R4)) for a in R4]
        nz = {(a, b, d): c[a][b][d] for a in R4 for b in R4 for d in R4 if c[a][b][d] != 0 and a < b}
        print('==', name, ': nonzero c_ab^d (a<b)', nz)
        print('   constant c:', const, '; [rho_I, E_a] = 0:', rho_comm,
              '; background equation (eta):', bgeq, '; c_ad^d:', tr)
        h = [[sp.Function('h%d%d' % (b, d))(*Y) for d in R4] for b in R4]
        w = [[[0] * 4 for _ in R4] for _ in R4]
        for b in R4:
            for (cc, d) in itertools.combinations(R4, 2):
                fn = sp.Function('w%d%d%d' % (b, cc, d))(*Y)
                w[b][cc][d] = fn
                w[b][d][cc] = -fn
        B1, B2 = brackets_lin(E, c, ETA, h, w)
        r1 = all(iszero(B2[b][d][e] - Mz(E, c, ETA, [w[x][d][e] for x in R4])[b])
                 for d in R4 for e in R4 for b in R4)
        zero_w = [[[0] * 4 for _ in R4] for _ in R4]
        B1h, _ = brackets_lin(E, c, ETA, h, zero_w)
        A = frame_in_rho(E, Rr)
        Ainv = sp.simplify(A.inv())
        f = [[sp.expand(-sum(h[b][x] * A[x, I] for x in R4)) for I in R4] for b in R4]
        MzF = [Mz(E, c, ETA, [f[b][I] for b in R4]) for I in R4]
        r2 = all(iszero(B1h[b][e] - sum(MzF[I][b] * Ainv[I, e] for I in R4)) for b in R4 for e in R4)
        print('   (R1) delta B2[h,w] = Mz[w^{de}] for arbitrary h, w:', r1)
        print('   (R2) delta B1[h,0] = Mz[-h A]^I Ainv_I^e for arbitrary h:', r2)
        ok_all = ok_all and r1 and r2
        if name in ('Heisenberg', 'null rotation'):
            # negative controls: the identity fails without the matrix A, and the frame bracket has a w-source
            ctl1 = all(iszero(B1h[b][e] - Mz(E, c, ETA, [-h[x][e] for x in R4])[b]) for b in R4 for e in R4)
            Bw, _ = brackets_lin(E, c, ETA, [[0] * 4 for _ in R4], w)
            ctl2 = all(iszero(Bw[b][e]) for b in R4 for e in R4)
            print('   controls (expected False, False): A replaced by 1 ->', ctl1, '; frame bracket free of w ->', ctl2)
    print('ALL REDUCTION IDENTITIES EXACT:', ok_all)


if __name__ == '__main__':
    main()
