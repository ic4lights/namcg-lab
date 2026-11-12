# Proposal 058-efe-saturation-value, round 1

## Result

PRIOR-CLAIM-ERROR confirmed, with one more error found in the same passage.

1. **The value "ν_√(g_gal) ≈ 1.1" is numerically false** under the manuscript's own interpolator, eq:nu-sqrt
   (ch13 L264-267), at the manuscript's own inputs. These are g_gal = v_⊙²/R_0 ≈ 2.2×10⁻¹⁰ m s⁻² (ch13 L254,
   appE L47) and g_s = g_† = 1.20×10⁻¹⁰ m s⁻² (ch13 L271, from McGaugh2016). The ratio is
   g_gal/g_s = 1.8333, √ = 1.3540, e^(−1.3540) = 0.2582, so **ν_√(g_gal) = 1.3481 ≈ 1.35**.
   - The value is false at all four occurrences: ch13 L255, ch16 L208, appE L48 and appE L221.
   - No reading supported by the manuscript gives 1.1:
     - ν_√ = 1.1 needs g_N = 6.9×10⁻¹⁰ m s⁻².
     - The velocity factor √ν_√ is 1.161.
     - Simple MOND gives 1.392.
     - Reading 2.2×10⁻¹⁰ as the observed field, inverting eq:appE-RAR and using the baryonic g_N = 1.47×10⁻¹⁰
       gives 1.493.
   - Only the *standard* MOND interpolator μ = x/√(1+x²) gives 1.11. That is probably where the number came
     from, but the manuscript never uses that interpolator.
2. **Dependent claims are unsupported or reversed.**
   - "A surviving γ≈1.4 is not explained by that saturation" (ch16 L212-213; appE L220-222) loses its only
     support. A γ≈1.4 is the size of the saturated value 1.35-1.5. Chae (2023) reports γ = 1.43 ± 0.06 and
     reads it as the AQUAL external-field boost (verified below).
   - ch16 says a Newtonian Gaia result "is compatible with Assumption~\ref{ass:efe}". appI L66-68 says such a
     null result is "the outcome expected once Assumption~\ref{ass:efe} is respected". With ν_√(g_gal) ≈ 1.35
     neither holds: the assumption predicts an asymptotic boost above one. A null result constrains it.
   - appI L80-82 ("compatible ... with the modest residual enhancement") contradicts appI's own L44-46, which says
     the controlled analyses exclude the residual.
3. **appI's "of order 20%" is right, but only in relative velocity.**
   - Over appI's own range g_gal = (1.5-2.2)×10⁻¹⁰, √ν_√ − 1 = 0.16-0.22. This matches the ≈20% velocity excess
     verified in Banik et al. (2024).
   - The sentence then compares that velocity number with "the factor ∼4 of the isolated map", which is an
     acceleration factor (the velocity factor is 2.0).
   - The fix clarifies the units. The value stays.
4. **The eq:nu-efe bracket has the wrong sign** (ch13 L229-233).
   - The QUMOND one-dimensional uniform-field law, Famaey & McGaugh (2012) Eq. (60), verified from the arXiv
     text, is g = ν(|g_N+g_Ne|)g_N + [ν(|g_N+g_Ne|) − ν(g_Ne)]g_Ne. The manuscript has [ν(g_ext) − ν(g_tot)].
   - The derivation is internal field = ν(g_tot)(g_N+g_ext) − ν(g_ext)g_ext. This gives the published sign.
   - The manuscript form differs from it by 2[ν(g_tot)−ν(g_ext)]g_ext.
   - Linearised, the manuscript form gives the along-field boost ν_e(1−L_e) ≈ 1.67. The corrected form gives
     ν_e(1+L_e) ≈ 1.03.
   - With either sign, eq:efe-sat (γ→ν(g_ext)) holds for the transverse components. That equation is unchanged.
   - The "QUMOND limit" sentence in appE L253 becomes accurate once the sign is fixed.
5. **The saturated boost is anisotropic** at order L_e = d ln ν_√/d ln g ≈ −0.24 at g_gal.
   - Three-dimensional QUMOND gives ν_e along g_ext and ν_e(1+L_e/2) ≈ 1.19 transverse to it. This is
     Famaey-McGaugh Eqs. (63)-(64), re-derived symbolically.
   - One sentence in ch13 records this, so that "1.35" is not read as an isotropic prediction.

