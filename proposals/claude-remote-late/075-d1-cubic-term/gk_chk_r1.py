import sympy as sp, itertools, numpy as np
from sympy.combinatorics import Permutation
eta=sp.diag(-1,1,1,1)
eps=sp.MutableDenseNDimArray.zeros(4,4,4,4)
for p in itertools.permutations(range(4)):
    eps[p]=Permutation(list(p)).signature()  # eps_{0123}=+1 lower
v=sp.symbols('v0:4'); vu=list(v)  # upper components
# cbar_{ab}^d = 1/2 eps_{ab}{}^{d}{}_{f} v^f : eps_ab^d_f = eps_{abgf} eta^{gd}
def c(a,b,d): return sp.Rational(1,2)*sum(eps[a,b,g,f]*eta[g,d]*vu[f] for g in range(4) for f in range(4))
# operator equation coefficient on E_e: [E^a,[E_a,E_b]] + 1/2 eps_{bcdf} v^f [E^c,E^d]
# [E_a,E_b]=c_ab^d E_d ; [E^a,[E_a,E_b]] = eta^{aa'} c_{ab}^d c_{a'd}^e E_e
res=[]
for b in range(4):
  for e in range(4):
    t=sum(eta[a,a]*c(a,b,d)*c(a,d,e) for a in range(4) for d in range(4))
    # 1/2 eps_{bcdf} v^f [E^c,E^d] = 1/2 eps_bcdf v^f eta^cc eta^dd c_cd^e E_e
    t+=sp.Rational(1,2)*sum(eps[b,cc,d,f]*vu[f]*eta[cc,cc]*eta[d,d]*c(cc,d,e) for cc in range(4) for d in range(4) for f in range(4))
    res.append(sp.simplify(t))
print('background residual set', set(res))
# Jacobi
jac=set()
for a,b,cc,e in itertools.product(range(4),repeat=4):
    jac.add(sp.expand(sum(c(a,b,d)*c(d,cc,e)+c(b,cc,d)*c(d,a,e)+c(cc,a,d)*c(d,b,e) for d in range(4))))
print('Jacobi', jac)
# opposite sign test
# TT
TT=sp.simplify(sum(c(a,b,d)**2*eta[a,a]*eta[b,b]*eta[d,d] for a in range(4) for b in range(4) for d in range(4)))
vv=sum(eta[i,i]*vu[i]**2 for i in range(4))
print('TT/vv', sp.simplify(TT/vv))
# timelike v=(m,0,0,0): spatial structure constant
m=sp.symbols('m',positive=True)
print('c_12^3 for v=(m,0,0,0):', c(1,2,3).subs({v[0]:m,v[1]:0,v[2]:0,v[3]:0}))
# det identity
q=sp.symbols('q0:4'); ql=[sum(eta[i,j]*q[j] for j in range(4)) for i in range(4)]
q2=sum(q[i]*ql[i] for i in range(4)); qv=sum(ql[i]*vu[i] for i in range(4))
# M_b^d acting on A_d: -(q^2 A_b - q_b q.A) + i eps_{bcdf} v^f q^c A^d ; write as matrix on A_d (lower) : A^d = eta^{dd} A_d
M=sp.zeros(4,4)
for b in range(4):
  for d in range(4):
    M[b,d]=-(q2*(1 if b==d else 0)-ql[b]*q[d]) + sp.I*sum(eps[b,cc,d,f]*vu[f]*q[cc] for cc in range(4) for f in range(4))*eta[d,d]
# M q-gauge: A_d=q_d
print('M q_gauge', sp.simplify(M*sp.Matrix(ql)).T)
Mm=M-sp.Matrix(4,4,lambda b,d: ql[b]*q[d])
print('det identity residual', sp.expand(Mm.det()-q2**2*(q2**2-qv**2+q2*vv)))
