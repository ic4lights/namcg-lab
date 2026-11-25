# Proposal 122-d1-bilocal-nondeg, round 2

MECHANICAL REVISION ROUND per review-r1 (ACCEPT WITH REQUIRED REVISIONS): findings 1-3 applied to the payload and
generator, finding 4 applied to the proposal record, finding 5 declined (recorded). No re-derivation, no new
mathematics, no tier or scope changes; the r1 tiering and scoping are accepted by the gatekeeper and carried
unchanged.

## Result
The manuscript-bound paragraph is re-issued as `payload-122.tex` (pin affd17c6f13d / 5942 bytes): it now terminates
in exactly one CRLF (r1 stray lone CR removed at the root: the generator's LF->CRLF re-encode pass no longer sees an
already-CRLF terminator), clause (ii) places the unitarity hypothesis on the carrier transport operator using the
gatekeeper's verbatim wording (finding 2), and the (ii) equality statement is scoped fibre-wise with operator
equality only for constant rho (finding 3). The generator's `det_eol` now flags any CR not followed by LF (regex
built from chr(92)); the dead lone-CR positive control is replaced by a CR-CR-LF control that provably fires, and
four terminator guard checks assert the invariant on the real payload bytes. Independent verifier
`check_payload_122_r2.py`: 17/17 checks pass, `CHECK-FAILURES: 0 (none)`, POST recomputed from live appH bytes
byte-for-byte equal to the shipped preview. New splice target: PRE 857887 + PAY 5942 + 2 = POST 863831, pin
d2af19df0f99. The bilocal reduction content, hypotheses, classifications and OPEN statuses are exactly those
accepted in round 1.

## Target and status
Target: D1.lorentz avenue 2 (059 review-r1: explicit bilocal composite frame with matrix parallel transporters and
a computed non-degeneracy criterion for ass:nondeg), as stated in r1. Affected ledger, quoted verbatim and
unchanged in r2 (from Problem D, appH ledger section, per review-r1): "Status: OPEN. Priority: CRITICAL PATH.
Completion: PROGRAMME-CONDITIONAL" with the D2 scope qualifier (appH L769-772). Problems D, D1, F and N remain
OPEN and PROGRAMME-CONDITIONAL; the package is PROGRAMME-CONDITIONAL evidence toward the D1 derivation, closing
nothing. Dependencies unchanged (Gibbs paragraph input for the moment class of (iv); ass:nondeg and ass:frame-lock
remain assumed).

## Source reading
digest + targeted reads. Read in full: `review-r1.md` (findings 1-4 and Recommended disposition = work order),
`proposal-r1.md` (target/status and the finding-4 record region ~L141-150), `manifest.md`, `make_payload_122.py`,
`payload-122.tex` (tail bytes); live pin of `chapters/appH-microscopic-proofs.tex` taken first at r2 start:
cf3139fbedb0 / 857887, match, no drift; re-verified unchanged at r2 end. Full scan not required (no
definition/assumption/scope/status change) and not performed.

## Research and reasoning
This round executes the accepted revision; reasoning is confined to making the two wording fixes and the byte
terminator exactly as directed.

1. Finding 1 (blocking, terminator). Root cause confirmed: the r1 generator built the paragraph with a trailing
   CRLF and then ran `.replace(chr(10), chr(13)+chr(10))`, converting the LF of that terminator into CRLF and
   leaving `. CR CR LF` (5783 = 5780 + 3); the r1 `det_eol` inspected only `endswith(CRLF)` and bare-LF, so its
   lone-CR control (which stripped the terminator) could never fire on that defect (dead branch). Fix: strip
   trailing CR/LF, run the LF->CRLF pass, append exactly one CRLF; `det_eol(b)` now returns True unless b ends in
   CRLF, has no LF without preceding CR, and matches no lone CR via regex `CR-not-followed-by-LF` assembled from
   chr(92). Control set: 7 named positive controls, the new `CR-CR-LF-terminator` control injecting `CR CR LF`
   into a test buffer and firing (printed among the 7); plus real-byte guards: fixed payload passes `det_eol`, the
   injected defect buffer is rejected, payload does not end `CR CR LF`, payload contains exactly one CR and one LF
   byte. Demonstrated: the new control genuinely triggers detection (FIRED CR-CR-LF-terminator in both runs) and
   the guard genuinely rejects (defect-buffer chk fails the run with exit 1 if the terminator regresses).
