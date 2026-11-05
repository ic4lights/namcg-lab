"""compile_check (044): copy the CURRENT working tree of the manuscript to a scratch directory outside the
repository, insert appH_insert.tex immediately before the unique line \section{Problem G: HBEV} (one blank
line before it, CRLF restored), run pdflatex, bibtex, pdflatex, pdflatex, report pages, undefined
references/citations and multiply defined labels, compare with the same build without the insert, and delete
the scratch copy.  Usage: python compile_check.py <scratch_dir>  (must be outside the repository)."""
import os, re, shutil, subprocess, sys
repo = r'C:\Users\redgi\Projects\namcg-lab'
here = os.path.dirname(os.path.abspath(__file__))
base = sys.argv[1]
assert not os.path.abspath(base).lower().startswith(repo.lower()), 'scratch dir must be outside the repository'
anchor = '\section{Problem G: HBEV}'
ins = open(os.path.join(here, 'appH_insert.tex'), encoding='utf-8').read().rstrip() + '\n\n'
CRLF, LF = '\r\n', '\n'
def build(sc, with_insert):
    os.makedirs(sc, exist_ok=True)
    shutil.copy(os.path.join(repo, 'namcg-book7.tex'), sc)
    for d in ('chapters', 'bib', 'frontmatter', 'figs', 'code'):
        if os.path.isdir(os.path.join(repo, d)):
            shutil.copytree(os.path.join(repo, d), os.path.join(sc, d), dirs_exist_ok=True)
    p = os.path.join(sc, 'chapters', 'appH-microscopic-proofs.tex')
    raw = open(p, 'rb').read().decode('utf-8')
    crlf = CRLF in raw
    s = raw.replace(CRLF, LF)
    assert s.count(anchor) == 1
    if with_insert:
        s = s.replace(anchor, ins + anchor)
    if crlf:
        s = s.replace(LF, CRLF)
    open(p, 'wb').write(s.encode('utf-8'))
    codes = []
    for cmd in (['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'], ['bibtex', 'namcg-book7'],
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'],
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex']):
        r = subprocess.run(cmd, cwd=sc, capture_output=True, text=True, errors='ignore')
        codes.append(r.returncode)
    log = open(os.path.join(sc, 'namcg-book7.log'), errors='ignore').read()
    und = sorted(set(re.findall(r"Reference `([^']*)' on page \d+ undefined", log)))
    cit = sorted(set(re.findall(r"Citation `([^']*)' on page \d+ undefined", log)))
    mult = sorted(set(re.findall(r"Label `([^']*)' multiply defined", log)))
    m = re.search(r'Output written on namcg-book7.pdf \((\d+) pages', log)
    return crlf, codes, (m.group(1) if m else 'none'), und, cit, mult
lines = []
for tag, w in (('baseline (current working tree)', False), ('with insert', True)):
    crlf, codes, pages, und, cit, mult = build(os.path.join(base, 'i' if w else 'b'), w)
    lines.append(f'{tag}: CRLF preserved {crlf}; exit codes (pdflatex, bibtex, pdflatex, pdflatex) {codes}; {pages} pages')
    lines.append(f'   undefined refs: {und}')
    lines.append(f'   undefined citations: {cit}')
    lines.append(f'   multiply defined labels: {mult}')
shutil.rmtree(base)
lines.append('scratch removed: ' + str(not os.path.exists(base)))
out = '\n'.join(lines)
open(os.path.join(here, 'compile_check.out.txt'), 'w', newline='\n').write(out + '\n')
print(out)
