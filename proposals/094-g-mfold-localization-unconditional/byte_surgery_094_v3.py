# 094 byte surgery v3 (v2 assert referenced stale filename; derivations now swap insert-r1f->insert-r1f2) v2 (v1 NEW contained a banned literal '['; fixed to (0,eps)^s, same integral): correct one false pointwise clause in insert-r1.tex -> NEW file insert-r1f.tex,
# and derive hygiene_094_v2.py / simulate_apply_094_v3.py pointing at the new insert.
# Reason (round-1 researcher review of own survivor insert): the old clause asserted the product of
# the vanishing pair factors is comparable, up to two positive constants, to rho^binom(s+1,2)
# POINTWISE on the face patch; false already for s=2 (y1*y2/(y1+y2)^2 -> 0 as y2/y1 -> 0).
# Replacement states the true two-sided bookkeeping: exact model-integral equivalence (bounded
# nonvanishing factors), Tonelli polar split, radial criterion, angular finiteness by induction
# over vanishing runs (l <= s-1 gives the weaker 1-beta < 2/(l+1)). insert-r1.tex is left untouched.
import hashlib
d = 'proposals/094-g-mfold-localization-unconditional/'
ins = open(d + 'insert-r1.tex', 'rb').read()
OLD = rb''' and they are comparable, up to two positive constants, to \((\sum_{k}y_{k})^{\binom{s+1}{2}}\) in the vanishing gaps, while every remaining pair factor and the Dirichlet factor \(\prod_{i}p_{i}^{a-1}\) is bounded above and below by positive constants, so transverse polar coordinates in the vanishing gaps reduce integrability on that face patch to \(\int_{0}\varrho^{\,s-1-(1-\beta)\binom{s+1}{2}}\,d\varrho\), which converges exactly for \(1-\beta<2/(s+1)\), and Fubini over the finitely many face patches gives the rest;'''
NEW = rb''' and each vanishing factor is a sum of consecutive vanishing gaps, while every remaining pair factor and the Dirichlet factor \(\prod_{i}p_{i}^{a-1}\) is bounded above and below by positive constants on the patch, so integrability on that face patch is equivalent to finiteness of the model integral \(\int_{(0,\varepsilon)^{s}}\prod_{1\le i\le j\le s}(y_{i}+\cdots+y_{j})^{-(1-\beta)}\,dy\) over the consecutive partial sums of the vanishing gaps; by Tonelli's theorem in polar coordinates that model integral is the product of the radial factor \(\int_{0}\varrho^{\,s-1-(1-\beta)\binom{s+1}{2}}\,d\varrho\), finite exactly for \(1-\beta<2/(s+1)\), and an angular factor over the gap simplex, which is positive and finite whenever \(1-\beta<2/(s+1)\), by induction over the vanishing runs of the simplex boundary, a run of \(l\le s-1\) vanishing gaps imposing only the weaker condition \(1-\beta<2/(l+1)\); Fubini over the finitely many face patches then gives the rest;'''
assert ins.count(OLD) == 1, 'OLD span not unique'
new = ins.replace(OLD, NEW)
assert new.endswith(b'close nothing in Problem~G.\r\n') and new.count(b'\r\n') == 1
assert all(0x20 <= c <= 0x7e for c in new[:-2])
open(d + 'insert-r1f2.tex', 'wb').write(new)
for src, dst in (('hygiene_094_v2.py', 'hygiene_094_v3.py'), ('simulate_apply_094_v3.py', 'simulate_apply_094_v4.py')):
    s = open(d + src, 'rb').read()
    assert s.count(b'insert-r1f.tex') >= 1
    open(d + dst, 'wb').write(s.replace(b'insert-r1.tex', b'insert-r1f2.tex'))
    print(dst, 'written')
print('insert-r1f bytes', len(new), 'sha256', hashlib.sha256(new).hexdigest())