2. Finding 2 (major, (ii) first clause). Replaced per the gatekeeper's verbatim wording: the hypothesis is now
   "the link-variable assembly makes the carrier transport operator unitary -- matrix link variables and exactly
   unitary fuzzy Wilson lines (transport as a unitary superoperator on the finite carrier), path-ordered
   exponentials of anti-Hermitian fibre connections, for which \(\sigma_{\min}=1\) exactly and uniformly in the
   carrier size --". This is the carrier-operator reading under which the gatekeeper independently verified w=1;
   the r1 link-wise reading was falsifiable (constant unitary kernel on n>=2 points has w=0). Seam check: the
   dash-opened clause closes into the unchanged continuation " then \(w=1\) ..." exactly as in r1; no glue word
   was needed (difflog: zero glue words).
3. Finding 3 (major, (ii) equality scope). "with equality on radial fibres \(\Phi=\rho\,U\)" replaced verbatim by
   "with fibre-wise equality on radial fibres \(\Phi=\rho\,U\) (and operator equality when \(\rho\) is constant)",
   matching the gatekeeper's counterexample (variable rho: sigma_min(T_M)=1 vs c^2 w=1/4).
4. Finding 4 (minor, record). Amended record for the Carrier topology item (replaces proposal-r1.md ~L146-147,
   which stays as the historical r1 record): the numerically diagonalised values 3.1e-18 (n=128) and 2.8e-19
   (n=256), s=0.15, are double-precision numerical-floor values, NOT the exact spectrum; the exact spectrum of the
   Fourier-diagonalised heat kernel is \(\sigma_{\min}=\exp(-s^2n^2/4)\), whose values are 3.15e-03 (n=32),
   9.86e-11 (n=64), 9.45e-41 (n=128), 7.97e-161 (n=256) -- the formula matches the numerics only at n=32, 64.
   Exact values printed by `check_payload_122_r2.py` (sourced there). The payload already states only the exact
   formula and is unchanged on this point.
5. Finding 5 (optional, declined): the r1 review marks the "\(\Phi\) invertible \(\mathrm d\mu_{\rm c}\)-a.e."
   clause "not required"; (i) already states the hypothesis \(c\le\sigma_{\min}(\Phi)\) a.e. (c>0 included) and the
   scope sentence restricts (i)-(iii) to the stated a.e. bounds. Adding a clause would exceed a mechanical round
   ("NO new mathematics" work order). Declined; recorded here and in Decisions Taken.

Answers to review-r1 findings: 1 closed (single CRLF; new detector; new control fires; guard rejects; regenerated
and re-pinned end to end, anchor unchanged and unique). 2 closed verbatim, seam coherent, no glue word. 3 closed
verbatim. 4 closed in this record (payload untouched, already exact). 5 declined with reason above. Byte proof of
minimality: new payload body = old payload body with exactly the two accepted substitutions (+160 bytes: +99
finding 2, +61 finding 3) and nothing else (script check printed diff-exactly-two-fixes: True). The review's
"expect PAY 5782, POST 863671" was finding-1-only arithmetic; with mandatory findings 2-3 included, PAY = 5942 and
POST = 863831 (= 857887 + 5942 + 2, verified twice: generator and independent verifier, the latter recomputing from
live appH and matching the shipped preview byte-for-byte; wrong-zone variant same size, different sha1).

## Claim classification
Unchanged from round 1 (accepted by the gatekeeper); the two wording fixes are precision corrections, not tier
changes:
- Established identity/derivation: (i) reduction inequalities and two-sided positivity equivalence (c>0); (iii)
  fibre identities and compression statements; (v) exact heat-kernel spectrum, band independence, compact-operator
  obstruction; Haar off-diagonal vanishing; Gronwall transport bound with sharp scalar case; R0/R2 inequalities
  with the corrected radial scope.
