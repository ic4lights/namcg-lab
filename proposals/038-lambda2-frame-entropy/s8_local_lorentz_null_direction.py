"""s8: which first-order frame Lagrangians L = sqrt(g)(a TT + b TT' + c V^2) are invariant under LOCAL frame rotations e^A -> Lambda^A_B(x) e^B ?

Invariance for arbitrary lambda_{AB}(x) (delta e^A_mu = lambda^A_B e^B_mu) holds iff the antisymmetric part of M_{AB} = E^mu_A e_{B mu}
vanishes identically, where E^mu_A is the Euler-Lagrange expression of e^A_mu.  d = 3 (all three irreducible torsion parts exist).
E is computed numerically at 60 digits (central differences of L in e and in the 'd_mu e' variables; x-derivative of pi by central difference).
Result: the antisymmetric part is linear in (a,b,c); its null space is one-dimensional, spanned by the TEGR combination (1/4, 1/2, -1).
"""
import random
import mpmath as mp

mp.mp.dps = 70
random.seed(5)
d = 3

def mat(rows):
    return mp.matrix(rows)

def L_of(e, D, abc):
    """e[A][m] = e^A_m ; D[A][m][n] = d_m e^A_n"""
    a, b, c = abc
    em = mp.matrix(d, d)
    for m in range(d):
        for A in range(d):
            em[m, A] = e[A][m]
    g = em*em.T
    gi = g**-1
    sg = mp.sqrt(mp.det(g))
    T = [[[D[A][m][n] - D[A][n][m] for n in range(d)] for m in range(d)] for A in range(d)]
    Tl = [[[sum(e[A][l]*T[A][m][n] for A in range(d)) for n in range(d)] for m in range(d)] for l in range(d)]
    # raise
    def up(Tt):
        out = [[[mp.mpf(0)]*d for _ in range(d)] for _ in range(d)]
        t1 = [[[sum(gi[l, a_]*Tt[a_][m][n] for a_ in range(d)) for n in range(d)] for m in range(d)] for l in range(d)]
        t2 = [[[sum(gi[m, b_]*t1[l][b_][n] for b_ in range(d)) for n in range(d)] for m in range(d)] for l in range(d)]
        t3 = [[[sum(gi[n, c_]*t2[l][m][c_] for c_ in range(d)) for n in range(d)] for m in range(d)] for l in range(d)]
        return t3
    Tu = up(Tl)
    TT = sum(Tl[l][m][n]*Tu[l][m][n] for l in range(d) for m in range(d) for n in range(d))
    TTp = sum(Tl[l][m][n]*Tu[m][l][n] for l in range(d) for m in range(d) for n in range(d))
    V = [sum(gi[l, n]*Tl[l][m][n] for l in range(d) for n in range(d)) for m in range(d)]
    V2 = sum(gi[m, n]*V[m]*V[n] for m in range(d) for n in range(d))
    return sg*(a*TT + b*TTp + c*V2)

# random polynomial frame e^A_m(x) (cubic in x) around a point
def rpoly():
    terms = []
    for _ in range(4):
        pw = [random.randint(0, 2) for _ in range(d)]
        terms.append((mp.mpf(random.randint(-3, 3))/random.randint(2, 5), pw))
    return terms
def ev(poly, x):
    return sum(co*mp.fprod([x[i]**pw[i] for i in range(d)]) for co, pw in poly)
def dev(poly, x, k):
    s = mp.mpf(0)
    for co, pw in poly:
        if pw[k] == 0:
            continue
        pw2 = list(pw); pw2[k] -= 1
        s += co*pw[k]*mp.fprod([x[i]**pw2[i] for i in range(d)])
    return s

def make_fields():
    polys = [[(rpoly()) for m in range(d)] for A in range(d)]
    def e_at(x):
        return [[(1 if A == m else 0) + mp.mpf(1)/5*ev(polys[A][m], x) for m in range(d)] for A in range(d)]
    def D_at(x):
        return [[[mp.mpf(1)/5*dev(polys[A][n], x, m) for n in range(d)] for m in range(d)] for A in range(d)]
    return e_at, D_at

