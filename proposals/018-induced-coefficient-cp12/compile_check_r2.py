"""Scratch-copy compile check (outside the repository). Inserts block-r2.tex before \\section{Problem G: HBEV}, adds BenArous1989 to the scratch bib."""
import shutil, subprocess, tempfile, os, re
repo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
tmp = tempfile.mkdtemp(prefix='cc018_')
for d in ('chapters', 'bib', 'frontmatter', 'figs'):
    if os.path.isdir(os.path.join(repo, d)):
        shutil.copytree(os.path.join(repo, d), os.path.join(tmp, d))
shutil.copy(os.path.join(repo, 'namcg-book7.tex'), tmp)
p = os.path.join(tmp, 'chapters', 'appH-microscopic-proofs.tex')
t = open(p, 'rb').read().decode('utf8')
blk = open(os.path.join(os.path.dirname(__file__), 'block-r2.tex'), 'rb').read().decode('utf8').replace('\r\n', '\n')
a = '\\section{Problem G: HBEV}'
assert t.count(a) == 1
nl = '\r\n' if '\r\n' in t else '\n'
open(p, 'wb').write(t.replace(a, blk.replace('\n', nl) + a).encode('utf8'))
with open(os.path.join(tmp, 'bib', 'namcg.bib'), 'a', encoding='utf8') as b:
    b.write("\n@article{BenArous1989,\n author={Ben Arous, G{\\'e}rard},\n title={D{\\'e}veloppement asymptotique du noyau de la chaleur hypoelliptique sur la diagonale},\n journal={Annales de l'Institut Fourier},\n volume={39}, number={1}, pages={73--99}, year={1989}, doi={10.5802/aif.1158}\n}\n")
def run(cmd):
    return subprocess.run(cmd, cwd=tmp, capture_output=True, text=True)
for cmd in (['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'], ['bibtex', 'namcg-book7'],
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'], ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex']):
    r = run(cmd); print(cmd[0], 'rc', r.returncode)
log = open(os.path.join(tmp, 'namcg-book7.log'), encoding='utf8', errors='replace').read()
print('errors:', len(re.findall(r'^!', log, re.M)), ' undefined refs/cites:', len(re.findall(r'undefined', log)), ' multiply defined:', len(re.findall(r'multiply', log)), ' double subscript:', len(re.findall('Double subscript', log)))
print(re.findall(r'Output written on .*', log))
shutil.rmtree(tmp)