- Conditional derivation: (ii) under finite carrier plus unitary carrier transport operator (structural input, not
  derived from eq:Smicro); (iv) under \(\mu_{\mathcal V}<\lambda v^4/4\).
- Input/mechanism: NAMCG transporter membership in the unitary class; carrier selection; state selection.
- Unresolved: computation of \(w\) for the D1 carrier from eq:Smicro; off-diagonal/mean-field control; eq:V
  selection. Nothing about the emergent metric; spacetime remains emergent (finite-N carrier primary).

## Proposed changes
File: `chapters/appH-microscopic-proofs.tex` (single insertion; identical location and anchor as r1).
Anchor (verified unique, count 1, in live bytes at r2):

    remains the upstream input that gates what any Presentation-B measure can be cited as; Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg} remain assumed, so Problem~D remains OPEN and PROGRAMME-CONDITIONAL.

Splice (canonical, count 1): replace anchor+CRLFCRLF by anchor+CRLFCRLF+payload+CRLF, i.e. insert payload-122.tex
as one paragraph line between the Gibbs paragraph and the Presentation-A paragraph (review-r1 checks 2/6 verified
this landing; unchanged in r2). Everything else in appH stays byte-identical.

Payload (new bytes; pin affd17c6f13d / 5942 including the single final CRLF). The embedded body below is the file
minus its final CRLF; appending exactly one CRLF to it reproduces the pin. Kept from r1: the entire remaining
text, all six refs (exactly \ref{ass:nondeg}, \ref{ass:frame-lock}, \eqref{eq:V}, \eqref{eq:vev-is-frame},
\eqref{eq:vacuum-manifold}, \eqref{eq:Smicro}; all six labels verified to exist, one file each), no new
\label/\cite/$, math delimiters balanced.

