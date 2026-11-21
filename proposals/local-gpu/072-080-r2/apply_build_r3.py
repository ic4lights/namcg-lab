"""072-080 r3: insertion rule, byte contract and applied-copy build (outside the repository).

Usage:
  python -I proposals/local-gpu/072-080-r2/apply_build_r3.py OUTDIR [--build]

Reads the live chapters/appH-microscopic-proofs.tex and bib/namcg.bib (read-only),
applies the r3 package in memory and writes the applied copies to OUTDIR (which
must lie outside the repository).  With --build it copies the build inputs to
OUTDIR/build, runs pdflatex, bibtex, pdflatex, pdflatex there and scans the log.

Insertion rule (all anchors must occur exactly once), applied in this order:
  R3  (first) dependency, see below;
  R1  insert insert_block_r3.tex, followed by one blank CRLF line, immediately
      before the line that starts with
        \\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023}
  R2  replace the whole line that starts with
        These statements are for a compact factor with positive contraction, a single
        projector at fixed frame for the deformed sphere and the two caps,
      by closing_r3.tex;
  R3  dependency (local 067, accepted, not part of this package): if the paragraph
        \\paragraph{Edge of a toric block on a product of two fuzzy spheres
      is absent, insert proposals/067-product-sphere-edge/appH_insert_r2.tex
      (sha256 f0fa634c...), followed by one blank CRLF line, immediately before the
      line \\section{Problem H: modular origin of the interpolating function};
  R5  (last) in the Bearing paragraph (the line that starts with
        \\emph{Bearing on Assumption~\\ref{ass:Sent-density}.} (i) The block is a region of the factor;
      the 067 insert has its own Bearing paragraph, so the shorter prefix is not
      unique after R3), replace the string
        up to a correction of the order of a logarithm (numerical)
      (exactly one occurrence in the file, inside that line) by
        up to a correction of the order of \\(\\ell_1^2/M_1+\\ell_2^2/M_2\\) and of a logarithm (numerical)
  R4  append bib_additions_r2.bib to bib/namcg.bib (one blank line before it) if the
      key Frenkel2023EdgeModes is absent.
Snippets are CRLF; the script asserts CRLF and no bare LF in every output.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
APPH = ROOT / 'chapters' / 'appH-microscopic-proofs.tex'
BIB = ROOT / 'bib' / 'namcg.bib'
P067 = ROOT / 'proposals' / '067-product-sphere-edge' / 'appH_insert_r2.tex'
SHA067 = 'f0fa634cbae16d6c41366f72a8c4e3f834b26fbe31d37532204eb513b6c014ee'

A1 = b'\\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023}'
A2 = (b'These statements are for a compact factor with positive contraction, a single '
      b'projector at fixed frame for the deformed sphere and the two caps,')
A3 = b'\\section{Problem H: modular origin of the interpolating function}'
H067 = b'\\paragraph{Edge of a toric block on a product of two fuzzy spheres'
KEY = b'@misc{Frenkel2023EdgeModes,'
A5 = rb'\emph{Bearing on Assumption~\ref{ass:Sent-density}.} (i) The block is a region of the factor'
O5 = b'up to a correction of the order of a logarithm (numerical)'
N5 = rb'up to a correction of the order of \(\ell_1^2/M_1+\ell_2^2/M_2\) and of a logarithm (numerical)'


def info(b):
    return '%d B sha256 %s CRLF %d bareLF %d' % (
        len(b), hashlib.sha256(b).hexdigest(), b.count(b'\r\n'), b.count(b'\n') - b.count(b'\r\n'))


def crlf(b):
    return b.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')


def snippet(name):
    b = (HERE / name).read_bytes()
    assert b.count(b'\n') == b.count(b'\r\n'), name + ' is not CRLF'
    assert b.endswith(b'\r\n'), name
    assert not b.startswith(b'\xef\xbb\xbf'), name + ' has a BOM'
    return b


def lines_starting(text, prefix):
    lines = text.split(b'\r\n')
    return [i for i, l in enumerate(lines) if l.startswith(prefix)], lines


def apply_one(text, block, closing, ins067):
    if ins067 is not None:
        idx, lines = lines_starting(text, A3)
        assert len(idx) == 1, ('R3 anchor count', len(idx))
        i3 = idx[0]
        lines = lines[:i3] + ins067[:-2].split(b'\r\n') + [b''] + lines[i3:]
        text = b'\r\n'.join(lines)
    idx, lines = lines_starting(text, A1)
    assert len(idx) == 1, ('R1 anchor count', len(idx))
    i1 = idx[0]
    blk = block[:-2].split(b'\r\n') + [b'']
    lines = lines[:i1] + blk + lines[i1:]
    text = b'\r\n'.join(lines)
    idx, lines = lines_starting(text, A2)
    assert len(idx) == 1, ('R2 anchor count', len(idx))
    lines[idx[0]] = closing[:-2]
    assert b'\r\n' not in closing[:-2]
    text = b'\r\n'.join(lines)
    idx, lines = lines_starting(text, A5)
    assert len(idx) == 1, ('R5 line anchor count', len(idx))
    assert text.count(O5) == 1 and lines[idx[0]].count(O5) == 1, ('R5 string count', text.count(O5))
    lines[idx[0]] = lines[idx[0]].replace(O5, N5)
    text = b'\r\n'.join(lines)
    assert text.count(N5) == 1 and O5 not in text
    return text


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1]).resolve()
    assert ROOT not in out.parents and out != ROOT, 'OUTDIR must lie outside the repository'
    out.mkdir(parents=True, exist_ok=True)
    build = '--build' in sys.argv
    apph = APPH.read_bytes()
    bib = BIB.read_bytes()
    print('PRE  appH', info(apph))
    print('PRE  bib ', info(bib))
    block = snippet('insert_block_r3.tex')
    closing = snippet('closing_r3.tex')
    bibadd = snippet('bib_additions_r2.bib')
    for n in ('insert_block_r3.tex', 'closing_r3.tex', 'bib_additions_r2.bib'):
        print('snippet %-22s' % n, info((HERE / n).read_bytes()))
    has067 = H067 in apph
    print('067 present in live appH:', has067)
    ins067 = None
    if not has067:
        raw = P067.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == SHA067, '067 accepted insert changed'
        ins067 = crlf(raw)
        if not ins067.endswith(b'\r\n'):
            ins067 += b'\r\n'
    # anchors
    for nm, a in (('R1', A1), ('R2', A2), ('R3', A3), ('R5 line', A5)):
        print('anchor %s line-start count: %d' % (nm, len(lines_starting(apph, a)[0])))
    print('anchor R5 string count: %d' % apph.count(O5))
    if ins067 is not None:
        print('anchor R5 string count in 067 insert: %d' % ins067.count(O5))
    print('anchor R1/R2/R5 string counts in block and closing: %d %d %d' % (
        (block + closing).count(A1), (block + closing).count(A2), (block + closing).count(O5)))
    only = apply_one(apph, block, closing, None)
    full = apply_one(apph, block, closing, ins067)
    assert only.count(b'\n') == only.count(b'\r\n') and full.count(b'\n') == full.count(b'\r\n')
    print('POST appH (r3 package, no 067)  ', info(only))
    print('POST appH (067, then r3)        ', info(full))
    if KEY in bib:
        bib2 = bib
    else:
        bib2 = bib + (b'' if bib.endswith(b'\r\n\r\n') else b'\r\n') + bibadd
    assert bib2.count(b'\n') == bib2.count(b'\r\n')
    print('POST bib                       ', info(bib2))
    # removed / added text checks
    assert A2 not in full and b'Two-component blocks and the transplanted selection rule.' in full
    assert full.count(b'Problem~G remains open and PROGRAMME-CONDITIONAL') == apph.count(
        b'Problem~G remains open and PROGRAMME-CONDITIONAL') + (1 if ins067 is not None else 0)
    assert full.count(b'close nothing in Problem~G') == 0 and full.count(b'closes nothing in Problem~G') == 0
    assert b'diagonal-cut' not in full
    assert full.count(rb'at equal row fractions \(u_1=u_2\)') == 1 and b'at fixed fractions the residual' not in full
    assert full.count(rb'holds at leading order for \(\ell_f\ll M_f\)') == 1
    i067 = full.find(H067); ib = full.find(b'Two-component blocks and the transplanted selection rule.')
    ibear = full.find(A5); iH = full.find(A3)
    print('order: Bearing %d < block %d < 067 %d < Problem H %d' % (ibear, ib, i067, iH))
    assert ibear < ib < i067 < iH
    (out / 'appH-microscopic-proofs.tex').write_bytes(full)
    (out / 'appH-microscopic-proofs.block-only.tex').write_bytes(only)
    (out / 'namcg.bib').write_bytes(bib2)
    if not build:
        print('APPLY OK (no build)')
        return
    b = out / 'build'
    if b.exists():
        shutil.rmtree(b)
    b.mkdir()
    for d in ('chapters', 'bib', 'figs', 'frontmatter'):
        shutil.copytree(ROOT / d, b / d, ignore=shutil.ignore_patterns('*.aux'))
    shutil.copy2(ROOT / 'namcg-book7.tex', b / 'namcg-book7.tex')
    for f in ROOT.glob('*.png'):
        shutil.copy2(f, b / f.name)
    for f in ROOT.glob('*.jpg'):
        shutil.copy2(f, b / f.name)
    (b / 'chapters' / 'appH-microscopic-proofs.tex').write_bytes(full)
    (b / 'bib' / 'namcg.bib').write_bytes(bib2)

    def run(cmd):
        return subprocess.run(cmd, cwd=b, capture_output=True, text=True, errors='replace', timeout=1200)

    seq = [['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'],
           ['bibtex', 'namcg-book7'],
           ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex'],
           ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'namcg-book7.tex']]
    pages = '?'
    for cmd in seq:
        p = run(cmd)
        m = re.search(r'Output written on .*?\((\d+) pages', p.stdout)
        if m:
            pages = m.group(1)
        print('%-8s rc=%d %s' % (cmd[0], p.returncode, ('pages=' + pages) if m else ''))
        if cmd[0] == 'pdflatex' and p.returncode != 0:
            print('\n'.join(l for l in p.stdout.splitlines() if l.startswith('!'))[:2000])
            sys.exit('BUILD FAILED')
    log = (b / 'namcg-book7.log').read_text(errors='replace')
    bad = [l for l in log.splitlines() if re.search(
        r"undefined references|Reference `.*' on page .* undefined|Citation `.*' on page .* undefined|"
        r"multiply[- ]defined|There were undefined", l)]
    print('undefined/multiply-defined warnings: %d' % len(bad))
    for l in bad[:10]:
        print('  ' + l)
    blg = (b / 'namcg-book7.blg').read_text(errors='replace')
    warn = [l for l in blg.splitlines() if 'Warning' in l and 'Frenkel2023EdgeModes' in l]
    print('bibtex warnings for Frenkel2023EdgeModes: %d' % len(warn))
    print('BUILD %s pages=%s' % ('PASS' if not bad else 'FAIL', pages))


if __name__ == '__main__':
    main()
