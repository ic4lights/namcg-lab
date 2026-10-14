"""
Independent cross-check of the O(eps^2) average of rho*R[g_rho] against the Fierz-Pauli form:
   <(rho R)^(2)>  =  <  rho0 * L_FP(h1) + rho1 * R^(1)[h1] >
   L_FP = -1/4 d_l h_mn d^l h^mn + 1/2 d_m h^mn d^l h_ln - 1/2 d_m h^mn d_n h + 1/4 d_l h d^l h,   R^(1) = d_m d_n h^mn - Box h
(indices moved with the constant background metric g0; sphere-positive curvature convention; det g_rho = 1 so h1 is g0-traceless).
Same setup as check_quadratic_form.py; compares the resulting 4x4 matrix with the stored Mh.
Usage: python check_fp_crosscheck.py s0 a0 b0 p0 p1 p2 p3
"""
import sympy as sp, sys
s0 = sp.Rational(sys.argv[1]); a0 = sp.Rational(sys.argv[2]); b0 = sp.Rational(sys.argv[3])
pv = [sp.Rational(v) for v in sys.argv[4:8]]
eps, th = sp.symbols('eps th'); u = sp.symbols('u0:4'); n = 4
eta = sp.diag(s0, 1, 1, 1); etai = eta.inv()
Tb = sp.zeros(4, 4); Tb[0, 1] = a0; Tb[1, 0] = -a0; Tb[2, 3] = b0; Tb[3, 2] = -b0
A = [u[m]*sp.cos(th) for m in range(n)]
dA = lambda m, k: pv[k]*sp.diff(A[m], th)
T = sp.Matrix(n, n, lambda m, k: sum(Tb[m, r]*dA(k, r) for r in range(n)) - sum(Tb[k, r]*dA(m, r) for r in range(n)))
Th = Tb + eps*T
def dual(M):
    return sp.Matrix(n, n, lambda m, k: sum(sp.LeviCivita(m, k, r, s)*M[r, s] for r in range(n) for s in range(n))/2)
Pf = Th[0, 1]*Th[2, 3] - Th[0, 2]*Th[1, 3] + Th[0, 3]*Th[1, 2]
Ts = dual(Th)
g = (Ts*etai*Ts.T)/Pf
g0 = g.subs(eps, 0); g0i = g0.inv()
h = g.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0))
rho1 = sp.diff(1/Pf, eps).subs(eps, 0); rho0 = (1/Pf).subs(eps, 0)
dm = lambda f, m: pv[m]*sp.diff(f, th)
hup = g0i*h*g0i
hl = h
trh = sum(g0i[a, b]*h[a, b] for a in range(n) for b in range(n))
print("trace of h1 (should be 0):", sp.simplify(trh))
# explicit contractions
def contr_dd():   # d_l h_mn d^l h^mn
    return sum(g0i[l, k]*dm(h[m, nn], l)*dm(h[a, b], k)*g0i[m, a]*g0i[nn, b]
               for l in range(n) for k in range(n) for m in range(n) for nn in range(n) for a in range(n) for b in range(n))
def divh(nn):    # d_m h^mn  (upper n)
    return sum(dm(hup[m, nn], m) for m in range(n))
t2 = sum(g0[nn, k]*divh(nn)*divh(k) for nn in range(n) for k in range(n))
t3 = sum(dm(trh, nn)*divh(nn) for nn in range(n))*(1)
t4 = sum(g0i[l, k]*dm(trh, l)*dm(trh, k) for l in range(n) for k in range(n))
LFP = -sp.Rational(1, 4)*contr_dd() + sp.Rational(1, 2)*t2 - sp.Rational(1, 2)*t3 + sp.Rational(1, 4)*t4
R1 = sum(dm(dm(hup[m, nn], m), nn) for m in range(n) for nn in range(n)) - sum(g0i[l, k]*dm(dm(trh, l), k) for l in range(n) for k in range(n))
L2 = sp.expand(rho0*LFP + rho1*R1)
q = sp.expand(sp.integrate(L2, (th, 0, 2*sp.pi))/(2*sp.pi))
M = sp.Matrix(n, n, lambda i, j: sp.diff(q, u[i], u[j])/2)
print("FP cross-check matrix:", M.tolist())
