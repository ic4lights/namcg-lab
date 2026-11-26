# Proposal 092-g-profile-coordinate-transport, round 1

## Result
Within the named coupled gaussian slot law of the rank-one Gaussian edge-charge class, at a
GENERAL strictly positive profile (no constancy or uniformity restriction), the profile
coordinate is transported exactly onto two derived-coordinate systems, and both transports are
executed in closed form:

1. **Transport orbit of the 089 pushforward family.** The group of positive profiles modulo
   common scaling acts simply transitively (freely) on the interior of the profile simplex by
   the projective diagonal maps tau_g(p)_i = g_i p_i / sum_j g_j p_j, with tau_g o tau_h =
   tau_{gh} and inverse tau_{1/g}, and simplex Jacobian prod_i g_i / <g,p>^D. Consequently the
   089 density (D-1)!/(G (sum_i p_i/g_i)^D) is exactly the flat Dirichlet density (D-1)!
   transported by tau_g: the whole pushforward family is a single transport orbit of its flat
   member, and the profile is recovered from any member as the unique group element carrying
   the flat member to it. This is the 089 identifiability rewritten as exact transport; the
   profile becomes the group parameter of the family rather than a list of supplied slot
   labels, but no profile content is produced by the core (the label content is reframed, not
   eliminated - the insert says this explicitly).
2. **Moment-map coordinates.** For the averaged charge moments m_{2p} = 2 E[ell^{2p}] of the
   Charge-to-edge moment identification paragraph (appH L3177) at its leading-order
   convention, m_{2p} = 2 (4 s^2 W)^p rho_p with rho_p = p! h_p(g)/W^p (h_p the complete
   homogeneous symmetric polynomial), so rho_p = 2^{p-1} m_{2p} / m_2^p is free of the state
   variance s^2 and equals exactly that paragraph's obstruction factor (its p=2 and p=3 forms
   reproduce). The map from the ordered chamber g_1 > ... > g_D > 0 to (rho_2,...,rho_D) is a
   bijection onto its image: the power sums recover from the rho's by the inverted Girard
   recursion, the elementary symmetric functions by Newton's identities, and g/W is the ordered
   root set of a monic degree-D polynomial. The power-sum Jacobian is the exact classical form
   prod_{k=1}^D k times the Vandermonde product prod_{i<j}(g_i - g_j), so the recovery is a
   diffeomorphism on the chamber, singular exactly on the coincidence walls. Thus at a general
   rank-one profile the ordered profile, up to relabelling and up to the scale fixed by W, is
   carried by the averaged charge-moment sequence rather than supplied to it; what the sequence
   does not supply is the scale datum s^2 W, exactly the state input the surrounding paragraphs
   record as unsupplied.
3. **D=2 mean-map faithful coordinate.** At D=2 even the first moment of the pushforward
   measure itself is a faithful chamber coordinate: with rates lambda_i = 1/g_i and
   L = lambda_1/lambda_2, E_{mu_g}(p_1) = L(log L + 1/L - 1)/(L-1)^2, strictly decreasing from
   1/2 at L=1 to 0 as L -> infinity (slope -1/6 at L=1). The analogous injectivity statement
   for mean or symmetric-moment maps at D >= 3 was NOT obtained and is recorded as such.

No closure of anything in Problem G; no status/priority/completion text; no label change.

## Target and status
- Target (frontier chain-2 rank 1, post-integration-22 note and edge
  G.moments-interaction-nonconvex / G.moments-nonproduct-measures hypothesis_class field,
  file reports/graph/frontier.yaml, 260,822 B / sha8 cc6d6222, grepped windows): "COORDINATE
  TRANSPORT of the profile coordinate asked for the 089 pushforward law at GENERAL rank-one
  profile ... transport of the Gram-spectrum / moment-map profile coordinate", the
  REVIEW-091-r3 ranked avenue (1), "most promising, correctly posed per r3".
- Problem G (appH sec:status-G): Status: OPEN. Priority: CRITICAL PATH. Completion:
  PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a
  scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion
  (L3026-3029, quoted verbatim from the live tree). Missing step (i)-(iv) at L3119-3130
  unchanged by this package.
