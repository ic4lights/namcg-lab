"""051 round 2: apply R1-R17 of review-r1.md to appH_insert.tex, verbatim and in order.

The strings are read raw, as bytes, from review-r1.md.  Each old string must occur exactly once at its turn.
Nothing is written unless all seventeen apply and the result has the size and sha256 stated by the task.
A second run is refused: appH_insert.r1.tex must not exist and appH_insert.tex must still have the r1 sha256.
The r1 bytes are kept as appH_insert.r1.tex.  No backslash sequence is interpreted anywhere here.
"""
import hashlib
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.join(here, 'review-r1.md')
INSERT = os.path.join(here, 'appH_insert.tex')
KEEP = os.path.join(here, 'appH_insert.r1.tex')
R1_SHA = '13c124fa6bc0465f17a014d6e3694f8d78af909233c699093adbce3ecd2e69b2'
R1_LEN = 12560
R2_SHA = 'b6ccbf5f8cbd2848413c3c1fddb7a6c112e52c103262c307d593c5cb45ef86dd'
R2_LEN = 14148


def sha(b):
    return hashlib.sha256(b).hexdigest()


class Refused(Exception):
    pass


def read_replacements(review_bytes):
    old_re = re.compile(rb'^\*\*R(\d+)\.\*\* Old: `(.*)`\r?$', re.M)
    new_re = re.compile(rb'^New: `(.*)`\r?$', re.M)
    olds = [(int(m.group(1)), m.group(2), m.end()) for m in old_re.finditer(review_bytes)]
    news = [(m.group(1), m.start()) for m in new_re.finditer(review_bytes)]
    if [o[0] for o in olds] != list(range(1, 18)):
        raise Refused('old strings are not exactly R1..R17 in order: %r' % [o[0] for o in olds])
    if len(news) != 17:
        raise Refused('expected 17 new strings, found %d' % len(news))
    reps = []
    for (n, old, end), (new, start) in zip(olds, news):
        if not (end < start and review_bytes[end:start].strip() == b''):
            raise Refused('R%d: its New line does not follow its Old line' % n)
        reps.append((n, old, new))
    return reps


def apply_all(text, reps):
    for n, old, new in reps:
        c = text.count(old)
        print('R%-2d old %4d bytes, new %4d bytes, count at its turn %d' % (n, len(old), len(new), c))
        if c != 1:
            raise Refused('R%d: old string occurs %d times at its turn' % (n, c))
        text = text.replace(old, new)
    return text


def main():
    if os.path.exists(KEEP):
        raise Refused('appH_insert.r1.tex exists: already applied')
    cur = open(INSERT, 'rb').read()
    if sha(cur) != R1_SHA or len(cur) != R1_LEN:
        raise Refused('appH_insert.tex is not the r1 bytes: %s, %d bytes' % (sha(cur), len(cur)))
    reps = read_replacements(open(REVIEW, 'rb').read())
    backslash_apostrophe = bytes([92, 39])
    print('R4 old contains backslash-apostrophe:', backslash_apostrophe in reps[3][1])
    if backslash_apostrophe not in reps[3][1]:
        raise Refused('R4 old string lost its backslash-apostrophe')

    bad = [(reps[0][0], reps[0][1] + b'x', reps[0][2])]
    try:
        print('self-test on a mutated old string:')
        apply_all(cur, bad)
    except Refused as e:
        print('  refused as required:', e)
    else:
        raise Refused('self-test: a mutated old string was accepted')

    print('applying:')
    out = apply_all(cur, reps)
    print('result', len(out), 'bytes, sha256', sha(out))
    print('ascii', all(b < 128 for b in out), '; CR', out.count(b'\r'), '; BOM', out[:3] == b'\xef\xbb\xbf')
    if out.count(b'\r') or not all(b < 128 for b in out):
        raise Refused('result is not LF ASCII')
    if len(out) != R2_LEN or sha(out) != R2_SHA:
        raise Refused('result differs from the expected %d bytes, %s' % (R2_LEN, R2_SHA))
    with open(KEEP, 'xb') as f:
        f.write(cur)
    with open(INSERT, 'wb') as f:
        f.write(out)
    print('kept r1 bytes:', sha(open(KEEP, 'rb').read()) == R1_SHA)
    print('wrote appH_insert.tex:', sha(open(INSERT, 'rb').read()) == R2_SHA)
    print('DONE')


if __name__ == '__main__':
    try:
        main()
    except Refused as e:
        print('REFUSED, nothing written:', e)
        sys.exit(2)
