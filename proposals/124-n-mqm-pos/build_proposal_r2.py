# -*- coding: ascii -*-
# Builds proposal-r2.md from proposal-r1.md by (a) patching the two displayed
# formulas superseded by the corrected payload, (b) replacing the fenced r1
# payload block by the byte-exact r2 payload between 123-convention extraction
# markers, (c) updating pins/cert numbers, (d) inserting the Revisions r1->r2
# section, round-2 decisions and round-2 gatekeeper notes. Every replacement is
# asserted to occur an exact number of times. Output: UTF-8 (one inherited
# o-umlaut at r1 L127), CRLF.
import hashlib, os

F = os.path.dirname(os.path.abspath(__file__))
B = chr(92)          # backslash
BT = chr(96)         # backtick
FENCE = BT * 3
OUML = chr(246)      # o-umlaut, present once in proposal-r1.md (Schr[o]dinger)

pay = open(os.path.join(F, 'payload-124.txt'), 'rb').read()
PAY_SHA = '8a86b389f85999161f8c7488064e13e9d1b8340c'
PAY_SIZE = 5831
assert hashlib.sha1(pay).hexdigest() == PAY_SHA and len(pay) == PAY_SIZE
POST_SHA = '76d862968c31d78fffc665f72aaf60d40c90367a'
POST_SIZE = 875106

text = open(os.path.join(F, 'proposal-r1.md'), encoding='utf-8').read()  # \n newlines

def rep(old, new, n=1):
    global text
    assert text.count(old) == n, (old[:60], text.count(old))
    text = text.replace(old, new)

# ---- title ----
rep('# Proposal 124-n-mqm-pos, round 1', '# Proposal 124-n-mqm-pos, round 2')

