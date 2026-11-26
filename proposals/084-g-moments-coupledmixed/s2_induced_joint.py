# s2_induced_joint.py (084) Exact induced joint law of (a,r) for the row-length Gaussian model.
# Slots w_i independent CN(0, s2*g_i); u_i = p_i + I q_i, sum|u_i|^2 = 1; alpha = sum conj(u_i) w_i;
# a = Im alpha; r = sum|w_i|^2 - |alpha|^2.  Real coords X_{2i}=Re w_i, X_{2i+1}=Im w_i,
# E[X_m X_n] = (s2*g_i/2) delta_mn.  Mixed moments via exact Isserlis.  Run from repo root:
#   python -I proposals/084-g-moments-coupledmixed/s2_induced_joint.py
import sympy as sp
from sympy import Rational, expand
def dataset(s2, gs, us):  # us: list of (p,q)
    D = len(gs); X = [sp.Symbol('X%d' % i) for i in range(2*D)]
    cov = {(2*i, 2*i): s2*gs[i]/2 for i in range(D)}
    cov.update({(2*i+1, 2*i+1): s2*gs[i]/2 for i in range(D)})
    def gmom(idx):
        if not idx: return Rational(1)
        i, rest = idx[0], idx[1:]
        return sum(cov.get((i, rest[k]), Rational(0)) * gmom(rest[:k] + rest[k+1:])
                   for k in range(len(rest)))
    def Eg(expr):
        p = sp.Poly(expand(expr), *X)
        return sum(c * gmom(sum([[j]*e for j, e in enumerate(mp) if e], []))
                   for mp, c in zip(p.monoms(), p.coeffs()))
    a = sum(us[i][0]*X[2*i+1] - us[i][1]*X[2*i] for i in range(D))
    are = sum(us[i][0]*X[2*i] + us[i][1]*X[2*i+1] for i in range(D))
    r = sum(X[2*i]**2 + X[2*i+1]**2 for i in range(D)) - are**2 - a**2
    return a, r, Eg
def run(s2, gs, us, name):
    a, r, Eg = dataset(s2, gs, us)
    mu = sum(g*(p*p+q*q) for g, (p, q) in zip(gs, us)); W = sum(gs)
    V = Eg(a*a); Gam = sum((p*p+q*q)*(g-mu)**2 for g, (p, q) in zip(gs, us))
    ch = {}
    ch['ar0'] = sp.simplify(Eg(a*r)) == 0
    ch['Vtie'] = sp.simplify(V - s2*mu/2) == 0
    ch['E_r'] = sp.simplify(Eg(r) - s2*(W-mu)) == 0
    ch['cov_a2r'] = sp.simplify(Eg(a*a*r) - V*Eg(r) - s2**2*Gam/2) == 0
    ch['a4'] = sp.simplify(Eg(a**4) - 3*V**2) == 0
    tr4 = Eg(32*(r*r + 8*a*a*r + 8*a**4))
    ch['tr4_excess'] = sp.simplify(tr4 - 32*(Eg(r*r) + 8*V*Eg(r) + 24*V**2) - 128*s2**2*Gam) == 0
    ch['gam'] = Gam > 0
    print(name, 'Gamma=%s' % Gam, {k: bool(v) for k, v in ch.items()})
    return ch
c1 = run(Rational(7,5), [Rational(11,10), Rational(3,10)],
         [(Rational(1,2), Rational(1,2)), (Rational(1,2), Rational(-1,2))], 'ds1 D=2 complex-u')
c2 = run(Rational(3,2), [Rational(1), Rational(1,2), Rational(1,3)],
         [(Rational(2,3), Rational(0)), (Rational(2,3), Rational(0)), (Rational(1,3), Rational(0))], 'ds2 D=3 real-u')
c4 = run(Rational(1), [Rational(2,5)]*3,
         [(Rational(2,3), Rational(0)), (Rational(2,3), Rational(0)), (Rational(1,3), Rational(0))], 'ds3 uniform-g')
a, r, Eg = dataset(Rational(1), [Rational(2,5)]*3,
                   [(Rational(2,3), Rational(0)), (Rational(2,3), Rational(0)), (Rational(1,3), Rational(0))])
V = Eg(a*a)
f5 = int(not (sp.simplify(Eg(a*a*r) - V*Eg(r)) == 0 and sp.simplify(Eg(a**4*r) - Eg(a**4)*Eg(r)) == 0
              and sp.simplify(Eg(a*a*r*r) - Eg(a*a)*Eg(r*r)) == 0))
allok = all(c.values() for c in (c1, c2, c4)) and f5 == 0
print('S2 invariant: uniform-g factorization (a _||_ r to checked orders) fail =', f5)
print('S2 OK' if allok else 'S2 FAIL')
