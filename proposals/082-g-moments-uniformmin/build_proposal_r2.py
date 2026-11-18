"""082 r2: assemble proposal-r2.md from proposal-r1.md + new section files,
injecting the insert-r2.tex body byte-exactly (never retyped). Writes only
proposal-r2.md. Run: python -I proposals/082-g-moments-uniformmin/build_proposal_r2.py"""
import hashlib
F = 'proposals/082-g-moments-uniformmin/'


def L(name):
    b = open(F + name, 'rb').read().replace(b'\r\n', b'\n')
    return b.rstrip(b'\n').split(b'\n')


src = L('proposal-r1.md')
body = open(F + 'insert-r2.tex', 'rb').read()
assert len(body) == 2029 and body[-2:] == b'\r\n'
body = body[:-2]


def hdr(h):
    c = [i for i, l in enumerate(src) if l == b'## ' + h]
    assert len(c) == 1, h
    return c[0]


i = [k for k, l in enumerate(src) if l.startswith(b'\\emph{Uniform minimiser')]
assert len(i) == 1 and b'k=0}^{p-1}(D+k)' not in body
assert src[0] == b'# Proposal 082-g-moments-uniformmin, round 1'
src[0] = src[0].replace(b'round 1', b'round 2')
i = [k for k, l in enumerate(src) if b'binom{D+p-1}{p}D^{-p}' in l]
assert len(i) == 1
src[i[0]] = src[i[0]] + b'=D^{-p}\\prod_{k=0}^{p-1}(D+k)'
i = [k for k, l in enumerate(src) if b'shipped as `insert-r1.tex`' in l]
assert len(i) == 1
src[i[0]:i[0] + 1] = [
    b'fenced block below, shipped as `insert-r2.tex` (the F1-corrected body;',
    b'`insert-r1.tex` retained as lineage only, SUPERSEDED FOR INTEGRATION),',
    b'single content line, CRLF,']
src[i[0] + 5] = body
a = hdr(b'Source reading'); c = hdr(b'Research and reasoning')
src[a:c] = L('_p2.md') + [b'']
a = hdr(b'Verification scripts and reproduction pack')
c = hdr(b'Decisions Taken')
src[a:c] = L('_p3.md') + [b''] + L('_p4.md') + [b'']
c = hdr(b'Milestone assessment')
src[c:c] = L('_p5.md') + [b'']
src = src[:-1] + [b''] + L('_p6.md') + [b'']
out = b'\n'.join(src)
open(F + 'proposal-r2.md', 'wb').write(out)
print('BUILT proposal-r2.md bytes %d sha8 %s'
      % (len(out), hashlib.sha256(out).hexdigest()[:8]))
