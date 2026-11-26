#!/usr/bin/env python3
"""Second pass on proposal-r2.md: restriction in Remaining open step, and the review's avenue ranking."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, 'proposal-r2.md')
s = open(p, encoding='utf-8').read()
reps = [
    ('That needs non-linear (thimble) contours or a direct oscillatory analysis. Even a positive answer',
     'That needs a direct oscillatory or conditionally convergent analysis, or non-linear (thimble) contours. The linear-contour exclusion of dominated convergence is stated only for γ converging to a finite limit; families with γ_j → ∞ are covered only by the rank-one and reality statements. Even a positive answer'),
    ('**Ranked open avenues for the queue:**\n',
     '**Ranked open avenues for the queue** (r2: the review ranks the direct oscillatory analysis first, as the only finite-N route left for fixed γ > 0; I adopt that order, so items 1 and 2 below are swapped in priority):\n'),
]
for old, new in reps:
    assert s.count(old) == 1, old[:60]
    s = s.replace(old, new)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(s.encode('utf-8')))