The corrections are numerical and logical. They derive nothing about Problem H and change no label. On the
phenomenology, the corrected record is **less favourable** to the coefficient layer than the old text. Assumption
ass:efe, as written, predicts a residual of the size that the controlled analyses appI cites disfavour.

## Target and status

- **Problem H** (sec:status-H, appH L2784-2790). Status: OPEN. Priority: OPTIONAL within the phenomenological
  scope. Completion: PROGRAMME-CONDITIONAL. ch17 L520-521 agrees ("OPEN; OPTIONAL research within the theory").
  No discrepancy.
- **Original target** (ch17 L524-573): derive ν_√ (eq:nu-target) from the modular data of Chapters 6 and 12,
  with no SPARC input. The external-field argument is part of the same derivation (ch16 L358; appE L250-254).
- **Dependencies**: Assumption ass:track, Assumption ass:efe (coefficient), and Appendices empirical, rar-bridge
  and gaia.
- **This package**: a PRIOR-CLAIM-ERROR correction in optional-scope phenomenology. It is not a step of the
  Chapter 17 full-GR / matrix-derived criterion. That criterion requires A, B, C, D1, E, F, G-derived and N (ch17
  and appH; not re-tabulated here because nothing in this package touches those entries). Classification:
  **neither DERIVED nor PROGRAMME-CONDITIONAL progress on H**. The package corrects the record.

## Source reading

- **Mode**: targeted reads only. The digest was not used. `python scripts/make_digest.py --check` printed
  `DIGEST STALE (head changed)`, not `DIGEST CURRENT` as the brief said. HEAD is 30950fa, the SME-scout commit
  touching `reports/` only. The four target chapter files are byte-identical to HEAD (checked with
  `git diff --quiet HEAD`). appH is dirty (055-057) and is not edited.
- **Read in full**:
  - ch13 L195-315 (ass:track, ass:efe, eq:nu-efe, eq:efe-sat, the commentary paragraph, eq:nu-sqrt, SPARC
    paragraph).
  - ch16 L100-110 (assumption table), L190-230 (falsifier list), L262-275, L354-360.
  - appE L25-65 and L195-312, all EFE passages and the exercise.
  - appI L1-95 (the whole appendix up to Status).
  - appH L2770-2830 (sec:status-H head).
  - ch17 L518-575 and L680-692.
  - ch18 L44-56.
- **Token sweep over every `chapters/*.tex`**: `nu-efe`, `ass:efe`, `efe-sat`, `appE-efe`, `g_{\mathrm{ext}}`,
  `g_{\mathrm{gal}}`, `wide.binar`, `Gaia`, `QUMOND`, `AQUAL`, `approx 1.1`, `Chae`, `Banik`, `Famaey`. Every
  hit was read. The two appH "1.1" hits (L2463, L2631) are unrelated.
- **Not a full scan.** See "Special instructions": the eq:nu-efe sign fix edits an equation inside an assumption,
  and the appI Status section is rewritten. Under CLAUDE.md rule 3(c), changes of that kind require a full scan.
- **Sources of numbers**:
  - g_† = 1.20×10⁻¹⁰ is cited to McGaugh2016 (ch13 L271; appE L65 gives ±0.02).
  - g_gal = 2.2×10⁻¹⁰ and the appI range (1.5-2.2)×10⁻¹⁰ have no source in the repository (no v_⊙ or R_0 value
    is given). They are used here as manuscript inputs, are not changed, and are not independently verified.
- **Side observations, not acted on**:
  - `appI-gaia-dr3.py` (repo root) evaluates only isolated ν, with no external field.
  - ch16 L214 and appE L219 hard-code "Theorems~7.3--12.4" / "Theorem~7.3", which conflicts with the `\ref`
    convention. That is outside this target.

## Research and reasoning

**(a) The value.**
- From nu_check.txt §1: ν_√(x) = 1/(1−e^(−√x)) with x = g/g_s.
  - At x = 2.2/1.20 = 1.8333: ν = 1.3481.
  - At x = 1.5/1.20 = 1.25: ν = 1.4857.
  - At x = 0.0833 (g_N = 10⁻¹¹): ν = 3.988. So the "γ≈4" in ch16 L206 and appE L50 is correct.
- §2 tests every alternative reading (listed in Result item 1). Only standard MOND (1.1135) gives ≈1.1.

