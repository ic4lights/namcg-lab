"""052 r2: apply R1-R13 and the two bib entries of review-r1.md, byte for byte.

Reads every old string, new string and the bib block raw from review-r1.md, and types none of them here.
Each old string must occur exactly once at its turn, in the order R1, ..., R13.  Everything is computed in memory and checked
against the sizes and sha256 stated in the review before a byte is written.  On any mismatch nothing is written.
Refuses a second run: appH_insert.r1.tex is created exclusively, and the input insert must still hash to the r1 value."""
import hashlib
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
R1_SHA = '8e71a47cd10873e65bf7d188efba1ac89565ffdc0a0bb2f412619c0289aeb1b8'
R1_BIB_SHA = 'd906855f4959c3f866cd06007dc1cf7b2fa60fc9a0cab514f7ed87e0cb3e46ad'
OUT_SHA = '4bacb6ee304e94af190d3bd88647dbed5d48bb6368551004030c227436692838'
OUT_LEN = 16413
OUT_LEN_CRLF = 16440
BIB_SHA = '81584d933ad25611bcf741b3f6913f31ab678b004f8f0ccd6f477eeff3d08cdc'
BIB_LEN = 2198


def path(n):
    return os.path.join(here, n)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def refuse(msg):
    print('REFUSED, nothing written:', msg)
    sys.exit(1)


if os.path.exists(path('appH_insert.r1.tex')) or os.path.exists(path('new_bib_entries.r1.bib')):
    refuse('r1 copy already exists, so this script has already run')
ins = open(path('appH_insert.tex'), 'rb').read()
bib = open(path('new_bib_entries.bib'), 'rb').read()
if sha(ins) != R1_SHA:
    refuse('input insert is not the r1 bytes: ' + sha(ins))
if sha(bib) != R1_BIB_SHA:
    refuse('input bib is not the r1 bytes: ' + sha(bib))
rev = open(path('review-r1.md'), 'rb').read()
if b'\r' in rev:
    refuse('review-r1.md has CR bytes')
pairs = re.findall(rb'^\*\*R(\d+) Old:\*\* `([^\n]*)`\n\*\*New:\*\* `([^\n]*)`$', rev, re.M)
if [int(p[0]) for p in pairs] != list(range(1, 14)):
    refuse('did not parse R1..R13 in order: ' + str([p[0] for p in pairs]))
out = ins
for num, old, new in pairs:
    n_before = ins.count(old)
    n_turn = out.count(old)
    print('R%s old %4d bytes, new %4d bytes; count in r1 %d, count at its turn %d' % (num.decode(), len(old), len(new), n_before, n_turn))
    if n_turn != 1:
        refuse('R%s old string occurs %d times at its turn' % (num.decode(), n_turn))
    if not all(b < 128 for b in new):
        refuse('R%s new string is not ASCII' % num.decode())
    out = out.replace(old, new)
print('insert result', len(out), 'bytes; sha256', sha(out))
if len(out) != OUT_LEN or sha(out) != OUT_SHA:
    refuse('insert result differs from the review')
if b'\r' in out or not all(b < 128 for b in out):
    refuse('insert result is not ASCII LF')
if len(out.replace(b'\n', b'\r\n')) != OUT_LEN_CRLF:
    refuse('CRLF size differs from the review')
m = re.search(rb'New bib entries, appended.*?\n```\n(.*?)\n```\n', rev, re.S)
if not m:
    refuse('bib block not found')
newbib = bib + b'\n' + m.group(1) + b'\n'
print('bib result', len(newbib), 'bytes; sha256', sha(newbib))
if len(newbib) != BIB_LEN or sha(newbib) != BIB_SHA:
    refuse('bib result differs from the review')
with open(path('appH_insert.r1.tex'), 'xb') as f:
    f.write(ins)
with open(path('new_bib_entries.r1.bib'), 'xb') as f:
    f.write(bib)
with open(path('appH_insert.tex'), 'wb') as f:
    f.write(out)
with open(path('new_bib_entries.bib'), 'wb') as f:
    f.write(newbib)
print('WRITTEN: appH_insert.r1.tex, new_bib_entries.r1.bib, appH_insert.tex, new_bib_entries.bib')
