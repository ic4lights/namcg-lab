# Manifest 085-g-moments-uniformity-locus, round 1

Target: frontier chain-2 rank 1 `G.moments-derivedprofile` (partial constraint
package; no closure). Proposed integration ordinal: next after 084 (15).

## Files (bytes / sha256-8)
- proposal-r1.md                    17480 7db7623a
- insert-r1.tex                      3371 994032c1   (single content line + 1 CRLF, UTF-8 no BOM, one \emph, banned-token sweep 0, no $ [ ] cite/ref/label)
- s1_locus_algebra.py                3092 f98632d2   out 1086 149c117a
- s2_haar_average.py                 2177 e21cca4e   out  575 0357b5c9
- s3_profile_extremes.py             2835 c067395e   out 1107 9e8cf9b3
- s4_joint_channel.py                5331 da09a518   out  850 6ab8ae15
- s5_proxy_locus_negative.py         2115 68bead5f   out 1227 233420a5
- simulate_apply_085.py              2232 dc2a6fcc   out  299 02fc519f (READ-ONLY, opens files 'rb' only)

All scripts re-run 2026-11-18 with `python -I <script> > <script>.out` from the
repo root; outputs deterministic (second run byte-identical, 6/6).

## Byte contract
PRE appH 735695 B / sha256 a13240a7... (sha8 a13240a7) / CRLF 3834 / bareLF 0
(uncommitted 081-084 on HEAD 384dfc1). Pin: full 084 closer sentence ending
"close nothing in Problem~G.", count 1; gap pin->G-side `\emph{Vacuum term.}`
exactly CRLFCRLF. Splice insert bytes + one CRLF before the anchor.
Expected POST: 739068 B / sha256 93d92968f519889cc367db2e74d95741e486e247b53df7bc49cb18bb51b44343 / CRLF 3836 / bareLF 0; close-idiom 12->13; new header count 1; `\emph{Vacuum term.}` count 2 (L3006 Problem F untouched).

## Lineage
081 (moment map, D_eff, proxies) -> 082 (fixed-D floor, uniform minimiser) ->
083 (master map, independence hypothesis) -> 084 (coupled slot law, Gamma,
128 s^4 excess, a-perp-r iff Gamma=0) -> 085 (uniformity consistency locus,
E_u Gamma identity, conditional selection sentence, proxy negative datum).
No consumed edge re-opened; no status/priority/completion text touched.

## Dead work registered
- scratch/wip085/: created, left empty (no WIP shipped).
- s3 and s4 carry in-place byte-surgery corrections made during development
  (s3: undefined index in the product call; s4: rng source, exact rational
  substitution restricted to unit frames, pooled-MC target corrected by the
  frame-level term -Var_u(mu)/2). The shipped .py files are the corrected
  versions; superseded drafts were never run to green and are not shipped.

## Claims at a glance (classification)
Established-in-class: full-support-frame decoupling iff uniform; slice bounds
on sum g^2 and the rho_2-1 range; E_u Gamma = W^2(D_eff^-1-D^-1)/(D+1) with
Haar frames; frame-averaged excess 128 s^4 W^2(D_eff^-1-D^-1)/(D+1); uniform
profile = unique common locus at fixed D; proxy profiles strictly off the locus
with exact reproduction of the integrated D_eff values and identification of
the quoted excesses as the p=4 leading bound.
Conjecture/mechanism (explicitly conditional in the insert): matrix-model
selection of the locus. Inputs unchanged: W, g, s, u, slot law.
