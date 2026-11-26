# build_v2_generator_126.resume.py -- writes make_payload_126.v2.py from the pinned
# make_payload_126.py bytes: (1) header note, (2) a runtime BODY-clause replacement block
# (finding F1) inserted before the PAYLOAD assignment, (3) v2 output names. The block
# replaces two backslash-free plain substrings of the concatenated BODY, so the inserted
# block itself carries no LaTeX and no escaping ambiguity (backslashes enter only via
# _P = chr(92) concatenation at runtime, with count==1 assertions that fire on drift).
# v1 bytes untouched (preserved as make_payload_126.v1.py, sha1 d2826812c80a).
import hashlib

B = chr(92)
src = open("make_payload_126.py", encoding="ascii").read()

hdr_old = "# make_payload_126.py -- writes payload-126.txt (exact splice bytes) and the spliced\n"
hdr_new = ("# make_payload_126.v2.py -- payload v2 for chain 126: one-clause fix of finding F1 (the\n"
           "# operator on End(C^4) is now stated as [D^a,[D_a,.]], the class ghost operator up to\n"
           "# the sign of X_a = i D_a (appH L1617, L1624); v1 bytes preserved in\n"
           "# make_payload_126.v1.py and payload-126.txt (sha1 7e6ed4cd6c83).\n"
           "# writes payload-126-v2.txt (exact splice bytes) and the spliced\n")
assert src.count(hdr_old) == 1, "header anchor"
s = src.replace(hdr_old, hdr_new)

anchor = 'PAYLOAD = BODY.encode("ascii") + b"' + B + 'r' + B + 'n"'
assert s.count(anchor) == 1, "PAYLOAD anchor"

block = (
    "_P = chr(92)\n"
    "assert BODY.count('The ghost operator on') == 1, 'F1 anchor 1 missing/duplicate'\n"
    "BODY = BODY.replace('The ghost operator on',\n"
    "    'The operator ' + _P + '([' + _P + 'mathbb D^a,[' + _P + 'mathbb D_a,'\n"
    "    + _P + 'cdot' + _P + ',]]' + _P + ') on')\n"
    "assert BODY.count('), the class ghost operator at') == 1, 'F1 anchor 2 missing/duplicate'\n"
    "BODY = BODY.replace('), the class ghost operator at',\n"
    "    '), the class ghost operator up to the sign of ' + _P + '(' + _P + 'hat X_a=' + _P + 'mathrm i'\n"
    "    + _P + 'mathbb D_a' + _P + ') at')\n"
    "assert 'up to the sign of' in BODY and 'The ghost operator on' not in BODY, 'F1 fix failed'\n"
    "\n"
)
s = s.replace(anchor, block + anchor)

s = s.replace('open("payload-126.txt", "wb")', 'open("payload-126-v2.txt", "wb")')
s = s.replace('open("appH-spliced-126.tex", "wb")', 'open("appH-spliced-126-v2.tex", "wb")')
assert 'open("payload-126.txt"' not in s and 'open("appH-spliced-126.tex"' not in s, "output names"
open("make_payload_126.v2.py", "w", encoding="ascii", newline="").write(s)
print("V2-GEN-WRITTEN", len(s), hashlib.sha1(s.encode("ascii")).hexdigest())
