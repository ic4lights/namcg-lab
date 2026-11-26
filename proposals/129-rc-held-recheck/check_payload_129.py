# check_payload_129.py -- item 129 r2 payload hygiene + splice-accounting check,
# with an in-memory positive control (item-117 lesson: every guard must be shown to fire).
# Run:  python -I proposals/129-rc-held-recheck/check_payload_129.py
# Expected invariant output: last line  CHK129 PASS  (real payload clean; 4/4 doctored
# controls each caught by the expected guard).
import os, sys

REPO = r'C:\Users\redgi\Projects\namcg-lab@gpu'
P = os.path.join(REPO, 'proposals', '129-rc-held-recheck', 'payload-F.tex')
APP = os.path.join(REPO, 'chapters', 'appH-microscopic-proofs.tex')

OLD = [rb'checked at \(N\le5\) with residual below \(10^{-13}\)',
       rb'supplied there as',
       rb'5.345']
NEW = [rb'checked at \(N\le5\) with residual below \(1.5\times10^{-13}\)',
       rb'specialised there to \(C_{ijk}=\mathrm i c_3\epsilon_{ijk}/g^2\) on the flux directions',
       rb'\beta_K\simeq2\cdot5.34/10.68\simeq1.000']

def check_bytes(d):
    """Return list of violated guard names for payload bytes d."""
    v = []
    if any(b >= 128 for b in d):
        v.append('ascii')
    if b'\n' in d.replace(b'\r\n', b''):
        v.append('bare-lf')
    if not d.endswith(b'\r\n'):
        v.append('trailing-crlf')
    for s in OLD:
        if s in d:
            v.append('old-string:' + s.decode('ascii', 'replace')[:24])
    for s in NEW:
        if d.count(s) != 1:
            v.append('new-count:' + s.decode('ascii', 'replace')[:24])
    if d.count(rb'\eqref{eq:Smatrix}') != 1:
        v.append('eqref-count')
    for tok in (rb'\cite', rb'\ref{', rb'\label{'):
        if tok in d:
            v.append('forbidden:' + tok.decode())
    return v

d = open(P, 'rb').read()
viol = check_bytes(d)
print('payload size %d B, CRLF %d, ASCII %s, ends-CRLF %s' % (
    len(d), d.count(b'\r\n'), all(b < 128 for b in d), d.endswith(b'\r\n')))

# splice accounting against the live appH
a = open(APP, 'rb').read()
anchor = b'On this evidence the sign of \\(\\hat U\\) depends on \\(K\\).\r\n\r\n'
scale = b'\\emph{Scale dependence.}'
assert a.count(anchor) == 1, 'anchor+blank count %d' % a.count(anchor)
assert a.count(scale) == 1, 'scale count %d' % a.count(scale)
assert len(a) == 883075, 'live appH size %d != 883075 pin' % len(a)
post = len(a) + len(d) + 2
print('splice: appH %d B + payload %d B + 2 B join => expected POST %d B' % (len(a), len(d), post))

if viol:
    print('CHK129 FAIL violations=%r' % (viol,))
    sys.exit(1)

# positive controls: doctored copies must each trip the expected guard (in memory only)
controls = [
    ('bare-lf', d.replace(b'tree cubic term.}', b'tree cubic term.\n}', 1)),
    ('old-string:5.345', d.replace(rb'5.34/10.68', rb'5.345/10.68', 1)),
    ('ascii', d[:-2] + b'\xe9\r\n'),
    ('trailing-crlf', d[:-2]),
]
fired = 0
for name, bad in controls:
    v = check_bytes(bad)
    ok = name in v
    print('control %-22s caught=%s (%r)' % (name, ok, v[:2]))
    fired += ok
assert fired == len(controls), 'positive controls fired %d/%d' % (fired, len(controls))
print('CHK129 PASS')
