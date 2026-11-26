# patch_r2.py -- build proposal-r2.md from proposal-r1.md with the round-2 fixes.
# Run: python -I -B patch_r2.py   (from the proposal folder)
import sys

buf = open("proposal-r1.md", "rb").read()
PAIRS = []

def rep(old, new, cnt=1):
    PAIRS.append((old.encode(), new.encode(), cnt))

# --- header ---
rep("# Proposal 116-d1-state-nondeg-realization, round 1",
    "# Proposal 116-d1-state-nondeg-realization, round 2")

# --- Finding 4: line-pointer fixes ---
rep("(live ch17 L59-62)", "(live ch17 L57-59)")
rep("(live L697-701)", "(live L698-701)")

# --- Finding 2: D3a d>v branch ---
rep("""satisfies `d <= d_eps` (on `d <= v`; `d > v` would give
`eps >= (lambda/4) v^2 (2v - v)^2` ... more directly, `sigma_4 = 0` is possible at
`d = v` and the root equation at `eps = lambda v^4/4` gives `d_eps = v` exactly; the
bound is only claimed for `eps <= lambda v^4/4`, where the pre-image `d <= v` is forced
by `V <= eps < inf{V : sigma_4 = 0}` once `eps < lambda v^4/4`, and at equality by
continuity).""",
    """satisfies `d <= d_eps`. The branch `d > v` is excluded (Finding 2): `r > v`
forces some `sigma_i > 2v` (since `sigma_i >= 0`), hence
`V >= (lambda/4)(sigma_i^2 - v^2)^2 > (lambda/4)(3 v^2)^2 = 9 lambda v^4/4 >
lambda v^4/4 >= eps`, a contradiction. The root equation at `eps = lambda v^4/4`
gives `d_eps = v` exactly.""")

# --- Finding 3: eta-quote fix ---
rep("""locked kinetic block - as that passage itself records ("the potential is indefinite"
there refers to that block, and "a quadratic diagnostic about a stationary background
and not a spectrum about a stable vacuum"). The insert says so in one clause.""",
    """locked kinetic block - as that passage records in the live wording (Finding 3):
"Because K is indefinite, this quadratic form is negative along the three 0i
self-adjoint directions for lambda > 0", and, verbatim there, "a quadratic diagnostic
about a stationary background and not a spectrum about a stable vacuum". The insert
says so in one clause.""")

# --- Finding 1 echo: Result item 3 (3-space list indent kept) ---
rep("""Hence every
   configuration of finite potential energy - in particular every classical solution of
   `eq:Phi-eom` with finite potential energy on a slice, and every finite Euclidean-form
   action history - realizes `V < lambda v^4/4` and pointwise frame non-degeneracy for
   `mu`-almost every point, with an explicit bound on the measure of the complement.""",
    """Consequently the sets
   `{V >= lambda v^4/4}` and `{det e = 0}` have `mu`-measure at most
   `4 E_V/(lambda v^4)`: every configuration of finite potential energy - in
   particular every classical solution of `eq:Phi-eom` with finite potential
   energy on a finite-measure slice, and every finite Euclidean-form action
   history - realizes `V < lambda v^4/4` and pointwise frame non-degeneracy off
   a set of at most that measure; null when `E_V = 0`, and NOT improvable to
   null for `E_V > 0` (the constant `sigma = (0,v,v,v)` field is an exact
   `eq:Phi-eom` solution - `D Phi = 0` and
   `Phi(Phi^dag Phi - v^2 I) = W diag(sigma_i(sigma_i^2 - v^2)) Z^dag = 0` since
   every `sigma_i` lies in `{0, v}` - with `V = lambda v^4/4` and `det e = 0`
   everywhere and finite energy on every finite-measure slice, attaining
   `mu{det e = 0} = 4 E_V/(lambda v^4)` with equality).""")

# --- Finding 1 echo: bottom line ---
rep("""delivered for the a.e. realization by finite-potential-energy configurations. No state of
the matrix theory is constructed and none is claimed: converting `ass:nondeg` into a
state hypothesis or an a.e.-non-degeneracy statement is NOT discharging it;""",
    """delivered as the sharp small-measure realization by finite-potential-energy
configurations (`mu{det e = 0} <= 4 E_V/(lambda v^4)`, null when `E_V = 0`, optimal in
`E_V` by the constant `(0,v,v,v)` `eq:Phi-eom` solution). No state of the matrix theory
is constructed and none is claimed: converting `ass:nondeg` into a state hypothesis or
a small-measure non-degeneracy statement is NOT discharging it;""")

