"""normalize_insert.py - rewrite insert-r1.tex as ONE content line + one terminal CRLF.

Run from the repository root:  python -I proposals/077-g-selrule-copyinv/normalize_insert.py
Reads the file, collapses all line-endings, requires exactly one non-empty line,
and writes back content + b'\r\n'. Prints size and sha256 of file and content.
"""
import hashlib

p = 'proposals/077-g-selrule-copyinv/insert-r1.tex'
raw = open(p, 'rb').read()
lines = raw.replace(b'\r\n', b'\n').split(b'\n')
content = [l for l in lines if l.strip() != b'']
assert len(content) == 1, 'expected exactly one non-empty line, got %d' % len(content)
c = content[0]
assert all(b < 128 for b in c), 'non-ASCII byte'
new = c + b'\r\n'
open(p, 'wb').write(new)
print('normalized: content %d B / file %d B' % (len(c), len(new)))
print('file sha256     %s' % hashlib.sha256(new).hexdigest())
print('content sha256  %s' % hashlib.sha256(c).hexdigest())