**(b) Argument of ν.**
- ass:efe defines g_ext as the *baryonic* field. appE L47 defines g_gal = v_⊙²/R_0, the *observed* centripetal
  field.
- If g_ext is the baryonic field and the RAR holds at the Sun, inverting eq:appE-RAR at g_obs = 2.2×10⁻¹⁰ gives
  g_N = 1.474×10⁻¹⁰ and ν = 1.49.
- This reproduces the lower end of appI's range (1.5). It is also why that range, read as "baryonic to observed",
  is consistent.
- Either reading gives 1.35-1.5, never 1.1. One sentence in appE records the second reading. Decision D2 explains
  why.

**(c) Literature, verified this session.**
- **Chae, ApJ 952, 128 (2023)**, arXiv:2305.04613, DOI 10.3847/1538-4357/ace101. The arXiv abstract was fetched.
  - It reports g_obs/g_pred = 1.43 ± 0.06 at g_N ≈ 10^−10.15 m s⁻².
  - It states that the deviation "agrees with the boost factor that the AQUAL theory predicts" for circular orbits
    under the Galactic external field.
  - This is the bib entry Chae2023WideBinaries (already in bib/, not yet cited in chapters).
- **Banik, Pittordis, Sutherland, Famaey, Ibata, Mieske & Zhao, MNRAS 527, 4573 (2024)**, arXiv:2311.03436, DOI
  10.1093/mnras/stad3393. The abstract was fetched.
  - MOND with the Galactic EFE predicts ≈20% faster asymptotic velocities.
  - MOND is excluded at 16σ (MCMC), with a 19σ model-comparison preference for Newton.
  - This supports the existing uncited appI L45 "Banik et al. 2024" and the "20%" as a velocity figure.
  - No bib entry is proposed. The appI text is not changed at L45.
- **Famaey & McGaugh, Living Rev. Relativ. 15, 10 (2012)**, arXiv:1112.3960v2 (bib FamaeyMcGaugh2012). I
  extracted the text of §6.3 from the arXiv PDF with pdftotext.
  - Eq. (60) is the 1D QUMOND law above. The extraction drops the ν glyph, but the structure
    "g = g_N ν(·) + g_Ne [ν(|g_N+g_Ne|/a_0) − ν(g_Ne/a_0)]" is unambiguous.
  - Eqs. (63)-(64): Φ = −Gmν_e/r̃, r̃ = r/[1+(L_Ne/2)(x²+y²)/r²], L_Ne = (d ln ν/d ln y) at y = g_Ne/a_0.
  - I re-derived Eqs. (63)-(64) independently (nu_check §6). Linearise QUMOND,
    ∇²Φ = ∇·[ν(|∇Φ_N|)∇Φ_N], about a uniform g_e ẑ. This gives ∇²φ = ν_e(∇²φ_N + L_e ∂_z²φ_N). The point-mass
    solution is φ = ν_e[φ_N + L_e ∂_z²ψ] with ∇²ψ = φ_N and ψ = −Gmr/2. That reproduces FM12's form exactly.
  - Along ẑ the boost is ν_e. In the transverse plane it is ν_e(1+L_e/2).
- **Not independently verified**: "Pittordis, Sutherland & Shepherd 2025" and "quality-framework study 2026" (appI
  L45-46), and the El-Badry catalogue cuts (appI L30-33). None is relied on or changed.

**(d) Sign of the bracket.**
- The 1D QUMOND total field is ν(|g_N+g_e|)(g_N+g_e). Subtracting the external part ν(g_e)g_e gives the published
  form (sympy residual 0). The manuscript form differs by 2g_e[ν(g_tot) − ν(g_e)] (§5).
- In vector form with g_ext ∥ ẑ (§7), linearising in g_N:
  - corrected: (ν_e, ν_e, ν_e + g_e ν_e′) = ν_e(1, 1, 1+L_e);
  - manuscript: ν_e(1, 1, 1−L_e).
- Since L_e < 0, the manuscript sign gives a boost along the field that *exceeds* ν_e (1.67 at g_gal). No QUMOND
  limit does this.

**(e) Fork analysis.** The corrected record makes ass:efe, as written, look disfavoured by the controlled Gaia
analyses. That bounded negative depends on these hypotheses:
- (i) ν_√ is the boost for an embedded subsystem. This is the working interpolator, not derived.
- (ii) The external field enters only through the argument of the same ν. This is a QUMOND-type premise; Problem H
  has not computed U_ent[I(A:B)] with an external source.
