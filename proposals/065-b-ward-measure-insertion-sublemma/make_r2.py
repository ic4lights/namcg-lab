"""Round-2 generator: builds proposal-r2.md from proposal-r1.md with the
review-r1 fixes. Run: python -I make_r2.py  (from the proposal folder)
"""
import io

NL = chr(10)
s = io.open('proposal-r1.md', encoding='utf-8').read()


def rep(old, new, cnt):
    global s
    c = s.count(old)
    assert c == cnt, (c, cnt, old[:60])
    s = s.replace(old, new)


# (a) title
rep("# Proposal 065-b-ward-measure-insertion-sublemma, round 1",
    "# Proposal 065-b-ward-measure-insertion-sublemma, round 2", 1)

# (b) chain sign fix (embedded insert + R3 prose)
rep(r"\langle\mathcal I_n\rangle_n=-\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n=0",
    r"\langle\mathcal I_n\rangle_n=\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n=0", 2)

# (c) insert descriptor (single line in the md)
rep("Insert (LF form, 6,668 bytes, sha256 `46a385840371e54af11590a143faf5cac3df58eb84b490c995a96381bfa051d3`):",
    "Insert (LF form, `insert-r2.tex`, 6,667 bytes, sha256 `7db417b6931078e143287531785cd5ff27e1531249b39d2f2f06da514c82b3d7`):"
    + NL
    + "the only difference from the r1 insert is the one-character sign fix of Revision-note finding 1 (diff"
    + NL
    + "verified: exactly one changed line, deletion of a single `-`).", 1)

# (d) predicted post-state appH
rep("- `chapters/appH-microscopic-proofs.tex`: **589,389 B, CRLF 3450, bare LF 0, sha256" + NL
    + "  `46ba16b9398ec63c1f70f8cabb046803968f635dc9aa029ee827b55fe1ebf26b`**.",
    "- `chapters/appH-microscopic-proofs.tex`: **589,388 B, CRLF 3450, bare LF 0, sha256" + NL
    + "  `d94b79458c3e3613992ed66b8ac12024db84f6f44910ebc0d1e0081e14dafe3d`** (reproduces the gatekeeper's" + NL
    + "  independent computation exactly).", 1)

# (e) stale r1 hash mention in Decisions
rep("new appH post" + NL + "  hash 46ba16b9…",
    "new appH post" + NL + "  hash 46ba16b9…, superseded by the round-2 sign fix: the current post hash is d94b7945…", 1)

# (f) paragraph range fix (finding 3)
rep('the "Matrix gauge realisation" paragraph (appH L462–471)',
    'the "Matrix gauge realisation" paragraph (appH L466–477; the recorded conclusion quoted here sits at' + NL
    + '  L462 in the preceding paragraph)', 1)

# (g) tr ad coefficient fix (finding 4)
rep(r"$\operatorname{ad}_\Lambda=I\otimes\Lambda-\Lambda^{T}\otimes I$ on $2\times2$ matrices has" + NL
    + r"$\operatorname{tr}\operatorname{ad}_\Lambda=4\operatorname{tr}\Lambda-4\operatorname{tr}\Lambda=0$ (symbolic, general" + NL
    + r"$\Lambda$)",
    r"$\operatorname{ad}_\Lambda=I\otimes\Lambda-\Lambda^{T}\otimes I$ on $N\times N$ matrices has" + NL
    + r"$\operatorname{tr}\operatorname{ad}_\Lambda=N\operatorname{tr}\Lambda-N\operatorname{tr}\Lambda=0$ for every $\Lambda$" + NL
    + r"(the script checks the $2\times2$, $N=2$, general-$\Lambda$ case; my r1 form with the coefficient 4 was" + NL
    + r"the wrong coefficient for the checked case, gatekeeper finding 4)", 1)

# (h) add r2 simulator bullet
rep("predicted" + NL + "  post-states above. Read-only (in-memory simulation; verified twice, outputs byte-identical).",
    "predicted" + NL + "  post-states above. Read-only (in-memory simulation; verified twice, outputs byte-identical)." + NL
    + "- `simulate_apply_r2.py` (3,654 B, sha256 `0208241dc4ae8db277624cb57d8528736e666d836bd12a682d527768b2f4b567`)" + NL
    + "  / `simulate_apply_r2.out` (1,204 B, sha256 `860c9b01cd106bbad5d7a6de126d048320d2eeea9e78a5aae2d6e8f9b1e94cc4`):" + NL
    + "  identical checks against `insert-r2.tex`; reproduces insert 6,667 B and appH post 589,388 B /" + NL
    + "  CRLF 3450 / bare LF 0 / sha256 d94b7945…, bib post unchanged (31,789 B / 9e9dfa06… / 99 entries). The r1" + NL
    + "  simulator and its `.out` are retained unchanged for provenance.", 1)

# (i) source reading addendum
rep("Prior proposals 062 (C no-go style precedent) and 063/064 folders were read to avoid repeating routes.",
    "Prior proposals 062 (C no-go style precedent) and 063/064 folders were read to avoid repeating routes." + NL
    + "Round 2: `proposals/065-b-ward-measure-insertion-sublemma/review-r1.md` read in full.", 1)

# (j) special instruction update for r2 re-runs
rep("- Re-run `python -I derive_ward_r1.py` and `python -I simulate_apply.py`; outputs must match the `.out`" + NL
    + "  files byte-for-byte.",
    "- Re-run `python -I derive_ward_r1.py` (unchanged in r2; its Check 1 already encodes the plus relation) and" + NL
    + "  `python -I simulate_apply_r2.py`; outputs must match `derive_ward_r1.out` and `simulate_apply_r2.out`" + NL
    + "  byte-for-byte.", 1)

