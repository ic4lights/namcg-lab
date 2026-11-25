# gen_payload_120.py -- generator for insert-commutator-lift-r1.tex (chain 120, round 1).
# Deterministic: embeds the payload, asserts hygiene with INJECTED positive controls for
# every guard (join guard and each hygiene assert must FIRE on an injected violation and
# pass on the real payload, per the chain-117/118 generator-self-test lesson), verifies
# live-file pins, prints POST. Run twice: output file must be byte-identical.
# NOTE: this file is written escape-free (no backslash-x literals) because shell-heredoc
# editing of it lost a backslash level once; edit with the Write tool only.
import hashlib
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LIVE = os.path.join(REPO, "chapters", "appH-microscopic-proofs.tex")
OUT = os.path.join(HERE, "insert-commutator-lift-r1.tex")
ANCHOR = "\\section{Problem E: signature}"
BASE_SIZE = 848842
BASE_SHA1_12 = "9e0b198af2c3"
ANCHOR_OFFSET = 295299
CRLF = chr(13) + chr(10)
NONASCII = "caf" + chr(233)          # injection sample: non-ASCII byte
BOMSTR = bytes([0xEF, 0xBB, 0xBF]).decode("utf-8")  # injection sample: BOM

# ---- payload (single additive paragraph; one sentence-group per line) ----
SENT = [
r"\emph{A commutator-type lift: the dictionary bridge as an exact identity.} Take constant real \(\Theta^{\mu\nu}\), Hermitian matrix symbols \(A_\mu\), and the embedding ansatz \(\hat X^\mu=x^\mu\mathbb I+\Theta^{\mu\rho}A_\rho(x)\) as an input on the matrix coordinates (a Poisson-dressing identification, not a consequence of Equation~\eqref{eq:Smatrix}), and read the connection on \(\Phi\) in the adjoint (commutator) sense rather than the left action of Equation~\eqref{eq:Dmu-Phi}: for every matrix-valued Weyl symbol \(\Phi\) the Weyl calculus then gives \([\hat X^\mu,\Phi]_\star=\mathrm i\Theta^{\mu\nu}(\partial_\nu\Phi-\mathrm i[A_\nu,\Phi]_\star)\) exactly to all orders, so Equation~\eqref{eq:dictionary} of Assumption~\ref{ass:dictionary} is, conditional on these inputs, an identity at dictionary order with quantified even star-corrections \(O(\Theta^2)\) and beyond.",
r"The printed left action is exactly incompatible with this class: for \(D_\mu\Phi=\partial_\mu\Phi-\mathrm iA_\mu\Phi\) the \(A\)-linear mismatch of the identity is \(-\Theta^{\mu\nu}\Phi A_\nu\), a right-action product no commutator produces, and the central \(u(1)\) part of \(A\) is invisible to commutators, so no commutator-type lift reproduces Equation~\eqref{eq:Smicro} with the connection as printed; the adjoint reading is a representation choice recorded as datum, with quartic gauge coupling of \(\operatorname{Tr}([A_\mu,\Phi][A_\nu,\Phi]^\dagger)\)-type.",
r"The quadratic content of the class is bound to \(K\)-type: the shift-symmetric lift \(-(\kappa/2)\int\mathrm d^4x\,g^{\mu\nu}\operatorname{Tr}([\hat X_\mu,\Phi]_\star[\hat X_\nu,\Phi]_\star)\), with normalization \(\kappa\) a datum (of order \(\Theta^{-2}\) against Equation~\eqref{eq:Smicro}), has kinetic tensor proportional to \(K^{\mu\nu}\) of Definition~\ref{def:matrix-coords-ext}, hence never \(g\)-type for real nonzero Lorentzian data, since \(K=c\,g\) admits no real solution with \(\Theta\neq0\), the non-proportionality recorded for \(G=K^{-1}\) under Assumption~\ref{ass:emergent-op}; for purely spatial \(\Theta\) the tensor \(K\) is degenerate, so \(\Phi\) carries no time-derivative term.",
r"The class is exactly blind to the frame mode: writing \(\Phi=\phi_0\mathbb I+\tilde\Phi\), star-commutators with \(\phi_0\mathbb I\) collapse to \(\mathrm i\Theta^{\mu\nu}\partial_\mu\phi_0\)-type terms, so every appearance of \(\phi_0\) in a commutator word carries a derivative: no quadratic term and no \(X\)-dependent potential exists at any order, in particular neither the mass nor the locking direction of Equation~\eqref{eq:V} lies in the class, the frame couples only derivatively through \(K\), and the gauge-quartic coupling vanishes at \(\Phi=v\,\mathbb I\), so no gauge-boson mass arises from the condensate.",
r"The shift statement of the preceding paragraph is sharp at the level of \(X=\Phi^\dagger\Phi\): no quadratic shift-invariant term exists, and at quartic order the \(X\)-free shift-invariant sector is one-dimensional, spanned by \(W_1=\operatorname{Tr}([\Phi,\Phi^\dagger])^2\) (checked at matrix sizes \(2,3\) over the conjugation-invariant families): with \(C=[\Phi,\Phi^\dagger]\) Hermitian one has \(W_1=\operatorname{Tr}(C^\dagger C)\ge0\), with equality exactly for normal \(\Phi\) and hence on all of the vacuum manifold Equation~\eqref{eq:vacuum-manifold}, so this lone quartic locks nothing.",
r"Moreover \(W_1\) is not a function of \(X\): left-multiplication by a fixed unitary preserves \(X\) and changes \(W_1\) (diagonal \(\Phi\): \(W_1=0\); its Hadamard image at distinct entries: nonzero), so the class quartic does not enter the \(\operatorname{Tr}X^2\), \((\operatorname{Tr}X)^2\) counterterm channels of the preceding paragraph: the induced \(W(X)\)-channel data of the commutator class is \((0,0)\) for every group choice, the fixed-ray system of that paragraph is vacuous on this branch, and the missing selection datum is not the ratio \(r=c_2/c_3\) or the group but a shift-breaking sector supplying \(W(X)\), every such sector carrying its own instance of the underdetermination above.",
r"Hypotheses and limits: constant real \(\Theta\), the Weyl calculus as the semiclassical description of matrix commutators, the embedding ansatz, adjoint connection, matrix size and reality data of \(\Phi\) as inputs, shift-preserving regularization at the cutoff \(\LUV\) of Equation~\eqref{eq:LUV-def}, and quadratic and quartic order for the class invariants; under these inputs the identity, incompatibility, \(K\)-type bound, frame blindness and \(W_1\) statements are derivations, while the retention of the vanishing of the \(W(X)\) sector to loops is a kinematic-symmetry argument not computed here, the loop coefficient of \(W_1\) is not evaluated, and no matrix-model state or dynamics enters.",
r"Within this class the bridge becomes a derived identity for the adjoint reading while the matching of Section~\ref{sec:ch3-relate} stays conditional on the representation choice, and the datum selecting Equation~\eqref{eq:V} is relocated outside the class rather than supplied: this paragraph closes none of Problem~D, Problem~D1, or Problem~A.",
]
PAYLOAD_TXT = CRLF.join(SENT) + CRLF


