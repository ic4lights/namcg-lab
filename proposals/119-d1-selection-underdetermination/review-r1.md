# Review 119 round 1

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The package's central one-loop machine — scalar structure tensors, u/su gauge channel coefficients, the quadratic beta_r system, the fixed-ray threshold analysis, the scheme teeth, and the constant-field Moyal collapse — survives independent re-derivation on every number I tested with my own off-default inputs; acceptance is withheld only for two wording/consistency defects in the manuscript-bound payload (an internally inconsistent endpoint in the iff clause, a group-data conflation in the beta clause) plus one false-by-construction symmetry claim (shift symmetry against the actual eq:Smicro lift).

## Source reading
digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT`, but the tree is dirty (`dirty-chapters: yes`), so the check is weak by the known ledger protocol finding; I therefore re-read every relied passage live. Files read in full: `proposals/119-d1-selection-underdetermination/{proposal-r1.md, manifest.md, notes.md, insert-overdetermination-r1.tex, out-r119.txt, out-r119-run1-fail.txt}` and targeted ranges of `chapters/appH-microscopic-proofs.tex` (Problem D ledger L765-771; appH tail L1708-1718; anchor region), `chapters/ch03-matrix-action.tex` (L119, L142-157, L215-228, L240-245, L310, L335, L345-363), `chapters/ch17-agenda.tex` L329-362, `reports/ledger.md` tail. Full-scan trigger 3(c) ruled **not triggered**: the payload is a purely additive `\emph{...}` paragraph changing no definition, assumption, scope statement or status; counter 2/5. No unreadable files.

## Claim under review
Presentation-A vs Presentation-B selection underdetermination at the one-loop level: with the calibrated `STrM4 = Tr(H_W H_W)` machine, the (c3, c2, c1, c0) couplings of a quartic-in-X potential obey a closed one-loop system whose fixed-ray structure has a strong-coupling threshold `w* = 64 + 16*sqrt(42) ~ 167.69 > 16*pi^2 ~ 157.91` (n=4, v4=0, u(4)); sign(c1) and the gauge channel data are UV-scheme/group content, not loop structure; constant-field Moyal corrections collapse to (total) derivatives; shift symmetry of the lift is not available for the eq:Smicro lift as written. Original target: **Problem D (local Lorentz), ledger verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."** Status: OPEN. Priority: CRITICAL PATH. The payload explicitly does not close D or D1; it records an underdetermination constraint on what any selection argument can cite.

## Checks performed
**STEP 0 baseline (my values):** appH sha1[:12] `2ed53c7778c1`, 843649 B; anchor `\section{Problem E: signature}` count 1 at byte 290106 — both match dispatch pins.

**Reproduction pack (exact re-runs, `python -I -B`):**
- `verify_r119.py` run twice by me: output byte-identical to pinned `out-r119.txt` (`009de59d50ac`/6476, ends `TOTAL 62/62 PASS` / `ALL CHECKS DONE 119`) — two independent determinism reruns.
- run-1 failure pin `out-r119-run1-fail.txt` (`19f92196bf46`/6272) confirmed raw: FAIL D4 + FAIL G3, `TOTAL 59/61`, `FAILURES: 2`. Both fixes are check-side only: D4 grid point (0,60) violated the interior antecedent ((0-60-64)^2=15376>10752), moved to (0,30) (8836<10752) — mathematics untouched; G3 compared a scalar trace to a zero matrix — replaced plus new companion G3b; I independently re-established the underlying claims (GK19/GK20 below). The D7 off-default two-root tooth survives at w=200: r = 3/14, 1.
- `gen_payload_119.py` run twice: byte-identical, `GEN OK 119`, join-guard positive control fires; payload `3b4c2d0794a9`/4704.
- `cert-r119p.py` in **my own fresh temp tree**: `CERT PASS`, `CERT-EXIT=0`, two pdflatex passes rc=0, 0 undefined/multiply-defined refs (pre-compaction; package `out-cert-r119p.txt` e87ae59a3c4a/393 consistent).
- POST byte-reconstruction from the LIVE tree with `replace(anchor, payload+CRLF+anchor,1)`: **848355 B, sha1 `eaea0964e7f50c27c24540b9ac523c443af873d7`** — byte-exact to pin.
- 118-folder audit: `proposal-r1-superseded-F1F2.md` byte-identical to old r1 pin (`4a6fa455daa2`/48887); diff of superseded vs current r1 is **exactly** F1 `x = (1/sqrt(2 eps), 0, 0, 0)` and F2 `sigma^2 = w^2 = ...` (one occurrence each); new pins `b6c55d51a73f`/48902, manifest `8df4f47c7d19`/13057; manifest section 10 records old/new.
- Manifest self-hash: substituting the printed token into the 40-hex cell reproduces `1d18781c772c8ef31665aacf7582c40df75fac07` — rule verified reproducible (NOTE: the parenthetical "fixed length" is inaccurate, token is 38 B vs cell 40 B; the Recheck procedure itself works).

**Independent re-derivation (my own scripts `scratch/gk119/gk_indep.py`, `gk20b.py`, 32 checks; side-by-side mine vs package):**
| quantity | mine | package | agree |
|---|---|---|---|
| T33/T32/T22 tensors n=2,3,4 (own exact Hessians, residual 0) | (32(n+4),96)/(96,32(n+4))/(0,128(n+1)) | same (B1) | yes |
| n=4 (A33,B32->B33) and ratio | (256,96), 3/8 | (256,96), 3/8 (B2) | yes |
| off-diagonal bilinear identity (c3=2,c2=3) | S-pred = 0 | 0 (B3) | yes |
| u(4)/u(5) gauge: S, (TrX)^2 coeff | 4 TrX^2 / 0; 5 TrX^2 / 0 | C2/C6 | yes |
| su(N) (A,B) own Gell-Mann-type orthonormal bases N=2..5 | (1,1/4),(7/3,1/9),(7/2,1/16),(23/5,1/25) | C4 | yes |
| su(4) mixed orthonormal basis | (7/2, 1/16) | C4 | yes |
| B/A tooth u(4) vs su(4) | 0 vs 1/56 | C8 | yes |
| P(r) = 448r^2+(256+4(v4-w))r+96+B_G w; A22=0 | exact (GK11) | D1/D10a/b | yes |
| disc = 16[(w-v4-64)^2-10752-112 B_G w] | exact (GK12) | D3/D3b | yes |
| w=200 roots | {3/14, 1} | D7 | yes |
| w*=64+16*sqrt42, double root | sqrt42/14 (GK14) | D5 | yes |
| real ray at w=w* exactly | **exists (double)** (GK17) | D5 says same | see F-1 |
| w*(2) / w*(3) / w*(4) / 16pi^2 | 115.8823 / 143.6356 / 167.6919 / 157.9137 | 115.88 / 143.64 / 167.69 / 157.91 (D9) | yes |
| general-n threshold w*(n)=8(n+4)+sqrt(3072(n-1/2)), n=2..6 | matches disc sign change (GK15) | D9 | yes |
| K3, K2 (own Tr Hess computations) | 64, 136 | F3 | yes |
| C_u(n)=n; C_su(4),C_su(5) | n; 15/4, 24/5 | F4/F5 | yes |
| Moyal p=1,2 p-terms on constant fields | 0 (GK19) | G1-G3b | yes |
| O(theta) term total derivative | TRUE with primitive V^mu=(i/2)Theta^{mu nu} f d_nu g (my first ansatz was wrong twice — GK-TOTAL 31/32 with GK20 FAIL was **my** bug; corrected `gk20b.py` = TRUE) | G3b claim supported | yes |

**Manuscript-bound "any N" check:** payload states the exact n=4 iff and window corollary only; D9 w*(n) values are verifier print, not payload text; notes.md item 5 correctly records that a blanket "any N" claim fails at n=2,3 (w*(2),w*(3) < 16pi^2). No "any N" in payload — verified by full read of `insert-overdetermination-r1.tex`.

**Not independently verified (accepted pack-side, flagged):** F1 closed-form radial integral (my F2 spot-check `m^2 Lambda^2/64pi^2` agrees); F7 PV threshold coefficient `A M0 (2 ln(M0/mu^2)+1)`; H1-H3 textbook calibration anchors. **Citations:** payload adds no new `\cite` — nothing to fetch; no invented-reference risk. Numbers: all payload numbers tie to verifier output or universal constants (rule 7 satisfied). Repo stray `out-q4.txt` at root is a failed-run traceback (notes item 1), not a package artifact — orchestrator cleanup note, no finding against 119.

## Findings

**F-1 — Severity: MINOR. Location:** payload `insert-overdetermination-r1.tex`, fixed-ray clause: "real fixed rays exist if and only if \((w-v_4-64)^2>10752+112B_Gw\): at \(B_G=v_4=0\) none occur for \(0\le w\le 64+16\sqrt{42}\approx167.7>16\pi^2\)". **Finding:** false at the endpoint. At w = w* exactly, disc = 0 and there is a real marginal double root r* = sqrt(42)/14 — the package's own D5 and my GK14/GK17 confirm it. So the strict `>` iff omits the equality case and the closed interval `\le` asserts "none occur" at a point where a (degenerate) ray does occur. **Reason:** internal inconsistency with the package's own verified content; measure-zero boundary, interior claim exact. **Required action:** replace `\le` with `<` in the window clause and state the equality case, e.g. "if and only if \((w-v_4-64)^2\ge 10752+112B_Gw\), with a single marginal double ray at equality" (Corrected snippet below). Verifier D3's printed message may keep strict-iff wording; check-side text is not manuscript-bound and `verify_r119.py` is pin-stable as is.

**F-2 — Severity: MAJOR. Location:** payload beta clause: "\(B_G=0\) for \(u(4)\), \(1/16\) for \(su(4)\)" printed next to the displayed beta system whose beta_c3 carries `+4w`. **Finding:** the printed beta system is the u(4) instance: the `+4w` coefficient is the u(4) TrX^2 channel coefficient A_G = 4 (my GK7/GK8 and package C2: S = N TrX^2); for su(4) the same channel carries A_G = N - 2/N = 7/2 (my GK5/GK6 mixed-basis computation and package C4/C7: S = (7/2)TrX^2 + (1/16)(TrX)^2). The parenthetical pairs su(4) B_G data with a u(4) beta function, so as printed the su(4) numbers cannot both belong to the displayed system; the rays condition `((w-v_4-64)^2 >= 10752+112B_Gw)` is likewise the A_G=4 form. (For the record, computed on the su(4) data the true threshold ~199.1 and even the printed-form su(4) instance ~173.4 both still exceed 16pi^2, so the window conclusion is robust to the mix-up — but the printed pairing is not a valid statement of either theory.) **Reason:** a group-content mismatch in manuscript-bound equations; the package's own verifier distinguishes the two channels (C8 tooth), so this is presentation, not derivation, error. **Required action:** either (a) minimal: delete the `1/16 for su(4)` parenthetical and label the displayed system `u(4)` (all printed numbers then valid), or (b) parameterize: beta_c3 with `+A_G w`, `P(r)=448r^2+(256+4v_4-A_G w)r+96+B_G w`, state `(A_G,B_G)=(4,0)` for u(4) and `(7/2,1/16)` for su(4), and replace the rays condition by `(((A_G/4)w - v_4 - 64)^2 >= 10752+112B_G w)` — I verified this generalized discriminant identity symbolically (disc = 16[(64+v4-(A_G/4)w)^2 - 10752 - 112 B_G w]). Option (b) changes payload numbers and requires full re-pinning.

**F-3 — Severity: MAJOR. Location:** payload shift clause (line 2) and proposal-r1.md reasoning item 1 ("minimal shift-symmetric lift", "|D Phi|^2-type terms ... invariant under Phi -> Phi + kappa I"). **Finding:** the claim is false for the lift actually in the manuscript. ch03 L215-216 defines `D_mu Phi = partial_mu Phi - i A_mu Phi` acting by **left multiplication on the I index**; then `D_mu(Phi + kappa I) = D_mu Phi - i kappa A_mu`, so the eq:Smicro lift (L221, kinetic `-g^{(0)mu nu}(D_mu Phi)^dagger D_nu Phi - V(Phi^dagger Phi)`) is **not** shift-invariant. Nor is the dictionary bridge shift-covariant: `[Xhat_mu, Phi] <-> i Theta_{mu nu} D^nu Phi` (ass:dictionary, ch03 L346) picks up `kappa Theta_{mu nu} A^{nu}` under Phi -> Phi + kappa I. Shift invariance holds only for lifts in which Phi enters exclusively through commutators `[.,Phi]` (the Presentation-A commutator-type lift), which is a strictly smaller class. **Reason:** as written the payload attributes a symmetry to the manuscript's chosen microscopic lift that the lift does not have — a false claim in manuscript-bound text, and it strengthens rather than weakens the underdetermination thesis (the obstruction is lift-specific, not general), so it need not survive. **Required action:** scope the clause, e.g. "lifts in which \(\Phi\) enters only through commutators are invariant under \(\Phi\mapsto\Phi+\kappa I\); the \emph{eq:Smicro} lift with \(D_\mu\Phi=\partial_\mu\Phi-iA_\mu\Phi\) and the \emph{eq:dictionary} bridge are not", and sync the proposal's "minimal shift-symmetric lift" wording to "commutator-type lift". No new physics; corrected snippet below.

**F-4 — Severity: NOTE. Location:** manifest.md self-hash rule. **Finding:** reproducible — substituting the printed token into the 40-hex cell at offset 1178 yields sha1 `1d18781c772c...` = the cell value (fixed point verified). The parenthetical "fixed length" is inaccurate (token 38 B vs cell 40 B), harmless for the documented Recheck procedure. No action required.

**F-5 — Severity: NOTE. Location:** verifier check messages D3/D3b wording ("fixed rays iff >"). **Finding:** after the F-1 payload fix the check-side strict-iff wording becomes slightly looser than the payload's; check-side only, not manuscript-bound, no re-pin needed. No action required unless the researcher chooses to align wording in round 2.

No other findings: algebra, signs, factors (3/8, 96/512/640, 448, 10752=16*672, 112), the P-quadratic mechanism (A22=0), the boundedness boundary P(-1/4)=60+w(1+B_G)-v4 (D8, my re-check agrees), the c1=0 mass-independent RG surface (F8 logic valid: beta_c1 = c1*gamma is additive-generation-free by dimensional analysis in a mass-independent scheme), limits n->2,3, and the constant-field Moyal statements all verified.

## Scope of what is established
**Proved (independently re-derived here, given the stated truncations):** the tensor identities T33/T32/T22 for n=2..6; the u(N)/su(N) one-loop channel coefficients; the quadratic beta_r polynomial, its discriminant, the exact ray condition and thresholds (with F-1/F-2 fixes); w*(4) > 16pi^2 for u(4) and both su(4) variants; scheme teeth (sharp-cutoff K3/K2, PV finiteness datum, c1=0 mass-independent surface); constant-field Moyal collapse to total derivatives.
**Conditional (correctly scoped in the package):** the whole machine is one-loop perturbation theory of the dimension-4 quartic-in-X sector with symbolic S_matter and stated gauge/fermion bookkeeping; it constrains selection arguments but derives no vacuum.
**Remains OPEN:** Problem D (verbatim ledger above), D1, A, E — the payload claims none of these closures and its final sentence disclaims closing D, D1 or A; consistent with ch17 L329-362 and rule 3. This is a constraint/no-go-style record, not progress by closure.
**Relaxations that could still favour the infrared / full-GR derivation, ranked:**
1. **Commutator-type explicit lift or explicit non-minimal S_matter** (directly exposed by F-3): the shift/no-shift obstruction is lift-specific; a Presentation-A UV completion where Phi enters only via commutators is the least-exploited door and is exactly the assumption the underdetermination statement quantifies over.
2. **Specifying gauge group + fermion content + the UV boundary condition at eq:LUV-def**: the c1=0 surface and B_G(A_G) data convert underdetermination into selection once a boundary condition is imposed; cheap and upstream of any D1 frame construction.
3. **Group choice su(N) with correct A_G**: thresholds move up (199.1 vs 167.7), so the window result is robust — listed for honesty; unlikely to favour the target.
4. **n=2,3 window-internal rays**: w*(2), w*(3) < 16pi^2 means fixed rays inside the perturbativity window are not excluded there; physically the matter content is n=4, so low promise for the target.
5. **Dynamical Theta / all-order Moyal resummation** and 6. **non-renormalizable/double-trace completions beyond dimension 4**: change the question; only worth attention if 1-2 fail.

## Recommended disposition
**Revise, then integrate.** Not integrate-as-is (F-2, F-3 are false-as-printed manuscript-bound statements). Round 2 must land F-1 (endpoint wording), F-2 (recommended minimal fix: label the system u(4) and drop the su(4) parenthetical — option (b) only if the researcher wants the general-G statement), F-3 (scope the shift clause to commutator-type lifts; sync proposal reasoning item 1). Because the revisions change payload bytes, the current POST pins (848355 / `eaea0964...`) apply only to this payload. Integrator guidance for the revised payload: re-pin against the **live** baseline (`2ed53c7778c1`/843649; anchor count 1 @ 290106 — re-check at integration time, the tree is actively re-typeset), splice `replace(anchor, payload+CRLF+anchor, 1)`, regenerate via the patched `gen_payload_119.py` twice byte-identical, fresh `cert-r119p.py` run in a clean temp tree, rerun `verify_r119.py` (62/62 expected), then `python scripts/build_check.py` and `python scripts/make_digest.py`; do not commit; label-touched: no.

## Corrected snippet
(no new physics; F-1 and F-2 option (a); F-3)

F-1+F-2(a), replacing the fixed-ray and gauge clauses:
```latex
real fixed rays exist if and only if \((w-v_4-64)^2\ge 10752+112B_Gw\), with a single
marginal double ray at equality and two distinct rays above it: at \(B_G=v_4=0\) none
occur for \(0\le w<64+16\sqrt{42}\approx167.7>16\pi^2\). The displayed system is the
\(u(4)\) instance \((A_G,B_G)=(4,0)\); for \(su(4)\) the \(\Tr X^2\) channel carries
\(A_G=N-2/N=7/2\) in addition to \(B_G=1/16\), and both give thresholds above \(16\pi^2\).
```
F-3, replacing the shift clause:
```latex
lifts in which \(\Phi\) enters only through commutators are invariant under
\(\Phi\mapsto\Phi+\kappa I\); the eq:Smicro lift with
\(D_\mu\Phi=\partial_\mu\Phi-iA_\mu\Phi\) acting on the \(I\) index, and the
eq:dictionary bridge, are not shift-covariant.
```
(If option F-2(b) is chosen instead: `P(r)=448r^2+(256+4v_4-A_G w)r+96+B_G w`, rays iff `((A_G/4)w-v_4-64)^2\ge 10752+112B_G w`, `(A_G,B_G)=(4,0)` u(4) / `(7/2,1/16)` su(4) — I verified this generalized discriminant identity independently.)