# ---- Revisions section (inserted before ## Result) ----
REV = """## Revisions r1 -> r2 (this round)

r1 verdict (review-r1.md, sha1 `a201c520ba50a3f0049830fe1c993c9a17efb6fa`, 13,778 B):
ACCEPT WITH REQUIRED REVISIONS, MILESTONE none, flags none. The r1 mathematics was
verified by independent re-derivation and ACCEPTED in substance; this round applies
exactly the three required payload corrections, regenerates every byte pin, and
re-certifies. The payload changed ONLY in the three specified spans
(`diff_payload_124.py`, invariant outputs `BYTE-EXACT-OK`, `CLUSTERS: 3`,
`EXACTLY-THREE OK`); no status/priority/completion label is touched anywhere and
`chapters/` was not modified.

Finding 1 (MAJOR, one-token sign slip in the no-go half). Required replacement,
adopted verbatim from the review's Corrected snippet: the displayed Hamiltonian
kinetic polynomial `\\(\\sum_{\\mu,\\nu}\\eta^{\\mu\\nu}(-\\operatorname{Tr}P^\\mu P^\\nu)\\)`
becomes `\\(\\sum_{\\mu,\\nu}\\eta^{\\mu\\nu}\\operatorname{Tr}(P^\\mu P^\\nu)\\)`;
the evaluated value `\\(-\\operatorname{Tr}(P^0)^2<0\\)` at `P^i=0` is now the value
of the displayed polynomial (and its quantization is the B3 operator
`-\\eta^{\\mu\\nu}\\partial_\\mu\\partial_\\nu` the script checks). Payload span:
`(-\\operatorname{Tr}P^\\mu P^\\nu)` -> `\\operatorname{Tr}(P^\\mu P^\\nu)`.

Finding 2 (minor, g_YM prefactor). The quartic display gains its overall
`g_{\\mathrm{YM}}^{-2}` prefactor, matching eq:Smatrix and the ray value
`-t^4/(4g_{\\mathrm{YM}}^2)` in the same sentence: `\\(\\tfrac14\\sum ...\\|^2\\)`
becomes `\\(g_{\\mathrm{YM}}^{-2}\\bigl(\\tfrac14\\sum ...\\|^2\\bigr)\\)`. The
review's byte-inspected snippet ends `\\|^2\\bigr)\\)` (\\bigl and the inline-math
closer are distinct characters); the first r2 splice attempt dropped the
display-closing `\\)` and FAILED the compile certificate (see Certificate
history); the final payload ends the fragment exactly as the snippet does.

Finding 3 (minor, closer adjacency). Final clause `...they change no status
label, and Problems~F and~N remain open.` replaced by `...they change no status
label, and they close nothing in Problem~N.` per the review, removing a verbatim
repetition of the adjacent completion-class closer (appH L4068).

Finding 4 (record-only, actioned optionally). Comment-only script fixes, code
byte-identical modulo comments (asserted programmatically before/after):
`verify_pos_124.py` line 5 comment `2|a12|^2` -> `4|a12|^2` (the review
attributed this comment to `verify_nogo_124.py` line 5; grep shows the string
`a12` occurs in that comment only in `verify_pos_124.py`), and
`verify_nogo_124.py` line 18 comment `Sum eta^{mu nu} (-Tr(P^mu P^nu))` ->
`Sum eta^{mu nu} Tr(P^mu P^nu)` to match finding 1's corrected classical
polynomial. KL min-residue values are run-dependent at the 1e-28..1e-32 noise
floor (r1 researcher run 3.7e-28, gatekeeper run 7.1e-29, r2 runs 3.109e-32 /
7.646e-30, all >= 0); text notes this and no claim changes.

Pin lineage (sha1 / bytes):
- payload: r1 `8988a8baf171cc510ed109618c25fa729f2fb5d2`/5,797 -> intermediate
  `1e8ce8a959c45a4e11e985245120a06a3e74d301`/5,829 (superseded within this round
  by the finding-2 closer fix; bytes not preserved, hash recorded) -> r2 final
  `8a86b389f85999161f8c7488064e13e9d1b8340c`/5,831 (+34 B).
- PRE (live appH, unchanged, re-verified at every script run):
  `ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1`/869,275/4,140 lines, anchor count 1.
- POST: r1 `1d192b89bd2d20c50a4c70dfd108656a529baa4d`/875,072 (void) -> r2
  `76d862968c31d78fffc665f72aaf60d40c90367a`/875,106 = 869,275 + 5,831.
- Certificate history (item-108 rule; r1 cert void): the intermediate splice was
  built in fresh tree `namcg-124-build-r3` and FAILED (pdflatex rc 1; single
  error, `LaTeX Error: Bad math environment delimiter` at appH L4023, the payload
  line: the dropped `\\)` left the `\\(g_{\\mathrm{YM}}^{-2}\\bigl(` math
  unclosed). After the closer fix the r2 splice was rebuilt clean in a new tree
  `namcg-124-build-r4` (pdflatex/bibtex/pdflatex/pdflatex all rc 0; final pass:
  0 undefined references, 0 undefined citations, 0 multiply-defined, 0 LaTeX
  Warnings, 448 pages, PDF 3,284,690 B); recorded fresh in `cert-summary-124.txt`
  with the r1 summary preserved as `cert-summary-124.r1.txt`. All superseded
  round-1 bytes are preserved in this folder with `.r1-bytes` suffix (and
  `cert-summary-124.r1.txt`); hashes in `manifest.md`.

"""
rep('\n## Result\n', '\n' + REV + '## Result\n')

# ---- Result + P5 quartic formula (two occurrences) ----
q_old = r'\(\tfrac14\sum_{ij}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\)'
q_new = r'\(g_{\rm YM}^{-2}\bigl(\tfrac14\sum_{ij}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\bigr)\)'
rep(q_old, q_new, 2)

# ---- P5 kinetic formula ----
rep(r'\(\sum_{\mu\nu}\eta^{\mu\nu}(-\mathrm{Tr}P^\mu P^\nu)\) evaluates to',
    r'\(\sum_{\mu\nu}\eta^{\mu\nu}\mathrm{Tr}(P^\mu P^\nu)\) evaluates to')

# ---- P3 residue run-dependence note ----
rep(r'minimum residue \(3.7\cdot10^{-28}\ge0\) on 12 states',
    r'minimum residue \(3.109\cdot10^{-32}\ge0\) on 12 states (the numerical residue '
    r'minimum is run-dependent at the 1e-28..1e-32 numerical noise floor; the invariant '
    r'claim is nonnegativity; the gatekeeper r1 run obtained \(7.1\cdot10^{-29}\))')

