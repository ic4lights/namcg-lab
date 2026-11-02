"""compile_check (052): build check of the bytes on a copy outside the repository, nothing in the repository written.

Differs from compile_check.py, kept as the r1 record, only in the insertion: it works on bytes, as the integrator would.
The anchor is the byte string of the section line plus CRLF, required exactly once, with bare LF required zero times.
appH_insert.tex is converted to CRLF and placed immediately before it, and new_bib_entries.bib is converted to CRLF and appended.
It reports the count of bare LF after insertion, exit codes, pages, undefined references and citations, multiply defined labels,
and bibtex warnings, for the baseline and for the insert.  Usage: python compile_check_r2.py <scratch_dir>."""
import hashlib
import os
import re
import shutil
import subprocess
import sys

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
    print('SKIPPED: manuscript not found; set NAMCG_REPO')
    sys.exit(0)
base = sys.argv[1]
assert not os.path.abspath(base).lower().startswith(os.path.abspath(repo).lower()), 'scratch dir must be outside the repository'
assert not os.path.exists(base), 'scratch dir must not exist yet'

BS = bytes([92])
ANCHOR = BS + b'section{Problem E: signature}'
CRLF, LF = b'\r\n', b'\n'
ins_raw = open(os.path.join(here, 'appH_insert.tex'), 'rb').read()
bib_raw = open(os.path.join(here, 'new_bib_entries.bib'), 'rb').read()
assert CRLF not in ins_raw and CRLF not in bib_raw
print('insert', len(ins_raw), 'bytes sha256', hashlib.sha256(ins_raw).hexdigest())
print('bib   ', len(bib_raw), 'bytes sha256', hashlib.sha256(bib_raw).hexdigest())
ins = ins_raw.replace(LF, CRLF)
bibadd = bib_raw.replace(LF, CRLF)
print('insert after CRLF conversion', len(ins), 'bytes; bib after CRLF conversion', len(bibadd), 'bytes')


def bare_lf(b):
    return b.count(LF) - b.count(CRLF)


def build(sc, with_insert):
    os.makedirs(sc)
    shutil.copy(os.path.join(repo, 'namcg-book7.tex'), sc)
    for d in ('chapters', 'bib', 'frontmatter', 'figs', 'code'):
        if os.path.isdir(os.path.join(repo, d)):
            shutil.copytree(os.path.join(repo, d), os.path.join(sc, d))
    p = os.path.join(sc, 'chapters', 'appH-microscopic-proofs.tex')
    raw = open(p, 'rb').read()
    print('  anchor+CRLF count', raw.count(ANCHOR + CRLF), '; anchor+bare LF count', raw.count(ANCHOR + LF), '; bare LF in appH before', bare_lf(raw))
    assert raw.count(ANCHOR + CRLF) == 1 and raw.count(ANCHOR + LF) == 0
    q = os.path.join(sc, 'bib', 'namcg.bib')
    bib = open(q, 'rb').read()
    if with_insert:
        new = raw.replace(ANCHOR + CRLF, ins + ANCHOR + CRLF)
        assert len(new) == len(raw) + len(ins)
        print('  bare LF in appH after', bare_lf(new), '; bytes added', len(new) - len(raw))
        assert bare_lf(new) == bare_lf(raw)
        open(p, 'wb').write(new)
        assert bib.endswith(CRLF)
        for key in re.findall(rb'@\w+\{([^,\s]+),', bib_raw):
            assert (b'{' + key + b',') not in bib, key
        newbib = bib + CRLF + bibadd
        print('  bare LF in bib after', bare_lf(newbib))
        open(q, 'wb').write(newbib)
    codes = []
    tex = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex']
    for cmd in (tex, ['bibtex', 'namcg-book7'], tex, tex):
        r = subprocess.run(cmd, cwd=sc, capture_output=True, text=True, errors='ignore')
        codes.append(r.returncode)
    log = open(os.path.join(sc, 'namcg-book7.log'), errors='ignore').read()
    blg = open(os.path.join(sc, 'namcg-book7.blg'), errors='ignore').read()
    und = sorted(set(re.findall(r"Reference `([^']*)' on page \d+ undefined", log)))
    cit = sorted(set(re.findall(r"Citation `([^']*)' on page \d+ undefined", log)))
    mult = sorted(set(re.findall(r"Label `([^']*)' multiply defined", log)))
    m = re.search(r'Output written on namcg-book7.pdf \((\d+) pages', log)
    warn = re.findall(r'Warning--.*', blg)
    print('  exit codes (pdflatex, bibtex, pdflatex, pdflatex)', codes, ';', m.group(1) if m else 'none', 'pages')
    print('  undefined refs', und, '; undefined citations', cit, '; multiply defined labels', mult)
    print('  bibtex warnings', len(warn), warn[:8])
    bbl = open(os.path.join(sc, 'namcg-book7.bbl'), errors='ignore').read()
    print('  in bbl:', [k for k in ('Sakai2017', 'OsterwalderSchrader1973', 'OsterwalderSchrader1975', 'IsonoTomino2010', 'Liao2026') if '{' + k + '}' in bbl], '; bibitems', bbl.count('bibitem'))


os.makedirs(base)
print('baseline (current working tree):')
build(os.path.join(base, 'b'), False)
print('with insert and bib entries:')
build(os.path.join(base, 'i'), True)
shutil.rmtree(base)
print('scratch removed:', not os.path.exists(base))