```latex
\emph{Bilocal composite: exact reduction of the two-point-kernel gap and conditional non-degeneracy bounds.} This paragraph records derivations that discharge the two-point-kernel non-degeneracy step under explicit hypotheses and scope what the bilocal reading of Assumption~\ref{ass:nondeg} can supply. Let \(M(x,y)=\Phi(x)\,W(x,y)\,\Phi(y)^\dagger\) be the bilocal composite with transport coefficients \(W(x,y)\in\mathbb C^{4\times4}\) on a carrier measure \(\mathrm d\mu_{\rm c}\) over the base, and let \(T_M\) be the operator \((T_M f)(x)=\int M(x,y)f(y)\,\mathrm d\mu_{\rm c}(y)\) on \(L^2(\mathrm d\mu_{\rm c})\otimes\mathbb C^4\), with \(T_W\) the operator of \(W\) alone and \(\kappa(T):=\sigma_{\max}(T)/\sigma_{\min}(T)\). (i)~Reduction. The factorization \(T_M=\mathsf P\,T_W\,\mathsf P^\dagger\), with \(\mathsf P\) fibrewise multiplication by \(\Phi\), applied to the identities \(\sigma_{\min}(AB)\ge\sigma_{\min}(A)\,\sigma_{\min}(B)\) and \(\sigma_{\max}(AB)\le\sigma_{\max}(A)\,\sigma_{\max}(B)\), gives: if \(c\le\sigma_{\min}(\Phi)\) and \(\sigma_{\max}(\Phi)\le C\) \(\mathrm d\mu_{\rm c}\)-a.e., then \(\sigma_{\min}(T_M)\ge c^2\sigma_{\min}(T_W)\) and \(\kappa(T_M)\le(C/c)^2\kappa(T_W)\). The gap recorded above therefore reduces exactly to the transport-kernel lower bound \(w:=\sigma_{\min}(T_W)\), and no bound on \(w\) follows from pointwise \(\Phi\)-data: with \(\Phi\equiv v\,\mathbb I\) and \(W\) fibrewise a rank-deficient projector, \(w=0=\sigma_{\min}(T_M)\) with \(\Phi\) invertible, and a fibre of smallest singular value \(c\) drives the bound at rate \(c^2\). (ii)~Unitary-transporter carrier case. If the carrier is finite and the link-variable assembly makes the carrier transport operator unitary -- matrix link variables and exactly unitary fuzzy Wilson lines (transport as a unitary superoperator on the finite carrier), path-ordered exponentials of anti-Hermitian fibre connections, for which \(\sigma_{\min}=1\) exactly and uniformly in the carrier size -- then \(w=1\) and \(\sigma_{\min}(T_M)\ge c^2\); on a region where \(\mathcal V\le\varepsilon\) for \(\mathcal V\) of Equation~\eqref{eq:V}, the recorded bound \(\sigma_i(\Phi)^2\ge v^2-2\sqrt{\varepsilon/\lambda}\) upgrades this to \(\sigma_{\min}(T_M)\ge v^2-2\sqrt{\varepsilon/\lambda}>0\) for \(\varepsilon<\lambda v^4/4\). The estimate is an inequality in general, with fibre-wise equality on radial fibres \(\Phi=\rho\,U\) (and operator equality when \(\rho\) is constant), so it transfers non-degeneracy and does not determine the spectrum of \(T_M\). (iii)~Coincidence fibre and positivity. At coincidence, \(\sigma_{\min}(\Phi\Phi^\dagger)=\sigma_{\min}(\Phi)^2\) and \(\det(\Phi\Psi^\dagger)=\det\Phi\,\overline{\det\Psi}\) hold exactly, so the diagonal composite inherits pointwise non-degeneracy; every orthogonal compression of a positive-semidefinite fibre bounded below by \(c\) retains lower bound \(c\), while compression of a non-positive factor can drop below \(\sigma_{\min}\) -- positivity of the composite is what transports. (iv)~Diagonal state bound. For any one-point state \(\omega\) with potential moment \(\mu_{\mathcal V}:=\mathbb E_\omega[\mathcal V(x)]<\lambda v^4/4\), the Loewner estimate \(\lambda_{\min}(\mathbb E_\omega[\Phi\Phi^\dagger])\ge\mathbb E_\omega[\lambda_{\min}(\Phi\Phi^\dagger)]\), the fibre identity of (iii), and Markov's inequality give \(\lambda_{\min}(\mathbb E_\omega[\Phi\Phi^\dagger])\ge\sup_{\mu_{\mathcal V}<\varepsilon<\lambda v^4/4}\,(v^2-2\sqrt{\varepsilon/\lambda})(1-\mu_{\mathcal V}/\varepsilon)>0\): under the single moment hypothesis \(\mu_{\mathcal V}<\lambda v^4/4\) -- the one-point moment class made finite by the Gibbs paragraph above, whose smallness remains an input -- the coincidence composite \(\mathbb E_\omega[\Phi\Phi^\dagger]\) is state-nondegenerate; this is a statement about the composite and not about the mean-field frame \(e=\langle\Phi\rangle/v\) of Equation~\eqref{eq:vev-is-frame}, whose control is the mean-field gap recorded above. The hypothesis is sharp, the bound being non-positive at \(\mu_{\mathcal V}=\lambda v^4/4\) on the threshold fibre \((0,v,v,v)\), and no analogous bound holds for the off-diagonal expectation composite, whose fibre-wise Haar average vanishes identically. (v)~Carrier topology. The lower bound \(w\) is a property of the carrier, not of the kernel alone: on a periodic grid of \(n\) points the Fourier-diagonalised heat kernel of diffusion parameter \(s\) has smallest eigenvalue \(\exp(-s^2 n^2/4)\to0\), while its compression to a fixed band \(|k|\le K\) has grid-independent smallest eigenvalue \(\exp(-s^2K^2)\); a continuum smooth-kernel reading of the composite therefore cannot carry a uniform \(w>0\), and the bilocal non-degeneracy of Assumption~\ref{ass:nondeg} must be stated on a finite carrier as in (ii), the finite-\(N\) matrix-theory regime, or through the coincidence fibre (iii). For a path-ordered transporter \(W=P\exp\int\omega\) one has \(\sigma_{\min}(W)\ge\exp(-\int\sigma_{\max}(\omega))\), with equality on scalar-gauge paths and \(\sigma_{\min}=1\) for anti-Hermitian \(\omega\). Scope: (i)-(iii) and (v) are identities and conditional estimates under the stated a.e.\ bounds with explicit sharpness examples, and (iv) is a conditional estimate under the stated moment hypothesis; the carrier measure, the connection class of \(W\), and the state \(\omega\) are inputs and are not derived from Equation~\eqref{eq:Smicro}, no measure or state is constructed here, the off-diagonal expectation composite is not bounded, the vacuum-manifold fibre measure of Equation~\eqref{eq:vacuum-manifold} is untouched, and the computation of \(w\) for the specific carrier of Problem~D1 remains open; Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg} remain assumed and this paragraph closes none of Problem~D, Problem~D1, Problem~F or Problem~N, all of which remain OPEN and PROGRAMME-CONDITIONAL.
```

