# 095 insert hygiene checks (read-only). Run from repo root:
# python -I proposals/095-g-gram-moment-identification/hygiene_095.py
import glob, hashlib

INS = 'proposals/095-g-gram-moment-identification/insert-r1h.tex'
ins = open(INS, 'rb').read()
checks = []
def chk(name, cond):
    checks.append((name, bool(cond))); print(name, 'PASS' if cond else 'FAIL')

chk('ascii_only', all(c < 128 for c in ins))
ctrl = [c for c in ins if c < 0x20 and c not in (0x0d, 0x0a)]
chk('no_ctrl_except_eol', not ctrl)
chk('one_line_terminal_crlf', ins.endswith(b'\r\n') and ins.count(b'\n') == 1 and ins.count(b'\r') == 1)
chk('no_bareLF', ins.count(b'\n') == ins.count(b'\r\n'))
for bad in (b'$', b'[', b']', b'\\cite', b'\\ref', b'\\eqref', b'\\label'):
    chk('banned_' + bad.decode().replace('\\', ''), ins.count(bad) == 0)
chk('single_emph_run', ins.count(b'\\emph{') == 1 and ins.startswith(b'\\emph{'))
hdr_end = ins.find(b'}')
chk('header_ends_with_period', hdr_end > 0 and ins[hdr_end-1:hdr_end] == b'.')
txt = ins.decode('ascii')
header = txt[:hdr_end+1]
chk('header_period_runin', hdr_end > 10 and txt[hdr_end+1] == ' ')
import re
for w in ('OPEN', 'CRITICAL PATH', 'PROGRAMME-CONDITIONAL', 'status', 'Status',
          'priority', 'Priority', 'complete', 'completion', 'closure', 'solved', 'closed'):
    pat = w if w.isupper() or ' ' in w else r'' + w + r''
    chk('vocab_' + w.replace(' ', '_'), re.search(pat, txt) is None)
chk('ends_with_idiom', txt.rstrip('\r\n').endswith('close nothing in Problem~G.'))
chk('one_math_block_open', txt.count('\\(') == txt.count('\\)'))

# header uniqueness across chapters/ (read-only)
hits = []
for f in glob.glob('chapters/*.tex'):
    if header.encode('ascii') in open(f, 'rb').read():
        hits.append(f)
print('HEADER_HITS_IN_CHAPTERS', hits)
chk('header_unique', not hits)

# idiom counts on simulated POST (recompute splice in memory, no writes)
b = open('chapters/appH-microscopic-proofs.tex', 'rb').read()
vac = b'\\emph{Vacuum term.'
h94 = b'\\emph{Unconditional stratum localization'
i94 = b.find(h94); eol = b.find(b'\r\n', i94)
pin = b[eol-96:eol] + b'\r\n\r\n' + vac
assert b.count(pin) == 1
cut = b.find(pin) + len(b[eol-96:eol]) + 4
post = b[:cut] + ins + b'\r\n' + b[cut:]
chk('post_idiom_21', post.count(b'close nothing in Problem~G.') == 21)
chk('post_idiom_verb_1', post.count(b'closes nothing in Problem~G.') == 1)
print('INSERT_SIZE', len(ins), 'INSERT_SHA8', hashlib.sha256(ins).hexdigest()[:8])
print('SUMMARY', 'ALL PASS' if all(c for _, c in checks) else 'FAIL')
