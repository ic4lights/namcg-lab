#!/usr/bin/env python3
"""Build proposal-r2.md from proposal-r1.md: carry the R1-R3 scope changes into the proposal text."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(HERE, 'proposal-r1.md'), encoding='utf-8').read()

changes = """## Changes r1 -> r2

| # | Review finding | Change |
|---|---|---|
| 1 | F1 (minor): (iii) claimed failure of domination for gamma_j unbounded; domination step implicit | R2 (two replacements) applied verbatim: non-integrability is for any real gamma in the mass term; the domination conclusion is restricted to gamma converging to a finite limit, and the step "a dominating function would also dominate the integrand at eps=0 on Lambda_inf with that limit of gamma" is stated. Proposal: Result item 2, order-of-limits answer, Step 6, claim classification and Remaining open step carry the same restriction. |
| 2 | F2 (minor): "there" ambiguous in the gamma <= 0 sentence | R1 applied verbatim: "For gamma <= 0, where -pi/2 <= phi <= 0, the interval (-pi, 2phi-pi] is empty, and the inertia argument of (i) of the preceding paragraph applies instead." |
| 3 | F3 (minor): closing clause repeated 056's | R3 applied verbatim: "... so they select no signature, and the positive mass does not discharge Assumption~ref{ass:lorentzian}." |
| 4 | F4 (bookkeeping) | apply_check and scratch build re-run; new hashes below. r1 insert kept as appH_insert.r1.tex (7714 bytes, f7fbbade...af82). Edits applied by apply_r2_edits.py (r1 hash checked; each old string once before, each new string once after; output apply_r2_edits.txt). |

No other change to the insert. The mathematics is unchanged.

"""

reps = [
    ('# Proposal 057-mass-plane-class, round 1\n', '# Proposal 057-mass-plane-class, round 2\n\n' + changes),
    ('   - So for fixed γ > 0, no linear contour reached from the Hermitian contour carries the dominated-convergence argument used for γ ≤ 0. This explains the "admissible u closes like ε/γ" already recorded in appH.',
     '   - This non-integrability holds with any real γ in the mass term.\n   - So for fixed γ > 0, and for γ/ε → ∞ with γ converging to a finite limit, no linear contour reached from the Hermitian contour, fixed or convergent as ε → 0, carries the dominated-convergence argument used for γ ≤ 0: a dominating function would also dominate the ε = 0 integrand on Λ_∞ with that limit of γ. For γ_j → ∞ only the rank-one and reality statements are claimed. This explains the "admissible u closes like ε/γ" already recorded in appH.'),
    ('With ε → 0 at fixed γ > 0, or γ/ε → ∞, the linear-contour reduction is unavailable,',
     'With ε → 0 at fixed γ > 0, or γ/ε → ∞ with γ converging to a finite limit, the linear-contour reduction is unavailable,'),
    ('  - So ∫|integrand| ≥ C∫^∞ R²⁶ · R²⁴ · R⁻⁹ dR = ∞.\n',
     '  - So ∫|integrand| ≥ C∫^∞ R²⁶ · R²⁴ · R⁻⁹ dR = ∞. The mass part is bounded on the shift ball for any real γ, so this holds with any real γ in the mass term.\n- **Domination step (r2).** If γ_j → γ_∞ finite, the integrands on Λ_j converge pointwise to the ε = 0 integrand on Λ_∞ with γ_∞; a dominating function G would satisfy G ≥ |that limit|, which is not integrable, so no integrable G exists. If γ_j → ∞, the pointwise limit of the moduli is supported on y = 0 and Fatou gives nothing; no domination statement is made there.\n'),
    ('| N = 2: ε = 0 integrand on Λ_∞ not absolutely integrable | established (N = 2) |',
     '| N = 2: ε = 0 integrand on Λ_∞ not absolutely integrable, any real γ in the mass term | established (N = 2) |\n| No dominated convergence along reached families for fixed γ > 0, or γ/ε → ∞ with γ converging to a finite limit | established (N = 2) |\n| Domination statement for γ_j → ∞ | not claimed |'),
    ('(i) \\emph{Classes of planes.} ... [full text in appH_insert.tex; 7714 bytes LF]',
     '(i) \\emph{Classes of planes.} ... [full text in appH_insert.tex; 8046 bytes LF]'),
    ('- insert, LF form: 7714 bytes, sha256 f7fbbade4567d6843f13fe50f06ccb457cc78ac230863e1505b0bdb8f074af82;\n- insert, CRLF form: 7724 bytes, sha256 aa8fa08b3402bfe2b98542a6e1ab9367b2e799bf29bd0b6d4d758d9f454962a3;\n- resulting appH: 569192 bytes, sha256 e97ec8301e67d8e7f05d207d9425ce2a2ad723694e6488adda436dc6cb9c07f0, CRLF 3266, bare LF 0.',
     '- insert (r2), LF form: 8046 bytes, sha256 4e0a85d101eaa1300a6206ed8760d83e4c5a74950b8b789d8fcfc3d7c20c0a7d;\n- insert (r2), CRLF form: 8056 bytes, sha256 bcc5ccef706012f26ae998ed121eb4e7aa025391cbb37da004991def5bc49253;\n- resulting appH: 569524 bytes, sha256 9443341b74f991d49fee3b08830dd44da7f9a12245922f52aaa193b0bd607bcd, CRLF 3266, bare LF 0;\n- r1 insert kept as appH_insert.r1.tex: 7714 bytes, sha256 f7fbbade4567d6843f13fe50f06ccb457cc78ac230863e1505b0bdb8f074af82.'),
    ('- Both passes exited 0. Output: **365 pages**, 0 "undefined" and 0 "multiply" matches in the log.',
     '- r2 rebuild: both passes exited 0. Output: **365 pages**, 0 "undefined" and 0 "multiply" matches in the log. The appH in the build copy has the expected resulting hash 9443341b...7bcd.'),
    ('- `edit_insert.py`, `edit_insert2.py`, `edit_insert3.py`: the drafting edits applied to the insert, recorded for transparency. They are idempotent.',
     '- `edit_insert.py`, `edit_insert2.py`, `edit_insert3.py`: the r1 drafting edits applied to the insert, recorded for transparency. They are idempotent.\n- `apply_r2_edits.py` → `apply_r2_edits.txt`: the r1 → r2 replacements R1, R2a, R2b, R3 (r1 hash check; uniqueness of old and new strings).\n- `make_r2.py`: builds this file from proposal-r1.md.'),
]
for old, new in reps:
    c = s.count(old)
    assert c == 1, (c, old[:70])
    s = s.replace(old, new)
    assert s.count(new) == 1
open(os.path.join(HERE, 'proposal-r2.md'), 'w', encoding='utf-8', newline='\n').write(s)
print('proposal-r2.md written', len(s.encode('utf-8')), 'bytes;', len(reps), 'replacements')
