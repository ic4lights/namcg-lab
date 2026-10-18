"""Scratch-copy compile check outside the repo: inserts block-r2.tex before the Problem G section."""
import shutil, subprocess, tempfile, os, re
here = os.path.dirname(os.path.abspath(__file__)); repo = os.path.abspath(os.path.join(here, '..', '..'))
tmp = tempfile.mkdtemp(prefix='cc027r2_', dir=os.environ.get('SCRATCH'))
for d in ('chapters', 'bib', 'frontmatter', 'figs'):
    if os.path.isdir(os.path.join(repo, d)): shutil.copytree(os.path.join(repo, d), os.path.join(tmp, d))
shutil.copy(os.path.join(repo, 'namcg-book7.tex'), tmp)
p = os.path.join(tmp, 'chapters', 'appH-microscopic-proofs.tex'); t = open(p, 'rb').read().decode('utf8')
blk = open(os.path.join(here, 'block-r2.tex'), 'rb').read().decode('utf8').replace('\r\n', '\n')
a = '\section{Problem G: HBEV}'; assert t.count(a) == 1
assert 'Problem~F remains open.' in t[:t.index(a)][-1500:]
nl = '\r\n' if '\r\n' in t else '\n'
open(p, 'wb').write(t.replace(a, blk.replace('\n', nl) + nl + a).encode('utf8'))
print('anchor unique')
for cmd in (['pdflatex','-interaction=nonstopmode','-halt-on-error','namcg-book7.tex'],['bibtex','namcg-book7'],['pdflatex','-interaction=nonstopmode','-halt-on-error','namcg-book7.tex'],['pdflatex','-interaction=nonstopmode','-halt-on-error','namcg-book7.tex']):
    r = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True); print(cmd[0], 'rc', r.returncode)
log = open(os.path.join(tmp,'namcg-book7.log'),encoding='utf8',errors='replace').read()
print('errors:',len(re.findall(r'^!',log,re.M)),' undefined:',len(re.findall(r'undefined',log)),' multiply:',len(re.findall(r'multiply',log)),' double subscript:',len(re.findall('Double subscript',log)))
print(re.findall(r'Output written on .*',log)); shutil.rmtree(tmp)
