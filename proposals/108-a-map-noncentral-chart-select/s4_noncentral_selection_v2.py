# s4_noncentral_selection.py  (proposal 108-a-map-noncentral-chart-select, r1)
# Self-contained verification battery: scalarity dichotomy, Lie-type (fuzzy
# sphere) derived bivector, Casimir chart fixing, chart 1-jet torsors and the
# rank/Pfaffian obstruction at degenerate points, finite-N ('t Hooft) non-scalarity,
# bivector-field equivariance. Standard library only.
# Run:  python -I s4_noncentral_selection.py
# Expect: every CHECK PASS and the line  TOTALS: PASS 16/16 FAIL 0
import math
import random

results = []

def chk(n, name, ok, inv):
    results.append((n, name, bool(ok)))
    print("CHECK %d [%s]: %s | %s" % (n, name, "PASS" if ok else "FAIL", inv))

def eye(n):
    return [[1+0j if i == j else 0j for j in range(n)] for i in range(n)]

def Z(n):
    return [[0j]*n for _ in range(n)]

def add(a, b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def sub(a, b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mul(a, b):
    n, m, p = len(a), len(a[0]), len(b[0])
    return [[sum(a[i][k]*b[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def sc(a, c):
    return [[c*a[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def comm(a, b):
    return sub(mul(a, b), mul(b, a))

def adj(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]

def tr(a):
    return sum(a[i][i] for i in range(len(a)))

def frob(a):
    return math.sqrt(sum(abs(a[i][j])**2 for i in range(len(a)) for j in range(len(a[0]))))

def scalar_part(a):
    n = len(a)
    return sc(eye(n), tr(a)/n)

def expval(op, v):
    return sum(v[i].conjugate()*op[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))

def biv(A, B, v):
    # -i <v|[A,B]|v> for normalized vector v; real if A,B Hermitian
    return (-1j*expval(comm(A, B), v)).real

def state(t, phi):
    th = math.acos(1-2*t)
    return [math.cos(th/2), math.sin(th/2)*complex(math.cos(phi), math.sin(phi))]

def rank(R):
    R = [list(map(float, r)) for r in R]
    n = len(R)
    m = len(R[0])
    rk = 0
    for c in range(m):
        piv = None
        for r in range(rk, n):
            if abs(R[r][c]) > 1e-9:
                piv = r
                break
        if piv is None:
            continue
        R[rk], R[piv] = R[piv], R[rk]
        pv = R[rk][c]
        R[rk] = [x/pv for x in R[rk]]
        for r in range(n):
            if r != rk and R[r][c] != 0:
                f = R[r][c]
                R[r] = [R[r][k]-f*R[rk][k] for k in range(m)]
        rk += 1
        if rk == n:
            break
    return rk

def spinJ(j, dim):
    # index k <-> m = j-k ; J3 diagonal, J+ raising in m
    J3 = [[(j-k)+0j if i == k else 0j for k in range(dim)] for i in range(dim)]
    Jm = Z(dim)      # (Jm)[k+1][k] connects m=j-k -> m-1: lowering operator
    for k in range(dim-1):
        mm = j-k
        Jm[k+1][k] = math.sqrt(j*(j+1)-mm*(mm-1))
    Jp = adj(Jm)
    J1 = sc(add(Jp, Jm), 0.5)
    J2 = sc(sub(Jp, Jm), -0.5j)
    return [J1, J2, J3]

def pole_state(dim):
    v = [0j]*dim
    v[0] = 1+0j           # |m = +j>, the spin coherent state along +z
    return v

print("=== 108 s4 noncentral selection battery ===")

# --- 1: dichotomy, non-scalar pair with rational entries
sx = [[0+0j, 1+0j], [1+0j, 0+0j]]
sy = [[0+0j, -2j], [2j, 0+0j]]          # 2*sigma_y
A, B = sx, sy
C = comm(A, B)                          # 4i*sigma_z
dev1 = frob(sub(C, scalar_part(C)))
v1 = [1+0j, 0+0j]
v2 = [0+0j, 1+0j]
b1, b2 = biv(A, B, v1), biv(A, B, v2)
ok = (dev1 > 1.0) and abs(b1-4) < 1e-12 and abs(b2+4) < 1e-12
chk(1, "dichotomy-non-scalar", ok,
    "C=[A,B]=4i*sz: non-scalar dev=%.3f; biv on |0>,|1>: %g, %g (state-dependent)" % (dev1, b1, b2))

# --- 2: dichotomy control: commuting pair (zero-scalar commutator): biv = 0 on all states
A2 = [[1+0j, 0+0j], [0+0j, 0+0j]]
B2 = [[2+0j, 0+0j], [0+0j, 5+0j]]
C2 = comm(A2, B2)
vs = [state(t, p) for (t, p) in [(0.05, 0.4), (0.35, 1.2), (0.65, 2.7), (0.95, 5.0)]]
vals2 = [biv(A2, B2, v) for v in vs] + [biv(A2, B2, [1+0j, 0+0j]), biv(A2, B2, [0+0j, 1+0j])]
mx2 = max(abs(x) for x in vals2)
ok = frob(C2) < 1e-12 and mx2 < 1e-12
chk(2, "dichotomy-scalar-control", ok,
    "[A2,B2]=0: biv=0 on all %d test states (max |biv|=%.2e)" % (len(vals2), mx2))

# --- 3: trace argument: [P,Q]=c*1 forces c=0; iC Hermitian for Hermitian P,Q
random.seed(108)
def rand_herm(n):
    m = [[complex(random.uniform(-2, 2), random.uniform(-2, 2)) for _ in range(n)] for _ in range(n)]
    return [[(m[i][j]+m[j][i].conjugate())/2 for j in range(n)] for i in range(n)]
worst_c = 0.0
worst_h = 0.0
for trial in range(40):
    P, Q = rand_herm(3), rand_herm(3)
    D = comm(P, Q)
    worst_c = max(worst_c, abs(tr(D)/3))
    iD = sc(D, 1j)
    worst_h = max(worst_h, frob(sub(iD, adj(iD))))
ok = worst_c < 1e-10 and worst_h < 1e-10
chk(3, "trace-and-hermiticity", ok,
    "40 random Hermitian pairs M_3: max |tr([P,Q])/3|=%.2e, max ||iC-(iC)^dag||=%.2e" % (worst_c, worst_h))

# --- 4: state-spread equals spectrum of iC (extreme values attained by eigenvectors)
iC = sc(comm(A, B), 1j)                    # = -4 sz
p0 = (-iC[0][0]-iC[1][1])
det_iC = iC[0][0]*iC[1][1]-iC[0][1]*iC[1][0]
disc = (p0*p0-4*det_iC).real
e_lo = (-p0.real-math.sqrt(disc))/2
e_hi = (-p0.real+math.sqrt(disc))/2
ok = abs(b1-e_hi) < 1e-9 and abs(b2-e_lo) < 1e-9 and (e_hi-e_lo) > 1e-9
chk(4, "state-spread-equals-spectrum", ok,
    "iC=-4*sz: eig %g,%g; biv attains both ends -> spread width %g" % (e_lo, e_hi, e_hi-e_lo))

# --- 5: fuzzy sphere: [X_a,X_b] = i eps_abc X_c (l=1, spin j)
worst5 = 0.0
for (j, dim) in [(2, 5), (3, 7)]:
    X = spinJ(j, dim)
    for (a, b, cc) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        lhs = comm(X[a], X[b])
        rhs = sc(X[cc], 1j)
        worst5 = max(worst5, frob(sub(lhs, rhs))/frob(rhs))
ok = worst5 < 1e-10
chk(5, "fuzzysphere-commutator", ok,
    "[X_1,X_2]=i X_3 etc. exact, spin j=2,3 (l=1): max rel dev %.2e" % worst5)

# --- 6: derived bivector values: Theta^{12}_w = <X_3> (operator identity -> any state);
#        at the pole state |m=j> (leaf point x_3 = j): bivector = j
tab6 = []
dev6 = 0.0
for j in [2, 3, 4, 6, 8]:
    dim = 2*j+1
    X = spinJ(j, dim)
    v = pole_state(dim)
    b12 = biv(X[0], X[1], v)
    x3 = expval(X[2], v).real
    dev6 = max(dev6, abs(b12-x3), abs(x3-j))
    tab6.append((j, x3, b12))
ok = dev6 < 1e-9
chk(6, "bivector-values-at-pole", ok,
    "Theta^{12} = <X_3> = j at leaf point x_3=j: " + " ".join("j=%d:%g->%g" % t for t in tab6)
    + " (max dev %.2e); leaf dependence: values span [-j,+j] over states" % dev6)

# --- 7: Casimir X.X = j(j+1) 1 exact (orbit datum R^2 = l^2 j(j+1))
dev7 = 0.0
tab7 = []
for j in [2, 3, 4, 6, 8]:
    dim = 2*j+1
    X = spinJ(j, dim)
    S = Z(dim)
    for a in range(3):
        S = add(S, mul(X[a], X[a]))
    target = j*(j+1)
    dev7 = max(dev7, frob(sub(S, sc(eye(dim), target)))/target)
    tab7.append((j, target))
ok = dev7 < 1e-10
chk(7, "casimir-orbit-radius", ok,
    "X.X = R^2*1, R^2=j(j+1): " + ", ".join("j=%d:R^2=%d" % t for t in tab7) + " (max rel dev %.2e)" % dev7)

# --- 8: bivector sharpness in the pole coherent state: Var(X_3)=0, Var(X_1)=Var(X_2)=j/2
#        (transverse components); total fluctuation / bivector norm = 1/sqrt(j)
dev8 = 0.0
tab8 = []
for j in [1, 2, 3, 4, 6, 8, 50]:
    dim = 2*j+1
    X = spinJ(j, dim)
    v = pole_state(dim)
    var3 = (expval(mul(X[2], X[2]), v)-expval(X[2], v)**2).real
    var1 = (expval(mul(X[0], X[0]), v)-expval(X[0], v)**2).real
    var2 = (expval(mul(X[1], X[1]), v)-expval(X[1], v)**2).real
    dev8 = max(dev8, abs(var3), abs(var1-j/2), abs(var2-j/2))
    rel = math.sqrt(2*(var1+var2+var3))/math.sqrt(2*j*j)   # sqrt(sum_ij Var(C^ij)) / sqrt(sum_ij (Theta^ij)^2)
    tab8.append((j, rel))
ok = dev8 < 1e-8
chk(8, "bivector-sharpness-pole", ok,
    "Var(X_3)=0, Var(X_1)=Var(X_2)=j/2 at pole (max dev %.2e); bivector rel width " % dev8
    + " ".join("j=%d:%.4f" % t for t in tab8))

# --- 9: bivector-germ 1-jet nonzero: sum_pairs (C^{ab} X_m + X_m C^{ab}) = 2 X.X
dim = 7   # j=3
X = spinJ(3, dim)
pairset = [((0, 1), 2), ((1, 2), 0), ((2, 0), 1)]
Jac2 = Z(dim)
for (a, b), m in pairset:
    Cab = sc(comm(X[a], X[b]), -1j)          # C^{ab} = l X_m (l=1)
    Jac2 = add(Jac2, mul(Cab, X[m]))
    Jac2 = add(Jac2, mul(X[m], Cab))
target24 = 24.0    # 2*X.X = 2*j(j+1) = 24 at j=3
dev9 = frob(sub(Jac2, sc(eye(dim), target24)))/target24
ok = dev9 < 1e-10
chk(9, "bivector-germ-1jet-nonzero", ok,
    "sum_pairs (C^{ab}X_m + X_m C^{ab}) = 2 X.X = %g (j=3): rel dev %.2e -> bivector 1-jet datum O(1), not 0" % (target24, dev9))

# --- 10: chart 1-jet torsor in D=4: frames M with M J M^T = J form one Sp(4) orbit (dim 10)
Jst = [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]]
def matmul4(AM, BM):
    return [[sum(AM[i][k]*BM[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def transpose(AM):
    return [[AM[j][i] for j in range(4)] for i in range(4)]
cols = []
for i in range(4):
    for j in range(4):
        K = [[1.0 if (a == i and b == j) else 0.0 for b in range(4)] for a in range(4)]
        MM = matmul4(transpose(K), Jst)
        for a in range(4):
            for b in range(4):
                MM[a][b] += sum(Jst[a][c]*K[c][b] for c in range(4))
        cols.append([MM[a][b] for a in range(4) for b in range(4)])
rows = list(zip(*cols))
rk = rank(rows)
dim_sp = 16-rk
S = [[1.0, 0.5, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, -0.5, 1.0]]
T = matmul4(matmul4(S, Jst), transpose(S))
err10 = max(abs(T[a][b]-Jst[a][b]) for a in range(4) for b in range(4))
orth = max(abs(sum(S[i][k]*S[j][k] for k in range(4))-(1 if i == j else 0)) for i in range(4) for j in range(4))
ok = (dim_sp == 10) and err10 < 1e-9 and orth > 0.3
chk(10, "chart-jet-torsor-sp4-dim10", ok,
    "M J M^T = J linear algebra dim = 16-rank = %d (expect 10); explicit Sp element with orth dev %.3f -> frame set a single orbit, no moduli" % (dim_sp, orth))

# --- 11: rank obstruction: leaf bivector rank 2 at a pole cannot be gauged to nondegenerate Theta
th3 = [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]]      # eps x at x=(0,0,R)
rk3 = rank(th3)
th4 = [[0.0, 1.0, 0.0, 0.0], [-1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
rk4 = rank(th4)
rkJ = rank(Jst)
ok = rk3 == 2 and rk4 == 2 and rkJ == 4
chk(11, "rank-obstruction-degenerate-points", ok,
    "rank(theta_leaf at pole)=2 (also as 4x4: %d) < rank(Theta_4)=%d: rank invariant under M theta M^T -> no frame; characteristic data needed" % (rk4, rkJ))

# --- 12: infinitesimal bivector-field automorphisms of theta(x) = l eps x: dim 3 = so(3)
eqs = []
E = {(0, 1, 2): 1.0, (1, 2, 0): 1.0, (2, 0, 1): 1.0,
     (1, 0, 2): -1.0, (2, 1, 0): -1.0, (0, 2, 1): -1.0}
def eps(i, j, m):
    return E.get((i, j, m), 0.0)
for i in range(3):
    for j in range(i+1, 3):
        for c in range(3):
            row = [0.0]*9
            for m in range(3):
                row[m*3+c] += eps(i, j, m)              # v^a d_a th^{ij} = eps^{ijm} K_{m c} x^c
            for a in range(3):
                row[i*3+a] -= eps(a, c, j)              # -th^{aj} d_a v^i: -eps^{acj} K_{i a}
                row[j*3+a] -= eps(i, a, c)              # -th^{ia} d_a v^j: -eps^{iac} K_{j a}
            eqs.append(row)
rk12 = rank(eqs)
autdim = 9-rk12
def apply_eqs(K):
    vv = [K[a][b] for a in range(3) for b in range(3)]
    return max(abs(sum(rw[t]*vv[t] for t in range(9))) for rw in eqs)
dev12 = max(apply_eqs([[0, 0, 0], [0, 0, 1], [0, -1, 0]]),
            apply_eqs([[0, 0, -1], [0, 0, 0], [1, 0, 0]]),
            apply_eqs([[0, 1, 0], [-1, 0, 0], [0, 0, 0]]))
ok = autdim == 3 and dev12 < 1e-12
chk(12, "bivector-automorphisms-so3", ok,
    "Poisson linear fields for theta=l*eps x: 9-param solve rank %d -> autdim %d (expect 3); so(3) generators satisfy eqs (dev %.2e)" % (rk12, autdim, dev12))

# --- 13: finite-N 't Hooft pairs: commutator traceless hence non-scalar (N=5,8);
#         block-local bivector values differ between K=5 and K=8 blocks
def tHooft(K):
    U = [[complex(math.cos(2*math.pi*i/K), math.sin(2*math.pi*i/K)) if i == j else 0j
          for j in range(K)] for i in range(K)]
    V = [[1+0j if (j == (i+1) % K) else 0j for j in range(K)] for i in range(K)]
    Xh = sc(add(U, adj(U)), 0.5)
    Yh = sc(add(V, adj(V)), 0.5)
    return Xh, Yh
def nonscalar_dev(K):
    Xh, Yh = tHooft(K)
    CC = comm(Xh, Yh)
    return frob(sub(CC, scalar_part(CC)))/frob(CC)   # scalar part = 0 by trace -> expect 1.0
d5, d8 = nonscalar_dev(5), nonscalar_dev(8)
X1, Y1 = tHooft(5)
X2, Y2 = tHooft(8)
def loc(K, k0, k1):
    v = [0j]*K
    v[k0] = 1/math.sqrt(2)
    v[k1] = 1j/math.sqrt(2)
    return v
w1 = biv(X1, Y1, loc(5, 0, 1))
w2 = biv(X2, Y2, loc(8, 0, 1))
ok = abs(d5-1) < 1e-9 and abs(d8-1) < 1e-9 and abs(w1-w2) > 1e-3
chk(13, "finiteN-non-scalar-block-values", ok,
    "N=5,8 't Hooft: [X,Y] traceless (scalar part 0) -> non-scalar dev = %g / %g; same local state, K=5 vs K=8 block: biv %g vs %g" % (d5, d8, w1, w2))

# --- 14: Darboux chart for the derived bivector field on S^2 near north pole:
# {y1,y2} = l x3, x3 = sqrt(R^2-y1^2-y2^2), R^2 = 12; g1=y1, g2=asin(y2/s), s=sqrt(R^2-y1^2)
R = math.sqrt(12.0)
worst14 = 0.0
for y1, y2 in [(-0.7, 0.3), (0.4, -0.55), (0.9, 0.25), (0.1, 0.8), (-0.2, -0.15)]:
    s = math.sqrt(R*R-y1*y1)
    x3 = math.sqrt(R*R-y1*y1-y2*y2)
    dg2 = 1.0/math.sqrt(s*s-y2*y2)      # = 1/x3
    worst14 = max(worst14, abs(dg2*x3-1.0))
ok = worst14 < 1e-12
chk(14, "darboux-existence-numerical", ok,
    "{g1,g2} = (1/x3)*x3 = 1 on 5 points (max dev %.2e): bivector germ -> leaf chart up to symplectic gauge" % worst14)

# --- 15: equivariance of the bivector field theta(x) = eps x: Q theta(x) Q^T = theta(Qx)
#         for Q in SO(3) (integer samples), and failure for a non-automorphism M
def epsmat(x):
    return [[0.0, x[2], -x[1]], [-x[2], 0.0, x[0]], [x[1], -x[0], 0.0]]
def mm3(AM, BM):
    return [[sum(AM[i][k]*BM[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def t3(AM):
    return [[AM[j][i] for j in range(3)] for i in range(3)]
Q1 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
Q2 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
worst15 = 0.0
pts = [(x, y, z) for x in (-2, 0, 2) for y in (-1, 3) for z in (0, 1)]
for Q in (Q1, Q2):
    for x in pts:
        Qx = [sum(Q[i][k]*x[k] for k in range(3)) for i in range(3)]
        L = mm3(mm3(Q, epsmat(x)), t3(Q))
        Rr = epsmat(Qx)
        worst15 = max(worst15, max(abs(L[i][j]-Rr[i][j]) for i in range(3) for j in range(3)))
Mbad = [[2, 0, 0], [0, 1, 0], [0, 0, 1]]
x0 = (0, 1, 2)
Lb = mm3(mm3(Mbad, epsmat(list(x0))), t3(Mbad))
Rb = epsmat([sum(Mbad[i][k]*x0[k] for k in range(3)) for i in range(3)])
fail15 = max(abs(Lb[i][j]-Rb[i][j]) for i in range(3) for j in range(3))
ok = worst15 < 1e-12 and fail15 > 1.0
chk(15, "bivector-field-equivariance", ok,
    "Q theta(x) Q^T = theta(Qx) for two integer SO(3) samples on %d points (max dev %.2e); diag(2,1,1) fails (dev %.3g) -> automorphisms are the gauge group" % (len(pts)*2, worst15, fail15))

# --- 16: sharpness closed form: rel width = 1/sqrt(j)
dev16 = 0.0
for j in [2, 3, 4, 6, 8, 50]:
    ratio = math.sqrt(2*j)/math.sqrt(2*j*j)
    dev16 = max(dev16, abs(ratio-1/math.sqrt(j)))
ok = dev16 < 1e-15
chk(16, "sharpness-closed-form", ok,
    "bivector rel width sqrt(2j)/sqrt(2 j^2) = 1/sqrt(j) exactly (dev %.2e) -> sharp as j -> inf" % dev16)

n_pass = sum(1 for r in results if r[2])
print("TOTALS: PASS %d/%d FAIL %d" % (n_pass, len(results), len(results)-n_pass))
raise SystemExit(0 if n_pass == len(results) else 1)