# --- Finding 1 echo: DERIVED-vs-PC conversion statement ---
rep(""""sharp geometric domain + a.e. realization by all finite-potential-energy
  configurations, with a saturated volume bound", inside Presentation B.""",
    """"sharp geometric domain + small-measure realization by all
  finite-potential-energy configurations, with a saturated volume bound (the saturation
  configuration is itself an `eq:Phi-eom` solution, so no pointwise strengthening holds
  in this class)", inside Presentation B.""")

# --- Finding 1 echo: D5 claim + proof tail + unconditional paragraph ---
rep("""Hence `V < lambda v^4/4` and `det e != 0` hold for `mu`-a.e. `x`.
*Proof.*""",
    """The exceptional set (where the bound or the non-vanishing may fail) has
`mu`-measure at most `4 E_V/(lambda v^4)` (at most `E_V/eps` for the refined set);
it is null when `E_V = 0` and is NOT null in general when `E_V > 0` (see the
optimality paragraph below).
*Proof.*""")

rep("""What is *unconditional* is the a.e. statement for
every configuration with finite `int V dmu`: it is the measure-theoretic shadow of the
115 threshold and it is realization-grade for the state route inside Presentation B.""",
    """What is *unconditional* is the small-measure statement for
every configuration with finite `int V dmu` (a.e. only when `E_V = 0`): it is the
measure-theoretic shadow of the 115 threshold and it is realization-grade for the state
route inside Presentation B. *Optimality / honest limit (gatekeeper counterexample,
adopted, Finding 1):* the constant field `sigma = (0,v,v,v)` satisfies `eq:Phi-eom`
exactly (`D Phi = 0`, and `Phi(Phi^dag Phi - v^2 I) = W diag(sigma_i(sigma_i^2 - v^2))
Z^dag = 0` since every `sigma_i` lies in `{0, v}`), has `V = lambda v^4/4` and
`det e = 0` everywhere, and on a slice of measure `M` attains
`mu{det e = 0} = M = 4 E_V/(lambda v^4)`: the upper bound is optimal in `E_V` and no
a.e. statement can replace it when `E_V > 0`. This converts state construction into a
single consumable estimate: any candidate state/measure with `E_mu[V] <= f lambda
v^4/4` gives `mu{det e = 0} <= f`.""")

# --- Finding 1 echo: C7 row ---
rep("""| C7 | a.e. realization of `V < lambda v^4/4` and `det e != 0` by every finite-`int V dmu` configuration | conditional result (hypotheses: Presentation B, `eq:V`, `eq:vev-is-frame` reading, finite potential energy; a.e., not pointwise) |""",
    """| C7 | small-measure realization of `V < lambda v^4/4` and `det e != 0` by every finite-`int V dmu` configuration: exceptional set at most `4 E_V/(lambda v^4)`, null when `E_V = 0`, optimal by the constant `(0,v,v,v)` `eq:Phi-eom` solution | established measure bound + conditional application (hypotheses: Presentation B, `eq:V`, `eq:vev-is-frame` reading, finite potential energy; small-measure, not pointwise) |""")

# --- Finding 1 echo: comparison-with-target paragraph ---
rep("""(iii) a.e. realization
by every finite-potential-energy configuration with a saturated volume bound. It does""",
    """(iii) small-measure realization
by every finite-potential-energy configuration (`mu{det e = 0} <= 4 E_V/(lambda v^4)`,
null when `E_V = 0`, optimal by the constant `(0,v,v,v)` solution) with a saturated
volume bound. It does""")

rep("""discharge `ass:nondeg` (a.e. or otherwise): the target remains OPEN.""",
    """discharge `ass:nondeg` (small-measure or otherwise): the target remains OPEN.""")

# --- Finding 1 echo: stale-passages note ---
rep("""which remains true beyond the a.e. finite-energy statement established here; the new""",
    """which remains true beyond the small-measure finite-energy statement established
here; the new""")

# --- Finding 1 echo: milestone note ---
rep("""positive complement (a.e. realization by every finite-potential-energy configuration;
sharp radius `delta_*`), with the remainder of the caveat explicitly intact.""",
    """positive complement (small-measure realization - `mu{det e = 0} <=
4 E_V/(lambda v^4)`, null when `E_V = 0` - by every finite-potential-energy
configuration, and pointwise realization inside the sharp radius `delta_*`), with the
remainder of the caveat explicitly intact.""")