def guard_join(text, tag):
    m = re.search(r"\\[A-Za-z]+$", text)
    if m:
        raise SystemExit("JOIN GUARD FIRED (%s): payload ends in dangling command %r" % (tag, m.group(0)))


def check_hygiene(text, tag):
    try:
        pb = text.encode("ascii")
    except UnicodeEncodeError:
        raise SystemExit("HYGIENE FIRED (%s): non-ASCII byte" % tag)
    if pb.startswith(b"\xef\xbb\xbf"):
        raise SystemExit("HYGIENE FIRED (%s): BOM" % tag)
    if chr(9) in text:
        raise SystemExit("HYGIENE FIRED (%s): tab byte" % tag)
    if text.count(chr(13)) != text.count(chr(10)) or not text.endswith(CRLF):
        raise SystemExit("HYGIENE FIRED (%s): CRLF structure" % tag)
    for pat in ("\\label", "\\cite", "$", "\\Tr"):
        if pat in text:
            raise SystemExit("HYGIENE FIRED (%s): forbidden token %r" % (tag, pat))
    for w in ("status", "priority", "completion", "todo", "fixme"):
        if w in text.lower():
            raise SystemExit("HYGIENE FIRED (%s): process word %r" % (tag, w))
    if text.count("{") != text.count("}"):
        raise SystemExit("HYGIENE FIRED (%s): brace imbalance" % tag)
    if text.count("\\(") != text.count("\\)"):
        raise SystemExit("HYGIENE FIRED (%s): inline-math imbalance" % tag)


