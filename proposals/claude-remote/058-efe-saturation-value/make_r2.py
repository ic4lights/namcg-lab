#!/usr/bin/env python3
"""Build proposal-r2.md from proposal-r1.md: r1->r2 change list, updated snippets, hashes, build and decisions."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
BS = chr(92)
p = open(os.path.join(HERE, 'proposal-r1.md'), encoding='utf-8').read()

def rep(old, new):
    global p
    old = old.replace('@', BS); new = new.replace('@', BS)
    assert p.count(old) == 1, (old[:70], p.count(old))
    p = p.replace(old, new)

HEADER = """# Proposal 058-efe-saturation-value, round 2

## r1 -> r2 changes (addressing review-r1.md)

- **Finding 1 (required), applied verbatim.** appE Edit 1 NEW is now the review's Corrected snippet. Assumption
  ass:efe's g_ext is stated as baryonic and v_⊙²/R_0 as the observed field, and "If eq:appE-RAR holds at the Sun"
  is stated as the condition for g_ext ≈ 1.5e-10 and ν ≈ 1.5. This replaces the r1 wording "If g_ext is instead
  read as the baryonic Newtonian field ...".
- **Finding 2 (required), applied verbatim.** In ch13 Edit 2 NEW, "The saturated boost" became
  "The saturated boost~@eqref{eq:efe-sat}" on the same line, followed by "is anisotropic at order". The rest of the
  edit is unchanged. The label `eq:efe-sat` (ch13 L240) is defined once.
- **Finding 3 (optional), adopted.** "is of the size of that saturated value" became "is comparable to that
  saturated value" in the ch16 edit and in appE Edit 2. This is decision D7.
- **Finding 4 (out of scope), not acted on.** The hard-coded "Theorems~7.3--12.4", "Appendix~D", "Theorem~7.3" and
  "Assumption~E.1", and the unsourced g_gal inputs, are left for a later bookkeeping item.
- **Unchanged.**
  - The r1 edit files are kept as `*_edits.r1.txt`, and the r1 check output as `apply_check.r1.txt`.
  - `appI_edits.txt` is byte-identical to r1.
  - ch13 Edit 1 (the sign fix) is unchanged.
  - `nu_check.py` and `nu_check.txt` are unchanged; no number changed.
- **Re-verified.**
  - The four target baselines are unchanged and match HEAD d24f435 (`git diff --quiet HEAD` clean).
  - `apply_check.txt` was re-run: ALL CHECKS PASS.
  - A new scratch build was run (see Verification scripts).

"""
rep("# Proposal 058-efe-saturation-value, round 1\n", HEADER)
rep("Result 17240 bytes, sha256 `23fc14239605dd258714a3c7fb4e6a5c995347bb2e660cca5942fb792f92fd9a`",
    "Result 17259 bytes, sha256 `66afb3c5a872d615324b0c4e869373048734f22241935d89a4d05e195a344eda`")
rep("1.35@). The saturated boost\nis anisotropic", "1.35@). The saturated boost~@eqref{eq:efe-sat}\nis anisotropic")
rep("Result 16833 bytes, sha256 `521226a8ee830dd31372c4c36144bad918bdec1af671bece503f9a61faf92ed4`",
    "Result 16832 bytes, sha256 `49529f7146e71e285e47b711c54eb7925e5b6a64b655151af55a21e42f3dc565`")
rep("1.4@) is of the size of that\n        saturated value;", "1.4@) is comparable to that\n        saturated value;")
rep("Result 13859 bytes, sha256 `a0dd0df8189dee98339750b3ed742394617c1e6ef7d8b624b122636f7cf7bd80`",
    "Result 13921 bytes, sha256 `854cc10a0e0363e25d6f79e7a5a40c222697398bc9bce6d535c977341e3e6dd8`")
rep("""If @(g_{@mathrm{ext}}@) is instead read as the baryonic Newtonian field
obtained by inverting~@eqref{eq:appE-RAR} at
@(g_{@mathrm{obs}}=v_{@odot}^{2}/R_{0}@), then
""", """Assumption~@ref{ass:efe} takes @(g_{@mathrm{ext}}@) to be baryonic,
whereas @(v_{@odot}^{2}/R_{0}@) is the observed field. If~@eqref{eq:appE-RAR}
holds at the Sun, inverting it at @(g_{@mathrm{obs}}=v_{@odot}^{2}/R_{0}@) gives
""")
rep("survives quality cuts is of the size of that saturated value; it would",
    "survives quality cuts is comparable to that saturated value; it would")
rep("`eq:nu-efe` (ch13 L228),", "`eq:nu-efe` (ch13 L228), `eq:efe-sat` (ch13 L240),")
rep("""  - Result: **365 pages**, the same as the repository's last log. **0 undefined, 0 multiply-defined** references
    or citations. No BibTeX warnings. FamaeyMcGaugh2012 and Chae2023WideBinaries resolved.
  - Deleting the scratch build directory was denied by the permission system. It remains in the session
    scratchpad, outside the repository.""",
"""  - **r2 result.**
    - Setup: a fresh directory `scratchpad/build058r2` holding the four r2 files written by
      `apply_check.py <scratch>/out058r2` (sha256 prefixes 66afb3c5, 49529f71, 854cc10a, b91dc5e4).
    - All runs exit 0. **365 pages**, the same as the repository's last log.
    - **0 undefined, 0 multiply-defined** references or citations. No BibTeX warnings.
  - The r1 scratch build gave the same result. Deleting the r1 build directory was denied by the permission system.
    It and the r2 build directory remain in the session scratchpad, outside the repository.""")
rep("- **D6. Cite Chae2023WideBinaries", """- **D7 (r2, review Finding 3). Use "comparable to", not "of the size of".**
  - Chae's 1.43 is measured at g_N/g_ext ≈ 0.3, outside the strict g_N ≪ g_ext limit. There the ν_√
    quadrature-sum value is at most 1.35, and the orbit-averaged anisotropic value is lower.
  - "Comparable to" records order-of-size agreement and does not suggest a match at the limit.
  - Rejected: keeping the r1 wording, which the gatekeeper found acceptable but which is less conservative.
- **D6. Cite Chae2023WideBinaries""")
rep("- Integration ordinal would be 56.\n",
    "- Integration ordinal would be 56. Review-r1 ruled the CLAUDE.md 3(c) full-scan requirement satisfied in substance,\n  on the basis of the ordinal-55 scan record, the unchanged target hashes and the dependency sweep.\n")
p = p.replace(BS + 'n', BS + 'n')
open(os.path.join(HERE, 'proposal-r2.md'), 'w', encoding='utf-8', newline='\n').write(p)
print('proposal-r2.md written,', len(p.encode('utf-8')), 'bytes')