Difflog, old payload (33165816b9fd) -> new (affd17c6f13d):
- terminator: body + CR + CR + LF (stray lone CR) -> body + CRLF (exactly one CRLF; 5783 -> 5782 before text fixes).
- (ii) first clause (finding 2, verbatim): "the transporter matrix is unitary -- matrix link variables and exactly
  unitary fuzzy Wilson lines, path-ordered" -> "the link-variable assembly makes the carrier transport operator
  unitary -- matrix link variables and exactly unitary fuzzy Wilson lines (transport as a unitary superoperator on
  the finite carrier), path-ordered" (+99; clause closes unchanged into " then \(w=1\)"; no glue word).
- (ii) equality sentence (finding 3, verbatim): "with equality on radial fibres \(\Phi=\rho\,U\), so" -> "with
  fibre-wise equality on radial fibres \(\Phi=\rho\,U\) (and operator equality when \(\rho\) is constant), so"
  (+61).
- Nothing else changed (verified: applying the two substitutions to the old body reproduces the new body exactly).
Total: 5783 -> 5942 = 5780 + 160 + 2.

Generator `make_payload_122.py` (4f7eb6a0afdc; r1 bytes preserved as make_payload_122-r1-superseded.py):
terminator construction, `det_eol` lone-CR regex, named controls with the CR-CR-LF positive control replacing the
dead lone-CR one, and four real-byte terminator guards (all pass; GEN-FAILURES: 0 twice with identical outputs).

Stale passages and their replacements: manifest.md round-1 "Expected invariants" (PAY 5783 / POST 863672) replaced
by the r2 section (PAY 5942 / POST 863831 / pin d2af19df0f99), r1 table retained; proposal-r1.md ~L146-147
"3.1e-18, 2.8e-19 ... exact spectrum" superseded by the finding-4 record above; review-r1 expected sizes 5782 /
863671 superseded by 5942 / 863831 for the reason given. No manuscript passage other than the single insertion is
touched; no other chapter refers to these numbers.

## Verification scripts
All in this folder; re-runnable; reproduction pack:
- `python -I proposals/122-d1-bilocal-nondeg/bilocal_nondeg_s1.py` -> last line "FAILURES: 0 (none)" (unchanged r1;
  captures 62ea7c6e5b25). Consumes none of the changed artifacts.
- `python -I proposals/122-d1-bilocal-nondeg/bilocal_nondeg_s2.py` -> "FAILURES: 0 (none)" (captures 2ab6fb1050ee).
- `python -I proposals/122-d1-bilocal-nondeg/make_payload_122.py` -> invariant output: "controls fired: 7/7" with
  "FIRED CR-CR-LF-terminator" listed, all chk lines OK, "PRE 857887 PAY 5942 POST 863831", "POST-SHA1
  d2af19df0f99...", "PAYLOAD-SHA1 affd17c6f13d...", "GEN-FAILURES: 0 (none)". Captures out-gen122-r2-run1.txt and
  out-gen122-r2-run2.txt are byte-identical (5cab45b3dd9d): determinism.
