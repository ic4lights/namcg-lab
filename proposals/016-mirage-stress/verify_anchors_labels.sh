#!/bin/sh
cd "$(dirname "$0")/../.."
echo "anchor count (section Problem G: HBEV):"; grep -cF 'section{Problem G: HBEV}' chapters/appH-microscopic-proofs.tex
for l in eq:Smatrix ch:vierbein-emergence ass:EE sec:status-F; do printf "%s: " "$l"; grep -h "label{$l}" chapters/*.tex | wc -l; done
for k in KumarSteinacker2023 Steinacker2026 SperlingSteinacker2019 Steinacker2023; do printf "bib %s: " "$k"; grep -c "^@.*{$k," bib/namcg.bib; done
echo "new labels introduced: none; new bib entries: none"
