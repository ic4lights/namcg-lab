"""apply_r2.py (proposal 045): save the r1 insert as appH_insert_r1.tex and apply exactly the review-r1
replacements R1-R8 (R6 in three parts) to appH_insert.tex; each old string must occur exactly once.
Then a byte check of the result."""
import shutil, re
shutil.copyfile('appH_insert.tex', 'appH_insert_r1.tex')
s = open('appH_insert.tex', encoding='utf-8').read()
reps = [
('R1', r"Hence, in the units \(c\) of the preceding paragraph, \(c_T=",
       r"Hence, in this averaged-frame reading, which is not the fibre trace treated below, and in the units \(c\) of the preceding paragraph, \(c_T="),
('R2', r"for the finite parts, without the dressed density of the paragraph on local frame rotations.",
       r"for the finite parts, without the dressed density of the paragraph on local frame rotations; this inherits the equality of the Dirac cone value with the coefficient of the Einstein term in the index density, which the preceding paragraph does not derive."),
('R3', r"for a real wave averaged over its phase, the index density at a fibre point is",
       r"for a real wave averaged over its phase, and taking the index density to be the torsion invariant of the four-coordinate class evaluated on the frame at the fibre point (an identification carried over from that class and not recomputed for the leaf \(\mathbb{CP}^{1,2}\)), the index density at a fibre point is"),
('R4', r"On the six polarisations neither form lies in the span of",
       r"On the six polarisations, with the inert amplitudes set to zero, neither form lies in the span of"),
('R5', r"makes their sum proportional to \(\mathrm{EH}(\bar h)\) or covariant (exact linear algebra",
       r"makes their sum proportional to \(\mathrm{EH}(\bar h)\) or covariant under the Lorentz group of the frozen point (a form that also depends on the background vector \(y^\mu/\ell\) is not tested; exact linear algebra"),
('R6a', r"For this trace no single \(G_T\) covers the six polarisations or the five traceless ones,",
        r"For this trace, with the inert amplitudes set to zero rather than eliminated, no single \(G_T\) covers the six polarisations or the five traceless ones,"),
('R6b', r"so the mixed-term part of the fixed-state gap vanishes on no traceless polarisation.",
        r"so the mixed-term part of the fixed-state gap vanishes on no generalised eigendirection of the traceless polarisations."),
('R6c', r"the interpolation between the two regimes, or the fibre spectrum.",
        r"the interpolation between the two regimes, the elimination of the inert amplitudes or the fibre spectrum."),
('R7', r"\(m=M^{45}\))", r"\(m=M^{45}\), units \(R=1\))"),
('R8', r"five wave vectors including a time-like one", r"five wave vectors including two time-like ones"),
]
out = []
for tag, a, b in reps:
    n = s.count(a)
    out.append(f"{tag}: old string occurrences = {n}")
    assert n == 1, (tag, n)
    s = s.replace(a, b)
open('appH_insert.tex', 'w', encoding='utf-8', newline='\n').write(s)
bts = s.encode('utf-8')
ctrl = sum(1 for c in bts if c < 32 and c != 10)
out.append(f"r2 bytes {len(bts)}; TAB {bts.count(9)}; CR {bts.count(13)}; non-ASCII {sum(c > 127 for c in bts)}; control (non-LF) {ctrl}")
out.append(f"brace balance {s.count('{') - s.count('}')}; \\( - \\) {s.count(chr(92)+'(') - s.count(chr(92)+')')}; \\[ - \\] {s.count(chr(92)+'[') - s.count(chr(92)+']')}")
out.append(f"\\paragraph {s.count(chr(92)+'paragraph')}; \\label {s.count(chr(92)+'label')}")
print("\n".join(out))
open('apply_r2.out.txt', 'w', newline='\n').write("\n".join(out) + "\n")
