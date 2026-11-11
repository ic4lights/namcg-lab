"""068-j-spherical-reduction-consistency: stage 2, spherical
three-function (A,B,C) and five-function (with g_tr = D(r)) identity
checks.
Run:
  python -I proposals/068-j-spherical-reduction-consistency/ecg_cas_stage2.py \
    > proposals/068-j-spherical-reduction-consistency/ecg_cas_stage2.out
Shares conventions and helpers with ecg_cas_stage1.py through
ecg_cas_lib.py (whose docstring records the shared conventions).

The two-function slice objects L2, EN, EF, Fdef needed by T3 are rebuilt
here in this process (the stage scripts run as separate processes); this
duplicates computation, not conventions.

Every check prints PASS/FAIL and is counted; stdout is the byte-reproducible
record (wall-clock timings go to stderr) and the shipped .out file is
authoritative and must reproduce byte-identically:
  python -I proposals/068-j-spherical-reduction-consistency/ecg_cas_stage2.py \
    > proposals/068-j-spherical-reduction-consistency/ecg_cas_stage2.out
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ecg_cas_lib import *

hb('stage2 start')

# ------------------------------------------------ two-function slice (input to T3)
Nr, fr = fn('N'), fn('f')
gmN = build_metric([[-Nr ** 2, 0, 0, 0], [0, 1 / fr, 0, 0],
                    [0, 0, r ** 2, 0], [0, 0, 0, r ** 2 * sp.sin(th) ** 2]],
                   [0, r, th, ph])
hb('gmN tensors built')
PNf = cubic_P(gmN)
hb('P[N,f] summed')
L2 = Nr * r ** 2 * (gmN['Rscalar'] - 2 * LAM + kap * PNf)
EN = el(L2, Nr)
EF = el(L2, fr)
hb('EN, EF of L2 computed')
Brec = (sp.Rational(4, 3) * fr.diff(r) ** 3
        - (8 / r) * fr * fr.diff(r, 2) * (r * fr.diff(r) / 2 + 1 - fr)
        + (4 / r) * fr.diff(r) ** 2
        - (8 / r ** 2) * fr * fr.diff(r) * (fr - 1))
Fdef = sp.expand(2 * r * (1 - fr) - 3 * ALP * Brec)
hb('Fdef built')

# ------------------------------------------------ T3: spherical 3-function
Ar, Br, Cr = fn('A'), fn('B'), fn('C')
gmABC = build_metric([[-Ar, 0, 0, 0], [0, Br, 0, 0], [0, 0, Cr, 0],
                      [0, 0, 0, Cr * sp.sin(th) ** 2]], [0, r, th, ph])
hb('gmABC tensors built')
PABC = cubic_P(gmABC)
hb('P[A,B,C] summed')
RABC = gmABC['Rscalar']
sABC = sp.sqrt(sp.simplify(gmABC['detgL']) / sp.sin(th) ** 2)
L4 = sABC * (RABC - 2 * LAM + kap * PABC)

slice_sub = {Ar: Nr ** 2, Br: 1 / fr, Cr: r ** 2}
L4sub = sp.simplify(L4.subs(slice_sub))
report('T3a L4[A=N^2, B=1/f, C=r^2] = L[N,f] exactly',
       zero(L4sub - L2))
hb('T3a done')

EA = el(L4, Ar, simp=None)
EB = el(L4, Br, simp=None)
EC = el(L4, Cr, simp=None)
hb('EA,EB,EC computed')
print('orders: EA A %d B %d C %d | EB A %d B %d C %d | EC A %d B %d C %d'
      % (maxd(EA, Ar), maxd(EA, Br), maxd(EA, Cr), maxd(EB, Ar),
         maxd(EB, Br), maxd(EB, Cr), maxd(EC, Ar), maxd(EC, Br),
         maxd(EC, Cr)))

bid = sp.simplify(sp.diff(EA * Ar + EB * Br + EC * Cr, r)
                  - (EA * Ar.diff(r) + EB * Br.diff(r) + EC * Cr.diff(r)))
report('T3b off-shell radial-diffeomorphism (Noether/Bianchi) identity, '
       '3-function spherical system', bid == 0)
hb('T3b done')

ehat_t = sp.together(EA * Ar / sABC)
ehat_r = sp.together(EB * Br / sABC)
ehat_th = sp.together(EC * Cr / (2 * sABC))
bian = sp.simplify(ehat_r.diff(r) + (Nr.diff(r) / Nr) * (ehat_r - ehat_t)
                   + 2 / r * (ehat_r - ehat_th))
bians = sp.simplify(bian.subs(slice_sub))
report('T3c component Bianchi identity on the 2-function slice (off shell)',
       bians == 0)
hb('T3c done')

ENs = sp.simplify(EN.subs(slice_sub))
EFs = sp.simplify(EF.subs(slice_sub))
report('T3d reduced chain rule: E_N[N,f] = 2N * E_A|_{A=N^2,B=1/f,C=r^2} '
       '(tt component)', zero(ENs - 2 * Nr * sp.simplify(EA.subs(slice_sub))))
report('T3e reduced chain rule: E_f[N,f] = -(1/f^2) * E_B| (rr component, '
       'dB/df = -1/f^2)',
       zero(EFs + sp.simplify(EB.subs(slice_sub)) / fr ** 2))
hb('T3d/T3e done')

Flineq = sp.expand(Fdef - sp.Rational(2, 3) * LAM * r ** 3 - 4 * M)
sol = sp.solve(sp.Eq(Flineq, 0), fr.diff(r, 2), dict=True)
print('branches solving the first integral for f-prime-prime:', len(sol))
report('T3f first integral linear in f-prime-prime: exactly one branch',
       len(sol) == 1)
if sol:
    sol2 = sol[0][fr.diff(r, 2)]
    sol3 = sp.simplify(sp.diff(sol2, r))
    ECs = sp.simplify(EC.subs({Ar: 1, Br: 1 / fr, Cr: r ** 2}))
    ECos = sp.simplify(sp.factor(sp.simplify(
        ECs.subs({fr.diff(r, 2): sol2, fr.diff(r, 3): sol3}))))
    report('T3g angular operator E_C restricted to N=1 slice vanishes on the '
           'on-shell branch (f2 and f3 eliminated along the branch)',
           ECos == 0)
else:
    report('T3g angular operator E_C restricted to N=1 slice vanishes on the '
           'on-shell branch (f2 and f3 eliminated along the branch)', False)
hb('T3g done')

# ------------------------------------------------ T4: tr component
Dr = fn('D')
gm5 = build_metric([[-Nr ** 2, Dr, 0, 0], [Dr, 1 / fr, 0, 0],
                    [0, 0, r ** 2, 0], [0, 0, 0, r ** 2 * sp.sin(th) ** 2]],
                   [0, r, th, ph])
hb('gm5 tensors built')
R5 = gm5['Rscalar']
P5 = cubic_P(gm5)
hb('P[N,f,D] summed')
s5 = sp.sqrt(sp.simplify(gm5['detgL']) / sp.sin(th) ** 2)
L5 = s5 * (R5 - 2 * LAM + kap * P5)
ED = el(L5, Dr)
ED0 = sp.simplify(ED.subs(Dr, 0))
report('T4a mixed tr operator vanishes identically on D = 0 (no tr flux in '
       'the static diagonal sector; finite-order check, full D-odd '
       'structure not expanded)', ED0 == 0)
hb('T4a done')

print()
print('ALL PASS: %s (%d/%d)' % (len(FAILS) == 0,
                                len(RESULTS) - len(FAILS), len(RESULTS)))
if FAILS:
    print('failed checks:')
    for tag in FAILS:
        print('  ' + tag)
print('[elapsed %.3f s]' % (time.time() - t0), file=sys.stderr)
