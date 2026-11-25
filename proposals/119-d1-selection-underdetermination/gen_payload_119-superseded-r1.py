# gen_payload_119.py -- generator for insert-overdetermination-r1.tex (chain 119, round 1).
# Deterministic: embeds the payload, asserts hygiene, verifies live-file pins, prints POST.
# Join guard with MANDATORY positive control (injected broken fragment must FIRE the guard)
# and negative control (real payload must pass), per chain-117/118 lessons.
import hashlib
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LIVE = os.path.join(REPO, "chapters", "appH-microscopic-proofs.tex")
OUT = os.path.join(HERE, "insert-overdetermination-r1.tex")
ANCHOR = "\\section{Problem E: signature}"
BASE_SIZE = 843649
BASE_SHA1_12 = "2ed53c7778c1"
CRLF = "\r\n"

# ---- payload (single additive paragraph; one sentence-group per line) ----
SENT = [
r"\emph{One-loop and scheme-level constraints on the selection datum.} Write \(X=\Phi^\dagger\Phi\) and \(r=c_2/c_3\) for the four couplings \((c_3,c_2,c_1,c_0)\) of the general \(U(4)\)-invariant potential \(c_3\operatorname{Tr}X^2+c_2(\operatorname{Tr}X)^2+c_1\operatorname{Tr}X+c_0\), so that Equation~\eqref{eq:V} is the slice \((\lambda/4,\,0,\,-\lambda v^2/2,\,\lambda v^4)\).",
r"At tree level nothing fixes this slice: the matter term \(S_{\mathrm{matter}}\) of Equation~\eqref{eq:Smatrix} is a symbolic placeholder that has never been specified, and the minimal kinetic lift of Equation~\eqref{eq:Smatrix} to the bifundamental of Equation~\eqref{eq:Smicro} is invariant under \(\Phi\mapsto\Phi+\kappa\,\mathbb I\), a symmetry that forbids any potential, whereas Equation~\eqref{eq:V} is not shift-invariant; every local \(W(X)\) assigned in Presentation~B is therefore an added datum rather than an output of Equation~\eqref{eq:Smatrix}.",
r"At one loop the scalar sector generates \((\operatorname{Tr}X)^2\): for the counterterm kernel \(\operatorname{Tr}(H_WH_W)\), with \(H_W\) the Hessian in the real components of \(\Phi\), one has \(\operatorname{Tr}(H_{\operatorname{Tr}X^2}^2)=256\operatorname{Tr}X^2+96(\operatorname{Tr}X)^2\) at \(n=4\) (ratio \(3/8\)), so \(\beta_{c_2}>0\) on the slice \(c_2=0\).",
r"The gauge contribution is group data: over an orthonormal Hermitian \(u(N)\) basis the gauge loop gives exactly \(+N\operatorname{Tr}X^2\) with vanishing \((\operatorname{Tr}X)^2\) coefficient, while over an orthonormal \(su(N)\) basis it gives \((N-2/N)\operatorname{Tr}X^2+(1/N^2)(\operatorname{Tr}X)^2\), so the generated ratio of \((\operatorname{Tr}X)^2\) to \(\operatorname{Tr}X^2\) at \(N=4\) is \(1/56\) against \(0\) for \(U(4)\), and the group choice itself is not fixed by Equation~\eqref{eq:Smicro}.",
r"With \(w=g^4/c_3^2\), \(v_4=\sum_f y_f^4/c_3^2\), and \(B_G\) the coefficient of the gauge contribution to \(\beta_{c_2}\) in units of \(w\) (\(B_G=0\) for \(u(4)\), \(1/16\) for \(su(4)\)), \(\beta_{c_3}=c_3^2(256+192r+4w-4v_4)/(32\pi^2)\), \(\beta_{c_2}=c_3^2(96+512r+640r^2+B_Gw)/(32\pi^2)\), and \(\beta_r=c_3P(r)/(32\pi^2)\) with \(P(r)=448r^2+(256+4(v_4-w))r+96+B_Gw\).",
r"Renormalizable Yukawa couplings enter through \(\operatorname{Tr}X^2\) only (single cyclic-word identity), so \(P(0)=96+B_Gw>0\) is fermion-independent, the slice \(c_2=0\) is not a fixed ray and not an infrared attractor, and real fixed rays exist if and only if \((w-v_4-64)^2>10752+112B_Gw\): at \(B_G=v_4=0\) none occur for \(0\le w\le 64+16\sqrt{42}\approx167.7>16\pi^2\), and off-window at \(w=200\) the two exact rays are \(r=3/14\) and \(r=1\).",
r"The \(c_1\) direction is scheme- and content-dependent: a sharp cutoff generates \(\delta c_1=(\Lambda^2/64\pi^2)(64c_3+136c_2+\ldots)\operatorname{Tr}X\) with the omitted gauge-ghost and Yukawa terms of content-dependent sign (bosonic loops positive, fermionic negative), Pauli--Villars replaces the quadratic sensitivity by a finite regulator-spectrum datum, and in a mass-independent minimal-subtraction scheme \(\beta_{c_1}=c_1\gamma\) carries no additive term, so \(c_1=0\) is an exact renormalization surface rather than a derived value.",
r"The constant-\(\Theta\) Moyal structure generates no potential either: every \(p\)-th star term carries at least one derivative on each factor, so at zero gradient the star potential collapses to the ordinary potential to all orders, the \(O(\Theta)\) correction being a total derivative and the \(O(\Theta^2)\) correction a pure derivative operator.",
r"Scope: within this hypothesis class (tree-level Presentation~A with unspecified matter term or minimal shift-symmetric lift, a local Presentation-B potential \(W(X)\) for \(n=4\) bifundamental scalars, renormalizable gauge and Yukawa couplings, group choice as input, fixed-\(\Theta\) deformation, one-loop accuracy) these computations constrain but do not select the slice of Equation~\eqref{eq:V}; closing the selection would require an explicit \(S_{\mathrm{matter}}\) or lift, or a specified group, fermion content and ultraviolet boundary condition on \((c_3,c_2,c_1)\) at the cutoff \(\LUV\) of Equation~\eqref{eq:LUV-def}, or a non-renormalizable double-trace completion, none of which Equation~\eqref{eq:Smatrix} supplies; a dynamical-\(\Theta\) or strongly coupled branch is not evaluated here, and none of the listed data, if specified, is excluded from realizing the slice.",
r"The selection of Equation~\eqref{eq:V} by Presentation~A therefore remains an input of the matching discussed in Section~\ref{sec:ch3-relate}: it is constrained but underdetermined as datum, and nothing in this paragraph closes Problem~D, Problem~D1, or Problem~A.",
]
PAYLOAD_TXT = CRLF.join(SENT) + CRLF


