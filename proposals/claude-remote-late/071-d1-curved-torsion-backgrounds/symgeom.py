"""Exact (sympy) section-value geometry of left-invariant data (C, W) in the
first-order equivariant class; conventions of bg.py.  Used by s1_backgrounds.py."""
import itertools
import sympy as sp

R4 = range(4)
PA = [(c, d) for c in R4 for d in R4 if c < d]


def gen(vals):
    M = sp.zeros(4, 4)
    for (c, d), v in vals.items():
        M[c, d] = v
        M[d, c] = -v
    return M


def geometry(C, W, eta):
    etai = eta.inv()
    Om = [[[sum(W[a][c][d] * eta[d, b] for d in R4) for c in R4] for b in R4] for a in R4]
    T = [[[-C[a][b][c] - Om[a][b][c] + Om[b][a][c] for c in R4] for b in R4] for a in R4]
    Rr = [[[[sum(Om[a][c][d] * Om[b][d][f] - Om[b][c][d] * Om[a][d][f] - C[a][b][d] * Om[d][c][f] for d in R4)
             for f in R4] for c in R4] for b in R4] for a in R4]
    Rup = [[[[sum(eta[c, e] * Rr[a][b][c][f] for c in R4) for e in R4] for f in R4] for b in R4] for a in R4]

    def nT(x, a, b, e):
        return sum(Om[x][a][z] * T[z][b][e] + Om[x][b][z] * T[a][z][e] - Om[x][z][e] * T[a][b][z] for z in R4)

    def nR(x, a, b, d, e):
        return sum(Om[x][a][z] * Rup[z][b][d][e] + Om[x][b][z] * Rup[a][z][d][e]
                   - Om[x][z][d] * Rup[a][b][z][e] - Om[x][z][e] * Rup[a][b][d][z] for z in R4)
    B1 = sp.Matrix(4, 4, lambda b, e: sp.simplify(
        sum(-etai[x, a] * nT(x, a, b, e) for x in R4 for a in R4)
        + sum(T[a][b][c] * etai[a, x] * T[x][c][e] for a in R4 for c in R4 for x in R4)
        + sum(Rup[a][b][a][e] for a in R4)))
    B2 = {(b, d, e): sp.simplify(sum(etai[x, a] * nR(x, a, b, d, e) for x in R4 for a in R4)
                                 - sum(T[a][b][c] * etai[a, x] * Rup[x][c][d][e] for a in R4 for c in R4 for x in R4))
          for b in R4 for (d, e) in PA}
    Tl = [[[sum(T[a][b][c] * eta[c, d] for c in R4) for d in R4] for b in R4] for a in R4]
    TT = sp.simplify(sum(Tl[a][b][c] * etai[a, a] * etai[b, b] * etai[c, c] * Tl[a][b][c]
                         for a in R4 for b in R4 for c in R4))
    trace = [sp.simplify(sum(T[a][c][c] for c in R4)) for a in R4]
    Ric = sp.Matrix(4, 4, lambda b, e: sp.simplify(sum(Rup[a][b][a][e] for a in R4)))
    Rl = [[[[sum(Rup[a][b][f][e] * eta[f, g] * eta[e, h] for f in R4 for e in R4) for h in R4] for g in R4]
           for b in R4] for a in R4]
    RR = sp.simplify(sum(Rl[a][b][c][d] ** 2 * etai[a, a] * etai[b, b] * etai[c, c] * etai[d, d]
                         for a in R4 for b in R4 for c in R4 for d in R4))
    scal = sp.simplify(sum(Ric[b, b] for b in R4))           # R_ab^{ab} = Ric_b^b (round 2: no metric weight)
    scal_weighted = sp.simplify(sum(Ric[b, e] * eta[e, b] for b in R4 for e in R4))   # round-1 quantity, not a scalar
    Rmat = sp.Matrix([[Rup[a][b][c][d] for (c, d) in PA] for (a, b) in PA])
    return dict(T=T, Rup=Rup, B1=B1, B2=B2, TT=TT, trace=trace, Ric=Ric, RR=RR, scal=scal, scal_weighted=scal_weighted, Rmat=Rmat, Om=Om)


def zeroC():
    return [[[0] * 4 for _ in R4] for _ in R4]


def W_from(cov_gens):
    """cov_gens: list of (covector k_a (len 4), generator matrix X^{cd})."""
    return [[[sum(k[a] * X[c, d] for k, X in cov_gens) for d in R4] for c in R4] for a in R4]
