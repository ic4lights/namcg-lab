"""s5_insert_mechanics.py (proposal 046): byte-level and reference checks of appH_insert.tex against the
current working tree (anchor uniqueness, labels referenced exist exactly once, bib keys exist, no new labels,
no title collision)."""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(os.path.join(here, '..', '..'))
b = open(os.path.join(here, 'appH_insert.tex'), 'rb').read()
s = b.decode('utf-8')
out = []
def P(x): print(x); out.append(x)
ncr, ntab = b.count(bytes([13])), b.count(bytes([9]))
P(f"bytes {len(b)}; non-ASCII {sum(c > 127 for c in b)}; CR {ncr}; TAB {ntab}")
P(f"brace balance {s.count('{') - s.count('}')}; \\( - \\) {s.count(chr(92)+'(') - s.count(chr(92)+')')}; \\[ - \\] {s.count(chr(92)+'[') - s.count(chr(92)+']')}")
P(f"\\label in insert: {s.count(chr(92)+'label')}; \\paragraph count: {s.count(chr(92)+'paragraph')}")
refs = sorted(set(re.findall(r'\\(?:ref|eqref)\{([^}]*)\}', s)))
cites = sorted(set(k.strip() for grp in re.findall(r'\\cite\{([^}]*)\}', s) for k in grp.split(',')))
chap = os.path.join(repo, 'chapters')
alltex = ''.join(open(os.path.join(chap, f), encoding='utf-8').read() for f in sorted(os.listdir(chap)) if f.endswith('.tex'))
for r in refs:
    P(f"ref {r}: label occurrences in chapters = {alltex.count(chr(92)+'label{'+r+'}')}")
bib = open(os.path.join(repo, 'bib', 'namcg.bib'), encoding='utf-8').read()
for c in cites:
    nb = len(re.findall(r'@\w+\{' + re.escape(c) + r',', bib))
    P(f"cite {c}: bib entries = {nb}")
appH = open(os.path.join(chap, 'appH-microscopic-proofs.tex'), encoding='utf-8').read()
anchor = '\\section{Problem G: HBEV}'
P(f"anchor '{anchor}' occurrences in appH: {appH.count(anchor)}")
title = 'fibre spectrum, proper-time interpolation between the two readings'
P(f"title fragment '{title}' occurrences in appH: {appH.count(title)}")
P("process-language scan: " + str([w for w in ('proposal', 'researcher', 'gatekeeper', 'as proposed', 'this package', 'we ', 'routine', 'script') if w in s.lower()]))
open(os.path.join(here, 's5_insert_mechanics.out.txt'), 'w', newline='\n').write('\n'.join(out) + '\n')
# anchor context: the line before the anchor must be the closing sentence of the product-background paragraph
i = appH.index(anchor)
prev = appH[:i].rstrip().splitlines()[-1]
P("line before anchor ends with: " + prev[-60:])
P("macros used: " + str(sorted(set(re.findall(chr(92)*2 + "([A-Za-z]+)", s)))))
open(os.path.join(here, 's5_insert_mechanics.out.txt'), 'w', newline='\n').write('\n'.join(out) + '\n')
q = 'The full trace approaches them when the fibre gaps exceed the scale of \(K\)'
P("045 sentence corrected by the insert, occurrences in appH: " + str(appH.count(q)))
open(os.path.join(here, 's5_insert_mechanics.out.txt'), 'w', newline='\n').write('\n'.join(out) + '\n')