# --- Finding 1 echo: remaining open step ---
rep("""(this package gives the a.e. statement conditional on finite
potential energy of a configuration, and the weighted path-integral form conditional
on the measure's existence - neither is the construction)""",
    """(this package gives the small-measure bound conditional on
finite potential energy of a configuration - `mu{det e = 0} <= 4 E_V/(lambda v^4)`, so
that construction of the state reduces to the single estimate `E_mu[V] <= f lambda
v^4/4 => mu{det e = 0} <= f` (gatekeeper ranking, review-r1 Scope) - and the weighted
path-integral form conditional on the measure's existence; neither is the construction)""")

rep("""resolved (sharp-radius domain `r < delta_*`
pointwise; all finite-`int V dmu` configurations a.e.).""",
    """resolved (sharp-radius domain `r < delta_*`
pointwise; all finite-`int V dmu` configurations off a set of measure at most
`4 E_V/(lambda v^4)`, null when `E_V = 0`).""")

# --- Finding 1 echo: gatekeeper instructions ---
rep("""(a.e. is not pointwise; the scope sentence says all of""",
    """(a small-measure exception is not pointwise; the scope sentence says all of""")

rep("""that the finite-energy a.e. result
  holds for the physical state (the state is not constructed); that `delta_*` is a gap""",
    """that the finite-energy small-measure result
  holds pointwise or for the physical state (the state is not constructed; the constant
  `(0,v,v,v)` `eq:Phi-eom` solution shows the exceptional set need not be null for
  `E_V > 0`); that `delta_*` is a gap""")

rep("""(1) beyond the a.e. named class""", """(1) beyond the small-measure named class""")

# --- pins ---
rep("""`daa9d33f29414c0aa856af37314fe8981f2d8bc7`,
3473 bytes""", """`d99b67be680f3b727ab16367ea283680cd2d6269`,
3782 bytes""")
rep("bytes 3473 CR 1 LF 1 CRLF 1", "bytes 3782 CR 1 LF 1 CRLF 1", 2)
rep("the gen output): 3473 bytes, single CRLF line",
    "the gen output): 3782 bytes, single CRLF line")
rep("""`gen_payload_116.py` | `b74dbb1d6893d6dc17a9930948cf2df509229bf3` | 5395 |""",
    """`gen_payload_116.py` | `54b64f4c7d7b25438c35a0d31440e229a605fa5a` | 6101 |""")
rep("""`cert-r116p.py` | `831a789e1ab5b0747e1247e229895f9af39d6e21` | 3320 |""",
    """`cert-r116p.py` | `ea4eef9764ae62c5eee22a11eae9423cbae97cf7` | 3484 |""")
rep("""; asserts anchor uniqueness)""",
    """; asserts anchor uniqueness; Finding 5 makes both reference counters hard assertions before `CERT PASS`)""")
rep("""`out-cert-r116p.txt` (sha1 `d3328d624898bff4bf734831b8d8b5b1372247e5`,
158 B)""",
    """`out-cert-r116p.txt` (sha1 `bb6d6c7fbeaf80e4db145716e00ab15ecbeb7850`,
158 B)""")

# --- label renames found by the post-patch grep audit ---
rep("### D5. Volume/a.e. realization (edge 1(b), positive)",
    "### D5. Volume/small-measure realization (edge 1(b), positive)")
rep("a.e./volume realization).** Chosen because both rest on one derivation",
    "small-measure/volume realization).** Chosen because both rest on one derivation")

# --- payload line swap (r1 quoted block -> r2 payload) ---
old_pay = open("_old_payload_line.txt", "rb").read()
new_pay = open("insert-d1-state-nondeg.tex", "rb").read().rstrip(b"\r\n")
PAIRS.append((old_pay, new_pay, 1))

