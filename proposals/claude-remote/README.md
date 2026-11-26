# Evidence from the other branch of the 053 fork (`origin/remote/claude`)

Copied verbatim on 2026-11-11 by the orchestrator at the author's instruction. Nothing in this
tree was edited, renumbered or merged: each file is the blob from `origin/remote/claude` at
tip `e59a120`.

## Why these are namespaced

The manuscript work in this folder was integrated on `origin/remote/claude`, which forked from the
local line at `2cd49d0` (after proposal 053 r1/r2) and then ran its own cycle. That run reused the
proposal ordinals `054`-`067` for proposals that are **not** the proposals carrying the same numbers
in `proposals/054-*` .. `proposals/068-*` here. The numbers are therefore not comparable across the
two sets; the slugs are the identifiers. See `reports/merge-remote-claude-20261111.md`.

## Provenance

| item | state on that branch | integrated text |
|---|---|---|
| `053-lorentzian-integral-limit-order` | r3 round, ACCEPT, M3, PRIOR-CLAIM-ERROR | that branch's own 053 r3 text (the local line ran a different 053 r3) |
| `054`-`065` | ACCEPT after revision (some rounds AWRR) | yes, into `appH`, `bib`, `ch13`, `ch16`, `appE`, `appI`, `ch14` |
| `066-bw-diamond-scope-correction` | **STALLED at the round cap after r4 (AWRR), never integrated** | none |
| `067-product-sphere-edge` | two working files only, no ledger entry | none — un-ledgered work in progress |

Dates on that branch: 2026-11-06 .. 2026-11-09. Their integrated-item count reached 65; the local
line's count reached 68. The two counts are separate runs, not a single sequence.
