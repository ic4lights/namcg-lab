"""Fibre-constant (l=0) sector: Box g = m d^a(m d_a g) on functions of y^mu, m=y^4=sqrt((y^0)^2-ell^2-|y|^2) (sheet y^4>0).
Check Box = rho^{-1} d_mu(rho m^2 eta^{mu nu} d_nu .) with rho=1/m (Liouville density pushed to the base), and compute the
Seeley-DeWitt a_1 density sqrt|G|(R_G/6 - E) for G^{mu nu}=m^2 eta^{mu nu} (Euclidean eta->delta as well), psi=rho/sqrt|G|=m^3,
E = (1/2) Box_G ln psi + (1/4)|d ln psi|^2_G   (O = -(D^2) + E-type, see text).
"""
import sympy as sp
y=sp.symbols('y0:4',real=True); l2=sp.Symbol('l2',positive=True)
for sig in ('lorentz','euclid'):
    eta=sp.diag(-1,1,1,1) if sig=='lorentz' else sp.eye(4)
    m=sp.sqrt(y[0]**2-l2-y[1]**2-y[2]**2-y[3]**2) if sig=='lorentz' else sp.sqrt(y[0]**2+y[1]**2+y[2]**2+y[3]**2-l2) 
    g=sp.Function('g')(*y)
    # on functions: D^a g = s m eta^{aa} d_a g  (index up), a-sum with eta_{aa}
    Dg=[m*eta[a,a]*sp.diff(g,y[a]) for a in range(4)]
    box=sum(eta[a,a]*m*eta[a,a]*sp.diff(Dg[a],y[a]) for a in range(4))      # eta_aa D^a D^a g, D^a=m eta^{aa} d_a
    rho=1/m
    O=sum(sp.diff(rho*m**2*eta[a,a]*sp.diff(g,y[a]),y[a]) for a in range(4))/rho
    print(sig,"Box g - rho^-1 d(rho K d g) =",sp.simplify(box-O))
    G=eta/m**2; Gi=G.inv(); sqG=m**-4
    ln=lambda f: sp.log(f)
    dlnm=[sp.diff(ln(m),y[i]) for i in range(4)]
    # R for G=e^{2phi} eta, phi=-ln m
    phi=-ln(m)
    d1=[sp.diff(phi,y[i]) for i in range(4)]
    boxeta=sum(eta[i,i]*sp.diff(phi,y[i],2) for i in range(4))
    gradsq=sum(eta[i,i]*d1[i]**2 for i in range(4))
    R=-6*sp.exp(-2*phi)*(boxeta+gradsq)
    psi3=3*ln(m)  # ln psi
    # Box_G f = sqG^-1 d(sqG G^{mu nu} d f)
    f=psi3
    boxG=sum(sp.diff(sqG*Gi[i,i]*sp.diff(f,y[i]),y[i]) for i in range(4))/sqG
    gsq=sum(Gi[i,i]*sp.diff(f,y[i])**2 for i in range(4))
    a1=sqG*(R/6-sp.Rational(1,2)*boxG-sp.Rational(1,4)*gsq)
    a1=sp.simplify(a1.subs(l2,-sp.Symbol('Y')**2+0) ) if False else sp.simplify(a1)
    print(sig,"sqrt|G| a_1 =",a1)
    # express with m: substitute y0^2 -> m^2 + l2 + |y|^2 (lorentz)
    mm=sp.Symbol('mm',positive=True)
    if sig=='lorentz':
        a1m=sp.simplify(a1.subs(y[0],sp.sqrt(mm**2+l2+y[1]**2+y[2]**2+y[3]**2)))
    else:
        a1m=sp.simplify(a1.subs(y[0],sp.sqrt(-mm**2+l2-y[1]**2-y[2]**2-y[3]**2)+0)) 
    print(sig,"in terms of m:",a1m)
