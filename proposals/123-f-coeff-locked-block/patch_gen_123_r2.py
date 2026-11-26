# -*- coding: ascii -*-
# r2 patch for make_payload_123.py: exact replacements, each asserted
# count==1. All literals are raw strings copied VERBATIM from the generator.
# Old generator bytes preserved as make_payload_123.py.r1-bytes (25063ff6...).
import hashlib
P = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\123-f-coeff-locked-block\make_payload_123.py"
src = open(P, "rb").read()
print("pre-patch sha1", hashlib.sha1(src).hexdigest(), len(src))

def rep(old, new):
    global src
    o = old.encode("ascii"); n = new.encode("ascii")
    c = src.count(o)
    assert c == 1, "count %d for %r" % (c, old[:70])
    src = src.replace(o, n, 1)

# --- R1 (required): fibre-traced endomorphism definition clause
rep(r'''r"Laplace-type block of ten symmetric-tensor components with \(E_{\mathrm{ten}}=e_h R_E\), and the diffeomorphism ghost, supplied as an infrared "''',
    r'''r"Laplace-type block of ten symmetric-tensor components with fibre-traced endomorphism \(\mathrm{tr}\,E_{\mathrm{ten}}="'''
    + "\n " +
    r'''r"e_h R_E\), and the diffeomorphism ghost, supplied as an infrared "''')

# --- R2 (optional A adopted): specify M as Laplace-type; drop the
#     first-variation definition and the "equals" derivation claim.
rep(r'''r"counterterm at this order. Results (identities within the stated scheme, verified symbolically): (i)~the ghost operator "''' + "\n " +
    r'''r"\(M\xi^\mu:=\frac{\mathrm d}{\mathrm d\varepsilon}\big|_0 F^\mu[g+\varepsilon\mathcal L_\xi g]\) equals \(g^{ab}\nabla_a\nabla_b\xi^\mu+"''' + "\n " +
    r'''r"R^\mu{}_\nu\xi^\nu\) in the curvature conventions of Equations~\eqref{eq:christoffel}--\eqref{eq:riemann}, with principal symbol "''' + "\n " +
    r'''r"\(g^{ab}\delta^\mu_\nu\) and overall sign calibrated by the unit sphere at \(R=+2\); hence the positive Euclidean operator \(-M\) is Laplace-type "''',
    r'''r"counterterm at this order. Results (identities within the stated scheme, verified symbolically): (i)~the ghost operator is specified as "''' + "\n " +
    r'''r"the Laplace-type operator \(M\xi^\mu:=g^{ab}\nabla_a\nabla_b\xi^\mu+R^\mu{}_\nu\xi^\nu\) in the curvature conventions of "''' + "\n " +
    r'''r"Equations~\eqref{eq:christoffel}--\eqref{eq:riemann}, with principal symbol \(g^{ab}\delta^\mu_\nu\) and overall sign calibrated by the unit "''' + "\n " +
    r'''r"sphere at \(R=+2\); the positive Euclidean operator \(-M\) has endomorphism "''')

# --- R2 continuation: next source line led with "with endomorphism"; the new
#     lead-in already ends "...has endomorphism ", so drop "with ".
rep(r'''r"with endomorphism \(E_{\mathrm{gh}}{}^\mu{}_\nu=-R^\mu{}_\nu\) and, by \(a_1=\mathrm{tr}(R/6-E)\) of Equation~\eqref{eq:appA-a1}, the ghost fibre "''',
    r'''r"\(E_{\mathrm{gh}}{}^\mu{}_\nu=-R^\mu{}_\nu\) and, by \(a_1=\mathrm{tr}(R/6-E)\) of Equation~\eqref{eq:appA-a1}, the ghost fibre "''')

# --- R2 status list: the ghost operator is now specified, not derived
rep(r'''r"the ghost operator, weight, endomorphism and \(a_1\) contribution, the counts and the windowed \(a_1\)-coefficient are derivations within the "''',
    r'''r"the ghost weight, endomorphism and \(a_1\) contribution, the counts and the windowed \(a_1\)-coefficient are derivations within the "''')

# --- context anchor upgrade (review-r1: bare sentence recurs; count on context)
rep(r'''ANCHOR = ("These statements are for the hypotheses and the channel convention "''',
    r'''# CONTEXT anchor per review-r1: the bare closing clause recurs in other''' + "\n" +
    r'''# section closers, so uniqueness is counted on the full context string''' + "\n" +
    r'''# (anchor sentence + CRLFCRLF + section line).''' + "\n" +
    r'''ANCHOR = ("These statements are for the hypotheses and the channel convention "''')
rep(r'''          "PROGRAMME-CONDITIONAL.")''',
    r'''          "PROGRAMME-CONDITIONAL.")''' + "\n" +
    r'''SECTION = "\section{Problem G: HBEV}"''' + "\n" +
    r'''CTX = (ANCHOR + "\r\n\r\n" + SECTION).encode("ascii")''')
rep(r'''n = pre.count(anchor + CRLF + CRLF)''' + "\n" +
    r'''if n != 1: die("anchor+CRLFCRLF count = %d (need 1)" % n)''' + "\n" +
    r'''print("ANCHOR unique (count 1)")''' + "\n\n" +
    r'''post = pre.replace(anchor + CRLF + CRLF,''' + "\n" +
    r'''                   anchor + CRLF + CRLF + pay + CRLF, 1)''',
    r'''n = pre.count(CTX)''' + "\n" +
    r'''if n != 1: die("context anchor count = %d (need 1)" % n)''' + "\n" +
    r'''print("ANCHOR unique on CONTEXT string (count 1)")''' + "\n\n" +
    r'''post = pre.replace(CTX,''' + "\n" +
    r'''                   anchor + CRLF + CRLF + pay + CRLF + SECTION.encode("ascii"), 1)''')

# --- r2 payload-content guards with injected positive controls
rep(r'''if refs_ok(b"\\ref{nope}", WHITELIST)[0]: die("refs detector dead (control)")''' + "\n" +
    r'''print("CTRL refs: fires OK")''',
    r'''if refs_ok(b"\\ref{nope}", WHITELIST)[0]: die("refs detector dead (control)")''' + "\n" +
    r'''print("CTRL refs: fires OK")''' + "\n" +
    r'''FTOK = rb"fibre-traced endomorphism \(\mathrm{tr}\,E_{\mathrm{ten}}=e_h R_E\)"''' + "\n" +
    r'''NOTOK = rb"\frac{\mathrm d}{\mathrm d\varepsilon}"''' + "\n" +
    r'''def r2tok_ok(b): return (FTOK in b) and (NOTOK not in b)''' + "\n" +
    r'''if r2tok_ok(FTOK + b" tail"): print("CTRL r2-fibretrace: fires OK")''' + "\n" +
    r'''else: die("r2 fibre-trace detector dead (missing-token control)")''' + "\n" +
    r'''if r2tok_ok(b"x" + NOTOK + b"y"): die("r2 first-variation detector dead (present-token control)")''' + "\n" +
    r'''print("CTRL r2-nofirstvar: fires OK")''')
rep(r'''if not braces_ok(pay): die("payload braces unbalanced")''',
    r'''if not braces_ok(pay): die("payload braces unbalanced")''' + "\n" +
    r'''if not r2tok_ok(pay): die("payload missing fibre-traced clause or still has first-variation formula")''' + "\n" +
    r'''print("R2 TOKENS OK")''')

open(P, "wb").write(src)
print("post-patch sha1", hashlib.sha1(src).hexdigest(), len(src))
print("PATCH VERDICT: PASS")
