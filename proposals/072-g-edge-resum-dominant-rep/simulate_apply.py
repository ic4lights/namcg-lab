"""072-g-edge-resum-dominant-rep: predicted post-state simulation.

Reads chapters/appH-microscopic-proofs.tex and bib/namcg.bib (read-only),
applies the proposed insert and the bib append in memory, and prints the
predicted post-state byte count, sha256 and line-ending counts for both
files. Does NOT write to the manuscript or the bibliography.

Run:
  python -I proposals/072-g-edge-resum-dominant-rep/simulate_apply.py
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
BIBADD = os.path.join(HERE, 'bib_additions.bib')

crlf = b'\r\n'

data = open(APPH, 'rb').read()
print('appH pre  bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(data), hashlib.sha256(data).hexdigest(),
         data.count(crlf), data.count(b'\n') - data.count(crlf)))

bib = open(BIB, 'rb').read()
print('bib  pre  bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(bib), hashlib.sha256(bib).hexdigest(),
         bib.count(crlf), bib.count(b'\n') - bib.count(crlf)))

# --- anchor checks: short form is ambiguous (2 occurrences), long is unique ---
short = b'\\emph{Vacuum term.}'
long = (b'\\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023}')
assert data.count(short) == 2, ('short anchor count', data.count(short))
assert data.count(long) == 1, ('long anchor count', data.count(long))
anchor = crlf + long  # the paragraph starts a line: unique with the leading CRLF
assert data.count(anchor) == 1, ('line-start anchor count', data.count(anchor))

# --- insert validation (LF, ASCII, no process content, no refs/labels) ---
ins = open(INSERT, 'rb').read()
assert b'\r' not in ins and all(b < 128 for b in ins), 'insert not LF-ASCII'
assert not any(l != l.rstrip() for l in ins.split(b'\n')), 'trailing ws'
assert b'$' not in ins and b'\\label' not in ins, 'forbidden token'
assert ins.count(b'\\cite{Frenkel2023EdgeModes}') == 1
assert ins.count(b'\\cite{FlissFrenkelHartnollSoni2025}') == 1
assert ins.count(b'\\ref') == 0 and ins.count(b'\\eqref') == 0

ins_crlf = ins.replace(b'\n', crlf)
block = ins_crlf.rstrip(crlf) + crlf + crlf
out = data.replace(anchor, crlf + block + long, 1)
assert out.count(short) == 2 and out.count(long) == 1  # insert adds no new 'Vacuum term'
print('appH post bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(out), hashlib.sha256(out).hexdigest(),
         out.count(crlf), out.count(b'\n') - out.count(crlf)))

# --- bib append ---
assert bib.count(b'Frenkel2023EdgeModes') == 0, 'key already present'
assert bib.endswith(b'}\r\n'), 'bib does not end with }\r\n'
add = open(BIBADD, 'rb').read()
assert add.replace(b'\r\n', b'\n').count(b'\r') == 0, 'bibadd has bare CR'
add = add.replace(b'\r\n', b'\n').replace(b'\n', crlf)
assert all(b < 128 for b in add) and add.startswith(b'@misc{Frenkel2023EdgeModes')
out_bib = bib + add
print('bib  post bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(out_bib), hashlib.sha256(out_bib).hexdigest(),
         out_bib.count(crlf), out_bib.count(b'\n') - out_bib.count(crlf)))

i = out.find(block)
print('context around insertion:')
print(out[i - 300:i + 260].decode('ascii', 'backslashreplace'))
