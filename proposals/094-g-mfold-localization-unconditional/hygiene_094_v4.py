# 094 hygiene: insert-r1f2.tex byte and content checks (read-only, print-only)
import hashlib, glob, re, sys
ins = open('proposals/094-g-mfold-localization-unconditional/insert-r1f2.tex', 'rb').read()
checks = []
def ck(name, cond): checks.append((name, bool(cond)))
ck('one content line + terminal CRLF only', ins.count(b'\r\n') == 1 and ins.endswith(b'\r\n') and ins.count(b'\n') == 1 and not ins.endswith(b'\r\n\r\n'))
ck('pure printable ASCII (0x20..0x7e) except terminal CRLF', all(0x20 <= x <= 0x7e for x in ins[:-2]))
for tok in (b'$', b'[', b']', b'\\cite', b'\\ref', b'\\eqref', b'\\label', b'%', b'&', b'#', b'\t'):
    ck('absent ' + repr(tok)[1:-1], ins.count(tok) == 0)
low = ins.lower()
for w in (b'status', b'priority', b'completion', b'open', b'critical', b'programme', b'derived'):
    ck('banned word absent: ' + w.decode(), low.count(w) == 0)
ck('exactly one \\emph{', ins.count(b'\\emph{') == 1)
ck('header present once', ins.count(b'\\emph{Unconditional stratum localization of the beta-family wall integrals.}') == 1)
ck('ends with idiom + CRLF', ins.endswith(b'close nothing in Problem~G.\r\n'))
ck('idiom occurs exactly once in insert', ins.count(b'close nothing in Problem~G.') == 1)
ck('braces balanced', ins.count(b'{') == ins.count(b'}'))
ck('\\( \\) balanced', ins.count(b'\\(') == ins.count(b'\\)') and ins.count(b'\\(') > 0)
hdr = b'Unconditional stratum localization'
ck('header absent from all chapters/*.tex', sum(open(f, 'rb').read().count(hdr) for f in glob.glob('chapters/*.tex')) == 0)
ck('no process words', not any(w in low for w in (b'the researcher', b'proposal', b'gatekeeper', b'as above', b'we ')))
for n, c in checks: print('%-52s %s' % (n, 'PASS' if c else 'FAIL'))
print('bytes', len(ins), 'sha256', hashlib.sha256(ins).hexdigest())
print('HYGIENE OVERALL:', 'PASS' if all(c for _, c in checks) else 'FAIL')