# ---- Source reading round-2 addition ----
rep('Unreadable files: none.',
    'Unreadable files: none.\n\nRound 2 additionally read IN FULL: `review-r1.md` '
    '(all findings, the Corrected snippet, certificate and lineage sections) and its '
    'sha1-pinned bytes; the extraction-marker embedding convention of '
    '`proposals/123-f-coeff-locked-block/proposal-r2.md`; every superseded r1 artifact '
    'byte-for-byte before overwriting (`.r1-bytes` copies). Live appH pin re-verified '
    'before splicing: sha1 `ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1`, 869,275 B, '
    '4,140 lines, anchor count 1.')

# ---- payload block replacement (index-based) ----
i0 = text.find('Payload bytes (`payload-124.txt`')
assert i0 > 0
i1 = text.find(FENCE + 'latex', i0)
i2 = text.find('\n' + FENCE + '\n', i1)
assert i1 > i0 and i2 > i1
payload_line = pay[:-4].decode('ascii')
assert pay.endswith(b'\r\n\r\n') and B + 'label' not in payload_line
newblock = (
    'Payload bytes (`payload-124.txt`, sha1 `' + PAY_SHA + '`\n'
    '(' + str(PAY_SIZE) + ' B), single ASCII line + CRLFCRLF; braces balanced). '
    'Byte-exact\nembedding (123 convention): the payload file bytes are the single line\n'
    'between the markers below plus CRLF + CRLF (the file terminator); the\n'
    'extraction markers occur exactly once in this file.\n\n'
    '>>> BEGIN PAYLOAD-124.TXT BYTE-EXACT (r2, sha1 ' + PAY_SHA + ', ' + str(PAY_SIZE) + ' B) <<<\n'
    + payload_line + '\n'
    '>>> END PAYLOAD-124.TXT <<<'
)
text = text[:i0] + newblock + text[i2 + len('\n' + FENCE + '\n'):]
assert text.count('>>> BEGIN PAYLOAD-124.TXT BYTE-EXACT') == 1
assert text.count('>>> END PAYLOAD-124.TXT <<<') == 1
assert FENCE + 'latex' not in text

# ---- verification section pin updates ----
rep('PAY `8988a8baf171cc510ed109618c25fa729f2fb5d2`/5797,',
    'PAY `' + PAY_SHA + '`/' + str(PAY_SIZE) + ',')
rep('POST `1d192b89bd2d20c50a4c70dfd108656a529baa4d`/875072.',
    'POST `' + POST_SHA + '`/' + str(POST_SIZE) + '.')
rep('`A3 KL ...: min r_n (expect >= 0) = 3.7e-28`',
    '`A3 KL ...: min r_n (expect >= 0) = 3.109e-32 this run (run-dependent noise floor, >= 0 at every run)`')
rep('five pdflatex passes + bibtex, all', 'one pdflatex + bibtex + two pdflatex, all')
rep('multiply-defined, 0 LaTeX Warnings, 448 pages).',
    'multiply-defined, 0 LaTeX Warnings, 448 pages, PDF 3,284,690 B).')
rep('sha1 1d192b89bd2d20c50a4c70dfd108656a529baa4d, reproducible from',
    'sha1 ' + POST_SHA + ', reproducible from')
rep('pdflatex` (nonstopmode).',
    'pdflatex` (nonstopmode).\n'
    '6. `diff_payload_124.py` -> `diff_payload_124.out` (rc 0). Proves the r2 payload is\n'
    '   the r1 payload (`payload-124.txt.r1-bytes`) with EXACTLY the three required\n'
    '   substring replacements applied once each and nothing else changed (invariant\n'
    '   outputs: `BYTE-EXACT-OK`, `CLUSTERS: 3`, `EXACTLY-THREE OK`).')

# ---- Decisions Taken: round-2 bullets ----
R2D = """- **Round 2, finding 2 closer**: adopted the review snippet byte-exactly, ending
  `\\|^2\\bigr)\\)` (the `\\bigl`/`\\bigr` delimiters and the inline-math closer are
  three distinct characters; the intermediate splice that dropped the closer failed
  the compile certificate at pass 1 and was rejected - the failure is recorded in
  the Certificate history above rather than hidden).
- **Round 2, finding 4 attribution**: the erroneous `2|a12|^2` comment is at
  `verify_pos_124.py` line 5, not `verify_nogo_124.py` line 5 (grep: `a12` does not
  occur in `verify_nogo_124.py`); fixed where it actually is, plus the consistent
  comment alignment in `verify_nogo_124.py` line 18. Rejected leaving them: the
  comments document the checked identities, and finding 1 shows the old comment
  text is the same false equation as finding 1.
- **Round 2, cert trees**: fresh directories (`namcg-124-build-r3`, then
  `namcg-124-build-r4`) under the system TEMP instead of deleting failed trees
  (delete denied by policy); no repository build, no `scripts/build_check.py`.

"""
rep('## Milestone assessment', R2D + '## Milestone assessment')

