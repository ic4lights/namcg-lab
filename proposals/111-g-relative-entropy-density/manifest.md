# Manifest 111-g-relative-entropy-density — r2 revision (2026-11-22)

RESTATED FROM ACTUAL DISK BYTES (review-r1.md F1, blocking). Every sha1-10 and byte
count below was computed from the file as it now sits in this folder (sha1sum + stat,
2026-11-22, post-r2). Integrators pin ONLY hashes of actual files.

PROVENANCE (F1): the r1-pass entry for p2_fock_srel.py stated sha1-10 0904f2f7d8; that
entry was STALE (the folder is untracked; those bytes are unrecoverable). The on-disk
file, sha1 b6bac2a036398994d7b2f848ee99914eeab532da (1565 B, bytes unchanged since the
r1 pass), was verified by the gatekeeper (review-r1, "Object shas" and "P1/P2/P3
re-run" rows) to run and reproduce every P2 number in the proposal exactly; the
evidence chain is therefore closed on the on-disk bytes and the manifest is restated
from disk. FROZEN battery/probe files were NOT modified in r2 (F6: the
p1_symbolic_a0.py comment noted in review-r1 is deliberately left as-is so its pinned
hash 8d2bd3624d stays verifiable).

## r2 pin table (sha1-10, bytes) — all values from disk this pass

| file | sha1-10 | bytes | note |
|---|---|---|---|
| proposal-r2.md | f3d9ee751e | 27143 | round-2 proposal (record-level corrections F2-F5 + changelog) |
| r1_to_r2.diff | b50734e91a | 6284 | unified diff r1->r2, 5 hunks / 6 changed body lines |
| surg_r2.py | 7bc53cbdd2 | 5958 | byte-surgery script that produced r2 + diff (python -I surg_r2.py; asserts counts and post-checks) |
| proposal-r1.md | 7aee411e3f | 24966 | round-1 proposal (frozen for the diff) |
| review-r1.md | 48118920cf | 10209 | gatekeeper review r1 (ACCEPT WITH REQUIRED REVISIONS) |
| _common.py | 52497c0c45 | 8018 | battery core (FROZEN, unchanged) |
| check_modular.py | cd982322f9 | 4628 | battery driver (FROZEN, unchanged) |
| run_modular.out | 7247af5bf4 | 2250 | battery output (FROZEN, unchanged) |
| rerun.out | 7247af5bf4 | 2250 | battery re-run, byte-identical to run_modular.out |
| p1_symbolic_a0.py | 8d2bd3624d | 1407 | P1 exact n=1 congruence proof (FROZEN; F6 comment fix deferred so this pin stays verifiable) |
| p2_fock_srel.py | b6bac2a036 | 1565 | P2 two-state direct-vs-form anchor; FULL sha1 b6bac2a036398994d7b2f848ee99914eeab532da (supersedes stale 0904f2f7d8, see PROVENANCE) |
| p3_fock_srel_cold.py | 819d478da6 | 1410 | P3 gap decomposition, clipped-log final (FROZEN, unchanged) |
| stab-notes.md | 9293e644f8 | 3107 | stabilization notes (cited) |
| stab_probe1.py | bf79f76518 | 795 | stabilization probe (cited as scalars only) |
| stab_probe2.py | f8da9b9c41 | 1005 | stabilization probe (cited as scalars only) |
| stab_probe3.py | 152fb87d40 | 733 | stabilization probe (cited as scalars only) |
| stab_probe4.py | 2831404d37 | 388 | stabilization probe (cited as scalars only) |
| stab_run0.txt | 306a9e67a0 | 3216 | stabilization run log (context only) |
| stab_run1.txt | dd41242279 | 2424 | stabilization run log (context only) |
| diag1.py | 89163d03dd | 1631 | QUARANTINED, NOT CITED |
| diag2.py | cd77d7c06c | 907 | QUARANTINED, NOT CITED |
| probe2.py | 7eccf7f43e | 1556 | QUARANTINED, NOT CITED |
| probe3.py | 78ea8401f0 | 2637 | QUARANTINED, NOT CITED |
| run_modular_deadpass.log | b92a33e906 | 3206 | QUARANTINED, NOT CITED |

manifest.md carries no self-hash. __pycache__/ is transient (excluded).

## HISTORY — r1-pass section, SUPERSEDED by the table above (do not pin from it)

Preserved verbatim below for audit; note its p2 row (0904f2f7d8) was the stale entry
corrected per F1.

## R111 WRITE-UP pass 2026-11-22 (appended; sha1-10, bytes)

| file | sha1-10 | bytes | note |
|---|---|---|---|
| proposal-r1.md | 7aee411e3f | 24966 | round-1 proposal (FINAL after this append) |
| p1_symbolic_a0.py | 8d2bd3624d | 1407 | P1 exact n=1 congruence proof (hash supersedes e4885a8d98 above; file current) |
| p2_fock_srel.py | 0904f2f7d8 | 1565 | P2 two-state direct-vs-form anchor [STALE PIN, see F1] |
| p3_fock_srel_cold.py | 819d478da6 | 1410 | P3 gap decomposition, clipped-log final (supersedes 4336c79164) |
| rerun.out | 7247af5bf4 | 2250 | battery re-run, byte-identical to run_modular.out |
| stab-notes.md | 9293e644f8 | 3107 | stabilization notes (cited) |
| stab_probe1..4.py | bf79f76518 f8da9b9c41 152fb87d40 2831404d37 | 795 1005 733 388 | stabilization probes (cited as scalars only) |
| stab_run0.txt stab_run1.txt | 306a9e67a0 dd41242279 | 3216 2424 | stabilization run logs (context only) |
| diag1.py diag2.py probe2.py probe3.py run_modular_deadpass.log | 89163d03dd cd77d7c06c 7eccf7f43e 78ea8401f0 b92a33e906 | 1631 907 1556 2637 3206 | QUARANTINED, NOT CITED |

CORRECTION: the 110-probe entries (probe_344..347.py) added above by another writer are
NOT files of this folder (absent from its listing); they belong to the 110 chain folder.
Verified present in this folder at this pass: the 17 rows above plus the battery trio and
run_modular.out (unchanged hashes); no other files (probe_340..343.py also absent).