# --- round-2 response section (appended) ---
RESP = b"""

## Response to review-r1 (round 2)

Verdict addressed: ACCEPT WITH REQUIRED REVISIONS. The geometric core (Procrustes
identity, sharp two-sided estimate, `delta_*`, Markov bound + saturation) is unchanged.

- **Finding 1 (blocking) - addressed.** The false quantifier clause is gone from every
  artefact. The payload was regenerated through `gen_payload_116.py` with the
  gatekeeper's Corrected snippet applied VERBATIM (substring-identity check against
  `review-r1.md`: corrected clause and scope clause each present byte-for-byte; the
  strings "almost every point" and `\\mu`-almost-every quantifier absent from the new
  payload bytes; `\\checkmark` recorded in `r2-report.md`). The scope clause is the
  gatekeeper's ("the small-measure exception obtained when \\(E_{\\mathcal V}>0\\) is a
  fortiori not the pointwise statement..."). All proposal-side echoes (Result item 3,
  bottom line, conversion statement, D5 claim/proof/unconditional paragraph, C7,
  comparison paragraph, stale-passages note, milestone note, remaining-open step,
  gatekeeper instructions) now state the measure-upper-bound with `null when
  \\(E_{\\mathcal V}=0\\)` and non-improvability. The gatekeeper's counterexample - the
  constant `sigma = (0,v,v,v)` field as an exact `eq:Phi-eom` solution with
  `det e = 0` everywhere, finite energy on finite-measure slices, attaining
  `mu{det e = 0} = 4 E_V/(lambda v^4)` with equality - is adopted into the
  honest-limitations record (D5 optimality paragraph, Result item 3) and into the
  ranked-avenue statement (construction reduced to `E_mu[V] <= f lambda v^4/4`).
- **Minor 2 - addressed.** D3a now carries the two-line `d > v` exclusion (`r > v`
  forces some `sigma_i > 2v`, hence `V >= 9 lambda v^4/4 > lambda v^4/4 >= eps`).
- **Minor 3 - addressed.** The non-verbatim quote is replaced by the live appH wording
  ("Because K is indefinite, this quadratic form is negative along the three 0i
  self-adjoint directions for lambda > 0"); the one clause that IS verbatim there is
  kept quoted.
- **Minor 4 - addressed.** Line pointers corrected: ch17 DERIVED criterion at live
  L57-59; appH note at live L698-701.
- **Minor 5 - addressed.** `cert-r116p.py` now hard-asserts `undefrefs_pass2 == 0` and
  zero package-label undefined refs BEFORE writing `CERT PASS`; the certificate was
  re-run fresh (two passes) and `out-cert-r116p.txt` re-recorded.
- **Finding 6 - addressed.** The payload now reads "attained as an identity on any
  region where the singular values are \\((0,v,v,v)\\)" (part of the verbatim corrected
  block).
- **verify pack:** `verify_r116.py` unchanged (grep: no check text echoed the false
  quantifier); fresh rerun prints `PASS 29 FAIL 0` / `ALL CHECKS DONE 116`.

## Decisions Taken (round 2)

- Adopted the gatekeeper's corrected quantifier and counterexample verbatim rather
  than re-deriving an independent wording (maximizes verifiability; the mathematics
  was re-checked by hand: `W diag(sigma_i(sigma_i^2 - v^2)) Z^dag = 0` for
  `sigma_i in {0, v}` and `D Phi = 0` for a constant field, so the counterexample is
  an exact solution, and equality in the Markov chain holds on the `(0,v,v,v)` region).
  This strengthens rather than weakens the package: the bound is now recorded as
  optimal, and state construction is reduced to one consumable estimate
  (`E_mu[V] <= f lambda v^4/4 => mu{det e = 0} <= f`), which is the derivation-first
  ranking for the next package.
- Kept `verify_r116.py` at round 1 (procedure condition: rerun unchanged unless a
  check echoed the false quantifier; it did not - grep evidence in `r2-report.md`),
  preserving the accepted `PASS 29 FAIL 0` record.
- Recorded the round-1 payload `daa9d33f29414c0aa856af37314fe8981f2d8bc7` (3473 B) as
  SUPERSEDED by `d99b67be680f3b727ab16367ea283680cd2d6269` (3782 B); the canonical POST
  size must be recomputed by the integrator from the NEW payload (arithmetic pointer
  only: 830881 + 3782 = 834663 if the tree is unchanged; not pinned).
- Rejected alternatives: (a) keeping "a.e." with a caveat - rejected, the quantifier
  itself is the error; (b) weakening to `E_V = 0`-only statements - rejected, the
  Markov bound for `E_V > 0` is exactly the positive realization-grade input the state
  route consumes; (c) hand-editing the payload - forbidden by byte discipline, the
  generator is the single source.
"""
PAIRS.append((b"", RESP, None))  # sentinel handled below

for old, new, cnt in PAIRS[:-1]:
    c = buf.count(old)
    if c != cnt:
        print("MISMATCH count=%d expected=%d: %r" % (c, cnt, old[:90]))
        sys.exit(1)
    buf = buf.replace(old, new)

assert buf.count(old_pay) == 0
buf = buf + RESP
open("proposal-r2.md", "wb").write(buf)
print("proposal-r2.md written, %d bytes" % len(buf))
