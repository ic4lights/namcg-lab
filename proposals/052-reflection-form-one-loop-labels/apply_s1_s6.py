"""052 r3: applies S1-S5 to appH_insert.tex and appends S6 to new_bib_entries.bib, with every string read raw from review-r2.md.

Each old string must occur exactly once at its turn. All results are computed and checked against the hashes before anything is
written; on any mismatch nothing is written and the exit code is 1. A second run is refused, since the inputs then no longer have
the r2 hashes and the kept r2 copies already exist. The r2 bytes are kept as appH_insert.r2.tex and new_bib_entries.r2.bib."""
import hashlib
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
INS, BIB = os.path.join(here, 'appH_insert.tex'), os.path.join(here, 'new_bib_entries.bib')
INS_R2, BIB_R2 = os.path.join(here, 'appH_insert.r2.tex'), os.path.join(here, 'new_bib_entries.r2.bib')
INS_IN = (16413, '4bacb6ee304e94af190d3bd88647dbed5d48bb6368551004030c227436692838')
BIB_IN = (2198, '81584d933ad25611bcf741b3f6913f31ab678b004f8f0ccd6f477eeff3d08cdc')
INS_OUT = (16814, '444aaf5ddb42c266f890f7b20eef4e7eb2279dd586ee18096eae9d0d578242aa')
BIB_OUT = (2563, '5c771b380c9286b066002297ef8b0b6a674180b05092219613230f5ccddb8f4f')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def refuse(msg):
    print('REFUSED, nothing written:', msg)
    sys.exit(1)


def rd(p):
    with open(p, 'rb') as f:
        return f.read()


for p in (INS_R2, BIB_R2):
    if os.path.exists(p):
        refuse('kept copy already exists: ' + os.path.basename(p))
ins, bib, review = rd(INS), rd(BIB), rd(os.path.join(here, 'review-r2.md'))
if (len(ins), sha(ins)) != INS_IN:
    refuse('appH_insert.tex is not the r2 bytes: %d %s' % (len(ins), sha(ins)))
if (len(bib), sha(bib)) != BIB_IN:
    refuse('new_bib_entries.bib is not the r2 bytes: %d %s' % (len(bib), sha(bib)))
print('inputs: insert', INS_IN, 'bib', BIB_IN, 'CR', ins.count(b'\r'), bib.count(b'\r'), '; review-r2.md CR', review.count(b'\r'), 'sha256', sha(review))
if review.count(b'\r'):
    refuse('review-r2.md has CR bytes')

pairs = re.findall(rb'\*\*S(\d) Old:\*\* `([^`\n]+)`\n\*\*New:\*\* `([^`\n]+)`\n', review)
if [int(p[0]) for p in pairs] != [1, 2, 3, 4, 5]:
    refuse('could not parse S1-S5 in order: %r' % [p[0] for p in pairs])

cur = ins
for n, old, new in pairs:
    c = cur.count(old)
    print('S%s: old count at its turn %d; count in the r2 bytes %d; lengths %d -> %d; delta %+d' % (n.decode(), c, ins.count(old), len(old), len(new), len(new) - len(old)))
    if c != 1:
        refuse('S%s old string occurs %d times at its turn' % (n.decode(), c))
    cur = cur.replace(old, new)
print('insert result', len(cur), sha(cur), 'ASCII', all(b < 128 for b in cur), 'CR', cur.count(b'\r'))
if (len(cur), sha(cur)) != INS_OUT or cur.count(b'\r') or not all(b < 128 for b in cur):
    refuse('insert result differs from the expected %r' % (INS_OUT,))

m = re.findall(rb'\*\*S6: append to `new_bib_entries\.bib`, after one blank line:\*\*\n```\n(.*?\n)```\n', review, re.S)
if len(m) != 1:
    refuse('could not parse S6, %d matches' % len(m))
entry = m[0]
if not bib.endswith(b'}\n') or bib.endswith(b'\n\n'):
    refuse('bib file does not end in a single newline')
newbib = bib + b'\n' + entry
print('S6: entry bytes', len(entry), '; bib result', len(newbib), sha(newbib), 'CR', newbib.count(b'\r'))
if (len(newbib), sha(newbib)) != BIB_OUT or newbib.count(b'\r'):
    refuse('bib result differs from the expected %r' % (BIB_OUT,))

for p, b in ((INS_R2, ins), (BIB_R2, bib), (INS, cur), (BIB, newbib)):
    with open(p, 'wb') as f:
        f.write(b)
print('WRITTEN: appH_insert.r2.tex, new_bib_entries.r2.bib (r2 bytes); appH_insert.tex, new_bib_entries.bib (r3 bytes)')
