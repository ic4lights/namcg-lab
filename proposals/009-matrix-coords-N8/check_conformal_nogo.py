"""
D-independent no-go: 4D symplectic brane in R^{1,D-1} (any D>=4), real Lorentzian induced metric g, symplectic form omega
(theta = omega^{-1}).  Operator metric: G = (theta^T g theta)^{-1} = omega g^{-1} omega^T.  Claim: G != c g for every c.
Proof: G = c g  <=>  M^2 = -c, M = g^{-1} omega (g-antisymmetric).  Real M, M^2=-c => c>0 (sign of G vs g) and eigenvalues
+-i sqrt(c) in conjugate pairs => det M = c^2 > 0; but det M = Pf(omega)^2/det g < 0 for Lorentzian g.
Checks: symbolic identities; random embeddings D=4..11; closed-form least-squares c and residual; Euclidean contrast.
"""
import numpy as np, sympy as sp
rng = np.random.default_rng(3)
import random
random.seed(5)
def rat(): return sp.Rational(random.randint(-6,6), random.randint(1,4))
ok1=ok2=ok3=True
for _ in range(30):
    w=[rat() for _ in range(6)]
    om = sp.Matrix([[0,w[0],w[1],w[2]],[-w[0],0,w[3],w[4]],[-w[1],-w[3],0,w[5]],[-w[2],-w[4],-w[5],0]])
    Pf = w[0]*w[5]-w[1]*w[4]+w[2]*w[3]
    A = sp.Matrix(4,4,lambda i,j: rat()); eta=sp.diag(-1,1,1,1)
    g = A.T*eta*A
    if g.det()==0 or Pf==0: continue
    M = g.inv()*om
    ok1 &= (om.det()==Pf**2)
    ok2 &= (M.det()==Pf**2/g.det())
    ok3 &= ((om*g.inv()*om.T + g*M*M)==sp.zeros(4,4))
    assert g.det()<0 and M.det()<0
print("exact rational: det(omega)=Pf^2 %s; det M = Pf^2/det g (<0) %s; G = -g M^2 %s"%(ok1,ok2,ok3))
def rand_om():
    a = rng.normal(size=(4,4)); return a-a.T
for D in range(4,12):
    eta = np.diag([-1.]+[1.]*(D-1)); minres = np.inf; n=0
    for _ in range(3000):
        dx = rng.normal(size=(D,4)); gm = dx.T@eta@dx
        if np.linalg.det(gm) >= 0: continue
        o = rand_om(); G = o@np.linalg.inv(gm)@o.T
        c = np.sum(G*gm)/np.sum(gm*gm)
        res = np.linalg.norm(G-c*gm)/np.linalg.norm(G); minres=min(minres,res); n+=1
    print("D=%2d Lorentzian samples %4d  min relative residual |G-c g|/|G| = %.3e"%(D,n,minres))
# contrast: Euclidean g with g-orthogonal complex structure: G = c g attainable
gE = np.eye(4); J = np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0.]]); o = gE@J
G = o@np.linalg.inv(gE)@o.T
print("Euclidean contrast: G = g?", np.allclose(G,gE))
# Kleinian (2,2) contrast
gK = np.diag([-1,-1,1,1.]); J = np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0.]]); o = gK@J
G = o@np.linalg.inv(gK)@o.T
print("Kleinian (2,2) contrast: G proportional to g?", np.allclose(G,-gK) or np.allclose(G,gK))
