#!/usr/bin/env python3
"""Byte-level anchor check for proposal 054, and optional application to a COPY of the tree.

usage: python -I apply_check.py <repo-root>              report anchors, EOLs and hashes, write nothing
       python -I apply_check.py <repo-root> --copy DIR   apply the edits inside DIR, a copy made by the caller;
                                                        refuses a second run, and refuses when DIR is the repository or lies inside it
E2 appends one pointer sentence to the closing paragraph of the 053 block (OLD -> NEW, exact bytes).
E1 inserts appH_insert.tex as its own paragraph before the Status paragraph of Problem E
(the anchor is the blank line before "\\paragraph{Status.}"+CRLF+"Remains Assumption~\\ref{ass:lorentzian}.", made unique by the blank line).
There are no bib additions in this package (all cited keys are already in bib/namcg.bib).
Pins of the accepted 053 working tree: appH 532576 B sha256 7a75554e..., bib 25976 B a651fe60...
The proposal-folder files are LF as written; normalise to LF before hashing and to CRLF before insertion.
"""
import sys, pathlib, re, hashlib
HERE=pathlib.Path(__file__).resolve().parent
OLD=(rb"or about non-polynomial observables such as \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\), "
     rb"which grow on \(\mathcal R_u\), so that the domination above fails for them.")
NEW=(OLD+rb" The next paragraph sharpens this at \(N=2\) and \(\gamma=0\): the failure occurs for every nonzero \(k\) "
     rb"in the contour class (B), and it is absent at fixed \(\gamma<0\).")
ANCHOR_STATUS=rb"\paragraph{Status.}"+b"\r\n"+rb"Remains Assumption~\ref{ass:lorentzian}."
ANCHOR_E1=b"\r\n\r\n"+ANCHOR_STATUS
CR,LF=b"\r",b"\n"
def lf(b): return b.replace(CR+LF,LF)
def crlf(b): return lf(b).replace(LF,CR+LF)
def show(name,b): print(f"{name}: size {len(b)} sha256 {hashlib.sha256(b).hexdigest()}")
def eol(name,b): print(f"{name}: size {len(b)} CRLF {b.count(CR+LF)} bare-LF {b.count(LF)-b.count(CR+LF)} CR {b.count(CR)} sha256 {hashlib.sha256(b).hexdigest()}")
def main():
    root=pathlib.Path(sys.argv[1])
    data=(root/'chapters/appH-microscopic-proofs.tex').read_bytes()
    print('PIN appH  size 532576 sha256 7a75554ef8cb7efe0e4c5cd3c53d6a9c4ffd2a9149e6ff29c7e8e067bb7f6aaa  matches:',
          len(data)==532576 and hashlib.sha256(data).hexdigest()=='7a75554ef8cb7efe0e4c5cd3c53d6a9c4ffd2a9149e6ff29c7e8e067bb7f6aaa')
    raw_bib=(root/'bib/namcg.bib').read_bytes()
    print('PIN bib   size 25976 sha256 a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b  matches:',
          len(raw_bib)==25976 and hashlib.sha256(raw_bib).hexdigest()=='a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b')
    print('E2 OLD occurrences:',data.count(OLD))
    print('E1 anchor (blank line + Status paragraph) occurrences:',data.count(ANCHOR_E1))
    print('bare Status anchor occurrences (context only):',data.count(ANCHOR_STATUS))
    ins=lf((HERE/'appH_insert.tex').read_bytes())
    print('insert ASCII:',all(c<128 for c in ins),'bare-LF after normalising:',ins.count(LF)-ins.count(CR+LF))
    show('insert, LF form',ins); show('insert, CRLF form',crlf(ins))
    show('E2 old',OLD); show('E2 new',NEW)
    eol('appH working file',data); eol('bib working file',raw_bib)
    bib=raw_bib.decode('utf-8'); tex=ins.decode()+NEW.decode()
    for k in sorted(set(re.findall(r'\\cite\{([^}]*)\}',tex))):
        for key in k.split(','):
            print(' cite',key,'in bib:',('{'+key+',') in bib)
    for lab in sorted(set(re.findall(r'\\(?:ref|eqref)\{([^}]*)\}',tex))):
        n=sum(p.read_text(encoding='utf-8').count(r'\label{'+lab+'}') for p in (root/'chapters').glob('*.tex'))
        print(' label',lab,'defined',n,'times')
    labs=re.findall(r'\\label\{([^}]*)\}',tex)
    print(' labels introduced by this package:',labs if labs else 'none')
    if '--copy' in sys.argv:
        d=pathlib.Path(sys.argv[sys.argv.index('--copy')+1]).resolve()
        r=root.resolve()
        if d==r or r in d.parents: sys.exit('refusing to write into the repository')
        f=d/'chapters/appH-microscopic-proofs.tex'; x=f.read_bytes()
        if b'Exponential observables \\(\\operatorname{Tr}\\mathrm e^{\\mathrm ik^\\mu A_\\mu}\\) at \\(N=2\\)' in x:
            sys.exit('already applied; refusing a second run')
        assert x.count(OLD)==1 and x.count(ANCHOR_E1)==1, 'anchor counts wrong in copy'
        x=x.replace(OLD,NEW)
        x=x.replace(ANCHOR_E1,CR+LF+CR+LF+crlf(ins)+CR+LF+CR+LF+ANCHOR_STATUS)
        f.write_bytes(x)
        print('applied to copy',d)
        eol('appH after',x)
        print('bare LF after application: appH',x.count(LF)-x.count(CR+LF))
        print('bib untouched; recheck pin:',hashlib.sha256((d/'bib/namcg.bib').read_bytes()).hexdigest()==
              'a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b')
main()
