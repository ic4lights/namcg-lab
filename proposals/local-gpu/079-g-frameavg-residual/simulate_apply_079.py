"""079 simulate_apply (r1): in-memory byte contract for the insert. Never writes
to chapters/. Loads live appH-microscopic-proofs.tex, asserts the PRE contract
against the dispatch values, inserts the insert paragraph blank-separated
immediately before the unique line-start Vacuum-term anchor, and asserts the
POST contract in memory only. Also runs the insert hygiene scan.

Run:  python -I proposals/079-g-frameavg-residual/simulate_apply_079.py
Expected final line: PASS simulate_apply
"""
import hashlib

APPH = 'chapters/appH-microscopic-proofs.tex'
INS = 'proposals/079-g-frameavg-residual/insert-r1.tex'

PRE_BYTES, PRE_SHA = 716985, 'be3dbddd91560f5af9d5e47ee9c559bae59e233f65abb113fe18b46f8c3b1b2e'
PRE_CRLF = 3822
ANCHOR = '\\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023'
ANCHOR_LINE = 3173   # 1-based in PRE

raw = open(APPH, 'rb').read()
print('PRE bytes %d sha256 %s' % (len(raw), hashlib.sha256(raw).hexdigest()))
assert len(raw) == PRE_BYTES
assert hashlib.sha256(raw).hexdigest() == PRE_SHA
crlf = raw.count(b'\r\n')
lf = raw.count(b'\n')
print('PRE CRLF %d bareLF %d' % (crlf, lf - crlf))
assert crlf == PRE_CRLF and lf == crlf

lines = raw.split(b'\r\n')
hits = [i for i, l in enumerate(lines) if l.startswith(ANCHOR.encode())]
print('anchor hits (0-based):', hits, 'count', len(hits))
assert hits == [ANCHOR_LINE - 1]

ins = open(INS, 'rb').read()
print('insert bytes %d sha256 %s' % (len(ins), hashlib.sha256(ins).hexdigest()))
assert ins.endswith(b'\r\n') and ins.count(b'\r\n') == 1 and ins.count(b'\n') == 1
text = ins.decode('ascii')  # raises if non-ASCII; no BOM (decode would show)
low = text.lower()
for w in ('status', 'priorit', 'complet', 'open', 'critic', 'programme', 'derived',
          '\\cite', '\\ref{', '\\label', '\\eqref', '$', '[', ']', 'subagenthandback',
          'handback-send-enforce'):
    assert w not in low, w
assert text.count('\\emph{') == 1
assert len(text.splitlines()) == 1 and text.count('~') >= 1
print('hygiene: ASCII, 1 content line + terminal CRLF, 1 emph, 0 banned tokens, 0 injection markers')

# insert as its own blank-separated paragraph immediately before the anchor line
post_lines = lines[:ANCHOR_LINE - 1] + [ins.rstrip(b'\r\n')] + [b''] + lines[ANCHOR_LINE - 1:]
post = b'\r\n'.join(post_lines)
print('POST bytes %d sha256 %s' % (len(post), hashlib.sha256(post).hexdigest()))
assert len(post) == PRE_BYTES + len(ins) + 2, (len(post), PRE_BYTES + len(ins) + 2)
pcrlf = post.count(b'\r\n')
print('POST CRLF %d bareLF %d' % (pcrlf, post.count(b'\n') - pcrlf))
assert pcrlf == PRE_CRLF + 2 and post.count(b'\n') == pcrlf
plines = post.split(b'\r\n')
phits = [i for i, l in enumerate(plines) if l.startswith(ANCHOR.encode())]
assert phits == [ANCHOR_LINE + 1]   # moved down by exactly 2 lines
print('anchor line POST (1-based): %d (PRE %d)' % (phits[0] + 1, ANCHOR_LINE))
header = '\\emph{Frame-uniformity of the finite-N residual bound.}'.encode()
c_pre = sum(1 for l in lines if header in l)
c_post = sum(1 for l in plines if header in l)
print('insert header occurrences: PRE %d POST %d (expected 0, 1)' % (c_pre, c_post))
assert c_pre == 0 and c_post == 1
print('no write performed on', APPH)
print('PASS simulate_apply')
