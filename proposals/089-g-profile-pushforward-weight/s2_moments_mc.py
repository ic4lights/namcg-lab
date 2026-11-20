import numpy as np, sympy as sp
from fractions import Fraction
rng = np.random.default_rng(20261118)
gv = np.array([1.0, 2.0, 3.0]); D = 3; N = 400000
# slot draws: proper complex gaussian |w|^2 ~ Exp(mean s^2 g_i); use s^2=1
E = rng.exponential(gv, size=(N, D))
p = E / E.sum(axis=1, keepdims=True)
# (a) density vs MC on box B: p1 in [0.15,0.25], p2 in [0.45,0.55] (area = 0.01)
B = (p[:, 0] >= 0.15) & (p[:, 0] <= 0.25) & (p[:, 1] >= 0.45) & (p[:, 1] <= 0.55)
volB = 0.1*0.1  # box [0.15,0.25]x[0.45,0.55] in (p1,p2) coords
empB = B.mean() / volB
G = np.prod(gv)
def fdens(px):
    return __import__("math").factorial(D-1) / (G * (px @ (1.0/gv))**D)
mid = np.array([0.20, 0.50, 0.30])
exactB_mid = fdens(mid)
print('(a) simplex box density MC=%.4f exact(mid)=%.4f' % (empB, exactB_mid))
# (b) exact E[p1] D=2 closed form vs MC ; formula from sympy
g1, g2, t = sp.symbols('g1 g2 t', positive=True)
Ep1 = sp.integrate(t/(g1*g2*(t/g1+(1-t)/g2)**2), (t, 0, 1))
Ep1f = sp.lambdify((g1, g2), sp.simplify(Ep1))
E2 = rng.exponential([2.0, 5.0], size=(N, 2)); p2 = E2/E2.sum(axis=1, keepdims=True)
print('(b) E[p1] D=2 g=(2,5): MC=%.6f exact=%.6f' % (p2[:,0].mean(), Ep1f(2.0, 5.0)))
# (c) Haar frame moments: sample u ~ complex gaussian, normalize; Dirichlet(1,..,1)
def haaq(D, n):
    u = rng.standard_normal((n, D)) + 1j*rng.standard_normal((n, D))
    q = np.abs(u)**2; return q / q.sum(axis=1, keepdims=True)
for D2 in (3, 4):
    q = haaq(D2, N)
    m_exact = float(sp.factorial(D2-1)*sp.factorial(2)*sp.factorial(1)/sp.factorial(D2-1+3))
    print('(c) D=%d E[q1^2 q2] MC=%.6f exact Dirichlet=%.6f' % (D2, (q[:,0]**2*q[:,1]).mean(), m_exact))
# (d) factorization: E[p1*q1] = E[p1]*E[q1] (independent slot/frame)
qs = haaq(3, N)
print('(d) E[p1 q1] MC=%.6f  E[p1]MC*E[q1]MC=%.6f' % ((p[:,0]*qs[:,0]).mean(), p[:,0].mean()*qs[:,0].mean()))
# (e) uniform g: E[p1] -> 1/D
gu = rng.exponential(1.0, size=(N, 4)); pu = gu/gu.sum(axis=1, keepdims=True)
print('(e) uniform g D=4 E[p1] MC=%.6f exact 0.25' % pu[:,0].mean())
# (f) mode concentration: mass in {p1>0.9} vs {p3>0.9}  (argmax g is slot 3)
print('(f) frac(p1>0.9)=%.5f frac(p3>0.9)=%.5f  (max-variance slot dominates)' %
      ((p[:,0] > 0.9).mean(), (p[:,2] > 0.9).mean()))
# (g) flat-prior D=2 marginal h(t)=2*int_0^1 u(1-u)/(u t+(1-u)(1-t))^2 duu = sp.symbols('u', positive=True)
u = sp.symbols('u', positive=True)
h = sp.simplify(2*sp.integrate(u*(1-u)/(u*t+(1-u)*(1-t))**2, (u, 0, 1)))
hf = sp.lambdify(t, h.rewrite(sp.log))
print('(g) h(1/2) exact limit=%s; h(0.05)=%.4f h(0.005)=%.4f h(0.0005)=%.4f; h(t)=h(1-t): %s' % (
  str(sp.limit(h, t, sp.Rational(1, 2))), hf(0.05), hf(0.005), hf(0.0005),
  str(sp.simplify(h - h.subs(t, 1 - t)) == 0)))
