"""
060 / s4:
 (i) the equation of motion of S = S_b + S_gamma with the manuscript's signs,
     S_b = -(1/4g^2) Tr [A_mu,A_nu][A^mu,A^nu],  S_gamma = -(gamma/2g^2) Tr A_mu A^mu  (indices by h0),
     is [A^mu,[A_mu,A_nu]] = gamma A_nu: finite-difference gradient at random Hermitian matrices.
 (ii) invariant measure of the hyperboloid y_A y^A = -c (A = 0..4, eta = diag(-1,1,1,1,1)) in the
     coordinates y^mu (mu = 0..3) on each sheet of m = y^4: d^4y / |m|; invariance of d^4(y_i,m)/|y0| under
     a boost checked by the Jacobian.
 (iii) dilaton rho^2 = rho_M |det gamma^{mu nu}|^{1/2} and coupling g^2 ~ 1/rho^2 (2605.13294, Eqs. 34, 104
     and the dilaton definition) for the conjugate presentation (gamma = m^2 eta^{-1}) and the base
     presentation ([gamma] = diag(m^2,(2c-m^2)/3,..) at rest).
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(7)
N, D = 4, 5
h0 = np.diag([-1.] + [1.]*(D-1))
def herm():
    X = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)); return (X + X.conj().T)/2
def comm(X, Y): return X @ Y - Y @ X
def S(A, gam):
    s = 0
    for mu in range(D):
        for nu in range(D):
            s += -0.25*h0[mu, mu]*h0[nu, nu]*np.trace(comm(A[mu], A[nu]) @ comm(A[mu], A[nu]))
    s += -0.5*gam*sum(h0[mu, mu]*np.trace(A[mu] @ A[mu]) for mu in range(D))
    return s.real
gam = 0.37
A = [herm() for _ in range(D)]
dA = [herm() for _ in range(D)]
e = 1e-6
num = (S([a + e*d for a, d in zip(A, dA)], gam) - S([a - e*d for a, d in zip(A, dA)], gam))/(2*e)
# predicted: dS = sum_nu h0^{nu nu} Tr dA_nu ( [A^mu,[A_mu,A_nu]] - gamma A_nu )
pred = 0
for nu in range(D):
    box = sum(h0[mu, mu]*comm(A[mu], comm(A[mu], A[nu])) for mu in range(D))
    pred += h0[nu, nu]*np.trace(dA[nu] @ (box - gam*A[nu]))
print(f"(i) dS numeric {num:.10f}  vs  sum h0 Tr dA ([A^mu,[A_mu,A_nu]] - gamma A_nu) = {pred.real:.10f}")
print("    so the equation of motion is [A^mu,[A_mu,A_nu]] = gamma A_nu")

y1, y2, y3, m, c = sp.symbols('y1 y2 y3 m c', real=True)
y0 = sp.sqrt(c + y1**2 + y2**2 + y3**2 + m**2)
J = sp.diff(y0, m)
print("(ii) d y0/d m =", sp.simplify(J), " => d^4(y_i, m)/y0 = d^3y_i d y0 /|m|  (since dm = y0 dy0 / m)")
# invariance of d^4(y_i,m)/y0 under a boost in the (0,1) plane, numerically by Jacobian
def to5(p, cc=1.0):
    yi, mm = p[:3], p[3]
    return np.array([np.sqrt(cc + yi@yi + mm*mm), *yi, mm])
def boostmap(p, b=0.8):
    Y = to5(p)
    Bm = np.eye(5); Bm[0, 0] = Bm[1, 1] = np.cosh(b); Bm[0, 1] = Bm[1, 0] = np.sinh(b)
    Yp = Bm @ Y
    return np.array([Yp[1], Yp[2], Yp[3], Yp[4]])
worst = 0
for k in range(5):
    p = rng.normal(size=4)
    Jm = np.zeros((4, 4)); h = 1e-6
    for j in range(4):
        dp = np.zeros(4); dp[j] = h
        Jm[:, j] = (boostmap(p + dp) - boostmap(p - dp))/(2*h)
    lhs = abs(np.linalg.det(Jm))/to5(boostmap(p))[0]
    rhs = 1/to5(p)[0]
    worst = max(worst, abs(lhs/rhs - 1))
print(f"    boost invariance of d^4(y_i,m)/y0: max relative deviation {worst:.1e}")

mm = sp.symbols('m', positive=True)
rhoM = 1/mm
conj = rhoM*sp.sqrt(sp.Abs(sp.det(sp.diag(mm**2, mm**2, mm**2, mm**2))))
base = rhoM*sp.sqrt(sp.Abs(sp.det(sp.diag(mm**2, (2*c - mm**2)/3, (2*c - mm**2)/3, (2*c - mm**2)/3))))
print("(iii) conjugate presentation: rho^2 ~", sp.simplify(conj), " -> g^2 ~ |m|^-3 (2605.13294 Eq. 104: r^4/(2 sinh^3 tau))")
print("      base presentation:      rho^2 ~", sp.simplify(base), " -> g^2 ~ |2c - m^2|^(-3/2), finite on 0 <= m^2 < 2c")
