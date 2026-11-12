#!/usr/bin/env python3
"""Byte-level anchor check for proposal 053, and optional application to a COPY of the tree.

usage: python apply_check.py <repo-root>              report anchors, EOLs and hashes, write nothing
       python apply_check.py <repo-root> --copy DIR   apply both edits and the bib entries inside DIR, a copy made by the caller;
                                                      refuses a second run, and refuses when DIR is the repository or lies inside it
The edit E1 replaces one sentence pair of the 052 block; the edit E2 inserts appH_insert.tex before the Status paragraph of Problem E.
Round 2: appH and the working bib/namcg.bib are CRLF, so the insert and the appended bib entries are written CRLF. The proposal-folder files are
LF as written, but core.autocrlf may turn them CRLF on a later checkout, so they are normalised to LF before hashing and to CRLF before insertion.
Round 3: OLD, NEW and ANCHOR are unchanged.  EXPECT records the input and output hashes for the baseline of 2026-11-05; --copy refuses
inputs that differ from them and reports whether the outputs match.
"""
import sys, pathlib, re, hashlib
HERE=pathlib.Path(__file__).resolve().parent
OLD=(rb"That route is not asserted in that section, and it is not the route of a Lorentzian matrix integral with a convergence regulator, "
     rb"which is then no longer related to the Euclidean model by Wick rotation~\cite{Steinacker2026Invitation}; "
     rb"the reflection statement does not bear on that integral. Its hypotheses are the Euclidean contraction,")
NEW=(rb"That route is not asserted in that section. A Lorentzian matrix integral with a convergence regulator is a different starting point, "
     rb"and its relation to the Euclidean model is disputed. At finite \(N\), in the limit and under the hypotheses recorded in Section~\ref{sec:status-E} (proved at \(N=2\), conditional for \(N\ge3\)), "
     rb"its polynomial moments of low degree are those of the Euclidean model up to phases, so the reflection statement is not excluded from bearing on it in that limit; "
     rb"for \(N\to\infty\) taken first, or for a fixed positive mass, no such relation is stated. The hypotheses of the reflection statement are the Euclidean contraction,")
ANCHOR=rb"\paragraph{Status.}"+b"\r\n"+rb"Remains Assumption~\ref{ass:lorentzian}."
CR,LF=b"\r",b"\n"
EXPECT={'insert_lf':(10766,'e5562f7670046d486f9855703190b04d78a08994aee9f661b124f930f6d15009'),
        'insert_crlf':(10783,'bab65e9595a2b2c2f7dad231e1427cfeae0de0ff0ac4e262b33dd8d95b504285'),
        'appH_in':(521477,'c0f9462fd2c6daf7e1b085250ea9f4bc7d45f605b93afc21857950bb796ba777'),
        'bib_in':(24258,'09ac48a5a1157723a766f1aa118081b1c3f5ec4c928158ba3d0c43a80a90a3aa'),
        'appH_out':(532576,'7a75554ef8cb7efe0e4c5cd3c53d6a9c4ffd2a9149e6ff29c7e8e067bb7f6aaa'),
        'bib_out':(25976,'a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b')}
def sz(b): return (len(b),hashlib.sha256(b).hexdigest())
def lf(b): return b.replace(CR+LF,LF)
def crlf(b): return lf(b).replace(LF,CR+LF)
def show(name,b): print(f"{name}: size {len(b)} sha256 {hashlib.sha256(b).hexdigest()}")
def eol(name,b): print(f"{name}: size {len(b)} CRLF {b.count(CR+LF)} LF {b.count(LF)} CR {b.count(CR)} sha256 {hashlib.sha256(b).hexdigest()}")
def main():
    root=pathlib.Path(sys.argv[1])
    data=(root/'chapters/appH-microscopic-proofs.tex').read_bytes()
    print('E1 old sentence occurrences:',data.count(OLD))
    print('E2 anchor occurrences:',data.count(ANCHOR))
    ins=lf((HERE/'appH_insert.tex').read_bytes())
    add_b=lf((HERE/'bib_additions.bib').read_bytes())
    print('insert ASCII:',all(c<128 for c in ins),'CR bytes after normalising:',ins.count(CR))
    show('insert, LF form',ins); show('insert, CRLF form',crlf(ins))
    show('E1 old',OLD); show('E1 new',NEW)
    show('bib additions, LF form',add_b); show('bib additions, CRLF form',crlf(add_b))
    raw_bib=(root/'bib/namcg.bib').read_bytes()
    eol('appH working file',data); eol('bib working file',raw_bib)
    print('expected: insert LF',sz(ins)==EXPECT['insert_lf'],'insert CRLF',sz(crlf(ins))==EXPECT['insert_crlf'],
          'appH input',sz(data)==EXPECT['appH_in'],'bib input',sz(raw_bib)==EXPECT['bib_in'])
    bib=raw_bib.decode('utf-8')
    tex=ins.decode()
    add=add_b.decode()
    for k in sorted(set(re.findall(r'\\cite\{([^}]*)\}',tex)))+re.findall(r'\\cite\{([^}]*)\}',NEW.decode()):
        for key in k.split(','):
            print(' cite',key,'in bib:',('{'+key+',') in bib,'in additions:',('{'+key+',') in add)
    for key in re.findall(r'@\w+\{([^,]*),',add):
        print(' new key',key,'already in bib:',('{'+key+',') in bib)
    for lab in sorted(set(re.findall(r'\\(?:ref|eqref)\{([^}]*)\}',tex+NEW.decode()))):
        n=sum(p.read_text(encoding='utf-8').count(r'\label{'+lab+'}') for p in (root/'chapters').glob('*.tex'))
        print(' label',lab,'defined',n,'times')
    if '--copy' in sys.argv:
        d=pathlib.Path(sys.argv[sys.argv.index('--copy')+1]).resolve()
        r=root.resolve()
        if d==r or r in d.parents: sys.exit('refusing to write into the repository')
        f=d/'chapters/appH-microscopic-proofs.tex'; x=f.read_bytes()
        if b'The regulated Lorentzian integral at finite' in x: sys.exit('already applied; refusing a second run')
        if sz(x)!=EXPECT['appH_in'] or sz(ins)!=EXPECT['insert_lf']: sys.exit('appH in the copy or the insert differs from EXPECT; nothing written')
        assert x.count(OLD)==1 and x.count(ANCHOR)==1
        x=x.replace(OLD,NEW)
        x=x.replace(ANCHOR,crlf(ins)+ANCHOR)
        f.write_bytes(x)
        b=d/'bib/namcg.bib'; y=b.read_bytes()
        if sz(y)!=EXPECT['bib_in']: sys.exit('bib in the copy differs from EXPECT; appH already written, bib not written')
        assert y.count(LF)==y.count(CR+LF) and y.endswith(CR+LF), 'bib in the copy is not fully CRLF'
        y=y+CR+LF+crlf(add_b)
        b.write_bytes(y)
        print('applied to copy',d)
        eol('appH after',x); eol('bib after',y)
        print('bare LF after application: appH',x.count(LF)-x.count(CR+LF),'bib',y.count(LF)-y.count(CR+LF))
        print('outputs equal EXPECT: appH',sz(x)==EXPECT['appH_out'],'bib',sz(y)==EXPECT['bib_out'])
main()