# (k) Decisions bullet for r2
rep("- **No eprints added to LM / Donnelly–Wall / Solodukhin** (hazard: bib carries none; none are cited).",
    "- **No eprints added to LM / Donnelly–Wall / Solodukhin** (hazard: bib carries none; none are cited)." + NL
    + "- **Round 2 (r1 finding 1):** accepted the required sign fix in full (minus → plus in the unimodularity" + NL
    + "  chain); it is the unique one-character change to the manuscript text. The optional rewordings of" + NL
    + "  findings 2–4 were applied to the *proposal prose only* (paragraph range, tr ad coefficient) and declined" + NL
    + "  for the *insert text* (finding 2 shorthand), keeping the integrate-diff exactly the required fix." + NL
    + "  Rejected alternatives: broader editorial rewrites (rule: smallest accurate text; the gatekeeper ruled" + NL
    + "  findings 2–4 not required).", 1)

# (l) round context line
rep("Intended integration ordinal: 63.",
    "Intended integration ordinal: 63. Round 2: revision of an ACCEPT-WITH-REQUIRED-REVISIONS round-1 verdict;" + NL
    + "the only manuscript-text change from r1 to r2 is the one-character sign fix recorded in the Revision note.", 1)

rev = (
    "## Revision note (round 2)" + NL + NL
    + "Gatekeeper verdict r1: ACCEPT WITH REQUIRED REVISIONS; milestone none; flags none. Findings addressed:" + NL + NL
    + "1. **(major, required; manuscript text)** Sign slip in insert paragraph 1 (i), the chain" + NL
    + r"   `\(\langle\mathcal I_n\rangle_n=-\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n=0\)`." + NL
    + "   From the identity displayed two sentences earlier," + NL
    + r"   `\(\partial_\varepsilon\ln Z_n=-\langle\mathcal I_n\rangle_n+\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n\)`," + NL
    + "   together with `\\varepsilon`-independence of `Z_n`, the relation is" + NL
    + r"   `\(\langle\mathcal I_n\rangle_n=+\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n\)`; both terms then vanish" + NL
    + "   under unimodularity, so no downstream conclusion was affected, but the printed general equality" + NL
    + "   contradicted the insert's own identity and the shipped Check-1 data (there `\\mathcal I\\equiv0` and" + NL
    + r"   `\(\partial_\varepsilon\ln Z=\langle\partial_\varepsilon\ln j_\varepsilon\rangle\)`). **Self-report:** the slip" + NL
    + '   came from compressing "the insertion equals the flow derivative of the action" while carrying the Jacobian' + NL
    + "   sign across; Check 1 of my own script had the correct sign and I failed to cross-check the prose against" + NL
    + "   it. Fixed in `insert-r2.tex` (diff vs r1: exactly one changed line, deletion of a single `-`); also fixed" + NL
    + "   in this document's R3 prose (2 occurrences of the chain corrected). `derive_ward_r1.py` needs no edit;" + NL
    + "   re-run confirms `derive_ward_r1.out` byte-identical." + NL
    + "2. **(minor; declined for the insert, per the no-required-change ruling)** \"the flat Lebesgue matrix measure" + NL
    + "   of Equation~\\eqref{eq:Smatrix}\": acceptable shorthand given ch03/appH usage; the optional rewording (\"of" + NL
    + "   the matrix path integral of\") was declined to keep the r1→r2 integrate-diff minimal and exactly the" + NL
    + "   required fix." + NL
    + "3. **(minor; proposal prose fixed)** \"Matrix gauge realisation paragraph (appH L462–471)\" corrected here to" + NL
    + "   L466–477, noting the quoted conclusion sits at L462 in the preceding paragraph; the insert's own" + NL
    + "   cross-references were already accurate (gatekeeper verified) and are unchanged." + NL
    + "4. **(minor; proposal prose fixed)** R3 stated" + NL
    + r"   `\(\operatorname{tr}\operatorname{ad}_\Lambda=4\operatorname{tr}\Lambda-4\operatorname{tr}\Lambda\)`" + NL
    + "   (the `N=4` coefficient) while the script checks the `2×2` (`N=2`) adjoint; corrected here to the general" + NL
    + r"   identity `\(\operatorname{tr}\operatorname{ad}_\Lambda=N\operatorname{tr}\Lambda-N\operatorname{tr}\Lambda=0`," + NL
    + "   valid for every `\\Lambda`. Manuscript text unaffected (it states only" + NL
    + r"   `\(\operatorname{tr}\operatorname{ad}_\Lambda=0\)`)." + NL + NL
    + "Re-certification: `simulate_apply_r2.py` asserts the same certified pre-states (appH 582,706 B / dd0bea77… /" + NL
    + "CRLF 3435 / bare LF 0; bib 28,038 B / c71780a9… / CRLF 931 / 88 entries) and reproduces insert-r2 = 6,667 B," + NL
    + "appH post = **589,388 B / CRLF 3450 / bare LF 0 / sha256 d94b79458c3e3613992ed66b8ac12024db84f6f44910ebc0d1e0081e14dafe3d**," + NL
    + "bib post unchanged (**31,789 B / 9e9dfa06… / CRLF 1050 / 99 entries**) — an exact match with the gatekeeper's" + NL
    + "independent computation, not taken from it." + NL + NL
)
i = s.index("## Result")
s = s[:i] + rev + s[i:]

io.open('proposal-r2.md', 'w', encoding='utf-8', newline='\n').write(s)
print("proposal-r2.md written, bytes:", len(s.encode('utf-8')))
