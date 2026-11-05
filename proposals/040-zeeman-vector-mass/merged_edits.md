# Edits to merged text in chapters/appH-microscopic-proofs.tex (proposal 040 r2)

Flag: PRIOR-CLAIM-ERROR (032 and 034): sign of the logarithmic term in the Fin routine (s7/s6 of 032, l3_fin of 034 and 040). Each OLD string below was checked
with Python on the current file (CRLF normalised to LF; none of the strings spans a line break): count = 1 for each (see `merged_edits_check.out.txt`).
Verification of the new numbers: 032 by an actual rerun of `s7_resummed_sector_mp.py` with `+c*log(rho1*PH)` (`s7_corrected_sign.py`, output `s7_corrected_sign.out.txt`;
original output `s7_original_sign.out.txt`), all 9 frames; 034 by `t7_correct_034_forms.py`.

## Edit 1 (034 block, item (iii) of "Result in the class")
OLD (count 1):
```
is \(0.54\) and \(0.85\) (centre direction \(0.8\)), \(0.08\) and \(0.48\) (direction \(2.0\)) at one orbit point, and \(0.004\) and \(0.000\) at a second point
```
NEW:
```
is \(0.63\) and \(0.82\) (centre direction \(0.8\)), \(0.49\) and \(0.99\) (direction \(2.0\)) at one orbit point, and \(0.011\) and \(0.94\) at a second point
```
Number check: t7 gives 0.634/0.815, 0.492/0.994, 0.011/0.943. Confirmed, as in the gatekeeper's string.

## Edit 2 (032 block, "Einstein--Hilbert sector in a four-dimensional Landau model"), values
OLD (count 1):
```
its real part is about \(7.6\), \(8.1\), \(6.8\) in three Lorentz frames of \(F\) at \((a,b)=(0.7,1.3)\) (data \(\kappa,\alpha,y\) rotated, \(A\) fixed; imaginary parts between \(-0.32\) and \(0.20\)), and \(7.6\), \(5.9\), \(7.3\) in three frames at \((a,b)=(1.92,1.0)\) (imaginary parts \(1.05\)--\(1.28\))
```
NEW (gatekeeper's numbers, all confirmed by the rerun):
```
its real part is about \(1.05\), \(1.58\), \(0.27\) in three Lorentz frames of \(F\) at \((a,b)=(0.7,1.3)\) (data \(\kappa,\alpha,y\) rotated, \(A\) fixed; imaginary parts between \(-1.52\) and \(-1.00\)), and \(0.31\), \(-1.40\), \(0.03\) in three frames at \((a,b)=(1.92,1.0)\) (imaginary parts between \(-0.15\) and \(0.08\))
```
Rerun values (Fin/c): (0.7,1.3): 1.0507-1.4343i, 1.5762-0.9997i, 0.2726-1.5214i; (1.919,1.0): 0.3135+0.0814i, -1.3956-0.1486i, 0.0314+0.0649i; (0.4696,1.0), not quoted in the manuscript: 1.2375-1.4915i, 0.5978-1.6837i, 1.3091-1.5277i. Each equals the original value plus 2 ln s1 (-6.516-1.2i, -7.295-1.2i, -5.991-1.2i) to the printed digits. The Maxwell integrals are unchanged (c = 0), as in the original output.

## Edit 3 (same paragraph), frame spread
OLD (count 1):
```
the real part varies between frames by roughly \(20\%\)
```
NEW (CHANGED relative to the gatekeeper's wording "of the order of its mean": at (1.92,1.0) the spread, about 1.7, exceeds the mean, -0.35):
```
the real part varies between frames by an amount of the order of, or larger than, its mean
```
Spread check: (0.7,1.3) real parts 0.27..1.58 (mean 0.97); (1.92,1.0) -1.40..0.31 (mean -0.35).

## Unchanged in those paragraphs
The Maxwell-part statements ("about 30--45%" and "of order one"), the statement that the coefficient of the logarithm is the flux-independent A, and the 034 sentence "the quotient by \(\kappa\) has eigenvalues of both signs in every case (as has \(A\))" (tetrad part; corrected spectra of Re and Im of the yy form are mixed in all six cases, t7).
