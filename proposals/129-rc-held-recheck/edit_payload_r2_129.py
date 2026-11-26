# edit_payload_r2_129.py -- item 129 r2: applies the three gatekeeper-mandated exact string
# replacements (review-r1 findings 1-3) to payload-F.tex. Each old string must occur exactly
# once (assert); no other byte is touched; CRLF/ASCII/trailing-CRLF are re-checked after.
# Run:  python -I proposals/129-rc-held-recheck/edit_payload_r2_129.py
# Expected first run: prints EDIT129 APPLIED + new size/hashes. Re-run after application:
# prints EDIT129 ALREADY-APPLIED (idempotent guard; guards above fire on any partial state).
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, 'payload-F.tex')
d = open(P, 'rb').read()
n0 = len(d)

# (old, new) -- ASCII byte strings; backslashes literal (raw strings).
EDITS = [
    (rb'checked at \(N\le5\) with residual below \(10^{-13}\)',
     rb'checked at \(N\le5\) with residual below \(1.5\times10^{-13}\)'),          # finding 2
    (rb'supplied there as \(C_{ijk}=\mathrm i c_3\epsilon_{ijk}/g^2\)',
     rb'specialised there to \(C_{ijk}=\mathrm i c_3\epsilon_{ijk}/g^2\) on the flux directions'),  # finding 3
    (rb'\beta_K\simeq2\cdot5.345/10.68\simeq1.000',
     rb'\beta_K\simeq2\cdot5.34/10.68\simeq1.000'),                                 # finding 1
]

old_counts = [d.count(o) for o, _ in EDITS]
new_counts = [d.count(n) for _, n in EDITS]
if old_counts == [0, 0, 0] and new_counts == [1, 1, 1]:
    print('EDIT129 ALREADY-APPLIED size=%d sha256_12=%s sha1_12=%s' % (
        n0, hashlib.sha256(d).hexdigest()[:12], hashlib.sha1(d).hexdigest()[:12]))
    sys.exit(0)

assert old_counts == [1, 1, 1], 'old-string counts %r (partial application?)' % (old_counts,)
assert new_counts == [0, 0, 0], 'new-string counts %r (old not applied cleanly?)' % (new_counts,)

for o, n in EDITS:
    assert d.count(o) == 1
    d = d.replace(o, n, 1)

# post-checks: untouched bytes are pure CRLF + ASCII + trailing CRLF
assert b'\n' not in d.replace(b'\r\n', b''), 'bare LF introduced'
assert all(b < 128 for b in d), 'non-ASCII byte'
assert d.endswith(b'\r\n'), 'trailing CRLF lost'
assert d.count(b'\r\n') == 3, 'line structure changed: %d CRLF' % d.count(b'\r\n')

open(P, 'wb').write(d)
print('EDIT129 APPLIED: 3 replacements, size %d -> %d B (delta %+d B)' % (n0, len(d), len(d) - n0))
print('EDIT129 sha256_12=%s sha1_12=%s' % (
    hashlib.sha256(d).hexdigest()[:12], hashlib.sha1(d).hexdigest()[:12]))
