"""
Proposal 062 C-R1 verification (r2, F1-corrected): q=0 non-derivative sector of
the trace channel in the 048/049 hypothesis class (conjugate-coordinate class
times a fuzzy factor, equal weights, V=T, frozen symbol, product background,
formal continuation).

r2 change (gatekeeper finding F1): the recorded convention has A=(V+2T)/24
(appH L2750) with V=F*Vhat*chi^2, T=F*That*chi^2 (appH L2779), so the recorded
L = 32 pi^2 m^6 / A (appH L2809) is L = 768 pi^2 m^6 / (F (Vhat+2That) chi^2).
With this L the recorded q_b^2 (appH L2811) and q_*^2 = 2 M L hold
simultaneously; r1's A=(Vhat+2That)/24 dropped the F chi^2 factor.

Algebra checks only (symbolic/numeric; not a proof of the manuscript claims):

 1. Determinant expansion.  With eps = g^{-1} hbar,
      sqrt|g+hbar| = sqrt|g| [ 1 + tr(eps)/2 + (tr eps)^2/8 - tr(eps^2)/4 + O(eps^3) ].
    For a pure-trace fluctuation hbar = (t/4) g (t = hbar^mu_mu) this gives
      sqrt|g+hbar| = sqrt|g| ( 1 + t/2 + t^2/16 + O(t^3) ).
    Verified two ways: exact pure-trace det, and a random symmetric 4x4 at eps=1e-3.
    Direction caveat: along a rank-one direction the second-order part is -lam^2/8.

 2. Recorded densities (appH L2776-2777; V=T form; L2779 "carry sqrt|g| alone"):
      U4 = -(F/32 pi^2) sqrt|g| Uhat chi^4
      U2 = -(F/32 pi^2) sqrt|g| [2(Vhat-That) - (3/4) vartheta (Vhat-2That)] chi^2
      U2(V=T) = -(3F/128 pi^2) sqrt|g| vartheta That chi^2
    The tree density rho_M V_t/g^2 carries no sqrt|g| (recorded form, appH L2775).
    Write the total sqrt|g|-coefficient of the density as W (density contains
    W sqrt|g|, plus a supplied sqrt|g| counterterm -Lambda_ct).

 3. Tadpole/mass relation (formal continuation S_E = -S_L, appH L2809 displays S_E):
    Expanding W sqrt|g+hbar| in the trace channel:
      tadpole (coefficient of t in S_E):  T_t = -sqrt|g| W / 2
      mass term (1/2) M t^2 in S_E:      M   = -sqrt|g| W / 8
    hence M = T_t/4 (ratio continuation-invariant) and, with the recorded
    convention that an added (1/2) M t^2 contributes q_*^2 = 2 M L (appH L2809),
      q_*^2 = L * T_t / 2 .
    Consequences:  T_t = 0  <=>  M = 0  <=>  q_*^2 = 0  for every density term
    whose hbar-dependence is exactly the sqrt|g| factor.

 4. Recorded scales (appH L2750, L2779, L2809, L2811):
      A = (V+2T)/24 with V = F Vhat chi^2, T = F That chi^2,
      L = 32 pi^2 m^6 / A = 768 pi^2 m^6 / (F (Vhat+2That) chi^2),
      q_b^2 = 12 Uhat chi^2 / ( m^2 (Vhat+2That) )   (division by m^2(Vhat+2That)),
    cross-derived from the vacuum chain q_b^2 = -16 pi^2 V0 / (A m^2) with
    V0 = -F Uhat chi^4 / 32 pi^2 (appH L2811), which equals the recorded q_b^2
    ONLY in this A-convention, and whose S^2_N large-N limit (Uhat/N^2->1,
    (Vhat+2That)/N^2->12) is chi^2/m^2 as recorded.
      M_E[U4]  = F sqrt|g| Uhat chi^4 / 256 pi^2   (positive for Uhat>0 in S_E),
      q_*^2[U4] = 2 M_E[U4] L = +6 sqrt|g| Uhat chi^2 m^6 / (Vhat+2That),
      q_*^2[U4] / q_b^2 = sqrt|g| m^8 / 2   (F, Uhat, chi cancel; comparison is
      convention-bound in m and sqrt|g|).

 5. Saddle completion: eliminating t from (q^2/4L + M/2) t^2 - J t gives
    -L J^2/(q^2 + 2ML); with the appH vacuum shift (q^2 -> q^2 - q_b^2 in
    the t kinetic coefficient) the first denominator of the appH display becomes
    q^2 - q_b^2 + q_*^2, so the pole sits at q^2 = q_b^2 - q_*^2:
    tachyonic-signed for Uhat>0 unless q_*^2 > q_b^2.

 6. Flatness vs Yukawa threshold: the tadpole-cancelling counterterm
    Lambda_ct* = (U4+U2)/sqrt|g| forces total M = 0, q_*^2 = 0; the Yukawa
    threshold q_*^2 = q_b^2 requires |T_t| = 2 q_b^2/L = F Uhat chi^4 / (32 pi^2 m^8);
    |T_need / T_t[U4]| = 2 / (sqrt|g| m^8).
"""
import sympy as sp