- Dependencies touched: none. The package is a coordinate/transport result inside the named
  class; it changes no dependency. The 091 closer sentence "the identification with the
  profile coordinate of the moment map is not supplied by the repository" is NOT contradicted:
  what is supplied here is the transport of the profile onto the averaged-charge-moment
  coordinates (the L3177 moment map), not an identification of the slot-power coordinate with
  the Gram-spectrum coordinate of the constant-variance edge block; the insert adds the exact
  one-line fact that inside the rank-one class the slot coordinate is the diagonal of the
  slot-vector Gram, whose spectrum is a single atom, so the Gram-spectrum carrier question is
  vacuous at rank one.
- DERIVED or PROGRAMME-CONDITIONAL: the three results above are exact derivations inside the
  named class; they do not touch the matrix-derived criterion and close nothing.

## Source reading
Digest + targeted reads. scratch/digest.md read in full (DIGEST CURRENT, appH sha8 46dbfb3f
matching the live tree). frontier.yaml: grepped, windows read around the ledger head line 8,
post_integration_note_2026_11_19_post22 (line 16), edge hypothesis_class (line 561) and
lead_for_researcher (line 565) - never read whole. appH windows read IN FULL: L3022-3043 (G
ledger/status), L3119-3132 (Missing step), L3132-3139 (Edge datum start), L3147 (Row length),
L3149-3190 header preview, L3177 (moment map), L3183 (named coupled gaussian slot law),
L3185, L3187, L3189, L3191 (089), L3193 (090), L3195 (091), L3197 (Vacuum term, G-side).
proposals/091/review-r3.md "Scope of what is established" and "Recommended disposition"
headers grepped and window read. Proposals 089/090/091 manifests listed and their insert
texts re-read from appH L3191/L3193/L3195. reports/sme-scout-20261118-2350.md (sha8 9dd6d3f0
verified) structure grepped: its ranked routes R1/R3 were written for target 090 and are
background for this target; NO literature citation was adopted into this package (all results
are self-contained derivations), so nothing carries a "not independently verified" flag.
No unreadable files. No files changed outside this folder.

## Research and reasoning
The 091 review posed the open question as: under what map does the profile coordinate g -
until now a supplied input labelling the slot law - become a derived coordinate, for the 089
pushforward law at general rank-one profile? Two maps answer this inside the named class.

(A) Internal transport of the family. Write the slot law in polar form (089): E_i = |w_i|^2
independent exponentials of means s^2 g_i. The diagonal rescaling E_i -> g_i E_i maps the
uniform-profile slot law to the law at profile g and descends through the quotient
p = E/sum E to the simplex map tau_g because it is fibre-preserving (scaling total E does not
move p). So tau_g pushes the flat member to the member at g for every profile, at general
rank-one profile included - no constancy enters anywhere. The group law and freeness are one
line: tau_g(p) = p forces g_i = <g,p> for all i at any interior p. The Jacobian on the simplex
was checked two ways: exactly for D = 2, 3 (chart determinant, s1b part 3) and by high-precision
tangent-basis determinants at random points for D = 4,...,8 (s1b part 3b, relative error
<= 1e-30 at dps 40); the closed form prod h_i/<h,p>^D then gives, for h = 1/g, the 089 density
as flat density times Jacobian exactly (s1b part 4). Physical reading: the profile is the
group parameter of a simply transitive projective action; the "profile coordinate" of the
family is the transport coordinate of the flat coordinate. What this does NOT do: the group
element is reconstructed FROM a member, i.e. from data that already carries the labels - the
insert states this reframing honestly, consistent with 089's "re-imports the profile" verdict.

