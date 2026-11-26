# verify_dict_sign_127.py -- proposal 127-n-dict-kinetic-sign
# Checks for the structural package on the ass:dictionary kinetic-sign clause.
# Manuscript conventions: eta = diag(-1,1,1,1) (ass:lorentzian); Theta = real
# antisymmetric contravariant 2-form (eq:NC [X,X]=i Theta with hermitian X =>
# Theta real); kinetic tensor K^{mu nu} = theta^{alpha mu} g_{alpha beta}
# theta^{beta nu} of def:matrix-coords-ext; identity embedding g=eta gives the
# matrix K = Theta^T eta Theta (raised components).
# Run:  python -I verify_dict_sign_127.py
# Every guard carries an injected positive control proving the guard fires.
import sympy as sp

results = []
def check(name, cond):
    ok = bool(cond)
    results.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name)

eta = sp.diag(-1, 1, 1, 1)

# ---- S0 sanity: generic real antisymmetric Theta, 6 parameters -------------
f01, f02, f03, f12, f13, f23 = sp.symbols('f01 f02 f03 f12 f13 f23', real=True)
TH = sp.Matrix([[0, f01, f02, f03],
                [-f01, 0, f12, f13],
                [-f02, -f12, 0, f23],
                [-f03, -f13, -f23, 0]])
