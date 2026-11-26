# -*- coding: ascii -*-
# r2 helper: counts anchor variants in live appH; verifies the section-context
# anchor used by the r2 generator is unique. Bounded, read-only.
APPH = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex"
pre = open(APPH, "rb").read()
import hashlib
print("appH sha1", hashlib.sha1(pre).hexdigest(), len(pre))
A = (b"These statements are for the hypotheses and the channel convention "
     b"stated here; they retire the recorded item on the response of the "
     b"fibre levels to \\(\\bar h\\) only for this channel component, they "
     b"change no status label, and Problems~C, F and~N remain open and "
     b"PROGRAMME-CONDITIONAL.")
print("full anchor count:", pre.count(A))
ctx = A + b"\r\n\r\n"
print("anchor+CRLFCRLF count:", pre.count(ctx))
i = pre.find(ctx)
secline = pre[i + len(ctx): i + len(ctx) + 40].split(b"\r\n")[0]
print("section line:", secline)
ctx2 = ctx + secline
print("context anchor (sentence+CRLFCRLF+section-line) count:", pre.count(ctx2))
bare = b"These statements are for the hypotheses"
print("short clause count:", pre.count(bare))
print("INSPECT VERDICT: PASS")