(B) External coordinates from observable moments. The L3177 paragraph already computes the
averaged charge moments as 2(4s^2W)^p rho_p(g); this proposal inverts that map exactly.
E[T^p] = p! h_p(g) for T = sum of independent exponentials of means s^2 g_i (Laplace transform
differentiated, verified exactly at D=2 p=1..3 and D=3 p=1..4, s2 part 1) gives
m_{2p} = 2^{2p+1} p! s^{2p} h_p(g); the ratio rho_p = 2^{p-1} m_{2p}/m_2^p cancels s^2
(verified s2 part 2) and equals p! h_p/W^p, matching L3177's rho_p(g) = p! h_p(g)/(sum g)^p,
its p=3 expansion 1 + 3 s_2/W^2 + 2 s_3/W^3 against L3177's stated 3/D_eff + 2 s_3/(sum g)^3
with D_eff = W^2/s_2, and its partition form against the Girard/z_lambda formula there (s2
part 5). Inversion (s2 part 3): from hat h_k = rho_k/k!, the Girard relation
k h_k = sum_{i=1}^k sigma_i h_{k-i} (unnormalized version with sigma_i = s_i(g)) is
triangular and inverts to sigma_k = k hat h_k - sum_{i<k} sigma_i hat h_{k-i}; Newton gives
e_k(g/W); roots give g/W. Exact symbolic round-trips at D = 2, 3, end-to-end seeded MC
round-trip at D = 3, profile (1, 0.5, 2), from 2e6 exponential slots: reconstruction error
1.6e-3 (statistical) against exact target (s3 part A). Injectivity on the ordered chamber is
not a conjecture: the composite from the ordered chamber to root-sets of monic polynomials
determines the ordered root list uniquely; the Jacobian
det[d(s_1,...,s_D)/d(g_1,...,g_D)] = prod_k k * prod_{i<j}(g_i-g_j) is the classical alternant
identity (verified numerically-exact via the W=1 slice at D = 2, 3, 4 in s2 part 4,
det/V = +2, -6, -24, magnitudes D!, and by direct expansion of the alternant the general
constant is prod_k k = D!). So (rho_2,...,rho_D) is a coordinate on the chamber, with
Vandermonde singularity structure made explicit (recovery degrades like root condition numbers
near walls - the same walls the orbit-rigidity paragraphs keep hitting, now as a quantitative
singularity of the coordinate map).

(C) The measure's own first moment, D=2 (s4): direct integration gives
E_{mu_g}(p_1) = lambda_1 lambda_2/(lambda_1-lambda_2)^2 [log(lambda_1/lambda_2) +
lambda_2/lambda_1 - 1] = L(log L + 1/L - 1)/(L-1)^2; sympy confirms equality with the closed
form and the limits 1/2 (L->1) and 0 (L->infty); monotonicity by strictly negative derivative
(sampled with exact-sign symbolic d/dt at L = e^t) - injective on the chamber. Cross-checked
against quadrature of the 089 density at g = (2,5) to 1e-12. At D >= 3 the mean map (and the
symmetric power-moment maps, whose first variation at uniform vanishes identically for
profile-preserving perturbations - a structural reason the naive approach fails) was NOT
proved injective; stated as not obtained.

Attack choice (Decisions below). Relation to the 091 closer sentence: the inserted text states
the rank-one Gram diagonal fact (one-line identity) and supplies the moment-map transport; it
does not assert the Gram-spectrum/profile identification, which remains unsupplied.

## Claim classification
- tau_g projective action, group law, inverse, freeness: established derivation (exact
  symbolic D=2,3; one-line general argument; script s1b).
- simplex Jacobian prod h_i/<h,p>^D: established for D=2,3 exact symbolic, D=4..8 verified
  numerically at rel <= 1e-30, general by the tangent-space rank-one computation in the text;
  classified established identity/derivation.
- 089 density = flat density transported by tau_g: established derivation (corollary of the
  two items above; density identity checked D=2,3,4).
- profile as unique group element carrying flat member to member: established (freeness +
  transitivity); its reading as "reframed label data, not core-produced profile" is an
  interpretive clause consistent with 089, marked as such in the insert text itself.
- m_{2p} = 2(4s^2W)^p rho_p with rho_p = p! h_p/W^p, and rho extraction 2^{p-1}m_{2p}/m_2^p
  state-free: established identity within the named gaussian rank-one class at the
  leading-order convention (exact symbolic integration + MC).
- inversion by Girard + Newton + roots; chamber bijection; Jacobian prod k * Vandermonde:
  established derivation (classical symmetric-function theory; constants checked exact at
  D=2,3,4).
