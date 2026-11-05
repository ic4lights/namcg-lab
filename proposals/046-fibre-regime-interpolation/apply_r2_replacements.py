"""apply_r2_replacements.py (proposal 046, round 2): applies replacements (a), (b), (c) of review-r1.md to
appH_insert.tex, byte for byte, and nothing else.  Each old string must occur exactly once, and each new string
must not occur yet; otherwise the script stops without writing.  Records hashes and the changed spans."""
import difflib, hashlib, os
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, 'appH_insert.tex')
REPL = [
    ('a', r'which fails for every \(M\) in the Poisson limit.',
          r'which, at fixed \(M\), fails as \(n\to\infty\), since the sum grows as \(2\ln n\).'),
    ('b', r'the weight \(\beta_X\) is close to one and the fibre trace of the preceding paragraph applies.',
          r'the weight \(\beta_X\) is of order one (it tends to one as \(n\) grows) and the fibre trace of the preceding paragraph is the leading reading.'),
    ('c', r'Within these computations no open range of the scale of \(K\) gives a single Einstein coefficient on the five traceless polarisations with \(c_A=c_T\); isolated values',
          r'Within these computations no open range of the scale of \(K\) gives a single Einstein coefficient on the five traceless polarisations with \(c_A=c_T\); the range \(M\sim\coth^2\tau\), where the first-order torsion parameter is of order one, is not computed, and isolated values'),
]
old_b = open(p, 'rb').read()
s = old_b.decode('utf-8')
out = [f'before: {len(old_b)} bytes, sha256 {hashlib.sha256(old_b).hexdigest()}']
new_s = s
for tag, old, new in REPL:
    assert new_s.count(old) == 1, (tag, 'old count', new_s.count(old))
    assert new_s.count(new) == 0, (tag, 'new already present')
    new_s = new_s.replace(old, new)
    out.append(f'({tag}) old occurrences 1 -> replaced; length change {len(new) - len(old):+d}')
new_b = new_s.encode('utf-8')
open(p, 'wb').write(new_b)
out.append(f'after: {len(new_b)} bytes, sha256 {hashlib.sha256(new_b).hexdigest()}')
sm = difflib.SequenceMatcher(None, s.split(' '), new_s.split(' '), autojunk=False)
n = sum(1 for op in sm.get_opcodes() if op[0] != 'equal')
out.append(f'word-level changed spans between before and after: {n}')
lines_before, lines_after = s.split('\n'), new_s.split('\n')
out.append('lines changed: ' + str([i + 1 for i, (x, y) in enumerate(zip(lines_before, lines_after)) if x != y]) + f' of {len(lines_after)}')
text = '\n'.join(out)
print(text)
open(os.path.join(here, 'apply_r2_replacements.out.txt'), 'w', newline='\n').write(text + '\n')
