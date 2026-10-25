"""compile_check: apply appH_insert.tex (BLOCK 1 before the unique line \\section{Problem C: conformal mode and Cassini},
BLOCK 2 before the unique line \\section{Problem G: HBEV}) to a scratch COPY of the manuscript outside the repository,
run two pdflatex passes, report undefined references / multiply defined labels, and remove the scratch copy.
Usage: python compile_check.py <scratch_dir>   (scratch_dir must be outside the repository; it is created and deleted)"""
import os, re, shutil, subprocess, sys

repo = r'C:\Users\redgi\Projects\namcg-lab'
here = os.path.dirname(os.path.abspath(__file__))
sc = sys.argv[1]
assert not os.path.abspath(sc).startswith(repo), 'scratch dir must be outside the repository'
os.makedirs(sc, exist_ok=True)
shutil.copy(os.path.join(repo, 'namcg-book7.tex'), sc)
for d in ('chapters', 'bib', 'frontmatter', 'figs', 'code'):
    shutil.copytree(os.path.join(repo, d), os.path.join(sc, d), dirs_exist_ok=True)
p = os.path.join(sc, 'chapters', 'appH-microscopic-proofs.tex')
raw = open(p, 'rb').read().decode('utf-8')
crlf = '\r\n' in raw
s = raw.replace('\r\n', '\n')
ins = open(os.path.join(here, 'appH_insert.tex'), encoding='utf-8').read()
bS = ins.index('\\paragraph{Moser variables')
fS = ins.index('\\paragraph{Conjugate-coordinate class: the Casimir form')
blockB = ins[bS:ins.index('%% ===== BLOCK 2')].rstrip() + '\n\n'
blockF = ins[fS:].rstrip() + '\n\n'
aC = '\\section{Problem C: conformal mode and Cassini}'
aG = '\\section{Problem G: HBEV}'
assert s.count(aC) == 1 and s.count(aG) == 1
s = s.replace(aC, blockB + aC).replace(aG, blockF + aG)
if crlf:
    s = s.replace('\n', '\r\n')
open(p, 'wb').write(s.encode('utf-8'))
codes = []
for i in (1, 2):
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'], cwd=sc, capture_output=True, text=True, errors='ignore')
    codes.append(r.returncode)
log = open(os.path.join(sc, 'namcg-book7.log'), errors='ignore').read()
und = re.findall(r"Reference `([^']*)' on page \d+ undefined", log)
cit = set(re.findall(r"Citation `([^']*)' on page \d+ undefined", log))
mult = re.findall(r"Label `([^']*)' multiply defined", log)
pages = re.search(r'Output written on namcg-book7.pdf \((\d+) pages', log).group(1)
out = (f'compile_check (scratch copy outside the repository; CRLF preserved: {crlf})\n'
       f'pdflatex exit codes {codes}, {pages} pages\n'
       f'undefined \\ref targets: {und}\nmultiply defined labels: {mult}\n'
       f'undefined citations: {len(cit)} (bibtex not run in the scratch copy; the inserted text contains no \\cite and no \\ref)\n')
open(os.path.join(here, 'compile_check.out.txt'), 'w').write(out)
print(out)
shutil.rmtree(sc)
print('scratch removed')