H = mp.mpf(10)**(-22)
def pi_at(e_at, D_at, x, abc):
    e_ = e_at(x); D_ = D_at(x)
    pi = [[[None]*d for _ in range(d)] for _ in range(d)]
    for A in range(d):
        for m in range(d):
            for n in range(d):
                Dp = [[[D_[A2][m2][n2] for n2 in range(d)] for m2 in range(d)] for A2 in range(d)]
                Dm = [[[D_[A2][m2][n2] for n2 in range(d)] for m2 in range(d)] for A2 in range(d)]
                Dp[A][m][n] += H; Dm[A][m][n] -= H
                pi[A][m][n] = (L_of(e_, Dp, abc) - L_of(e_, Dm, abc))/(2*H)
    return pi

def EL_at(e_at, D_at, x, abc):
    e_ = e_at(x); D_ = D_at(x)
    dLde = [[None]*d for _ in range(d)]
    for A in range(d):
        for m in range(d):
            ep = [[e_[A2][m2] for m2 in range(d)] for A2 in range(d)]
            em_ = [[e_[A2][m2] for m2 in range(d)] for A2 in range(d)]
            ep[A][m] += H; em_[A][m] -= H
            dLde[A][m] = (L_of(ep, D_, abc) - L_of(em_, D_, abc))/(2*H)
    h = mp.mpf(10)**(-14)
    E = [[None]*d for _ in range(d)]       # E[A][n]
    dpi = {}
    for k in range(d):
        xp = list(x); xm = list(x); xp[k] += h; xm[k] -= h
        pp = pi_at(e_at, D_at, xp, abc); pm = pi_at(e_at, D_at, xm, abc)
        for A in range(d):
            for m in range(d):
                for n in range(d):
                    dpi[(A, m, n, k)] = (pp[A][m][n] - pm[A][m][n])/(2*h)
    for A in range(d):
        for n in range(d):
            E[A][n] = dLde[A][n] - sum(dpi[(A, m, n, m)] for m in range(d))
    return E, e_

def antisym_M(abc, seed):
    random.seed(seed)
    e_at, D_at = make_fields()
    x = [mp.mpf(random.randint(1, 4))/7 for _ in range(d)]
    E, e_ = EL_at(e_at, D_at, x, abc)
    M = [[sum(E[A][m]*e_[B][m] for m in range(d)) for B in range(d)] for A in range(d)]
    return [M[A][B] - M[B][A] for A in range(d) for B in range(A+1, d)]

basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
rows = []
for seed in (1, 2, 3):
    cols = [antisym_M(abc, seed) for abc in basis]      # each: 3 numbers
    for comp in range(3):
        rows.append([cols[j][comp] for j in range(3)])
Mx = mp.matrix(rows)
print("antisymmetric part of E^mu_A e_{B mu}: rows = (seed, pair), columns = coefficients of (TT, TT', V^2); first rows:")
for r in rows[:3]:
    print("  ", [mp.nstr(v, 8) for v in r])
# null vector
U, S, Vt = mp.svd_r(Mx)
print("singular values:", [mp.nstr(s, 6) for s in S])
nv = Vt[Vt.rows-1, :]
nv = [nv[0, j] for j in range(3)]
scale = nv[0]/mp.mpf(1)/4
print("null vector normalised to first entry 1/4:", [mp.nstr(v/(nv[0])*mp.mpf(1)/4, 10) for v in nv], "(TEGR: 1/4, 1/2, -1)")
print("TEGR combination residual:", mp.nstr(mp.norm(Mx*mp.matrix([mp.mpf(1)/4, mp.mpf(1)/2, -1])), 5))
print("X = TT alone residual     :", mp.nstr(mp.norm(Mx*mp.matrix([1, 0, 0])), 5))
