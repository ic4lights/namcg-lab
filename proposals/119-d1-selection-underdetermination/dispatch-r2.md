# Orchestrator dispatch note - chain 119 round 2 (2026-11-23)

Verdict r1: ACCEPT WITH REQUIRED REVISIONS (review-r1.md 484736e8c8f0/17539). Payload/proposal NOT integrated. Round 2 = required actions only.

## Mandatory actions (verbatim intent)
- F-1 (MINOR, payload): rays iff -> ">=", equality case = single marginal double ray r*=sqrt(42)/14; window clause strict "<": none occur for 0<=w<64+16sqrt42. Snippet in review-r1 Corrected snippet block.
- F-2 (MAJOR, payload): displayed beta system is u(4) instance (beta_c3 carries +4w = A_G w with A_G=4) while parenthetical paired su(4) B_G=1/16 with it. Choose (a) label system u(4), state su(4) channel data A_G=N-2/N=7/2 with B_G=1/16 outside the displayed pairing (gatekeeper snippet, smallest-text default), or (b) parameterize P(r)=448r^2+(256+4v4-A_G w)r+96+B_G w, rays iff ((A_G/4)w-v4-64)^2>=10752+112B_G w, (A_G,B_G)=(4,0)/(7/2,1/16). Pick ONE, record rationale in proposal Decisions.
- F-3 (MAJOR, payload + proposal): shift clause -> commutator-type lifts only; state that the eq:Smicro lift (D_mu Phi = partial_mu Phi - i A_mu Phi, left mult on I index) and the eq:dictionary bridge are NOT shift-covariant. Sync proposal reasoning item 1 wording ("minimal shift-symmetric lift" -> commutator-type lift + non-invariance note).

## Constraints
- Baseline re-verify live before byte work: appH 2ed53c7778c1 / 843649, anchor \section{Problem E: signature} count 1 @ 290106. If moved: STOP, report.
- Notation: gatekeeper snippets use \Tr - verify which trace macro the adjacent appH paragraphs actually use (grep namcg-book7.tex preamble + neighbors); match the manuscript, not the snippet.
- Supersession before edit: insert-overdetermination-r1.tex -> insert-overdetermination-r1-superseded-r1.tex; proposal-r1.md -> proposal-r1-superseded-r1.md; gen_payload_119.py -> gen_payload_119-superseded-r1.py. Record old+new sha1/size with reason in manifest.
- Verify pack: if (b) chosen, ADD generalized-discriminant-identity check (both instances); D3/D3b wording align optional per F-5. Raw recapture to NEW filename (out-r119-r2.txt), print TOTAL + ALL CHECKS DONE 119; never hand-edit outputs.
- Generator re-run twice byte-identical, join-guard positive control intact.
- Cert: hard asserts updated (baseline pin, anchor, NEW payload pin, POST = 843649 + len + 2 byte-reconstructed from live tree, sha1 printed); run in fresh out-of-repo temp tree; output out-cert-r119p-r2.txt.
- manifest.md fully re-pinned incl review-r1.md 484736e8c8f0/17539; self-hash cell per its documented rule.
- No changes beyond F-1/F-2/F-3 + the syncs they force; no status/priority/completion language; rule-3 disclaimer sentence unchanged in force; CRLF/ASCII/no-BOM.

## Report back
New pins (payload/proposal/generator/manifest), POST bytes + sha1, TOTAL x/x, CERT result, F-2 option chosen + rationale, any place review-r1 conflicted with live sources (report, do not fix silently).
