# 071-j-ecg-passage-sync: read-only integration simulator (no files are written).
# Applies the two byte-exact OLD->NEW replacements in memory, one per file
# (chapters/ch17-agenda.tex E1, chapters/ch09-ultraviolet.tex E2), asserts each
# anchor occurs exactly once, and prints PRE/POST byte counts, sha256, CRLF and
# bare-LF counts for both files. Re-run from the repo root:
#   python -I proposals/071-j-ecg-passage-sync/simulate_apply.py
# Expected invariant outputs are quoted in proposal-r1.md ("Verification scripts").
import hashlib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def stat(name, b):
    print("%s: bytes %d sha256 %s CRLF %d bareLF %d"
          % (name, len(b), hashlib.sha256(b).hexdigest(),
             b.count(b"\r\n"), b.count(b"\n") - b.count(b"\r\n")))


# ---------------- E1: chapters/ch17-agenda.tex ----------------
CH17 = os.path.join(ROOT, "chapters", "ch17-agenda.tex")

CH17_OLD = (
    b"the action~\\eqref{eq:S-ECG}, Section~\\ref{sec:status-J} records\r\n"
    b"checked reduced Euler--Lagrange\r\n"
    b"identities, the resulting first integral including"
)

CH17_NEW = (
    b"the action~\\eqref{eq:S-ECG}, Section~\\ref{sec:status-J} records the\r\n"
    b"reduced Euler--Lagrange identities together with the audit finding\r\n"
    b"that, under the literal bivector-map index reading of \\eqref{eq:ECG},\r\n"
    b"a symbolic re-evaluation of the same reduced action does not\r\n"
    b"reproduce them; the section also records the resulting first integral\r\n"
    b"of that displayed one-dimensional system, including"
)

# ---------------- E2: chapters/ch09-ultraviolet.tex ----------------
CH09 = os.path.join(ROOT, "chapters", "ch09-ultraviolet.tex")

CH09_OLD = (
    b"  \\item For the reduced action in Section~\\ref{sec:status-J}, the\r\n"
    b"        Euler--Lagrange equations have been checked symbolically:\r\n"
    b"        \\(N=1\\) is a consistent vacuum branch and the lapse equation\r\n"
    b"        yields the displayed first integral, including\r\n"
    b"        \\(\\Lambda_{\\mathrm{eff}}\\). This check uses the static\r\n"
    b"        spherical reduction;"
)

CH09_NEW = (
    b"  \\item For the reduced action in Section~\\ref{sec:status-J}, a\r\n"
    b"        symbolic re-evaluation under the literal bivector-map index\r\n"
    b"        reading of \\eqref{eq:ECG} does not reproduce the recorded\r\n"
    b"        Euler--Lagrange identities: on that reading \\(N=1\\) is not\r\n"
    b"        an exact consistent truncation for a general profile, while\r\n"
    b"        the displayed one-dimensional system has the recorded first\r\n"
    b"        integral, including\r\n"
    b"        \\(\\Lambda_{\\mathrm{eff}}\\), internally consistent. This reduction uses\r\n"
    b"        the static spherical ansatz;"
)

# sanity: the untouched continuations must survive byte-identically
CH17_KEEP_AFTER = (b"\r\n\\(\\Lambda_{\\mathrm{eff}}\\), its conditional "
                   b"regular-centre constraint\r\n")
CH09_KEEP_AFTER = (b" its relation to the unrestricted field\r\n")

ok = True
total_delta = 0
for name, old, new, keep in [
        (CH17, CH17_OLD, CH17_NEW, CH17_KEEP_AFTER),
        (CH09, CH09_OLD, CH09_NEW, CH09_KEEP_AFTER)]:
    b = open(name, "rb").read()
    print("PRE  ", os.path.relpath(name, ROOT))
    stat("PRE  ", b)
    n = b.count(old)
    print("anchor count:", n, "(must be 1)")
    if n != 1:
        ok = False
        continue
    nb = b.replace(old, new, 1)
    if nb.count(keep) != b.count(keep):
        print("KEEP-AFTER count changed:", b.count(keep), "->", nb.count(keep))
        ok = False
    print("POST ", os.path.relpath(name, ROOT))
    stat("POST ", nb)
    total_delta += len(new) - len(old)
    if new.count(b"\r\n") != len(new.split(b"\r\n")) - 1:
        print("internal CRLF consistency failed")
        ok = False

print("total byte delta:", total_delta)
print("SIMULATION", "OK" if ok else "FAILED")
sys.exit(0 if ok else 1)
