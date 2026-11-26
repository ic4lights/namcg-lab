from sympy import *
Ns,a,nD=symbols('N_s alpha n_D')
cT=(Ns+a-1)/6+4*nD/3-Rational(11,3)
cA_anti=(Ns+a+1)/6+nD/3
cA_per=(Ns+a+1)/6-2*nD/3
print('gap antiperiodic',simplify(cA_anti-cT))
print('gap periodic',simplify(cA_per-cT))
s={Ns:6,a:1,nD:2}
print('D=10: cT',cT.subs(s),'cA anti',cA_anti.subs(s),'cA per',cA_per.subs(s))
print('rho^2 X coefficient 1-nD/2 at nD=2:',(1-nD/2).subs(nD,2))
