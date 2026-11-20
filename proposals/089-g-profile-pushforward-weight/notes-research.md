# Research notes 089, round 1 - full derivations and change detail

Support file for proposal-r1.md; classification markers as in the proposal.

## Research and reasoning (full)

Established: E_i = |w_i|^2 are iid exponentials, rate 1/(s^2 g_i); E_i = T p_i has Jacobian T^(D-1);
integrating T against exp(-T Lambda), Lambda = sum p_i/(s^2 g_i), gives (D-1)!/Lambda^D; times the product of
rates 1/(s^(2D) G) this yields f = (D-1)!/(G(sum p_i/g_i)^D), a density in dp_1..dp_(D-1), exactly normalized
(s1). f is invariant under g -> c g (W fixes the scale), and log f = const - D log L recovers the linear form
L = sum p_i/g_i, so f determines g up to scale (s3 exact at D=2). L linear and f=c*L^(-D) decreasing in L; -log L convex, so f is log-convex, has an interior
stationary profile only when g is uniform, and its maximum is the vertex of the largest g_i (linear forms
extremize at vertices; s1). The dead-pass claim that sum E_i is independent of p is false for non-uniform g
and was removed. Frame (established): a normalized standard complex Gaussian vector has q = (|u_i|^2)
Dirichlet(1,..,1) (Gamma construction; MC s2) - flat, the fully degenerate symmetric case of the L3189
dichotomy (whole simplex minimising), flat on the unordered quotient; Var_q(g) of L3187 is a statistic of q,
not a further weight; the joint fibre integral factorizes. Conditional: for product slot laws s^2 g_i xi_i,
iid nondegenerate continuous xi - exchangeable at uniform input; identifiable via the pushforward ratio laws
p_i/p_j = (g_i/g_j)(xi_i/xi_j) (quantile argument, not proved); the closed form is exponential-specific (s3
shape shift 0.1998 -> 0.1839). Reading fact: g indexes the named slot measure, p carries it equivariantly
with O(1) Dirichlet noise, and the flat-profile mixture diverges at vertices (s2(g)) - no sharpening inside
the named class.

## Verification detail

python -I proposals/089-g-profile-pushforward-weight/<script> from the repo root; .out files are live rc-0
reruns (s1 and simulate regenerated after the corrections below; s2/s3 byte-identical). Invariants: s1
normalizations D=2,3,4 = 1, vertex argmax = argmax g, uniform constant (D-1)! = 2; s2 Dirichlet moments
2(D-1)!/(D+2)!, h(1/2) = 4/3, vertex divergence; s3 equivariance maxdiff 2e-4, shape shift; hygiene PASS,
bytes 3823, sha8 602e63d9, banned {}, nonascii []; simulate rc 0 (read-only): PRE 748814 / ecb67a25...6749 /
CRLF 3840 / bareLF 0; PIN 711637, gap CRLFCRLF; POST 752639 / sha256
2da0e0764e92970923bb0a3d54393454cb95387e90be1590f13770fd9be654bb / CRLF 3842 / bareLF 0; close-idiom
15->16; new-header 1; Vacuum-term 2; SIMULATION OK. hygiene_089.py rebuilds the tex from insert-body.txt. NOTE (round 2): the bytes above are the live r1 contract (insert-r1.tex); round 2 supersedes with insert-r2.tex 3975 / sha8 bba6adc4 and POST 752791 / e5355e61f99f9b1e5dee0f17c727c478cf22cd0d1fad28fcf175128bfe10f1c8 (simulate_apply_089_r2.out).

## Proposed changes (full anchor detail)

One new paragraph in chapters/appH-microscopic-proofs.tex, inserted at byte 711,637 after the unique closer
"...and they close nothing in Problem~G." (count 1) of the \emph{Variational rigidity...} paragraph, before
\emph{Vacuum term.} (gap exactly CRLFCRLF). Spliced block = insert-r1.tex (one content line + terminal CRLF)
plus one spacer CRLF; all bytes outside the window preserved (asserted in simulate_apply_089.py). Nothing
replaced; no labels, refs, citations or bib. Verified paragraph indices: 4th preceding L3183 (slot law), 3rd
L3185 (uniformity locus), 2nd L3187 (frame-weight variance), 1st L3189 (dichotomy), 6th L3179 (obstruction
factor).

## Decisions Taken (full)

(1) insert-r1.tex is authoritative; insert-body.txt its source (tex = body minus trailing LF plus terminal
CRLF; hygiene rebuilds it). (2) Three dead-pass insert statements corrected after re-derivation: dropped the
false independence of sum E_i from p (true only at equal g), T-integral derivation substituted; the
"face of equal 1/g" strictness clause replaced by constancy of sum p_i/g_i along the segment (D=3
counterexample: direction (1,1,-4.5) with sum d_i/g_i = 0); "only" coordinate weakened to "canonical".
(3) The s1 uniform line used factorial(3) = D! mislabeled as (D-1)! (true D=3 constant is 2); fixed, .out
regenerated; Result wording aligned (log-convex; maximum, not minimum, at the vertex). (4) The simulate
post-splice assertion rebuilt from the splice geometry: ins ends in CRLF, so after the block come exactly one
spacer CRLF then \emph{Vacuum term.; added outside-window suffix byte-identity. Rejected: shipping the
mislabeled check; softening rather than correcting the false independence clause.
