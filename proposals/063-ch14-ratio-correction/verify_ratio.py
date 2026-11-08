"""Check P_ent/P_GW scaling in ch14 (eq:Pent, eq:Peters) for circular Newtonian orbits.
Units as in eq:Peters (c=1). Inclination factor of the angle-integrated power = 1."""
import sympy as sp
G, M, mu, d, eta, n, f = sp.symbols('G M mu d eta n f', positive=True)
v2 = G*M/d
Om2 = G*M/d**3
P_GW = sp.Rational(32, 5)*G*mu**2*d**4*Om2**3
P_ent = eta*mu*v2/d**4                      # eq:Pent with eq:Fdiss (n=4)
print("P_GW      =", sp.simplify(P_GW))
print("P_ent     =", sp.simplify(P_ent))
R = sp.simplify(P_ent/P_GW)
print("ratio     =", R, "; d/dd ratio =", sp.simplify(sp.diff(R, d)))
# general drag exponent F = -eta mu v / d^n
P_ent_n = eta*mu*v2/d**n
Rn = sp.simplify(P_ent_n/P_GW)
print("ratio(n)  =", Rn, "; exponent of d =", sp.simplify(d*sp.diff(Rn, d)/Rn))
# dimensional check: [eta] from F = eta mu v / d^4 with c=1 => eta ~ L^4/T = L^3 ; G M ~ L
L = sp.symbols('L', positive=True)
dimR = (L**3)/(L**2*L)  # eta / (GM)^2 (G mu)
print("dim of ratio (c=1, GM~L, G mu~L, eta~L^3):", sp.simplify(dimR))
# Exercise 3: dU_N/dt along a Peters inspiral
E = -G*M*mu/(2*d)
ddot_peters = -P_GW/sp.diff(E, d)
dUN_dt = sp.diff(-G*M*mu/d, d)*ddot_peters
print("ddot_Peters =", sp.simplify(ddot_peters))
print("dU_N/dt     =", sp.simplify(dUN_dt), "; / P_GW =", sp.simplify(dUN_dt/P_GW))
print("P_ent/|dU_N/dt| =", sp.simplify(P_ent/(-dUN_dt)))
print("eta at P_ent=|dU_N/dt| :", sp.solve(sp.Eq(P_ent, -dUN_dt), eta))
print("eta at P_ent=P_GW      :", sp.solve(sp.Eq(P_ent, P_GW), eta))
# Entropic-only decay rate
ddot_ent = -P_ent/sp.diff(E, d)
print("ddot_ent    =", sp.simplify(ddot_ent))
# Chirp: GW frequency f = Omega/pi, with total loss (1+R) P_GW
Rc = sp.symbols('R', positive=True)
Om = sp.sqrt(Om2)
ddot_tot = -(1+Rc)*P_GW/sp.diff(E, d)
fdot = sp.diff(Om/sp.pi, d)*ddot_tot
dsol = (G*M/(sp.pi*f)**2)**sp.Rational(1, 3)
fdot_f = sp.simplify(fdot.subs(d, dsol))
Mc = mu**sp.Rational(3, 5)*M**sp.Rational(2, 5)
target = sp.Rational(96, 5)*sp.pi**sp.Rational(8, 3)*(G*Mc)**sp.Rational(5, 3)*f**sp.Rational(11, 3)
print("fdot / [(96/5) pi^(8/3) (G Mc)^(5/3) f^(11/3)] =", sp.simplify(fdot_f/target))
print("=> (1+R) Mc^(5/3) = Mc_eff^(5/3): Mc_eff = (1+R)^(3/5) Mc")
