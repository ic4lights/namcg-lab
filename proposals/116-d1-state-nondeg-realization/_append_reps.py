# _append_reps.py -- add the two grep-audit label renames into patch_r2.py so it
# reproduces the FINAL proposal-r2.md bytes in one run.
p = "patch_r2.py"
d = open(p, "rb").read()
anchor = b"# --- payload line swap (r1 quoted block -> r2 payload) ---"
assert d.count(anchor) == 1
add = (
    b"# --- label renames found by the post-patch grep audit ---\n"
    b"""rep(\"### D5. Volume/a.e. realization (edge 1(b), positive)\",\n"""
    b"""    \"### D5. Volume/small-measure realization (edge 1(b), positive)\")\n"""
    b"""rep(\"a.e./volume realization).** Chosen because both rest on one derivation\",\n"""
    b"""    \"small-measure/volume realization).** Chosen because both rest on one derivation\")\n\n"""
)
d = d.replace(anchor, add + anchor)
open(p, "wb").write(d)
print("patch_r2.py updated,", len(d), "bytes")
