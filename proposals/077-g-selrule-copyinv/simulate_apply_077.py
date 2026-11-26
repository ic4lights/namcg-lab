"""simulate_apply_077.py - anchor + byte contract check for the 077 insert-r1.tex.

Run from the repository root:
  python -I proposals/077-g-selrule-copyinv/simulate_apply_077.py
Reads chapters/appH-microscopic-proofs.tex, proposals/077-g-selrule-copyinv/insert-r1.tex
and bib/namcg.bib; verifies the PRE pins, the insert hygiene (ASCII, single content
line + terminal CRLF, no forbidden tokens/words), verifies anchor uniqueness, builds
the POST bytes IN MEMORY by asserting a unique line-start anchor replacement that
keeps the paragraph blank-separated on BOTH sides, and prints the POST contract.
Writes nothing except stdout. Exit 0 with all asserts passing is the invariant.
"""
import hashlib
import re

appH_path = 'chapters/appH-microscopic-proofs.tex'
ins_path = 'proposals/077-g-selrule-copyinv/insert-r1.tex'
bib_path = 'bib/namcg.bib'

appH = open(appH_path, 'rb').read()
ins = open(ins_path, 'rb').read()
bib = open(bib_path, 'rb').read()

# ---- PRE pins (live-verified 2026-11-17 by researcher #3)
assert len(appH) == 707434, len(appH)
assert hashlib.sha256(appH).hexdigest().startswith('94b39393bdf8')
assert appH.count(b'\r\n') == 3818
assert appH.replace(b'\r\n', b'').count(b'\n') == 0
assert len(bib) == 37463
assert hashlib.sha256(bib).hexdigest().startswith('4d6d7b2a668f')
print('PRE appH %d B / %s... / CRLF %d / bareLF 0' %
      (len(appH), hashlib.sha256(appH).hexdigest()[:12], appH.count(b'\r\n')))
print('PRE bib  %d B / %s...' % (len(bib), hashlib.sha256(bib).hexdigest()[:12]))

# ---- insert hygiene
assert all(b < 128 for b in ins), 'non-ASCII byte in insert'
assert ins.endswith(b'\r\n'), 'insert must end with a single terminal CRLF'
body = ins[:-2]
assert b'\r' not in body and b'\n' not in body, 'insert must be ONE content line'
for tok in (b'\\ref', b'\\eqref', b'\\cite', b'\\label', b'$', b'[', b']'):
    assert body.count(tok) == 0, 'forbidden token ' + repr(tok)
low = body.lower()
for w in (b'status', b'priority', b'completion', b'open', b'derived',
          b'programme', b'critical'):
    assert low.count(w) == 0, 'forbidden word ' + repr(w)
assert body.count(b'\\emph{') == 1, 'exactly one \\emph header expected'
assert body.endswith(b'they close nothing in Problem~G.')
print('INSERT hygiene OK: content %d B, sha256 %s' %
      (len(body), hashlib.sha256(body).hexdigest()))

# ---- anchor: unique line-start long-form 'Vacuum term.' line (076 precedent);
# the short form '\\emph{Vacuum term.}' occurs twice (L3006 + this line)
anchor = b'\r\n\\emph{Vacuum term.} The abstract of~\\cite{Steinacker2023}'
assert len(re.findall(re.escape(anchor), appH)) == 1
assert appH.count(b'\\emph{Vacuum term.}') == 2
assert appH.count(b'State realization of copy-invariant momenta') == 0

# insert the body between blank lines, keeping the anchor line intact
post = appH.replace(anchor, b'\r\n' + body + b'\r\n' + anchor, 1)
assert post.count(b'\r\n\r\n' + body + b'\r\n\r\n\\emph{Vacuum term.}') == 1
assert len(post) == len(appH) + len(body) + 4
assert post.count(b'\r\n') == 3818 + 2
assert post.replace(b'\r\n', b'').count(b'\n') == 0
assert post.count(b'State realization of copy-invariant momenta') == 1
assert post.count(b'\\emph{Vacuum term.}') == 2
assert post.count(anchor) == 1
# no triple blank line introduced at the site
i = post.index(b'\r\n\r\n' + body)
assert b'\r\n\r\n\r\n' not in post[max(0, i - 200):i + len(body) + 300]
print('POST appH %d B / sha256 %s / CRLF %d / bareLF 0 / delta +%d B / +%d CRLF'
      % (len(post), hashlib.sha256(post).hexdigest(), post.count(b'\r\n'),
         len(post) - len(appH), post.count(b'\r\n') - 3818))
# 0-based count of CRLFs before the anchor line == (1-based anchor line) - 1
print('anchor line after insert (1-based):',
      post[:post.index(anchor) + 2].count(b'\r\n') + 1)
print('body line after insert (1-based):',
      post[:i + 4].count(b'\r\n') + 1)
print('ALL ASSERTS PASS')
