"""070 s3: the order-Lambda^2 ledger of sec:status-B as a function of (N_s, n_D), alpha = 1, and its values at
(6,0) and (6,2); cone constants; the r-family; the mass-weighted extension.
Per-sector data (units c: S = (Lambda^2 A_G / 8 pi) c ; density sqrt(G) a_1 = n/6 rho R[g_rho] + kappa rho^2 X):
  sector            weight  n  kappa   cone constant per unit weight (c_A units)
  scalar component    +1    1    0     1/6
  connection          +1    4    1     4/6      (unrotated internal index)
  ghosts              -2    1    0     1/6
  Dirac field         -1    4   1/2    antiperiodic: -1/3 (so weight*value = +1/3) ; periodic: 4/6
s1 gives (n, kappa); s2 gives the on-mode rule c_T = c_R - 4 kappa_X.
Re-run: python proposals/070-b-content-class/s3_content_ledger.py
"""
import sympy as sp
Ns, nD, r, n, a = sp.symbols('N_s n_D r n a')
R = sp.Rational
# --- cone constants -------------------------------------------------------------------------------------
ent = lambda f: sp.simplify((f - n*sp.diff(f, n)).subs(n, 1))          # (1 - n d_n) at n = 1
C = lambda aa: (aa**2 - aa + R(1, 6))/(2*n) - n/12                      # C(n,a) = B_2(a)/(2n) - n/12
scal = ent(C(0))
print("scalar component: (1-n d_n) C(n,0) =", scal)
k = sp.symbols('k')
for nn in (3, 5, 7):
    ks = [R(2*j - (nn - 1), 2) for j in range(nn)]
    assert sum((kk/nn)**2 for kk in ks) == R(nn**2 - 1, 12*nn)
dirac_block = ent((n**2 - 1)/(12*n))
print("Dirac two-component block, sum_k a_k^2 = (n^2-1)/(12 n) checked at n = 3,5,7; (1-n d_n) =", dirac_block)
dirac_ap = -1*2*dirac_block           # weight -1, two blocks
print("Dirac field, antiperiodic, weight included:", dirac_ap, "; periodic, weight included:", -R(4, 6))
print("vector holonomy alpha_v = 1, n<1, two components with a = 1-n: shift of c =", sp.simplify(2*(ent(C(1 - n)) - ent(C(0)))))
# --- ledger ---------------------------------------------------------------------------------------------
Ntot = Ns + 2 - 4*nD
kX = 1 - nD/2
cR = Ntot/6                                   # coefficient of rho R[g_rho]
cT = cR - 4*kX                                # on the two modes with delta rho = 0 (s2)
cA_per = Ns*R(1, 6) + R(4, 6) - R(2, 6) - nD*R(4, 6)
cA_fs = Ns*R(1, 6) + R(4, 6) - R(2, 6) + nD*R(1, 3)
cA_sm = -cR/2
cW = cR + kX*r
cText = cR - 2*kX
rows = [("c_R", cR), ("kappa_X", kX), ("c_T", cT), ("c_T^ext", cText), ("c_W(r)", cW),
        ("c_A periodic", cA_per), ("c_A fixed-state", cA_fs), ("c_A fixed-state + vector holonomy (n<1)", cA_fs - 1),
        ("c_A smooth", cA_sm)]
