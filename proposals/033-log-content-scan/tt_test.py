"""Plane-wave test about Theta-bar = (eta^3)^-1 (SD, G=delta, rho=1).  Amplitude S = p p (p^v).
Reports per mode: delta ln rho Hessian (0 for delta-rho=0 modes), R, C^2, Euler (should be 0: total derivative),
T-side kappa_J = (1/12) sum tr(Omega Omega)/C^2, A-side tau vs (W,Rsig,R) and tau + Rj."""
import random, sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib
Thb = lib.eta3()[2].inv()
random.seed(3)
out=[]
def rnd(): return Q(random.randint(-4,4), random.randint(1,3))
rows=[]
for trial in range(8):
    p=[rnd() for _ in range(4)]
    if all(x==0 for x in p): continue
    # choose v with delta-rho=0: tr(Theta w)=0 with w=p^v  <=> v . (Theta^T p-type) = 0 ; solve linear condition on v
    v=sp.symbols('v0:4')
    S,w=L.hat_S(p,list(v))
    cond=sp.expand((Thb*w).trace())
    # pick random v satisfying cond
    vv=[rnd() for _ in range(3)]
    sol=sp.solve(cond.subs({v[0]:vv[0],v[1]:vv[1],v[2]:vv[2]}),v[3],dict=True)
    if not sol:
        continue
    vals={v[0]:vv[0],v[1]:vv[1],v[2]:vv[2],v[3]:sol[0][v[3]]}
    vnum=[x.subs(vals) for x in v]
    S,w=L.hat_S(p,vnum)
    d=L.linear_data(Thb,S)
    if d['C2']==0: continue
    kJ=sp.Rational(1,12)*d['trOm2']/d['C2']
    print('p',p,'v',vnum,'dlnrho',d['D2lnrho'][(0,0)],'R',d['R'],'Euler',d['Euler'],'C2',d['C2'],'kappa_J',kJ,'tau',d['tau'],'Rj',d['Rj'],'tau+Rj',d['tau']+d['Rj'],'W',d['W'],'Rsig',d['Rsig'])
    rows.append((d['tau'],d['W'],d['Rsig'],d['R'],d['Rii'],d['Rj']))
M=sp.Matrix([[r[1],r[2],r[3]] for r in rows]); y=sp.Matrix([r[0] for r in rows])
print('rank [W,Rsig,R]',M.rank(),'rank with tau',M.row_join(y).rank())
sol=sp.linsolve((M,y))
print('fit tau = a W + b Rsig + c R :',sol)
