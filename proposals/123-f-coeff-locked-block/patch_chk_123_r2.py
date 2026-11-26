# -*- coding: ascii -*-
# r2 patch for check_payload_123_r1.py: update PAY/POST constants to the r2
# payload, upgrade the anchor check to the section-context string, add r2
# content checks with positive controls. Literals raw, verbatim from file.
# Old bytes preserved as check_payload_123_r1.py.r1-bytes (462ed5b332ac...).
import hashlib
P = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\123-f-coeff-locked-block\check_payload_123_r1.py"
src = open(P, "rb").read()
print("pre-patch sha1", hashlib.sha1(src).hexdigest(), len(src))

def rep(old, new):
    global src
    o = old.encode("ascii"); n = new.encode("ascii")
    assert src.count(o) == 1, "count %d for %r" % (src.count(o), old[:70])
    src = src.replace(o, n, 1)

rep(r'''POST_SHA1 = "704f3765797a89371fa683089b560e6a496f5df6"''',
    r'''POST_SHA1 = "ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1"''')
rep(r'''PAY_SHA1 = "5548ee218f2c"  # 12-hex of payload-123.txt''',
    r'''PAY_SHA1 = "e0b8d6b31cad"  # 12-hex of payload-123.txt (r2 bytes)''')

# context anchor: append the section line to ANCHOR-based uniqueness checks
rep(r'''          b"PROGRAMME-CONDITIONAL.")''',
    r'''          b"PROGRAMME-CONDITIONAL.")''' + "\n" +
    r'''SECLINE = b"\section{Problem G: HBEV}"  # context anchor (review-r1)''' + "\n" +
    r'''CTX = ANCHOR + CRLF + CRLF + SECLINE''')
rep(r'''chk("ANCHOR_UNIQUE", pre.count(ANCHOR + CRLF + CRLF) == 1)''' + "\n" +
    r'''post = pre.replace(ANCHOR + CRLF + CRLF, ANCHOR + CRLF + CRLF + pay + CRLF, 1)''',
    r'''chk("ANCHOR_UNIQUE_CTX", pre.count(CTX) == 1)''' + "\n" +
    r'''chk("CTRL_ANCHOR_DEAD", pre.count(b"PROGRAMME-CONDITIONAL.XYZ" + CRLF + CRLF + SECLINE) == 0)''' + "\n" +
    r'''i0 = pre.find(CTX) + len(CTX) - len(SECLINE)''' + "\n" +
    r'''post = pre[:i0] + pay + CRLF + pre[i0:]''')

# r2 content checks with positive controls
rep(r'''print("CHECKER VERDICT:", "PASS" if all(ok) else "FAIL")''',
    r'''FTOK = rb"fibre-traced endomorphism \(\mathrm{tr}\,E_{\mathrm{ten}}=e_h R_E\)"''' + "\n" +
    r'''STOK = rb"the ghost operator is specified as the Laplace-type operator"''' + "\n" +
    r'''NOTOK = rb"\frac{\mathrm d}{\mathrm d\varepsilon}"''' + "\n" +
    r'''chk("PAY_FIBRETRACE", FTOK in pay)''' + "\n" +
    r'''chk("PAY_GHOST_SPEC", STOK in pay)''' + "\n" +
    r'''chk("PAY_NO_FIRSTVAR", NOTOK not in pay)''' + "\n" +
    r'''chk("CTRL_PAY_NO_FIRSTVAR", NOTOK not in (pay + b"z") and NOTOK in (pay + NOTOK))''' + "\n" +
    r'''chk("CTRL_PAY_FIBRETRACE", FTOK in pay and FTOK.replace(b"fibre", b"fibrX") not in pay)''' + "\n" +
    r'''print("CHECKER VERDICT:", "PASS" if all(ok) else "FAIL")''')

open(P, "wb").write(src)
print("post-patch sha1", hashlib.sha1(src).hexdigest(), len(src))
print("PATCH VERDICT: PASS")
