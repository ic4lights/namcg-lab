"""
Exact-rational rank of the linearised Einstein operator on the fibre-moment response of the CP^{1,2} conjugate-coordinate class.

Model (derived in proposal-r1.md, geometry confirmed numerically by check_cp12_geometry.py):
  fibre-integrated first-order operator tensor, plane wave e^{i q.y}, frozen coefficients:
      h^{mu nu} = q_rho ( B^{nu;mu rho} + B^{mu;nu rho} )          (overall constant s*m*i dropped)
  B^{nu;mu rho} = int_fibre M^{mu rho} A^nu  in  R^4 (x) W_y,   W_y = span{S_1,S_2,S_3} (3-dim subspace of Lambda^2 R^4),
  S_i = [ e_i ^ vhat + e_j ^ e_k ]_{0..3 block},  vhat = (y^4,0,0,0,y^0)/ell  (unit vector in y^perp, y^a upper components),
  at the base point y^a = (y^0,0,0,0,y^4), ell^2 = (y^0)^2 - (y^4)^2.     (chirality +1 matches numerics.)
  delta G_{mu nu} is proportional to eta_{mu a} eta_{nu b} h^{ab} (background conformally flat, conformal factor irrelevant for rank).
Quantities (all exact, sympy Rational):
  dim of the response image I (expected 9 = 10 - 1: q_mu q_nu h^{mu nu} = 0),
  dim of the intersection of I with linearised diffeomorphisms q o xi (expected 3 = {xi.q = 0}),
  rank of the linearised Einstein operator E[h] on I (expected 6 = all conserved sources),
  gauge image (leading order): B = q^nu Lambda^{mu rho}, Lambda in W_y:  h = q o (Lambda q), dimension, E annihilates it.
"""
import sympy as sp, random, itertools

eta = sp.diag(-1, 1, 1, 1)
idx = [(i, j) for i in range(4) for j in range(i, 4)]
vec = lambda h: [h[i, j] for (i, j) in idx]
def lin_einstein(h, gb, p):
    gi = gb.inv(); hu = gi*h; tr = hu.trace(); pu = gi*p; p2 = (p.T*pu)[0]; ph = h*pu; pph = (pu.T*h*pu)[0]
    Ric = sp.Matrix(4, 4, lambda a, b: sp.Rational(1, 2)*(-ph[b]*p[a] - ph[a]*p[b] + p2*h[a, b] + p[a]*p[b]*tr))
    return Ric - sp.Rational(1, 2)*gb*(-pph + p2*tr)

CHI = 1
def model(y0, y4):
    ell2 = y0**2 - y4**2
    ell = sp.sqrt(ell2)
    assert ell.is_rational, "choose (y0,y4) with rational ell"
    v = sp.Matrix([y4, 0, 0, 0, y0])/ell
    e = [sp.Matrix([0]*(i+1) + [1] + [0]*(3-i)) for i in (0, 1, 2)]    # e_1,e_2,e_3 as 5-vectors
    def wedge(a, b): return a*b.T - b*a.T
    S = []
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        W5 = wedge(e[i], v) + CHI*wedge(e[j], e[k])
        S.append(W5[:4, :4])
    return S

