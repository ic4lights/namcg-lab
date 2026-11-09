"""Byte-exact single-pass splice for proposal 060-rp-n2-invariant-failure.

CERTIFIED APPLY RULE (gatekeeper r2, single pass, ascending byte offsets on
the working-tree bytes of chapters/appH-microscopic-proofs.tex):

    out = src[:235613] + D_crlf + src[235613:269406] + E_crlf + src[269406:]

Pre-state (must match): 555396 B, 3269 CRLF, 0 bare LF,
  sha256 c39e90f5b3431f8197b8b759e83c95564456cf6191549c7838dd0517a473ca26
Applied inserts: D_crlf 467 B (stored LF form, trailing newline stripped,
  no CRLF conversion -- spliced mid-line), sha256 73c35e54...;
  E_crlf 4880 B (stored LF form, every LF -> CRLF, CR count 57),
  sha256 a3185144...
Post-state (must match): 560743 B, 3326 CRLF, 0 bare LF,
  sha256 fe02de8970b7dee8b0df8cad9a84ca557b1ecf41bc9d2b4984135a50b8faab8d

Run: python -I proposals/060-rp-n2-invariant-failure/apply_integration.py
from the repository root. Refuses to write unless every gate passes.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TARGET = os.path.join(ROOT, "chapters", "appH-microscopic-proofs.tex")
BACKUP = os.path.join(ROOT, "scratch", "integrator-backup",
                      "060-rp-n2-invariant-failure", "chapters",
                      "appH-microscopic-proofs.tex")
PROPDIR = os.path.join(ROOT, "proposals", "060-rp-n2-invariant-failure")

PRE_SHA = "c39e90f5b3431f8197b8b759e83c95564456cf6191549c7838dd0517a473ca26"
D_SHA = "73c35e54f36c94a9de1cc6c0135837cf58e078b2c07b7edc951e774b630f612e"
E_SHA = "a31851441bda9b415dea11d344fdddb9fbdae8945db327c9c4171c181a0e56ad"
POST_SHA = "fe02de8970b7dee8b0df8cad9a84ca557b1ecf41bc9d2b4984135a50b8faab8d"


def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    src = open(TARGET, "rb").read()
    if len(src) != 555396 or sha(src) != PRE_SHA:
        fail("pre-state mismatch: bytes=%d sha=%s" % (len(src), sha(src)))
    if src.count(b"\r\n") != 3269 or (src.count(b"\n") - src.count(b"\r\n")) != 0:
        fail("pre-state line-ending mismatch")

    D = open(os.path.join(PROPDIR, "insert-D.tex"), "rb").read()
    E = open(os.path.join(PROPDIR, "insert-E.tex"), "rb").read()
    D_crlf = D[:-1] if D.endswith(b"\n") else D          # trailing newline stripped, mid-line splice
    E_crlf = E.replace(b"\n", b"\r\n")                    # every LF -> CRLF
    if len(D_crlf) != 467 or sha(D_crlf) != D_SHA:
        fail("D applied-form mismatch: bytes=%d sha=%s" % (len(D_crlf), sha(D_crlf)))
    if len(E_crlf) != 4880 or E_crlf.count(b"\r") != 57 or sha(E_crlf) != E_SHA:
        fail("E applied-form mismatch: bytes=%d CR=%d sha=%s"
             % (len(E_crlf), E_crlf.count(b"\r"), sha(E_crlf)))

    # Anchor-context uniqueness on the pre-state (full contexts, each exactly once)
    dctx = src[235533:235613] + b" (ii) \\emph{Constraint.}"
    if src.count(dctx) != 1 or src.find(dctx) != 235533:
        fail("D anchor context not unique/at expected offset")
    ectx = (b"not of the contour family. Problem~E remains open and "
            b"PROGRAMME-CONDITIONAL.\r\n\r\n")
    if src.count(ectx) != 1 or src.find(ectx) + len(ectx) != 269406:
        fail("E anchor context not unique/end offset != 269406")

    out = src[:235613] + D_crlf + src[235613:269406] + E_crlf + src[269406:]

    if len(out) != 560743:
        fail("post byte count %d != 560743" % len(out))
    if out.count(b"\r\n") != 3326 or (out.count(b"\n") - out.count(b"\r\n")) != 0:
        fail("post line-ending counts wrong: CRLF=%d bareLF=%d"
             % (out.count(b"\r\n"), out.count(b"\n") - out.count(b"\r\n")))
    if sha(out) != POST_SHA:
        fail("post sha %s != %s -- NOT writing" % (sha(out), POST_SHA))

    # keep a verified copy of the pre-state bytes in the backup location
    os.makedirs(os.path.dirname(BACKUP), exist_ok=True)
    if not (os.path.exists(BACKUP) and sha(open(BACKUP, "rb").read()) == PRE_SHA):
        open(BACKUP, "wb").write(src)

    with open(TARGET, "wb") as f:
        f.write(out)

    # read back and re-verify
    chk = open(TARGET, "rb").read()
    if chk != out:
        fail("read-back mismatch")
    print("OK wrote %s" % TARGET)
    print("post bytes %d CRLF %d bareLF %d sha %s"
          % (len(chk), chk.count(b"\r\n"), chk.count(b"\n") - chk.count(b"\r\n"), sha(chk)))
    print("D junction:", chk[235613 - 40:235613], "||",
          D_crlf[:40], "||", chk[235613 + len(D_crlf):235613 + len(D_crlf) + 40])
    e_start = 269406
    e_end = e_start + len(E_crlf)
    print("E before:", chk[e_start - 40:e_start])
    print("E head:", E_crlf[:60])
    print("E tail:", E_crlf[-60:])
    print("E after:", chk[e_end:e_end + 60])
    print("Remains Assumption count post:", chk.count(b"Remains Assumption"))


if __name__ == "__main__":
    main()
