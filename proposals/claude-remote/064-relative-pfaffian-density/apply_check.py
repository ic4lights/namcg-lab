"""
064 apply check (report mode). Reads the working appH and bib, verifies the baselines, locates the unique
two-line Problem E anchor, inserts appH_insert.tex (converted to CRLF) before it, and reports the resulting
size, sha256 and line-ending counts. Writes the would-be result only to the directory given as argv[1]
(outside the repository); never writes into the repository.
"""
import hashlib, os, re, sys

BS = chr(92)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
APPH = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
BIB = os.path.join(ROOT, 'bib', 'namcg.bib')
INS = os.path.join(os.path.dirname(__file__), 'appH_insert.tex')
outdir = sys.argv[1] if len(sys.argv) > 1 else None

def sha(b): return hashlib.sha256(b).hexdigest()
out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

a = open(APPH, 'rb').read(); b = open(BIB, 'rb').read()
log('appH baseline:', len(a), sha(a)); log('bib baseline:', len(b), sha(b))
assert len(a) == 606731 and sha(a) == '4808ae9ca68ac249a2f01d4e02261da98cabf32b913713f82a0429b0f4c230cf'
assert len(b) == 29360 and sha(b).startswith('1d280848')
assert a.count(b'\r\n') == a.count(b'\n')

anchor = (BS + 'paragraph{Status.}\r\nRemains Assumption~' + BS + 'ref{ass:lorentzian}.').encode()
n_anchor = a.count(anchor)
log('anchor occurrences:', n_anchor, '; plain Status paragraphs:', a.count((BS + 'paragraph{Status.}').encode()))
assert n_anchor == 1
pos = a.index(anchor)
assert a[pos - 4:pos] == b'\r\n\r\n'
log('anchor line:', a[:pos].count(b'\n') + 1, '(preceded by a blank line)')

ins = open(INS, 'rb').read()
assert b'\r' not in ins and ins.endswith(b'\n')
ins_txt = ins.decode('ascii')
ins_crlf = ins.replace(b'\n', b'\r\n') + b'\r\n'      # insert followed by a blank line
log('insert (LF source):', len(ins), sha(ins), '; as CRLF block:', len(ins_crlf), sha(ins_crlf))
new = a[:pos] + ins_crlf + a[pos:]
log('result appH:', len(new), sha(new), '; CRLF', new.count(b'\r\n'), '; bare LF', new.count(b'\n') - new.count(b'\r\n'))

# labels, refs, cites
refs = set(re.findall(r'\\ref\{([^}]*)\}', ins_txt))
labels_new = re.findall(r'\\label\{([^}]*)\}', ins_txt)
cites = set(k.strip() for grp in re.findall(r'\\cite\{([^}]*)\}', ins_txt) for k in grp.split(','))
chap = os.path.join(ROOT, 'chapters')
alltex = ''.join(open(os.path.join(chap, f), encoding='utf-8').read() for f in os.listdir(chap) if f.endswith('.tex'))
for r in sorted(refs):
    c = alltex.count(BS + 'label{' + r + '}')
    log(f'ref {r}: label occurrences {c}'); assert c == 1
log('new labels:', labels_new); assert not labels_new
bibtxt = b.decode('utf-8')
for k in sorted(cites):
    c = len(re.findall(r'@\w+\{' + re.escape(k) + ',', bibtxt))
    log(f'cite {k}: bib entries {c}'); assert c == 1
log('bib unchanged (no new entries)')
for bad in ('researcher', 'proposal', 'as proposed', 'gatekeeper'):
    assert bad not in ins_txt.lower()
log('no process language found')
if outdir:
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, 'appH-microscopic-proofs.tex'), 'wb').write(new)
    log('would-be appH written to', outdir)
open(os.path.join(os.path.dirname(__file__), 'apply_check.txt'), 'w').write('\n'.join(out) + '\n')
