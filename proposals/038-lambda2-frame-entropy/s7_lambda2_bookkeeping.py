"""s7: Lambda^2-order area-coefficient bookkeeping for the 031 hypotheses (Poisson limit, one loop, alpha=1, totally geodesic Sigma,
first order in 1-n, n<1 branch sigma=+1 / n>1 branch sigma=-1).

Units: the entropy is S = (Lambda^2 A /8pi) c per sector, c = 1/6 for one flat-cone scalar component (1/G = c Lambda^2/(2 pi)).
Inputs taken from Appendix H (not re-derived): c_R = N_tot/6 (replica, rho regular), c_T = N_tot/6 - 4 kappa_X (quadratic form on the two
delta-rho=0 modes), N_tot = N_s + 2 - 4 n_D, kappa_X = 1 - n_D/2.
Inputs derived/checked here: twisted-cone constant (s2), irreducible torsion split of X (s1, s4).
"""
import sympy as sp
from sympy import Rational as Q

Ns, nD, aV, sig = sp.symbols('N_s n_D alpha_v sigma')
Ntot = Ns + 2 - 4*nD
kX = 1 - nD/2

cA_periodic = Ntot/6                              # unrotated periodic gluing of every sector (graded trace for the Dirac fields)
cA_fixed    = Ntot/6 + nD                         # fixed-state: antiperiodic Dirac (+1 per Dirac field over periodic)
cT          = Ntot/6 - 4*kX

def contact_E():          # uniform E_delta = pi(1-n) delta on every component, Q=1/4 : c -> c - Q * (weighted component count)
    return -Ntot/4

def contact_hol_vec(alpha_v=aV):   # holonomy alpha_v J12 of the vector bundle around Sigma: two components with J12 = +-1 twist by alpha_v|1-n|
    return -alpha_v*sig                # from C(n,a) = B_2(a)/(2n) - n/12, first order in |a| (s2)

def contact_hol_dirac(alpha_f=sp.Symbol('alpha_f')):
    return 0                          # a^2 + 1/6 per block with the less singular extension, sum_k a_k = 0 : no term linear in the shift (see below)

print("Dirac holonomy shift: sum_k (a_k+d)^2 over the symmetric twists a_k = k/n, k=-(n-1)/2..(n-1)/2:")
nn, d_ = sp.symbols('n d')
# check sum_k a_k = 0 and sum a_k^2 = (n^2-1)/(12 n) for integer n
for nint in [2, 3, 4, 5, 7]:
    ks = [sp.Rational(2*j - (nint-1), 2) for j in range(nint)]
    ak = [k/nint for k in ks]
    assert sum(ak) == 0 and sum(a**2 for a in ak) == sp.Rational(nint**2-1, 12*nint)
    first_order = sp.expand(sum((a + d_)**2 for a in ak)).coeff(d_, 1)
    assert first_order == 0
print("   first-order coefficient in the common shift d vanishes (n=2,3,4,5,7): Dirac holonomy contact = 0 at first order.\n")

rows = {
 "fixed-state replica (no delta, no holonomy)":              cA_fixed,
 "fixed-state + vector holonomy alpha_v":                    cA_fixed + contact_hol_vec(),
 "periodic Dirac (graded trace), no delta, no holonomy":      cA_periodic,
 "uniform E_delta only (smooth-type bosonic+Dirac contact)":  cA_periodic + contact_E(),
 "completed: uniform E_delta + vector holonomy alpha_v":      cA_periodic + contact_E() + contact_hol_vec(),
}
print("Area coefficient c and residue c - c_T  (c_T = N_tot/6 - 4 kappa_X):")
for name, c in rows.items():
    print(f"  {name}\n      c      = {sp.simplify(c)}\n      c-c_T  = {sp.simplify(c - cT)}")

print("\nBosonic content n_D = 0, alpha_v = 1 (cone angle fixes c_a = 1):")
for name, c in rows.items():
    res = sp.simplify((c - cT).subs({nD: 0, aV: 1}))
    print(f"  {name}: residue = {res}")
    for s in (1, -1):
        r_ = sp.simplify(res.subs(sig, s))
        sols = sp.solve(sp.Eq(r_, 0), Ns)
        print(f"        sigma={s:+d}: residue = {r_}; zero at N_s = {sols}")

print("\nGeneral N_s-independence argument: residue is linear in N_s with slope")
print("   uniform E_delta:", sp.diff(sp.simplify((rows['uniform E_delta only (smooth-type bosonic+Dirac contact)'] - cT).subs(nD, 0)), Ns),
      "(scalars carry the delta), all other rows: 0")

print("\nPer-sector cutoffs (scalars Lambda_s, connection+ghost Lambda_v), n_D = 0, in units Lambda^2/(2 pi):")
Ls, Lv, = sp.symbols('Lambda_s Lambda_v', positive=True)
c_s = Ns*Q(1, 6)*Ls**2
c_v = (Q(2, 3) - Q(1, 3))*Lv**2
cT_split = c_s + c_v - 4*Lv**2
cA_split = c_s + c_v
print("   1/G_A - 1/G_T = (c_A - c_T)/(2 pi) =", sp.simplify((cA_split - cT_split)/2), "/ pi")
E_split = -Q(1, 4)*Ns*Ls**2 - Q(1, 4)*(4 - 2)*Lv**2
print("   residue after uniform E_delta (alpha_v=0):", sp.simplify(cA_split + E_split - cT_split), " -> zero iff N_s Lambda_s^2 = 14 Lambda_v^2")
print("   residue after vector holonomy only (alpha_v=1, sigma=+1):", sp.simplify(cA_split - Lv**2 - cT_split))

print("\nNoether (pure-diffeo) coefficient of R in the induced Lagrangian c_R rho R[g_rho] + kappa_X rho^2 X, X = TT, for the presentations of s1:")
r_pres = {"b-presentation (X independent)": 0, "keep R, V^2, S^2 (q^2 eliminated; ledger identity)": -2, "keep R, S^2, q^2 (V^2 eliminated)": 1,
          "keep R, V^2, q^2 (S^2 eliminated)": 4, "mode-null remainder (Z = 2S^2 - q^2)": -4}
for name, r_ in r_pres.items():
    cW = Ntot/6 + kX*r_
    print(f"  r = {r_:+d}  {name}: c_W = {sp.simplify(cW)};  c_W - c_T = {sp.simplify(cW - cT)}")
print("  (r = -4 is the only value with c_W = c_T for all contents; on the delta-rho=0 modes X = -4<R> (s4).)")
