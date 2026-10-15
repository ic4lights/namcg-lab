#!/bin/sh
# run from the repository root:  sh proposals/017-GT-GA-gap/verify_anchors_labels.sh
cd "$(dirname "$0")/../.." || exit 1
echo "anchor 'the off-shell quadratic form is gauge dependent' in appH (expect 1):"
grep -c "the off-shell quadratic form is gauge dependent" chapters/appH-microscopic-proofs.tex
echo "anchor '\section{Problem C: conformal mode and Cassini}' in appH (expect 1):"
grep -c 'section{Problem C: conformal mode and Cassini}' chapters/appH-microscopic-proofs.tex
for l in sec:status-F sec:status-B sec:status-A ass:emergent-op thm:Geff ass:EE thm:mT rem:ch3-trace-quadratic eq:O-eta eq:Geff-structure eq:W-expand; do
  printf "label %s defined %s time(s)\n" "$l" "$(grep -o "\\label{$l}" chapters/*.tex | wc -l)"
done
echo "bib keys:"; grep -c "^@article{Solodukhin2011," bib/namcg.bib; grep -c "^@article{IKKT1997," bib/namcg.bib; grep -c "^@article{Steinacker2023," bib/namcg.bib
echo "macros:"; grep -c 'newcommand{.LUV}' namcg-book7.tex
echo "new labels introduced by 017: none"
