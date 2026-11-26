# simulate_apply_102.py -- proposal 102 r1: simulation of the integration splice.
# Applies insert-r2.tex to an IN-MEMORY copy of chapters/appH-microscopic-proofs.tex at the
# G-block cut immediately AFTER the eigenvalue-reduction paragraph and BEFORE the transport
# paragraph, and writes the simulated POST ONLY to scratch/102_sim_post.tex (git-ignored).
# Never writes under chapters/. Run from repo root:
#   python -I proposals/102-g-profile-selection-output/simulate_apply_102.py
# Regional idiom (verified on live bytes, 2026-11-20): paragraphs in this block are
# separated by exactly ONE blank CRLF line; insert-r2.tex is one CRLF-terminated line, so
# the payload is the insert line (3173 B, CRLF-terminated) plus one blank-CRLF separator.
# r2: retargeted to insert-r2.tex per review-r1 Finding 1/Corrected snippet (orchestrator
# byte surgery after agent death #38/#39; verbatim clause governs). review-r1 expected 13
# added bytes / 3168 B; the clause pair differs by 18 ASCII bytes -> 3173 B (measured; the
# dead agent's fix note in _mk_r2_102.py, adopted). POST is computed and printed, not asserted.
# PIN (complete full line immediately preceding the cut, plus its CRLF and the blank-CRLF
# separator line; asserted to occur exactly once in the appH bytes):
PIN = b'\\emph{Eigenvalue reduction of the edge Gram and the Jacobian origin of the beta factor.} Let \\(\\Pi\\) be a momentum matrix of the gaussian state class of the Row length paragraph, in the subclass of constant variance on the block entries, and let \\(A=\\Theta\\Pi\\bar\\Theta\\) be the \\(M\\times(N-M)\\) edge block of the Edge datum paragraph. Then the entries of \\(A\\) are independent identically distributed complex gaussians, and the Gram matrix \\(G=AA^{\\dagger}\\), whose nonzero spectrum has size \\(D=\\min(M,N-M)\\), carries under the change of variables to its ordered eigenvalues \\(\\lambda_{1}>\\dots>\\lambda_{D}>0\\) and fibre the Jacobian \\(\\prod_{i<j}(\\lambda_{i}-\\lambda_{j})^{2}\\): the squared Vandermonde factor of the fixed-trace beta deformation of the preceding paragraph is, on this coordinate, a change-of-variables Jacobian, and its exponent two is fixed by the complex Hermitian structure of the core matrices rather than posed. At \\(D=2\\) the chart computation is exact, the eigenvalue-eigenvector Jacobian of a Hermitian \\(2\\times2\\) matrix being \\(\\det J=\\tfrac{1}{2}(y_{1}-y_{2})^{2}\\lvert\\sin 2\\theta\\rvert\\); at \\(D=3\\) the coincidence slopes of \\(\\det J\\) are \\(2\\) per pair and \\(6\\) at triple collision, to within \\(0.01\\) numerically. Conditioning on the block trace \\(\\tau=\\operatorname{Tr}G=\\lVert A\\rVert_{F}^{2}\\) is a fixed-invariant fibre: the scale separation of the preceding paragraph holds with the exponents \\(a=\\lvert N-2M\\rvert+1\\) and \\(\\beta=2\\) computed rather than posed, and the normalised eigenvalue profile \\(p_{i}=\\lambda_{i}/\\tau\\) carries exactly the \\(a=\\lvert N-2M\\rvert+1\\), \\(\\beta=2\\) member of the family of the preceding paragraph, free of the block variance as there. Two exact pair statistics at \\(D=2\\) quantify the repulsion: with \\(u=\\lvert p_{1}-p_{2}\\rvert\\) the separation density is \\(f(u)\\propto u^{2}(1-u^{2})^{a-1}\\), the variance is \\(\\operatorname{Var}(p_{1})=3/(8a+12)\\) against \\(1/(4(2a+1))\\) at \\(\\beta=0\\) for the same \\(a\\), and at \\(a=1\\) the coincidence probability is \\(\\mathbb{P}(u<\\varepsilon)=\\varepsilon^{3}\\) against \\(\\varepsilon\\) for the flat member (exact identities). The exponent two is kinematic: it belongs to the change of variables, not to the gaussian weight, so a non-constant variance profile on the block entries deforms the prefactor of the eigenvalue density and leaves the repulsion exponent two, confirmed numerically by Monte Carlo under heterogeneous column variances; the closed family form is stated in the constant-variance subclass, where the block law is exactly the gaussian one. Two boundaries are recorded. In the rank-one edge-datum class of the Row length paragraph at constant variance on the contracted entries the slot vector is a gaussian column contraction with independent identically distributed complex entries, and its normalised squared entries are exactly flat on the simplex at \\(D=2\\), with the flat Dirichlet moments confirmed numerically at \\(D=3\\): the slot-power profile of the moment map therefore carries no repulsion in that class, and the repulsive weight lives on the Gram-spectrum coordinate \\(p_{i}=\\lambda_{i}/\\operatorname{Tr}G\\), whose identification with the profile coordinate of the moment map is not supplied by the repository. And every member obtained here is relabelling-invariant, so the orbit-rigidity alternative of the preceding paragraph applies verbatim to the computed member: whole orbits, never single profiles. These statements are change-of-variables and exact-statistics statements for the named constant-variance edge-block subclass and the constant-profile rank-one slot subclass of the gaussian state model; the matrix integral of the core action is not evaluated, no state is fixed, the missing steps of the Missing step paragraph are unchanged, and they close nothing in Problem~G.\r\n\r\n'
import hashlib
import os
import sys

