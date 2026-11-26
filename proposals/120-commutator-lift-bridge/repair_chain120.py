# repair_chain120.py - combined audit re-deriver for the check-side repair chain.
# Copies verify_r120-preR1.py and the three patch scripts into a temp dir, applies
# R1 -> R2 -> R3 there in order (each in APPLIED mode on the rebuilt chain), and checks
# the result equals the current verify_r120.py byte for byte. Deletes the temp dir.
# Run: python -I -B repair_chain120.py   ->   "CHAIN OK 120"
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["verify_r120-preR1.py", "patch_r1_t5c.py", "patch_r2_simplify.py",
         "patch_r3_liftcongruence.py"]
tmp = tempfile.mkdtemp(prefix="chain120_")
try:
    for f in FILES:
        shutil.copyfile(os.path.join(HERE, f), os.path.join(tmp, f))
    shutil.copyfile(os.path.join(HERE, "verify_r120-preR1.py"),
                    os.path.join(tmp, "verify_r120.py"))
    for scr in ["patch_r1_t5c.py", "patch_r2_simplify.py", "patch_r3_liftcongruence.py"]:
        r = subprocess.run([sys.executable, "-I", "-B", scr], cwd=tmp,
                           capture_output=True, text=True)
        last = [l for l in (r.stdout + r.stderr).splitlines() if l.strip()][-1] if (r.stdout + r.stderr).strip() else ""
        print("%s -> rc=%d | %s" % (scr, r.returncode, last))
        assert r.returncode == 0, scr + " failed:\n" + r.stdout + r.stderr
    out = io.open(os.path.join(tmp, "verify_r120.py"), "rb").read()
    cur = io.open(os.path.join(HERE, "verify_r120.py"), "rb").read()
    ho = hashlib.sha1(out).hexdigest()[:12]
    hc = hashlib.sha1(cur).hexdigest()[:12]
    print("re-derived %s/%d B; current %s/%d B" % (ho, len(out), hc, len(cur)))
    assert out == cur, "chain re-derivation differs from current verify_r120.py"
    # every pre-repair chk claim string must still occur verbatim in the final file
    pre = io.open(os.path.join(tmp, FILES[0]), "r").read()
    import re
    import io as _io
    presrc = _io.open(os.path.join(HERE, "verify_r120-preR1.py"), "r").read()
    names = re.findall(r'chk\("([^"]+)"', presrc)
    cursrc = cur.decode("ascii")
    missing = [nm for nm in names if nm not in cursrc and nm != "T5c full star lift: L(Phi + s I) - L(Phi) = 0 exactly (quadratic Phi, linear A, numeric Theta)"]
    kept_t5c = "T5c full star lift: L(Phi + s I) - L(Phi) = 0 exactly (quadratic Phi, linear A, numeric Theta)" in cursrc
    print("pre-repair chk names: %d; missing (expected 0): %d; T5c claim string kept: %s"
          % (len(names), len(missing), kept_t5c))
    assert not missing and kept_t5c, "chk-name audit failed: %s" % missing
    print("CHAIN OK 120")
finally:
    shutil.rmtree(tmp, ignore_errors=True)