- `python -I proposals/122-d1-bilocal-nondeg/check_payload_122_r2.py` -> 17 OK lines and "CHECK-FAILURES: 0
  (none)" (capture out-check122-r2.txt, bffb7cc5198e): pure ASCII; zero lone LF; zero lone CR; ends exactly one
  CRLF; not CR-CR-LF terminated; zero \label/\cite tokens; refs exactly the six whitelisted and all resolving in
  chapters/; both gatekeeper wordings present verbatim; both old wordings absent; anchor count 1; independent POST
  recompute from live appH == shipped preview bytes; POST = PRE + PAY + 2; wrong-zone variant same size, different
  hash; exact heat-kernel values 3.15e-03, 9.86e-11, 9.45e-41, 7.97e-161.
Tool output is a check, not a proof; the proofs are the r1 derivations (accepted) plus the byte-level identity
argument in the difflog (two substitutions and the terminator, nothing else).

## Decisions Taken
- Finding 5 declined (invertible-a.e. clause not added): review-r1 marks it not required; (i) already hypothesises
  \(c\le\sigma_{\min}(\Phi)\) a.e., which with the scope sentence covers c>0; the round is mechanical, so the
  minimal-accurate-text rule favours adding nothing. Alternative (adding the clause) rejected as out-of-order.
- Adopted the gatekeeper's replacement wordings for (ii) and (iii) verbatim (work order); seam check showed no
  glue word is required, so none was inserted and none needs flagging.
- Kept 7 positive controls (count unchanged from r1) and moved terminator verification additionally onto real-byte
  guards rather than inflating the control count.
- Preserved r1 bytes by copy (payload, generator, preview) before editing, both hashes recorded in manifest.md.

## Milestone assessment
Routine. No milestone trigger: no critical-path step derived; statuses untouched.

## Status-label recommendation
Derived from the current agenda and ledger (via review-r1 and appH Problem D): Problems D, D1, F, N remain OPEN,
CRITICAL PATH where applicable, PROGRAMME-CONDITIONAL. Labels affected by this package: none changed, none
proposed for change.

## Author decision needed
None.

## Remaining open step
Unchanged from r1: (a) prove the fuzzy link-variable / Wilson-line assembly of the NAMCG carrier is a unitary
carrier transport superoperator from eq:Smicro -- this is exactly the hypothesis (ii) retains and what discharges
the transport half of the two-point-kernel gap; (b) derive \(\mu_{\mathcal V}<\lambda v^4/4\) for a constructed
one-point state (the Gibbs paragraph supplies only the moment class); (c) off-diagonal / mean-field control beyond
the vanishing-Haar model; (d) eq:V selection. Problems D, D1, F, N stay OPEN and PROGRAMME-CONDITIONAL; nothing in
this package computes w for the specific D1 carrier.

## Special instructions for the gatekeeper
Scope limits: r2 changes ONLY the payload bytes (terminator + the two accepted word substitutions), the generator,
the manifest, and this record; s1/s2 and their captures are untouched r1 artifacts. The r1 compile certificate
certifies the OLD bytes; per the r1 Recommended disposition a compile certificate on the NEW spliced bytes (pin
d2af19df0f99) must be repeated at r2 before integration (do it outside the repository). Required r2 checks: re-run
the pack (expected invariants above; controls 7/7 must include FIRED CR-CR-LF-terminator); confirm the payload body
equals the old body plus exactly the two substitutions (difflog claim) and terminates in one CRLF; recompute POST
independently from live appH (expect 863831 / d2af19df0f99; POST = 857887 + 5942 + 2; wrong-zone variant different
hash); verify the (ii) dash clause closes into " then \(w=1\)" with no glue word and the sentence is grammatical;
verify finding-4 numbers against check_payload_122_r2.py output. Must NOT be asserted from this package: closure
of D, D1, F or N; derivation of the transport-operator unitarity from eq:Smicro; anything about the emergent
metric. Integrator (only after r2 ACCEPT): re-pin appH and payload at integration time, splice with the canonical
replace(anchor+CRLFCRLF, anchor+CRLFCRLF+payload+CRLF, 1) at anchor count 1, then scripts/build_check.py and
scripts/make_digest.py; no commit.