def expect_fire(tag, fn):
    fired = False
    try:
        fn()
    except SystemExit:
        fired = True
    assert fired, "SELF-TEST FAILED: %s did not fire on injected violation" % tag


# ---- positive controls: every guard must FIRE on an injected violation ----
expect_fire("join", lambda: guard_join("{x}" + chr(92) + "secti", "positive-control"))
expect_fire("ascii", lambda: check_hygiene(NONASCII, "positive-control"))
expect_fire("tab", lambda: check_hygiene("a" + chr(9) + "b" + CRLF, "positive-control"))
expect_fire("bom", lambda: check_hygiene(BOMSTR + "x" + CRLF, "positive-control"))
expect_fire("crlf", lambda: check_hygiene("a" + chr(10) + "b", "positive-control"))
expect_fire("dollar", lambda: check_hygiene("x$y" + CRLF, "positive-control"))
expect_fire("label", lambda: check_hygiene(chr(92) + "label{a}" + CRLF, "positive-control"))
expect_fire("cite", lambda: check_hygiene(chr(92) + "cite{a}" + CRLF, "positive-control"))
expect_fire("Tr", lambda: check_hygiene(chr(92) + "Tr Y" + CRLF, "positive-control"))
expect_fire("word", lambda: check_hygiene("the status is" + CRLF, "positive-control"))
expect_fire("brace", lambda: check_hygiene("{" + CRLF, "positive-control"))
expect_fire("math", lambda: check_hygiene(chr(92) + "(" + CRLF, "positive-control"))
# negative control: the real payload passes all guards
guard_join(PAYLOAD_TXT, "payload")
check_hygiene(PAYLOAD_TXT, "payload")

# ---- live-file pins and POST (recomputed independently) ----
raw = io.open(LIVE, "rb").read()
assert len(raw) == BASE_SIZE, "baseline size mismatch: %d" % len(raw)
assert hashlib.sha1(raw).hexdigest()[:12] == BASE_SHA1_12, "baseline sha1 pin mismatch"
text = raw.decode("utf-8")
assert text.count(ANCHOR) == 1, "anchor count != 1"
assert raw.find(ANCHOR.encode("ascii")) == ANCHOR_OFFSET, "anchor offset moved"
spliced = text.replace(ANCHOR, PAYLOAD_TXT + CRLF + ANCHOR, 1)
post = len(spliced.encode("utf-8"))
pb = PAYLOAD_TXT.encode("ascii")
assert post == BASE_SIZE + len(pb) + 2, "POST mismatch"

# ---- write output (byte-identical on rerun) ----
if os.path.exists(OUT):
    old = io.open(OUT, "rb").read()
    assert old == pb, "rerun not byte-identical"
io.open(OUT, "wb").write(pb)
print("payload bytes: %d  sha1[:12]: %s" % (len(pb), hashlib.sha1(pb).hexdigest()[:12]))
print("POST: %d (= %d + %d + 2)  full sha1: %s"
      % (post, BASE_SIZE, len(pb), hashlib.sha1(spliced.encode("utf-8")).hexdigest()))
print("GUARDS: 12 positive controls fired, payload passed")
print("GEN OK 120")
