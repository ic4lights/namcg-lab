"""Scratch copy outside the repo: insert block-r1.tex before the unique anchor, build twice, report errors/undefined/multiply-defined, delete copy."""
import shutil, subprocess, tempfile, os, re
repo = r'C:\Users\redgi\Projects\namcg-lab'
tmp = tempfile.mkdtemp(prefix='c030_')
for n in os.listdir(repo):
    if n in ('.git', 'proposals', 'reports', 'scratch', 'code', 'agents', '.claude'):
        continue
    s = os.path.join(repo, n)
    (shutil.copytree if os.path.isdir(s) else shutil.copy)(s, os.path.join(tmp, n))
p = os.path.join(tmp, 'chapters', 'appH-microscopic-proofs.tex')
t = open(p, encoding='utf-8', newline='').read()
a = '\\section{Problem G: HBEV}'
assert t.count(a) == 1
blk = open('block-r1.tex', encoding='utf-8').read().replace('\r\n', '\n').replace('\n', '\r\n')
t = t.replace(a, blk + '\r\n' + a)
open(p, 'w', encoding='utf-8', newline='').write(t)
for i in range(2):
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'], cwd=tmp, capture_output=True, text=True)
log = open(os.path.join(tmp, 'namcg-book7.log'), errors='ignore').read()
print('anchor unique: True; returncode', r.returncode, '; errors', len(re.findall(r'^!', log, re.M)), '; undefined', len(re.findall(r'undefined', log)), '; multiply defined', len(re.findall(r'multiply', log)))
print('pages', re.findall(r'Output written on .*\((\d+) pages', log))
print('double subscripts in block:', len(re.findall(r'_[A-Za-z0-9]+_', open('block-r1.tex').read())))
shutil.rmtree(tmp, ignore_errors=True)
