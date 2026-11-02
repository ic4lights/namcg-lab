#!/usr/bin/env python3
"""Byte-level anchor check for proposal 053, and optional application to a COPY of the tree.

usage: python apply_check.py <repo-root>              report anchors only, write nothing
       python apply_check.py <repo-root> --copy DIR   apply both edits and the bib entries inside DIR, a copy made by the caller;
                                                      refuses a second run, and refuses when DIR is the repository itself
The edit E1 replaces one sentence pair of the 052 block; the edit E2 inserts appH_insert.tex before the Status paragraph of Problem E.
"""
import sys, pathlib, re
HERE=pathlib.Path(__file__).resolve().parent
OLD=(rb"That route is not asserted in that section, and it is not the route of a Lorentzian matrix integral with a convergence regulator, "
     rb"which is then no longer related to the Euclidean model by Wick rotation~\cite{Steinacker2026Invitation}; "
     rb"the reflection statement does not bear on that integral. Its hypotheses are the Euclidean contraction,")
NEW=(rb"That route is not asserted in that section. A Lorentzian matrix integral with a convergence regulator is a different starting point, "
     rb"and its relation to the Euclidean model is disputed. At finite \(N\), with the limit and the hypotheses recorded in Section~\ref{sec:status-E}, "
     rb"its polynomial moments of low degree are those of the Euclidean model up to phases, so the reflection statement is not excluded from bearing on it in that limit; "
     rb"for \(N\to\infty\) taken first, or for a fixed positive mass, no such relation is stated. The hypotheses of the reflection statement are the Euclidean contraction,")
ANCHOR=rb"\paragraph{Status.}"+b"\r\n"+rb"Remains Assumption~\ref{ass:lorentzian}."
def main():
    root=pathlib.Path(sys.argv[1])
    data=(root/'chapters/appH-microscopic-proofs.tex').read_bytes()
    print('E1 old sentence occurrences:',data.count(OLD))
    print('E2 anchor occurrences:',data.count(ANCHOR))
    ins=(HERE/'appH_insert.tex').read_bytes()
    print('insert ASCII:',all(c<128 for c in ins),'CR bytes:',ins.count(b'\r'),'size',len(ins))
    bib=(root/'bib/namcg.bib').read_bytes().decode('utf-8')
    tex=ins.decode()
    for k in sorted(set(re.findall(r'\\cite\{([^}]*)\}',tex)))+re.findall(r'\\cite\{([^}]*)\}',NEW.decode()):
        for key in k.split(','):
            add=(HERE/'bib_additions.bib').read_text()
            print(' cite',key,'in bib:',('{'+key+',') in bib,'in additions:',('{'+key+',') in add)
    for lab in sorted(set(re.findall(r'\\(?:ref|eqref)\{([^}]*)\}',tex+NEW.decode()))):
        n=sum(p.read_text(encoding='utf-8').count(r'\label{'+lab+'}') for p in (root/'chapters').glob('*.tex'))
        print(' label',lab,'defined',n,'times')
    if '--copy' in sys.argv:
        d=pathlib.Path(sys.argv[sys.argv.index('--copy')+1]).resolve()
        if d==root.resolve(): sys.exit('refusing to write into the repository')
        f=d/'chapters/appH-microscopic-proofs.tex'; x=f.read_bytes()
        if b'The regulated Lorentzian integral at finite' in x: sys.exit('already applied; refusing a second run')
        assert x.count(OLD)==1 and x.count(ANCHOR)==1
        x=x.replace(OLD,NEW)
        x=x.replace(ANCHOR,ins.replace(b'\n',b'\r\n')+ANCHOR)
        f.write_bytes(x)
        b=d/'bib/namcg.bib'; b.write_bytes(b.read_bytes()+b'\n'+(HERE/'bib_additions.bib').read_bytes())
        print('applied to copy',d)
main()
