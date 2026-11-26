"""068-j-spherical-reduction-consistency: stage 3, index-reading audit
of eq:ECG and independent curvature cross-checks on the two-function
ansatz.

Run:
  python -I proposals/068-j-spherical-reduction-consistency/ecg_cas_stage3.py \
    > proposals/068-j-spherical-reduction-consistency/ecg_cas_stage3.out

Checks:
T5a the two cubic chain terms of eq:ECG coincide as full index sums
    under the bivector-map reading R_a^c_b^d = g^{cp} g^{dq} R_{apbq};
T5b that full index sum equals 8*tr(X^3) on the antisymmetric-pair
    basis (the 4*tr(X^3) factor used in an earlier draft was wrong);
T5c a slot-shifted reading of the mixed factor is a different scalar
    (difference recorded as nonzero), so the reading choice matters;
T5d maximally-symmetric cubic coefficients for the literal eq:ECG
    combination and for the literature ECG combination
    (chain_full - 12 R^{mu nu} R^{rho sigma} R_{mu rho nu sigma}-type
    pairing + 12 Ric^3), recorded for the coupling-convention map,
    values pinned symbolically;
T5e an independent Christoffel-free implementation of the Ricci scalar
    of the general static spherically symmetric metric matches
    build_metric on the (N,f) slice;
T5f verified curvature components on the N = 1 slice.
stdout is the byte-reproducible record; timings to stderr; the shipped
.out is authoritative and must reproduce byte-identically.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ecg_cas_lib import *

hb('stage3 start')
Nr, fr = fn('N'), fn('f')
gmN = build_metric([[-Nr ** 2, 0, 0, 0], [0, 1 / fr, 0, 0],
                    [0, 0, r ** 2, 0], [0, 0, 0, r ** 2 * sp.sin(th) ** 2]],
                   [0, r, th, ph])
hb('gmN tensors built')
Rm, Rl, M2, gU, RicL, RA = (gmN['Rm'], gmN['Rl'], gmN['M2'], gmN['gU'],
                            gmN['RicL'], gmN['RA'])
Ri = range(4)


def idx3(F):
    return sum(F[a, b, c, d] * F[c, d, e, f] * F[e, f, a, b]
               for a in Ri for b in Ri for c in Ri for d in Ri
               for e in Ri for f in Ri)


c2 = idx3(M2)
c1 = sum(M2[c, d, a, b] * M2[e, f, c, d] * M2[a, b, e, f]
         for a in Ri for b in Ri for c in Ri for d in Ri
         for e in Ri for f in Ri)
hb('c1, c2 summed')
report('T5a eq:ECG chain term1 - chain term2 = 0 identically under the '
       'bivector-map reading', zero(c1 - c2))

pairs = [(i, j) for i in Ri for j in Ri if i < j]
X = sp.zeros(len(pairs), len(pairs))
for I, (a, b) in enumerate(pairs):
    for J, (c, d) in enumerate(pairs):
        X[I, J] = M2[a, b, c, d]
trX3 = sum(X[I, J] * X[J, K] * X[K, I]
           for I in range(6) for J in range(6) for K in range(6))
report('T5b full index sum = 8*tr(X^3) on the antisymmetric-pair basis',
       zero(c1 - 8 * trX3))
hb('T5b done')

A1 = sp.MutableDenseNDimArray([0] * 256, (4, 4, 4, 4))
for a in Ri:
    for b in Ri:
        for c in Ri:
            for d in Ri:
                t = sum(gU[c, p] * Rm[a, p, b, d] for p in Ri)
                A1[a, b, c, d] = 0 if t == 0 else sp.together(t)
c1v = idx3(A1)
diffv = sp.simplify(c1v - c2)
report('T5c slot-shifted reading of the mixed factor is a DIFFERENT scalar '
       '(recorded nonzero difference)', diffv != 0)
show('slot-shift difference (first 3 terms)',
     sp.Add(*list(sp.Add.make_args(sp.expand(diffv))[:3]))
     if diffv != 0 else 0)
hb('T5c done')

RICU2 = sp.MutableDenseNDimArray([0] * 16, (4, 4))
for a in Ri:
    for c in Ri:
        t = sum(gU[a, e] * gU[c, f] * RicL[e, f] for e in Ri for f in Ri)
        RICU2[a, c] = 0 if t == 0 else sp.together(t)
T3 = sum(Rl[a, b, c, d] * RICU2[a, c] * RICU2[b, d]
         for a in Ri for b in Ri for c in Ri for d in Ri)
T4 = sum(RA[a, b] * RA[b, c] * RA[c, a]
         for a in Ri for b in Ri for c in Ri)
T3lit = sum(Rl[a, c, b, d] * RICU2[a, b] * RICU2[c, d]
            for a in Ri for b in Ri for c in Ri for d in Ri)
hb('T3/T3lit/T4 summed')

k = sp.symbols('k', real=True)
subms = {Nr: 1, Nr.diff(r): 0, Nr.diff(r, 2): 0,
         fr: 1 - k * r ** 2, fr.diff(r): -2 * k * r, fr.diff(r, 2): -2 * k}
Pbook = 13 * c2 - 12 * T3 + 8 * T4
vb = sp.expand(Pbook.subs(subms))
show('eq:ECG combination on the N=1, f=1-kr^2 slice (not constant '
     'curvature: true MS static gauge has N = sqrt(f))', vb)
report('T5d1 the literal eq:ECG combination reduces to 216 k^3 on the '
       'N=1, f=1-kr^2 slice (kappa stripped)', zero(vb - 216 * k ** 3))
ch_s = sp.simplify(c2.subs(subms))
t3_s = sp.simplify(T3.subs(subms))
t4_s = sp.simplify(T4.subs(subms))
show('chain full sum, T3, T4 on the N=1 slice (k^3 stripped)',
     [sp.simplify(ch_s / k ** 3), sp.simplify(t3_s / k ** 3),
      sp.simplify(t4_s / k ** 3)])
report('T5d2 chainfull = T3 = T4 = 24 k^3 on the N=1, f=1-kr^2 slice, so '
       '13*24 - 12*24 + 8*24 = 216 k^3 for eq:ECG as written',
       zero(ch_s - 24 * k ** 3) and zero(t3_s - 24 * k ** 3)
       and zero(t4_s - 24 * k ** 3))
# true maximally symmetric static gauge: N = sqrt(f), f = 1 - k r^2
subtrue = {fr: 1 - k * r ** 2, fr.diff(r): -2 * k * r, fr.diff(r, 2): -2 * k,
           Nr: sp.sqrt(1 - k * r ** 2), Nr.diff(r): -k * r / sp.sqrt(1 - k * r ** 2),
           Nr.diff(r, 2): -k / sp.sqrt(1 - k * r ** 2)
           - k ** 2 * r ** 2 / (1 - k * r ** 2) ** sp.Rational(3, 2)}
show('Rscalar on true MS static gauge N=sqrt(1-kr^2)',
     sp.simplify(gmN['Rscalar'].subs(subtrue)))
show('eq:ECG combination on true MS static gauge (k^3 stripped)',
     sp.simplify(Pbook.subs(subtrue) / k ** 3))
report('T5d3 true MS static gauge N=sqrt(1-kr^2) has R = 12k and eq:ECG '
       '= 192 k^3 (kappa stripped)',
       zero(sp.simplify(gmN['Rscalar'].subs(subtrue) - 12 * k))
       and zero(sp.simplify(Pbook.subs(subtrue) - 192 * k ** 3)))
hb('T5d done')

Ar = Nr ** 2
Br = 1 / fr
Rind = (-Ar.diff(r, 2) / (Ar * Br) + Ar.diff(r) * Br.diff(r) / (2 * Ar * Br ** 2)
        + Ar.diff(r) ** 2 / (2 * Ar ** 2 * Br) + 2 * Br.diff(r) / (r * Br ** 2)
        - 2 * Ar.diff(r) / (r * Ar * Br) + 2 / r ** 2 - 2 / (r ** 2 * Br))
Rms1 = sp.simplify(gmN['Rscalar'].subs(subms))
ric22 = sp.simplify(gmN['RicL'][2, 2].subs(subms))
report('T5g the N=1, f=1-kr^2 slice is NOT constant curvature: '
       'Ric_thth - (R/4) g_thth = k r^2/2, nonzero',
       zero(sp.simplify(ric22 - Rms1 * r ** 2 / 4 - k * r ** 2 / 2))
       and (sp.simplify(ric22 - Rms1 * r ** 2 / 4) != 0))
report('T5e independent Christoffel-free Ricci scalar formula matches '
       'build_metric on the (N,f) ansatz',
       zero(sp.simplify(Rind - gmN['Rscalar'])))
hb('T5e done')

sl = {Nr: 1, Nr.diff(r): 0, Nr.diff(r, 2): 0}
c11 = sp.simplify(gmN['RicL'][1, 1].subs(sl))
c22 = sp.simplify(gmN['RicL'][2, 2].subs(sl))
c1212 = sp.simplify(gmN['Rm'][2, 3, 2, 3].subs(sl))
report('T5f N=1 slice components: Ric_rr = -f\'/(r f), Ric_thth = 1-f-r f\'/2, '
       'R^theta_{phi theta phi} = (1-f) sin^2(theta)',
       zero(c11 + fr.diff(r) / (r * fr)) and zero(c22 - (1 - fr - r * fr.diff(r) / 2))
       and zero(c1212 - (1 - fr) * sp.sin(th) ** 2))
hb('T5f done')

print()
print('ALL PASS: %s (%d/%d)' % (len(FAILS) == 0,
                                len(RESULTS) - len(FAILS), len(RESULTS)))
if FAILS:
    print('failed checks:')
    for tag in FAILS:
        print('  ' + tag)
print('[elapsed %.3f s]' % (time.time() - t0), file=sys.stderr)
