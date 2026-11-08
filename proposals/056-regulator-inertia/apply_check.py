#!/usr/bin/env python3
"""Report-mode check of the 056 insertion.  Reads chapters/appH-microscopic-proofs.tex and appH_insert.tex,
verifies the baseline hash, the anchor's uniqueness and the insert's form (ASCII, LF only, no trailing
whitespace), and, given an output path OUTSIDE the repository, writes the would-be appH there (CRLF insert
placed immediately before the anchor, followed by one blank line).  It never writes inside the repository and
refuses to overwrite an existing file.
Usage: python apply_check.py [OUTPUT_PATH]
"""
import sys, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
APPH = os.path.join(ROOT, 'chapters', 'appH-microscopic-proofs.tex')
INS = os.path.join(HERE, 'appH_insert.tex')
BASE_LEN = 550508
BASE_SHA = '01a3bf55a888ea30f4f3182358877b4ba6db5ac6237f2b7fff7e06093277d7a9'
CR = bytes([13]); LF = bytes([10]); CRLF = CR+LF
ANCHOR = b'\\paragraph{Status.}'+CRLF+b'Remains Assumption~\\ref{ass:lorentzian}.'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def counts(b):
    return b.count(CRLF), b.count(LF)-b.count(CRLF)

def main():
    a = open(APPH, 'rb').read()
    ins = open(INS, 'rb').read()
    print("appH:", len(a), "bytes sha256", sha(a), " CRLF, bare LF:", counts(a))
    ok = (len(a) == BASE_LEN and sha(a) == BASE_SHA)
    print("baseline matches expected:", ok)
    if not ok:
        sys.exit("baseline differs; stop")
    print("anchor:", len(ANCHOR), "bytes sha256", sha(ANCHOR), " count", a.count(ANCHOR),
          " line", a[:a.find(ANCHOR)].count(LF)+1)
    if a.count(ANCHOR) != 1:
        sys.exit("anchor not unique; stop")
    assert all(c < 128 for c in ins), "insert not ASCII"
    assert CR not in ins, "insert has CR"
    assert ins.endswith(LF), "insert must end with LF"
    assert all(l == l.rstrip(b' \t') for l in ins.split(LF)), "trailing whitespace"
    crlf = ins.replace(LF, CRLF)
    print("insert LF:", len(ins), "bytes sha256", sha(ins), "; CRLF form:", len(crlf), "bytes sha256", sha(crlf))
    if a.count(crlf[:200]) != 0:
        sys.exit("insert already present; stop")
    i = a.find(ANCHOR)
    new = a[:i]+crlf+CRLF+a[i:]
    print("result:", len(new), "bytes sha256", sha(new), " CRLF, bare LF:", counts(new))
    if len(sys.argv) > 1:
        out = os.path.abspath(sys.argv[1])
        if out.lower().startswith(ROOT.lower()):
            sys.exit("output inside the repository; refusing")
        if os.path.exists(out):
            sys.exit("output exists; refusing to overwrite")
        open(out, 'wb').write(new)
        print("wrote", out)

if __name__ == "__main__":
    main()
