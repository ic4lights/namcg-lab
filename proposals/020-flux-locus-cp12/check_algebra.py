import sympy as sp
f1,f2,sx,f3,z=sp.symbols('f1 f2 s f3 z',positive=True)
# V4 = -4 tr F^4 + (tr F^2)^2 for a 4D 2-form with plane strengths f1,f2
F=sp.Matrix([[0,f1,0,0],[-f1,0,0,0],[0,0,0,f2],[0,0,-f2,0]])
V4=sp.expand(-4*(F**4).trace()+((F**2).trace())**2)
print("V4 =",sp.factor(V4))
# self-dual Landau supertrace, N=1-type content: vector 4cosh2sf, ghosts -2, Majorana -(1/2)*4cosh^2(sf)
f=sp.symbols('f',positive=True)
tot=4*sp.cosh(2*sx*f)-2-sp.Rational(1,2)*4*sp.cosh(sx*f)**2
print("SD bracket - 6 sinh^2(sf) =",sp.simplify((tot-6*sp.sinh(sx*f)**2).rewrite(sp.exp)))
# large-f vector density at f1=f2: (f/(4 pi sinh sf))^2 * 4cosh(2sf) -> f^2/(2 pi^2)
d=(f/(4*sp.pi*sp.sinh(sx*f)))**2*4*sp.cosh(2*sx*f)
print("limit sf->inf of vector density / (f^2/(2pi^2)) =",sp.limit(d/(f**2/(2*sp.pi**2)),f,sp.oo))
# Troost lowest vector level with planes f1>=f2,f3: sum f - 2 f1 ; stable iff f1<=f2+f3
print("lowest level:",sp.simplify(f1+f2+f3-2*f1))
# closed forms: ratios
l,y4=sp.symbols('l y4',positive=True); a,b,m=sp.symbols('a b m',positive=True)
print("detQ check:", sp.simplify(sp.Matrix.diag(-1,1,1,1).det()*y4**8*(1+(-l**2-y4**2)/y4**2)))
