# Manifest 085-g-moments-uniformity-locus, round 2

Target: frontier chain-2 rank 1 `G.moments-derivedprofile` (partial constraint
package; no closure). Round 2 executes review-r1 required revisions (F1-F5,
claim-7 withdrawal) and re-pins all byte contracts to the post-INTEGRATION-16
live tree. This file supersedes manifest.md (r1, kept unmodified) for
integration; manifest.md itself is not edited.

## Files (bytes / sha256-8), re-hashed fresh 2026-11-18 (round 2)
Round-1 history (kept, unmodified; hashes re-measured and confirmed):
- proposal-r1.md                    17480 7db7623a   (matches r1 manifest)
- insert-r1.tex                      3371 994032c1   REJECTED as written (F1/F4)
- s1_locus_algebra.py                3092 f98632d2   out 1086 149c117a
- s2_haar_average.py                 2177 e21cca4e   out  575 0357b5c9
- s3_profile_extremes.py             2835 c067395e   out 1107 9e8cf9b3
- s4_joint_channel.py                5331 da09a518   out  850 6ab8ae15
- s5_proxy_locus_negative.py         2115 68bead5f   out 1227 233420a5
- simulate_apply_085.py              2232 dc2a6fcc   out  299 02fc519f  RETIRED
- review-r1.md                      19570 d0d9661e
- manifest.md                        3046 76fef361
Round-2 work (new):
- proposal-r2.md                      30331 0e2288fb
- insert-r2.tex                     3399 63f76322   single content line + 1 CRLF, UTF-8 no BOM, one \emph, banned set 0, no $ [ ] cite/ref/eqref/label (hygiene_r2.out)
- build_insert_r2.py                1224 82fc7e68   byte-surgery r1 -> r2 (2 asserted single-occurrence edits)
- s6_r2_f1_ramp.py                  2356 f4bb2cdf   out 1157 b9bda10c (F1/F5 exact-rational ramp, both slot-count conventions; .py carries a disclosed 2e-3 -> 5e-3 tolerance patch for two 3-s.f. quoted references)
- hygiene_r2.py                     1731 add525d0   out  389 99f34023
- simulate_apply_085_r2.py          2617 c85325f9   out  518 aa3a6055 (READ-ONLY, opens 'rb' only, prints "no write performed")
- manifest_r2.md                       this file (self-hash not listed)

## r1 manifest discrepancy check (dispatch item, recorded honestly)
The round-2 dispatch expected a hash mismatch for s4_joint_channel.py in the r1
manifest. Round-2 re-hash: on-disk s4_joint_channel.py = 5,331 B / sha8
da09a518, exactly as manifest.md lists, and review-r1 Source reading also
recorded all r1 sizes/sha8 as matching. The discrepancy is NOT reproducible
against the current on-disk file; recorded as a no-finding. All other r1 files
likewise match their r1-manifest entries.

## Byte contract (round 2; the r1 contract is VOID)
PRE appH 735,695 B / sha256 b8bd51f6a82d4edebc44f870ff3f07249e723f3302d871243b
227ba0b22ca777 / CRLF 3,834 / bareLF 0 (INTEGRATION-16 state: 086 correction on
top of the uncommitted 081-084 paragraphs, HEAD 384dfc1, dirty-chapters yes).
Pin: full 084 closer sentence ending "close nothing in Problem~G.", count 1;
short suffix "do not fix the state that sets" count 5, NEVER a pin; gap
pin -> G-side `\emph{Vacuum term.}` exactly CRLFCRLF; anchor at line start
(insert offset byte 698,878). Splice insert-r2.tex bytes + one CRLF.
Expected POST: 739,096 B / sha256 31b345ed5e957910bacd3c02ebae87edfbeb5f0effa7
7c98149f6eafc2a2679d / CRLF 3,836 / bareLF 0; close-idiom 12 -> 13; new header
count 1; `\emph{Vacuum term.}` count 2 (F-side untouched). Void: r1 POST
739,068 / 93d92968... (tied to the rejected insert-r1 bytes AND the superseded
PRE a13240a7).

## Proxy slot-count convention (F5 record)
sum_{l=1..l_c}(2l+1) = (l_c+1)^2 - 1 nonzero-variance slots; D = (l_c+1)^2 adds
one l=0 zero-variance (g=0) slot, which leaves W, sum g_i^2 and D_eff invariant
(s5 evaluated D = 1681, 25921 with the zero slot, D_eff = 1488.00/23016.89
unchanged; s6 prints E_u Gamma under both conventions: 23.2332 vs 23.3264 at
l_c = 40). The review-r1 ramp data (23.233/91.009/359.9/1431; fixed-W
4.57e-8 -> 1.18e-11) correspond to the no-zero-slot convention D = (l_c+1)^2-1.
No manuscript surface carries either slot count.

## Lineage
081 (moment map, D_eff, proxies; numerals corrected by 086) -> 082 (fixed-D
floor, uniform minimiser) -> 083 (master map, independence hypothesis) -> 084
(coupled slot law, Gamma, 128 s^4 excess, a-perp-r iff Gamma=0) -> 086
(factor-6 moment mislabel correction, integrated ordinal 16, discharges
REVIEW-085-r1 F2) -> 085 r2 (uniformity consistency locus, E_u Gamma identity,
conditional selection sentence, proxy negative datum with the fixed-W/fixed-nu
distinction). No consumed edge re-opened; no status/priority/completion text
touched.

## Claims at a glance (classification)
Established-in-class: full-support-frame decoupling iff uniform; slice bounds on
sum g^2 and the rho_2-1 range; E_u Gamma = W^2(D_eff^-1-D^-1)/(D+1) with Haar
frames; frame-averaged excess 128 s^4 W^2(D_eff^-1-D^-1)/(D+1); uniform profile
= unique common locus at fixed D; proxy profiles strictly off the locus with
exact reproduction of the integrated D_eff values and of the corrected
1/D_eff = 6.7e-4 / 4.3e-5 fourth-moment excesses; F1 datum (fixed-nu growth
~ nu^2 L^2/72 vs fixed-W decay ~ W^2/(8D^2), exact rationals, s6).
Conjecture/mechanism (explicitly conditional in the insert): matrix-model
selection of the locus. Inputs unchanged: W, g, s, u, slot law.
WITHDRAWN: round-1 claim 7 ("false-alarm resolution" of the 6x factor; the
prior error was real - corrected by 086 as ordinal 16).
