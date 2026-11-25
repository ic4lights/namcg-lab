# -*- coding: ascii -*-
# Round-2 patch of make_payload_124.py PAY_TEXT: gatekeeper findings 1-3.
# Operates on the doubled-backslash source text (the .py source stores the
# payload string literal with doubled backslashes). Each replacement must
# match exactly once or the script aborts.
import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_payload_124.py')
s = open(p, encoding='ascii').read()

B = chr(92)  # backslash
def src(t):  # convert a plain LaTeX fragment to its doubled-backslash source form
    return t.replace(B, B + B)

f1o = src(r'has Hamiltonian kinetic polynomial \(\sum_{\mu,\nu}\eta^{\mu\nu}(-\operatorname{Tr}P^\mu P^\nu)\), which evaluates to')
f1n = src(r'has Hamiltonian kinetic polynomial \(\sum_{\mu,\nu}\eta^{\mu\nu}\operatorname{Tr}(P^\mu P^\nu)\), which evaluates to')
f2o = src(r'while its quartic form equals \(\tfrac14\sum_{i,j}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\) with')
f2n = src(r'while its quartic form equals \(g_{\mathrm{YM}}^{-2}\bigl(\tfrac14\sum_{i,j}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\bigr) with')
f3o = r'they change no status label, and Problems~F and~N remain open.'
f3n = r'they change no status label, and they close nothing in Problem~N.'

for o, n, name in ((f1o, f1n, 'f1-kinetic-sign'), (f2o, f2n, 'f2-gYM-prefactor'), (f3o, f3n, 'f3-closer')):
    c = s.count(o)
    assert c == 1, 'finding %s: expected exactly 1 occurrence, found %d' % (name, c)
    s = s.replace(o, n, 1)
    print('%s: replaced (count was 1)' % name)

open(p, 'w', encoding='ascii', newline='').write(s)
print('make_payload_124.py written')