def guard_join(text, tag):
    # join guard: payload must not end dangling inside a command name, because the splice
    # concatenates payload + CRLF + anchor; a trailing "\secti" would emit an undefined cmd.
    m = re.search(r"\\[A-Za-z]+$", text)
    if m:
        raise SystemExit("JOIN GUARD FIRED (%s): payload ends in dangling command %r" % (tag, m.group(0)))


# ---- controls ----
# positive control: inject a broken fragment at the join and prove the guard FIRES
fired = False
try:
    guard_join("{x}\\secti", "positive-control")
except SystemExit:
    fired = True
assert fired, "SELF-TEST FAILED: join guard did not fire on injected fragment"
# negative control: the real payload passes
guard_join(PAYLOAD_TXT, "payload")

# ---- hygiene asserts on the payload text ----
pb = PAYLOAD_TXT.encode("ascii")  # raises if any non-ASCII byte
assert b"\t" not in pb and not pb.startswith(b"\xef\xbb\xbf")
assert pb.count(b"\r") == pb.count(b"\n") and pb.endswith(b"\r\n")
assert b"\\label" not in pb and b"\\cite" not in pb and b"$" not in pb
assert PAYLOAD_TXT.count("{") == PAYLOAD_TXT.count("}"), "brace imbalance"
assert PAYLOAD_TXT.count("\\(") == PAYLOAD_TXT.count("\\)"), "inline-math imbalance"

# ---- live-file pins and POST (recomputed independently of any other tool) ----
raw = io.open(LIVE, "rb").read()
assert len(raw) == BASE_SIZE, "baseline size mismatch: %d" % len(raw)
assert hashlib.sha1(raw).hexdigest()[:12] == BASE_SHA1_12, "baseline sha1 pin mismatch"
text = raw.decode("utf-8")
assert text.count(ANCHOR) == 1, "anchor count != 1"
spliced = text.replace(ANCHOR, PAYLOAD_TXT + CRLF + ANCHOR, 1)  # canonical splice: blank line before \section
post = len(spliced.encode("utf-8"))
assert post == BASE_SIZE + len(pb) + 2, "POST mismatch"

# ---- write output (byte-identical on rerun) ----
if os.path.exists(OUT):
    old = io.open(OUT, "rb").read()
    assert old == pb, "rerun not byte-identical"
io.open(OUT, "wb").write(pb)
print("payload bytes: %d  sha1[:12]: %s" % (len(pb), hashlib.sha1(pb).hexdigest()[:12]))
print("POST: %d (= %d + %d + 2)  full sha1: %s" % (post, BASE_SIZE, len(pb), hashlib.sha1(spliced.encode("utf-8")).hexdigest()))
print("GEN OK 119")
