"""
Split <(rho R)^(2)> = rho0 <L_FP(h1)> + <rho1 R^(1)[h1]> and find the generalized eigenvalues (relative to M_Max, on the gauge quotient)
of each piece, to see how a position-dependent cutoff  Lambda^2(x) = Lambda0^2 f(rho),  f = rho^s  (term  f(rho) rho R)  changes the three modes:
   (rho^{s+1} R)^(2) = rho0^s [ rho0 R^(2)  + (s+1) rho1 R^(1) ]  = rho0^s [ <rho R>^(2) + s * rho1 R^(1) ]
Usage: python check_cutoff_split.py s0 a0 b0 p0 p1 p2 p3
"""
import sympy as sp, sys
exec(open('check_fp_crosscheck.py').read().split("L2 = sp.expand(rho0*LFP + rho1*R1)")[0].replace("sys.argv[1]", "sys.argv[1]"))
lam = sp.symbols('lam')
def avgmat(L):
    q = sp.expand(sp.integrate(sp.expand(L), (th, 0, 2*sp.pi))/(2*sp.pi))
    return sp.Matrix(n, n, lambda i, j: sp.diff(q, u[i], u[j])/2)
M_fp = avgmat(rho0*LFP); M_r1 = avgmat(rho1*R1)
q = Tb*sp.Matrix(pv); ql = eta*q; q2 = (q.T*eta*q)[0]
MMax = q2*eta - ql*ql.T
for drop in range(4):
    if q[drop] != 0: break
idx = [i for i in range(4) if i != drop]
E = sp.zeros(4, 3)
for c_, i in enumerate(idx): E[i, c_] = 1
rho0v = rho0
p2 = (sp.Matrix(pv).T*etai*sp.Matrix(pv))[0]
for name, M in (('rho0*L_FP(h1)', M_fp), ('rho1*R1', M_r1), ('sum = (rho R)^(2)', M_fp + M_r1)):
    cp = sp.factor((E.T*M*E - lam*E.T*MMax*E).det())
    print(name, ": char poly of (M - lam M_Max) on the quotient:", cp, "   [p^2_eta =", p2, ", rho0 =", rho0v, "]")
