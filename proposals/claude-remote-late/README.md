# Evidence from the late window of the other branch (`origin/remote/claude`)

Copied verbatim on 2026-11-25 by the orchestrator at the author's instruction ("route the held
data"). Nothing edited, renumbered or merged: each file is the blob from `origin/remote/claude`
at tip `1aafb3d` (2026-11-25). Companion to `proposals/claude-remote/` (the same branch at tip
`e59a120`, copied 2026-11-11; see `reports/merge-remote-claude-20261111.md`).

## Why these are namespaced

That branch ran its own pipeline after the 2026-11-05 fork at `2cd49d0` and reused ordinals
054-067 for different proposals; items 068-076 here are ITS items, not comparable to any local
number. Their integrated appH text reached this branch's tip and produced the held blocks
analysed in `reports/rc-import-review-2026-11-25.md` and
`reports/rc-parallel-apph-blocks-2026-11-25.md`, which had no provenance here until this copy.

## Provenance (their own gatekeeper's last recorded verdicts)

| item | their verdict (latest review) | probable held-block link |
|---|---|---|
| `068-d1-torsion-nonzero` | ACCEPT (conditional on scan passes 2-4 CLEAN) | E-relaxations / torsion material (block 27 region) |
| `069-f-nonderivative-sector` | ACCEPT, M3, PRIOR-CLAIM-ERROR | F q=0 non-derivative sector (block 48 region) |
| `070-b-content-class` | NEEDS EVIDENCE | B/C content-class passages (block 22 region; UNRESOLVED there too) |
| `071-d1-curved-torsion-backgrounds` | ACCEPT WITH REQUIRED REVISIONS (flat) | block 27 region |
| `072-d1-heisenberg-wider-linearised` | ACCEPT WITH REQUIRED REVISIONS | Heisenberg Landau sectors (block 28) |
| `073-d1-heisenberg-nonnull-leg` | ACCEPT (conditional) | block 28 region |
| `074-f-tree-nonderivative-wave` | ACCEPT (conditional) | tree non-derivative waves (block 48) |
| `075-d1-cubic-term` | NEEDS EVIDENCE, M2 (UNRESOLVED there too) | cubic/mass branches (block 48 region) |
| `076-fc-singlet-kinetic-matrix` | ACCEPT (conditional) | singlet sector q=0 (blocks 49/50/51) |

"Conditional" verdicts referenced their own scan passes; per CLAUDE rule 6 none of this is
authoritative here. The re-derivation and intake decision for all held material is item
`proposals/129-rc-held-recheck/` (researcher), whose gatekeeper then follows the normal route.
Their scripts, if used as reproduction packs, must be read before running.
