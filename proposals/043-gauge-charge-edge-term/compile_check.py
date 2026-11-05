"""compile_check (043): copy the CURRENT working tree of the manuscript to a scratch directory outside the
repository, insert appH_insert.tex immediately before the unique line
\\section{Problem C: conformal mode and Cassini} (one blank line before it), append bib_add.bib to the
copied bib/namcg.bib, run pdflatex, bibtex, pdflatex, pdflatex, report pages, undefined
references/citations and multiply defined labels, compare with the same build without the insert,
and delete the scratch copy.
Usage: python compile_check.py <scratch_dir>  (must be outside the repository)."""
import os, re, shutil, subprocess, sys

repo = r'C:\Users\redgi\Projects\namcg-lab'
here = os.path.dirname(os.path.abspath(__file__))
base = sys.argv[1]
assert not os.path.abspath(base).lower().startswith(repo.lower()), 'scratch dir must be outside the repository'
anchor = '\\section{Problem C: conformal mode and Cassini}'
ins = open(os.path.join(here, 'appH_insert.tex'), encoding='utf-8').read().rstrip() + '\n\n'
bibadd = open(os.path.join(here, 'bib_add.bib'), encoding='utf-8').read()
CRLF = '\r\n'
LF = '\n'


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
        bp = os.path.join(sc, 'bib', 'namcg.bib')
        braw = open(bp, 'rb').read().decode('utf-8')
        assert 'Chen2022' not in braw
        nl = CRLF if CRLF in braw else LF
        open(bp, 'wb').write((braw.rstrip() + nl + nl + bibadd.replace(LF, nl)).encode('utf-8'))
        cp = os.path.join(sc, 'chapters', 'ch07-massless-tensor.tex')
        craw = open(cp, 'rb').read().decode('utf-8')
        o7 = r'   \bigl((\ell^2-t^2-r^2)\partial_t^\mu+2t\,x^\mu\bigr)'
        n7 = r'   \bigl((\ell^2-t^2-r^2)\partial_t^\mu-2t\,x^i\delta^\mu_i\bigr)'
        assert craw.count(o7) == 1
        open(cp, 'wb').write(craw.replace(o7, n7).encode('utf-8'))
    if crlf:
        s = s.replace(LF, CRLF)
    open(p, 'wb').write(s.encode('utf-8'))
    codes = []
    for cmd in (['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'],
                ['bibtex', 'namcg-book7'],
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'],
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex']):
        r = subprocess.run(cmd, cwd=sc, capture_output=True, text=True, errors='ignore')
        codes.append(r.returncode)
    log = open(os.path.join(sc, 'namcg-book7.log'), errors='ignore').read()
    und = sorted(set(re.findall(r"Reference `([^']*)' on page \d+ undefined", log)))
    cit = sorted(set(re.findall(r"Citation `([^']*)' on page \d+ undefined", log)))
    mult = sorted(set(re.findall(r"Label `([^']*)' multiply defined", log)))
    m = re.search(r'Output written on namcg-book7.pdf \((\d+) pages', log)
    pages = m.group(1) if m else 'none'
    return crlf, codes, pages, und, cit, mult


lines = []
for tag, w in (('baseline (current working tree)', False), ('with insert, bib entry and ch07 L227 fix', True)):
    sc = os.path.join(base, 'b' if not w else 'i')
    crlf, codes, pages, und, cit, mult = build(sc, w)
    lines.append(f'{tag}: CRLF preserved {crlf}; exit codes (pdflatex, bibtex, pdflatex, pdflatex) {codes}; {pages} pages')
    lines.append(f'   undefined refs: {und}')
    lines.append(f'   undefined citations: {cit}')
    lines.append(f'   multiply defined labels: {mult}')
shutil.rmtree(base)
lines.append('scratch removed: ' + str(not os.path.exists(base)))
out = '\n'.join(lines)
open(os.path.join(here, 'compile_check.out.txt'), 'w').write(out + '\n')
print(out)