APP = os.path.join("chapters", "appH-microscopic-proofs.tex")
FOLDER = os.path.join("proposals", "102-g-profile-selection-output")
INSERT = os.path.join(FOLDER, "insert-r2.tex")

def sha16(data):
    return hashlib.sha256(data).hexdigest()[:16]

pre = open(APP, "rb").read()

def report(name, value):
    print(name, "=", value)

report("PRE bytes", len(pre))
report("PRE sha256-16", sha16(pre))
report("PRE CRLF", pre.count(b"\r\n"))
report("PRE bareLF", pre.count(b"\n") - pre.count(b"\r\n"))
report("PRE BOM present", pre[:3] == b"\xef\xbb\xbf")

ok = (
    len(pre) == 798457
    and sha16(pre).startswith("cfb6af516017367f")
    and pre.count(b"\r\n") == 3866
    and pre.count(b"\n") - pre.count(b"\r\n") == 0
    and pre[:3] != b"\xef\xbb\xbf"
)
if not ok:
    print("PRE MISMATCH")
    sys.exit(1)

print("PIN (complete full preceding line + CRLF + one blank-CRLF separator):")
print(PIN.decode("ascii"))
pin_count = pre.count(PIN)
report("PIN count in appH bytes", pin_count)
if pin_count != 1:
    print("PRE MISMATCH (PIN not unique)")
    sys.exit(1)

cut = pre.find(PIN) + len(PIN)
head = pre[cut:cut + 47]
report("bytes at cut (expected transport paragraph head)", head)
if not head.startswith(b"\\emph{Transport of the profile coordinate"):
    print("PRE MISMATCH (wrong paragraph at cut)")
    sys.exit(1)

ins = open(INSERT, "rb").read()
report("insert-r2.tex bytes", len(ins))
report("insert-r2.tex sha8", hashlib.sha256(ins).hexdigest()[:8])
if len(ins) != 3173 or hashlib.sha256(ins).hexdigest()[:8] != "86d4b849":
    print("PRE MISMATCH (insert payload)")
    sys.exit(1)

payload = ins + b"\r\n"  # insert line (CRLF-terminated) + one blank-CRLF separator
report("payload bytes (insert + blank-CRLF separator)", len(payload))
post = pre[:cut] + payload + pre[cut:]
report("POST bytes", len(post))
report("POST sha256-16", sha16(post))
report("POST CRLF", post.count(b"\r\n"))
report("POST bareLF", post.count(b"\n") - post.count(b"\r\n"))
report("POST == PRE + payload bytes", len(post) == len(pre) + len(payload))
report("POST CRLF == PRE CRLF + 2", post.count(b"\r\n") == pre.count(b"\r\n") + 2)
report("PIN still count 1 in POST", post.count(PIN))

os.makedirs("scratch", exist_ok=True)
out = os.path.join("scratch", "102_sim_post.tex")
with open(out, "wb") as f:
    f.write(post)
report("simulated POST written to", out)

if (
    len(post) == len(pre) + len(payload)
    and post.count(b"\n") - post.count(b"\r\n") == 0
    and post.count(PIN) == 1
):
    print("SIMULATION PASS")
    sys.exit(0)
print("SIMULATION FAIL")
sys.exit(1)
