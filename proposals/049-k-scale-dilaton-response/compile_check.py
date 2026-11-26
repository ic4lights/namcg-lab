"""compile_check (049): copy the current working tree to a scratch directory outside the repository, add
new_bib_entry.bib to the copy of bib/namcg.bib, insert appH_insert.tex immediately before the unique line
\section{Problem G: HBEV} (CRLF restored in the copy), run pdflatex, bibtex, pdflatex, pdflatex, report pages,
undefined references/citations and multiply defined labels, compare with the same build without the insert,
and delete the scratch copy.  Usage: python compile_check.py <scratch_dir> (outside the repository)."""
import os, re, shutil, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
def find_repo():
    r = os.environ.get('NAMCG_REPO')
    if r and os.path.isfile(os.path.join(r, 'namcg-book7.tex')):
        return r
    d = here
    while True:
        if os.path.isfile(os.path.join(d, 'namcg-book7.tex')):
            return d
        n = os.path.dirname(d)
        if n == d:
            return None
        d = n
repo = find_repo()
if repo is None:
    print('SKIPPED: manuscript not found; set NAMCG_REPO'); sys.exit(0)
base = sys.argv[1]
assert not os.path.abspath(base).lower().startswith(repo.lower()), 'scratch dir must be outside the repository'
anchor = '\section{Problem G: HBEV}'
ins = open(os.path.join(here, 'appH_insert.tex'), encoding='utf-8').read().rstrip() + '\n\n'
bibnew = open(os.path.join(here, 'new_bib_entry.bib'), encoding='utf-8').read()
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
        with open(os.path.join(sc, 'bib', 'namcg.bib'), 'a', encoding='utf-8', newline='') as f:
            f.write('\n' + bibnew)
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
for tag, w in (('baseline (current working tree)', False), ('with insert and bib entry', True)):
    crlf, codes, pages, und, cit, mult = build(os.path.join(base, 'i' if w else 'b'), w)
    print(f'{tag}: CRLF preserved {crlf}; exit codes (pdflatex, bibtex, pdflatex, pdflatex) {codes}; {pages} pages')
    print(f'   undefined refs: {und}')
    print(f'   undefined citations: {cit}')
    print(f'   multiply defined labels: {mult}')
shutil.rmtree(base)
print('scratch removed:', not os.path.exists(base))
