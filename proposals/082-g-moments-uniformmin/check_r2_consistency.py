"""082 r2 consistency check (read-only): the fenced insert body inside
proposal-r2.md must be byte-identical to insert-r2.tex minus terminal CRLF;
old buggy display absent, corrected display present. Keep output <500 B.
Run: python -I proposals/082-g-moments-uniformmin/check_r2_consistency.py"""
import hashlib
P2 = 'proposals/082-g-moments-uniformmin/proposal-r2.md'
R2 = 'proposals/082-g-moments-uniformmin/insert-r2.tex'
OLD = 'k=1}^{p-1}(D+k)'
NEW = 'k=0}^{p-1}(D+k)'
d = open(P2, 'rb').read().replace(b'\r\n', b'\n')
i = d.index(b'```latex\n')
body = d[i + len(b'```latex\n'):d.index(b'\n```', i + 9)]
rb = open(R2, 'rb').read()[:-2]
ok_body = body == rb
txt = d.decode('utf-8')
ok_old, ok_new = txt.count(OLD) == 0, txt.count(NEW) >= 1
print('%s body sha8 %s insert sha8 %s size %d; old-hits %d new-hits %d'
      % ('PASS' if (ok_body and ok_old and ok_new) else 'FAIL',
         hashlib.sha256(body).hexdigest()[:8],
         hashlib.sha256(rb).hexdigest()[:8], len(rb),
         txt.count(OLD), txt.count(NEW)))
