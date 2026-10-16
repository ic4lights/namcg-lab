import re,os
d=os.path.dirname(os.path.abspath(__file__))
p=open(os.path.join(d,'proposal-r1.md'),encoding='utf8').read()
m=re.search(r'```latex\n(.*?)```',p,re.S); b=m.group(1)
def rep(s,a,c):
    assert s.count(a)==1,a; return s.replace(a,c)
b=rep(b,r"The closed forms give \(f_1=f_2\) for all \(\zeta\) exactly on",r"Conditional on the self-duality statement above, the closed forms give \(f_1=f_2\) for all \(\zeta\) exactly on")
b=rep(b,r"is a union of at most two lines unless \(F\) is (anti-)self-dual identically",r"is a linear subspace of the \(\zeta\)-plane (a line, or the whole plane only if \(F\) is (anti-)self-dual)")
b=rep(b,r"(Troost's levels \(2\pi(\sum_i(2m_i+1)f_i\pm2f_k)\), hep-th/9909187, eq.~(35), and the no-tachyon condition of its Section~9, \(f_1\le f_2+\dots+f_n\))",r"(the Landau levels of the same form, \(2\pi(\sum_i(2m_i+1)f_i\pm2f_k)\), of \cite{Troost2000}, eq.~(35), and the no-tachyon condition of its Section~9, \(f_1\le f_2+\dots+f_n\))")
b=rep(b,r"constant additional fluxes and bosonic content. It does",r"constant additional fluxes and bosonic content. The self-duality of \(Q^{-1/2}FQ^{-1/2}\) is verified numerically at sampled points and is not proved, so the classification of the set \(f_1=f_2\) is conditional on it. It does")
open(os.path.join(d,'block-r2.tex'),'w',encoding='utf8',newline='\n').write(b)
bib=r"""@article{Troost2000,
  author  = {Troost, Jan},
  title   = {Constant field strengths on {$T^{2n}$}},
  journal = {Nucl. Phys. B},
  volume  = {568},
  pages   = {180--194},
  year    = {2000},
  doi     = {10.1016/S0550-3213(99)00721-X},
  eprint  = {hep-th/9909187}
}"""
head=p.split('## Result')[0].replace('round 1','round 2')
new=head+"""## Changelog (r1 -> r2)
- Finding 1a: item (i) now begins "Conditional on the self-duality statement above, the closed forms give ...".
- Finding 1b: "a union of at most two lines" replaced by "a linear subspace of the zeta-plane (a line, or the whole plane only if F is (anti-)self-dual)".
- Finding 1c: final scope paragraph gains the sentence that self-duality of Q^{-1/2}FQ^{-1/2} is verified numerically at sampled points, is not proved, and that the classification of f1 = f2 is conditional on it.
- Finding 2: Troost phrased as "the Landau levels of the same form"; \cite{Troost2000} added with a BibTeX entry. DOI 10.1016/S0550-3213(99)00721-X verified via Crossref (title "Constant field strengths on T2n", author Jan Troost, Nuclear Physics B 568, pages 180-194, 2000-02). Verified by me this round: Crossref record only; the paper's content was verified by the gatekeeper in review-r1.
- Finding 3: left as is, per instruction.
- "Remaining open step" replaced by the review's ranked avenues (H2 first).
- Anchor re-verified: `\section{Problem G: HBEV}` occurs once (appH line 1982); the 018 paragraph ending "Problem~F remains open." immediately precedes it (checked by compile_check_r2.py). block-r2.tex equals the r2 block below (asserted in compile_check_r2.py).
- Unchanged from r1: Result, claims, scripts, no label change. Items 2 and 3 of the r1 Result list that say "exactly"/"holds exactly" refer to the closed forms and are to be read as conditional on the self-duality identification (see the block).

"""
body=p.split('## Result',1)[1]
body=rep(body,"Optional bibliography entry (arXiv record and journal data from the arXiv abstract page; DOI not independently verified), only if the integrator wants a citation:","Bibliography entry required by the block (DOI verified via Crossref):")
body=re.sub(r'```latex\n.*?```',lambda _:'```latex\n'+b+'```',body,count=1,flags=re.S)
body=re.sub(r'```bibtex\n.*?```',lambda _:'```bibtex\n'+bib+'\n```',body,count=1,flags=re.S)
body=rep(body,"The block (identical to block-r1.tex) uses no labels or citations; Troost's equations are named in words.","The block (identical to block-r2.tex) uses one citation key, Troost2000 (entry below; absent from bib/namcg.bib at present, no duplicate), and no labels.")
body=rep(body,"compile_check_r1.py / .out.txt: scratch-copy build","compile_check_r2.py / .out.txt (supersedes r1): scratch-copy build with bib entry and block-r2.tex; make_r2.py generates block-r2.tex from r1")
body=rep(body,"Re-check: chirality = sign(y^4), the codimension counts, the Troost section numbering, that no status label changes, and that the block equals block-r1.tex.","Re-check: chirality = sign(y^4), the codimension counts, the Troost section numbering, that no status label changes, and that the block equals block-r2.tex. The integrator must add the Troost2000 entry to bib/namcg.bib together with the block.")
i=body.index('## Remaining open step'); j=body.index('## Special instructions')
body=body[:i]+"""## Remaining open step
Ranked avenues (from review-r1; each relaxes a hypothesis; none completed here):
1. H2 (most favourable): the position-dependent ambient contraction Q^{-1}, for which f1 = f2 identically. Determine whether the matrix action, gauge fixing or regulator supplies the Q^{-1} contraction, i.e. the term (y_a D^a)^2/l^2 (the unit time-like vector of the background built from matrix data).
2. H4 with a finite fibre: truncation of l with transverse flux f3 >= 2 sup|Ln| zeta_max, giving a finite positive fibre sum (the R-b3 analogue).
3. SO(4,1)-covariant presentation X^A = M^{A5} (five horizontal fields; not computed).
4. R-f2: SUSY flux expansion of the Lorentzian one-loop action; compare its radius of convergence with |r|/|p|. V4 = -4(f1^2-f2^2)^2 vanishes on (anti-)self-dual flux, but no identification with Steinacker's dF is claimed: a lead, not an application.
5. H1: exact so(4,2) character analysis with Moyal terms.
6. Fermions help only on the codimension-4 locus; at f1 != f2 the Dirac-squared Landau levels are non-negative and cannot cancel a tachyon.

"""+body[j:]
open(os.path.join(d,'proposal-r2.md'),'w',encoding='utf8').write(new+'## Result'+body)
