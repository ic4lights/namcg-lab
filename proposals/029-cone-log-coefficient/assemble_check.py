import sympy as sp
n=sp.symbols('n',positive=True)
cB=sp.pi/3*(1-n**2)/n; dB=-sp.pi/180*(1-n**2)*(1+n**2)/n**3
# scalar density per component: S=-d_n[(4pi)^-2 (cB(R/6-E)+dB Q)]
dc=sp.diff(cB,n).subs(n,1); dd=sp.diff(dB,n).subs(n,1)
print('cB\'=',dc,' dB\'=',dd,'  -> S_B = (1/24pi)(R/6-E) - Q/(720pi):',sp.simplify(-dc/(16*sp.pi**2)*24*sp.pi),sp.simplify(-dd/(16*sp.pi**2)*720*sp.pi))
# sphere S^4, Sigma great S^2: R=12,Rii=6,Rijij=2, conformal scalar E=R/6 -> area 4pi
R,Rii,Rj=12,6,2
print('scalar sphere lnLambda coeff =',sp.simplify(4*sp.pi*(-dd/(16*sp.pi**2))*(Rii-2*Rj)),' (expect -1/90)')
# Dirac: a=11/360 input => -11/90; Z_n twist sums
print('Dirac sphere (input a=11/360): ',-4*sp.Rational(11,360))
# assembly symbolic: 24pi*S = 8R/6-(8e-Xp)+R-(4e-Xp/2)-T-Rijij-Rsig+2W
R,Rii,Rj,e,Xp,T,W=sp.symbols('R Rii Rj e Xp T W')
Rsig=R-2*Rii+Rj
S=8*R/6-(8*e-Xp)+R-(4*e-Xp/2)-T-Rj-Rsig+2*W
print('24pi S =',sp.expand(S))
conf=S.subs({e:R/6,W:0,Rj:Rii-R/3})
print('conformally flat, e=R/6:',sp.simplify(conf),'  (=3/2 Xp - T)')