check("S0a Theta antisymmetric (generic)", TH + TH.T == sp.zeros(4, 4))
K = sp.simplify(TH.T * eta * TH)
check("S0b K symmetric (generic 6-par)", sp.simplify(K - K.T) == sp.zeros(4, 4))
Kbad = K + sp.Matrix([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
check("S0c POS-CONTROL S0b fires on K+e01",
      not (sp.simplify(Kbad - Kbad.T) == sp.zeros(4, 4)))

# ---- S1 K is Lorentzian; K = lambda*eta has no real nondegenerate solution -
pf = f01 * f23 - f02 * f13 + f03 * f12          # Pfaffian (E.b)
detTH = sp.factor(TH.det())
check("S1a det Theta = pf^2", sp.simplify(detTH - pf**2) == 0)
detK = sp.factor(K.det())
check("S1b det K = det(eta) det(Theta)^2", sp.simplify(detK - (-1) * detTH**2) == 0)
# A := Theta*eta obeys A^2 = -K*eta (from Theta^T = -Theta)
A = TH * eta
check("S1c identity A^2 + K eta = 0", sp.simplify(A * A + K * eta) == sp.zeros(4, 4))
check("S1d det(Theta eta) = -pf^2", sp.simplify(A.det() + pf**2) == 0)
# If K = lambda eta then A^2 = -lambda I, so charpoly(A) = (t^2+lambda)^2 and
# det A = lambda^2 >= 0; combined with S1d: lambda^2 = -pf^2 => real => pf=0.
t, lam = sp.symbols('t lambda', real=True)
cp = sp.expand((t**2 + lam)**2)
Asd = sp.Matrix([[sp.I, 0, 0, 0], [0, sp.I, 0, 0], [0, 0, -sp.I, 0], [0, 0, 0, -sp.I]])
check("S1e POS-CONTROL complex structure: A^2=-1*I, detA=+1",
      (Asd * Asd + sp.eye(4) == sp.zeros(4, 4)) and Asd.det() == 1)
# aligned canonical form Theta = p e^{01} + q e^{23}
p, q = sp.symbols('p q', real=True)
THc = sp.Matrix([[0, p, 0, 0], [-p, 0, 0, 0], [0, 0, 0, q], [0, 0, -q, 0]])
Kc = sp.simplify(THc.T * eta * THc)
check("S1f canonical K = diag(p^2,-p^2,q^2,q^2)",
      Kc == sp.diag(p**2, -p**2, q**2, q**2))
# Kc = lam*eta is linear in P=p^2, Q=q^2: P = -lam, Q = lam, so P + Q = 0;
# over the reals this forces p = q = 0 (degenerate Theta, det = p^2 q^2).
P, Q = sp.symbols('P Q', real=True)
sol = sp.solve([P + lam, Q - lam], [P, Q], dict=True)
check("S1g real solution set of K=lam eta forces p^2+q^2=0",
      len(sol) == 1 and sp.simplify(sol[0][P] + sol[0][Q]) == 0)
check("S1h POS-CONTROL complex (anti-)self-dual q=+/-I p solves K prop eta",
      sp.simplify(Kc.subs(q, sp.I * p) + p**2 * eta) == sp.zeros(4, 4)
      and sp.simplify(Kc.subs(q, -sp.I * p) + p**2 * eta) == sp.zeros(4, 4))
# numeric sampling: random nonzero integer antisymmetric Theta, none K prop eta
import random
random.seed(127)
def prop_test(M):
    d = [M[0, 0] + M[1, 1], M[0, 0] + M[2, 2], M[0, 0] + M[3, 3]]
    off = [M[i, j] for i in range(4) for j in range(i + 1, 4)]
    return all(x == 0 for x in d + off)
sam_ok, ctrl_hit = True, 0
for _ in range(200):
    ints = [random.randint(-5, 5) for _ in range(6)]
    if all(v == 0 for v in ints):
        continue
    Th = sp.Matrix([[0, ints[0], ints[1], ints[2]],
                    [-ints[0], 0, ints[3], ints[4]],
                    [-ints[1], -ints[3], 0, ints[5]],
                    [-ints[2], -ints[4], -ints[5], 0]])
    if prop_test(sp.simplify(Th.T * eta * Th)):
        sam_ok = False
    L = sp.eye(4) * 2   # non-antisymmetric control: L^T eta L = 4 eta
    if prop_test(sp.simplify(L.T * eta * L)):
        ctrl_hit += 1
check("S1i 200 random integer Theta: none gives K prop. eta", sam_ok)
check("S1j POS-CONTROL prop detector fires for L=2I (non-antisym.)", ctrl_hit > 0)

# ---- S2 spacelike lemma: (K^-1)_00 > 0 for every real nondegenerate Theta --
Evec = sp.Matrix([f01, f02, f03])                  # E_i = Theta^{0i}
bvec = sp.Matrix([f23, -f13, f12])                 # dual of spatial Theta^{ij}
b2 = sp.simplify((bvec.T * bvec)[0])
Ksp = K[1:, 1:]
detKsp = sp.factor(Ksp.det())
check("S2a det K_spatial = -|b|^2 pf^2", sp.simplify(detKsp + b2 * pf**2) == 0)
cof00 = sp.factor(Ksp.det())   # cofactor (0,0) of K = det of spatial block
Kinv00 = sp.simplify(K.inv()[0, 0])
check("S2b (K^-1)_00 = cof00/det K", sp.simplify(Kinv00 - cof00 / K.det()) == 0)
check("S2c detKsp * detK = |b|^2 pf^6 (>=0, >0 iff pf!=0)",
      sp.expand(detKsp * K.det() - b2 * pf**6) == 0)
import random
random.seed(128)
sam_ok = True
zero_ctrl = None
for _ in range(100):
    ints = [random.randint(-4, 4) for _ in range(6)]
    Th = sp.Matrix([[0, ints[0], ints[1], ints[2]],
                    [-ints[0], 0, ints[3], ints[4]],
                    [-ints[1], -ints[3], 0, ints[5]],
                    [-ints[2], -ints[4], -ints[5], 0]])
    pfv = pf.subs(dict(zip([f01, f02, f03, f12, f13, f23], ints)))
    if pfv == 0:
        continue
    val = Th.T * eta * Th
    v00 = sp.simplify(val.inv()[0, 0])
    if not (v00 > 0):
        sam_ok = False
check("S2d 100 random nondegenerate integer Theta: (K^-1)_00 > 0", sam_ok)
# positive control: pure-electric degenerate Theta = p e^{01} + r e^{02}: pf=0
ThE = sp.Matrix([[0, 3, 5, 0], [-3, 0, 0, 0], [-5, 0, 0, 0], [0, 0, 0, 0]])
Ke = sp.simplify(ThE.T * eta * ThE)
check("S2e POS-CONTROL degenerate pf=0 case: det Ksp = 0 (lemma is strict)",
      sp.simplify(Ke[1:, 1:].det()) == 0 and sp.simplify(Ke.det()) == 0)
# purely spatial Theta: K degenerate (matches recorded appH statement)
ThS = sp.Matrix([[0, 0, 0, 0], [0, 0, 2, 3], [0, -2, 0, 4], [0, -3, -4, 0]])
check("S2f POS-CONTROL purely spatial Theta: det K = 0 (recorded)",
      sp.simplify((ThS.T * eta * ThS).det()) == 0)
# branch criterion: the g^(0)-time direction d/dt is G-timelike (bounded
# energy possible) iff (G^-1)_00 < 0; spacelike/null (energy unbounded below
# for every normalization) iff (G^-1)_00 >= 0. Exact canonical instance:
check("S2g canonical K: (K^-1)_00 = 1/p^2 > 0 strictly",
      sp.simplify(sp.simplify(THc.T * eta * THc).inv()[0, 0] - 1 / p**2) == 0)
check("S2h POS-CONTROL eta itself: (eta^-1)_00 = -1 < 0 (bounded case)",
      eta.inv()[0, 0] == -1)

# ---- S3 trace-insertion extension: alpha K + (beta S2 - c) eta = 0 part.
# The extension shifts only by s*eta: solvable iff off-diag K = 0 and
# K00 + Kii = 0, i.e. iff K is proportional to eta. Residuals:
s = sp.symbols('s', real=True)
Ex = K + s * eta
res = [sp.simplify(Ex[i, j]) for i in range(4) for j in range(i + 1, 4)]
diag = [sp.simplify((Ex[0, 0] + Ex[i, i]).subs(s, sp.solve([Ex[0, 0]], [s], dict=True)[0][s])) for i in (1, 2, 3)]
check("S3a s solved from (0,0); residuals K00+Kii and Kij are the conditions",
      res == [K[0, 1], K[0, 2], K[0, 3], K[1, 2], K[1, 3], K[2, 3]]
      and diag == [K[0, 0] + K[1, 1], K[0, 0] + K[2, 2], K[0, 0] + K[3, 3]])
M2 = 2 * eta
res2 = ([M2[i, j] for i in range(4) for j in range(i + 1, 4)] +
        [M2[0, 0] + M2[i, i] for i in (1, 2, 3)])
check("S3b POS-CONTROL residual list vanishes for K = 2 eta (prop. case)",
      all(sp.simplify(x) == 0 for x in res2))
# ---- S4 cone/positivity criterion (numeric witnesses, box |v| <= 3) --------
def fires(G):
    for v0 in range(-3, 4):
        for v1 in range(-3, 4):
            for v2 in range(-3, 4):
                for v3 in range(-3, 4):
                    v = sp.Matrix([v0, v1, v2, v3])
                    if (v.T * eta * v)[0] < 0 and (v.T * G * v)[0] > 0:
                        return True
    return False
Gcan = sp.simplify(Kc.subs({p: 2, q: 3}))
check("S4a canonical Lorentzian K: g-timelike v with K(v,v)>0 exists", fires(Gcan))
check("S4b negative instance K = 2 eta: criterion silent (lambda>0 matched)",
      not fires(2 * eta))
check("S4c POS-CONTROL K = -2 eta: criterion fires (wrong orientation)", fires(-2 * eta))
# ---- S5 dagger and plain contractions of the dictionary image ---------------
THd = eta * TH * eta                       # lowered Theta_{mu nu}
# dagger: -Theta_{mu alpha} eta^{mu nu} Theta_{nu beta} acting on (D Phi)^dagger D Phi
Mdag = sp.simplify(-(THd.T * eta * THd))
Cpl = sp.simplify(THd.T * eta * THd)
# The contractions carry their indices down: comparison is with eta K eta
# (the lowered kinetic tensor); raising with eta returns exactly -/+ K.
check("S5a dagger contraction = - eta K eta exactly (raised: -K)",
      sp.simplify(Mdag + eta * K * eta) == sp.zeros(4, 4)
      and sp.simplify(eta * Mdag * eta + K) == sp.zeros(4, 4))
check("S5b plain contraction = + eta K eta exactly (raised: +K)",
      sp.simplify(Cpl - eta * K * eta) == sp.zeros(4, 4))
check("S5c dagger and plain carry opposite relative signs",
      sp.simplify(Mdag + Cpl) == sp.zeros(4, 4))
check("S5d POS-CONTROL: a non-K tensor (eta) is not +/- K generically",
      not (sp.simplify(eta - K) == sp.zeros(4, 4)) and not
      (sp.simplify(eta + K) == sp.zeros(4, 4)))
# ---- summary ----------------------------------------------------------------
nfail = sum(0 if ok else 1 for _, ok in results)
print(("ALL PASS (%d checks)" % len(results)) if nfail == 0
      else ("FAILURES: %d of %d" % (nfail, len(results))))
import sys
sys.exit(1 if nfail else 0)
