"""
065 apply check (report mode). Reads the working appH and bib, verifies the baselines, locates the unique multi-line
anchor at the end of the Problem G section, inserts appH_insert.tex (converted to CRLF) after the Status paragraph
and before the Problem H section, appends bib_entry.bib (CRLF) to the bib, and reports sizes, sha256 values, line
endings, labels, refs and cites. Reports go to stdout only. If a directory is given as argv[1] (it must lie outside
the repository), the would-be appH and bib are written there; nothing is ever written into the repository.
"""
import hashlib, os, re, sys

BS = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
APPH = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
BIB = os.path.join(ROOT, 'bib', 'namcg.bib')
INS = os.path.join(HERE, 'appH_insert.tex')
BIBINS = os.path.join(HERE, 'bib_entry.bib')
outdir = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
if outdir:
    assert not (outdir + os.sep).lower().startswith((ROOT + os.sep).lower()), 'output directory must be outside the repository'

def sha(b): return hashlib.sha256(b).hexdigest()

a = open(APPH, 'rb').read(); b = open(BIB, 'rb').read()
print('appH baseline:', len(a), sha(a)); print('bib baseline:', len(b), sha(b))
assert len(a) == 614579 and sha(a) == '7d15a3f287a59df1de78163f75eb1a18fe1ca894479889e1bbbbadae1ea5f85b'
assert len(b) == 29360 and sha(b) == '1d280848d1bb597193dc648963f81b9b635afce238aa2467fd13ce792002856d'
assert a.count(b'\r\n') == a.count(b'\n') and b.count(b'\r\n') == b.count(b'\n')

anchor = ('justified result is programme-conditional and supports only a\r\nscope-limited model.\r\n\r\n'
          + BS + 'section{Problem H: modular origin of the interpolating function}').encode()
n_anchor = a.count(anchor)
print('anchor occurrences:', n_anchor, '; plain Status paragraphs in appH:', a.count((BS + 'paragraph{Status.}').encode()))
assert n_anchor == 1
pos = a.index(anchor)
cut = pos + len(('justified result is programme-conditional and supports only a\r\nscope-limited model.\r\n').encode())
print('anchor starts at line', a[:pos].count(b'\n') + 1, '; insertion after line', a[:cut].count(b'\n'))
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

bi = open(BIBINS, 'rb').read()
assert b'\r' not in bi and bi.endswith(b'\n')
assert b.endswith(b'}\r\n')
newbib = b + b'\r\n' + bi.replace(b'\n', b'\r\n')
print('result bib:', len(newbib), sha(newbib), '; CRLF', newbib.count(b'\r\n'), '; bare LF', newbib.count(b'\n') - newbib.count(b'\r\n'))

refs = set(re.findall(r'\\ref\{([^}]*)\}', ins_txt)) | set(re.findall(r'\\eqref\{([^}]*)\}', ins_txt))
labels_new = re.findall(r'\\label\{([^}]*)\}', ins_txt)
cites = set(k.strip() for grp in re.findall(r'\\cite\{([^}]*)\}', ins_txt) for k in grp.split(','))
chap = os.path.join(ROOT, 'chapters')
alltex = ''.join(open(os.path.join(chap, f), encoding='utf-8').read() for f in os.listdir(chap) if f.endswith('.tex'))
for r in sorted(refs):
    c = alltex.count(BS + 'label{' + r + '}')
    print(f'ref {r}: label occurrences {c}'); assert c == 1
print('new labels:', labels_new); assert not labels_new
bibtxt = newbib.decode('utf-8')
for k in sorted(cites):
    c = len(re.findall(r'@\w+\{' + re.escape(k) + ',', bibtxt))
    print(f'cite {k}: entries in resulting bib {c}'); assert c == 1
print('key FlissFrenkelHartnollSoni2025 in baseline bib:', b.count(b'FlissFrenkelHartnollSoni2025'))
for bad in ('researcher', 'proposal', 'as proposed', 'gatekeeper', 'package'):
    assert bad not in ins_txt.lower(), bad
print('no process language found')
if outdir:
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, 'appH-microscopic-proofs.tex'), 'wb').write(new)
    open(os.path.join(outdir, 'namcg.bib'), 'wb').write(newbib)
    print('would-be appH and bib written to', outdir)
print('APPLY CHECK PASS')
