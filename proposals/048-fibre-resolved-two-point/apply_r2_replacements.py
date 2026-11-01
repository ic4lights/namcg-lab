"""apply_r2_replacements.py (proposal 048, round 2).

Applies R1-R21 of review-r1.md to the round-1 insert, in sequence, and writes appH_insert.tex.
The old and new strings are read as raw text from review-r1.md; nothing is retyped here.

Refuses to write, leaving every file untouched, unless all of these hold:
  - the input is the round-1 insert (sha256 below);
  - exactly R1..R21 are parsed, each line having exactly one " => " between backticked strings;
  - each old string occurs exactly once at its turn, and also exactly once in the round-1 text;
  - the result is ASCII, with no CR and no BOM, and has exactly EXPECTED_CHARS characters.

The round-1 text is kept as appH_insert.r1.tex. If that file exists it is the input, so a re-run from a finished
state recomputes the result and compares it with appH_insert.tex.

Usage: python apply_r2_replacements.py [--check]    (--check never writes)
"""
import hashlib, os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.join(here, 'review-r1.md')
TARGET = os.path.join(here, 'appH_insert.tex')
KEPT_R1 = os.path.join(here, 'appH_insert.r1.tex')
R1_SHA = '6ec4f65732b683bb5320deb5fd54733640b977ebeb39f0f509ab9b379ac87a5c'
EXPECTED_CHARS = 16390
check_only = '--check' in sys.argv[1:]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def refuse(msg):
    print('REFUSED, nothing written:', msg)
    sys.exit(1)


review_bytes = open(REVIEW, 'rb').read()
print('review-r1.md sha256', sha(review_bytes))
pairs = {}
for line in review_bytes.decode('utf-8').split('\n'):
    line = line.rstrip('\r')
    head = re.match(r'^- \*\*R(\d+)\.\*\* ', line)
    if not head:
        continue
    body = line[head.end():]
    if body.count('`') != 4 or body.count('` => `') != 1 or not (body.startswith('`') and body.endswith('`')):
        refuse('R%s is not of the form `old` => `new`' % head.group(1))
    old, new = body[1:-1].split('` => `')
    n = int(head.group(1))
    if n in pairs:
        refuse('R%d appears twice in the review' % n)
    pairs[n] = (old, new)
if sorted(pairs) != list(range(1, 22)):
    refuse('expected R1..R21, parsed %s' % sorted(pairs))

source = KEPT_R1 if os.path.exists(KEPT_R1) else TARGET
r1_bytes = open(source, 'rb').read()
if sha(r1_bytes) != R1_SHA:
    refuse('%s is not the round-1 insert (sha256 %s)' % (os.path.basename(source), sha(r1_bytes)))
r1_text = r1_bytes.decode('ascii')
print('input', os.path.basename(source), 'bytes', len(r1_bytes), 'sha256', sha(r1_bytes))

text = r1_text
for n in range(1, 22):
    old, new = pairs[n]
    in_r1, now = r1_text.count(old), text.count(old)
    if in_r1 != 1 or now != 1:
        refuse('R%d: old string occurs %d times in the round-1 text and %d times at its turn' % (n, in_r1, now))
    text = text.replace(old, new)
    print('R%-2d ok: old once; delta %+d chars' % (n, len(new) - len(old)))

out = text.encode('utf-8')
if any(b >= 128 for b in out):
    refuse('result is not ASCII')
if b'\r' in out or out[:3] == b'\xef\xbb\xbf':
    refuse('result has a CR or a BOM')
if len(text) != EXPECTED_CHARS:
    refuse('result has %d characters, the review states %d' % (len(text), EXPECTED_CHARS))
print('result chars', len(text), 'bytes', len(out), 'ASCII True CR 0 BOM False')
print('result sha256', sha(out))

current = open(TARGET, 'rb').read()
if current == out:
    print('appH_insert.tex already equals the result; nothing written')
elif check_only:
    print('--check: appH_insert.tex differs from the result (sha256 %s); nothing written' % sha(current))
    sys.exit(1)
elif sha(current) != R1_SHA:
    refuse('appH_insert.tex is neither the round-1 insert nor the result (sha256 %s)' % sha(current))
else:
    if not os.path.exists(KEPT_R1):
        with open(KEPT_R1, 'wb') as f:
            f.write(r1_bytes)
        print('kept round-1 text as appH_insert.r1.tex')
    with open(TARGET, 'wb') as f:
        f.write(out)
    print('wrote appH_insert.tex')
