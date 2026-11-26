"""082 r2: assemble proposal-r2.md from proposal-r1.md + verified r2 fragments
(_p1,_p2,_q3,_p4,_p5,_p6), injecting the insert-r2.tex body byte-exactly
(never retyped). Corrected rebuild of build_proposal_r2.py, which was left
broken (inverted body-display assertion L26; fence written at wrong offset
L38; final Special-instructions line dropped L46). Writes only proposal-r2.md.
Run: python -I proposals/082-g-moments-uniformmin/build_proposal_r2_v2.py"""
import hashlib
F = 'proposals/082-g-moments-uniformmin/'
OLD, NEW = b'k=1}^{p-1}(D+k)', b'k=0}^{p-1}(D+k)'


def L(name):
    b = open(F + name, 'rb').read().replace(b'\r\n', b'\n')
    return b.rstrip(b'\n').split(b'\n')


src = L('proposal-r1.md')
body = open(F + 'insert-r2.tex', 'rb').read()
assert len(body) == 2029 and body[-2:] == b'\r\n' and body.count(b'\n') == 1
body = body[:-2]
assert body.count(OLD) == 0 and body.count(NEW) == 1
assert src[0] == b'# Proposal 082-g-moments-uniformmin, round 1'


def one(pat):
    c = [k for k, l in enumerate(src) if pat in l]
    assert len(c) == 1, pat
    return c[0]


def hdr(h):
    c = [i for i, l in enumerate(src) if l == b'## ' + h]
    assert len(c) == 1, h
    return c[0]


src[0:hdr(b'Target and status')] = L('_p1.md') + [b'']
src[one(b'binom{D+p-1}{p}D^{-p}')] += b'=D^{-p}\\prod_{k=0}^{p-1}(D+k)'
i = one(b'shipped as `insert-r1.tex`')
src[i:i + 1] = [b'the fenced block below, shipped as `insert-r2.tex` (the',
                b'F1-corrected body; `insert-r1.tex` retained as lineage only,',
                b'SUPERSEDED FOR INTEGRATION), single content line, CRLF,']
src[one(b'\\emph{Uniform minimiser')] = body
a, c = hdr(b'Source reading'), hdr(b'Research and reasoning')
src[a:c] = L('_p2.md') + [b'']
a, c = hdr(b'Verification scripts and reproduction pack'), hdr(b'Decisions Taken')
src[a:c] = L('_q3.md') + [b''] + L('_p4.md') + [b'']
m = hdr(b'Milestone assessment')
src[m:m] = L('_p5.md') + [b'']
src += [b''] + L('_p6.md') + [b'']
out = b'\n'.join(src)
assert out.count(OLD) == 0 and out.count(NEW) >= 1 and out.count(b'```') == 2
open(F + 'proposal-r2.md', 'wb').write(out)
print('BUILT proposal-r2.md bytes %d sha8 %s old-hits 0 new-hits %d'
      % (len(out), hashlib.sha256(out).hexdigest()[:8], out.count(NEW)))
