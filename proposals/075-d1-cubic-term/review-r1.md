VERDICT: NEEDS EVIDENCE | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 1/0

Gatekeeper r1 review, remote/claude, 2026-11-22. Saved by the orchestrator. The gatekeeper's check scripts are gk_chk_r1.py, gk_fd_r1.py and gk_rk_r1.py.

## Source reading
Digest + targeted reads:
- appH L715-804, L1513-1533, and the 068-073 closers;
- ch03 L125-194;
- ch10 L40-118;
- ch17 D;
- a grep of all chapters for C_munulambda / cubic, with each hit read in context.

## Verified
- s1-s6: byte-identical output.
- apply_and_build: pre 84f9c61e, post 8aed4519; anchor unique; 2 new bib keys; 424 pp, clean.
- Re-derived independently:
  - Variation coefficient 1/2, checked by finite difference on 5x5 matrices.
  - Reality: C_[] = i(real) eps v.
  - Covariance identity.
  - Lemma logic. The orbit differences span R^4, Hodge duality is injective, so [D,D]=0 and T=R=F=0. Correct.
  - Linearised corollary: equivariant fluctuations about flat are pure gauge.
  - H_v backgrounds, exact (r = 4/|v|).
  - Determinant identity det(M-qq) = (q^2)^2[...], exact. M has rank 3 at null q, so (q^2)^2 is not a root.
  - All branches.
- Citations:
  - CFJ1990: Crossref metadata matches.
  - AdamKlinkhamer2001: arXiv and section 2 read. Eq (2.1) and (2.3) match. DOI 10.1016/S0550-3213(01)00161-4 VERIFIED.
- No PRIOR-CLAIM-ERROR. Every first-order-class passage is scoped to C=0. L2651 is consistent. Problem F's cubic term on K meets H4 and is unaffected.
- Rulings:
  - H_v fibre: WITHIN CORE, not STRUCTURAL. It cannot contribute to D1 closure (the target is local SO(3,1)).
  - Emergence: preserved.
  - Classification: M2 bounded no-go under hypotheses H1-H5, tree level. Not a breakthrough. It redirects D1: in this class, the tree-level route needs C_[] = 0.

## Findings
1. BLOCKING, procedural: the M2 full scan (3(b)) is owed.
2. optional: after "with multiplicity seven," add "(for \(\mathsf v\neq0\) the factor \((q^2)^2\) is not a drop in rank of \(M\))".
3. optional: add the doi to AdamKlinkhamer2001; optionally also cite its Eq (2.3).
4. observation (no edit now): ch03 L161-164. After this result, gravity-bearing content in the first-order class with a c-number C exists only at C_[]=0. A later scoped pointer from ch03 is optional.

## Avenues, ranked
1. The C_[]=0 branch, with a torsion gap from loops or bilocal modes (upstream).
2. Relax H1: a covariant, section-valued C (v = u^-1 v-hat(y)). This keeps local SO(3,1) with spontaneous breaking to H_v, close to ch10 locking. STRUCTURAL if adopted as the reading of eq:Smatrix.
3. One loop at C != 0 about commuting matrices.
4. Non-equivariant fluctuations.
5. H_v classes beyond flat.

## Disposition
Full scan; then accept as written (the optional minors are the researcher's choice). No label change. D OPEN.
