"""apply_r3_replacements.py (proposal 047, round 3): apply replacements (n), (o), (p) of review-r2.md to appH_insert.tex.

The old and new strings are read from review-r2.md as raw text, so no backslash is interpreted.

  python apply_r3_replacements.py            apply to appH_insert.tex; writes only if the file holds the r2 bytes,
                                             each old string occurs exactly once, and the result has the expected
                                             size, encoding, line endings and sha256
  python apply_r3_replacements.py --verify   write nothing; rebuild from the r2 bytes committed in git and compare
                                             with the current appH_insert.tex
Prints to stdout. Exits non-zero, with the file untouched, on any mismatch.
"""
import hashlib, os, re, subprocess, sys

here = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(os.path.join(here, '..', '..'))
insert_path = os.path.join(here, 'appH_insert.tex')
review_path = os.path.join(here, 'review-r2.md')
R2_SHA = '92464fa5ef88d23f589d2ea203a78cc518050d0faa8c6b65d69ae5aed1c5c9be'
R2_COMMIT = 'b9c8b10'
R3_SHA = 'd722bd481556f125bdd9974762c0f040e970eab24021f887c91889afd2d98d2b'
R3_BYTES = 14281
LABELS = 'nop'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fail(msg):
    print('REFUSED: ' + msg)
    sys.exit(1)


def parse_review():
    text = open(review_path, 'rb').read().decode('utf-8').replace('\r\n', '\n')
    start = text.index('## Corrected snippet')
    end = text.index('## Files', start)
    lines = text[start:end].split('\n')
    pairs = {}
    for i, line in enumerate(lines):
        m = re.match(r'^\(([n-p])\) `(.*)`$', line)
        if not m:
            continue
        lab, old = m.group(1), m.group(2)
        new_line = lines[i + 1]
        if lab in pairs or '`' in old:
            fail(f'({lab}): repeated label or backtick inside the old string')
        if not (new_line.startswith('-> `') and new_line.endswith('`') and new_line.count('`') == 2):
            fail(f'({lab}): new-string line is not one backticked string')
        pairs[lab] = (old, new_line[4:-1])
    if ''.join(sorted(pairs)) != LABELS:
        fail('labels found: ' + ''.join(sorted(pairs)))
    return pairs


def apply_all(r2_text, pairs):
    s = r2_text
    for lab in LABELS:
        old, new = pairs[lab]
        if r2_text.count(old) != 1:
            fail(f'({lab}): old string occurs {r2_text.count(old)} times in the r2 insert')
        if s.count(old) != 1:
            fail(f'({lab}): old string occurs {s.count(old)} times at its turn')
        s = s.replace(old, new)
    for lab in LABELS:
        old, new = pairs[lab]
        if s.count(old) != 0:
            fail(f'({lab}): old string survives in the result')
        if s.count(new) != 1:
            fail(f'({lab}): new string occurs {s.count(new)} times in the result')
    return s


def main():
    verify = '--verify' in sys.argv[1:]
    pairs = parse_review()
    print('review-r2.md sha256', sha(open(review_path, 'rb').read()))
    for lab in LABELS:
        old, new = pairs[lab]
        print(f'({lab}) old {len(old)} chars, new {len(new)} chars, delta {len(new) - len(old):+d}')
    current = open(insert_path, 'rb').read()
    if verify:
        rel = 'proposals/047-lichnerowicz-torsion-closed-forms/appH_insert.tex'
        r2 = subprocess.run(['git', '-C', repo, 'show', f'{R2_COMMIT}:{rel}'], capture_output=True, check=True).stdout
    else:
        r2 = current
    if sha(r2) != R2_SHA:
        fail(f'input sha256 {sha(r2)} is not the r2 insert; replacements may already be applied')
    result = apply_all(r2.decode('ascii'), pairs).encode('ascii')
    print('r2 bytes', len(r2), 'sha256', sha(r2))
    print('r3 bytes', len(result), 'sha256', sha(result))
    print('CR', result.count(b'\r'), 'non-ASCII', sum(c > 127 for c in result))
    if len(result) != R3_BYTES or sha(result) != R3_SHA or b'\r' in result:
        fail('result does not match the expected size, line endings and sha256')
    if verify:
        same = result == current
        print('current appH_insert.tex equals rebuild from r2 and review:', same)
        sys.exit(0 if same else 1)
    with open(insert_path, 'wb') as f:
        f.write(result)
    print('WROTE appH_insert.tex; all 3 replacements applied exactly once')


main()
