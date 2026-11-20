# gen_scripts_097_r2.py - derive hygiene_097_r2.py and simulate_apply_097_r2.py from the r1 originals.
# Run from repo root. Byte-exact substitutions only; asserts every substitution lands exactly once.
D = "proposals/097-g-nonbridge-hetero-variance/"

s = open(D + "hygiene_097.py", "rb").read()
assert s.count(b"insert-r1.tex") == 2
s = s.replace(b"insert-r1.tex", b"insert-r2.tex")
extra = (
    b'chk("H17 F1 snippet applied", "every exact identity" not in body and '
    b'"tilted one, exactly so at" in body)\n'
    b'chk("H18 F2 wording", body.count("the variance profile ") == 1)\n'
    b'chk("H19 F2 old wording gone", "the profile " + BS + "(g" not in body)\n'
)
assert s.count(b'print("SUMMARY') == 1
s = s.replace(b'print("SUMMARY', extra + b'print("SUMMARY', 1)
open(D + "hygiene_097_r2.py", "wb").write(s)

t = open(D + "simulate_apply_097.py", "rb").read()
assert t.count(b"insert-r1.tex") == 2
t = t.replace(b"insert-r1.tex", b"insert-r2.tex")
old_line = b'assert len(post) == 786123 and len(ins) == 5373, "insert/POST sizes"'
new_line = b'assert len(post) == 786170 and len(ins) == 5420, "insert/POST sizes"'
assert t.count(old_line) == 1
t = t.replace(old_line, new_line)
open(D + "simulate_apply_097_r2.py", "wb").write(t)
print("PATCH OK: hygiene_097_r2.py, simulate_apply_097_r2.py written")
raise SystemExit(0)
