# Manifest 087-g-derivedprofile-selection, round 1 (2026-11-18)

Resumed dead pass: the previous researcher completed all computation and
died to context overflow before writing the proposal body. All shipped
artifacts were re-hashed AND every script re-run this pass with
`python -I` from the repository root; stdout of every re-run was
byte-identical to the shipped .out (see table). One defect was found in the
shipped simulator (same-line splice, see proposal "Proposed changes"); the
shipped file is kept unmodified for the audit trail and superseded by
simulate_apply_087_fix.py (added this pass), which is AUTHORITATIVE.

## File table (size B / sha256 first 8)

Carried from dead pass, re-verified byte-identical on 2026-11-18:
- build_insert_087.py 5,460 / 4f02d531 (re-run: regenerates insert-r1.tex
  exactly, 5,280 / 3fc233c9)
- insert-r1.tex 5,280 / 3fc233c9 (the manuscript insert, single content line
  + terminal CRLF)
- hygiene_087.py 1,921 / ffd08b6c ; hygiene_087.out 1,336 / f8a7016a (PASS)
- s1_variance_graph.py 5,769 / fbfc512a ; s1_variance_graph.out 397 / dba73a0c
- s2_haar_stiffness.py 4,359 / a389d3d8 ; s2_haar_stiffness.out 652 / 70abf974
- s3_proxy_closedforms.py 5,501 / 4f203f52 ; s3_proxy_closedforms.out 1,261
  / e5a483ee
- s4_selection_content.py 4,456 / 584e64ec ; s4_selection_content.out 483
  / 53fcf550
- simulate_apply_087.py 1,796 / 93d77efb ; simulate_apply_087.out 382
  / b1e2855a (SPLICE DEFECTIVE: same-line splice; stdout reproduces
  byte-identically but its POST 744,376 / d65eb64f is DEAD - do not integrate
  against it)

Added this pass:
- simulate_apply_087_fix.py 3,096 / 62cb48c9 ; simulate_apply_087_fix.out
  589 / fb1359a2 (AUTHORITATIVE splice: 085-recipe Vacuum-line-start splice;
  POST 744,378 B / sha256 38db6497530b15663f6d206912dfce0e59662941eb1dc3d46
  912ae7d43d640bd / CRLF 3,838 / bareLF 0 / close-idiom 14 / new header 1 /
  Vacuum-term 2)
- proposal-r1.md (see current hash at end of pass)
- manifest.md (this file)

Live-repo pins at this pass (read-only, unchanged before/after all runs):
chapters/appH-microscopic-proofs.tex 739,096 B / sha256
31b345ed5e957910bacd3c02ebae87edfbeb5f0effa77c98149f6eafc2a2679d / CRLF 3,836
/ bareLF 0. Digest: DIGEST STALE (head changed) - not regenerated per
dispatch; no conclusion relies on the digest (all targeted reads from the
pinned live bytes). No git write commands were run; no file outside this
proposal folder was created or modified by this pass.

## Reproduction pack (run from the repository root; expect exit 0)

1. python -I proposals/087-g-derivedprofile-selection/build_insert_087.py
   -> stdout "insert bytes 5280"; insert-r1.tex stays 5,280 / 3fc233c9.
2. python -I proposals/087-g-derivedprofile-selection/s1_variance_graph.py
   -> stdout == s1_variance_graph.out (dba73a0c); invariants: 200/60/360
   "OK" lines, "S1 DONE".
3. python -I proposals/087-g-derivedprofile-selection/s2_haar_stiffness.py
   -> stdout == s2_haar_stiffness.out (70abf974); invariants: Sigma_Haar
   exact D=2..8, "S2 DONE".
4. python -I proposals/087-g-derivedprofile-selection/s3_proxy_closedforms.py
   -> stdout == s3_proxy_closedforms.out (e5a483ee); invariants: shortfall
   strictly positive for L>=2, limit 1/9; leading fixed-nu term L^2/72;
   D_eff 1488 / 23017 at L=40 / 160; "S3 DONE".
5. python -I proposals/087-g-derivedprofile-selection/s4_selection_content.py
   -> stdout == s4_selection_content.out (53fcf550); invariants: E_pi Gamma
   = 0 exactly, D_eff = 338/109 < 4; "S4 DONE".
6. python -I proposals/087-g-derivedprofile-selection/hygiene_087.py
   -> stdout == hygiene_087.out (f8a7016a); invariant: "overall PASS".
7. python -I proposals/087-g-derivedprofile-selection/simulate_apply_087.py
   -> stdout == simulate_apply_087.out (b1e2855a) [deterministic re-check of
   the DEAD contract only; not an integration target].
8. python -I proposals/087-g-derivedprofile-selection/simulate_apply_087_fix.py
   -> stdout == simulate_apply_087_fix.out (fb1359a2); invariants: PRE 739,096
   / 31b345ed...; POST 744,378 / 38db6497... / CRLF 3,838 / bareLF 0;
   close-idiom 14; header 1; Vacuum 2; three boundary probes CRLFCRLF;
   "no write performed".

## Hygiene notes (from hygiene_087.py, part of the contract)

insert-r1.tex: single content line + terminal CRLF; no control bytes < 0x20
except terminal; valid UTF-8 no BOM; no dollar sign, square brackets, \cite,
\ref, \eqref, \label; none of the words status / priority / completion /
open / critical / programme / derived; exactly one \emph header, unique
across chapters/; braces and parens balanced; ends with the block close
idiom; every numeral within a derivable allowlist (all traceable to the
s1-s4 closed forms or to integrated L3177 numerals). No bib entries needed
(insert cites nothing). Tex style: insert is one content line; the
integrator splices bytes exactly as in reproduction step 8 (CRLF-preserving
binary splice; no editing of the line).

manifest.md size/sha8 at close of pass: 4946 / 323f5412
