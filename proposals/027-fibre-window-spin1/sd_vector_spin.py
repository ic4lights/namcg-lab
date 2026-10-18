"""027 script 2: vector sector of the invariant (fibre-constant) sector, four-matrix class.
(a) Casimir identity: with Sigma the vector-index generators, C_G = 1/2 eta eta (J+Sigma)(J+Sigma), the cross term eta_{ac} eta_{bd} J^{ab} Sigma^{cd} equals -2 s J_{ab} A^b (checked symbolically on a test field), so H_V = -Box - 2sJ_{ab}A^b + mu^2 = C_G - C_41 - C_Sigma + mu^2.
(b) SD first coefficient of exp(P_V), P_V = t Delta_4 - i s H_V  (rank 4, lower-index components A_c) computed with 4x4 matrix connection; compare tr(E+R/6) with
    4*(scalar E+R/6) + 6 s^2 (1+a^2)/(t + i s a^2) - 4 i s mu^2 .   (closed form of the spin term derived analytically in the proposal)."""
import sympy as sp
from sd_core import *
y = sp.symbols('y0:4', real=True); ell, t, s, mu2 = sp.symbols('ell t s mu2', positive=True)
eta = sp.diag(-1, 1, 1, 1)
yl = [sum(eta[i, j]*y[j] for j in range(4)) for i in range(4)]
yy = sum(y[i]*yl[i] for i in range(4))
m2 = -yy - ell**2
# ---- (a) Casimir identity on a test vector field, lower components A_c(y)
sb = sp.symbols('sb')   # bracket sign (+1 or -1) substituted below
fA = [sp.Function('A%d' % c)(*y) for c in range(4)]
def Jup(a, b, F, sgn):                       # J^{ab} F = sgn*(y^b d^a - y^a d^b) F  (acting on a function F(y)); d^a = eta^{ac} d_c
    return sgn*(y[b]*eta[a, a]*sp.diff(F, y[a]) - y[a]*eta[b, b]*sp.diff(F, y[b]))
def Sig(a, b, vec, sgn2):                    # (Sigma^{ab} A)_c with lower index: (Sigma^{ab})_c^d A_d = sgn2*(delta^a_c eta^{bd} - delta^b_c eta^{ad}) A_d
    out = []
    for c in range(4):
        out.append(sgn2*((1 if a == c else 0)*eta[b, b]*vec[b] - (1 if b == c else 0)*eta[a, a]*vec[a]))
    return out
def Jvec(a, b, vec, sgn):
    return [Jup(a, b, v, sgn) for v in vec]
def tot(a, b, vec, sgn, sgn2):
    j = Jvec(a, b, vec, sgn); sg = Sig(a, b, vec, sgn2)
    return [j[c] + sg[c] for c in range(4)]
def is_rep(sgn, sgn2):
    # check [tot^{01}, tot^{12}] = (+-) tot^{02}-type closure  on a test field:  compare commutator with sgn*(eta^{11} tot^{02}) from {M^{ab},M^{cd}} = sgn(eta^{ac} M^{bd} - ...)
    v = fA
    lhs1 = tot(0, 1, tot(1, 2, v, sgn, sgn2), sgn, sgn2); lhs2 = tot(1, 2, tot(0, 1, v, sgn, sgn2), sgn, sgn2)
    comm = [sp.simplify(lhs1[c] - lhs2[c]) for c in range(4)]
    # {M^{01},M^{12}} = sgn*( -eta^{11} M^{02} ) from  eta^{AC}M^{BD} - eta^{AD}M^{BC} - eta^{BC}M^{AD} + eta^{BD}M^{AC}, A=0,B=1,C=1,D=2: -eta^{11}M^{02}... 
    rhs = tot(0, 2, v, sgn, sgn2); rhs = [-sgn*eta[1, 1]*r for r in rhs]
    return all(sp.simplify(comm[c] - rhs[c]) == 0 for c in range(4))
for sg2 in (1, -1):
    print("Sigma sign", sg2, "forms a representation together with J (bracket sign +1):", is_rep(1, sg2))
sg, sg2 = 1, [x for x in (1, -1) if is_rep(1, x)][0]
# C_G, C_31, C_Sigma, cross
def contract(op1, op2):
    return None
