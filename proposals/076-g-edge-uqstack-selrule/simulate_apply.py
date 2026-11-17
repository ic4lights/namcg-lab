"""076-g-edge-uqstack-selrule: predicted post-state simulation (read-only).

Reads chapters/appH-microscopic-proofs.tex and bib/namcg.bib in binary,
applies the proposed insert in memory (no bibliography change is proposed),
and prints the predicted post-state byte counts, sha256 and line-ending
counts for both files. Does NOT write to the manuscript or the bibliography.

Run:
  python -I proposals/076-g-edge-uqstack-selrule/simulate_apply.py
"""
import hashlib
import os
import sys

sys.stdout.reconfigure(encoding='ascii', errors='backslashreplace')
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
APPH = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
BIB = os.path.join(ROOT, 'bib', 'namcg.bib')
HERE = os.path.dirname(__file__)
INSERT = os.path.join(HERE, 'insert-r1.tex')

crlf = b'\r\n'

data = open(APPH, 'rb').read()
print('appH pre  bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(data), hashlib.sha256(data).hexdigest(),
         data.count(crlf), data.count(b'\n') - data.count(crlf)))
assert len(data) == 704082
assert hashlib.sha256(data).hexdigest() == (
    '58eb0c7fa4a360d4c9f2fc400c5112555d8b7480fe0873ae9b35a07f57c6e5e0')
assert data.count(crlf) == 3816 and data.count(b'\n') - data.count(crlf) == 0

bib = open(BIB, 'rb').read()
print('bib  pre  bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(bib), hashlib.sha256(bib).hexdigest(),
         bib.count(crlf), bib.count(b'\n') - bib.count(crlf)))
assert len(bib) == 37463
assert hashlib.sha256(bib).hexdigest() == (
    '4d6d7b2a668fdaa64663e624b3f296d833c3bbcaa06a74ec5012a7f494ce0de6')
assert bib.count(crlf) == 1239 and bib.count(b'\n') - bib.count(crlf) == 0

# --- the 075 insert must already be integrated in the live tree ---
hdr075 = b'\\emph{Frame average of the fixed-frame excess at the saddle.}'
assert data.count(hdr075) == 1, ('075 header count', data.count(hdr075))

# --- anchor checks: short form is ambiguous (2 occurrences: the fibre-point
# paragraph and the Steinacker2023 paragraph), the long form is unique ---
short = b'\\emph{Vacuum term.}'
long = (b'\\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023}')
assert data.count(short) == 2, ('short anchor count', data.count(short))
assert data.count(long) == 1, ('long anchor count', data.count(long))
anchor = crlf + long  # the paragraph starts a line: unique with the leading CRLF
assert data.count(anchor) == 1, ('line-start anchor count', data.count(anchor))

# --- insert validation: CRLF, ASCII, no process content, no refs/labels/cites ---
ins = open(INSERT, 'rb').read()
assert ins.count(b'\n') == ins.count(crlf), 'insert has bare LF'
assert all(b < 128 for b in ins), 'insert not ASCII'
assert not any(l != l.rstrip(b' \t') for l in ins.split(crlf)[:-1]), 'trailing ws'
assert b'$' not in ins and b'\\label' not in ins, 'forbidden token'
assert ins.count(b'\\ref') == 0 and ins.count(b'\\eqref') == 0, 'ref in insert'
assert ins.count(b'\\cite') == 0, 'no citation is load-bearing in this insert'
assert ins.count(b'[') == 0 and ins.count(b']') == 0, 'square bracket in insert'
low = ins.lower()
for tok in (b'status', b'priority', b'completion', b'open', b'derived',
            b'programme', b'critical'):
    assert tok not in low, ('forbidden word in insert', tok)
assert ins.count(b'\\emph{Vacuum term.') == 0
hdr = b'\\emph{Selection-rule consistency of stacked diagrams at coincident caps.}'
assert ins.count(hdr) == 1 and data.count(hdr) == 0

block = ins.rstrip(crlf) + crlf + crlf
out = data.replace(anchor, crlf + block + long, 1)
assert out.count(short) == 2 and out.count(long) == 1  # insert adds no new 'Vacuum term'
assert out.count(hdr) == 1
print('appH post bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(out), hashlib.sha256(out).hexdigest(),
         out.count(crlf), out.count(b'\n') - out.count(crlf)))
print('delta appH: bytes %+d CRLF %+d bareLF %+d'
      % (len(out) - len(data), out.count(crlf) - data.count(crlf),
         (out.count(b'\n') - out.count(crlf)) - (data.count(b'\n') - data.count(crlf))))

# --- bibliography: no change proposed; it stays byte-identical ---
out_bib = bib
print('bib  post bytes %d sha256 %s CRLF %d bareLF %d  (unchanged: no bib addition proposed)'
      % (len(out_bib), hashlib.sha256(out_bib).hexdigest(),
         out_bib.count(crlf), out_bib.count(b'\n') - out_bib.count(crlf)))

i = out.find(block)
print('context around insertion:')
print(out[i - 300:i + 300].decode('ascii', 'backslashreplace'))
