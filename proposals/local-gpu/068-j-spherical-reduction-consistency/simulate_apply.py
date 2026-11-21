"""068-j-spherical-reduction-consistency: predicted post-state simulation.

Reads chapters/appH-microscopic-proofs.tex (read-only), applies the
four edits proposed in proposal-r1.md in memory, and prints the
predicted post-state byte count, sha256 and line-ending counts. Does
NOT write to the manuscript.

Run:
  python -I proposals/068-j-spherical-reduction-consistency/simulate_apply.py
"""
import hashlib
import os
import sys

sys.stdout.reconfigure(encoding='ascii', errors='backslashreplace')
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
APPH = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
INSERT = os.path.join(os.path.dirname(__file__), 'insert-r1.tex')

data = open(APPH, 'rb').read()
print('pre  bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(data), hashlib.sha256(data).hexdigest(),
         data.count(b'\r\n'), data.count(b'\n') - data.count(b'\r\n')))

crlf = b'\r\n'

# E1: one-sentence replacement of the stale 'checked symbolically' claim
a1 = ('specified \\(\\mathcal P\\), these reduced equations have been '
      'checked').encode('ascii') + crlf + b'symbolically:'
r1 = ('specified \\(\\mathcal P\\), the displayed reduced '
      'one-dimensional').encode('ascii') + crlf + b'system is:'
assert data.count(a1) == 1, ('E1 anchor count', data.count(a1))
out = data.replace(a1, r1)

# E1b: condition the 'consistent vacuum branch' consequence
a2 = ('Thus \\(N=1\\) is a consistent vacuum branch of the reduced '
      'equations,').encode('ascii') + crlf + ('and, with '
      '\\(\\alpha=-\\kappa\\), the lapse equation has first integral').encode('ascii')
r2 = ('Conditional on the displayed identities, \\(N=1\\) is a branch of '
      'that one-dimensional system and, with '
      '\\(\\alpha=-\\kappa\\), the lapse equation has first integral').encode('ascii')
assert out.count(a2) == 1, ('E1b anchor count', out.count(a2))
out = out.replace(a2, r2)

# E2: insert the audit paragraph before the MS branch paragraph
anchor = b'\\paragraph{Maximally symmetric branch.}'
assert out.count(anchor) == 1, ('E2 anchor count', out.count(anchor))
ins = open(INSERT, 'rb').read()
assert b'\r' not in ins and all(b < 128 for b in ins), 'insert not LF-ASCII'
assert not any(l != l.rstrip() for l in ins.split(b'\n')), 'trailing ws'
assert b'$' not in ins and b'\\label' not in ins
ins_crlf = ins.replace(b'\n', crlf)
block = ins_crlf.rstrip(crlf) + crlf + crlf
out = out.replace(anchor, block + anchor, 1)

# E3: condition the Status paragraph's 'have been checked' sentence
a3 = ('Conditional on the stated symmetric reduction, the reduced-action\r\n'
      'identities, first integral, regular-centre constraint, maximally\r\n'
      'symmetric curvature relation, and asymptotic tail above have been\r\n'
      'checked for the specified \\(\\mathcal P\\).').encode('ascii')
r3 = ('Conditional on the stated symmetric reduction, the first-integral\r\n'
      'arithmetic, regular-centre constraint, maximally symmetric curvature\r\n'
      'relation, and asymptotic tail above are internally consistent for the\r\n'
      'displayed one-dimensional system, and a symbolic re-evaluation of the\r\n'
      'reduced-action identities for \\(\\mathcal P\\) as written '
      'in~\\eqref{eq:ECG} does not reproduce them.').encode('ascii')
assert out.count(a3) == 1, ('E3 anchor count', out.count(a3))
out = out.replace(a3, r3)

print('post bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(out), hashlib.sha256(out).hexdigest(),
         out.count(b'\r\n'), out.count(b'\n') - out.count(b'\r\n')))
i = out.find(anchor)
print('context around insertion:')
print(out[i - 400:i + 60].decode('ascii', 'backslashreplace'))
ch09 = open(os.path.join(ROOT, 'chapters', 'ch09-ultraviolet.tex'),
            'rb').read()
for key in (b'\\label{eq:ECG}', b'\\label{eq:S-ECG}'):
    print('label exists once in ch09:', key.decode(), ch09.count(key) == 1)
print('eqref count in insert:', ins.count(b'\\eqref'))
