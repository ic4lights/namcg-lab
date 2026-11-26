# -*- coding: ascii -*-
# Round-2 check: the r2 payload equals the r1 payload with EXACTLY the three
# gatekeeper-specified substring replacements applied, each exactly once, and
# nothing else changed. Primary invariant: after the three replacements the
# result is byte-identical to payload-124.txt ("BYTE-EXACT-OK", rc 0).
# Secondary view: difflib opcodes merged across small equal gaps cluster into
# exactly 3 edit regions ("CLUSTERS: 3").
import os, difflib

F = os.path.dirname(os.path.abspath(__file__))
old = open(os.path.join(F, 'payload-124.txt.r1-bytes'), 'rb').read()
new = open(os.path.join(F, 'payload-124.txt'), 'rb').read()
B = lambda t: t.encode('ascii')

edits = [
    ('f1 kinetic sign (finding 1, MAJOR)',
     B(r'\(\sum_{\mu,\nu}\eta^{\mu\nu}(-\operatorname{Tr}P^\mu P^\nu)\), which evaluates to'),
     B(r'\(\sum_{\mu,\nu}\eta^{\mu\nu}\operatorname{Tr}(P^\mu P^\nu)\), which evaluates to')),
    ('f2 gYM prefactor (finding 2, minor)',
     B(r'while its quartic form equals \(\tfrac14\sum_{i,j}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\) with'),
     B(r'while its quartic form equals \(g_{\mathrm{YM}}^{-2}\bigl(\tfrac14\sum_{i,j}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\bigr)\) with')),
    ('f3 closer (finding 3, minor)',
     B(r'they change no status label, and Problems~F and~N remain open.'),
     B(r'they change no status label, and they close nothing in Problem~N.')),
]

s = old
for name, o, n in edits:
    c = s.count(o)
    print('%s: old-marker count %d (expect 1)' % (name, c))
    assert c == 1, name
    s = s.replace(o, n, 1)
    print('   -> replaced; marker now count %d in new (expect 1)' % new.count(n))
print('old size %d  new size %d  delta %+d' % (len(old), len(new), len(new) - len(old)))
print('BYTE-EXACT-%s' % ('OK' if s == new else 'FAIL'))

# secondary view: merge difflib opcodes whose separating equal run is short
ops = [op for op in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes() if op[0] != 'equal']
clusters = []
for t, i1, i2, j1, j2 in ops:
    if clusters and (i1 - clusters[-1][1]) < 128 and (j1 - clusters[-1][3]) < 128:
        clusters[-1][1] = i2; clusters[-1][3] = j2
    else:
        clusters.append([i1, i2, j1, j2])
for n, (i1, i2, j1, j2) in enumerate(clusters, 1):
    print('cluster %d: old[%d:%d] -> new[%d:%d]  new-text: %s' % (n, i1, i2, j1, j2, new[j1:j2].decode('ascii')))
print('CLUSTERS: %d' % len(clusters))

ok = (s == new) and len(clusters) == 3
print('EXACTLY-THREE %s' % ('OK' if ok else 'FAIL'))
raise SystemExit(0 if ok else 1)
