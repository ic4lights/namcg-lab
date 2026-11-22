import hashlib
NL = chr(10)
def L(*lines): return NL.join(lines)
def sha(f): return hashlib.sha1(open(f,'rb').read()).hexdigest()

assert sha('insert-bilocal-coinc.tex') == '2cca5842ace0c3a1e67e6712d2c521990023f508'
assert sha('run_induced.out') == '32b3701886be98430b5430d00fc4f2c49163992a'
b = open('proposal-r1.md','rb').read()
assert b.count(chr(13).encode()) == 0
s = b.decode('utf-8')

def rep(old, new):
    global s
    n = s.count(old)
    assert n == 1, ('COUNTFAIL', n, old[:70])
    s = s.replace(old, new)

rep('# Proposal 110-cd1-bilocal-coincidence-evaluation, round 1',
    '# Proposal 110-cd1-bilocal-coincidence-evaluation, round 2')

rep(L('never enters the symmetric sector; the full symmetric O(ell^2) sector',
      '   decomposes as (profile) + (radial e_rs) + (mixed e-w) + the',
      "   anticommutator connector (`run_induced.out`). The item-109 draft claims"),
    L('never enters the symmetric sector; the full symmetric O(ell^2) sector',
      '   decomposes as (profile) + (radial e_rs) + (radial-gradient x e) +',
      '   (mixed e-w) + the anticommutator connector',
      "   (`run_induced.out`, corrected r2 identity in R6). The item-109 draft claims"))

rep(L('is exactly F_rs eta + F_0 sym(eta E_rs) + F_0 sym(eta(w_r e_s + w_s e_r))',
      '+ sym(F_r eta w_s + F_s eta w_r) + F_0 (1/2) sym(eta {w_r,w_s}), i.e. the',
      'connector-soldering term is exactly (1/2)(1+sigma/v)^2 sym(eta {w_r,w_s})',
      '(the printed claim "soldering-type connector first at O(ell^2)" with its',
      'coefficient made explicit); I6, I6b: sym(eta F_12) = 0, sym(eta d_1 w_1) ='),
    L('is exactly F_rs eta + F_0 sym(eta E_rs) + F_0 sym(eta(w_r e_s + w_s e_r))',
      '+ sym(F_r eta w_s + F_s eta w_r) + sym(F_r eta e_s + F_s eta e_r)',
      '+ F_0 (1/2) sym(eta {w_r,w_s}), with F_0 = (1+a)^2 = (1+sigma/v)^2',
      'and F_r = (1+a) a_r, where a_r = partial_r(sigma/v)|0 is the linear',
      'coefficient of delta; i.e. the connector-soldering term is exactly',
      '(1/2)(1+sigma/v)^2 sym(eta {w_r,w_s})',
      '(the printed claim "soldering-type connector first at O(ell^2)" with its',
      'coefficient made explicit). Ground truth for I7 is direct',
      'differentiation of G = f eta U E: the r1 exactly-list omitted the',
      'term sym(F_r eta e_s + F_s eta e_r) and the battery targets G2 and',
      'tgt7 omitted it too, so the r1 I7 check was tautological off-vacuum',
      '(review-r1 finding 1 and its S1 ground-truth check); the corrected',
      'identity above equals the direct-differentiation ground truth',
      'exactly. The narrower claims pinned in the payload are unaffected:',
      'the connector-quadratic part and the connector-free O(ell) sector',
      'stand as printed. I6, I6b: sym(eta F_12) = 0, sym(eta d_1 w_1) ='))

rep('F_12(0), where B_{mu nu} = d_mu w_nu(0), C_mu = w_mu(0), and',
    'F_12(0), where B_{rho mu} = d_mu w_rho(0), C_mu = w_mu(0), and')

rep(L('- HEAD anchor (43 bytes): `sign fixed by the transport convention). `',
      '- TAIL anchor (81 bytes): `The representation content is admissible where the linear Repair~I`',
      '- Joined anchor HEAD+TAIL: occurrence count = 1 (verified by grep and by',
      '  the splice assert). The block is inserted BETWEEN the two anchors; both'),
    L('- HEAD anchor (41 chars; ASCII, so 41 bytes): `sign fixed by the transport convention). `',
      '- TAIL anchor (66 chars; ASCII, so 66 bytes): `The representation content is admissible where the linear Repair~I`',
      '  (r1 stated 43/81; corrected at r2 by python len on the anchor',
      '  strings, review-r1 finding 2: bookkeeping only).',
      '- Joined anchor HEAD+TAIL: occurrence count = 1 (re-verified at r2 by',
      '  count-only python on the live appH: HEAD 1, TAIL 1, joined 1; the',
      '  integrator asserts the counts, not the lengths). The block is',
      '  inserted BETWEEN the two anchors; both'))