print("\nidentities in (N_s, n_D):")
print("  c_A^per - c_R =", sp.simplify(cA_per - cR), "; c_A^fs - c_R - n_D =", sp.simplify(cA_fs - cR - nD))
print("  c_A^fs - c_T - (4 kappa_X + n_D) =", sp.simplify(cA_fs - cT - 4*kX - nD), "; c_A^per - c_T - 4 kappa_X =", sp.simplify(cA_per - cT - 4*kX))
print("  (c_A^fs - 1) - c_W(-1) =", sp.factor(sp.simplify(cA_fs - 1 - cW.subs(r, -1))), " [zero iff n_D = 0]")
print("  (c_A^fs - 1) - c_T - 3 kappa_X =", sp.factor(sp.simplify(cA_fs - 1 - cT - 3*kX)), " [zero iff n_D = 0]")
print("  c_W(r) - c_T =", sp.factor(cW - cT), "; d c_W / d r =", sp.diff(cW, r))
print("  c_A^sm - c_T =", sp.factor(sp.simplify(cA_sm - cT)), "; c_A^fs - c_T^ext =", sp.simplify(cA_fs - cText))
print("\n%-42s %-22s %-10s %-10s" % ("quantity", "general", "(6,0)", "(6,2)"))
for name, e in rows:
    print("%-42s %-22s %-10s %-10s" % (name, sp.simplify(e), sp.simplify(e.subs({Ns: 6, nD: 0})), sp.simplify(e.subs({Ns: 6, nD: 2}))))
print("\ngaps c_A - c_T at (6,2): periodic", (cA_per - cT).subs({Ns: 6, nD: 2}), ", fixed-state", (cA_fs - cT).subs({Ns: 6, nD: 2}),
      ", fixed-state + holonomy n<1 / n>1", (cA_fs - 1 - cT).subs({Ns: 6, nD: 2}), "/", (cA_fs + 1 - cT).subs({Ns: 6, nD: 2}),
      ", smooth", (cA_sm - cT).subs({Ns: 6, nD: 2}))
print("uniform E_delta contact -N_tot/4 at (6,2):", (-Ntot/4).subs({Ns: 6, nD: 2}))
print("Weyl-coefficient gaps (appH, content paragraph) at n_D = 2: periodic", 4 - 2*2, ", fixed-state", 4 - 2, ", completed", 2 - 2,
      "; kappa_C^T at (6,2) =", (Ntot/120 - kX/3).subs({Ns: 6, nD: 2}))
# --- mass-weighted extension ----------------------------------------------------------------------------
fs_, fv, fD = sp.symbols('f_s f_v f_D')   # f(m^2) = int_{Lambda^-2}^inf ds s^-2 e^{-s m^2} / Lambda^2, per sector (ghosts with the connection)
Sn = Ns*fs_ + 2*fv - 4*nD*fD
Sk = fv - nD*fD/2
cTm = Sn/6 - 4*Sk
cAper_m = Sn/6
cAfs_m = Sn/6 + nD*fD
print("\nmass-weighted sums: S_n =", Sn, "; S_kappa =", Sk)
print("  c_T(m) =", sp.expand(cTm), "; c_A^per(m) - c_T(m) =", sp.simplify(cAper_m - cTm), "= 4 S_kappa ; c_A^fs(m) - c_T(m) =", sp.simplify(cAfs_m - cTm))
fb, ff = sp.symbols('f_b f_f')
sub = {Ns: 6, nD: 2, fs_: fb, fv: fb, fD: ff}
print("  (6,2), one bosonic and one fermionic mass: c_T =", sp.factor(cTm.subs(sub)), "; c_A^per =", sp.factor(cAper_m.subs(sub)),
      "; ratio c_A^per/c_T =", sp.simplify(cAper_m.subs(sub)/cTm.subs(sub)), "; c_A^fs =", sp.expand(cAfs_m.subs(sub)))
import mpmath as mp
mp.mp.dps = 30
for (L2, m2) in ((mp.mpf(10)**6, mp.mpf(1)), (mp.mpf(10)**8, mp.mpf(3))):
    f = mp.quad(lambda t: mp.exp(-t*m2)/t**2, [1/L2, 1, mp.inf])
    approx = L2 - m2*mp.log(L2/m2) - (1 - mp.euler)*m2
    print("  f(m^2) = int_{Lambda^-2}^inf ds s^-2 e^{-s m^2}: Lambda^2 =", mp.nstr(L2, 3), "m^2 =", m2, " f - [Lambda^2 - m^2 ln(Lambda^2/m^2) - (1-gamma) m^2] =", mp.nstr(f - approx, 5))
