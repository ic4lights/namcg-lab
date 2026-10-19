p = open('proposal-r1.md', encoding='utf-8').read()
blk = open('block-r2.tex', encoding='ascii').read().rstrip('\n')


def sub(old, new):
    global p
    assert p.count(old) == 1, old
    p = p.replace(old, new)


sub('# Proposal 034-leaf-commutator, round 1', '# Proposal 034-leaf-commutator, round 2')
sub('Bounded no-go plus a correction. Class:',
    'Bounded no-go plus a supersession of the 032 Landau model (032 is superseded, not falsified: it labelled itself "a model and not the leaf"). '
    'Revision round 2: findings F1-F3 of review-r1 applied by the review\'s corrected-snippet items 1-5; no new physics, no new computation. Class:')
sub('2. (Correction of 032.)', '2. (Supersession of the 032 model.)')
sub('Verdict: finite per centre variable (M_str term); EH form A survives only as the logarithm coefficient; not covariant; not sign-definite. No finite, covariant, sign-definite EH coefficient: no candidate missing link.',
    'Scoped verdict: Fin is finite per centre variable (M_str term); A survives as the logarithm coefficient and is non-covariant (030); the tetrad (yy) part of Fin is neither proportional to A nor sign-definite at the sampled points. '
    'Not tested: sign and covariance of the full Fin form (yy+cc+cross) and the window average over the centre variable (the cc part has positive real part in one sample, seed 21 theta 1.4: eigenvalues 0.006, 0.31, 1). '
    'No finite, covariant, sign-definite EH coefficient is obtained here; none is excluded either. No candidate missing link.')
sub('Class: PROGRAMME-CONDITIONAL bounded no-go with a correction of a model in an integrated paragraph.',
    'Class: PROGRAMME-CONDITIONAL bounded no-go with a supersession of a model in an integrated paragraph.')
sub('Digest (current at start, `dirty-chapters: yes` for the expected 032/033 integrations) + targeted reads:',
    'Round 2: review-r1 read in full; anchor re-verified in the current working tree (`\\section{Problem G: HBEV}` occurs once, appH line 2234, immediately after the 032 block whose last sentence is "This changes no ledger label; Problem~F remains open."). '
    'Round 1: digest (stale, `dirty-chapters: yes` for the expected integrations) + targeted reads:')
i = p.index('```latex')
j = p.index('```\n', i + 8) + 4
p = p[:i] + '```latex\n' + blk + '\n```\n' + p[j:]
sub('Block identical to `block-r1.tex` (no TAB, ASCII only; the integrator converts to CRLF). Scratch-copy compile outside the repo: 301 pages, 0 errors, 0 undefined, 0 multiply defined (`compile_check_r1.out.txt`;',
    'Block identical to `block-r2.tex` (generated from `block-r1.tex` by `make_block_r2.py`, which asserts each replacement matches exactly once; Python byte check in `block-r2.check.out.txt`: 0 TAB, 0 non-ASCII bytes, no CR; the integrator converts to CRLF). '
    'Scratch-copy compile outside the repo with block-r2.tex: `compile_check_r2.py`, `compile_check_r2.out.txt` (r1 gave 301 pages, 0 errors, 0 undefined, 0 multiply defined, `compile_check_r1.out.txt`;')
sub('Stale passages elsewhere: the 032 sentences',
    'Changelog r1 -> r2 (block-r2.tex vs block-r1.tex; five substitutions, exactly the review\'s corrected-snippet items 1-5):\n'
    '1. Heading: "correction of the preceding Landau model" -> "supersession of the preceding Landau model".\n'
    '2. "this is the commutator that the Jacobi identity forbids at the nilpotent order." -> "this commutator is inconsistent with the Jacobi identity at the nilpotent order with frozen coefficients."\n'
    '3. Checks paragraph, after the 2D-test sentence: "The two-dimensional test validates the prescription for a central \\(K\\); the identification of the leaf field \\(Y\\) with the seam insertion \\(P\\) is conditional on the nilpotent order and the frozen first jet."\n'
    '4. Result (iv), last sentence replaced by the scoped per-centre-variable sentence, which states that the full finite remainder and its window average were not tested.\n'
    '5. Closing paragraph: "the sign and covariance of the full finite remainder" added to the not-included list.\n'
    'No ledger label, numerical content or reference changed. In this proposal body "correction" of 032 is replaced by "supersession" throughout.\n\n'
    'Response to findings: F1 by item 4 (and the scoped verdict in Result item 4); F2 by items 1-2; F3 by item 3. No PRIOR-CLAIM-ERROR (032 superseded, not falsified). '
    'The review could not complete the non-ASCII check; it is done here in Python (`block-r2.check.out.txt`).\n\n'
    'Stale passages elsewhere: the 032 sentences')
sub('a correction (non-invariance of the 032 Landau EH model), a validated central model, c unchanged, Fin forms not proportional to A (sampled), no covariant sign-definite EH coefficient.',
    'a supersession (non-invariance of the 032 Landau EH model at F!=0, y!=0), a central model validated in a 2D toy for central K, c unchanged, the tetrad part of Fin not proportional to A and indefinite (sampled). '
    'It claims nothing about the full Fin form, its sign or covariance, or its window average.')
sub('- Treated the commutator as a structural correction of', '- Treated the commutator as a structural supersession of')
sub('Routine/structural: a correction of an integrated model plus a bounded no-go for the EH coefficient in the class.',
    'Routine/structural: a supersession of an integrated model plus a bounded no-go for the tetrad part of the finite remainder in the class.')
sub('- Fin finite, gauge-invariant parts, non-proportionality to A, indefinite spectra: numerical, three samples.',
    '- Fin finite, gauge-invariant parts, non-proportionality of the tetrad part to A, indefinite tetrad spectra: numerical, three samples. Full-Fin sign/covariance and window average: unresolved (untested).')
sub('- Vector-mass Zeeman term at order epsilon^2, weight-one terms, window average: unresolved.',
    '- Vector-mass Zeeman term at order epsilon^2, weight-one terms, window average, full-Fin sign and covariance: unresolved.')
k = p.index('## Remaining open step')
m = p.index('## Special instructions')
p = p[:k] + """## Remaining open step
Class of the no-go: Poisson limit, leaf CP^{1,2}, one loop, nilpotent symbol with central P at the seam, Lorentzian i-epsilon proper time, M_str term, sampled orbit points and centre directions. Ranked open avenues (review-r1), each relaxing a stated hypothesis:
1. Zeeman-dressed vector-mass term at order epsilon^2 (matrix-valued Gaussian engine with P at the seam): decides whether the mass-linear coefficient is finite; the e^{+2x} growth is the present obstruction.
2. Window average of the full Fin(zeta) (tetrad, charge and cross parts), testing sign-definiteness and covariance of the actual coefficient (relaxes "per centre variable").
3. Weight-one terms and gradients of y^k and y^c, ratio up to 0.5 (relaxes the nilpotent order).
4. Spectral, mode-by-mode definition of the vector sector with ghost subtraction; non-perturbative or positive mass.
5. Moyal order and wider sampling.
Neither F nor E is closed.

""" + p[m:]
open('proposal-r2.md', 'w', encoding='utf-8', newline='\n').write(p)
