# cert_129.py -- item 129 compile certificate for payload-F.tex (spliced into a scratch copy
# of chapters/appH-microscopic-proofs.tex OUTSIDE the repository; scratch deleted at the end).
# Run:  python -I proposals/129-rc-held-recheck/cert_129.py
# Expected invariant output: last line  CERT129 PASS (exit 0, undefined refs/citations = 0)
import os, shutil, subprocess, sys, tempfile, hashlib

REPO = r'C:\Users\redgi\Projects\namcg-lab@gpu'
FOLDER = os.path.join(REPO, 'proposals', '129-rc-held-recheck')
TMP = tempfile.mkdtemp(prefix='cert129_')

for rel in ['chapters', 'frontmatter', 'bib', 'figs']:
    dst = os.path.join(TMP, rel)
    shutil.copytree(os.path.join(REPO, rel), dst, ignore=shutil.ignore_patterns('*.aux', '*.bbl', '*.blg', '*.toc'))
for f in ['namcg-book7.tex']:
    shutil.copy(os.path.join(REPO, f), os.path.join(TMP, f))

# --- splice payload-F.tex after the unique anchor tail, before \emph{Scale dependence.}
apH = os.path.join(TMP, 'chapters', 'appH-microscopic-proofs.tex')
txt = open(apH, 'rb').read()
anchor = ('On this evidence the sign of \\(\\hat U\\) depends on \\(K\\).').encode() + b'\r\n\r\n'
scale = b'\\emph{Scale dependence.}'
assert txt.count(anchor) == 1, 'anchor count %d' % txt.count(anchor)
assert txt.count(scale) == 1, 'scale count %d' % txt.count(scale)
payload = open(os.path.join(FOLDER, 'payload-F.tex'), 'rb').read()
assert payload.endswith(b'\r\n')
new = txt.replace(anchor, anchor + payload + b'\r\n', 1)
assert new.count(scale) == 1 and new.count(payload) == 1
open(apH, 'wb').write(new)
print('splice: pre %d B -> post %d B (payload %d B + join)' % (len(txt), len(new), len(payload)))

def run(cmd):
    r = subprocess.run(cmd, cwd=TMP, capture_output=True, text=True)
    return r.returncode

rc = 1
for i in range(2):
    rc = run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'])
    assert rc == 0, 'pdflatex pass %d exit %d' % (i + 1, rc)
    if i == 0:
        rb = run(['bibtex', 'namcg-book7'])
        print('bibtex exit', rb)
        rc = run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'])
        assert rc == 0
log = open(os.path.join(TMP, 'namcg-book7.log'), 'r', errors='replace').read()
import re
m = re.search(r'Output written on namcg-book7.pdf \((\d+) pages', log)
pages = int(m.group(1))
und = len(re.findall(r'Reference .* undefined', log)) + len(re.findall(r'Citation .* undefined', log))
mult = len(re.findall(r'multiply defined', log, re.I))
print('pdflatex exit 0/0, pages = %d, undefined refs/citations = %d, multiply-defined = %d' % (pages, und, mult))
shutil.rmtree(TMP, ignore_errors=True)
assert rc == 0 and pages > 0 and und == 0 and mult == 0
print('CERT129 PASS (exit 0, undefined refs/citations = 0)')
