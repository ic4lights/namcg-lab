import sympy as sp
x,n=sp.symbols('x n',positive=True)   # x = s f, n = n_ex
W=4*sp.cosh(2*x)+1-2+n               # 4 horizontal vector comps (Zeeman +-2f twice each), 1 normal comp, 2 ghosts, n extra scalars
dens=W/(16*sp.pi**2*sp.sinh(x)**2)    # times f^2
print("W - (8 sinh^2 x + 3 + n) =",sp.simplify(sp.expand(sp.expand_trig(W)-(8*sp.sinh(x)**2+3+n))).rewrite(sp.exp).simplify())
print("large-x limit of f^2-density coefficient:",sp.limit(dens.subs(n,0),x,sp.oo),"= 1/(2 pi^2) ->",sp.simplify(sp.limit(dens.subs(n,0),x,sp.oo)-1/(2*sp.pi**2)))
print("int_0^oo u^3/sinh^2(u) du =",sp.integrate(x**3/sp.sinh(x)**2,(x,0,sp.oo)),"= 3 zeta(3)/2:",sp.simplify(sp.integrate(x**3/sp.sinh(x)**2,(x,0,sp.oo))-3*sp.zeta(3)/2))
