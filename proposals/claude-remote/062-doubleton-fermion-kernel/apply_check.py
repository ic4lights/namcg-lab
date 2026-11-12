"""
062 apply_check: report mode by default (writes nothing in the repository).
  python apply_check.py                -> verify baselines, anchor, and print the result hashes
  python apply_check.py --out DIR      -> also write the patched appH and bib into DIR (outside the repository)
Insert: appH_insert.tex (LF in the proposal), converted to CRLF, placed immediately before the unique anchor
  "\paragraph{Status.}" CRLF "Remains Assumption~\ref{ass:lorentzian}."  of Problem E, followed by one blank line.
Bib: bib_entries.bib converted to CRLF, appended after a CRLF blank line.
Backslashes are built with chr(92).
"""
import hashlib, os, sys
BS = chr(92)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
APPH = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
BIB = os.path.join(ROOT, 'bib', 'namcg.bib')
BASE_APPH = (599923, '82ab236415a5fbbea02be7ceb6eebc791e560eef4a7e589cb25be2cf9ffa279c')
BASE_BIB = (28049, '582f09d5a0bca24e930a8e7c130907f495e738f6d14d89809aac6f7f7e7e1f22')

def sha(b): return hashlib.sha256(b).hexdigest()
def crlf(b):
    b = b.replace(b'\r\n', b'\n')
    return b.replace(b'\n', b'\r\n')

a = open(APPH, 'rb').read()
bb = open(BIB, 'rb').read()
print('appH baseline:', len(a), sha(a), 'match' if (len(a), sha(a)) == BASE_APPH else 'MISMATCH')
print('   CRLF', a.count(b'\r\n'), 'bare LF', a.count(b'\n') - a.count(b'\r\n'))
print('bib baseline:', len(bb), sha(bb), 'match' if (len(bb), sha(bb)) == BASE_BIB else 'MISMATCH')
print('   CRLF', bb.count(b'\r\n'), 'bare LF', bb.count(b'\n') - bb.count(b'\r\n'), 'ends with CRLF:', bb.endswith(b'\r\n'))

anchor = (BS + 'paragraph{Status.}\r\nRemains Assumption~' + BS + 'ref{ass:lorentzian}.').encode('ascii')
n = a.count(anchor); pos = a.find(anchor)
print('anchor count', n, 'line', a[:pos].count(b'\n') + 1)
assert n == 1

ins_lf = open(os.path.join(HERE, 'appH_insert.tex'), 'rb').read()
assert b'\r' not in ins_lf and b'\t' not in ins_lf and all(c < 128 for c in ins_lf)
ins = crlf(ins_lf)
if not ins.endswith(b'\r\n'):
    ins += b'\r\n'
print('insert: LF', len(ins_lf), sha(ins_lf), '; CRLF', len(ins), sha(ins))
new_a = a[:pos] + ins + b'\r\n' + a[pos:]
print('result appH:', len(new_a), sha(new_a), 'CRLF', new_a.count(b'\r\n'), 'bare LF', new_a.count(b'\n') - new_a.count(b'\r\n'))
print('   preceding bytes before insert end with blank line:', a[pos-4:pos] == b'\r\n\r\n')

bib_lf = open(os.path.join(HERE, 'bib_entries.bib'), 'rb').read()
bib_ins = crlf(bib_lf)
if not bib_ins.endswith(b'\r\n'):
    bib_ins += b'\r\n'
new_b = bb + b'\r\n' + bib_ins
print('bib entries:', len(bib_ins), sha(bib_ins))
print('result bib:', len(new_b), sha(new_b), 'CRLF', new_b.count(b'\r\n'), 'bare LF', new_b.count(b'\n') - new_b.count(b'\r\n'))

# label / cite checks
import re
txt = ins_lf.decode('ascii')
refs = set(re.findall(BS*2 + r'(?:ref|eqref)\{([^}]*)\}', txt))
labs_all = []
for fn in os.listdir(os.path.join(ROOT, 'chapters')):
    if fn.endswith('.tex'):
        labs_all += re.findall(BS*2 + r'label\{([^}]*)\}', open(os.path.join(ROOT, 'chapters', fn), encoding='utf-8').read())
for r in sorted(refs):
    print('  ref', r, 'labels found:', labs_all.count(r))
print('  new labels in insert:', re.findall(BS*2 + r'label\{([^}]*)\}', txt))
cites = set()
for grp in re.findall(BS*2 + r'cite\{([^}]*)\}', txt):
    cites.update(k.strip() for k in grp.split(','))
bibkeys = re.findall(r'@\w+\{([^,]+),', new_b.decode('utf-8'))
for c in sorted(cites):
    print('  cite', c, 'in bib (after append):', bibkeys.count(c))
dups = sorted(set(k for k in bibkeys if bibkeys.count(k) > 1))
print('  duplicate bib keys after append:', dups)

if '--out' in sys.argv:
    out = sys.argv[sys.argv.index('--out') + 1]
    assert not os.path.abspath(out).startswith(ROOT), 'refusing to write inside the repository'
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'appH-microscopic-proofs.tex'), 'wb').write(new_a)
    open(os.path.join(out, 'namcg.bib'), 'wb').write(new_b)
    print('wrote patched copies to', out)
