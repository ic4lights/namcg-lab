"""068 round 3: independent byte-count check of the four appH anchors.

Re-confirms anchor uniqueness in the CURRENT working-tree
chapters/appH-microscopic-proofs.tex without applying any edit
(read-only). Anchors are embedded as bytes exactly as in
simulate_apply.py L28-31, L36-38, L46, L57-60. Prints the pre-state
bytes/sha/line-ending counts, then each anchor's count and the 1-based
start line of the anchor text.

Run:
  python -I proposals/068-j-spherical-reduction-consistency/check_anchors_r3.py
"""
import hashlib
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
APPH = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
CRLF = b'\r\n'

data = open(APPH, 'rb').read()
print('pre bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(data), hashlib.sha256(data).hexdigest(),
         data.count(CRLF), data.count(b'\n') - data.count(CRLF)))

a1 = (b'specified \\(\\mathcal P\\), these reduced equations have been '
      b'checked') + CRLF + b'symbolically:'
a2 = (b'Thus \\(N=1\\) is a consistent vacuum branch of the reduced '
      b'equations,') + CRLF + (b'and, with '
      b'\\(\\alpha=-\\kappa\\), the lapse equation has first integral')
a2b = b'\\paragraph{Maximally symmetric branch.}'
a3 = (b'Conditional on the stated symmetric reduction, the reduced-action'
      + CRLF +
      b'identities, first integral, regular-centre constraint, maximally'
      + CRLF +
      b'symmetric curvature relation, and asymptotic tail above have been'
      + CRLF +
      b'checked for the specified \\(\\mathcal P\\).')

for name, a in (('E1', a1), ('E1b', a2), ('E2', a2b), ('E3', a3)):
    c = data.count(a)
    i = data.find(a)
    line = data[:i].count(b'\n') + 1 if i >= 0 else -1
    print(name, 'count', c, 'start line', line)
