import numpy as np, sympy as sp
from scipy.stats import gamma as gammad
rng = np.random.default_rng(7)
N = 400000
gv = np.array([1.0, 2.0, 3.0]); D = 3
def pdraw(shape):  # |w_i|^2 = s^2 g_i * xi_i, xi iid Gamma(shape, 1/sqrt(shape)) (mean 1)
    xi = rng.gamma(shape, 1.0/np.sqrt(shape), size=(N, D))
    E = gv * xi
    return E / E.sum(axis=1, keepdims=True)
p1_ = pdraw(1.0); p2_ = pdraw(2.0)
print('shape-dependence: E[p1] shape1=%.5f shape2=%.5f (differ: induced law depends on fiber shape)'
      % (p1_[:,0].mean(), p2_[:,0].mean()))
gu = np.array([1.0, 1.0, 1.0])
def pdrawu(shape):
    xi = rng.gamma(shape, 1.0/np.sqrt(shape), size=(N, D))
    E = gu * xi
    return E / E.sum(axis=1, keepdims=True)
pu = pdrawu(1.0); pv = pdrawu(2.0)
# exchangeability at uniform g: E[p1 p2] equal for any pair, and distribution invariant under a fixed permutation
perm = [2, 0, 1]
print('uniform-g exchangeable: |E[p1p2]-E[p1p3]|=%.5f, |E[p1]-E[p3]|=%.5f; shape2: |E[p1p2]-E[p2p3]|=%.5f'
      % (abs((pu[:,0]*pu[:,1]).mean()-(pu[:,0]*pu[:,2]).mean()), abs(pu[:,0].mean()-pu[:,2].mean()),
         abs((pv[:,0]*pv[:,1]).mean()-(pv[:,1]*pv[:,2]).mean())))
print('uniform-g perm-invariance (Gamma2): KS-ish |mean p - mean sigma p|=%.5f'
      % abs(pv.mean(axis=0) - pv[:, perm].mean(axis=0)).max())
# equivariance: g and its permutation swap expectations
gp = np.array([2.0, 1.0, 3.0])  # swap slots 1,2
def pdrawg(gvec):
    E = gvec * rng.gamma(1.0, 1.0, size=(N, D))
    return E / E.sum(axis=1, keepdims=True)
pa = pdrawg(gv); pb = pdrawg(gp)
print('equivariance: E[p] at g=%s is %s ; at swapped g %s is swapped %s (maxdiff %.4f)'
      % (gv, np.round(pa.mean(axis=0), 4), gp, np.round(pb.mean(axis=0)[[1,0,2]], 4),
         np.abs(pa.mean(axis=0) - pb.mean(axis=0)[[1,0,2]]).max()))
# identifiability (D=2 exact): density determines (1/g1,1/g2) up to scale
g1, g2, t = sp.symbols('g1 g2 t', positive=True)
f2 = 1/(g1*g2*(t/g1+(1-t)/g2)**2)
c1 = sp.simplify(f2.subs(t, sp.Rational(1, 3)))
c2 = sp.simplify(f2.subs(t, sp.Rational(2, 3)))
a, b = sp.symbols('a b', positive=True)   # a=1/g1, b=1/g2 up to scale 1/s: solve f(1/3),f(2/3) given
S = sp.symbols('S', positive=True)        # scale: f = S/(a t + b(1-t))^2 ; match two values + note scale free
sol = sp.solve([sp.Eq(S/(a/3+2*b/3)**2, c1), sp.Eq(S/(2*a/3+b/3)**2, c2)], [a, b], dict=True)
print('identifiability D=2: from 2 density values, (1/g1,1/g2) proportional solution:',
      [{k: sp.simplify(v) for k, v in s.items()} for s in sol])
