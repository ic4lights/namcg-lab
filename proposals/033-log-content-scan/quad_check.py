"""Second-order check at the origin of a cubic potential about Theta-bar=(eta^3)^-1, eps=1/1000:
 (v_a2 - 4 s_a2)/eps^2 vs (1/12) tr Omega^(1)2 /eps^2 ;  Dirac d_a2 - 4 s_a2 vs (1/2)(v_a2-4 s_a2) ; X^(1): trE2 of vector minus 4 e^2 ~ 0."""
import random, itertools, sympy as sp
from common import *
import jetlib as jl
from jetlib import Jet
import geom, lib
import lin_lib as L
use_gaussian(3)
gm = gam_mn_domain()
wbar = lib.eta3()[2]; Thb = wbar.inv()
def cc(z):
    z = z.c0() if hasattr(z,'c0') else z
    return sp.sympify(QQ_I.to_sympy(z))
for seed in (5,6):
    random.seed(seed)
    C=[[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for tri in itertools.combinations_with_replacement(range(4),3):
            val=sp.Rational(random.randint(-3,3),random.randint(1,3))
            for perm in set(itertools.permutations(tri)): C[mu][perm[0]][perm[1]][perm[2]]=val
    eps=sp.Rational(1,1000)
    A=[]
    for mu in range(4):
        d={}
        for tri in itertools.combinations_with_replacement(range(4),3):
            mon=[0]*4
            for t in tri: mon[t]+=1
            val=eps*C[mu][tri[0]][tri[1]][tri[2]]/6*len(set(itertools.permutations(tri)))
            if val!=0: d[tuple(mon)]=QQ_I.from_sympy(sp.Rational(val))
        A.append(Jet(d))
    w=omega_from_A(A)
    w=[[w[m][n]+Jet.const(QQ_I.from_sympy(sp.Integer(int(wbar[m,n])))) for n in range(4)] for m in range(4)]
    Th=theta_from_omega(w)
    out,sg,base=geom.sector_all(Th,gm)
    s=cc(out['scalar'][1]); v=cc(out['vector'][1]); dd=cc(out['dirac'][1])
    S0=L.cubic_S([[[[eps*C[m][a][b][c] for c in range(4)] for b in range(4)] for a in range(4)] for m in range(4)])
    lin=L.linear_data(Thb,S0)
    print('seed',seed,' (v-4s)/eps^2 =',float((v-4*s)/eps**2),' (1/12)trOm2/eps^2 =',float(lin['trOm2']/12/eps**2),
          ' (d-4s)/(v-4s) =',float((dd-4*s)/(v-4*s)),' s/eps^2 =',float(s/eps**2),' C2/120/eps^2',float(lin['C2']/120/eps**2),' Euler',float(lin['Euler']/eps**2))