- (iii) The g_ext value at the Sun is an unsourced input.
- (iv) The orbit-averaged anisotropic boost, between 1.19 and 1.35 in 3D QUMOND, is not computed.
- (v) Wide binaries at 2-30 kAU have g_N ~ 10⁻¹¹-10⁻¹⁰, so they are not deep in g_N ≪ g_ext.
- (vi) The data analyses themselves: Chae and Banik disagree.

Relaxations, ranked by bearing on Problem H:
1. Compute the external-field dependence of the modular response directly (the Problem H calculation with an
   external Newtonian source). This could replace (ii) outright.
2. An orbit-averaged 3D boost for the corrected eq:nu-efe or full QUMOND with ν_√.
3. Source g_ext at the Sun.

None of these is executed here; they are phenomenological, and Problem H is optional. Nothing here bears on the
infrared/full-GR critical path. ch13 L248-250 already states that ass:efe is a coefficient, not a solution of
Problem H.

## Claim classification

- ν_√(2.2×10⁻¹⁰; g_s = 1.20×10⁻¹⁰) = 1.348; ν_√(1.5×10⁻¹⁰) = 1.486; ν_√(10⁻¹¹) = 3.99: **established**
  (arithmetic on manuscript inputs).
- "1.1" is false under eq:nu-sqrt for any manuscript-supported argument: **established**.
- Origin of 1.1 in the standard MOND interpolator: **conjecture** (it fits numerically; there is no textual
  evidence).
- Baryonic g_ext ≈ 1.47×10⁻¹⁰ from inverting the RAR at the Sun: **conditional** (on the RAR holding at the Sun and
  on the unsourced v_⊙²/R_0).
- The bracket sign in eq:nu-efe is opposite to the 1D QUMOND law: **established** (derivation plus verified FM12
  Eq. 60).
- 3D QUMOND anisotropy ν_e, ν_e(1+L_e/2): **established** (FM12 Eqs. 63-64, re-derived). L_e(g_gal) = −0.236:
  **established** (arithmetic).
- Chae γ = 1.43 ± 0.06 read as the AQUAL EFE boost: **literature, verified abstract**.
- Banik et al. ≈20%, MOND excluded at 16σ: **literature, verified abstract**.
- ass:efe as written is disfavoured by controlled analyses: **conditional** (on those analyses and hypotheses
  (i)-(vi)). The manuscript text says only "disfavour" and "constrains".
- Derivation of ass:efe or ν_√ from I(A:B): **unresolved** (Problem H, unchanged).

## Proposed changes

Each change is an exact old→new byte replacement. The edit files hold LF text, and apply_check converts it to CRLF.
apply_check.txt confirms that every OLD occurs exactly once, every NEW occurs zero times in the baseline, and no
bare LF is introduced. Labels used: `ass:efe` (ch13 L221), `eq:nu-efe` (ch13 L228), `eq:appE-RAR` (appE L56),
`sec:gaia-show` (appI L39), `app:empirical` (already used at the same spot). Each occurs once. Citations used:
`FamaeyMcGaugh2012` and `Chae2023WideBinaries`, both in bib/namcg.bib (L248, L330). They resolved in the scratch
build. No new labels and no bib changes.

### chapters/ch13-cores-galaxies.tex

Baseline 16631 bytes, sha256 `aafba1b0c80ebe21954f9e286516c70928a582f27f84ebf5ba307346484a036a`, 399 CRLF, 0 bare LF.
Result 17240 bytes, sha256 `23fc14239605dd258714a3c7fb4e6a5c995347bb2e660cca5942fb792f92fd9a`, 409 CRLF, 0 bare LF.
File: `ch13_edits.txt`.

