"""081-088 r3: insertion rule, byte contract and applied-copy build (outside the repository).

Usage:
  python -I proposals/local-gpu/081-088-r2/apply_build_r3.py OUTDIR [--build] [--keep]

Reads chapters/appH-microscopic-proofs.tex (read-only), applies the package in memory, writes the
applied copy to OUTDIR (outside the repository). With --build it copies the build inputs to
OUTDIR/build and runs pdflatex, bibtex, pdflatex, pdflatex there and scans the log.
Unless --keep is given, OUTDIR/build is removed at the end (the applied appH copy is kept).

Rule (each anchor must occur exactly once in the live file):
  S1  insert insert_r3.tex (two paragraphs, each followed by one blank CRLF line) immediately before
      the line that starts with  \\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023}
      (that is, after the paragraph \\emph{Coincident copies and the multiplicity reading.});
  S2  in the line that starts with
        These statements are for a compact factor with positive contraction; for a single projector
      replace the clause (first line of clause_r2.txt) by the second line of clause_r2.txt; the
      resulting line equals closing_r2.tex (unchanged in r3);
  S3  in the line that starts with  \\emph{Row length.} If  (the Row length paragraph), replace the
      text in the first line of rowlen_r3.txt (unique in the file and in that line) by its second line.
No other byte changes. bib/ is not touched (no new citation keys).
"""
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
APPH = ROOT / 'chapters' / 'appH-microscopic-proofs.tex'
PRE_SHA = '779bfcac09504722912302eb74299f4ba045dca64c65c166799b7bc3f70f723f'
CRLF = bytes([13, 10])
A1 = b'\\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023}'
A3 = b'\\emph{Row length.} If '
A2 = b'These statements are for a compact factor with positive contraction; for a single projector'
COIN = b'\\emph{Coincident copies and the multiplicity reading.}'


def info(b):
    return '%d B sha256 %s CRLF %d bareLF %d' % (
        len(b), hashlib.sha256(b).hexdigest(), b.count(CRLF), b.count(b'\n') - b.count(CRLF))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1]).resolve()
    assert ROOT not in out.parents and out != ROOT, 'OUTDIR must lie outside the repository'
    out.mkdir(parents=True, exist_ok=True)
    apph = APPH.read_bytes()
    print('PRE  appH', info(apph))
    print('PRE  sha matches recorded pre-hash:', hashlib.sha256(apph).hexdigest() == PRE_SHA)
    ins = (HERE / 'insert_r3.tex').read_bytes()
    clause = (HERE / 'clause_r2.txt').read_bytes().split(CRLF)
    old, new = clause[0], clause[1]
    closing = (HERE / 'closing_r2.tex').read_bytes()
    rl = (HERE / 'rowlen_r3.txt').read_bytes().split(CRLF)
    dold, dnew = rl[0], rl[1]
    for n, b in (('insert_r3.tex', ins), ('closing_r2.tex', closing)):
        assert b.count(b'\n') == b.count(CRLF) and not b.startswith(b'\xef\xbb\xbf'), n
        print('snippet %-15s' % n, info(b))
    lines = apph.split(CRLF)
    i1 = [i for i, l in enumerate(lines) if l.startswith(A1)]
    i2 = [i for i, l in enumerate(lines) if l.startswith(A2)]
    ic = [i for i, l in enumerate(lines) if l.startswith(COIN)]
    i3 = [i for i, l in enumerate(lines) if l.startswith(A3)]
    print('anchor S3 count %d, (d) text count in file %d, in S3 line %d' % (
        len(i3), apph.count(dold), lines[i3[0]].count(dold) if i3 else -1))
    assert len(i3) == 1 and apph.count(dold) == 1 and lines[i3[0]].count(dold) == 1
    assert ins.count(dold) == 0 and ins.count(dnew) == 0
    print('anchor S1 count %d, S2 count %d, clause count in file %d, in S2 line %d' % (
        len(i1), len(i2), apph.count(old), lines[i2[0]].count(old) if i2 else -1))
    assert len(i1) == 1 and len(i2) == 1 and apph.count(old) == 1 and lines[i2[0]].count(old) == 1
    assert len(ic) == 1 and ic[0] + 2 == i1[0] and lines[ic[0] + 1] == b'', 'S1 must follow Coincident copies'
    for a in (A1, A2, old):
        assert ins.count(a) == 0
    blk = ins[:-2].split(CRLF)
    assert blk[-1] == b''
    new_lines = lines[:i1[0]] + blk + lines[i1[0]:]
    j2 = [i for i, l in enumerate(new_lines) if l.startswith(A2)][0]
    new_lines[j2] = new_lines[j2].replace(old, new)
    j3 = [i for i, l in enumerate(new_lines) if l.startswith(A3)][0]
    new_lines[j3] = new_lines[j3].replace(dold, dnew)
    assert new_lines[j2] + CRLF == closing
    full = CRLF.join(new_lines)
    assert full.count(b'\n') == full.count(CRLF)
    # contract: only additions are the insert and the clause change
    assert len(full) == len(apph) + len(ins) + len(new) - len(old) + len(dnew) - len(dold)
    assert full.count(dnew) == 1 and full.count(new) == 1 and full.count(ins) == 1
    assert full.replace(ins, b'', 1).replace(new, old, 1).replace(dnew, dold, 1) == apph
    assert b'29.5' not in ins and b'D_{\\mathrm{eff}}=38.0' in ins
    assert b'diagonal-cut' not in full and b'Missing step paragraph' not in full
    assert full.count(b'Problem~G remains open and PROGRAMME-CONDITIONAL') == apph.count(
        b'Problem~G remains open and PROGRAMME-CONDITIONAL')
    sec = full[full.find(b'\\section{Problem G: HBEV}'):full.find(b'\\section{Problem H')]
    for ref in (b'\\emph{Row length.}', b'\\emph{State and coarse-graining.}',
                b'\\emph{Two-component blocks and the transplanted selection rule.}'):
        assert sec.count(ref) == 1, ref
    print('POST appH', info(full))
    (out / 'appH-microscopic-proofs.tex').write_bytes(full)
    if '--build' not in sys.argv:
        print('APPLY OK (no build)')
        return
    b = out / 'build'
    if b.exists():
        shutil.rmtree(b)
    b.mkdir()
    for d in ('chapters', 'bib', 'figs', 'frontmatter'):
        if (ROOT / d).exists():
            shutil.copytree(ROOT / d, b / d, ignore=shutil.ignore_patterns('*.aux'))
    shutil.copy2(ROOT / 'namcg-book7.tex', b / 'namcg-book7.tex')
    for pat in ('*.png', '*.jpg', '*.sty', '*.cls', '*.bst'):
        for f in ROOT.glob(pat):
            shutil.copy2(f, b / f.name)
    (b / 'chapters' / 'appH-microscopic-proofs.tex').write_bytes(full)

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
    print('BUILD %s pages=%s' % ('PASS' if not bad else 'FAIL', pages))
    if '--keep' not in sys.argv:
        shutil.rmtree(b, ignore_errors=True)
        print('build directory removed:', not b.exists())


if __name__ == '__main__':
    main()