rep(L('Digest status: `python scripts/make_digest.py --check` printed "DIGEST',
      'STALE (head changed)" at run start; per protocol 3 the digest was NOT',
      'relied on and I used live targeted reads'),
    L('Digest status at r1 run start: `python scripts/make_digest.py --check`',
      'printed "DIGEST STALE (head changed)"; at r2 run time it prints DIGEST',
      'CURRENT (head 23266972cd07dd01497abe5e0962810fa059db63, dirty-chapters:',
      'no). r2 required reading: review-r1.md (sha1',
      '5fc150de1587cc15fbe4cba31d893169405ccd14), read in full; r2 adds no',
      'manuscript reading beyond the count-only appH anchor re-verification.',
      'Per protocol 3 the r1 digest was NOT relied on and I used live targeted reads'))

rep('- check_induced_expansion.py c857d4f016c48d0e66d0438a1bde0766bc187d79',
    '- check_induced_expansion.py ' + sha('check_induced_expansion.py')
    + NL + '  (r2: G2 target corrected per review-r1 finding 1)')

rep('- check_induced_expansion_part3.py 4035bdf7e72ded2bdfb707a178c17b1505211b21',
    '- check_induced_expansion_part3.py ' + sha('check_induced_expansion_part3.py')
    + NL + '  (r2: tgt7 target corrected per review-r1 finding 1)')

rep('- run_induced.out 32b3701886be98430b5430d00fc4f2c49163992a',
    '- run_induced.out ' + sha('run_induced.out')
    + NL + '- run_induced_r1_outdated.out 32b3701886be98430b5430d00fc4f2c49163992a'
    + NL + '  (superseded r1 battery output, inert provenance; the r2 re-run of the'
    + NL + '  corrected scripts is byte-identical because the added terms enter the'
    + NL + '  check targets, not the printed PASS lines)')

rep(L('   sym(G2_rs) = profile + radial + mixed + (1/2) F0 sym(eta{w_r,w_s});',
      '   sym(eta F_12) = 0.'),
    L('   sym(G2_rs) = profile + radial + (Fd1[r] eta Ed1[s] + Fd1[s] eta',
      '   Ed1[r]) + mixed + (1/2) F0 sym(eta{w_r,w_s});',
      '   sym(eta F_12) = 0. r2 correction: the r1 G2/tgt7 targets omitted',
      '   the Fd1*eta*Ed1 terms (review-r1 finding 1); the corrected targets',
      '   match the direct-differentiation ground truth (review-r1 S1) and',
      '   the r2 re-run is byte-identical to the stored output, whose r1',
      '   copy is kept as run_induced_r1_outdated.out.'))

rep(L('rational instances); re-runs verified byte-identical to the stored .out',
      'files (cmp) on 2026-11-22.'),
    L('rational instances); re-runs verified byte-identical to the stored .out',
      'files (cmp) on 2026-11-22; in r2 the induced battery was corrected per',
      'review-r1 finding 1 and re-run (output byte-identical), the other',
      'three batteries untouched.'))

rep(L('   part of the O(ell^2) symmetric coefficient (the full symmetric part',
      '   also contains sigma-gradient x w and e x w cross terms; claiming more',
      '   would be false off-vacuum).'),
    L('   part of the O(ell^2) symmetric coefficient (the full symmetric part',
      '   also contains sigma-gradient x w, sigma-gradient x e and e x w',
      '   cross terms; claiming more would be false off-vacuum). r1 listed',
      '   only the first and third families; r2 restores the',
      '   sigma-gradient x e family consistently in Result 3, R6 and the',
      '   battery targets (review-r1 finding 1).'))

