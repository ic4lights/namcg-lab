"""
Proposal 021, script 3: (A) the spin excess of the antiperiodic Dirac cone equals the Lichnerowicz contact at n = 1;
                        (B) bookkeeping of c_A in the replica prescriptions, and of the contact/edge candidates, against c_T.
Normalisation (proposal 019 / 017): c is the coefficient in units where one real scalar component gives 1/6; S_area = c * Lambda^2 A /(8 pi);
statistical weights: scalar +1, connection +1 (4 comps), ghost -2 (1 comp), Dirac -1 (4 comps); alpha = 1.
"""
import sympy as sp
from fractions import Fraction as Fr

n = sp.symbols('n', positive=True)
Ns, nD = sp.symbols('N_s n_D')
Rat = sp.Rational

print('=== (A) cone constants per two-component block (heat-trace constant of Tr_n - n Tr_1, units A/(4 pi s)) ===')


def aset(N):
    return [Fr(2 * j - (N - 1), 2 * N) for j in range(N)]       # k/n, k = -(n-1)/2 .. (n-1)/2


for N in (1, 3, 5, 7, 9, 11, 13, 15):
    A = aset(N)
    s2 = sum(a * a for a in A)
    s1 = sum(abs(a) for a in A)
    AP = s2                                  # Dirac domain, a^2 + 1/6 per mode minus n/6
    P = s2 - s1                              # componentwise-regular domain, B2(|a|)
    assert AP == Fr(N * N - 1, 12 * N)
    assert P == -2 * AP                      # odd n
    assert P == Fr(1, 6) * (Fr(1, N) - N)    # = scalar-like flat-cone value for two components
print('odd n = 1..15: AP = (n^2-1)/(12 n), P = -2 AP = (1/6)(1/n - n)  (scalar-like) : OK')
AP_n = (n**2 - 1) / (12 * n)
P_n = Rat(1, 6) * (1 / n - n)
dAP = sp.diff(AP_n, n).subs(n, 1)
dP = sp.diff(P_n, n).subs(n, 1)
print('d/dn at n=1:  AP =', dAP, '  P =', dP, '  AP/P =', dAP / dP)
Q = sp.symbols('Q')
contact = -(1 - n) * 2 * Q                   # per block of two components, E = E0 + Q R, R continued with its conical delta
dcontact = sp.diff(contact, n).subs(n, 1)
print('contact term derivative per block = 2Q;  (AP - P)\' =', dAP - dP, ' => Q =', sp.solve(sp.Eq(dAP - dP, dcontact), Q)[0], '(per component; Lichnerowicz R/4)')
print('only F\'(1) enters S = (1-n d_n)F|_{n=1} when F(1)=0:  (1 - n d_n)(AP_n) =', sp.simplify((AP_n - n * sp.diff(AP_n, n)).subs(n, 1)), ' ; -F\'(1) =', -dAP)

print()
print('=== (B) bookkeeping ===')
b = 1 - nD / 2
W = Ns + 2 - 4 * nD                          # weighted component count N_tot
cT = W / 6 - 4 * b
c_unrot = W / 6                              # replica (I), unrotated pull-back gluing of every Cartesian component
c_AP = W / 6 + nD                            # replica (I), antiperiodic (Tr rho^n) Dirac, unrotated vectors
c_smooth = -W / 12                           # first-order smooth Poisson deformation: Q = 1/4 in every sector
Q_boson = Ns * Rat(1, 4) + 4 * Rat(1, 4) - 2 * Rat(1, 4)     # sum w tr Q over scalars, connection, ghosts (torsion reading)
c_AP_bosonQ = c_AP - Q_boson                 # (I)-AP plus bosonic Q=1/4 contacts
print('c_T          =', sp.expand(cT))
print('c_A unrot    =', sp.expand(c_unrot), ' gap =', sp.expand(c_unrot - cT))
print('c_A AP       =', sp.expand(c_AP), ' gap =', sp.expand(c_AP - cT))
print('c_A smooth   =', sp.expand(c_smooth), ' gap =', sp.expand(c_smooth - cT))
print('c_A AP + bosonic Q=1/4 contacts - c_A smooth =', sp.simplify(c_AP_bosonQ - c_smooth), '  (identity: the smooth value IS AP + bosonic contacts)')
c_kabat = c_AP - 1                           # AP Dirac + vector contact (Kabat / Donnelly-Wall, -1 in these units)
print('c_A AP + vector contact -1 =', sp.expand(c_kabat), ' gap =', sp.expand(c_kabat - cT))
print()
sub = {Ns: 6, nD: 2}
for name, e in [('c_T', cT), ('unrot', c_unrot), ('AP', c_AP), ('smooth', c_smooth), ('AP+vector contact', c_kabat)]:
    print(f'  IKKT (N_s=6, n_D=2): {name:18s} = {e.subs(sub)}')
print('  W at IKKT =', W.subs(sub), ', b =', b.subs(nD, 2))
print()
print('covariant-QFT benchmark (minimally coupled scalars, Dirac with Lichnerowicz, Maxwell with Ricci, ghosts minimal), N=4 SYM content 6 + 2 Dirac + 1 vector:')
cov = Rat(6, 6) + 2 * Rat(1, 3) + (Rat(4, 6) - 1) - Rat(2, 6)
print('  Sum w tr(1/6 - Q) =', cov, ' (equal for induced action and cone entropy with the Kabat contact)')
print()
print('smooth-reading equality c_smooth = c_T  <=>', sp.solve(sp.Eq(c_smooth, cT), Ns), '(N_s as a function of n_D)')
for nd in (Rat(1, 2), 1, 2, Rat(5, 2), 3):
    ns = (14 - 4 * nd)
    Wv = ns + 2 - 4 * nd
    print(f'   n_D={nd}: N_s={ns}, W={Wv}, c_T={cT.subs({Ns: ns, nD: nd})}, c_smooth={c_smooth.subs({Ns: ns, nD: nd})}')
print('   (D = N_s + 4 = 18 - 4 n_D; the supersymmetric D=6 (n_D=1, N_s=2) is NOT on this line: gap =', sp.simplify((c_smooth - cT).subs({Ns: 2, nD: 1})), ')')
print('   (D=4, n_D=1/2, N_s=0: gap =', sp.simplify((c_smooth - cT).subs({Ns: 0, nD: Rat(1, 2)})), ')')
print()
print('sector-resolved gap Delta_s = c_A,s - c_T,s (AP), per field (alpha=1): scalar 0, connection 4, ghost 0, Dirac', sp.Rational(1, 3) - Rat(4, 3))
Lv, Lf = sp.symbols('Lambda_v^2 Lambda_f^2')
print('   gap with separate cutoffs, n_D=2: ', 4 * Lv + 2 * (sp.Rational(1, 3) - Rat(4, 3)) * Lf, '  vanishes iff Lambda_f^2 = 2 Lambda_v^2 (not forced by anything derived)')