def main():
    out = []
    def P(*a):
        out.append(" ".join(str(x) for x in a))

    I4 = sp.eye(4)

    # ---------- 1. determinant expansion ----------
    import random
    random.seed(7)
    A = [[random.uniform(-1, 1) for _ in range(4)] for _ in range(4)]
    Hm = sp.Matrix(A)
    Hm = (Hm + Hm.T) / 2
    e = sp.Rational(1, 1000)
    ser = sp.expand(sp.sqrt((I4 + e * Hm).det()))
    trH = Hm.trace()
    trH2 = (Hm * Hm).trace()
    pred = 1 + trH * e / 2 + trH**2 * e**2 / 8 - trH2 * e**2 / 4
    err = ser - sp.expand(pred)
    P("1. sqrt(det(1+eH)) vs 1 + tr/2 + (tr)^2/8 - tr(H^2)/4, random symmetric 4x4, e=1/1000:")
    P("   exact expanded difference (O(e^3) remainder):", err, " ~ float:", float(err))
    t = sp.symbols('t', real=True)
    hs = (t / 4) * I4
    pure = sp.sqrt((I4 + hs).det())
    P("   pure trace h=(t/4)I: sqrt det =", sp.expand(pure))
    P("   check 1+t/2+t^2/16:", sp.simplify(sp.series(pure, t, 0, 4).removeO() - (1 + t/2 + t**2/16)))
    lam = sp.symbols('lambda', real=True)
    v = sp.Matrix([1, 0, 0, 0])
    rank1 = sp.expand(sp.sqrt((I4 + lam * v * v.T).det()).series(lam, 0, 3).removeO())
    P("   rank-one direction sqrt det(1+lam v v^T):", rank1,
      "  -> t^2-type coefficient is -lam^2/8 (negative): the sign of the quadratic determinant part is direction-dependent; the +1/16 sign claim is only for the pure-trace channel")

    # ---------- 2. recorded densities ----------
    F, sqg, Uhat, chi, th, Vh, Th, m, Lq, J, q = sp.symbols(
        'F sqrtg Uhat chi vartheta Vhat That m L J q', positive=True)
    U4 = -(F / (32 * sp.pi**2)) * sqg * Uhat * chi**4
    U2gen = -(F / (32 * sp.pi**2)) * sqg * (2*(Vh - Th) - sp.Rational(3,4)*th*(Vh - 2*Th)) * chi**2
    U2VT = sp.simplify(U2gen.subs(Vh, Th))
    P("")
    P("2. U2 at Vhat=That:", U2VT, " (manuscript V=T form) matches:",
      sp.simplify(U2VT + (3*F/(128*sp.pi**2))*sqg*th*Th*chi**2) == 0)

    # Euclidean (S_E = -S_L formal continuation) coefficients of the t channel:
    Lamct = sp.symbols('Lambda_ct', real=True)
    W = sp.simplify((U4 + U2VT)/sqg) - Lamct     # density coefficient of sqrt|g| (Lorentzian)
    Tt = sp.simplify(-sqg * W / 2)               # tadpole: coefficient of t in S_E
    M  = sp.simplify(-sqg * W / 8)               # coefficient in (1/2) M t^2 in S_E
    P("")
    P("3. (formal continuation S_E=-S_L) T_t = -sqrt|g| W/2,  M = -sqrt|g| W/8  =>  M = T_t/4, q_*^2 = 2 M L = L T_t/2:")
    qstar2 = sp.simplify(2*M*Lq)
    P("   q_*^2 =", qstar2)
    P("   q_*^2 - L*T_t/2 =", sp.simplify(qstar2 - Lq*Tt/2), "  (must be 0: exact relation)")

    # ---------- 4. recorded scales (r2: recorded A-convention, F1) ----------
    Arec = F*(Vh + 2*Th)*chi**2/24          # appH L2750 A=(V+2T)/24, L2779 V=F Vhat chi^2, T=F That chi^2
    Lrec = sp.simplify(32*sp.pi**2*m**6/Arec)
    qb2 = 12*Uhat*chi**2/(m**2*(Vh + 2*Th))  # appH L2811 (division reading)
    V0 = -(F*Uhat*chi**4)/(32*sp.pi**2)      # appH L2811
    qb2_chain = sp.simplify(-16*sp.pi**2*V0/(Arec*m**2))
    M_E_U4 = sp.simplify(-sqg*(-(F/(32*sp.pi**2))*Uhat*chi**4)/8)   # M_E[U4] = -sqrt|g| W_4/8
    qsU4 = sp.simplify(2*M_E_U4*Lrec)
    ratio = sp.simplify(qsU4/qb2)
    P("")
    P("4. A (recorded) =", Arec, ";  L =", Lrec)
    P("   q_b^2 (recorded L2811) =", qb2)
    P("   vacuum-chain cross-derivation q_b^2 = -16 pi^2 V0/(A m^2) =", qb2_chain,
      "   equals recorded:", sp.simplify(qb2_chain - qb2) == 0,
      "   (with r1's A=(Vhat+2That)/24 it would be", sp.simplify(-16*sp.pi**2*V0/(((Vh+2*Th)/24)*m**2)), "= wrong)")
    P("   M_E[U4] =", M_E_U4)
    P("   q_*^2[U4] = 2 M_E[U4] L =", qsU4, "  (positive for Uhat>0)")
    P("   ratio q_*^2[U4]/q_b^2 =", ratio, "  (F, Uhat, chi cancel; convention-bound in m, sqrt|g|)")
    P("   large-N S2_N: q_b^2 ->", sp.simplify(qb2.subs({Uhat: 1, Vh: 4, Th: 4})), " (Uhat/N^2=1, (Vhat+2That)/N^2=12: expect chi^2/m^2)")

    # ---------- 5. saddle completion ----------
    P("")
    P("5. saddle completion:")
    tsa = sp.symbols('t_sa', real=True)
    S = (q**2/(4*Lq) + M/2)*tsa**2 - J*tsa
    tsol = sp.solve(sp.diff(S, tsa), tsa)[0]
    Sval = sp.simplify(S.subs(tsa, tsol))
    P("   S(t*) + L J^2/(q^2+2ML) =", sp.simplify(Sval + Lq*J**2/(q**2 + 2*M*Lq)))
    S2 = ((q**2 - qb2)/(4*Lq) + M/2)*tsa**2 - J*tsa
    tsol2 = sp.solve(sp.diff(S2, tsa), tsa)[0]
    Sval2 = sp.simplify(S2.subs(tsa, tsol2))
    P("   shifted vacuum kinetic coefficient: S(t*) + L J^2/(q^2 - q_b^2 + q_*^2) =",
      sp.simplify(Sval2 + Lq*J**2/(q**2 - qb2 + 2*M*Lq)))

    # ---------- 6. flatness vs Yukawa threshold ----------
    P("")
    P("6. flatness vs Yukawa:")
    Lamct_star = sp.solve(sp.Eq(Tt, 0), Lamct)[0]
    M_flat = sp.simplify(M.subs(Lamct, Lamct_star))
    P("   tadpole-cancelling counterterm Lambda_ct* =", Lamct_star,
      "  (equals (U4+U2)/sqrt|g|:", sp.simplify(Lamct_star - (U4+U2VT)/sqg) == 0, ")")
    P("   total M at Lambda_ct* =", M_flat, "  =>  q_*^2 =", sp.simplify(2*M_flat*Lq))
    T_need = sp.simplify(2*qb2/Lrec)
    P("   Yukawa threshold q_*^2 = q_b^2 needs |T_t| = 2 q_b^2/L =", T_need)
    TtU4 = sp.simplify(-U4/2)  # T_t[U4] = -sqrt|g| (U4/sqrt|g|)/2 = -U4/2 in S_E
    P("   |T_need / T_t[U4]| =", sp.simplify(sp.Abs(T_need/TtU4)))

    print("\n".join(str(x) for x in out))

if __name__ == "__main__":
    main()
