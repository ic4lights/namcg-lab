#!/usr/bin/env python3
"""Build insert-r2.tex from insert-r1.tex by the three gatekeeper substitutions F1-F3
(review-r1 Corrected snippet). Asserts each old string occurs exactly once, the old/new
byte-difference accounts exactly for the size change, and the result keeps the hygiene
contract: ASCII, single content line + terminal CRLF, one \\emph{} header, no $ [ ] \\cite
\\ref \\label \\eqref, banned-word count 0 except the single closing idiom.
Writes only insert-r2.tex inside this proposal folder."""
import hashlib, os, re
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, 'insert-r1.tex'), 'rb').read().decode('ascii')

F1_old = (r"- for sorted nonzero eigenvalues the multiplicity of each extreme value is "
          r"strictly below \(q\) at genuine mismatch, so one of its two defining gaps is "
          r"then strictly positive -")
F1_new = (r"- each pair contributes one negative and one positive element, their product "
          r"being \(-4n_f<0\), so the \(q\) smallest sorted eigenvalues are exactly the "
          r"lower pair elements and the two defining gaps are the spreads of the lower and "
          r"upper elements, which vanish together only when all pairs \((h_f,n_f)\) coincide -")
F2_old = r"and \(1\) at equal depths (exact rational arithmetic)"
F2_new = r"and \(1\) at equal depths \(2\) (exact rational arithmetic)"
F3_old = r"exactly as the two paragraphs above"
F3_new = r"exactly as the second and third paragraphs above"

out = src
for name, old, new in (("F1", F1_old, F1_new), ("F2", F2_old, F2_new), ("F3", F3_old, F3_new)):
    n = out.count(old)
    assert n == 1, (name, 'old count', n)
    out = out.replace(old, new, 1)
    assert out.count(new) == 1 and out.count(old) == 0, (name, 'new count')

expected_delta = sum(len(n) - len(o) for _, o, n in
                     (("F1", F1_old, F1_new), ("F2", F2_old, F2_new), ("F3", F3_old, F3_new)))
assert len(out) - len(src) == expected_delta, (len(out) - len(src), expected_delta)

b = out.encode('ascii')                      # raises if any non-ASCII byte appears
assert b.endswith(b'\r\n') and b.count(b'\n') == 1 and b.count(b'\r') == 1
assert b.count(b'\\emph{') == 1
for tok in (b'$', b'[', b']', b'\\cite', b'\\ref', b'\\label', b'\\eqref'):
    assert b.count(tok) == 0, tok
text_l = out.lower()
banned = [w for w in ('status', 'priority', 'completion', 'open', 'critical',
                      'programme', 'derived') if w in text_l]
assert banned == [], banned
assert text_l.count('they close nothing in problem~g.') == 1

dst = os.path.join(D, 'insert-r2.tex')
open(dst, 'wb').write(b)
print('insert-r2 size=%d sha256=%s' % (len(b), hashlib.sha256(b).hexdigest()))
print('size delta=%d (expected %d)' % (len(b) - len(src), expected_delta))
print('banned-word count=0 closing-idiom count=1 emph=1 content-lines=1 terminalCRLF=True')
