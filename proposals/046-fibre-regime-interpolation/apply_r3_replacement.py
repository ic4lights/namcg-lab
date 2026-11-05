"""apply_r3_replacement.py (proposal 046, round 3): applies replacement (d) of review-r2.md to appH_insert.tex, byte
for byte, and nothing else.  The strings are extracted programmatically from review-r2.md, not retyped.  The old string
must occur exactly once and the new string not at all; the result must have the size and sha256 the review states.
Otherwise the script stops without writing."""
import hashlib, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, 'appH_insert.tex')
EXPECT_SHA = '81bb7f1674b176f3c675377154f60fbc79641dde13b39ece9c219786234c9c71'
EXPECT_LEN = 10874

review = open(os.path.join(here, 'review-r2.md'), 'rb').read().decode('utf-8').replace('\r\n', '\n')
m = re.search(r'\(d\) In "Consequence", replace \(exactly one occurrence\)\n`([^`\n]+)`\nwith\n`([^`\n]+)`', review)
assert m, 'replacement (d) not found in review-r2.md'
old, new = m.group(1).encode('ascii'), m.group(2).encode('ascii')

before = open(p, 'rb').read()
out = [f'before: {len(before)} bytes, sha256 {hashlib.sha256(before).hexdigest()}']
assert before.count(old) == 1, ('old count', before.count(old))
assert before.count(new) == 0, 'new already present'
after = before.replace(old, new)
sha = hashlib.sha256(after).hexdigest()
if len(after) != EXPECT_LEN or sha != EXPECT_SHA:
    print('\n'.join(out))
    print(f'MISMATCH: result would be {len(after)} bytes, sha256 {sha}; expected {EXPECT_LEN}, {EXPECT_SHA}. Nothing written.')
    sys.exit(1)
open(p, 'wb').write(after)
reread = open(p, 'rb').read()
out.append(f'(d) old occurrences 1 -> replaced; length change {len(new) - len(old):+d}')
out.append(f'after: {len(reread)} bytes, sha256 {hashlib.sha256(reread).hexdigest()}')
out.append(f'non-ASCII {sum(c > 127 for c in reread)}; CR {reread.count(bytes([13]))}; TAB {reread.count(bytes([9]))}')
out.append(f'matches review-r2 expected bytes and hash: {len(reread) == EXPECT_LEN and hashlib.sha256(reread).hexdigest() == EXPECT_SHA}')
lb, la = before.split(b'\n'), reread.split(b'\n')
out.append('lines changed: ' + str([i + 1 for i, (x, y) in enumerate(zip(lb, la)) if x != y]) + f' of {len(la)}')
text = '\n'.join(out)
print(text)
open(os.path.join(here, 'apply_r3_replacement.out.txt'), 'w', newline='\n').write(text + '\n')
