"""patch_r2.py - apply the round-2 wording fixes (gatekeeper findings 1-3, 4, 5, 7)
to proposals/077-g-selrule-copyinv/insert-r1.tex IN PLACE (byte replacements on the
single content line; CRLF terminal preserved; no other byte changes).

Run from the repository root:
  python -I proposals/077-g-selrule-copyinv/patch_r2.py > proposals/077-g-selrule-copyinv/patch_r2.out 2>&1
Exit 0 means: every old clause occurred exactly once, all replacements applied, and
the full insert hygiene (the simulate_apply_077.py scan list) re-passes on the patched
file. Prints old/new content sha256 and sizes.
"""
import hashlib

p = 'proposals/077-g-selrule-copyinv/insert-r1.tex'
raw = open(p, 'rb').read()
assert raw.endswith(b'\r\n') and b'\r' not in raw[:-2] and b'\n' not in raw[:-2]
body = raw[:-2]
old_sha = hashlib.sha256(body).hexdigest()

REP = [
    # finding 1 + finding 2 (mandatory): corrected 1-based D formula matching the
    # shipped code statistic, and the U_2 vanishing clause (U_2 vanishes exactly at
    # equal moduli, NOT at a generic tiling; verified in verify_r2_clauses.py)
    (rb"tiling of this spectrum by the one-copy multiset is measured by the relative gap \(D=\max_k(e_{(k+1)q-1}-e_{kq})/\max_k|e_k|\) and the fourth-moment signature excess \(U_2=\operatorname{Tr}\widetilde Q^{4}/(2q(\operatorname{Tr}\widetilde Q^{2}/(2q))^{2})-1\), which vanish at tiling.",
     rb"tiling of this spectrum by the one-copy multiset is measured by the relative gap \(D=\max_{k=1,2}\bigl(e_{kq}-e_{(k-1)q+1}\bigr)/\max_j|e_j|\), which vanishes at tiling, and by the fourth-moment signature excess \(U_2=\operatorname{Tr}\widetilde Q^{4}/(2q(\operatorname{Tr}\widetilde Q^{2}/(2q))^{2})-1\), which vanishes exactly when the nonzero eigenvalues have equal modulus (in particular at a tiling by the symmetric multiset \(\{-\varepsilon,\varepsilon\}\)), and at a generic tiling measures the \(\operatorname{Im}\alpha\) shift, decaying as \(O(1/N)\) below the leading order in the matched-scale ensembles tested (numerical)."),
    # finding 3: q=32 window extent is {4q^2, 8q^2} only (CAP_N = 8192)
    (rb"to \(16q^{2}\) through \(q=32\) give slopes",
     rb"to \(16q^{2}\) through \(q=16\) and to \(8q^{2}\) at \(q=32\) give slopes"),
    # finding 4: CV 0.4 is neither the variance multiplier's CV (0.98) nor exact for
    # the std multiplier (0.428); state the std multiplier's CV 0.43 (verified)
    (rb"for a lognormal scale mixture of coefficient of variation \(0.4\)",
     rb"for a lognormal per-copy scale mixture whose standard-deviation multipliers have coefficient of variation \(0.43\)"),
    # finding 5: scope "only" to the tested classes
    (rb"and exact tiling is realized only on thin families,",
     rb"and exact tiling is observed, in the tested classes, only on thin families,"),
    # finding 7: s6 measures |alpha|/|w| with the FULL row vector w (label fix;
    # the ratio to |alpha|/|w_perp| tends to 1, slope unchanged)
    (rb"at matched iid scales \(|\alpha|/\|w_\perp\|\) decays",
     rb"at matched iid scales \(|\alpha|/\|w\|\) decays"),
]

nb = body
for i, (o, n) in enumerate(REP):
    c = nb.count(o)
    assert c == 1, 'replacement %d: old clause count %d' % (i, c)
    nb = nb.replace(o, n, 1)
new = nb + b'\r\n'

# full hygiene re-scan (mirrors simulate_apply_077.py)
assert all(b < 128 for b in new), 'non-ASCII byte'
assert new.endswith(b'\r\n')
body2 = new[:-2]
assert b'\r' not in body2 and b'\n' not in body2, 'must remain ONE content line'
for tok in (b'\\ref', b'\\eqref', b'\\cite', b'\\label', b'$', b'[', b']'):
    assert body2.count(tok) == 0, 'forbidden token ' + repr(tok)
low = body2.lower()
for w in (b'status', b'priority', b'completion', b'open', b'derived',
          b'programme', b'critical'):
    assert low.count(w) == 0, 'forbidden word ' + repr(w)
assert body2.count(b'\\emph{') == 1, 'exactly one \\emph header'
assert body2.endswith(b'they close nothing in Problem~G.')
# sanity: the corrected tokens are present exactly once
for tok in (rb'\max_{k=1,2}\bigl(e_{kq}-e_{(k-1)q+1}\bigr)',
            rb'\{-\varepsilon,\varepsilon\}',
            rb"through \(q=16\) and to \(8q^{2}\) at \(q=32\)",
            rb'coefficient of variation \(0.43\)',
            rb'observed, in the tested classes, only on thin families',
            rb'at matched iid scales \(|\alpha|/\|w\|\)'):
    assert body2.count(tok) == 1, 'expected token once: ' + repr(tok)
# and the round-1 defective strings are gone
for tok in (rb'\max_k(e_{(k+1)q-1}-e_{kq})', rb'which vanish at tiling',
            rb'through \(q=32\) give', rb'variation \(0.4\)',
            rb'is realized only on thin'):
    assert body2.count(tok) == 0, 'stale token remains: ' + repr(tok)

open(p, 'wb').write(new)
print('content: %d -> %d B' % (len(body), len(body2)))
print('old content sha256 %s' % old_sha)
print('new content sha256 %s' % hashlib.sha256(body2).hexdigest())
print('old file     sha256 %s' % hashlib.sha256(raw).hexdigest())
print('new file     sha256 %s' % hashlib.sha256(new).hexdigest())
print('ALL REPLACEMENTS APPLIED; HYGIENE RE-PASS')
