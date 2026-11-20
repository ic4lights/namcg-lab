# 095 read-only splice simulation against the LIVE tree. NO WRITES.
# Run from repo root: python -I proposals/095-g-gram-moment-identification/simulate_apply_095.py
import hashlib, sys

APP = 'chapters/appH-microscopic-proofs.tex'
INS = 'proposals/095-g-gram-moment-identification/insert-r1h.tex'
b = open(APP, 'rb').read()

def sha(x): return hashlib.sha256(x).hexdigest()
crlf = b.count(b'\r\n'); lfs = b.count(b'\n')
print('PRE_SIZE', len(b)); print('PRE_SHA256', sha(b)); print('PRE_CRLF', crlf); print('PRE_bareLF', lfs - crlf)
fails = []
def req(name, cond, val=None):
    if not cond: fails.append((name, val))
    print(name, 'OK' if cond else 'STOP', val if val is not None else '')

req('pre_size', len(b) == 772537, len(b))
req('pre_sha', sha(b) == '3f81a3a9627ce491726a108a10153c657cb4dc6c6274dc9a3a3e4dc117aa5a86')
req('pre_crlf', crlf == 3852, crlf)
req('pre_bareLF', lfs - crlf == 0, lfs - crlf)

# compound PIN: 094 tail sentence read VERBATIM from disk + CRLFCRLF + line-initial Vacuum header
vac = b'\\emph{Vacuum term.}'
vt_heads = [i for i in range(len(b)) if b.startswith(vac, i)]
print('VACUUM_HEADER_COUNT', len(vt_heads))
req('vacuum_count', len(vt_heads) == 2, len(vt_heads))
# 094 paragraph line: find its start, take the last 96 bytes of the line as the tail
h94 = b'\\emph{Unconditional stratum localization'
i94 = b.find(h94); req('found_094', i94 != -1)
eol = b.find(b'\r\n', i94); tail = b[eol-96:eol]
pin = tail + b'\r\n\r\n' + vac
req('pin_count', b.count(pin) == 1, b.count(pin))
if fails:
    print('ABORT', fails); sys.exit(1)

cut = b.find(pin) + len(tail) + 4          # byte index of line-initial Vacuum header
req('cut_is_line_initial', b[cut:cut+len(vac)] == vac and b[cut-2:cut] == b'\r\n')

ins = open(INS, 'rb').read()
req('insert_terminal_crlf', ins.endswith(b'\r\n') and ins.count(b'\n') == 1, len(ins))
post = b[:cut] + ins + b'\r\n' + b[cut:]
idiom = 'close nothing in Problem~G.'
pre_n = b.count(idiom.encode()); post_n = post.count(idiom.encode())
print('POST_SIZE', len(post), 'EXPECT', len(b) + len(ins) + 2)
print('POST_SHA256', sha(post))
print('POST_CRLF', post.count(b'\r\n'), 'EXPECT', crlf + 2)
print('POST_bareLF', post.count(b'\n') - post.count(b'\r\n'))
print('IDIOM_pre_post', pre_n, post_n, 'EXPECT 20 21')
print('VACUUM_POST', post.count(vac), 'EXPECT 2')
print('PREFIX_IDENTITY', post[:cut] == b[:cut])
print('SUFFIX_IDENTITY', post[cut+len(ins)+2:] == b[cut:])
allok = (len(post) == len(b) + len(ins) + 2 and post.count(b'\r\n') == crlf + 2
         and post.count(b'\n') - post.count(b'\r\n') == 0
         and pre_n == 20 and post_n == 21 and post.count(vac) == 2
         and post[:cut] == b[:cut] and post[cut+len(ins)+2:] == b[cut:])
print('SUMMARY', 'ALL PASS' if allok and not fails else 'FAIL')
print('CUT_BYTE', cut)
