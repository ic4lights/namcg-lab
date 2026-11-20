# 094 simulate v2: read-only splice simulation with hard PRE/POST asserts; prints, never writes
# (v1: wrongly required zero triple-CRLF globally - appH already contains 3; v2 compares counts)
import hashlib
b = open('chapters/appH-microscopic-proofs.tex', 'rb').read()
sha = hashlib.sha256(b).hexdigest()
crlf = b.count(b'\r\n'); lf = b.count(b'\n')
assert len(b) == 769120 and sha == '5f62af10bbcfc0507c852e127bbad53a6829fce572c97e69f7a9b0e1e0e0d4e3' and crlf == 3850 and lf == crlf, 'PRE pin moved: 769120/5f62af10/CRLF3850/bareLF0 expected, got %d/%s/%d/%d' % (len(b), sha[:8], crlf, lf - crlf)
ins = open('proposals/094-g-mfold-localization-unconditional/insert-r1.tex', 'rb').read()
assert ins.endswith(b'\r\n') and ins.count(b'\r\n') == 1, 'insert must be one line + terminal CRLF'
tail = b'and they close nothing in Problem~G.'
vac = b'\\emph{Vacuum term.}'
pin = tail + b'\r\n\r\n' + vac
assert b.count(pin) == 1, 'compound PIN count != 1'
pos = b.find(pin)
cut = pos + len(tail) + 4                      # index of line-initial \emph{Vacuum term.}
assert b[cut:cut + len(vac)] == vac
assert b[cut - 4:cut] == b'\r\n\r\n', 'gap before Vacuum is not CRLFCRLF'
assert b[cut - 6:cut - 4] != b'\r\n', 'gap is wider than one blank line'
sep = b'\r\n'
post = b[:cut] + ins + sep + b[cut:]
assert post[:cut] == b[:cut] and post[cut + len(ins) + len(sep):] == b[cut:], 'prefix/suffix identity'
assert ins.endswith(b'\r\n') and post[cut + len(ins) - 2:cut + len(ins) + len(sep) + len(vac)] == b'\r\n' + sep + vac, 'seam must be exactly one blank line before Vacuum'
triple = b'\r\n\r\n\r\n'
assert post.count(triple) == b.count(triple), 'stray triple CRLF introduced (pre-existing count must be unchanged)'
newsha = hashlib.sha256(post).hexdigest()
pn = post.count(b'close nothing in Problem~G.'); pv = post.count(b'closes nothing')
pvt = post.count(vac); ph = post.count(b'\\emph{Unconditional stratum localization')
pcr = post.count(b'\r\n'); plf = post.count(b'\n')
print('PRE size', len(b), 'sha', sha, 'CRLF', crlf, 'bareLF', lf - crlf)
print('PIN at byte', pos, 'cut at', cut, 'insert bytes', len(ins))
print('POST size', len(post), 'sha256', newsha)
print('POST CRLF', pcr, 'bareLF', plf - pcr, 'noun idiom', pn, 'verb', pv, 'Vacuum-term', pvt, 'new header', ph)
assert len(post) == 769120 + len(ins) + 2 and pcr == 3852 and plf == pcr and pn == 20 and pv == 1 and pvt == 2 and ph == 1
print('SIMULATE OVERALL: PASS (no write performed)')
