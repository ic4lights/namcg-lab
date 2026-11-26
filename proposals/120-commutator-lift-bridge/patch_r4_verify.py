import hashlib

SRC = "verify_r120.py"
data = open(SRC, "r", encoding="utf-8", newline="").read()


def rep(old, new):
    global data
    n = data.count(old)
    assert n == 1, "anchor count %d for %r" % (n, old[:60])
    data = data.replace(old, new)


# 1) shift map: Phi -> Phi + s I (diagonal only)
rep(
    "SH = {}\r\nSH.update({zl[k]: zl[k] + ss for k in range(4)})\r\n"
    "SH.update({dl[k]: dl[k] + ssc for k in range(4)})",
    "# R4: the shift of the claim is Phi -> Phi + s I (frame mode phi_0*I; matches T6e),\r\n"
    "# i.e. only the diagonal entries shift. The previous all-entries map encoded\r\n"
    "# Phi -> Phi + s*(all-ones matrix), which is not that shift.\r\n"
    "SH = {}\r\n"
    "SH.update({zl[0]: zl[0] + ss, zl[3]: zl[3] + ss, dl[0]: dl[0] + ssc, dl[3]: dl[3] + ssc})",
)

# 2) left nullspace (family-combination coefficients), was right nullspace (monomial space)
rep(
    "    Mx = sp.Matrix(len(rows), len(mons), lambda i, j: rows[i].coeff_monomial(mons[j]))\r\n"
    "    return Mx.nullspace()",
    "    Mx = sp.Matrix(len(rows), len(mons), lambda i, j: rows[i].coeff_monomial(mons[j]))\r\n"
    "    # R4: family-combination kernel = LEFT nullspace (Mx^T v = 0); the previous\r\n"
    "    # right nullspace lives in monomial space and does not measure invariant combinations.\r\n"
    "    return Mx.T.nullspace()",
)

# 3) T6f expectation -> truth (3-dim traceless-part span; Tr X direction shift-variant)
rep(
    "nsq = nulltest(QUAD)\r\n"
    "chk(\"T6f no nonzero quadratic conjugation-invariant is shift-invariant (6-dim family, exact nullspace)\",\r\n"
    "    len(nsq) == 0)",
    "nsq = nulltest(QUAD)\r\n"
    "# R4 truth (probe_r4_triage2 heavy2): the shift-invariant quadratic subspace is exactly\r\n"
    "# the 3-dim span of the traceless-part invariants 2*TrX - TrPhi TrPhidag,\r\n"
    "# 2*Re TrPhi^2 - Re(TrPhi)^2, 2*Im TrPhi^2 - Im(TrPhi)^2; none is a function of X, and\r\n"
    "# the Tr X direction itself is shift-variant (no X-dependent quadratic invariant).\r\n"
    "GENQ = [sp.Matrix([-2, 0, 0, 1, 0, 0]), sp.Matrix([0, -2, 0, 0, 1, 0]),\r\n"
    "        sp.Matrix([0, 0, -2, 0, 0, 1])]\r\n"
    "okf = (len(nsq) == 3) and (sp.Matrix.hstack(*(nsq + GENQ)).rank() == 3)\r\n"
    "okx = (len(nulltest([QUAD[0]])) == 0)\r\n"
    "chk(\"T6f quadratic n=2: shift-invariant subspace exactly the 3 traceless-part invariants; Tr X direction shift-variant (no X-dependent quadratic invariant)\",\r\n"
    "    okf and okx)",
)

