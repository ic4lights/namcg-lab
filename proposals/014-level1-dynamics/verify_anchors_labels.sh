#!/bin/sh
cd "$(dirname "$0")/../.."
echo "anchor count (section Problem G: HBEV):"; grep -cF 'section{Problem G: HBEV}' chapters/appH-microscopic-proofs.tex
grep -nF 'section{Problem G: HBEV}' chapters/appH-microscopic-proofs.tex
for l in eq:Smatrix rem:ch3-trace-quadratic def:matrix-coords-ext ass:emergent-op ass:EE ch:vierbein-emergence; do
  printf "%s: " "$l"; grep -h "label{$l}" chapters/*.tex | wc -l
done
for k in SperlingSteinacker2019 MantaSteinacker2025 Steinacker2019NoGhost Steinacker2023 Steinacker2016Gravity; do
  printf "bib %s: " "$k"; grep -c "^@.*{$k," bib/namcg.bib
done
echo "new labels introduced by the proposal: none"
