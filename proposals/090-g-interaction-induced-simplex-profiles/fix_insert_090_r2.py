import hashlib, html
# Round-2 mechanical quantifier fix (review-r1 F1, F2, F3). The replacement clauses are EXTRACTED
# from review-r1.md bytes with html.unescape only (no retyping); the F1 clause is cut at its
# "strictly concave" start so the shared sentence prefix stays as shipped. Byte surgery on
# insert-r1.tex; r1 frozen. Run from repository root.
P = 'proposals/090-g-interaction-induced-simplex-profiles/'
raw = open(P + 'insert-r1.tex', 'rb').read()
assert len(raw) == 3735 and hashlib.sha256(raw).hexdigest()[:8] == '3a6a69c4'
assert raw.endswith(b'\r\n')
rev = html.unescape(open(P + 'review-r1.md', 'r', encoding='utf-8').read())
i = rev.index('e.g. "') + len('e.g. "'); j = rev.index('". No new mathematics')
NEW1 = rev[i:j].encode('ascii'); NEW1 = NEW1[NEW1.index(b'strictly concave'):]
i = rev.index('Action: write "') + len('Action: write "'); j = rev.index('". (Same sentence')
NEW2 = rev[i:j].encode('ascii')
i = rev.index('optional parenthetical "') + len('optional parenthetical "'); j = rev.index(')"', i)
NEW3 = (rev[i:j] + ") with log-weight curvature").encode("ascii")  # review clause + anchor
assert NEW1.startswith(b'strictly concave whenever') and NEW2.startswith(b'at any deformation strength')
assert NEW3.startswith(b'(at') and NEW3.endswith(b'barycenter) with log-weight curvature')
u = lambda s: s.encode('ascii')
OLD1 = u(r'strictly concave for \(a\ge 1\), so for \(a>1\) it has exactly one stationary profile there')
OLD2 = u('at any deformation strength')
OLD3 = u('with log-weight curvature')
out = raw
for OLD, NEW, tag in ((OLD1, NEW1, 'F1'), (OLD2, NEW2, 'F2'), (OLD3, NEW3, 'F3')):
    assert out.count(OLD) == 1, tag
    out = out.replace(OLD, NEW, 1)
    assert out.count(NEW) == 1 and out.count(OLD) - (1 if OLD in NEW else 0) == 0, tag
assert out.endswith(b'\r\n')
body = out[:-2]
assert body.decode('ascii') and b'\r' not in body and b'\n' not in body and not [c for c in body if c < 32]
assert body.count(b'\\(') == body.count(b'\\)')
open(P + 'insert-r2.tex', 'wb').write(out)
print('insert-r2.tex bytes:', len(out), 'sha8:', hashlib.sha256(out).hexdigest()[:8])
print('delta:', len(out) - len(raw), '= F1', len(NEW1) - len(OLD1), '+ F2', len(NEW2) - len(OLD2), '+ F3', len(NEW3) - len(OLD3))
print('paren-balance:', body.count(b'\\('), body.count(b'\\)'))
print('FIX R2 OK')
