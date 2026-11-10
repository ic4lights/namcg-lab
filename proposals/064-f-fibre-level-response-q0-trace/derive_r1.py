import sympy as sp

sp.init_printing(use_unicode=False)
t = sp.symbols('t', real=True)

print("== A1: determinant profile: sqrt|g+h| for h = (t/4) g, to t^2 ==")
prof = sp.expand((1 + sp.Rational(1, 4)*t)**2)
print("profile (1+t/4)^2 =", prof, " == 1 + t/2 + t^2/16:", sp.simplify(prof - (1 + t/2 + t**2/16)) == 0)

print("== A2: the fibre datum theta = -y.y/m^2 under the pure-trace wave ==")
# y fixed, gamma -> (1+t/4) gamma:  y.y -> (1+t/4) y.y, m fixed  =>  theta -> (1+t/4) theta exactly.
th0 = sp.symbols('theta_0', positive=True)
th_t = sp.simplify(th0*(1 + t/4))
print("theta(t)/theta_0 =", sp.simplify(th_t/th0), "; d theta/dt at t=0 =", sp.diff(th_t, t).subs(t, 0))
bgv = sp.Rational(15, 16)*th0**2  # background value 15/4 theta^2 F sqrt|g| / 16 pi^2, common factors suppressed
ratio_bg = sp.simplify(bgv.subs(th0, th0*(1 + t/4))*(1 + t/4)**2/bgv)
print("sqrt|g|*15/4*theta^2 response ratio =", sp.expand(ratio_bg), " (fourth power, not the determinant profile)")

print("== A3: level form of the first-term flux density: small-s integral and positivity ==")
s, muJ, mA2 = sp.symbols('s mu_J M_A2', positive=True)
th, cJ = sp.symbols('vartheta c_J', positive=True)
integrand = s**2*(sp.Rational(15, 4)*th**2 - s*th*cJ + s**2*cJ**2)*sp.exp(-s*(mA2 + muJ))
S = sp.integrate(integrand/s, (s, 0, sp.oo))
S = sp.simplify(S)
D = mA2 + muJ
print("S = int ds s^-1 e^{-sD} s^2(15/4 vth^2 - s vth cJ + s^2 cJ^2) =", S)
print("equals 15 vth^2/(4 D^2) - 2 vth cJ/D^3 + 6 cJ^2/D^4:",
      sp.simplify(S - (sp.Rational(15, 4)*th**2/D**2 - 2*th*cJ/D**3 + 6*cJ**2/D**4)) == 0)
X, Y = sp.symbols('X Y', positive=True)  # X = vartheta*D, Y = c_J
qY = sp.Rational(15, 4)*X**2 - X*Y + 2*Y**2
print("manuscript Y-bracket D^3*[15 vth^2/(4D) - vth cJ/D^2 + 2 cJ^2/D^3] = 15/4 X^2 - X Y + 2 Y^2:")
print("  match:", sp.simplify(sp.together((sp.Rational(15, 4)*th**2/D - th*cJ/D**2 + 2*cJ**2/D**3)*D**3)
                              - (qY.subs(X, th*D).subs(Y, cJ))) == 0,
      "; discriminant wrt X:", sp.discriminant(qY, X), "< 0 => positive definite (as recorded)")
qS = sp.Rational(15, 4)*X**2 - 2*X*Y + 6*Y**2
print("D^4*S =", sp.simplify(sp.together(S*D**4)), " = 15/4 X^2 - 2 X Y + 6 Y^2:",
      sp.simplify(sp.together(S*D**4) - qS.subs({X: th*D, Y: cJ})) == 0,
      "; discriminant:", sp.discriminant(qS, X), "< 0 => S > 0 levelwise")

print("== A4: first term F1(t) = sqrt|g|(1+t/4)^2 S((1+t/4)vth): coefficients and split ==")
S_of_t = sp.simplify((1 + t/4)**2 * S.subs(th, th*(1 + t/4)))
Sser = sp.expand(sp.series(S_of_t, t, 0, 3).removeO())
c1 = sp.simplify(Sser.coeff(t, 1)); c2 = sp.simplify(Sser.coeff(t, 2))
S0 = S; Sp = sp.diff(S, th)*th; Spp = sp.diff(S, th, 2)*th**2
print("t-coeff:", sp.simplify(c1 - (2*S0 + Sp)/4) == 0, "( = (2 S0 + vth S'_vth)/4 ); profile part = S0/2")
print("t^2-coeff:", sp.simplify(c2 - (2*S0 + 4*Sp + Spp)/32) == 0, "( = (2 S0 + 4 vth S' + vth^2 S'')/32 ); profile part = S0/16")
T_extra = sp.simplify(Sp/4)
M_extra = sp.simplify((4*Sp + Spp)/32)
print("extra tadpole summand vth S'/4 =", T_extra)
print("extra M summand (4 vth S' + vth^2 S'')/32 =", M_extra)
rT = sp.simplify(sp.together(T_extra*8*D**3/th))
print("  8 D^3 (extra tadpole)/vth =", rT, " = 15 X - 4 Y:", sp.simplify(rT - (15*X - 4*Y).subs({X: th*D, Y: cJ})) == 0)
rM = sp.simplify(sp.together(M_extra*64*D**3/th))
print("  64 D^3 (extra M)/vth =", rM, " = 75 X - 16 Y:", sp.simplify(rM - (75*X - 16*Y).subs({X: th*D, Y: cJ})) == 0)
print("  => per level: extra tadpole > 0 iff 15 vth D > 4 c_J; extra M > 0 iff 75 vth D > 16 c_J")
print("  => both extra parts are positive simultaneously when 15 vth D > 4 c_J (implies 75 vth D > 20 c_J > 16 c_J)")
rho_ = sp.symbols('rho_M', positive=True)
print("ratio extraM/extraT =", sp.simplify(M_extra/T_extra))