def C_cross(vec, sgn, sgn2):
    # eta_{ac} eta_{bd} J^{ab} Sigma^{cd} summed over all a,b (= 2 * sum_{a<b})
    out = [0]*4
    for a in range(4):
        for b in range(4):
            if a == b: continue
            w = eta[a, a]*eta[b, b]
            sv = Sig(a, b, vec, sgn2)
            jv = Jvec(a, b, sv, sgn)
            for c in range(4): out[c] += w*jv[c]
    return out
cross = C_cross(fA, sg, sg2)
# -2 s J_{ab} A^b with lower components: -2 s * s(y_b d_a - y_a d_b) A^b = -2 (y^c d_a A_c - y_a d^c A_c)
Y = [-2*(sum(y[c]*sp.diff(fA[c], y[a]) for c in range(4)) - yl[a]*sum(eta[c, c]*sp.diff(fA[c], y[c]) for c in range(4))) for a in range(4)]
print("cross term (J.Sigma, unit coefficient, both orderings summed) vs  -2 s J_{ab} A^b:",
      [sp.simplify(cross[c] - Y[c]) for c in range(4)], " | with opposite sign:", [sp.simplify(cross[c] + Y[c]) for c in range(4)])

ginv4 = sp.Matrix(4, 4, lambda i, j: eta[i, j] + y[i]*y[j]/ell**2)
# ---- (b) matrix SD  (numeric t, s, ell, mu2 substituted before differentiation; y symbolic)
print("(b) matrix-valued SD first coefficient")
z0, w0, a = sp.symbols('z0 w0 a', positive=True)
C = 1 + a**2; c4 = 8*a**4 + 8*a**2 + 1
D1 = -(-5*w0**2*z0*(c4 - 1) + 16*w0*z0*(w0*C + z0)*(3*C - 2) + (32*w0 + 64*z0)*(w0*C + z0)**2)/(32*(w0*C + z0)**2)
for (tt, ss, ee, y0v, y1v, mm) in [(sp.Rational(1, 3), sp.Rational(1, 2), 1, 2, 0, -3), (sp.Rational(2, 1), sp.Rational(-1, 3), sp.Rational(3, 2), 3, 1, -3), (sp.Rational(1, 5), 1, 2, 5, 0, 1)]:
    sub = {t: tt, s: ss, ell: ee, mu2: mm}
    m2n = m2.subs(sub)
    ginv4n = ginv4.subs(sub); sqrtg4n = ee/sp.sqrt(m2n)
    ADn = [ee**2*sum(sp.diff(sqrtg4n*ginv4n[i, j], y[i]) for i in range(4))/sqrtg4n for j in range(4)]
    ABoxn = [-y[j] for j in range(4)]
    Ginv_n = tt*ee**2*ginv4n + sp.I*ss*m2n*sp.Matrix(4, 4, lambda i, j: eta[i, j])
    ppn = tt*ee**2 + sp.I*ss*m2n
    Gcov_n = sp.Matrix(4, 4, lambda i, j: eta[i, j]/ppn - tt*yl[i]*yl[j]/(ppn*m2n*(sp.I*ss - tt)))
    def Xm(mu):
        return sp.Matrix(4, 4, lambda aa, c: 2*sp.I*ss*(y[c]*(1 if mu == aa else 0) - yl[aa]*eta[mu, c]))
    Amat = [(tt*ADn[j] + sp.I*ss*ABoxn[j])*sp.eye(4) + Xm(j) for j in range(4)]
    Bmat = -sp.I*ss*mm*sp.eye(4)
    pt = {y[0]: y0v, y[1]: y1v, y[2]: 0, y[3]: 0}
    trE, R6, Em = sd_first(Ginv_n, Amat, Bmat, y, pt, rank=4, Gcov=Gcov_n)
    m2v = y0v**2 - y1v**2 - ee**2
    aval = sp.sqrt(m2v)/ee
    sc = D1.subs({z0: tt - sp.I*ss, w0: sp.I*ss, a: aval})
    spin = 6*ss**2*(1 + aval**2)/(tt + sp.I*ss*aval**2)
    pred = 4*sc + spin - 4*sp.I*ss*mm
    full = trE + 4*R6
    print("t=%s s=%s ell=%s y=(%s,%s,0,0) a^2=%s mu2=%s | tr(E+R/6) = %s | 4 D1_scalar + 6 s^2 (1+a^2)/(t+i s a^2) - 4 i s mu^2 = %s | diff %s" % (tt, ss, ee, y0v, y1v, sp.nsimplify(aval**2), mm, sp.N(full, 12), sp.N(pred, 12), sp.N(full - pred, 3)))
