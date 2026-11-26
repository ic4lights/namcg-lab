import sympy as sp
# ---- (A) teleparallel decomposition from the manuscript identities (appendix H, torsion-invariant paragraph and replica paragraph)
R,T2,TT,V2,dV=sp.symbols('R T2 TT V2 dV')            # R_G, T_{lmn}T^{lmn}, T_{lmn}T^{mln}, V_mV^m, nabla_m V^m ;  V_m = d_m ln rho
Ttele=T2/4+TT/2-V2
Rid=-Ttele-2*dV                                      # R[G] = -(T2/4+TT/2-V2) - 2 nabla V   (Weitzenboeck identity, manuscript)
Es_torsion=R/4+T2/16+TT/8                            # E_s in (G,torsion) variables (manuscript)
Es_rho=-dV/2+V2/4                                    # E_s = -1/2 Box ln rho + 1/4 |d ln rho|^2
print("E_s(torsion) - E_s(rho) on the identity R=-T_tele-2 nabla V :",sp.simplify((Es_torsion-Es_rho).subs(R,Rid)))
Gam_s=R/6-Es_torsion
print("scalar density R/6-E_s  =  -R/12 - T_tele/4 - V^2/4 ?",sp.simplify(Gam_s-(-R/12-Ttele/4-V2/4)))
# Einstein-equivalent coefficient: replace T_tele by -R-2 nabla V (teleparallel equivalence), keep V^2 (zero on delta rho=0 modes at 2nd order)
Gam_eq=sp.expand((-R/12-Ttele/4-V2/4).subs(Ttele,-R-2*dV)) if False else sp.expand(-R/12-(-R-2*dV)/4-V2/4)
print("scalar density with T_tele = -R-2 nabla V : coefficient of R =",sp.Poly(Gam_eq,R).coeff_monomial(R),"  (= c_T per scalar component, 1/6)")
print("   boundary term B = R + T_tele = -2 nabla V ;  E_s = B/4 + V^2/4:",sp.simplify((R/4+Ttele/4+V2/4).subs(R,Rid)-Es_rho))
# ---- (B) contents table, alpha=1, Euclidean Poisson class (formulas of appendix H, Dirac/fermion paragraphs)
Ns,nD=sp.symbols('N_s n_D')
Ntot=Ns+2-4*nD
b=1-nD/2
cR =Ntot/6                      # coefficient of rho R[g_rho]  (G,rho,dTheta) variables
cT =cR-4*b                      # Einstein structure of the quadratic form on the two delta rho=0 modes
cAfx=(Ns+2)/6+nD/3              # fixed-state replica, antiperiodic Dirac gluing
cAsm=-Ntot/12                   # first-order smooth replica
cGtau=-Ntot/12                  # coefficient of sqrt(G) R_G in (G,torsion) variables (table in the replica paragraph)
print("c_A^sm - (-c_R/2)            =",sp.simplify(cAsm+cR/2))
print("c_A^sm - c_(G,torsion)       =",sp.simplify(cAsm-cGtau))
print("c_A^fx - c_T                 =",sp.simplify(cAfx-cT))
print("c_A^sm - c_T                 =",sp.factor(sp.simplify(cAsm-cT)))
print("c_A^fx - c_A^sm              =",sp.simplify(cAfx-cAsm)," = (N_s+2)/4 = bosonic contacts")
print("scalar-only (n_D=0 and no connection sector): c_A^fx = c_T = N/6; c_A^sm = -N/12")
for (ns,nd,lab) in [(6,2,'IKKT'),(10,1,'line'),(2,1,'D=6 SUSY'),(0,sp.Rational(1,2),'D=4 N=1 SYM')]:
    sub={Ns:ns,nD:nd}
    print("%-14s N_s=%s n_D=%s  c_R=%s c_T=%s c_A^fx=%s c_A^sm=%s ; fx-T=%s sm-T=%s"%(lab,ns,nd,cR.subs(sub),cT.subs(sub),cAfx.subs(sub),cAsm.subs(sub),(cAfx-cT).subs(sub),(cAsm-cT).subs(sub)))
# ---- (C) IKKT: the two independent vanishing conditions
print("c_A^sm=0 <=> N_tot=0 <=> N_s=4 n_D-2 ;  c_T=0 <=> N_tot=24 b : N_s =",sp.solve(sp.Eq(cT,0),Ns), " ; N_tot=0 :",sp.solve(sp.Eq(Ntot,0),Ns))
print("intersection:",sp.solve([sp.Eq(cT,0),sp.Eq(Ntot,0)],[Ns,nD]))
# ---- (D) flux-affine law under superposition of the two first-order contributions
f=sp.symbols('f')
cA_f=cAfx+f*(cAsm-cAfx)
print("c_A(f) at IKKT:",sp.simplify(cA_f.subs({Ns:6,nD:2})),"; slope = -(N_s+2)/4 =",sp.simplify((cAsm-cAfx)))