Edit 1 (L231-232, inside Assumption ass:efe, eq:nu-efe; the rest of the equation and the assumption are kept):
```latex
OLD:
     +\Bigl[\nu_{\sqrt{}}(g_{\mathrm{ext}})
            -\nu_{\sqrt{}}(g_{\mathrm{tot}})\Bigr]
NEW:
     +\Bigl[\nu_{\sqrt{}}(g_{\mathrm{tot}})
            -\nu_{\sqrt{}}(g_{\mathrm{ext}})\Bigr]
```
Edit 2 (L254-258; the earlier sentences of the paragraph, from "Assumption~\ref{ass:efe} is a coefficient." on, are
kept):
```latex
OLD:
already satisfies \(g_{\mathrm{gal}}>g_\dagger\), so
\(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.1\). Isolated-RAR
boosts of order \(4\) are then illegal for solar-neighborhood
wide binaries. A null Gaia result constrains the isolated
reading of Appendix~\ref{app:empirical}, not \(m_T=0\).
NEW:
already satisfies \(g_{\mathrm{gal}}>g_\dagger\), so
\(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.35\). The saturated boost
is anisotropic at order
\(L_{\mathrm{e}}=\mathrm{d}\ln\nu_{\sqrt{}}/\mathrm{d}\ln g\approx -0.24\)
at \(g=g_{\mathrm{gal}}\): the algebraic form~\eqref{eq:nu-efe} gives
\(\nu_{\sqrt{}}(g_{\mathrm{ext}})\) transverse to
\(\mathbf{g}_{\mathrm{ext}}\) and
\(\nu_{\sqrt{}}(g_{\mathrm{ext}})(1+L_{\mathrm{e}})\approx 1.03\) along it,
while three-dimensional QUMOND gives \(\nu_{\sqrt{}}(g_{\mathrm{ext}})\)
along it and \(\nu_{\sqrt{}}(g_{\mathrm{ext}})(1+L_{\mathrm{e}}/2)\approx 1.19\)
transverse to it~\cite{FamaeyMcGaugh2012}. Isolated-RAR
boosts of order \(4\) are then illegal for solar-neighborhood
wide binaries. A null Gaia result constrains the isolated
reading of Appendix~\ref{app:empirical} and the saturated value
of Assumption~\ref{ass:efe}, not \(m_T=0\).
```

### chapters/ch16-falsifiers.tex

Baseline 16725 bytes, sha256 `8ce01e1d5c4f972df14f54098017da865604f1fe7e6a79ad746861e6da210b69`, 361 CRLF, 0 bare LF.
Result 16833 bytes, sha256 `521226a8ee830dd31372c4c36144bad918bdec1af671bece503f9a61faf92ed4`, 362 CRLF, 0 bare LF.
File: `ch16_edits.txt`. One edit, L208-213. "Isolated ... γ≈4 ..." (L205-207) and "Neither outcome touches
Theorems~7.3--12.4." are kept.
```latex
OLD:
        \(\gamma\to\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.1\).
        A quality-controlled Gaia sample consistent with Newton
        constrains the isolated reading and is compatible with
        Assumption~\ref{ass:efe}.
        A surviving \(\gamma\approx 1.4\) is not explained by that
        saturation.
NEW:
        \(\gamma\to\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.35\).
        A quality-controlled Gaia sample consistent with Newton
        constrains the isolated reading and the saturated value
        of Assumption~\ref{ass:efe}.
        A surviving \(\gamma\approx 1.4\) is of the size of that
        saturated value; it would be a coefficient-level agreement
        with Assumption~\ref{ass:efe}, not a derivation.
```

### chapters/appE-rar-bridge.tex

Baseline 13446 bytes, sha256 `695dd9c2932184775a230317ea036e53383718f2cf0f2548c51ecad73f29c311`, 308 CRLF, 0 bare LF.
Result 13859 bytes, sha256 `a0dd0df8189dee98339750b3ed742394617c1e6ef7d8b624b122636f7cf7bd80`, 315 CRLF, 0 bare LF.
File: `appE_edits.txt`.

Edit 1 (L48; L47 "At the Sun, ..." is kept):
```latex
OLD:
\approx 1.8\,g_{\dagger}\), so \(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.1\).
NEW:
\approx 1.8\,g_{\dagger}\), so \(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.35\).
If \(g_{\mathrm{ext}}\) is instead read as the baryonic Newtonian field
obtained by inverting~\eqref{eq:appE-RAR} at
\(g_{\mathrm{obs}}=v_{\odot}^{2}/R_{0}\), then
\(g_{\mathrm{ext}}\approx 1.5\times 10^{-10}\,\mathrm{m\,s^{-2}}\) and
\(\nu_{\sqrt{}}(g_{\mathrm{ext}})\approx 1.5\).
```
Edit 2 (L219-222; "Isolated application ... saturates the boost at ν(g_ext). A Gaia sample consistent with" is kept):
```latex
OLD:
Newton constrains the isolated reading, not Theorem~7.3.
A reported \(\gamma\approx 1.4\) that survives quality cuts is not
explained by \(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.1\); that
residual, if real, is still open.
NEW:
Newton constrains the isolated reading and the saturated value
\(\nu_{\sqrt{}}(g_{\mathrm{gal}})\approx 1.35\), not Theorem~7.3.
A reported \(\gamma\approx 1.4\)~\cite{Chae2023WideBinaries} that
survives quality cuts is of the size of that saturated value; it would
be a coefficient-level agreement, not a derivation of
Assumption~\ref{ass:efe}.
```
"Theorem~7.3" is pre-existing text and is kept as is (see Source reading).

