r"""Apply the two snippets to a COPY of the repository outside it and build there.

Run: python -I apply_and_build_r3.py <repo_root> <scratch_dir>
The repository itself is only read. The copy in <scratch_dir> is deleted at the end.
"""
import hashlib, os, re, shutil, subprocess, sys

repo, scratch = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
APPH = os.path.join('chapters', 'appH-microscopic-proofs.tex')
PRE_SHA = 'a7f1492a30c89b52e9ecadcd2550aaab89261796c35266b19bfed0d5b354e842'

def sha(b): return hashlib.sha256(b).hexdigest()

src = open(os.path.join(repo, APPH), 'rb').read()
print('pre  appH bytes', len(src), 'sha', sha(src), 'CRLF', src.count(b'\r\n'), 'bareLF', src.count(b'\n') - src.count(b'\r\n'))
assert sha(src) == PRE_SHA, 'pre-state mismatch'

bc = open(os.path.join(HERE, 'block_C_r3.tex'), 'rb').read()
bf = open(os.path.join(HERE, 'block_F_r3.tex'), 'rb').read()
for b in (bc, bf):
    assert b.count(b'\n') == b.count(b'\r\n') and not b.endswith(b'\n')

# anchor C: insert a blank line and the Missing-step paragraph after the mixing block,
# directly before the existing closing line of the Problem C entry
AC = b'tensor operator or the remaining scalar couplings.\r\nProblems~B, C, D, F and~G remain open.\r\n\r\n\\section{Problem D: local Lorentz}'
assert src.count(AC) == 1, 'anchor C not unique'
cut = len(b'tensor operator or the remaining scalar couplings.')
newC = AC[:cut] + b'\r\n\r\n' + bc + AC[cut:]
# anchor F: insert the new paragraph before \section{Problem G: HBEV}
AF = b'Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.\r\n\r\n\\section{Problem G: HBEV}'
assert src.count(AF) == 1, 'anchor F not unique'
cutF = len(b'Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.')
newF = AF[:cutF] + b'\r\n\r\n' + bf + AF[cutF:]
out = src.replace(AC, newC).replace(AF, newF)
assert len(out) == len(src) + 4 + len(bc) + 4 + len(bf)
assert out.count(bc) == 1 and out.count(bf) == 1
# status lines untouched
for lab in (b'\\label{sec:status-C}', b'\\label{sec:status-F}'):
    assert out.count(lab) == 1
assert out.count(b'Status: OPEN. Priority: CRITICAL PATH.') == src.count(b'Status: OPEN. Priority: CRITICAL PATH.')
print('post appH bytes', len(out), 'sha', sha(out), 'CRLF', out.count(b'\r\n'), 'bareLF', out.count(b'\n') - out.count(b'\r\n'))
POST_SHA_R2 = '112b485c75518bd63eb7495a5ade2bced80028b6bbe05fab6ce7c6cebaeee07f'
assert sha(out) != POST_SHA_R2
MCHI = b'm_\chi^2=U_{\chi\chi}/Z_\chi'
assert out.count(MCHI) == 1 and out.index(MCHI) < out.index(bf), 'm_chi must be defined before block F'
rr, rs = os.path.realpath(repo).lower(), os.path.realpath(scratch).lower()
assert not (rs + os.sep).startswith(rr + os.sep), 'scratch must be outside the repo'

# refs used by the snippets must have exactly one label in chapters/
chap = os.path.join(repo, 'chapters')
alltex = b''.join(open(os.path.join(chap, f), 'rb').read() for f in os.listdir(chap) if f.endswith('.tex'))
refs = set(re.findall(rb'\\(?:eq)?ref\{([^}]*)\}', bc + bf))
for r in sorted(refs):
    n = alltex.count(b'\\label{' + r + b'}')
    print('label', r.decode(), n)
    assert n == 1
assert b'\\label' not in bc + bf

# build on a copy outside the repository
dst = os.path.join(scratch, 'namcg-build-062-064-r3')
if os.path.exists(dst):
    shutil.rmtree(dst)
shutil.copytree(repo, dst, ignore=shutil.ignore_patterns('.git', 'proposals', 'scratch', 'reports', 'namcg-book7.pdf', '.claude'))
open(os.path.join(dst, APPH), 'wb').write(out)
log = ''
for k in range(2):
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'],
                       cwd=dst, capture_output=True, text=True, errors='replace')
    print('pdflatex pass', k + 1, 'returncode', r.returncode)
log = open(os.path.join(dst, 'namcg-book7.log'), encoding='latin-1').read()
undef = re.findall(r"(?:Reference|Citation) `[^']*' on page \d+ undefined", log)
multi = re.findall(r"Label `[^']*' multiply defined", log)
print('undefined refs/cites:', len(undef), undef[:5])
print('multiply defined labels:', len(multi), multi[:5])
print('pdf exists:', os.path.exists(os.path.join(dst, 'namcg-book7.pdf')))
errs = [l for l in log.splitlines() if l.startswith('!')]
print('errors:', len(errs), errs[:5])
if errs:
    i = log.find(chr(10) + '!')
    print(log[i:i + 1500])
shutil.rmtree(dst)
print('scratch copy removed:', not os.path.exists(dst))