rep(L('- The 109 sentence about the right action of the orthogonal group of g+',
      '  is correct as printed (L6 verifies it); do not edit it.'),
    L('- The 109 sentence about the right action of the orthogonal group of g+',
      '  is correct as printed (L6 verifies it); do not edit it.',
      '- r2 addendum: the payload is unchanged (insert-bilocal-coinc.tex',
      '  sha1 2cca5842ace0c3a1e67e6712d2c521990023f508, compile cert',
      '  unchanged at that sha). Only check_induced_expansion.py (G2 gained',
      '  + Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r]) and',
      '  check_induced_expansion_part3.py (tgt7 gained the symmetrized same',
      '  term) changed among the scripts; fix_batt.py in this folder',
      '  reapplies exactly those two edits with count asserts. Verify the',
      '  corrected I7 identity in R6 by direct differentiation of',
      '  G = f eta U E, re-run the induced battery (expect ALL CHECKS',
      '  PASS), and check the anchor counts (not lengths) on the live appH',
      '  before splicing.'))

CH = L('## r1 -> r2 changelog',
 '',
 'Round 2 is a record-and-battery correction round on the gatekeeper',
 'verdict ACCEPT WITH REQUIRED REVISIONS (review-r1.md). The physics of',
 'the pinned payload was verified there and is unchanged; no manuscript',
 'text differs from round 1. Changes, keyed to the review findings:',
 '',
 '1. Finding 1 (major). R6/Result 3: the "exactly" I7 decomposition',
 '   gains the term sym(F_r eta e_s + F_s eta e_r), with F_0 = (1+a)^2 =',
 '   (1+sigma/v)^2 and F_r = (1+a) a_r, a_r = partial_r(sigma/v)|0; with',
 '   this term the identity equals the direct-differentiation ground',
 '   truth of G = f eta U E (review-r1 S1). Battery: G2 in',
 '   check_induced_expansion.py and tgt7 in check_induced_expansion_part3.py',
 '   gained the matching Fd1*eta*Ed1 terms (r1 omitted them on both sides,',
 '   making the r1 I7 check tautological off-vacuum). run_induced.out',
 '   re-run from the corrected scripts; its byte content is unchanged',
 '   (the terms enter the check targets, not the printed lines), and the',
 '   r1 output is archived as run_induced_r1_outdated.out (sha1',
 '   32b3701886be98430b5430d00fc4f2c49163992a). The Decision 2',
 '   cross-terms parenthetical is updated to match. The payload is',
 '   byte-identical (sha1 2cca5842ace0c3a1e67e6712d2c521990023f508): it',
 '   claims only the connector-quadratic part and the connector-free',
 '   O(ell) sector, both unaffected by the correction.',
 '2. Finding 2 (minor). Anchor contract: HEAD/TAIL lengths corrected to',
 '   the measured 41/66 chars (r1 said 43/81); occurrence counts',
 '   re-verified 1/1/1 on the live appH; the integrator contract (assert',
 '   counts, not lengths) unchanged.',
 '3. Finding 3 (minor). R2 body: the B-convention sentence now reads',
 '   B_{rho mu} = d_mu w_rho(0), matching the script convention under',
 '   which F_12 = B21 - B12 - [C1, C2].',
 '4. Finding 4 (minor). Source reading records the r2 digest state',
 '   DIGEST CURRENT (head 23266972cd07dd01497abe5e0962810fa059db63,',
 '   dirty-chapters: no) and review-r1.md as required reading.',
 '',
 'Result and claim classification are UNCHANGED: conditional',
 'in-hypothesis evaluations / derivation-grade inputs to Problem C',
 'Missing-step (i); nothing is closed (rule 3); no status, priority or',
 'completion label is touched (rule 2); the payload, labels and',
 'references are unchanged.',
 '',
 '## Milestone assessment')
rep('## Milestone assessment', CH)

assert s.count('sym(F_r eta e_s + F_s eta e_r)') >= 2
assert s.count('r1 -> r2 changelog') == 1
assert s.count('(43 bytes)') == 0 and s.count('(81 bytes)') == 0
assert s.count('B_{mu nu}') == 0
bad = [ord(c) for c in s if ord(c) < 32 and c != NL]
assert not bad, bad[:5]
assert sha('insert-bilocal-coinc.tex') == '2cca5842ace0c3a1e67e6712d2c521990023f508'
open('proposal-r2.md','wb').write(s.encode('utf-8'))
print('WROTE proposal-r2.md', sha('proposal-r2.md')[:12], len(s.split(NL)), 'lines')
