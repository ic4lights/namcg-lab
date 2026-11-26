"""Verification for proposal 069: duplicate provisional-bookkeeping block in ch10.

Checks (read-only on chapters/):
 1. The ch10 block (lines 331-367) and the ch05 block (lines 324-360): intro
    paragraph and tabular are character-identical; the closing sentences and
    section headings differ in wording.
 2. sec:ch10-table has zero incoming \ref anywhere in chapters/ (label at
    ch10:332 only).
 3. sec:ch5-count incoming \ref sites (expected: ch05:379, ch09:386, ch10:229).
 4. Uniqueness in ch10 of the three anchor strings used by the edit.
 5. sec:ch10-not and sec:ch10-exercises have no incoming \ref (so the ch10
    section-number shift is invisible to all cross-references); no cleveref /
    autoref usage anywhere; no literal "Section~10." hard-coded reference.
Run:  python -I verify_dedup.py   (from the proposal folder; paths relative to repo root)
"""
import io
import re
import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def load(rel):
    raw = io.open(os.path.join(ROOT, rel), 'rb').read()
    assert raw[:3] != b'\xef\xbb\xbf', rel + ': BOM present'
    assert raw.count(b'\n') == raw.count(b'\r\n'), rel + ': not pure CRLF'
    return raw.decode('utf-8').split('\r\n')

ch10 = load('chapters/ch10-lorentz-locking.tex')
ch5 = load('chapters/ch05-lorentz-decomposition.tex')

def L(lines, a, b):
    """1-based inclusive line range."""
    return lines[a - 1:b]

print('== check 1: block comparison ==')
# ch10: heading 331, label 332, intro 334-337, tabular 339-364, closing 366-367
# ch05: heading 324, label 325, intro 327-330, tabular 332-357, closing 359-360
print('ch10 heading :', L(ch10, 331, 331)[0])
print('ch05 heading :', L(ch5, 324, 324)[0])
print('intro identical      :', L(ch10, 334, 337) == L(ch5, 327, 330))
print('tabular identical    :', L(ch10, 339, 364) == L(ch5, 332, 357))
print('closing ch10 366-367 :', ' '.join(L(ch10, 366, 367)))
print('closing ch05 359-360 :', ' '.join(L(ch5, 359, 360)))
print('closing identical    :', L(ch10, 366, 367) == L(ch5, 359, 360))

print()
print('== checks 2-5: cross-file scan ==')
tex = []
for name in sorted(os.listdir(os.path.join(ROOT, 'chapters'))):
    if name.endswith('.tex'):
        tex.append(('chapters/' + name, load('chapters/' + name)))

refs10 = []
refs5 = []
lab10 = []
for rel, lines in tex:
    for i, ln in enumerate(lines, 1):
        if r'\ref{sec:ch10-table}' in ln:
            refs10.append((rel, i))
        if r'\ref{sec:ch5-count}' in ln:
            refs5.append((rel, i))
        if r'\label{sec:ch10-table}' in ln:
            lab10.append((rel, i))
print('incoming \\ref{sec:ch10-table} :', refs10)
print('\\label{sec:ch10-table} sites :', lab10)
print('incoming \\ref{sec:ch5-count}  :', refs5)

shift = {r'sec:ch10-not': 0, r'sec:ch10-exercises': 0, r'sec:ch10-vector': 0,
         r'sec:ch10-diffs': 0}
for rel, lines in tex:
    for i, ln in enumerate(lines, 1):
        for lab in shift:
            if r'\ref{' + lab + '}' in ln:
                shift[lab] += 1
print('incoming refs to labels after the deleted section:', shift)
print('(sec:ch10-diffs precedes the deletion; its number is unaffected.)')

allsrc = '\n'.join(ln for _, ls in tex for ln in ls)
print('cleveref/autoref used anywhere      :',
      bool(re.search(r'\\(usepackage\{cleveref\}|autoref)', allsrc)))
print('hard-coded "Section~10." references :',
      re.findall(r'Section~10\.', allsrc))

print()
print('== check 4: anchor uniqueness in ch10 ==')
for pat in [r'conditional vector row of the provisional sector bookkeeping; it',
            r'\\section\{Provisional sector bookkeeping \(frame/metric sector only\)\}',
            r'No total mode count of the full theory follows from this bookkeeping;']:
    n = sum(1 for ln in ch10 if re.search(pat, ln))
    print('count', n, 'for', pat)

print()
print('== check: the sentence the pointer will attach to (ch10 227-235) ==')
print(' '.join(L(ch10, 227, 235)))

print()
print('ALL CHECKS PRINTED; compare with verify_output.txt')
