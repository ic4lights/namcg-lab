# gen_manifest_097_r2.py - writes manifest_r2.md for the folder (no self-line). Run from repo root.
import hashlib, os
D = "proposals/097-g-nonbridge-hetero-variance/"
role = {
    "proposal-r1.md": ("proposal round 1", "SUPERSEDED by proposal-r2.md (kept as record)"),
    "insert-r1.tex": ("insert round 1", "SUPERSEDED, never integrate"),
    "gen_insert_097.py": ("generator r1", "kept (historical provenance of insert-r1.tex)"),
    "verify_097.py": ("math verification (21 checks)", "live, UNCHANGED since r1"),
    "verify_097.out": ("verify r1 output", "live, re-run r2 byte-identical (cmp SAME)"),
    "hygiene_097.py": ("hygiene r1", "kept (source of r2 derivative)"),
    "hygiene_097.out": ("hygiene r1 output", "kept as record"),
    "simulate_apply_097.py": ("splice sim r1", "kept (source of r2 derivative)"),
    "simulate_apply_097.out": ("splice sim r1 output", "kept as record (superseded POST)"),
    "manifest.md": ("manifest r1", "SUPERSEDED by manifest_r2.md"),
    "review-r1.md": ("gatekeeper review round 1", "live input record"),
    "proposal-r2.md": ("proposal round 2 (this package)", "live"),
    "gen_insert_097_r2.py": ("byte surgery r1->r2 + diff proof", "live"),
    "gen_scripts_097_r2.py": ("derives r2 check scripts from r1 bytes", "live"),
    "insert-r2.tex": ("SOLE INTEGRATION ARTIFACT", "live"),
    "hygiene_097_r2.py": ("hygiene r2 (24 checks)", "live"),
    "hygiene_097_r2.out": ("hygiene r2 output", "live"),
    "simulate_apply_097_r2.py": ("splice sim r2 (assert-only, no writes)", "live"),
    "simulate_apply_097_r2.out": ("splice sim r2 output", "live"),
"gen_manifest_097_r2.py": ("manifest r2 generator", "live"),
}
names = sorted(f for f in os.listdir(D) if f != "manifest_r2.md")
missing = [f for f in names if f not in role]
assert not missing, "unregistered: %s" % missing
lines = ["# Manifest for proposals/097-g-nonbridge-hetero-variance (round 2)", "",
         "Integration artifact: insert-r2.tex only. insert-r1.tex must never be integrated.", ""]
for f in names:
    b = open(D + f, "rb").read()
    lines.append("- `%s` | %d B | sha256 %s | %s | %s" % (f, len(b), hashlib.sha256(b).hexdigest(), role[f][0], role[f][1]))
open(D + "manifest_r2.md", "w", newline="").write((chr(13) + chr(10)).join(lines) + chr(13) + chr(10))
print("MANIFEST OK files=%d" % len(names))
raise SystemExit(0)