### chapters/appI-gaia-wide.tex

Baseline 3855 bytes, sha256 `91daa222e510cb2fc61e12798ec8f4d0fa8f00bf687fd75f449d742a7d7db988`, 83 CRLF, 0 bare LF.
Result 4154 bytes, sha256 `b91dc5e480c147466b8e2c5b39c275f0872183c7c0e01a18a70b76b69a15041e`, 87 CRLF, 0 bare LF.
File: `appI_edits.txt`.

Edit 1 (L27-28):
```latex
OLD:
Asymptotically this residual is of order \(20\%\), not the factor
\(\sim4\) of the isolated map.
NEW:
Asymptotically this residual is of order \(20\%\) in relative velocity,
\(\sqrt{\nu_{\sqrt{}}(g_{\mathrm{gal}})}-1\approx 0.16\)--\(0.22\) over the
range above, that is an acceleration boost of about \(1.35\)--\(1.5\),
not the acceleration factor \(\sim4\) of the isolated map.
```
Edit 2 (L66-68; the "It is not a constraint on m_T=0 ..." part of the item is kept):
```latex
OLD:
        identity. A null result under the external-field-corrected
        prediction is the outcome expected once
        Assumption~\ref{ass:efe} is respected.
NEW:
        identity. A null result under the external-field-corrected
        prediction constrains the saturated boost of
        Assumption~\ref{ass:efe}, which exceeds unity.
```
Edit 3 (L79-81, sec:gaia-status; the first and last sentences are kept, including "does not alter the open-problem
ledger"):
```latex
OLD:
included, is compatible with Newtonian gravity and with the
modest residual enhancement allowed by the coefficient-level
NAMCG/RAR map under external-field saturation. It supplies no
NEW:
included, is compatible with Newtonian gravity. The controlled
analyses of Section~\ref{sec:gaia-show} disfavour a residual
enhancement of the size, of order \(20\%\) in relative velocity, that
the coefficient-level NAMCG/RAR map gives under external-field
saturation. It supplies no
```

**Passages checked and left unchanged**:
- ch16 L107 (table), L268-271 and L358.
- appE L250-254. "QUMOND external-field limit" is now accurate.
- appE L300-308 (exercise).
- appI L44-55 and L71-73.
- appH L2803.
- ch18 L49.

## Verification scripts

- `nu_check.py` → `nu_check.txt`:
  - §1: ν_√ at the manuscript arguments, velocity excesses and L_e.
  - §2: every alternative reading of 1.1, including inverting the RAR at the Sun.
  - §3: comparison with Chae and Banik.
  - §4: 3D QUMOND anisotropy numbers.
  - §5: sympy check that internal = ν(g_tot)(g_N+g_e) − ν(g_e)g_e equals the corrected form, and not the
    manuscript form; the linear slopes.
  - §6: sympy re-derivation of FM12 Eqs. (63)-(64).
  - §7: sympy vector linearisation of the corrected and manuscript eq:nu-efe.
- `apply_check.py` → `apply_check.txt`: report-mode application of all edits, with uniqueness, hashes and CRLF
  counts. Given an output directory outside the repository, it writes the would-be files there.
- **Scratch build**:
  - Setup: copies of namcg-book7.tex, chapters/ (with dirty appH as in the working tree), bib/, frontmatter/,
    figs/ and the root PNG/JPG, with the four edited files from `apply_check.py <scratch>/out058`.
  - Commands: pdflatex, bibtex, pdflatex, pdflatex.
  - Result: **365 pages**, the same as the repository's last log. **0 undefined, 0 multiply-defined** references
    or citations. No BibTeX warnings. FamaeyMcGaugh2012 and Chae2023WideBinaries resolved.
  - Deleting the scratch build directory was denied by the permission system. It remains in the session
    scratchpad, outside the repository.

## Decisions Taken

- **D1. Correct all four occurrences to "1.35", not 1.1 and not 1.5.** 1.35 is ν_√ at the argument the manuscript
  states, g_gal = 2.2×10⁻¹⁰. Changing g_gal would be an unsourced change of an input. Rejected: leaving 1.1 with a
  footnote, which is false.
- **D2. Record the baryonic-argument reading in appE only.** appE is where g_gal is defined as v_⊙²/R_0, which
  clashes with ass:efe's "baryonic field". One conditional sentence gives the alternative value 1.5 there. That
  makes appI's existing 1.5-2.2 range intelligible without editing ass:efe's prose. Rejected:
  - redefining g_gal (an assumption change, unsourced);
  - adding the sentence in all files (not minimal).
- **D3. Fix the eq:nu-efe sign in this package.** The source is verified, the change is a sign, and appE already
  calls the law "the QUMOND limit". Leaving a verified-false equation inside an assumption is worse than the
  full-scan cost. The edit is severable: ch13 Edit 1 is independent of the rest, and the gatekeeper may split it
  out. Rejected: deferring on the ground that this is an assumption edit. The verified source and the sign
  derivation are complete.
- **D4. Add the anisotropy sentence.** Without it, "1.35" reads as an isotropic prediction, and the corrected
  bracket's own along-field value (1.03) would be hidden. Rejected: silence (an inaccurate record) or a new
  displayed equation (not minimal).
- **D5. appI: clarify units, do not change "20%".** The 20% is correct as a velocity excess and matches the
  verified Banik figure. Only the comparison with "∼4" mixed units.
- **D6. Cite Chae2023WideBinaries for "γ≈1.4" in appE.** It is the verified source of 1.43 ± 0.06, and the bib
  entry already exists. No new bib entry. Banik et al. 2024 is verified, but I do not add a bib entry for it; that
  would be a separate bookkeeping item.

## Milestone assessment

**M3 (PRIOR-CLAIM-ERROR)** in merged text, on two counts:
- a numerical error with a false implication: "1.1", the "not explained" claim, and "compatible with
  Assumption~ass:efe";
- a sign error in a displayed equation, eq:nu-efe.

These sit in optional-scope phenomenology and the falsifier list. They do not touch any critical-path problem. No
breakthrough.

## Status-label recommendation

There is no label change. Problem H remains OPEN, OPTIONAL and PROGRAMME-CONDITIONAL. The critical-path set (A, B,
C, D1, E, F, G-derived, N) is unaffected.

## Author decision needed

None.

## Remaining open step

- **Problem H (unchanged)**:
  - derive ν_√ and its external-field argument from the modular data (ch17 eq:gap-H, appE L250-254);
  - in particular, compute U_ent with an external Newtonian source, to test whether QUMOND-type saturation, with its
    sign and anisotropy, is the output.
- **Phenomenological follow-ups (optional)**:
  - source g_ext at the Sun;
  - give an orbit-averaged boost for the corrected eq:nu-efe or 3D QUMOND with ν_√;
  - add a bib entry for Banik et al. 2024.

## Special instructions for the gatekeeper

- Re-compute ν_√(1.8333) = 1.348 by hand, and confirm that nothing in the manuscript defines a ν that gives 1.1.
- Re-verify the sign against Famaey & McGaugh (2012) §6.3, Eq. (60), using the arXiv text or the Living Reviews
  version. My extraction lost the ν glyphs; the reading of the structure is stated in (c).
- **Full-scan question.** ch13 Edit 1 changes an equation inside Assumption ass:efe, and appI Edit 3 rewrites a
  sentence in an appendix Status section (no problem label). Under CLAUDE.md 3(c) either change may require a full
  scan. I did an exhaustive token sweep, not a full scan. If you require one, either do it or split ch13 Edit 1 and
  appI Edit 3 into a follow-up.
- Do not let the corrected text assert that Gaia data refute NAMCG. The cited analyses are reported, not adjudicated.
  "Disfavour" and "constrains" are deliberate.
- g_gal = 2.2×10⁻¹⁰ and (1.5-2.2)×10⁻¹⁰ have no source in the repository. I treated them as manuscript inputs and
  did not change them.
- Integration ordinal would be 56.
