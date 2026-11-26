import sympy as sp
n,xi,A,Lam,s,Phi=sp.symbols('n xi A Lambda s Phi',positive=True)
def S_of(lnZ_n):
    W=lnZ_n-n*lnZ_n.subs(n,1)
    return sp.simplify(((1-n*sp.diff(W,n))).subs(n,1)) if False else sp.simplify((W-n*sp.diff(W,n)).subs(n,1))
# (1) cone delta in the operator, E = xi R, R = 4 pi (1-n) delta_Sigma.  Heat-trace gain (flat transverse kernel (4 pi s)^-1 at the tip and on Sigma):
gain=-s*xi*4*sp.pi*(1-n)*A/(4*sp.pi*s)**2
dlnZ=sp.Rational(1,2)*sp.integrate(gain/s,(s,Lam**-2,sp.oo))
S_contact=S_of(dlnZ)
phi2=Lam**2/(16*sp.pi**2)
print("contact entropy shift      :",S_contact," ; -2 pi xi <phi^2> A =",sp.simplify(-2*sp.pi*xi*phi2*A), " equal:",sp.simplify(S_contact+2*sp.pi*xi*phi2*A)==0)
# (2) Herzog-Nishioka counterterm dI_E = -2 pi (1-n) xi int phi^2  (their eq (2.19)), lnZ_n -> lnZ_n - dI_E
dlnZ_ct=2*sp.pi*(1-n)*xi*phi2*A
S_ct=S_of(dlnZ_ct)
print("H-N counterterm entropy    :",sp.simplify(S_ct)," ; sum with contact:",sp.simplify(S_contact+S_ct))
# (3) Wald identity: 1/(4 G_eff) = 1/(4G) - 2 pi xi phi^2  for L = R/(16 pi G) - xi R phi^2/2
G,ph=sp.symbols('G phi',positive=True)
Leff=1/(16*sp.pi*G)-xi*ph**2/2
print("A/(4 G_eff)  :",sp.expand(4*sp.pi*A*Leff)," (Wald contact -2 pi xi phi^2 A, cf. Donnelly-Wall eq (4))")
