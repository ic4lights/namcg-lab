# retarget_r2_107b.py -- step 3 only (steps 1-2 already produced by retarget_r2_107.py).
# v5 -> v6 header comment fix (F4 reuse path, F5 "byte-for-byte" wording). The r1 driver's
# pattern missed the leading "# and" on the first header line; corrected here. Asserts:
# unique match, same line count, changed lines exactly the two header comment lines
# (0-based 15, 16), both comments, and identical ast.dump (code body unchanged).
import ast
import hashlib

d = "proposals/107-a-map-chart-condensate-selection/"
src, dst = d + "s3_symbol_selection_v5.py", d + "s3_symbol_selection_v6.py"
before = open(src, "rb").read()
old_hdr = (b"# and the selected table c(B) = B2PB table: the item-106 framework, definitions copied\n"
           b"# byte-for-byte from proposals/106-a-map-chart-condensate-selection/s2_matrix_selection.py\n")
new_hdr = (b"# and the selected table c(B) = B2PB table: the item-106 framework, definitions reused\n"
           b"# verbatim (shared blocks; v6 header-only F4/F5 fix) from proposals/106-a-map-matrix-selection-b2/s2_matrix_selection.py\n")
assert before.count(old_hdr) == 1, "header pattern not unique/absent"
b = before.replace(old_hdr, new_hdr, 1)
la, lb = before.split(b"\n"), b.split(b"\n")
assert len(la) == len(lb), "line count changed"
changed = [i for i in range(len(la)) if la[i] != lb[i]]
assert changed == [15, 16], "unexpected changed lines %s" % changed
for i in changed:
    assert la[i].lstrip().startswith(b"#") and lb[i].lstrip().startswith(b"#"), "not comments"
ast.parse(b.decode("utf-8"))
assert ast.dump(ast.parse(before.decode())) == ast.dump(ast.parse(b.decode())), "AST differs"
open(dst, "wb").write(b)
for p in (src, dst):
    x = open(p, "rb").read()
    print("%s %d sha256/16 %s" % (p, len(x), hashlib.sha256(x).hexdigest()[:16]))
print("v5->v6: header comments only, AST IDENTICAL. RETARGET+FIX: OK")
