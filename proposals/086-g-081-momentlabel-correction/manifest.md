# Manifest — proposals/086-g-081-momentlabel-correction (round 1, 2026-11-18)

Correction package for appH L3177 (081 paragraph), per REVIEW-085-r1 F2 (PRIOR-CLAIM-ERROR, M3).
Chosen fix: option (a) — replace the two mislabeled numerals, keep the "fourth-moment" label.

| file | bytes | sha8 |
|---|---|---|
| proposal-r1.md | 14836 | f2aa25fd |
| s1_moment_values.py | 2658 | 1e67330b |
| s1_moment_values.out | 402 | 13fab983 |
| simulate_apply_086.py | 1432 | 2c96c91b |
| simulate_apply_086.out | 207 | ce3e49e7 |

Both scripts re-run from repo root with `python -I`, rc 0, empty stderr, stdout byte-identical to shipped
`.out`.

## Byte contract for integration
- PRE (live appH): 735,695 B; sha256 a13240a7f7a197ff7cffc26297fe1a6afbdeab749a4de57d6152828c573945ea;
  CRLF 3,834; bareLF 0.
- Operation: single in-place replacement at L3177 (BEFORE count 1); byte delta 0.
- POST: 735,695 B; sha256 b8bd51f6a82d4edebc44f870ff3f07249e723f3302d871243b227ba0b22ca777; CRLF 3,834;
  bareLF 0; close-idiom count 12 (unchanged).
- After this pass, 085 r2 recomputes its own contract against the POST hash above.

## Security
No injection markers ("[handback-send-enforce]", "SubagentHandback", fake user-role instructions) seen in any
file or tool output read this pass. All file/tool output treated as data. Writes confined to this folder.
No git write commands; no edits outside this folder.