def run(y0, y4, q, label=""):
    S = model(y0, y4)
    q = sp.Matrix(q)                         # covector q_mu
    qu = eta.inv()*q                         # q^mu
    cols_h = []; cols_E = []
    for nu in range(4):
        for i in range(3):
            B = [sp.zeros(4, 4) for _ in range(4)]   # B[nu] = B^{nu;mu rho}
            B[nu] = S[i]
            hup = sp.zeros(4, 4)
            for mu in range(4):
                for n2 in range(4):
                    hup[mu, n2] = sum(q[r]*(B[n2][mu, r] + B[mu][n2, r]) for r in range(4))
            hlow = eta*hup*eta
            cols_h.append(vec(hlow)); cols_E.append(vec(lin_einstein(hlow, eta, q)))
            assert sum(q[a]*q[b]*hup[a, b] for a in range(4) for b in range(4)) == 0
    rI = sp.Matrix(cols_h).rank()
    rE = sp.Matrix(cols_E).rank()
    diffs = []
    for k in range(4):
        xi = sp.zeros(4, 1); xi[k] = 1
        diffs.append(vec(q*xi.T + xi*q.T))
    rSum = sp.Matrix(cols_h + diffs).rank()
    rInt = rI + 4 - rSum
    # gauge image at leading order: B^{nu;mu rho} = q^nu Lambda^{mu rho}, Lambda = sum l_i S_i
    gcols = []; gE = []
    for i in range(3):
        Lam = S[i]
        hup = sp.zeros(4, 4)
        for mu in range(4):
            for n2 in range(4):
                hup[mu, n2] = sum(q[r]*(qu[n2]*Lam[mu, r] + qu[mu]*Lam[n2, r]) for r in range(4))
        hlow = eta*hup*eta
        gcols.append(vec(hlow)); gE.append(vec(lin_einstein(hlow, eta, q)))
    rG = sp.Matrix(gcols).rank()
    gEzero = all(x == 0 for row in gE for x in row)
    # conserved check on the image of E
    cons = all(sum(eta.inv()[a, a]*q[a]*0 for a in range(4)) == 0 for _ in [0])
    # E image is conserved: q^mu E_{mu nu} = 0
    ok_cons = True
    for row in cols_E:
        Em = sp.zeros(4, 4)
        for c, (i, j) in enumerate(idx): Em[i, j] = Em[j, i] = row[c]
        ok_cons = ok_cons and all(sp.simplify(sum(qu[m]*Em[m, n] for m in range(4))) == 0 for n in range(4))
    full = []
    for (i, j) in idx:
        hh = sp.zeros(4, 4); hh[i, j] = hh[j, i] = 1
        full.append(vec(lin_einstein(hh, eta, q)))
    rFull = sp.Matrix(full).rank()
    xi = sp.Matrix([R(), R(), R(), R()])
    killsdiff = all(x == 0 for x in vec(lin_einstein(q*xi.T + xi*q.T, eta, q)))
    print("   [E on all 10 symmetric tensors: rank %d; E[q o xi]=0 for random xi: %s]" % (rFull, killsdiff))
    print("%s y=(%s,%s) q=%s: dim I=%d, dim(I and Diff)=%d, rank E|I=%d (max 6), gauge image dim=%d, E[gauge]=0: %s, E image conserved: %s"
          % (label, y0, y4, list(q), rI, rInt, rE, rG, gEzero, ok_cons))
    return rI, rInt, rE, rG, gEzero

random.seed(3)
R = lambda: sp.Rational(random.randint(-6, 6), random.randint(1, 3))
print("Exact-rational results (frozen coefficients, leading symbol):")
cases = [(5, 3), (13, 5), (5, 4), (25, 7)]
for (y0, y4) in cases:
    for t in range(3):
        q = [R() for _ in range(4)]
        if all(x == 0 for x in q): continue
        run(y0, y4, q, "generic")
print("\nSpecial q (base point y=(5,3)):")
run(5, 3, [1, 0, 0, 0], "q timelike along y (pure frequency)")
run(5, 3, [0, 1, 0, 0], "q spatial          ")
run(5, 3, [1, 1, 0, 0], "q null (q^2=0)     ")
run(5, 3, [2, 1, 3, 0], "q generic spacelike")
run(5, 3, [7, 2, 1, 1], "q generic timelike ")
print("\nFold locus y^4 = 0 (excluded from the class; W_y degenerates):")
run(4, 0, [2, 1, 3, 1], "y^4=0 fold         ")

print("Opposite chirality (anti-self-dual model, not realised by the orbit; count must not depend on it):")
CHI = -1
run(5, 3, [-1, 2, sp.Rational(-1, 3), sp.Rational(1, 3)], "chi=-1")
run(13, 5, [4, sp.Rational(-4, 3), -3, 6], "chi=-1")