print("== A5: robustness of the sign for the Y-derived homogeneous form ==")
Sb = sp.Rational(15, 4)*th**2/D - th*cJ/D**2 + 2*cJ**2/D**3
extraTb = sp.simplify(th*sp.diff(Sb, th)/4)
extraMb = sp.simplify((4*th*sp.diff(Sb, th) + th**2*sp.diff(Sb, th, 2))/32)
print("bracket extra tadpole =", sp.together(extraTb), "; bracket extra M =", sp.together(extraMb))
rTb = sp.simplify(sp.together(extraTb*8*D**2/th))
print("8 D^2 (extra tadpole)/vth, bracket form =", rTb, " = 15 X - 2 Y:", sp.simplify(rTb - (15*X - 2*Y).subs({X: th*D, Y: cJ})) == 0)
rMb = sp.simplify(sp.together(extraMb*64*D**2/th))
print("64 D^2 (extra M)/vth, bracket form =", rMb, " = 75 X - 8 Y:",
      sp.simplify(rMb - (75*X - 8*Y).subs({X: th*D, Y: cJ})) == 0)
print("=> same structure: extra M > 0 iff 75 vth D > 8 c_J; extra tadpole > 0 iff 15 vth D > 2 c_J")

print("== A6: 062 link identities (continuation, ratio, threshold bookkeeping) ==")
W, gabs, L = sp.symbols('W sqrtg L', positive=True)
Ti = -gabs*W/2
Mi = -gabs*W/8
print("T_i = -sqrt|g| W/2, M_i = -sqrt|g| W/8: ratio T/M =", sp.simplify(Ti/Mi))
print("q*^2 = 2 M L with M_i above equals (1/2) L T_i:", sp.simplify(2*Mi*L - L*Ti/2) == 0)
print("cancellation sum W_i = 0 gives sum T_i = 0 and sum M_i = 0 (same W_i): q*^2 = 0 on flat backgrounds")
Ub, Vh, Th2, chi2, m2 = sp.symbols('Uhat Vhat That chi^2 m^2', positive=True)
qb2 = 12*Ub*chi2/(m2*(Vh + 2*Th2))
m6 = m2**3
qstar2_U4 = 6*gabs*Ub*chi2*m6/(Vh + 2*Th2)
print("q_b^2 = 12 Uhat chi^2/(m^2 (Vhat+2That)) ; U4-only q*^2 = 6 sqrt|g| Uhat chi^2 m^6/(Vhat+2That)")
print("recorded ratio q*^2/q_b^2 = sqrt|g| m^8/2:", sp.simplify(qstar2_U4/qb2 - gabs*m2**4/2) == 0)
print("=> q*^2 - q_b^2 = (sqrt|g| m^8/2 - 1) q_b^2:",
      sp.simplify((qstar2_U4 - qb2) - (gabs*m2**4/2 - 1)*qb2) == 0,
      "; sign is fixed only if sqrt|g| m^8 > 2: convention-bound (as recorded)")
print("T/M ratio for any profile term is 4 (4*1/256 = 1/64):", sp.simplify(4*sp.Rational(1, 256) - sp.Rational(1, 64)) == 0)

print("== A7: exact P(Xi) flux-trace identities (re-check of the recorded non-negativity) ==")
ss, Xi1, Xi2 = sp.symbols('s Xi1 Xi2', positive=True)
P = lambda Xi: sp.exp(-ss)*(2*sp.cosh(ss*Xi) + 2/Xi*sp.sinh(ss*Xi))
e1 = sp.simplify(P(Xi1)*P(Xi2) - 2*(P(Xi1) + P(Xi2)) + 4 - (P(Xi1) - 2)*(P(Xi2) - 2))
print("tr_V e^{-sZ} - 2 tr_D e^{-sZ} + 4 = (P(Xi+)-2)(P(Xi-)-2): residual", e1, " == 0:", e1 == 0)
ml, sig = sp.symbols('m_L sigma', positive=True)
Xip = -ml + sp.I*sig
Xim = ml + sp.I*sig
dif = (P(Xim) - sp.conjugate(P(Xip))).rewrite(sp.exp)
difc = sp.simplify(sp.expand_complex(dif))
print("on the principal series Xi_+ = -m_L + i sigma, Xi_- = m_L + i sigma: P(Xi_-) - conj(P(Xi_+)) =",
      difc, " == 0:", difc == 0, " => first-term integrand |P(Xi_+)-2|^2 >= 0 as recorded")

print("== A8: level check of S((1+t/4)vth) against a brute-force proper-time expansion ==")
F1 = sp.integrate((1 + t/4)**2*sp.exp(-s*(mA2 + muJ))*s**2*(
        sp.Rational(15, 4)*(th*(1 + t/4))**2 - s*th*(1 + t/4)*cJ + s**2*cJ**2)/s, (s, 0, sp.oo))
F1s = sp.expand(sp.series(F1, t, 0, 3).removeO())
print("brute force t-coeff match:", sp.simplify(F1s.coeff(t, 1) - Sser.coeff(t, 1)) == 0,
      "; t^2-coeff match:", sp.simplify(F1s.coeff(t, 2) - Sser.coeff(t, 2)) == 0)
print("ALL CHECKS ABOVE ARE SYMBOLIC IDENTITIES OF THE STATED LEVEL FORM")
