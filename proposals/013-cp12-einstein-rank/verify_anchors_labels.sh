#!/bin/bash
# Run from repository root: bash proposals/013-cp12-einstein-rank/verify_anchors_labels.sh
cd "$(git rev-parse --show-toplevel)"
f=chapters/appH-microscopic-proofs.tex
echo "anchor \section{Problem G: HBEV}: $(grep -c 'section{Problem G: HBEV}' $f) occurrence(s), line $(grep -n 'section{Problem G: HBEV}' $f | cut -d: -f1)"
echo "last sentence of the 011 torsion paragraph (line 1855) ends with: $(sed -n 1855p $f | tr -d '\r' | grep -o 'This changes no ledger label; Problem~F remains open\.$')"
echo "'Connection-sector term' paragraph heading count: $(grep -c 'Connection-sector term' $f)"
for l in rem:ch3-trace-quadratic def:matrix-coords-ext ch:vierbein-emergence ass:emergent-op ass:EE; do
  echo "label $l defined $(grep -h "label{$l}" chapters/*.tex | wc -l) time(s)"
done
for k in MantaSteinacker2025 Steinacker2016Gravity Steinacker2019NoGhost SperlingSteinacker2019; do
  echo "bib key $k present in bib/namcg.bib: $(grep -c "{$k," bib/namcg.bib)"
done
echo "new labels introduced by the proposal: none"
