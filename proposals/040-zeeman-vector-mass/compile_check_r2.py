"""Scratch copy outside the repo: apply merged_edits.md (OLD->NEW) and insert appH_insert.tex before the unique anchor, build twice, report errors/undefined/multiply defined/duplicate labels."""
import shutil, subprocess, tempfile, os, re
LBL = chr(92)*2 + 'label' + chr(92) + '{([^}]*)' + chr(92) + '}'
repo = r'C:\Users\redgi\Projects\namcg-lab'
tmp = tempfile.mkdtemp(prefix='c040r2_')
for n in os.listdir(repo):
    if n in ('.git', 'proposals', 'reports', 'scratch', 'code', 'agents', '.claude'):
        continue
    s = os.path.join(repo, n)
    (shutil.copytree if os.path.isdir(s) else shutil.copy)(s, os.path.join(tmp, n))
p = os.path.join(tmp, 'chapters', 'appH-microscopic-proofs.tex')
t = open(p, encoding='utf-8', newline='').read().replace('\r\n', '\n')
md = open('merged_edits.md').read()
olds = re.findall(r'OLD \(count 1\):\n```\n(.*?)\n```', md, re.S)
news = re.findall(r'NEW[^\n]*:\n```\n(.*?)\n```', md, re.S)
assert len(olds) == len(news) == 3
for o, n in zip(olds, news):
    assert t.count(o) == 1
    t = t.replace(o, n)
a = '\section{Problem G: HBEV}'
assert t.count(a) == 1
t = t.replace(a, open('appH_insert.tex', encoding='utf-8').read() + a)
open(p, 'w', encoding='utf-8', newline='').write(t.replace('\n', '\r\n'))
for i in range(2):
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'], cwd=tmp, capture_output=True, text=True)
log = open(os.path.join(tmp, 'namcg-book7.log'), errors='ignore').read()
labels = []
for f in os.listdir(os.path.join(tmp, 'chapters')):
    labels += re.findall(LBL, open(os.path.join(tmp, 'chapters', f), encoding='utf-8').read())
labels += re.findall(LBL, open(os.path.join(tmp, 'namcg-book7.tex'), encoding='utf-8').read())
print('returncode', r.returncode, '; errors', len(re.findall(r'^!', log, re.M)), '; undefined', len(re.findall(r'undefined', log)), '; multiply defined', len(re.findall(r'multiply', log)), '; duplicate labels', len(labels) - len(set(labels)))
k = log.find('\n! ')
if k >= 0: print(log[k:k + 700])
print('pages', re.findall(r'Output written on .*\((\d+) pages', log))
shutil.rmtree(tmp, ignore_errors=True)
