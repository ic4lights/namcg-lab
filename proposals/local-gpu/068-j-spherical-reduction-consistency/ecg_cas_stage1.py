"""068-j-spherical-reduction-consistency: stage 1, conventions, the
recorded appH Problem-J identities against the literal eq:ECG reduced
action, maximally symmetric branch, regular centre, tail residual.

Run:
  python -I proposals/068-j-spherical-reduction-consistency/ecg_cas_stage1.py \
    > proposals/068-j-spherical-reduction-consistency/ecg_cas_stage1.out

Conventions, derived from the manuscript before any computation:
- ch09 (after eq:ECG): signature (-,+,+,+); 'with the Riemann convention
  for which R > 0 on spheres'. eq:ECG invariant P = 12 R_a^c_b^d R_c^e_d^f
  R_e^a_f^b + R^ab_cd R^cd_ef R^ef_ab - 12 R_abcd R^ac R^bd
  + 8 R_a^b R_b^c R_c^a. eq:S-ECG: S = int d4x sqrt(-g) [ (R - 2 Lambda_eff)
  / (16 pi G_eff) + beta_ECG P ].
- appH (Problem J): reduced Lagrangian L[N,f] = N r^2 (R - 2 Lambda_eff
  + kappa P), kappa = 16 pi G_eff beta_ECG, per unit coordinate time and
  angular volume; ansatz ds^2 = -N(r)^2 dt^2 + dr^2/f(r) + r^2 dOmega^2.
- Reduced coupling alpha = -kappa (appH; ch09).

Riemann convention used here:
  R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc}
              + Gamma^a_{ce} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{bc},
i.e. [nabla_c, nabla_d] v^a = R^a_{bcd} v^b. T0a enforces R(unit 2-sphere)
= +2, matching the manuscript statement.

Checks named 'recorded ... reproduced' test the appH Problem-J identities
against the literal eq:ECG reading; their FAIL results are the bounded
discrepancy reported in the proposal. Every check prints PASS/FAIL and is
counted; stdout is the byte-reproducible record (wall-clock timings go to
stderr) and the shipped .out file is authoritative and must reproduce
byte-identically by the run command above. The spherical three-function
and five-function identity checks are in ecg_cas_stage2.py (separate
process: the general three-function tensors are memory-hungry).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ecg_cas_lib import *

# ------------------------------------------------ T0: conventions
gm2 = build_metric([[1, 0], [0, sp.sin(th) ** 2]], [th, ph])
report('T0a R(unit 2-sphere) = +2', zero(gm2['Rscalar'] - 2))
hb('T0a done')

Nr, fr = fn('N'), fn('f')
fss = 1 - 2 * M / r
gm4 = build_metric([[-fss, 0, 0, 0], [0, 1 / fss, 0, 0], [0, 0, r ** 2, 0],
                    [0, 0, 0, r ** 2 * sp.sin(th) ** 2]], [0, r, th, ph])
P4 = cubic_P(gm4)
Pss = sp.simplify(P4)
Rss = sp.simplify(gm4['Rscalar'])
report('T0b R = 0 on the f = 1-2M/r metric', Rss == 0)
report('T0c P nonzero on the f = 1-2M/r metric', Pss != 0)
show('P[1-2M/r]', Pss)
hb('T0b/T0c done')

gmN = build_metric([[-Nr ** 2, 0, 0, 0], [0, 1 / fr, 0, 0],
                    [0, 0, r ** 2, 0], [0, 0, 0, r ** 2 * sp.sin(th) ** 2]],
                   [0, r, th, ph])
hb('gmN tensors built')
PNf = cubic_P(gmN)
hb('P[N,f] summed')
report('T0d P[N,f] is theta-independent (scalar check)',
       sp.simplify(sp.diff(PNf, th)) == 0)
PN1 = sp.factor(sp.simplify(PNf.subs(Nr, 1)))
show('P[N=1,f]', PN1)
hb('P[N=1,f] done')

# ------------------------------------------------ T1: recorded identities
L2 = Nr * r ** 2 * (gmN['Rscalar'] - 2 * LAM + kap * PNf)
EF = el(L2, fr)
EN = el(L2, Nr)
hb('EL operators of L2 computed')
print('derivative orders: EN f %d N %d | EF f %d N %d'
      % (maxd(EN, fr), maxd(EN, Nr), maxd(EF, fr), maxd(EF, Nr)))

EN1 = sp.simplify(EN.subs({Nr: 1, Nr.diff(r): 0, Nr.diff(r, 2): 0,
                           Nr.diff(r, 3): 0}))
EF1 = sp.simplify(EF.subs({Nr: 1, Nr.diff(r): 0, Nr.diff(r, 2): 0,
                           Nr.diff(r, 3): 0}))
hb('EN1, EF1 simplified')

Brec = (sp.Rational(4, 3) * fr.diff(r) ** 3
        - (8 / r) * fr * fr.diff(r, 2) * (r * fr.diff(r) / 2 + 1 - fr)
        + (4 / r) * fr.diff(r) ** 2
        - (8 / r ** 2) * fr * fr.diff(r) * (fr - 1))

EF1_GR = sp.simplify(EF1.subs(kap, 0))
report('T1a-GRA part of E_f|_{N=1} vanishes identically', EF1_GR == 0)
report('T1a recorded identity E_f|_{N=1} = 0 reproduced (CAS: cubic part '
       'nonzero, NOT reproduced)', EF1 == 0)
show('E_f|_{N=1} (literal eq:ECG)', EF1)
hb('T1a done')

FtotK = (2 * r * (1 - fr) + 3 * kap * Brec
         - sp.Rational(2, 3) * LAM * r ** 3)
report('T1b recorded identity E_N|_{N=1} = d/dr[2r(1-f) + 3 kappa B_rec '
       '- (2/3) Lam r^3] reproduced (CAS: NOT reproduced)',
       zero(EN1 - sp.diff(FtotK, r)))
Implied = sp.expand(EN1 - sp.diff(2 * r * (1 - fr)
                                  - sp.Rational(2, 3) * LAM * r ** 3, r))
helm = el(Implied, fr, simp=sp.simplify)
report('T1b2 the implied integrand (E_N|_{N=1} - d/dr[2r(1-f)-(2/3)Lam r^3]) '
       'is NOT a total d/dr of any local functional of f (Helmholtz '
       'criterion fails; bounded to the literal eq:ECG reading and any '
       'overall normalisation)', helm != 0)
show('Helmholtz of implied integrand', helm)
hb('T1b/T1b2 done')

EN1_GR = sp.simplify(EN1.subs({kap: 0, LAM: 0}))
report('T1c GR part: E_N|_{N=1} = d/dr[2r(1-f)] - d/dr[r^2 f\'], i.e. the '
       'recorded GR term misses the -(r^2 f-prime)-prime piece of the '
       'reduced-action N operator',
       zero(EN1_GR - (sp.diff(2 * r * (1 - fr), r)
                      - sp.diff(r ** 2 * fr.diff(r), r))))
hb('T1c done')

Fdef = sp.expand(2 * r * (1 - fr) - 3 * ALP * Brec)
d2Fdfpp = sp.simplify(sp.diff(sp.diff(Fdef, fr.diff(r, 2)), fr.diff(r, 2)))
report('T1d recorded F[f] linear in f-prime-prime (single algebraic branch '
       'of the recorded first integral)', d2Fdfpp == 0)
show('d Fdef / d f2', sp.simplify(sp.diff(Fdef, fr.diff(r, 2))))
hb('T1d done')

# ------------------------------------------------ T2: branches, residual
k = sp.symbols('k', real=True)
subms = {fr: 1 - k * r ** 2, fr.diff(r): -2 * k * r, fr.diff(r, 2): -2 * k}
ENms = sp.simplify(EN1.subs(subms))
EFms = sp.simplify(EF1.subs(subms))
report('T2a E_f|_{N=1}[1-kr^2] = 0 for all k (AdS slice is special)',
       EFms == 0)
show('E_N|_{N=1}[1-kr^2] / r^2', sp.collect(
    sp.expand(sp.simplify(ENms / r ** 2)), [k ** 3, k]))
report('T2b recorded MS relation: E_N|_{N=1}[1-kr^2] = 6 r^2 (k + 8 kappa '
       'k^3 - Lam/3) reproduced (CAS: NOT reproduced)',
       zero(ENms - 6 * r ** 2 * (k + 8 * kap * k ** 3 - LAM / 3)))
jets0 = {Nr: 1, Nr.diff(r): 0, Nr.diff(r, 2): 0, Nr.diff(r, 3): 0}
tt_ms = sp.simplify((gmN['Rscalar'] - 2 * LAM + kap * PNf)
                    .subs(dict(list(subms.items()) + list(jets0.items()))))
show('r^2 (R - 2 Lam + kap P)[N=1, 1-kr^2] / r^2', sp.collect(
    sp.expand(sp.simplify(tt_ms)), [k ** 3, k]))
Bms = sp.simplify(Brec.subs(subms))
report('T2b2 internal consistency of the RECORDED passage: B_rec[1-kr^2] '
       '= (16/3) k^3 r^3, so d/dr[2r(1-f) - 3 alpha B_rec - (2/3)Lam r^3] '
       'at f=1-kr^2 equals 6 r^2 (k + 8 kappa k^3 - Lam/3) with '
       'alpha = -kappa',
       zero(Bms - sp.Rational(16, 3) * k ** 3 * r ** 3))
hb('T2 done part 1')

c2 = sp.symbols('c2', real=True)
fs = 1 + c2 * r ** 2
subser = {fr: fs, fr.diff(r): sp.diff(fs, r), fr.diff(r, 2): sp.diff(fs, r, 2)}
Bser = sp.simplify(Brec.subs(subser))
show('B_rec[1+c2 r^2]', Bser)
report('T2c B_rec[1+c2 r^2] = -(16/3) c2^3 r^3 exactly',
       zero(Bser + sp.Rational(16, 3) * c2 ** 3 * r ** 3))
FtotS = 2 * r * (1 - fr) - 3 * ALP * Brec - sp.Rational(2, 3) * LAM * r ** 3
Fser = sp.simplify(FtotS.subs(subser))
show('Ftot[1+c2 r^2]', Fser)
report('T2d Ftot[1+c2 r^2] = r^3 (-2 c2 + 16 alpha c2^3 - (2/3) Lam) '
       'exactly (recorded-identity side)',
       zero(Fser - r ** 3 * (-2 * c2 + 16 * ALP * c2 ** 3
                             - sp.Rational(2, 3) * LAM)))
hb('T2c/T2d done')

r0 = sp.symbols('r0', positive=True)
freg = 1 - 2 * M * r ** 2 / (r ** 3 + r0 ** 3)
subreg = {fr: freg, fr.diff(r): sp.diff(freg, r),
          fr.diff(r, 2): sp.diff(freg, r, 2)}
Freg = sp.simplify(FtotS.subs(subreg))
Freg0 = sp.series(Freg, r, 0, 1).removeO()
show('Ftot[f_reg] value at r=0', Freg0)
report('T2e regular profile: Ftot[f_reg] -> 0 at r -> 0 (the integration '
       'constant of the recorded first integral would have to vanish)',
       Freg0 == 0)
Freg_ser = sp.series(Freg, r, 0, 4).removeO()
show('Ftot[f_reg] small-r (up to r^3)', Freg_ser)
report('T2e2 Ftot[f_reg] is not constant for generic (M, r0, alpha): its '
       'leading small-r term is (4M/r0^3 + 48 alpha M^2 (2 r0^3)/(r0^6 '
       'r0^3)-type) r^3 (coefficient printed; nonzero symbolically)',
       sp.simplify(sp.Poly(Freg_ser, r).coeff_monomial(r ** 3)) != 0)
hb('T2e done')

a = sp.symbols('a', positive=True)
frat = 1 - 2 * M * r ** 2 / (r ** 3 + a)
subrat = {fr: frat, fr.diff(r): sp.diff(frat, r),
          fr.diff(r, 2): sp.diff(frat, r, 2)}
Brat = sp.simplify(Brec.subs(subrat))
res = sp.series(2 * r * (1 - frat) - 3 * ALP * Brat
                - sp.Rational(2, 3) * LAM * r ** 3 - 4 * M, r, sp.oo, 6)
res = sp.simplify(res.removeO())
show('F[f_rat] - 4M large-r (Lam=0)', res)
report('T2f rational-profile residual = -4Ma/r^3 - 432 alpha M^2/r^5 '
       '(recorded eq:fr-ECG, recorded-identity side)',
       zero(res.subs(LAM, 0) - (-4 * M * a / r ** 3
            - 432 * ALP * M ** 2 / r ** 5)))

dFrat = sp.simplify(sp.diff(2 * r * (1 - frat) - 3 * ALP * Brat, r)
                    - sp.Rational(2, 3) * LAM * r ** 2)
solL = sp.solve(sp.Eq(dFrat, 0), LAM)
dLdr = sp.simplify(sp.diff(solL[0], r))
report('T2g no constant Lam makes dF[f_rat] identically zero when M*a != 0 '
       '(the required Lam(r) is not constant; recorded, not adopted)',
       dLdr != 0)
show('Lam(r) required by dF[f_rat] = 0', solL[0])
show('d Lam(r)/dr', dLdr)
hb('T2 done')

print()
print('ALL PASS: %s (%d/%d)' % (len(FAILS) == 0,
                                len(RESULTS) - len(FAILS), len(RESULTS)))
if FAILS:
    print('failed checks (bounded discrepancy record; see proposal):')
    for tag in FAILS:
        print('  ' + tag)
print('[elapsed %.3f s]' % (time.time() - t0), file=sys.stderr)
