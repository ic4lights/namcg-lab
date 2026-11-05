"""s6_insert_mechanics.py (proposal 047): byte-level and reference checks of appH_insert.tex against the current working
tree. Prints to stdout only; writes nothing."""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
repo = os.path.abspath(os.path.join(here, '..', '..'))
b = open(os.path.join(here, 'appH_insert.tex'), 'rb').read()
s = b.decode('utf-8')
print(f"bytes {len(b)}; non-ASCII {sum(c > 127 for c in b)}; CR {b.count(bytes([13]))}; TAB {b.count(bytes([9]))}")
print(f"brace balance {s.count('{') - s.count('}')}; \\( - \\) {s.count(chr(92)+'(') - s.count(chr(92)+')')}; \\[ - \\] {s.count(chr(92)+'[') - s.count(chr(92)+']')}")
print(f"\\label in insert: {s.count(chr(92)+'label')}; \\paragraph count: {s.count(chr(92)+'paragraph')}; status closing count: {s.count('remain open and PROGRAMME-CONDITIONAL')}")
refs = sorted(set(re.findall(r'\\(?:ref|eqref)\{([^}]*)\}', s)))
cites = sorted(set(k.strip() for grp in re.findall(r'\\cite\{([^}]*)\}', s) for k in grp.split(',')))
chap = os.path.join(repo, 'chapters')
alltex = ''.join(open(os.path.join(chap, f), encoding='utf-8').read() for f in sorted(os.listdir(chap)) if f.endswith('.tex'))
for r in refs:
    print(f"ref {r}: label occurrences in chapters = {alltex.count(chr(92)+'label{'+r+'}')}")
bib = open(os.path.join(repo, 'bib', 'namcg.bib'), encoding='utf-8').read()
for c in cites:
    print(f"cite {c}: bib entries = {len(re.findall(r'@[A-Za-z]+[{]' + re.escape(c) + r',', bib))}")
appH = open(os.path.join(chap, 'appH-microscopic-proofs.tex'), encoding='utf-8').read()
anchor = '\\section{Problem G: HBEV}'
print(f"anchor occurrences in appH: {appH.count(anchor)}, in all chapters: {alltex.count(anchor)}")
title = 'closed forms of the level-one forms'
print(f"title fragment occurrences in appH: {appH.count(title)}")
print("macro \\mathcal S_4 in appH:", appH.count('\\mathcal S_4'), "; \\mathcal Z_{ab} in appH:", appH.count('\\mathcal Z_{ab}'))
print("process-language scan:", [w for w in ('proposal', 'researcher', 'gatekeeper', 'as proposed', 'this package', ' we ', 'routine', 'script') if w in s.lower()])
i = appH.index(anchor)
print("line before anchor ends with:", appH[:i].rstrip().splitlines()[-1][-70:])
