"""
067 apply check, round 2 (report mode; inserts appH_insert_r2.tex). Reads the working appH and bib, verifies the appH baseline, locates the unique
multi-line anchor at the end of the Problem G section (closing sentence of the 065 paragraph followed by the Problem H
section header), inserts appH_insert.tex (converted to CRLF) between them, and reports sizes, sha256 values, line
endings, labels, refs and cites. No bib change. Reports go to stdout only. If a directory is given as argv[1] (it must
lie outside the repository), the would-be appH is written there; nothing is ever written into the repository.
"""
import hashlib, os, re, sys

BS = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
APPH = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
BIB = os.path.join(ROOT, 'bib', 'namcg.bib')
INS = os.path.join(HERE, "appH_insert_r2.tex")
outdir = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
if outdir:
    assert not (outdir + os.sep).lower().startswith((ROOT + os.sep).lower()), 'output directory must be outside the repository'

def sha(b): return hashlib.sha256(b).hexdigest()

a = open(APPH, 'rb').read(); b = open(BIB, 'rb').read()
print('appH baseline:', len(a), sha(a))
assert len(a) == 624232 and sha(a) == 'c2dac013f275fed851d53e8086bc3eceef717c5b607b10c09ae7541c43558b5c'
assert a.count(b'\r\n') == a.count(b'\n')

tail = ('Assumptions~' + BS + 'ref{ass:Sent-density} and~' + BS + 'ref{ass:bdy-EE} are not discharged, and Problem~G remains open and PROGRAMME-CONDITIONAL.\r\n')
anchor = (tail + '\r\n' + BS + 'section{Problem H: modular origin of the interpolating function}').encode()
n_anchor = a.count(anchor)
print('anchor occurrences:', n_anchor)
assert n_anchor == 1
pos = a.index(anchor); cut = pos + len(tail.encode())
print('anchor line', a[:pos].count(b'\n') + 1, '; insertion after line', a[:cut].count(b'\n'))
g = a.index((BS + 'section{Problem G: HBEV}').encode())
assert g < pos and a[g:pos].count((BS + 'section{').encode()) == 1, 'anchor not inside the Problem G section'

ins = open(INS, 'rb').read()
assert b'\r' not in ins and ins.endswith(b'\n') and not ins.startswith(b'\xef\xbb\xbf')
ins_txt = ins.decode('ascii')
block = b'\r\n' + ins.replace(b'\n', b'\r\n')          # blank line, insert; the existing blank line follows
print('insert (LF source):', len(ins), sha(ins), '; CRLF block:', len(block), sha(block))
new = a[:cut] + block + a[cut:]
print('result appH:', len(new), sha(new), '; CRLF', new.count(b'\r\n'), '; bare LF', new.count(b'\n') - new.count(b'\r\n'))
assert new.count(b'\n') == new.count(b'\r\n')

refs = set(re.findall(r'\\ref\{([^}]*)\}', ins_txt)) | set(re.findall(r'\\eqref\{([^}]*)\}', ins_txt))
labels_new = re.findall(r'\\label\{([^}]*)\}', ins_txt)
cites = set(k.strip() for grp in re.findall(r'\\cite\{([^}]*)\}', ins_txt) for k in grp.split(','))
chap = os.path.join(ROOT, 'chapters')
alltex = ''.join(open(os.path.join(chap, f), encoding='utf-8').read() for f in os.listdir(chap) if f.endswith('.tex'))
for r in sorted(refs):
    c = alltex.count(BS + 'label{' + r + '}')
    print(f'ref {r}: label occurrences {c}'); assert c == 1
print('new labels:', labels_new); assert not labels_new
bibtxt = b.decode('utf-8')
for k in sorted(cites):
    c = len(re.findall(r'@\w+\{' + re.escape(k) + ',', bibtxt))
    print(f'cite {k}: entries in bib {c}'); assert c == 1
assert ins_txt.count(BS + '(') == ins_txt.count(BS + ')') and ins_txt.count(BS + '[') == ins_txt.count(BS + ']')
assert ins_txt.count('{') == ins_txt.count('}')
print('math delimiters and braces balanced:', ins_txt.count(BS + '('), 'inline,', ins_txt.count(BS + '['), 'display')
for bad in ('researcher', 'proposal', 'as proposed', 'gatekeeper', 'package'):
    assert bad not in ins_txt.lower(), bad
print('no process language found')
print('status sentences (PROGRAMME-CONDITIONAL) in insert:', ins_txt.count('PROGRAMME-CONDITIONAL'))
assert ins_txt.count('PROGRAMME-CONDITIONAL') == 1
if outdir:
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, 'appH-microscopic-proofs.tex'), 'wb').write(new)
    print('would-be appH written to', outdir)
print('APPLY CHECK PASS')
