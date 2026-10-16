"""Gap table with the fermion gluing fixed (Tr rho^n, Dirac domain): c_A(Dirac) = +1/3; vector branches reported by integer-n test."""
from sympy import *
Ns,a,nD=symbols('N_s alpha n_D')
cT=(Ns+a-1)/6+4*nD/3-Rational(11,3)
cA_vec_unrot=(Ns+a+1)/6          # integer-n replica of Tr rho^n (rotation by 2 pi n is trivial on the vector index)
cA_vec_rotA=cA_vec_unrot-1       # rotated, analytic n<1 branch: gap 3 at nD=0 (017)
cA_vec_rotB=cA_vec_unrot+1       # rotated, n>1 branch: gap 5
cD=Rational(1,3)
for nm,cv in (('unrotated (integer-n data)',cA_vec_unrot),('rotated n<1 (does not match n=2)',cA_vec_rotA),('rotated n>1 (does not match n=2)',cA_vec_rotB)):
    gap=simplify(cv+nD*cD-cT)
    print('%-36s gap = %s ; at (nD,Ns,alpha)=(2,6,1): cT=%s cA=%s gap=%s' % (nm,gap,cT.subs({Ns:6,a:1,nD:2}),simplify((cv+nD*cD).subs({Ns:6,a:1,nD:2})),gap.subs({Ns:6,a:1,nD:2})))
print('gap = 0 requires n_D =', solve(simplify(cA_vec_unrot+nD*cD-cT),nD), '(unrotated); weight of rho^2 X there: ', (1-nD/2).subs(nD,4))
print('periodic Cartesian, scalar-like domain (017): cA(Dirac)=-2/3 -> gap 4-2 n_D: not Tr rho^n at even n, not a Dirac-operator trace; withdrawn as a gluing')
