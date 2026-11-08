#!/usr/bin/env python3
"""058 report-mode apply check.  For each manuscript file, reads the edit file (LF, blocks
@@OLD / @@NEW / @@END), converts each string to CRLF, checks that every OLD occurs exactly once and
every NEW occurs zero times in the baseline, applies the replacements in memory, and prints baseline
and result bytes/sha256 and CRLF / bare-LF counts.  With an output directory OUTSIDE the repository
it writes the would-be files there (never inside the repository; refuses to overwrite).
Usage: python apply_check.py [OUTPUT_DIR]
"""
import sys, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CR = bytes([13]); LF = bytes([10]); CRLF = CR + LF
FILES = [
    ('ch13-cores-galaxies.tex', 'ch13_edits.txt'),
    ('ch16-falsifiers.tex', 'ch16_edits.txt'),
    ('appE-rar-bridge.tex', 'appE_edits.txt'),
    ('appI-gaia-wide.tex', 'appI_edits.txt'),
]

def sha(b):
    return hashlib.sha256(b).hexdigest()

def counts(b):
    return b.count(CRLF), b.count(LF) - b.count(CRLF)

def parse(path):
    raw = open(path, 'rb').read()
    assert CR not in raw, path + ' has CR'
    assert all(c < 128 for c in raw), path + ' not ASCII'
    pairs, mode, old, new = [], None, [], []
    for line in raw.split(LF):
        if line == b'@@OLD':
            mode, old, new = 'old', [], []
        elif line == b'@@NEW':
            mode = 'new'
        elif line == b'@@END':
            pairs.append((CRLF.join(old), CRLF.join(new)))
            mode = None
        elif mode == 'old':
            old.append(line)
        elif mode == 'new':
            new.append(line)
    for o, n in pairs:
        for s in (o, n):
            assert all(l == l.rstrip(b' \t') for l in s.split(CRLF)), 'trailing whitespace'
    return pairs

def main():
    out = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
    if out and out.lower().startswith(ROOT.lower()):
        sys.exit('output inside the repository; refusing')
    ok_all = True
    for tex, ed in FILES:
        p = os.path.join(ROOT, 'chapters', tex)
        a = open(p, 'rb').read()
        print('==', tex)
        print('  baseline', len(a), 'bytes sha256', sha(a), ' CRLF, bare LF:', counts(a))
        new = a
        for i, (o, n) in enumerate(parse(os.path.join(HERE, ed)), 1):
            co, cn = a.count(o), a.count(n)
            line = a[:a.find(o)].count(LF) + 1 if co else None
            print('  edit %d: old count %d (line %s), new count in baseline %d' % (i, co, line, cn))
            if co != 1 or cn != 0:
                ok_all = False
                continue
            new = new.replace(o, n, 1)
        print('  result  ', len(new), 'bytes sha256', sha(new), ' CRLF, bare LF:', counts(new))
        if counts(new)[1] != counts(a)[1]:
            ok_all = False
            print('  bare-LF count changed')
        if out:
            os.makedirs(out, exist_ok=True)
            q = os.path.join(out, tex)
            if os.path.exists(q):
                sys.exit('output exists; refusing to overwrite ' + q)
            open(q, 'wb').write(new)
            print('  wrote', q)
    print('ALL CHECKS PASS' if ok_all else 'CHECK FAILURE')

if __name__ == '__main__':
    main()