- scale datum s^2 W not supplied by the moment sequence: established observation (consistency
  with the preceding paragraphs' state-data clauses).
- D=2 mean-map closed form, limits, strict monotonicity: established derivation + exact
  symbolic check.
- injectivity of mean/symmetric-moment maps at D>=3: UNRESOLVED (explicitly not obtained).
- rank-one slot Gram spectrum = single atom, slot coordinate = its diagonal: established
  one-line identity.
- everything about the core-action matrix integral, state selection, W: untouched, unresolved
  (unchanged from before).

## Proposed changes
One file: `chapters/appH-microscopic-proofs.tex`. New paragraph inserted in the G block between
the 091 paragraph and the G-side Vacuum term line.

- Anchor (compound PIN, verified count 1 live): the 091 tail sentence
  `the matrix integral of the core action is not evaluated, no state is fixed, the missing
  steps of the Missing step paragraph are unchanged, and they close nothing in Problem~G.`
  + CRLFCRLF + line-start `\emph{Vacuum term.}`.
- Splice: insert `insert-r1.tex` bytes (one line + terminal CRLF) + one extra CRLF immediately
  before the G-side `\emph{Vacuum term.}` line. Nothing else kept or removed; no existing
  sentence is replaced.
- Paragraph-reference arithmetic verified against the live tree: from the new paragraph, the
  named coupled gaussian slot law (L3183) is the seventh preceding paragraph, the 089
  paragraph (L3191) the third preceding, and the Charge-to-edge moment identification
  paragraph (L3177) the tenth preceding.

Paragraph content: see `insert-r1.tex` (single line, 4,544 B, sha8 a39bcb33). Reproduction of
the full text is in that file; it is ASCII-only, one `\emph{}`, 50 balanced `\( \)` pairs, no
`$ [ ] \cite \ref \label \eqref`, no banned words {status, priority, completion, open,
critical, programme, derived} (substring-insensitive scan), ends with the close idiom "they
close nothing in Problem~G." (noun form; live counts 17 -> 18 expected, verb form stays 1).

Stale passages elsewhere: none created. The 091 sentence "its identification with the profile
coordinate of the moment map is not supplied by the repository" remains true and is not edited
(the new paragraph supplies a different transport, and the insert never claims the
Gram-spectrum identification).

## Verification scripts
All under this folder; run with `python -I` from the repository root. Reproduction pack
(expected invariant outputs):
- `python -I proposals/092-g-profile-coordinate-transport/s1b_transport_group.py` ->
  `S1B: PASS`; invariants: group law/inverse exact D=2,3; Jacobian sign "plus" D=2,3; D=4..8
  rel err <= 1e-30; density identity rel <= 1e-30. Shipped `.out` byte-matches stdout
  (re-run verified for s1b; all MC seeded).
- `python -I .../s2_moment_map.py` -> `S2: PASS`; invariants: 28 OK; det/V = +2, -6, -24 at
  D=2,3,4.
- `python -I .../s3_mc_transport.py` -> `S3: PASS`; invariants: reconstruction max err < 5e-3
  (observed 1.57e-3, seed 920); E[P_2] within 3 se of quadrature; E[p_1] within 1e-3.
- `python -I .../s4_mean_map_d2.py` -> `S4: PASS`; invariants: closed-form equality exact;
  limits 1/2 and 0; slope -1/6 at L=1; quadrature match 1e-12.
- `python -I .../hygiene_092.py` -> `HYGIENE 092: PASS` (46 OK; PRE sweep: 760528 B,
  sha256 46dbfb3f..., CRLF 3846, noun 17, verb 1, Vacuum 2, compound pin 1, header 0 hits
  across chapters).
- `python -I .../smoke_compile_092.py` -> `SMOKE 092: PASS` (POS rc 0; NEG rc 1 undefined
  control sequence; scratch dir deleted).
- `python -I .../simulate_apply_092.py` -> `SIMULATE 092: PASS`, `no write performed`;
  POST sha256 b1b62410229383c112d3a50e7c47f0beccdb3835001858d01628b31736b3fd0e, POST size
  765,074 B, CRLF 3848, bareLF 0, noun 18, verb 1, Vacuum 2, header 1.

## Decisions Taken
- **Attack choice.** Chose coordinate transport (frontier rank-1 avenue) over (2) closed-form
  eigenvalue prefactors beyond the D=2 fibre, (3) orbit-rigidity sharpening for the
  (|N-2M|+1,2) member, (4) the core-action matrix integral: (1) is the only avenue that acts
  directly on the INPUT-STATUS of the profile coordinate, which is what both OPEN edges
  (G.moments-interaction-nonconvex, G.moments-nonproduct-measures) hinge on; (4) was excluded
  as out-of-round-scope (requires dynamics), (2)/(3) are downstream of a coordinate choice and
  were left untouched. Within transport, chose the two maps actually executable in closed form
  (family-internal projective transport; charge-moment inversion) rather than the
  Gram-spectrum route, which is provably vacuous at rank one (single-atom spectrum - fact
  recorded in the insert), and rather than mean-map injectivity beyond D=2, which resisted
  proof (first variation at uniform vanishes identically).
- **Insert wording.** Recorded the 089-consistent honesty clause inside the manuscript
  sentence ("a reframing of the label data as a coordinate of the family, and it produces no
  profile from the core") rather than leaving the transport result readable as a derivation of
  the profile: preferred the stronger scope statement over the more favourable-sounding one.
- **Rejected**: proposing any identification of the slot-power coordinate with the 091
  Gram-spectrum coordinate (not derivable at rank one; would contradict the 091 closer).
  Rejected em-dash punctuation (non-ASCII) in favour of ASCII clause structure per contract.

## Milestone assessment
Routine. No MILESTONE.md trigger: no critical-path step derived for the programme; G remains
as recorded.

## Status-label recommendation
Unchanged for all labels (G: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL untouched; edges
G.moments-interaction-nonconvex and G.moments-nonproduct-measures stay OPEN). The insert adds
an exact within-class coordinate result; it does not meet any closure standard.

## Author decision needed
none

## Remaining open step
- Injectivity (or any coordinate property) of the pushforward-measure mean map or symmetric
  power-moment maps at D >= 3 - the natural next round of avenue (1): the vanishing of the
  first variation at the uniform profile forces any such proof through higher-order or
  nonlinear statistics.
- Non-invertible direction of the transport: deriving a profile from the group action without
  pre-loaded labels (would require the core to select the group element - the same
  state-selection input every preceding paragraph names as unsupplied; not reachable within
  the named measures).
- Sharpened orbit-rigidity reading of the Vandermonde singularity structure near coincidence
  walls (frontier avenue 3, now with a quantitative handle).
- The core-action matrix integral (frontier avenue 4) remains untouched, as do missing steps
  (i)-(iv).

## Special instructions for the gatekeeper
- Verify the insert ONLY inside the named classes: coupled gaussian slot law at strictly
  positive profile (transport orbit statement), and the L3177 leading-order convention
  (moment statement). The insert must not be read as supplying the Gram-spectrum/profile
  identification (091 closer stands) or as producing the profile from the core.
- Re-derive centrally: (a) the simplex Jacobian prod h_i/<h,p>^D (tangent-space rank-one
  update; the numeric checks are checks, not the proof); (b) E[T^p] = p! h_p(g) via the
  Laplace transform; (c) rho_p = 2^{p-1} m_{2p}/m_2^p = p! h_p/W^p and its agreement with
  L3177's rho_p definition, p=2,3; (d) the D=2 mean-map closed form by direct integration and
  its monotonicity sign; (e) the alternant Jacobian identity.
- Confirm PRE live before splicing (760,528 / 46dbfb3f... / CRLF 3846 / bareLF 0); POST
  expectations are those printed by simulate_apply_092.py (sha256 b1b62410229383c1...,
  765,074 B, CRLF 3848, noun 18, verb 1, Vacuum 2, header 1).
- Check the ordinal references in the insert (seventh/third/tenth preceding paragraph) against
  the post-splice tree.