# 4) T6g: corrected W1 word, family without dependent column, expectation 4-dim + W1 direction
rep(
    "W1w = sp.expand(2 * w4 - w3 - w2 - cJ(w2))\r\n"
    "nsg = nulltest(QUAR + [W1w])\r\n"
    "ok = (len(nsg) == 1) and (nsg[0][len(QUAR)] != 0) if len(nsg) >= 1 else False\r\n"
    "chk(\"T6g quartic conjugation-invariant family + W1 at n=2: shift-invariant subspace exactly 1-dim, W1-direction\",\r\n"
    "    ok)",
    "# R4: corrected W1 word, Tr C^2 = 2 Tr(P Pd P Pd) - 2 Tr(P^2 Pd^2), C = P Pd - Pd P\r\n"
    "# (probe_r4_triage P0/P2). W1w = 2*w4 - 2*w3 is linearly dependent on the family, so it\r\n"
    "# is not appended as a separate column; the W1 direction (w4 - w3) is tested inside the\r\n"
    "# family. Truth (heavy2): the shift-invariant subspace of this 16-element family is\r\n"
    "# exactly 4-dimensional (W1 direction + three further traceless-part invariants), not 1.\r\n"
    "W1w = sp.expand(2 * w4 - 2 * w3)\r\n"
    "nsg = nulltest(QUAR)\r\n"
    "WDIR = sp.Matrix([0, 0, 0, 0, -1, 1] + [0] * 10)\r\n"
    "ok = (len(nsg) == 4) and (sp.Matrix.hstack(*(nsg + [WDIR])).rank() == 4)\r\n"
    "chk(\"T6g quartic conjugation-invariant family at n=2: shift-invariant subspace exactly 4-dim and contains the W1 direction w4 - w3\",\r\n"
    "    ok)",
)

# 5) T6h name to the corrected identity (expectation expression unchanged: to_ri(W1w) == W2)
rep(
    "chk(\"T6h W1 word identity: 2 Tr(P Pd P Pd) - Tr(P^2 Pd^2) - Tr(P^3 Pd) - h.c. = W1 (real/imag form)\",\r\n"
    "    sp.expand(to_ri(W1w) - W2) == 0)",
    "chk(\"T6h W1 word identity: 2 Tr(P Pd P Pd) - 2 Tr(P^2 Pd^2) = W1 (real/imag form; W1 = Tr(C^dag C), C = [Phi, Phi^dag])\",\r\n"
    "    sp.expand(to_ri(W1w) - W2) == 0)",
)

# 6) T7c: impose the unitarity constraint exactly via the numerator identity, plus teeth
rep(
    "al, be = sp.symbols(\"al be\", complex=True)\r\n"
    "U2g = sp.Matrix([[al, be], [-sp.conjugate(be), sp.conjugate(al)]])\r\n"
    "Pg = cmat(2, \"g\")\r\n"
    "ok = (sp.expand((U2g * Pg).adjoint() * (U2g * Pg) - Pg.adjoint() * Pg) == sp.zeros(2))\r\n"
    "chk(\"T7c left action by any matrix with U^dagger U = I preserves X for generic Phi (channel obstruction)\", ok)",
    "# R4: the old code checked an UNnormalized U (U^dag U = (|al|^2+|be|^2) I, not I), so the\r\n"
    "# old expectation was false for generic al, be. The general U(2) matrix is\r\n"
    "# U = (a1+i a2, a3+i a4; -(a3-i a4), a1-i a2)/sqrt(norm) with norm = |a1+ia2|^2+|a3+ia4|^2;\r\n"
    "# truth: (U2 Phi)^dag (U2 Phi) = norm * Phi^dag Phi exactly, so the normalized U preserves\r\n"
    "# X, and the unscaled matrix does not when norm != 1 (teeth).\r\n"
    "a1, a2, a3, a4 = sp.symbols(\"a1 a2 a3 a4\", real=True)\r\n"
    "U2g = sp.Matrix([[a1 + sp.I * a2, a3 + sp.I * a4], [-(a3 - sp.I * a4), a1 - sp.I * a2]])\r\n"
    "norm = a1 ** 2 + a2 ** 2 + a3 ** 2 + a4 ** 2\r\n"
    "Pg = cmat(2, \"g\")\r\n"
    "ok = (sp.expand((U2g * Pg).adjoint() * (U2g * Pg) - norm * (Pg.adjoint() * Pg)) == sp.zeros(2))\r\n"
    "ok = ok and (sp.expand((U2g * Pg).adjoint() * (U2g * Pg) - Pg.adjoint() * Pg) != sp.zeros(2))\r\n"
    "chk(\"T7c general U(2): (U2 Phi)^dag(U2 Phi) = norm * Phi^dag Phi, so normalized U preserves X (channel obstruction); unscaled U does not\",\r\n"
    "    ok)",
)

open(SRC, "w", encoding="utf-8", newline="").write(data)
b = open(SRC, "rb").read()
print("patched OK sha1[:12]", hashlib.sha1(b).hexdigest()[:12], "size", len(b))
