# -*- coding: ascii -*-
import re
P = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\123-f-coeff-locked-block\patch_gen_123_r2.py"
b = open(P, "rb").read()
i = b.find(b"gh}}")
print("context bytes:", b[i:i + 26])
# target: the pattern `gh}}{}_` followed by backslashes then `mu`
old = b"gh}}{}_" + b"\\" * 2 + b"mu"
new = b"gh}}{}^" + b"\\" * 2 + b"mu"
c = b.count(old)
print("count old:", c)
assert c == 2, c
b = b.replace(old, new)
open(P, "wb").write(b)
print("FIX VERDICT: PASS")