# ---- Milestone + status: round-2 sentences ----
rep('is closed and no missing link\nis closed without inputs (ass:dictionary sign, \\(T_{\\mu\\nu}\\), and the\ntruncation all remain).',
    'is closed and no missing link\nis closed without inputs (ass:dictionary sign, \\(T_{\\mu\\nu}\\), and the\ntruncation all remain). Round 2 adds no new mathematical claim: it applies the\ngatekeeper-verified corrections to the payload displays and re-certifies.')
rep('payload changes no status text).',
    'payload changes no status text). Round 2 changes no label.')

# ---- Special instructions: round-2 notes ----
rep('- The 067 review-r2 ranked relaxation list, avenue (b), is the dispatched\n  route; confirm the package answers avenue (b) and not a restatement\n  of the merged 067 conditional text.',
    '- The 067 review-r2 ranked relaxation list, avenue (b), is the dispatched\n'
    '  route; confirm the package answers avenue (b) and not a restatement\n'
    '  of the merged 067 conditional text.\n'
    '- Round 2 only: verify the payload diff (`diff_payload_124.out`: exactly three\n'
    '  changed spans vs `payload-124.txt.r1-bytes`), that the finding-2 fragment now\n'
    '  reads `...equals \\(g_{\\mathrm{YM}}^{-2}\\bigl(...\\bigr)\\) with...` (inline\n'
    '  math closed), and that the final clause reads `...they change no status label,\n'
    '  and they close nothing in Problem~N.` Re-run the certificate from the final\n'
    '  spliced bytes (`76d86296...`); the intermediate payload `1e8ce8a9...` is void\n'
    '  and must not be integrated.')

# ---- Remaining open step: round-2 note ----
rep('Each is stated in the inserted text as an open item; none is claimed.',
    'Each is stated in the inserted text as an open item; none is claimed. Round 2\nchanges nothing here.')

# ---- write UTF-8 + CRLF, verify embedding ----
assert all(32 <= ord(c) <= 126 or c in '\n' + OUML for c in text), 'unexpected non-ASCII'
n_ouml_r1 = open(os.path.join(F, 'proposal-r1.md'), encoding='utf-8').read().count(OUML)
assert text.count(OUML) == n_ouml_r1, 'o-umlaut count changed vs r1'
out = text.replace('\n', '\r\n')
open(os.path.join(F, 'proposal-r2.md'), 'wb').write(out.encode('utf-8'))

# embedding verification: extract between markers, compare to payload bytes
md = open(os.path.join(F, 'proposal-r2.md'), 'rb').read().decode('utf-8')
i = md.find('>>> BEGIN PAYLOAD-124.TXT BYTE-EXACT')
j = md.find('>>> END PAYLOAD-124.TXT <<<')
line_end = md.find('\r\n', i)
extracted = md[line_end + 2:j].replace('\r\n', '')
assert extracted == payload_line, 'embedded payload differs from payload file'
assert (extracted + '\r\n\r\n').encode('ascii') == pay
print('proposal-r2.md written:', os.path.getsize(os.path.join(F, 'proposal-r2.md')), 'B')
print('embedded payload byte-exact; sha1', hashlib.sha1(pay).hexdigest())
OKCTX = ('r1', 'intermediate', 'void', 'superseded', 'FAILED', 'must not', 'Round 2', 'round-1')
for stale in ('8988a8baf171', '1d192b89bd2d', '1e8ce8a959c4', '875,072', 'round 1'):
    bad = [ln for ln in md.split('\r\n') if stale in ln and not any(k in ln for k in OKCTX)]
    assert not bad, (stale, bad[:2])
print('no stale pins outside the lineage record')
