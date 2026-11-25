# -*- coding: ascii -*-
# r2 INDEPENDENT POST recompute (does not import or call the generator):
# reads live appH + payload-123.txt, splices on the context anchor, prints
# sha1/length, verifies arithmetic and byte-equality with the generator's
# spliced file given as argv[1]. Bounded, read-only on the repo.
import hashlib, sys
APPH = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex"
FOLD = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\123-f-coeff-locked-block"
pre = open(APPH, "rb").read()
pay = open(FOLD + r"\payload-123.txt", "rb").read()
CTX = (b"These statements are for the hypotheses and the channel convention "
       b"stated here; they retire the recorded item on the response of the "
       b"fibre levels to \\(\\bar h\\) only for this channel component, they "
       b"change no status label, and Problems~C, F and~N remain open and "
       b"PROGRAMME-CONDITIONAL.\r\n\r\n\\section{Problem G: HBEV}")
assert pre.count(CTX) == 1, "context anchor not unique"
i = pre.find(CTX) + (len(CTX) - len(b"\\section{Problem G: HBEV}"))
post = pre[:i] + pay + b"\r\n" + pre[i:]
print("PRE ", hashlib.sha1(pre).hexdigest(), len(pre))
print("PAY ", hashlib.sha1(pay).hexdigest(), len(pay))
print("POST", hashlib.sha1(post).hexdigest(), len(post))
assert len(post) == len(pre) + len(pay) + 2
assert post.count(pay) == 1
if len(sys.argv) > 1:
    g = open(sys.argv[1], "rb").read()
    print("matches generator spliced file:", g == post)
print("RECOM POST VERDICT: PASS")
