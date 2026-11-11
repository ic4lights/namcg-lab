Capture: https://ar5iv.labs.arxiv.org/html/1610.08019 fetched 2026-11-10
(WebFetch, ar5iv HTML rendering of arXiv:1610.08019). Abstract-page
record already captured separately in arxiv_1610.08019.md.

Equations quoted by the fetch (verbatim where returned):

(1) ECG cubic density, the paper's Eq. (1):
"P = 12R_a^b_c^d R_c^d_e^f R_e^f_a^b + R_ab^cd R_cd^ef R_ef^ab
   - 12R_abcd R^ac R^bd + 8R_a^b R_b^c R_c^a"
Coefficients: 12, 1, -12, +8. This is coefficient-wise and slot-wise
identical to the NAMCG eq:ECG invariant of ch09 L213-217 (with the
mixed-slot placement R_a^b_c^d as printed there as
R_a{}^c{}_b{}^d, up to the renaming of dummy slots), so the NAMCG
invariant matches the published ECG density as written.

(2) Action normalization, the paper's Eq. (2):
"S = (1/16 pi G) Int d^4x sqrt|g| [ -2 Lambda_0 + R - G^2 lambda P ]"
Cubic coupling: dimensionless lambda (assumed positive in the paper),
entering as G^2*lambda*P with a MINUS sign.

(3) Effective cosmological constant / embedding equation, the paper's
Eq. (48):
"(16/9) lambda G^2 Lambda_eff^3 - Lambda_eff + Lambda_0 = 0"
described as "the embedding equation that pure (A)dS_4 with curvature
Lambda = Lambda_eff/3 must satisfy in order to be a solution of the
ECG theory". No separate value of P on maximally symmetric backgrounds
is given in the fetched text; the paper refers to arXiv:1607.06463
for that computation.

(4) Effective Newton constant, the paper's Eq. (49):
"G_eff = G / (1 - (16/3) lambda G^2 Lambda_eff^2)"

Researcher cross-check (CAS, stage3 T5d3): with the NAMCG conventions
(signature (-,+,+,+), R > 0 on spheres) and the ansatz
ds^2 = -N^2 dt^2 + dr^2/f + r^2 dOmega^2, the constant-curvature
((A)dS) static gauge is N = sqrt(1-kr^2), f = 1-kr^2, on which
R = 12k and the eq:ECG invariant evaluates to 192 k^3. With the
lambda normalization of Eq. (2), kappa_book = -lambda G^2, the cubic
part of the maximally-symmetric embedding relation then carries the
coefficient 192/4 = 48 lambda G^2 k^3, and (16/9) lambda G^2
Lambda_eff^3 = 48 lambda G^2 k^3 for Lambda_eff = 3k, so the CAS
value 192 k^3 is consistent with the published embedding equation
(48) up to the EOM-contraction factor; the equality of the
contraction factor 4 was NOT derived here, it is inferred by matching
the literature's own algebraic equation. The recorded appH MS values
(6k GR slice and 48 kappa k^3, first integral of the recorded lapse
identity on the N = 1 slice) correspond instead to the N = 1 slice,
on which the CAS gives R = 6k and invariant 216 k^3 (stage3 T5d1,
T5d2), and the recorded first integral gives the MS relation
k - 8 alpha k^3 = Lambda_eff/3, whose cubic coefficient (8) differs
by a factor 2 from the published lambda-relation k - 16 lambda G^2
k^3 = Lambda_0/3 obtained from Eq. (48) with alpha = lambda G^2.
Class: the two CAS slice values are established derivations; the
factor-4 EOM contraction and the identification kappa_book =
-lambda G^2 are conditional bookkeeping inferences, not derived here.
