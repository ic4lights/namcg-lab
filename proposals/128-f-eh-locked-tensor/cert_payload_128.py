# cert_payload_128.py - compile certificate for payload-P1.txt (item 128).
# Wraps the payload paragraph in a minimal amsmath article OUTSIDE the
# repository (tempfile.mkdtemp), runs pdflatex twice in that temp dir, records
# exit codes, error-line count, the "Output written" log line and a page count,
# then deletes the temp dir. Undefined-reference warnings are EXPECTED
# (standalone wrapper lacks the manuscript preamble) and are counted, not
# failed on; a hard error (rc != 0 or an "!" error line) fails the certificate.
# Usage: python -I proposals/128-f-eh-locked-tensor/cert_payload_128.py
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.getcwd()
PAY = os.path.join(ROOT, "proposals", "128-f-eh-locked-tensor", "payload-P1.txt")
OUT = os.path.join(ROOT, "proposals", "128-f-eh-locked-tensor", "out-cert-128.txt")

def main():
    body = open(PAY, "rb").read()
    tmp = tempfile.mkdtemp(prefix="cert128_")
    lines = []
    try:
        with open(os.path.join(tmp, "p.tex"), "wb") as f:
            f.write(b"\\documentclass{article}\n\\usepackage{amsmath}\n\\begin{document}\n")
            f.write(body)
            f.write(b"\\end{document}\n")
        rc_total = 0
        for i in range(2):
            r = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "p.tex"],
                cwd=tmp, capture_output=True, text=True)
            rc_total |= r.returncode
        log = open(os.path.join(tmp, "p.log"), "r", errors="replace").read()
        err = [l for l in log.splitlines() if l.startswith("!")]
        undef = log.count("LaTeX Warning: Reference")
        outw = [l for l in log.splitlines() if "Output written" in l]
        lines.append("CERT rc = %d" % rc_total)
        lines.append("ERR_LINES = %d %s" % (len(err), err[:2]))
        lines.append("OUTPUT = %s" % (outw[:1]))
        lines.append("UNDEF_REF_WARNINGS(expected) = %d" % undef)
        pdf = os.path.join(tmp, "p.pdf")
        lines.append("PDF_EXISTS = %s / %d bytes" % (os.path.exists(pdf),
                     os.path.getsize(pdf) if os.path.exists(pdf) else -1))
        verdict = "CERT PASS" if rc_total == 0 and not err else "CERT FAIL"
        lines.append(verdict)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    txt = "\r\n".join(lines) + "\r\n"
    open(OUT, "wb").write(txt.encode())
    print(txt)
    return 0 if verdict == "CERT PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
