# retarget_r2_107.py -- proposal 107 round 2, retarget + header-fix driver.
# Three byte-surgery products, every replacement an asserted exact unique match,
# every output ast.parse-checked. Writes ONLY inside the proposal folder.
#  1) hygiene_107.py          -> hygiene_107_r2.py        (target constant insert-r1 -> r2)
#  2) simulate_apply_107.py   -> simulate_apply_107_r2.py (INS constant -> r2; OUT preview
#                                -> appH_after_107_r2.tex so the r1 preview survives)
#  3) s3_symbol_selection_v5.py -> s3_symbol_selection_v6.py (header-only F4/F5 fix: correct
#     reuse path and "byte-for-byte" -> "reused verbatim (shared blocks)"; diff must touch
#     only those two comment lines and ast.dump must be identical -> code body unchanged)
import ast
import hashlib

d = "proposals/107-a-map-chart-condensate-selection/"

def triple(p):
    b = open(p, "rb").read()
    return "%s %d sha256/16 %s" % (p, len(b), hashlib.sha256(b).hexdigest()[:16])

def edit(src, dst, reps, comment_only=None):
    b = open(src, "rb").read()
    before = b
    for old, new in reps:
        assert b.count(old) == 1, "pattern not unique/absent in %s: %r" % (src, old[:60])
        b = b.replace(old, new, 1)
    assert b != before
    if comment_only is not None:
        la, lb = before.split(b"\n"), b.split(b"\n")
        assert len(la) == len(lb), "line count changed"
        changed = [i for i in range(len(la)) if la[i] != lb[i]]
        assert changed == comment_only, "unexpected changed lines %s (expected %s)" % (changed, comment_only)
        for i in changed:
            assert la[i].lstrip().startswith(b"#"), "changed line %d not a comment" % i
    ast.parse(b.decode("utf-8"))
    open(dst, "wb").write(b)
    print("wrote " + triple(dst))

# 1) hygiene retarget
edit(d + "hygiene_107.py", d + "hygiene_107_r2.py",
     [(b"hygiene_107.py -- checks insert-r1.tex",
       b"hygiene_107_r2.py -- checks insert-r2.tex"),
      (rb'F = r"proposals\107-a-map-chart-condensate-selection\insert-r1.tex"',
       rb'F = r"proposals\107-a-map-chart-condensate-selection\insert-r2.tex"')])

# 2) simulate retarget (new preview name; r1 preview preserved)
edit(d + "simulate_apply_107.py", d + "simulate_apply_107_r2.py",
     [(b"simulate_apply_107.py -- PIN-based",
       b"simulate_apply_107_r2.py -- PIN-based"),
      (rb'INS = r"proposals\107-a-map-chart-condensate-selection\insert-r1.tex"',
       rb'INS = r"proposals\107-a-map-chart-condensate-selection\insert-r2.tex"'),
      (rb'OUT = r"scratch\sim\appH_after_107.tex"',
       rb'OUT = r"scratch\sim\appH_after_107_r2.tex"')])

# 3) v5 -> v6, header comments only (F4 path, F5 wording); code body byte-identical in AST
old_hdr = (b"# selected table c(B) = B2PB table: the item-106 framework, definitions copied\n"
           b"# byte-for-byte from proposals/106-a-map-chart-condensate-selection/s2_matrix_selection.py\n")
new_hdr = (b"# selected table c(B) = B2PB table: the item-106 framework, definitions reused\n"
           b"# verbatim (shared blocks; v6 header-only F4/F5 fix) from proposals/106-a-map-matrix-selection-b2/s2_matrix_selection.py\n")
edit(d + "s3_symbol_selection_v5.py", d + "s3_symbol_selection_v6.py",
     [(old_hdr, new_hdr)], comment_only=[15, 16])

b5 = open(d + "s3_symbol_selection_v5.py", "rb").read()
b6 = open(d + "s3_symbol_selection_v6.py", "rb").read()
assert ast.dump(ast.parse(b5.decode())) == ast.dump(ast.parse(b6.decode())), "AST differs"
print("v5 vs v6: AST dumps IDENTICAL (code body unchanged); v6 = " + triple(d + "s3_symbol_selection_v6.py"))
print("RETARGET+FIX: OK")
