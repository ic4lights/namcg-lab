"""s2b: closed form of the fermion zero-mode count of the compact member and its uniqueness.
Claim: on End(V_n) = sum_{0<=m2<=m1<=n} (m1,m2), K_psi = C5 - C4tot + 3/2 vanishes exactly on
the so(4) component (k1,k2)=(m1,m2) coupled to j_L+1/2 (left) and (m1,-m2) coupled to j_R+1/2
(right), and nowhere else; per chirality the count is
   z(n) = sum_{(m1,m2) != (0,0)} (m1+m2+2)(m1-m2+1).
The 16-component count is z16 = 4*(zL+zR) = 8 z(n).
Also: the identity C5(m1,m2) + 3/2 = C4(j_L+1/2, j_R) for j_L=(m1+m2)/2, j_R=(m1-m2)/2 (symbolic),
and the general statement for an arbitrary so(5) irrep Lambda (not only those in End(V_n)).
"""
import sympy as sp
from s2_casimir_spectra import *
m1,m2,n=sp.symbols('m1 m2 n',integer=True,nonnegative=True)
jL=(m1+m2)/sp.Integer(2); jR=(m1-m2)/sp.Integer(2)
C5=m1*(m1+3)+m2*(m2+1)
c4s=lambda a,b: 2*a*(a+1)+2*b*(b+1)
print("identity C5+3/2-C4(jL+1/2,jR) =",sp.simplify(C5+sp.Rational(3,2)-c4s(jL+sp.Rational(1,2),jR)))
print("identity C5+3/2-C4(jR',jL'+1/2), (k1,k2)=(m1,-m2) =",sp.simplify(C5+sp.Rational(3,2)-c4s(jR,jL+sp.Rational(1,2))))
z=sp.summation(sp.summation((m1+m2+2)*(m1-m2+1),(m2,0,m1)),(m1,0,n))-2
z=sp.factor(sp.expand(z)); print("z(n) closed form:",z, "  leading:",sp.limit(z/n**4,n,sp.oo),"n^4")
Nn=(n+1)*(n+2)*(n+3)/6
print("z16/(16(N^2-1)) ~", sp.limit(8*z/(16*(Nn**2-1))*n**2,n,sp.oo),"/ n^2 ;  z16/N ~",sp.limit(8*z/Nn/n,n,sp.oo),"* n")
# uniqueness and counts against the full spectrum
ok=True
for nn in range(1,21):
    N,dec,A,P,G,FL,FR=spectra(nn)
    zz=int(z.subs(n,nn))
    if FL.get(0,0)!=zz or FR.get(0,0)!=zz: ok=False
    print(f"n={nn:2d} N={N:5d} zL={FL.get(0,0)} zR={FR.get(0,0)} formula={zz} z16={8*zz} 16(N^2-1)={16*(N*N-1)}")
print("counts match formula for n=1..20:",ok)
# every so(5) irrep Lambda != 0 (also half-integral, as in End of a reducible V) has the top zero mode
bad=[]
for a2 in range(0,25):
    for a1 in range(a2,25):
        M1=Fr(a1,2); M2=Fr(a2,2)
        if (M1-M2).denominator!=1 or (a1==0): continue
        cnt=0
        for (k1,k2) in branch(M1,M2):
            JL,JR=jlr(k1,k2)
            for tL in tens(JL,Fr(1,2)):
                if so5_C(M1,M2)-c4(tL,JR)+Fr(3,2)==0: cnt+=1
        if cnt!=1: bad.append((M1,M2,cnt))
print("so(5) irreps (m1,m2)!=0 with m1<=12 lacking exactly one left zero multiplet:",bad)
