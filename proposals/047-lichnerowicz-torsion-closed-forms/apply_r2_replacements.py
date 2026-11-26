"""apply_r2_replacements.py (proposal 047, round 2): apply replacements (a)-(m) of review-r1.md to appH_insert.tex.

The old and new strings are read from review-r1.md as raw text, so no backslash is interpreted.

  python apply_r2_replacements.py            apply to appH_insert.tex; writes only if the file holds the r1 bytes
                                             and every check passes
  python apply_r2_replacements.py --verify   write nothing; rebuild from the r1 bytes committed in git and compare
                                             with the current appH_insert.tex
Prints to stdout. Exits non-zero, with the file untouched, on any mismatch.
"""
import hashlib, os, re, subprocess, sys

here = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(os.path.join(here, '..', '..'))
insert_path = os.path.join(here, 'appH_insert.tex')
review_path = os.path.join(here, 'review-r1.md')
R1_SHA = 'f1ce7fdae8cb3d7291867ed5ba01f1a7f1997925dec42fae05d9856212506efa'
R1_COMMIT = 'c930d87'
LABELS = 'abcdefghijklm'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fail(msg):
    print('REFUSED: ' + msg)
    sys.exit(1)


def parse_review():
    text = open(review_path, 'rb').read().decode('utf-8').replace('\r\n', '\n')
    start = text.index('### Required replacements')
    end = text.index('r2 must apply exactly these', start)
    lines = text[start:end].split('\n')
    pairs, label = {}, None
    for i, line in enumerate(lines):
        m = re.match(r'^\(([a-m])\) ', line)
        if m:
            label = m.group(1)
        if line.startswith('-> `'):
            if label is None or label in pairs:
                fail(f'unexpected replacement line {i} after label {label}')
            if not line.endswith('`') or line.count('`') != 2:
                fail(f'({label}): new-string line is not one backticked string')
            prev = lines[i - 1]
            prev = re.sub(r'^\([a-m]\) ', '', prev)
            if not (prev.startswith('`') and prev.endswith('`') and prev.count('`') == 2):
                fail(f'({label}): old-string line is not one backticked string')
            pairs[label] = (prev[1:-1], line[4:-1])
    if ''.join(sorted(pairs)) != LABELS:
        fail('labels found: ' + ''.join(sorted(pairs)))
    return pairs


def apply_all(r1_text, pairs):
    s = r1_text
    for lab in LABELS:
        old, new = pairs[lab]
        if r1_text.count(old) != 1:
            fail(f'({lab}): old string occurs {r1_text.count(old)} times in the r1 insert')
        if s.count(old) != 1:
            fail(f'({lab}): old string occurs {s.count(old)} times at its turn')
        s = s.replace(old, new)
    for lab in LABELS:
        old, new = pairs[lab]
        if s.count(old) != 0:
            fail(f'({lab}): old string survives in the result')
        if s.count(new) != 1:
            fail(f'({lab}): new string occurs {s.count(new)} times in the result')
    expected = len(r1_text) + sum(len(n) - len(o) for o, n in pairs.values())
    if len(s) != expected:
        fail(f'length {len(s)} differs from expected {expected}')
    return s


def main():
    verify = '--verify' in sys.argv[1:]
    pairs = parse_review()
    print('review-r1.md sha256', sha(open(review_path, 'rb').read()))
    for lab in LABELS:
        old, new = pairs[lab]
        print(f'({lab}) old {len(old)} chars, new {len(new)} chars, delta {len(new) - len(old):+d}')
    current = open(insert_path, 'rb').read()
    if verify:
        rel = 'proposals/047-lichnerowicz-torsion-closed-forms/appH_insert.tex'
        r1 = subprocess.run(['git', '-C', repo, 'show', f'{R1_COMMIT}:{rel}'], capture_output=True, check=True).stdout
    else:
        r1 = current
    if sha(r1) != R1_SHA:
        fail(f'input sha256 {sha(r1)} is not the r1 insert; replacements may already be applied')
    r1_text = r1.decode('ascii')
    result = apply_all(r1_text, pairs).encode('ascii')
    print('r1 bytes', len(r1), 'sha256', sha(r1))
    print('r2 bytes', len(result), 'sha256', sha(result))
    if verify:
        same = result == current
        print('current appH_insert.tex equals rebuild from r1 and review:', same)
        sys.exit(0 if same else 1)
    with open(insert_path, 'wb') as f:
        f.write(result)
    print('WROTE appH_insert.tex; all 13 replacements applied exactly once')


main()
