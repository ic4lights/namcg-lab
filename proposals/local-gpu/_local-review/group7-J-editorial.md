# Local re-review r1 (remote/claude, 2026-11-18): group J + editorial

## 068-j-spherical-reduction-consistency: REJECT | FLAGS: PRIOR-CLAIM-ERROR | OPEN 1/0
The audit's central claim is false. The gpu CAS made two errors:
- It used the ansatz -N^2 dt^2 + dr^2/f, for which sqrt(-g) = N r^2/sqrt f. That is inconsistent with L = N r^2(...) and with eq:sss. The correct ansatz is -N^2 f dt^2 + dr^2/f + r^2 dOmega^2.
- It read R_a^c_b^d as R^{cd}_{ab}. The literal reading is g^{cp} g^{dq} R_{apbq}.
With the correct ansatz and the literal reading (scratch/gk_j_ecg_check.py, exact sympy): E_f|_{N=1} = 0, and E_N|_{N=1} = d/dr[2r(1-f) + 3 kappa B[f] - 2/3 Lambda_eff r^3]. The HEAD identities hold.
Required: do not integrate; restore HEAD:
- appH:3495-3496 -> "specified \(\mathcal P\), these reduced equations have been checked" / "symbolically:"
- appH:3504 -> "Thus \(N=1\) is a consistent vacuum branch of the reduced equations," / "and, with \(\alpha=-\kappa\), the lapse equation has first integral"
- appH:3548-3586: delete the audit paragraph and its trailing blank line.
- appH:3616-3620 -> HEAD's "Conditional on the stated symmetric reduction, the reduced-action / identities, first integral, regular-centre constraint, maximally / symmetric curvature relation, and asymptotic tail above have been / checked for the specified \(\mathcal P\). The cited Einstein-like"
Recommended (minor), after "consider the reduced action per unit time and angular volume" (appH:3475), insert: "for \(ds^2=-N(r)^2f(r)\,dt^2+dr^2/f(r)+r^2d\Omega^2\), with the mixed factor in~\eqref{eq:ECG} read as \(R_a{}^c{}_b{}^d=g^{cp}g^{dq}R_{apbq}\),"

## 071-j-ecg-passage-sync: REJECT | OPEN 1/0
- It copies the false 068 finding into ch09:234-245 and ch17:601-607.
- Restore the HEAD text of both passages (git show HEAD:chapters/ch09-ultraviolet.tex / ch17-agenda.tex).
- Other mentions (ch09:369-374, ch13, ch12:397, ch01:287-296) are consistent with the correct identities.

## 069-ch10-duplicate-bookkeeping-removal: AWRR (minor) | OPEN 0/0
- The ch05 table (L324-360) carries every removed row byte-identically, including the Fierz-Pauli caveat and the A_mu/B rows.
- Required: ch10:14-15 objective -> "\item relate the Goldstone and vector lines to the provisional sector bookkeeping of Section~\ref{sec:ch5-count};"
- Note: ch05:340 hard-codes "(Ch.~10)".

## 070-peters-elbadry-citation-completion: ACCEPT
- PetersMathews1963 (Phys. Rev. 131, 435) and Peters1964 (Phys. Rev. 136, B1224) were verified on Crossref.

Source reading: digest + targeted reads plus a grep over all chapters for J mentions. No full scan.
