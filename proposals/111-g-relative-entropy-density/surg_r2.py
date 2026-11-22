# Byte surgery: proposal-r1.md -> proposal-r2.md (record-level corrections F2-F5 +
# changelog), r1_to_r2.diff via difflib. Run: python -I surg_r2.py (from this folder)
import hashlib, difflib, os

F = os.path.dirname(os.path.abspath(__file__))
def p(name): return os.path.join(F, name)

orig = open(p('proposal-r1.md'), 'rb').read()
d = orig
assert len(d) == 24966, 'r1 size changed: %d' % len(d)

i0 = d.index(b'\n')
nl = b'\r\n' if d[i0-1:i0] == b'\r' else b'\n'
print('first-line newline:', 'CRLF' if nl == b'\r\n' else 'LF')

def rep(data, old, new, expect=1):
    c = data.count(old)
    assert c == expect, 'count %d != %d for %r' % (c, expect, old[:60])
    return data.replace(old, new)

BS = chr(92).encode()  # backslash byte, heredoc-safe

# F2a: Result para 1 wrong-convention phrase
d = rep(d, b'c0 = ln Z0 the normalization',
           b'c0 = -ln Z0 = sum_j ln(2 sinh(h(nu_j)/2)) the normalization')
# F2b: C4 wrong-convention phrase
d = rep(d, b'C4. c0(G) = ln Z(G) with', b'C4. c0(G) = -ln Z(G) with')
# F3: battery table Test A row worst observed dSfock (tolerance unchanged)
d = rep(d, b'dSfock <= 1.5e-07', b'dSfock <= 9.7e-07')
# F4: Missing-step quotation carries the source symbol partial M (appH L3199)
f4_new = b'the boundary ' + BS + b'(' + BS + b'partial M' + BS + b') under which'
d = rep(d, b'the boundary under which', f4_new)

# F5: (star) sentence in C6 = SECOND occurrence of the phrase (Result para 1 is the
# first; the review requires the clause on the (star) sentence itself, one clause).
phrase = b'state rho1 with covariance G1,'
i1 = d.index(phrase); i2 = d.index(phrase, i1+1)
assert d.count(phrase) == 2 and d[i2:].startswith(phrase)
f5_new = (b'state rho1 with covariance G1, where G1 is the uncentered symmetrized '
          b'second moment G_ij = Tr rho1 (R_i R_j + R_j R_i)/2 per H2 (equivalently, '
          b'rho1 of zero mean),')
d = d[:i2] + f5_new + d[i2+len(phrase):]

# Title + r1->r2 changelog (changelog avoids re-emitting the superseded literals)
title_old = b'# Proposal 111-g-relative-entropy-density, round 1'
assert d.count(title_old) == 1
chg = nl.join([
 b'# Proposal 111-g-relative-entropy-density, round 2', b'',
 b'## r1 -> r2 changelog (review-r1.md sha1-10 48118920cf; record-level corrections',
 b'only, no new mathematics; all formulas, the (star) equation, and every battery',
 b'number other than the F3 restatement are byte-identical to r1)', b'',
 b'- F1 (blocking, manifest): manifest.md restated from actual disk bytes;',
 b'  p2_fock_srel.py pin corrected to b6bac2a036 (1565 B, bytes unchanged on disk).',
 b'  The r1 manifest entry 0904f2f7d8 was stale; the gatekeeper (review-r1 F1)',
 b'  verified the on-disk file runs and reproduces every P2 number.',
 b'- F2 (major): c0 normalization label corrected in Result para 1 and C4 (missing',
 b'  minus sign): now c0 = -ln Z0 = sum_j ln(2 sinh(h(nu_j)/2)), matching C6',
 b'  Z0 = exp(-c0), the (star) sign, and the battery dZ definition. No formula',
 b'  changed; every remaining ln-Z0 occurrence (C6 proof lines, C3 Z(G) definition,',
 b'  Test A row "ln Z vs c0" content note) was checked and is correct-convention',
 b'  as written.',
 b'- F3 (minor): battery table Test A row dSfock bound restated to "<= 9.7e-07"',
 b'  (observed worst 9.66e-07 at (17,0.70,1), run_modular.out line 2; the three',
 b'  observed values are 9.66e-07 / 1.47e-07 / 1.02e-07; tolerance 5e-3 unchanged).',
 b'- F4 (minor): Missing-step quotation now carries the source symbol: "the boundary',
 b'  ' + BS + b'(' + BS + b'partial M' + BS + b') under which" (appH-microscopic-proofs.tex',
 b'  L3199), replacing the silent one-word rendering of that symbol.',
 b'- F5 (minor): the (star) sentence (C6) now carries one clarifying clause: G1 is',
 b'  the uncentered symmetrized second moment G_ij = Tr rho1 (R_i R_j + R_j R_i)/2',
 b'  per H2 (equivalently, rho1 of zero mean). No new mathematics.',
 b'- F6 (minor, deliberately NOT taken): the p1_symbolic_a0.py comment "sq O sq = G',
 b'  at n=1" (false as written; correct: sq O sq = det(sq)*O; the encoded Kf_term',
 b'  and all printed outputs are correct and were independently re-derived by the',
 b'  gatekeeper) is left untouched so the pinned hash 8d2bd3624d stays verifiable;',
 b'  comment correction deferred to a future battery revision.', b''])
d = d.replace(title_old, chg, 1)

open(p('proposal-r2.md'), 'wb').write(d)

# ---- diff (clean headers: strip line endings, terminate with LF) ----
a = orig.decode('latin-1').splitlines()
b2 = d.decode('latin-1').splitlines()
dlines = list(difflib.unified_diff(a, b2, 'proposal-r1.md', 'proposal-r2.md',
                                   lineterm='\n'))
open(p('r1_to_r2.diff'), 'wb').write(''.join(x + '\n' for x in dlines)
                                     .encode('latin-1'))
hunks = sum(1 for ln in dlines if ln.startswith('@@'))
minus = [ln for ln in dlines if ln.startswith('-') and not ln.startswith('---')]
plus  = [ln for ln in dlines if ln.startswith('+') and not ln.startswith('+++')]
print('hunks:', hunks, 'minus-lines:', len(minus), 'plus-lines:', len(plus))
for ln in dlines:
    if ln.startswith('@@'): print(ln[:70])
assert hunks == 5, 'expected 5 hunks (C4+C6 share one hunk)'  # merged pair
assert len(minus) == 6, 'unexpected removed-line count'

# ---- post-checks ----
assert d.count(b'c0 = ln Z') == 0, 'wrong-convention phrase left'
assert d.count(b'1.5e-07') == 0, 'stale bound left'
assert d.count(b'9.7e-07') == 2  # changelog mention + Test A row
assert d.count(b'dSfock <= 9.7e-07 |') == 1  # exactly in the Test A row
assert f4_new in d
assert b'Tr rho1 (R_i R_j + R_j R_i)/2 per H2' in d
assert d.count(b'-S(rho1) + (1/2) Tr(A0 G1) - c0,') == 1        # (star) formula intact
assert d.count(b'-S(rho1) + (1/2) Tr(A0(G0) G1) - c0(G0).') == 1
assert b'Z0 = exp(-c0)' in d
assert d.count(b'<= 1.0e-12') == 1 and d.count(b'<= 5.6e-17') == 1  # rest of row intact
print('post-checks OK; r2 bytes:', len(d))
