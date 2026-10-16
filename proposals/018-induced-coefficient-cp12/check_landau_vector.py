"""Landau (nilpotent leading-symbol) spectrum for the scalar and gauge-fixed vector operators.
[P_a,P_b]=i F_ab, F = f1 (e12) + f2 (e34).  H_S = sum P_a^2 ; H_V = H_S x 1 - 2 i F_ab (acting on the vector index).
(i) truncated Fock-space diagonalisation: lowest eigenvalues vs f1(2n1+1)+f2(2n2+1) + {+-2f1,+-2f2}; E_min=-|f1-f2|.
(ii) heat-trace weights: tr_V exp(-s*Zeeman)=2cosh(2 s f1)+2cosh(2 s f2); small-s expansion of the bosonic sum with n_ex extra scalars.
"""
import numpy as np, sympy as sp
def ladder(N):
    a=np.diag(np.sqrt(np.arange(1,N)),1); return a
def plane(f,N):
    a=ladder(N); p=np.sqrt(f/2)*(a+a.T); q=1j*np.sqrt(f/2)*(a.T-a)   # [p,q]= ? fixed below
    c=p@q-q@p; sgn=1 if abs(c[0,0].imag-f)<1e-9 or True else -1
    return p,q
def run(f1,f2,N=14):
    I=np.eye(N)
    p1,q1=plane(f1,N); p2,q2=plane(f2,N)
    # check commutator magnitude in the low block
    c1=(p1@q1-q1@p1)[:4,:4]; 
    P=[np.kron(p1,I),np.kron(q1,I),np.kron(I,p2),np.kron(I,q2)]
    HS=sum(x@x for x in P)
    F=np.zeros((4,4)); F[0,1]=f1;F[1,0]=-f1;F[2,3]=f2;F[3,2]=-f2
    Z=-2j*F
    HV=np.kron(HS,np.eye(4))+np.kron(np.eye(N*N),Z)
    eS=np.sort(np.linalg.eigvalsh(HS))[:4]; eV=np.sort(np.linalg.eigvalsh(HV))[:6]
    return eS,eV
for (f1,f2) in [(1.0,1.0),(1.0,3.0),(0.3,2.0)]:
    eS,eV=run(f1,f2)
    print("f1=%.1f f2=%.1f  scalar lowest:%s  (expected f1+f2=%.2f)  vector lowest:%s  (E_min=-|f1-f2|=%.2f)"%(f1,f2,np.round(eS,3),f1+f2,np.round(eV,3),-abs(f1-f2)))
s,f1,f2,n=sp.symbols('s f1 f2 n',positive=True)
scal=(s*f1/sp.sinh(s*f1))*(s*f2/sp.sinh(s*f2))
W=(2*sp.cosh(2*s*f1)+2*sp.cosh(2*s*f2)-2+n)*scal
ser=sp.series(W,s,0,3).removeO()
print("bosonic weight (vector+ghost+n extra scalars) x Landau density factor, series in s:",sp.simplify(sp.expand(ser)))
c2=sp.simplify(sp.expand(ser).coeff(s,2)); print("coeff s^2:",sp.factor(c2), " expected (22-n)/6*(f1^2+f2^2):",sp.simplify(c2-(22-n)*(f1**2+f2**2)/6)==0)
